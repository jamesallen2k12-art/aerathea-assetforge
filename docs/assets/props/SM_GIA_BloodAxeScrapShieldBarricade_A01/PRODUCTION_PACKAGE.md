# SM_GIA_BloodAxeScrapShieldBarricade_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeScrapShieldBarricade_A01`
- Asset type: Static Mesh production package / Blood Axe Giant scrap-shield barricade prop
- Task: `AET-MA-20260629-135`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Barricade_ScrapShieldWall`
- Source route reference: `BloodAxeGate.png#Barricade_ScrapShieldWall`
- Related planning references: `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeForgeScrapSorting_A01`, `KIT_GIA_BloodAxeScrapPile_A01`, `KIT_GIA_BloodAxeReforging_A01`, and `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, collision proxy creation, material graph, runtime source, validator, startup placement, first DCC target selection, first build target selection, final visual approval, or source concept movement is included
- Source-storage guardrail: external source concept images remain outside the repository. Do not copy, move, edit, crop, embed, rename, inspect for final approval, or commit external source concepts for this package.

`SM_GIA_BloodAxeScrapShieldBarricade_A01` defines a static Blood Axe camp barricade assembled from broken shield faces, bent armor plates, broad scrap bars, blackened iron frames, chained braces, and restrained red warning paint. It should read as a hostile Giant-scale recycled-metal obstruction and camp dressing piece, not as a destructible gameplay object, cover system, loot source, resource node, trap, or interactable salvage pile.

Blood Axe remains a hostile Giant sub-faction. This asset must stay separate from neutral/civilized Giant culture: no refined cave-town shield walls, no blue-gray monumental masonry, no peaceful highland craft identity, no warm civic hearth language, no restrained blue runes, and no presentation that makes Blood Axe raider material the default identity of Giants in Aerathea.

## Gameplay Purpose

The barricade supports Blood Axe camp readability as static visual obstruction and recycled-metal dressing only. It helps a future camp layout communicate a hostile perimeter, gate approach, forge-yard scrap reuse, or raider staging edge without defining any gameplay behavior.

Allowed visual planning purpose:

- Mark hostile Blood Axe camp edges, gate flanks, forge-yard lanes, stronghold approaches, and rough perimeter choke points.
- Reuse the Blood Axe forge-scrap language as an organized shield-and-plate wall instead of a random scrap heap.
- Provide a Giant-scale recycled-metal prop near gates, watch platforms, forge hearths, weapon racks, path markers, and formation dressing.
- Show that raiders reclaim broken shields, stolen plate, failed forge stock, and battlefield debris into quick camp defenses.
- Preserve Blood Axe hostile sub-faction identity while avoiding neutral/civilized Giant cultural bleed.

Out of scope:

- Destructible behavior, damage states, trap behavior, spike damage, fire damage, repair behavior, breakable cover, combat cover behavior, AI cover logic, projectile-blocking gameplay claims, navmesh/pathfinding rules, collision proxy creation, physics simulation, trigger volumes, interaction prompts, inspect behavior, salvage behavior, loot tables, resource nodes, inventory behavior, crafting systems, vendor data, economy data, VFX, audio, material graph authoring, Blueprint behavior, runtime source, validators, startup placement, DCC source, FBX export, Unreal import, final visual approval, or source concept movement.

## Silhouette Notes

Primary read: a low-to-mid-height Giant-scale barricade made from overlapping broken shield faces and bent metal plates, braced by crude posts, broad bars, chains, and welded scrap. It should feel improvised, heavy, and hostile, with a jagged but readable upper line that blocks a camp lane visually without becoming a trap, cover object, or working defense system.

Required silhouette elements:

- Broad overlapping shield faces, broken heater-like slabs, round shield fragments, and rectangular plate sections sized for Giant use.
- A heavy lower spine or frame made from blackened iron bars, damaged timber blocks, or reforged metal rails.
- Two or three large vertical brace posts or plate stacks that establish rhythm across the wall segment.
- Jagged top profile from broken shield rims, blade-like scrap corners, split plate, and bent hardware, kept bold rather than densely spiked.
- Thick chain loops, crude clamp plates, and oversized rivet silhouettes only where they affect the primary read.
- Restrained red paint slashes, red warning cloth ties, or Blood Axe marks that identify the hostile sub-faction without turning the barricade into a red wall.
- Mud-packed base, wedge stones, or heavy foot plates so the barricade sits believably on camp ground.
- Optional side end caps that imply repeatable segments, without authoring modular snap behavior in this docs-only task.

Model real geometry for the shield faces, main plate slabs, frame rails, large brace posts, major chain loops, large clamp plates, broad red cloth ties, and grounded base forms. Use texture and normal detail for fine scratches, pitting, soot streaks, small rivets, chipped paint, hammer marks, quench stains, tiny dents, leather stitching, and minor cracks.

Avoid dense tiny shards, needle-spike clutter, graphic gore, treasure-pile readability, neutral/civilized Giant shield-wall language, polished armory display, glowing interaction affordances, loot beams, resource-node symbols, trap teeth, obvious cover cutouts, or fine micro-detail that will not survive mid-poly MMO production.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Recommended static barricade scale:

- Overall width: 650-1100 cm for a single visual obstruction segment.
- Overall height: 260-430 cm, tall enough to feel Giant-built but low enough to sit below the full 470 cm male Giant silhouette in review composition.
- Overall depth: 120-260 cm including angled brace feet, base wedges, and overlapping plate depth.
- Main shield/plate faces: 140-320 cm wide or tall per large piece, with partial fragments allowed.
- Lower frame rail height: 45-120 cm.
- Vertical brace post height: 260-430 cm.
- End-cap thickness: 60-120 cm.
- Chain or clamp accents: 30-90 cm broad where visible from MMO camera distance.
- Red cloth ties: 80-220 cm long, used sparingly.
- Clear camp lane guidance around the segment: 500-800 cm when placed along Giant-scale paths. This is composition guidance only, not navmesh or pathfinding behavior.

Future DCC validation must compare wall height, width, plate scale, brace reach, and base footprint against both the 442 cm female Giant and 470 cm male Giant baselines before any mesh, collision, Unreal import, or visual approval work. Do not shrink the barricade toward normal humanoid camp-prop scale.

## Materials and Color Palette

Primary Blood Axe material language:

- Blackened iron, dark steel, and dull reforged metal aligned with `MI_GIA_BloodAxeReforgedMetal_A01`.
- Broken shield faces, stolen armor plates, failed cast plates, broad blade offcuts, and bent bar stock.
- Scorched timber or dark wedge blocks only for base braces, if needed.
- Heavy chains, rough clamp plates, large bolt heads, damaged hinges, and warped rim bands.
- Soot, ash, mud, oil-dark grime, quench stains, and dull forge wear.
- Deep oxide red paint, chipped red shield marks, and torn red warning cloth used sparingly.
- Bone or horn markers are not a primary material for this asset; if used at all, keep them rare, non-graphic, and secondary to the shield-and-metal read.

Suggested palette:

- Soot black: `#0B0A09` to `#24201C`
- Blackened iron: `#151719` to `#2A2C2E`
- Worn dark steel: `#4F5556` to `#777B78`
- Burnt plate brown: `#2A1B14` to `#4A3023`
- Ash and dried mud: `#5A554D` to `#8A8275`
- Deep oxide red: `#5F1513` to `#8B211B`
- Faded red cloth: `#4A1010` to `#77201B`
- Weathered edge highlight: `#8A8275` to `#B0A28A`

