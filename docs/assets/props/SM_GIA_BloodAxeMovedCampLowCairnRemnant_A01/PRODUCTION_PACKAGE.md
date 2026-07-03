# SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- Asset type: Static Mesh prop production package, docs-only
- Task: `AET-MA-20260629-316`
- Parent kit: `KIT_GIA_BloodAxeMovedCampCairnLine_A01`
- Parent child row: `BloodAxeRitualStones_A01#MovedCamp_LowCairnRemnant_A01`
- Related packages: `KIT_GIA_BloodAxeMovedCampCairnLine_A01`, `KIT_GIA_BloodAxeCairnGuideposts_A01`, `KIT_GIA_BloodAxePathMarkers_A01`, and `SM_GIA_BloodAxeRitualCairnGuidepost_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package for a single static dressing prop

`SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` defines one low remnant from a former Blood Axe cairn left after a Giant raider camp moved on. It should read as a collapsed, half-buried memory of a crude cairn: a few large rough stones, cold ash, trampled mud, and one restrained aged Blood Axe material beat.

The asset is static environmental dressing only. It must not become a route marker, waypoint, breadcrumb, tracking clue, pickup, loot object, salvage object, interaction prop, spawn marker, patrol marker, encounter lane, objective marker, or first implementation target.

Blood Axe visual language must remain separate from neutral/civilized Giant culture. Use hostile raider residue: rough highland stone, soot, ash, mud, faded oxide red cloth or paint, rawhide, rope, and sparse old horn, bone, or blackened iron only if needed. Do not use refined blue-gray cave-town masonry, terrace or waterwork motifs, warm hearth settlement language, peaceful highland markers, restrained blue runes, civic carving, or neutral Giant craft identity as the default read.

This package explicitly blocks collision correctness, pickup behavior, implementation target selection, DCC work, FBX export, Unreal work, startup placement, final approval, gameplay behavior, source concept movement, Hermes work, global docs edits, runtime source, validators, material instances, texture assets, and source folder creation.

## Gameplay Purpose

The gameplay purpose is environmental storytelling only. The prop suggests that a Blood Axe camp once occupied or crossed the area, then moved on and left a single collapsed cairn remnant behind.

Allowed planning uses:

- Add one small Blood Axe moved-camp memory beat to highland ground dressing, camp outskirts, ritual-stone surroundings, or cave approach residue.
- Support the interrupted cairn-line kit without creating a readable path or route.
- Give future artists clear scale, silhouette, material, LOD, and naming guidance for a single static prop.
- Preserve the validated Giant scale lock while keeping the remnant low compared with Giant baselines.

Out of scope:

- Collision correctness, pickup behavior, loot behavior, salvage behavior, resource behavior, crafting behavior, implementation target selection, DCC, FBX, Unreal asset creation, startup placement, final visual approval, final camp-route approval, gameplay behavior, waypoint behavior, breadcrumb behavior, tracking mechanics, UI path logic, objective logic, navigation/pathfinding, route validation, encounter scripting, spawn logic, patrol logic, AI behavior, interaction prompts, VFX, audio, destructible behavior, physics behavior, source concept movement, Hermes work, runtime source, validators, global docs edits, source folders, material instances, or texture assets.

## Silhouette Notes

- Primary read: one low, collapsed cairn remnant made from a few large Giant-placed stones, wider than tall, with an uneven broken crown.
- Height read: 60-180 cm tall. The lower end should feel half-sunk or scattered; the upper end may read as a partly intact low stack, but never as a maintained guidepost.
- Footprint read: broad and grounded, with stones partially embedded into cold ash, mud, and trampled earth.
- Stone count: 3-7 main stones, with one dominant base stone and a few shifted support stones. Avoid dense pebble piles.
- Faction beat: one restrained oxide red cloth scrap, dirty red paint smear, rawhide tie, or small blackened accent may remain, but it must feel old and non-signal-like.
- Collapse read: offset stones, buried edges, ash-dark contacts, and mud buildup should imply abandonment without physics, destruction states, or scripted collapse.
- Camera read: the asset should remain readable from a normal MMO gameplay camera as a single low Blood Axe remnant, not as a trail arrow, objective ring, standing marker, or loot pile.

Model real geometry in future approved work only for the major stone masses, broad broken planes, large contact bevels, fixed cloth/lashing silhouette if present, and low ground base. Reserve fine cracks, chips, soot speckles, ash flecks, mud streaks, lichen, cloth weave, fray, rope fibers, chipped paint, and small scratches for texture, normal, AO, or mask detail.

Avoid readable text, glyphs, arrows, UI-like shapes, fresh banners, signal flags, glowing runes, trophy clutter, graphic gore, polished civic forms, warm neutral Giant settlement motifs, and repeated guidepost spacing.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- These Giant baselines must not be changed by this package.

Visual planning dimensions:

- Overall remnant height: 60-180 cm.
- Preferred common height: 80-140 cm so the asset reads as a low remnant rather than an active cairn guidepost.
- Footprint: 120-320 cm wide by 90-260 cm deep, including ash and mud grounding.
- Dominant base stone: 70-180 cm across the broad face, sized for Giant-built readability.
- Secondary stones: 45-130 cm across, broad and chunky rather than pebble-like.
- Optional cloth scrap or tie: 35-120 cm long and 12-40 cm wide, fixed low or trapped under stone.
- Ash/mud grounding: 140-360 cm footprint, very low height, visual residue only.

At 60-180 cm tall, the remnant sits far below the 442 cm female and 470 cm male Giant baselines. It should read as knee-low to thigh-low for Giants depending on the variant, while still feeling oversized to normal humanoids.

These dimensions are visual planning values only. They are not traversal metrics, route metrics, navigation values, collision correctness, spawn/patrol distances, objective-marker ranges, interaction reach, pickup reach, camera approval metrics, implementation targets, or runtime validation values.

## Materials and Color Palette

Primary materials:

- Rough highland stone, fractured field rock, ash-stained cairn slabs, and dark weathered granite.
- Cold ash, charcoal dust, soot-dark contact marks, trampled mud, packed earth, and sparse burned grass residue.
- Faded oxide red cloth, dirty maroon strip, chipped red paint smear, or sun-weathered Blood Axe marking used in one restrained beat.
- Rawhide, rough rope, sinew, scorched leather, or hide cord only as small support language.
- Sparse blackened iron, old horn, or dull bone as optional non-graphic accents only.

Palette targets:

- Dark stone and soot: `#17191A`, `#252728`, `#3C3D3A`, `#575650`
- Ash and worn stone: `#68645C`, `#878075`, `#A69D8E`
- Mud and packed earth: `#261D17`, `#3C2E23`, `#5A4432`
- Faded Blood Axe red: `#4F1210`, `#651814`, `#7B251C`, `#8B4A38`
- Rope, hide, and leather: `#554129`, `#705538`, `#947348`
- Optional horn, bone, and scrap: `#776B55`, `#9A8661`, `#B39B70`, `#202426`

