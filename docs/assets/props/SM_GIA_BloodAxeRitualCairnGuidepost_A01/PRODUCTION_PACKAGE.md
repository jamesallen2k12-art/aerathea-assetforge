# SM_GIA_BloodAxeRitualCairnGuidepost_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeRitualCairnGuidepost_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent planning source: `KIT_GIA_BloodAxeRitualStones_A01`
- Parent child row: `BloodAxeRitualStones_A01#CairnGuidepost_Single_A01`
- Related kit: `KIT_GIA_BloodAxeCairnGuideposts_A01`
- Shared policy references: `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01` and `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Role: static warning and memory read only
- Status: planning document only

`SM_GIA_BloodAxeRitualCairnGuidepost_A01` is a single crude cairn guidepost built from a few large stones, one restrained red cloth tie or wrap, and a low ash-stained base. It should read as an old Blood Axe warning or memory marker left in hostile highland territory, not as an active route system, objective, ritual device, or pickup.

Blood Axe identity must stay separate from neutral/civilized Giant culture. This asset may use rough highland stone, soot, ash, mud, rawhide, rope, oxide red cloth, and sparse old horn or dull bone if needed, but it must not borrow refined cave-town masonry, blue-gray civic stonework, terrace or waterwork motifs, warm hearth settlement identity, peaceful highland guide language, or restrained blue rune culture.

This package explicitly excludes trail gameplay, objective logic, waypoint behavior, navigation/pathfinding, pickup/loot behavior, VFX/audio, DCC, FBX, Unreal Content, startup placement, validators, source concept movement, first implementation target selection, final visual approval, final Blood Axe ritual approval, and final Giant culture approval.

## Gameplay Purpose

The gameplay purpose is environmental storytelling only. The prop provides a static warning and memory read for an abandoned or hostile Blood Axe place without defining any player-facing system.

Allowed visual planning uses:

- Mark a Blood Axe remnant site as a hostile Giant sub-faction space through a small, readable cairn silhouette.
- Provide a memory marker near ritual-stone compositions, cave-approach dressing, or old camp residue without selecting placement.
- Reinforce the contrast between Blood Axe raider language and neutral/civilized Giant culture.
- Support later static mesh planning with clear scale, material, LOD, collision, and naming notes.

Out of scope:

- Trail gameplay, objective logic, waypoint behavior, route logic, navigation/pathfinding, path widths, quest markers, UI symbols, readable rune text, interaction prompts, pickup/loot behavior, resource/crafting/economy behavior, offering mechanics, ritual activation, damage/aura behavior, encounter behavior, AI behavior, patrol/spawn logic, destructible behavior, physics behavior, VFX/audio, DCC, FBX, Unreal Content, runtime source, startup placement, validators, source concept movement, first implementation target selection, final visual approval, final Blood Axe ritual approval, or final Giant culture approval.

## Silhouette Notes

- Primary read: a short, blunt Giant-scale cairn made from 4-7 large stacked stones with uneven weight, offset balance, and a non-polished profile.
- Secondary read: one broad oxide red cloth tie, wrap, or hanging strip fixed around the upper or middle stone, sized for Giant hands but subordinate to the stone mass.
- Base read: cold ash, soot, mud, and packed earth forming a low footprint around the cairn. The base should ground the prop but must not become a trail, decal path, objective ring, or marker radius.
- The cairn should feel deliberate but crude: a Blood Axe remnant warning, not a civic monument, shrine altar, road sign, UI arrow, or polished wayfinding object.
- Model future large stones, major contact planes, broad bevels, the cloth silhouette, and any major rawhide or rope wrap as geometry only if a later implementation task approves it.
- Keep fine cracks, small chips, ash flecks, soot speckles, cloth weave, fray, rope fibers, lichen, mud streaks, and tiny paint wear in texture, normal, AO, or mask detail.
- Avoid dense pebble piles, excessive skull or trophy clutter, graphic gore, readable text, glowing runes, UI-like arrows, quest icons, polished blue-gray stoneworker forms, warm hearth motifs, and excessive micro-detail.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant range remains females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Future source, if separately approved, should be authored in centimeters with 1 Unreal unit = 1 cm.

Planning dimensions:

- Overall cairn height: 140-260 cm.
- Footprint: 160-340 cm wide by 130-280 cm deep, including stone spread and ash base.
- Largest lower stone: 90-170 cm wide, 55-120 cm deep, 45-90 cm high.
- Upper stones: 50-130 cm wide with clear stepped reduction toward the top.
- Cloth tie or strip: 55-160 cm long, 18-45 cm wide, placed roughly 90-190 cm above ground.
- Ash/mud base: 180-420 cm footprint, very low height, used as visual grounding only.

The prop should read as small by Giant standards, roughly knee-to-thigh height against a 470 cm male Giant depending on local terrain, but imposing to normal humanoids. These values are visual planning dimensions only and are not traversal, interaction, route, collision, camera, spawn, objective, aura, or nav/pathfinding values.

## Materials and Color Palette

Primary materials:

- Rough highland stone, dark fractured field rock, weathered granite, and ash-stained cairn stone.
- Soot, cold ash, charcoal dust, trampled mud, packed earth, and cave-mouth grit at the base.
- Oxide red cloth, faded maroon wrap, dirty red tie, or chipped red pigment used sparingly as the Blood Axe identity beat.
- Rough hide cord, rawhide wrap, rope lashing, or sinew tie only where it supports the cloth or stone-stack read.
- Sparse blackened iron, old horn, or dull bone only as optional secondary accents, kept non-graphic and low density.

Palette targets:

- Stone and soot: `#17191A`, `#242729`, `#3C3D3A`, `#5A5A53`
- Ash and worn stone: `#6F6D66`, `#8A867B`, `#ADA698`
- Mud and packed earth: `#2A2119`, `#403126`, `#5C4938`
- Oxide red cloth and paint: `#5A1412`, `#711B17`, `#84261E`
- Rope, rawhide, and worn leather: `#5B442B`, `#745C3C`, `#9A7A4E`
- Sparse horn, bone, or dull scrap: `#766A52`, `#927E59`, `#B19A6D`, `#222529`