Avoid neutral/civilized Giant blue-gray stoneworker motifs, refined masonry, peaceful highland markers, warm hearth craft, civic cave-town presentation, restrained blue runes, polished metalwork, or shamanic storm glow as baseline. No default emissive is approved.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeScrapShieldBarricade_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant scrap-shield barricade, static visual obstruction and recycled-metal dressing role, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, overlapping broken shield faces, bent armor plates, blackened iron frame rails, broad reforged scrap bars, crude vertical braces, heavy chain loops, large clamp plates, mud-packed base wedges, soot, ash, oil-dark grime, chipped oxide-red paint, torn red warning cloth, and Blood Axe hostile sub-faction identity. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh production sheet with front, side, back, top-down footprint, scale callouts beside 442 cm female and 470 cm male Giants, material swatches, LOD/collision notes, and labels stating non-interactive camp dressing only. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral/civilized Giant shield-wall or cave-town language, avoid destructible-state diagrams, avoid trap or damage callouts, avoid combat-cover diagrams, avoid loot/resource/salvage markers, avoid interaction prompts, avoid startup placement claims, avoid first-DCC-target selection, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeGate.png#Barricade_ScrapShieldWall` only through existing intake documentation. It does not inspect, move, copy, crop, embed, or approve external source concept art.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, Blueprint, validator, startup actor, runtime behavior, first DCC target selection, or final visual approval is created or approved here.

Future modeling should prioritize large readable forms:

- Main shield wall: build overlapping broken shield and armor-plate slabs as broad shapes with strong positive and negative reads.
- Lower frame: model a heavy blackened rail, bent bar, or crude base spine that visibly holds the wall together.
- Vertical braces: add two or three oversized brace posts, bent plate stacks, or timber-backed metal supports to create segment rhythm.
- End caps: include simple side caps or thicker terminal plates so the barricade can stand as a single prop without requiring modular snap rules.
- Scrap identity: mix shield faces, rim bands, failed plate casts, broken blade slabs, and large bar stock, but keep the silhouette cleaner than a scrap pile.
- Hardware: model broad clamp plates, large rivet blocks, heavy chain loops, and welded scrap straps only where visible from camera distance.
- Blood Axe marks: add a few large red paint slashes, chipped hand marks, or cloth ties as fixed static accents.
- Ground contact: use wedge feet, mud-packed base blocks, bent foot plates, or stone weights to make the asset feel planted.

Use texture, normal maps, or material masks for:

- Fine scratches.
- Dense pitting.
- Tiny dents.
- Soot gradients.
- Quench staining.
- Small rivets.
- Hammer noise.
- Chipped paint.
- Cloth weave.
- Leather stitching.
- Minor cracks.
- Mud spatter.

Do not model gameplay affordance geometry such as interact buttons, salvage handles, glowing outlines, trap teeth, spike-damage tips, loot beams, resource-node crystals, health-state fracture pieces, breakaway panels, cover-slot labels, objective markers, UI plaques, or pickup highlights.

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, emissive map, VFX graph, or Unreal import is authored by this package.

Material slot target:

- Slot 0: `MI_GIA_BloodAxeReforgedMetal_A01` or matching blackened metal instance for shield faces, armor plates, frame rails, plate rims, scrap bars, clamp plates, chains, and large rivets.
- Slot 1: planned soot/ash/mud material or atlas region for mud-packed base, dark grime, and ash buildup if not handled in Slot 0 masks.
- Slot 2: planned Blood Axe red cloth/paint material or atlas region for warning ties and red marks.
- Optional future Slot 3: rough timber or scorched leather only if brace construction needs a separate material for readability.

Shared material family alignment:

- `MI_GIA_BloodAxeReforgedMetal_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeSootAsh_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeRoughTimber_A01` only for brace variants

Texture naming examples:

- `T_GIA_BloodAxeScrapShieldBarricade_A01_BC`
- `T_GIA_BloodAxeScrapShieldBarricade_A01_N`
- `T_GIA_BloodAxeScrapShieldBarricade_A01_ORM`
- `T_GIA_BloodAxeScrapShieldBarricade_Metal_A01_BC`
- `T_GIA_BloodAxeScrapShieldBarricade_Base_A01_BC`
- `T_GIA_BloodAxeScrapShieldBarricade_RedMarks_A01_BC`

Texture resolution targets:

- Default repeated camp barricade: 2K texture set.
- Background perimeter variant: 1K texture set.
- Close-route hero barricade variant: 2K, with 4K only if a later hero-review task explicitly approves it.

Packed `ORM` guidance:

- R: strong ambient occlusion under overlapping shields, clamp plates, chains, brace posts, base wedges, and mud contact.
- G: high roughness for soot, ash, mud, chipped paint, cloth, and matte blackened metal; slightly lower roughness only on worn steel edges.
- B: metallic only for iron, steel, shield faces, plate rims, chains, clamp plates, rivets, and scrap bars.

No default emissive map is needed. Any forge-heat, magic, shamanic, alarm, trap, or active warning glow must be split into a later approval-gated variant.

## Triangle Budget

Default static barricade target:

- LOD0: 7k-14k tris.
- LOD0 hard cap: 18k tris only if a later approved build includes extra large shield silhouettes and end-cap variation in the same mesh.
- Material slots: 2-3 target, 4 maximum only by later approval.
- Texture target: 2K default.

Variant guidance:

- Compact repeated barricade segment: 4k-8k tris, 2 material slots.
- Standard scrap-shield barricade: 7k-14k tris, 2-3 material slots.
- Wider gate-flank obstruction variant: 12k-18k tris, 3 material slots.
- Far background dressing variant: keep under 4k tris and rely on broad dark metal, jagged shield profile, and red accent blocks.

Spend geometry on large shield faces, plate overlaps, main rail, brace posts, broad scrap bars, chain silhouettes, grounded base forms, and red accent cloth shapes. Do not spend geometry on tiny rivets, fine scratches, dense pitting, hundreds of small shards, thin wire, cloth fray, micro dents, small flakes, individual mud clumps, or tiny broken shield chips.