No default emissive is approved. Do not add ritual glow, shamanic glow, signal glow, torch state, animated material state, UI highlight, gameplay-readable color state, or blue rune language. Any active, glowing, ritual, signal, or gameplay-readable variant requires a separate approved package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG static prop concept sheet of `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` for the world of Aerathea. The design should emphasize a single low remnant from a former Blood Axe Giant cairn, 60-180 cm tall, a few large collapsed rough stones, broad Giant-scale massing, cold ash, trampled mud, soot-dark contact marks, one restrained faded oxide red cloth scrap or dirty red paint beat, rawhide or rope residue, hostile Giant raider sub-faction identity, strict separation from neutral/civilized Giant culture, abandoned moved-camp mood, and the gameplay role of static environmental storytelling only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh prop production sheet with front, side, top-down footprint, material swatches, LOD and collision guardrail notes, and scale markers beside female 442 cm and male 470 cm Giant baselines on a clean background. Avoid copying any existing franchise, avoid route arrows, avoid waypoint chains, avoid breadcrumb symbols, avoid tracking UI, avoid pickup or loot reads, avoid interaction prompts, avoid objective markers, avoid navigation diagrams, avoid spawn or patrol reads, avoid DCC claims, avoid FBX claims, avoid Unreal implementation claims, avoid startup placement, avoid final approval language, avoid source concept movement, avoid Hermes work, avoid neutral Giant civic materials as Blood Axe defaults, avoid graphic gore, and avoid excessive micro-detail that would not translate to a mid-poly game asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, Blender file, sculpt, mesh, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal asset, material instance, texture asset, material graph, validator, runtime source, Blueprint, socket, animation asset, startup placement, implementation target, source concept movement, Hermes work, final visual approval, or final camp-route approval is created or authorized.