No default emissive is approved. Do not use ritual glow, shamanic glow, signal glow, torch VFX, animated material states, UI highlights, or gameplay-readable color states. Do not use neutral/civilized Giant materials as the default read.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept sheet of `SM_GIA_BloodAxeRitualCairnGuidepost_A01` for the world of Aerathea. The design should emphasize a single crude Giant-scale cairn guidepost made from a few large rough stones, an uneven stacked silhouette, one restrained oxide red cloth tie, a low soot and ash base, dark highland stone, mud, rawhide or rope restraint, hostile Blood Axe Giant sub-faction identity, strict separation from neutral/civilized Giant culture, and the gameplay role of static warning and memory read only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh production sheet with front, side, back, and three-quarter views, material swatches, LOD/collision callouts, and scale markers beside female 442 cm and male 470 cm Giant baselines on a clean background. Avoid copying any existing franchise, avoid trail gameplay, avoid objective logic, avoid waypoint behavior, avoid navigation/pathfinding diagrams, avoid pickup or loot reads, avoid VFX/audio cues, avoid readable rune text, avoid quest/UI markers, avoid interaction affordances, avoid DCC or Unreal approval claims, avoid final visual approval, avoid neutral Giant civic materials as Blood Axe defaults, avoid graphic gore, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. It creates no DCC source, Blender file, sculpt, mesh, retopo, UVs, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content, material instance, texture asset, material graph, validator, runtime source, startup placement, source concept movement, final visual approval, or first implementation target selection.

Future modeling priorities after separate approval:

- Build the cairn from a few large, readable stone forms rather than many small rocks.
- Use 4-7 major stones with broad fractured planes, thick bevels, and clear contact shadows.
- Keep the stacked silhouette slightly uneven but physically plausible, with the largest stones low and smaller stones above.
- Add one broad fixed cloth tie or hanging strip as a simple static shape; no cloth simulation or wind preparation.
- Keep ash and mud as a low base form or material treatment, not as a path, ring, waypoint, or objective indicator.
- Use rawhide or rope only as large wraps or ties. Avoid dense rope nets and decorative knot clutter.
- Optional horn, dull bone, or blackened iron accents must be sparse, old, non-graphic, and removable from the design without losing the asset identity.
- Place the future pivot at ground center under the cairn footprint if implementation is separately approved.
- Face the strongest readable side toward +X unless a later export convention says otherwise.