## LOD Plan

All important barricade variants require LOD0-LOD3.

- LOD0: full overlapping shield-and-plate wall, lower frame, vertical braces, end caps, large chain loops, broad clamp plates, grounded base forms, red paint/cloth accents, and major asymmetry.
- LOD1: 60-70 percent of LOD0; reduce small bevels, secondary plate chips, minor chain subdivisions, cloth edge cuts, tiny rivets, and backside hardware.
- LOD2: 35-45 percent of LOD0; simplify plate overlaps, shield interior forms, base wedge detail, secondary braces, clamp bevels, and red cloth cuts while preserving the wall read.
- LOD3: 15-25 percent of LOD0; preserve overall barricade footprint, jagged shield-and-plate top profile, large brace rhythm, dark metal mass, and red Blood Axe accent blocks.

LOD reduction order:

1. Tiny scratches, pitting, soot speckles, paint flakes, small cracks, and micro dents.
2. Small rivets, minor metal band bevels, cloth edge nicks, fine lashing detail, and small chips.
3. Secondary shield fragments, duplicate small scrap plates, backside clamps, and minor chain links.
4. Interior overlap detail, underside base forms, and non-silhouette brace cuts.
5. Only after secondary details are reduced, simplify the main shield faces, lower rail, vertical braces, end caps, and red/black faction read.

Never reduce the Giant-scale footprint, broken shield-wall silhouette, brace rhythm, or Blood Axe red/black read before removing small surface and backside detail.

## Collision Notes

Collision remains simple, static, and display-focused planning only. This package does not create collision proxies, UCX meshes, physics bodies, runtime collision channels, nav links, nav blockers, cover tags, damage volumes, interaction volumes, or validation scripts.

Recommended future collision:

- Main wall mass: one to three simple boxes or low-count convex hulls around the broad shield-and-plate footprint.
- End caps and brace feet: folded into the main hulls unless a raised base affects player traversal.
- Lower frame rail: simple box or hull only where it visibly blocks movement.
- Chains, cloth ties, small clamps, individual shield rims, small plates, and rivets: no individual collision.
- Back side: simplified to broad blocking only if level placement requires it.
- Walkable collision: disabled by default on top edges, plate ledges, and brace forms.

Do not add pickup collision, salvage traces, loot outlines, resource harvesting volumes, crafting interaction volumes, trap triggers, damage volumes, destructible fracture collision, physics-simulated loose scrap, per-shield collision, per-chain collision, combat trace sockets, navmesh behavior, AI cover behavior, or projectile-blocking gameplay claims in this package.

Future implementation must decide whether the barricade is purely backdrop, static visual blocker, or level-art lane edge. This package does not define traversal policy, cover behavior, AI behavior, damage behavior, destruction behavior, loot/resource behavior, or gameplay collision channels.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Static mesh visual planning.
- Fixed shield faces, fixed plate slabs, fixed frame rails, fixed braces, fixed chains, fixed clamp plates, fixed base wedges, and fixed red cloth ties.
- No runtime motion claim.

Approval-gated future work:

- Cloth simulation, chain sway, plate rattle, physics-simulated scrap, break states, collapse states, impact reactions, repair states, trap states, heat shimmer, material-state animation, or VFX.
- Interaction prompts, salvage behavior, loot behavior, resource collection, crafting behavior, economy behavior, damage/trap behavior, combat cover behavior, AI use, encounter behavior, objective logic, audio cues, or startup-scene behavior.

Any moving, usable, breakable, damaging, or cover-tagged version must be split into a separately named Blueprint or variant so `SM_GIA_BloodAxeScrapShieldBarricade_A01` remains lightweight static camp dressing.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, Niagara system, validator, startup actor, runtime source, import script, collision proxy, or first DCC target is created by this package.

Planned future Unreal asset:

- Asset name: `SM_GIA_BloodAxeScrapShieldBarricade_A01`
- Asset type: Static Mesh
- Planned mesh folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Props/Barricades/`
- Planned material folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Planned texture folder: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/Barricades/`
- Naming convention: `SM_GIA_BloodAxeScrapShieldBarricade_A01`, `MI_GIA_BloodAxeScrapShieldBarricade_*_A01`, and `T_GIA_BloodAxeScrapShieldBarricade_A01_*`
- Pivot: ground-contact center of the barricade footprint, centered along the wall length.
- Orientation: primary hostile face and strongest read faces +X unless a future project import convention overrides it.
- Scale: centimeter-authored source, import at scale 1.0 after future DCC/export approval.
- Collision type: simple custom collision or generated primitive collision as described above, only in a later implementation task.
- LODs: import LOD0-LOD3 if and when mesh work is approved.
- Material slot count: 2-3 target, 4 maximum only by later approval.
- Default material family references: `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeSootAsh_A01`, `MI_GIA_BloodAxeRedCloth_A01`, optional `MI_GIA_BloodAxeRoughTimber_A01`.
- Texture list: `T_GIA_BloodAxeScrapShieldBarricade_A01_BC`, `T_GIA_BloodAxeScrapShieldBarricade_A01_N`, `T_GIA_BloodAxeScrapShieldBarricade_A01_ORM`.
- Sockets: none required. Do not add combat trace, damage, trap, loot, salvage, resource, pickup, cover, VFX, or interaction sockets in this docs-only package.
- Animation list: none. Static mesh baseline only.
- Blueprint behavior: none. This asset is static visual obstruction and recycled-metal dressing only.
- Performance notes: keep shard density low, merge repeated shield fragments where practical, preserve broad red/black reads, and use LODs aggressively for camp-background placement.

Potential future visual-only locator labels for a concept sheet or DCC blockout, not Unreal sockets in this task:

- `face_primary_visual`
- `endcap_left_visual`
- `endcap_right_visual`
- `brace_post_visual`
- `red_warning_cloth_visual`
- `scrap_plate_rhythm_visual`

## Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeScrapShieldBarricade_A01/`
- Package file: `docs/assets/props/SM_GIA_BloodAxeScrapShieldBarricade_A01/PRODUCTION_PACKAGE.md`
- Planned Unreal mesh: `SM_GIA_BloodAxeScrapShieldBarricade_A01`
- Planned material instances: `MI_GIA_BloodAxeScrapShieldBarricade_Metal_A01`, `MI_GIA_BloodAxeScrapShieldBarricade_Base_A01`, `MI_GIA_BloodAxeScrapShieldBarricade_RedMarks_A01`
- Planned textures: `T_GIA_BloodAxeScrapShieldBarricade_A01_BC`, `T_GIA_BloodAxeScrapShieldBarricade_A01_N`, `T_GIA_BloodAxeScrapShieldBarricade_A01_ORM`
- Planned future source root if later approved: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeScrapShieldBarricade_A01/`
- Planned future export path if later approved: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeScrapShieldBarricade_A01.fbx`
- Planned future Unreal folder if later approved: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Props/Barricades/`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, validators, material graphs, collision proxy files, external source concept copies, global index entries, task-board updates, production backlog edits, loot/resource definitions, destructible components, trap logic, cover tags, or pickup interactions from this task packet.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Blood Axe visual language remains separate from neutral/civilized Giant culture, including cave-town masonry, hearth, terrace, waterwork, warm civic craft, and restrained blue-rune language.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", with approved Giant ranges documented.
- The asset is static visual obstruction and recycled-metal camp dressing only.
- The barricade supports hostile camp edge, gate-flank, forge-yard, and stronghold-approach readability without destructible behavior, damage/trap behavior, cover behavior, loot/resource behavior, interaction behavior, or startup placement.
- Silhouette is readable at MMO camera distance: overlapping broken shields, bent plates, lower frame rail, vertical braces, end caps, chains, clamp plates, grounded base, and restrained red warning marks.
- Materials use blackened iron, dark steel, reforged scrap, soot, ash, mud, chipped red paint, and torn red cloth consistently.
- Tiny rivets, scratches, pitting, stitching, soot speckles, paint flakes, quench stains, minor dents, and dense hammer noise are assigned to textures or normals instead of geometry.
- Emissive use is absent by default and approval-gated for any later forge-heat, magic, shamanic, alarm, trap, or active warning variant.
- Triangle budgets, texture maps, material slot targets, LOD0-LOD3, collision planning, animation notes, Unreal import planning, folder naming, and stop gates are included.
- Source concept remains external and is not copied, moved, edited, cropped, embedded, inspected for final approval, or committed by this package.
- Package makes no DCC, FBX, Unreal Content, runtime source, material graph, validator, startup placement, collision proxy creation, first DCC target selection, combat behavior, damage/trap behavior, cover behavior, pickup behavior, inventory behavior, loot behavior, economy behavior, resource behavior, interaction behavior, destructible behavior, or final visual approval claim.