Future modeling guidance only if a later approved task promotes the asset:

- Build one compact static prop composition with a ground-centered footprint and strong front/three-quarter readability.
- Use 3-7 large stones. Keep the shapes chunky, uneven, and hand-placed, not pebble-dense.
- Make the remnant wider than tall with the largest stone half-buried or mud-sunk.
- Offset the upper stones so the former cairn reads collapsed and old, but keep the silhouette physically plausible.
- Use cold ash and mud as a low grounding form or texture-led base, not as a route line, objective circle, or tracking mark.
- Keep optional cloth, rawhide, rope, iron, horn, or bone accents sparse and subordinate to the stone mass.
- Treat the Blood Axe color beat as weathered residue, not an active signal or banner.
- If future source is approved, place the pivot at ground center under the remnant footprint and orient the strongest read toward +X unless a later export convention says otherwise.

Suggested future mesh groups, planning only:

- `LowCairnRemnant_StoneMasses`
- `LowCairnRemnant_AshMudBase`
- `LowCairnRemnant_ClothOrPaintAccent`
- `LowCairnRemnant_RawhideRopeOptional`
- `LowCairnRemnant_AccentOptional`

Do not add sockets, marker locators, route helpers, navigation helpers, spawn helpers, patrol helpers, VFX locators, audio locators, pickup affordances, interaction prompts, objective volumes, trigger volumes, damage volumes, aura volumes, gameplay collision, destructible states, physics setup, or implementation-specific files.

## Texture and Material Notes

Target material strategy for possible future source work:

- Default material count: 1 shared Blood Axe cairn/remnant material.
- Maximum material count: 2 only if a later art pass separates stone/base from cloth/hide accents.
- Default texture resolution: 1K BC/N/ORM for repeated static dressing.
- 512 can be acceptable for distant repeated dressing if atlas reuse is prioritized.
- 2K is acceptable only if a separate later task promotes the prop to close-view focal dressing.
- No default emissive map.

Future texture names if a unique texture set is separately approved:

- `T_GIA_BloodAxeMovedCampLowCairnRemnant_A01_BC`
- `T_GIA_BloodAxeMovedCampLowCairnRemnant_A01_N`
- `T_GIA_BloodAxeMovedCampLowCairnRemnant_A01_ORM`

`T_GIA_BloodAxeMovedCampLowCairnRemnant_A01_E` must not be created for the baseline asset. Emissive, active ritual, signal, torch, magic, VFX, or UI-readable states are outside this package.

Texture guidance:

- Base Color should carry broad stone value changes, soot staining, cold ash, mud buildup, faded Blood Axe red, rawhide/rope warmth, and optional muted horn, bone, or scrap tones.
- Normal should carry fine cracks, chipped stone edges, cloth weave, fray, rope fibers, lichen specks, mud ridges, shallow pitting, and small scratches.
- ORM should emphasize occlusion under stone contacts, buried edges, cloth overlaps, ash pockets, mud recesses, and underside creases.
- Roughness should stay high across stone, ash, mud, cloth, hide, rope, horn, bone, and old blackened iron.
- Metallic should remain near zero except for rare blackened iron scraps.

Avoid unique materials for each stone, chip, crack, ash patch, mud smear, cloth strip, rope tie, lichen spot, paint mark, horn token, bone token, or scrap.

## Triangle Budget

- Target category: small static prop, Giant-scaled environmental dressing.
- LOD0 target: 700-3k tris total.
- LOD0 hard upper limit: 4k tris only if a later approved focal variant adds a broader ash/mud base and fixed cloth/lashing silhouette.
- LOD1 target: 350-1.5k tris.
- LOD2 target: 150-650 tris.
- LOD3 target: 60-220 tris.
- Material budget: 1 material target, 2 maximum.
- Texture budget: 1K BC/N/ORM by default; no baseline emissive texture.

Spend geometry on the few large stone silhouettes, broad broken planes, contact forms, blunt crown, grounded base, major chips, and optional broad cloth/lashing outline. Do not spend geometry on tiny cracks, pebble scatter, dense scratches, soot speckles, ash flecks, cloth weave, rope fibers, chipped paint, lichen, mud flecks, repeated tokens, or hidden underside detail.

The triangle budget is a future planning range only. It does not authorize DCC work, FBX export, Unreal import, implementation target selection, runtime validation, collision correctness, or final approval.