Suggested future mesh groups:

- `CairnGuidepost_StoneStack`
- `CairnGuidepost_ClothTie`
- `CairnGuidepost_RawhideRope`
- `CairnGuidepost_AshMudBase`
- `CairnGuidepost_AccentOptional`

Do not add sockets, marker locators, route helpers, nav helpers, VFX locators, audio locators, pickup affordances, interaction prompts, objective volumes, damage volumes, aura volumes, gameplay collision, destructible states, or implementation-specific files.

## Texture and Material Notes

Target material strategy:

- Default target: 1 material slot using shared Blood Axe ritual-stone material language.
- Maximum: 2 material slots only if a later art pass separates stone/base from cloth/rawhide accents.
- No unique material slots for each stone, cloth strip, ash patch, rope tie, horn token, bone token, iron scrap, chip, or stain.
- Default texture target: 1K BC/N/ORM for repeated dressing.
- 2K is acceptable only if a later close-view package explicitly promotes this prop as focal dressing.
- 512 can be acceptable for distant repeated dressing if a shared atlas is prioritized.

Future texture names if a unique texture set is separately approved:

- `T_GIA_BloodAxeRitualCairnGuidepost_A01_BC`
- `T_GIA_BloodAxeRitualCairnGuidepost_A01_N`
- `T_GIA_BloodAxeRitualCairnGuidepost_A01_ORM`

No default emissive texture is planned. `T_GIA_BloodAxeRitualCairnGuidepost_A01_E` must not be created unless a separate emissive/VFX package is approved.

Texture guidance:

- Base Color should carry broad stone value, soot darkening, cold ash, trampled mud, controlled oxide red cloth, rawhide/rope warmth, and optional muted horn/bone/scrap accents.
- Normal should carry fine stone cracks, small chips, cloth weave, fray, rope fibers, horn rings, lichen flecks, and minor surface pitting.
- ORM should use ambient occlusion around stone contacts, cloth overlaps, rope ties, ash base edges, and underside creases.
- Roughness should stay high across stone, ash, mud, cloth, hide, rope, horn, and bone. Metallic should be reserved only for optional blackened iron scraps.

## Triangle Budget

Target budget:

- Asset category: small to medium static prop.
- LOD0: 1.2k-4k tris, 1 material target, 2 material maximum.
- LOD1: 650-2k tris.
- LOD2: 300-900 tris.
- LOD3: 100-300 tris.
- Texture budget: 1K BC/N/ORM by default, 2K only for later close-view use.

Budget notes:

- Spend geometry on the major stone-stack silhouette, stone contact planes, broad cloth outline, large wraps, and low ash base form.
- Use broad bevels and large chipped corners where they affect silhouette.
- Do not spend geometry on tiny pebble clutter, dense crack networks, ash flecks, soot dust, cloth weave, rope fibers, paint chips, small lichen spots, repeated horn chips, or hidden underside detail.
- Repeated placements should rely on instancing, shared material families, and LOD reduction rather than unique heavy variants.

## LOD Plan

All future static mesh implementation requires LOD0, LOD1, LOD2, and LOD3 before any shipping use.

- LOD0: full 4-7 stone cairn stack, major fractured planes, broad bevels, fixed cloth tie, large rawhide or rope wraps, low ash/mud base, and optional sparse accent.
- LOD1: 55-70 percent of LOD0; reduce secondary bevels, small chips, cloth edge cuts, minor wrap subdivisions, and non-visible contact detail while preserving the cairn height and cloth beat.
- LOD2: 30-45 percent of LOD0; merge smaller upper stones where needed, simplify large stones into broad planes, flatten ash base detail, and keep only the strongest red cloth read.
- LOD3: 10-25 percent of LOD0; preserve the blunt cairn mass, stacked height read, base footprint, and one oxide red warning accent only.