## LOD Plan

All future important static meshes require LOD0, LOD1, LOD2, and LOD3 before any separately approved shipping use.

- LOD0: full low remnant silhouette, 3-7 large stones, broad chipped planes, embedded base, cold ash/mud footprint, optional restrained cloth or paint beat, and any major lashing or old accent.
- LOD1: 55-70 percent of LOD0; reduce secondary bevels, small chips, underside cuts, cloth edge cuts, lashing subdivisions, minor mud forms, and hidden backside detail while preserving the low remnant read.
- LOD2: 30-45 percent of LOD0; simplify stones into larger planes, merge small base forms, flatten cloth folds, remove non-silhouette accent geometry, and retain one controlled Blood Axe color beat if present.
- LOD3: 10-25 percent of LOD0; preserve the low wide mound shape, broad base footprint, dominant stone mass, and one faded red accent only if needed for faction read.

Reduction order:

1. Tiny cracks, soot speckles, ash flecks, lichen specks, chipped paint edges, cloth weave, rope fibers, fray, and minor scratches.
2. Small lashing cuts, little knots, secondary cloth tears, tiny wedges, small iron nicks, and non-silhouette tokens.
3. Back-facing accent pieces, hidden underside bevels, buried base cuts, and non-visible mud undercuts.
4. Duplicate support stones, minor cloth holes, secondary chipped planes, and optional accent geometry.
5. Stone bevel density, cloth fold geometry, and minor base-plane subdivisions.
6. Only after small detail is removed, simplify the primary low cairn remnant silhouette.

Never reduce Giant-scale readability, the abandoned moved-camp memory, the low collapsed footprint, the few-large-stones construction, or the Blood Axe/neutral Giant culture separation before removing small detail.

## Collision Notes

This package creates no collision asset, collision proxy, UCX mesh, Unreal collision setting, physics body, nav blocker, smart link, gameplay volume, trigger volume, damage volume, aura volume, objective volume, interaction volume, validator script, runtime setup, or collision correctness claim.

Collision guardrails:

- Static dressing only; no collision correctness is approved or claimed.
- Collision disabled should be the baseline assumption for planning discussion only.
- If a later implementation task requires simple contact, it must separately approve any primitive hull around the largest stone mass.
- Cloth, rope, rawhide, ash, soot, mud, lichen, paint, horn, bone, small iron scraps, tiny chips, and texture-only detail should never drive collision.
- Do not use per-stone, per-chip, per-cloth, per-rope, per-ash, per-mud, per-paint, complex-as-simple, physics, destructible, cover, combat, pickup, route, waypoint, objective, trigger, interaction, damage, aura, spawn, patrol, or ritual-boundary collision.

This package makes no claim of terrain integration, route clearance, player movement validity, camera clearance, pickup reach, collision correctness, runtime performance validation, or implementation readiness.

## Animation Notes

The baseline asset is static.

Allowed planning language:

- Static mesh prop only.
- Fixed stone, ash, mud, cloth, rope, rawhide, paint, and optional accent silhouettes if a later source task is approved.
- Static material wear variation may be considered by a later material task, but no material animation is included here.

Not authorized:

- Skeletal animation, cloth simulation, vertex wind, rope physics, swaying cloth, collapse states, destruction, physics settling, material pulses, ritual activation, VFX, audio, UI feedback, objective state, waypoint behavior, breadcrumb behavior, trail gameplay, tracking behavior, navigation behavior, pickup behavior, loot behavior, salvage behavior, interaction behavior, damage/aura behavior, encounter behavior, AI behavior, spawn behavior, patrol behavior, startup placement, runtime behavior, Hermes work, or gameplay behavior.

Any moving, glowing, interactive, pickup-readable, objective-readable, waypoint-readable, gameplay-readable, damaging, aura-emitting, audio-linked, or VFX version must be split into a separately named and approved package.

## Unreal Import Notes

This section is a guardrail only. No Unreal asset, game content folder, import script, material instance, texture asset, socket, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX export, collision setup, navigation setup, trigger setup, objective setup, quest/UI setup, interaction setup, material graph, VFX, audio, final approval, or implementation target is created, selected, or authorized.

No first implementation target is selected by this package. No candidate Unreal folder is created or approved by this package.

If a later separate task authorizes implementation, it must re-confirm:

- Asset name: `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- Asset type: Static Mesh
- Naming convention: `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`, `MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01`, `T_GIA_BloodAxeMovedCampLowCairnRemnant_A01_BC`, `T_GIA_BloodAxeMovedCampLowCairnRemnant_A01_N`, `T_GIA_BloodAxeMovedCampLowCairnRemnant_A01_ORM`
- Pivot: ground center under the remnant footprint, if source is later approved.
- Orientation: strongest readable side faces +X unless a later DCC/export task confirms a different convention.
- Scale: centimeter-authored source, imported at scale 1.0, preserving female 442 cm and male 470 cm Giant baselines.
- Collision type: not approved here; no collision correctness claim.
- LOD plan: LOD0-LOD3 required before any shipping use.
- Material slot count: 1 target, 2 maximum.
- Texture list: BC, N, and ORM only by default; no baseline emissive.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: low material count, shared Blood Axe stone/cloth material language, aggressive LOD reduction, disabled collision on dressing detail, and instancing for repeated static use.

These notes are not Unreal work authorization. They do not permit source asset creation, DCC, FBX, import, Content edits, startup placement, validator work, final visual approval, or implementation target selection.

## Folder and Naming Recommendation

Documentation path created by this task:

- `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/PRODUCTION_PACKAGE.md`

Future asset naming references, for planning only:

- Static mesh: `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- Material instance: `MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- Base color: `T_GIA_BloodAxeMovedCampLowCairnRemnant_A01_BC`
- Normal: `T_GIA_BloodAxeMovedCampLowCairnRemnant_A01_N`
- ORM: `T_GIA_BloodAxeMovedCampLowCairnRemnant_A01_ORM`

Related planning references:

- Parent moved-camp cairn-line kit: `docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/`
- Child asset intake: `docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/CHILD_ASSET_INTAKE.md`
- Cairn guidepost reference: `docs/assets/props/SM_GIA_BloodAxeRitualCairnGuidepost_A01/PRODUCTION_PACKAGE.md`

Do not create or edit source asset folders, DCC files, FBX exports, Unreal game content folders, material instances, texture assets, material graphs, validators, global indexes, backlog docs, task-board docs, bootstrap docs, startup placement, external source concept files, Hermes files or configuration, runtime source files, VFX/audio assets, or unrelated package files from this task.

## Quality Gate Checklist

- Required universal package headings are present in the requested order.
- Package is docs-only and limited to `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/PRODUCTION_PACKAGE.md`.
- Asset remains a single low remnant from a former cairn, not a pair, kit, active guidepost, route marker, objective marker, or implementation target.
- Visual scale is locked to 60-180 cm tall and sized against female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines.
- Approved Giant ranges remain unchanged: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Materials stay on rough highland stone, soot, cold ash, trampled mud, faded oxide red cloth or paint, rawhide, rope, sparse blackened iron, old horn, and dull bone.
- Neutral/civilized Giant material language is excluded: no refined cave-town masonry, terrace/waterwork motifs, warm hearth settlement identity, peaceful highland wayfinding, civic carving, or restrained blue rune culture as the default read.
- Static dressing only; no collision correctness, pickup behavior, loot behavior, salvage behavior, implementation target, gameplay behavior, waypoint behavior, breadcrumb behavior, tracking mechanic, UI path, objective logic, navigation/pathfinding, spawn logic, patrol logic, interaction behavior, VFX, audio, destructible behavior, or physics behavior is defined.
- No DCC work, FBX export, Unreal work, source asset creation, source folder creation, material instance, texture asset, material graph, validator, runtime source, Blueprint, socket, startup placement, final approval, source concept movement, Hermes work, global docs edit, task-board edit, backlog edit, bootstrap edit, approval queue edit, or unrelated package edit is authorized.
- Texture plan includes BC, N, and ORM maps with no default emissive map.
- Triangle budgets, material limits, LOD0-LOD3 plan, collision guardrails, animation limits, Unreal import guardrails, folder naming, and stop gates are included.
- Fine cracks, soot speckles, ash flecks, cloth weave, rope fibers, chipped paint, lichen, pitting, mud streaks, fray, and small scratches are assigned to textures or normals in future work, not modeled clutter.
- The prop remains non-graphic environmental history about a moved Blood Axe camp and never becomes a functional trail, route, waypoint, objective, pickup, or gameplay clue.