Reduction order:

1. Tiny cracks, soot speckles, ash flecks, cloth weave, fray cuts, rope fibers, paint chips, lichen specks, small scratches, and minor pitting.
2. Small knots, secondary lashings, tiny cloth holes, little stone wedges, small horn or bone chips, and minor iron nicks.
3. Hidden underside detail, back-facing stone contacts, interior overlaps, and non-visible ash/mud undercuts.
4. Optional accent pieces, small duplicate foot stones, secondary cloth tears, and non-silhouette debris.
5. Secondary stone bevel density and minor broken-plane cuts.
6. Only after small detail is removed, simplify the primary cairn stack while preserving Giant-scale readability and Blood Axe material identity.

Never reduce the few-large-stones silhouette, static warning/memory read, controlled oxide red cloth beat, or separation from neutral/civilized Giant culture before removing small detail.

## Collision Notes

This package creates no collision asset, collision proxy, UCX mesh, Unreal collision setting, nav blocker, gameplay volume, trigger volume, damage volume, aura volume, objective volume, interaction volume, validator, runtime setup, or collision correctness claim.

Future collision defaults:

- Collision disabled by default for this visual dressing prop.
- If later placement requires simple contact, use one simple box or low-count convex hull around the largest cairn mass.
- Optional second simple hull may cover the lower base stones only if needed for basic player or camera contact.
- Cloth, rope, rawhide, horn, bone, small iron scraps, ash, soot, mud, lichen, paint, tiny chips, and texture-only detail should always have collision disabled.
- Do not use complex-as-simple collision for repeated cairn dressing.

Collision must not define trail gameplay, path gates, route validation, waypoint pairs, objective frames, navigation/pathfinding, traversal proof, encounter lanes, cover rules, damage fields, aura fields, interaction affordances, pickup/loot behavior, resource nodes, destructible behavior, ritual boundaries, or quest logic.

## Animation Notes

Baseline asset is static.

Allowed planning:

- Static mesh only.
- Static cloth and rawhide/rope silhouettes modeled in fixed poses if separately approved.
- Static material wear variants for stone value, soot, ash, mud, cloth age, lichen, paint wear, and roughness if a later material task approves them.

Not included:

- Skeletal animation, cloth simulation, vertex wind, rope physics, swaying cloth, collapse states, destruction, material pulses, ritual activation, VFX, audio, UI feedback, objective state, waypoint behavior, trail gameplay, navigation/pathfinding behavior, pickup/loot behavior, damage/aura behavior, interaction behavior, encounter behavior, AI behavior, startup placement, or runtime behavior.

Any moving, glowing, interactive, gameplay-readable, pickup-readable, objective-readable, waypoint-readable, damaging, aura-emitting, audio-linked, or VFX version must be split into a separately named and approved package.

## Unreal Import Notes

This section is future planning only. No Unreal Content, import script, material instance, texture asset, socket, collision proxy, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX export, source asset folder, final visual approval, or implementation file is created or authorized.

Potential future import identity after separate approval:

- Asset name: `SM_GIA_BloodAxeRitualCairnGuidepost_A01`
- Asset type: Static Mesh
- Candidate future folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/RitualStones/Guideposts/`
- Naming convention: `SM_GIA_BloodAxeRitualCairnGuidepost_A01`, `MI_GIA_BloodAxeRitualCairnGuidepost_A01`, `T_GIA_BloodAxeRitualCairnGuidepost_A01_BC`, `T_GIA_BloodAxeRitualCairnGuidepost_A01_N`, `T_GIA_BloodAxeRitualCairnGuidepost_A01_ORM`
- Pivot: ground center under the cairn footprint.
- Orientation: primary readable side faces +X unless a later export convention sets another direction.
- Scale: centimeter-authored source, imported at scale 1.0, preserving female 442 cm and male 470 cm Giant baselines.
- Collision type: disabled by default; simple primitive collision only if a later implementation lane needs basic contact.
- LOD plan: LOD0-LOD3 required before any shipping use.
- Material slot count: 1 target, 2 maximum.
- Texture list: `T_GIA_BloodAxeRitualCairnGuidepost_A01_BC`, `T_GIA_BloodAxeRitualCairnGuidepost_A01_N`, `T_GIA_BloodAxeRitualCairnGuidepost_A01_ORM`; no baseline emissive texture.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: keep material count low, use shared Blood Axe ritual-stone materials where possible, avoid micro-geometry, disable detail collision, and rely on aggressive LODs for repeated static dressing.

Do not create or authorize trail gameplay, objective logic, waypoint behavior, navigation/pathfinding, pickup/loot behavior, VFX/audio, DCC, FBX, Unreal Content, startup placement, validators, source concept movement, first implementation target selection, final visual approval, final Blood Axe ritual approval, or final Giant culture approval from this package.

## Folder and Naming Recommendation

Docs path created by this task:

- `docs/assets/props/SM_GIA_BloodAxeRitualCairnGuidepost_A01/PRODUCTION_PACKAGE.md`

Future naming recommendations after separate approval only:

- Static mesh: `SM_GIA_BloodAxeRitualCairnGuidepost_A01`
- Material instance: `MI_GIA_BloodAxeRitualCairnGuidepost_A01`
- Base color: `T_GIA_BloodAxeRitualCairnGuidepost_A01_BC`
- Normal: `T_GIA_BloodAxeRitualCairnGuidepost_A01_N`
- ORM: `T_GIA_BloodAxeRitualCairnGuidepost_A01_ORM`
- Emissive: not part of the baseline; approval-gated only as a separately scoped variant

Related planning references:

- `KIT_GIA_BloodAxeRitualStones_A01`
- `KIT_GIA_BloodAxeCairnGuideposts_A01`
- `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01`
- `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01`

Do not create source folders, DCC files, FBX exports, Unreal Content folders, material instances, texture assets, validators, images, source concept copies, runtime source, tools, startup placement files, task-board edits, global index edits, backlog edits, bootstrap edits, approval-queue edits, first implementation target documents, final visual approval notes, or additional docs from this task.

## Quality Gate Checklist

- Package uses the 15 required top-level headings in the required order.
- Package is docs-only and limited to `docs/assets/props/SM_GIA_BloodAxeRitualCairnGuidepost_A01/PRODUCTION_PACKAGE.md`.
- Asset remains a single crude cairn guidepost made from a few large stones, red cloth, and an ash base.
- Asset remains static warning and memory read only.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved female range 14-15 ft / 427-457 cm and approved male range 14'10"-16'0" / 452-488 cm.
- Blood Axe is documented as a hostile Giant sub-faction and remains separate from neutral/civilized Giant culture.
- Neutral/civilized Giant cave-town masonry, blue-gray civic stonework, terrace/waterwork motifs, warm hearth identity, peaceful guide language, and restrained blue rune culture are excluded as defaults.
- Materials use rough highland stone, soot, ash, mud, oxide red cloth, rawhide, rope, and sparse optional horn, bone, or blackened iron without default emissive.
- Texture plan includes Base Color, Normal, and packed ORM only; no default emissive texture.
- Triangle budgets, LOD0-LOD3 plan, disabled-by-default/simple collision limits, static animation notes, future import planning, folder naming, and stop gates are documented.
- No trail gameplay, objective logic, waypoint behavior, navigation/pathfinding, pickup/loot behavior, readable rune text, quest/UI markers, offering mechanics, ritual activation, damage/aura behavior, interaction behavior, encounter logic, AI behavior, patrol/spawn logic, destructible behavior, resource/crafting/economy behavior, VFX/audio, DCC, FBX, Unreal Content, runtime source, startup placement, validators, source concept movement, first implementation target selection, final visual approval, final Blood Axe ritual approval, or final Giant culture approval is created or authorized.
- No source folders, DCC files, Unreal files, validators, images, material instances, texture assets, external source concept movement, global docs, task board, backlog, bootstrap, approval queue, or other workers' package files are edited by this task.
