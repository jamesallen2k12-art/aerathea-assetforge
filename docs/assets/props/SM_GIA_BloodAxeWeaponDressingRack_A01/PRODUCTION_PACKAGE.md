# SM_GIA_BloodAxeWeaponDressingRack_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeWeaponDressingRack_A01`
- Asset type: Static Mesh production package / Blood Axe Giant weapon dressing rack prop
- Task: `AET-MA-20260629-126`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Zone_WeaponDressingRack`
- Source route reference: `BloodAxeCamp.png#Zone_WeaponDressingRack`
- Related planning references: `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeArmory_A01`, `KIT_GIA_BloodAxeBowParts_A01`, `KIT_GIA_BloodAxeReforging_A01`, and `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, material graph, runtime source, validator, startup placement, first DCC target selection, first build target selection, final visual approval, or source concept movement is included
- Source-storage guardrail: external source concept images remain outside the repository. Do not copy, move, edit, crop, embed, rename, inspect for final approval, or commit external source concepts for this package.

`SM_GIA_BloodAxeWeaponDressingRack_A01` defines a static camp dressing rack for hostile Blood Axe Giant weapon staging, field repair, and silhouette storytelling. It should read as a huge rough rail and brace frame holding oversized weapon silhouettes, repair blocks, lash points, and prop references from the Blood Axe armory language. The rack is dressing with silhouette slots and prop references, not gameplay inventory.

Blood Axe remains a hostile Giant sub-faction. The rack must stay separate from neutral/civilized Giant culture: no orderly cave-town weapon stands, no refined blue-gray masonry, no civic stoneworker craft pride, no warm hearth-hall language, no restrained blue runes, and no presentation that makes Blood Axe raider equipment the default identity of Giants in Aerathea.

This package is static visual production planning only. It does not authorize DCC, FBX, Unreal work, weapon pickup behavior, loot/economy/resource behavior, interaction behavior, destructible behavior, startup placement, or first DCC target selection.

## Gameplay Purpose

The weapon dressing rack supports Blood Axe camp readability as non-interactive environmental storytelling. Players should understand that this is a hostile Giant raider staging area where enormous weapons are stored, repaired, and leaned for display, without being given inventory, loot, pickup, crafting, repair, or economy affordances.

Allowed visual planning purpose:

- Mark a Blood Axe camp weapon staging and repair zone.
- Provide a Giant-scale silhouette anchor near forge hearth, scrap sorting, anvil/quench, sentry, hunter, and formation dressing packages.
- Reuse armory silhouettes as static prop references: double axe, crusher hammer, longbow, cleaver, hook spear, shortbow, quiver, arrow bundle, broken blade, bow limb, repair wedge, and scrap plate.
- Give environment artists a repeatable dressing prop for camp edges, forge yards, armory lean-tos, and warband muster spaces.
- Preserve Blood Axe hostile sub-faction identity while avoiding neutral/civilized Giant cultural bleed.

Out of scope:

- Weapon pickup behavior, gameplay inventory, loot containers, loot tables, resource nodes, salvage loops, crafting stations, vendor hooks, economy data, repair UI, upgrade systems, stat comparison, or weapon unlock behavior.
- Interaction prompts, usable workstation behavior, trigger volumes, inspect behavior, harvest behavior, drag/drop equipment behavior, physics-grab behavior, or player-facing objective logic.
- Destructible states, breakable racks, damage volumes, combat cover behavior, AI cover logic, projectile blockers, navmesh/pathfinding rules, encounter scripting, audio, VFX, material graph authoring, Blueprint behavior, runtime source, validators, startup placement, DCC source, FBX export, Unreal import, final visual approval, or source concept movement.

## Silhouette Notes

Primary read: a Giant-scale hostile weapon dressing rack made from raw timber, blackened iron bracing, heavy lashings, rough repair shelves, and oversized weapon silhouettes. It should look improvised, brutal, and field-built, but still readable at MMO camera distance.

Required silhouette elements:

- Two or three massive vertical timber posts with uneven heights and battered tops.
- A thick horizontal weapon rail sized for Giant weapons, held by blackened iron bands and rope or hide lashings.
- Broad lower cross brace or repair shelf for heavy blade slabs, bow limbs, quiver shells, and repair wedges.
- Large silhouette slots for armory references: double-axe head gap, hammer-head rest, hook-spear hook cradle, longbow arc lean, shortbow/bow-part groove, cleaver slab slot, quiver lean space, and arrow-bundle channel.
- A few static prop references attached or leaned into the rack: broken blade slab, spare grip wrap, cracked bow limb, arrow bundle, scrap plate, chain loop, and red cloth tag.
- Sparse red cloth, red paint slashes, or warning ties as Blood Axe identifiers.
- Optional small tool pegs for visual dressing only, sized for Giant use and not presented as interactable tools.

Model real geometry for the posts, rail, lower brace, large weapon silhouette slots, broad metal bands, repair shelf, large wedges, heavy chain loops, and major red cloth tags. Use texture and normal detail for fine wood grain, small chips, tiny rivets, leather stitching, soot, scratches, minor cracks, dense pitting, frayed fibers, and small red paint flakes.

Avoid a clean retail weapon rack, neutral/civilized Giant armory display, ornate mountain-stone stand, humanoid-scale barracks fixture, glowing interaction ring, weapon pickup highlight, loot-beam shape, inventory tag, resource-node symbol, dense tiny tools, excessive trophies, graphic gore, or unreadable micro-detail.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Recommended static rack scale:

- Overall width: 620-980 cm.
- Overall height: 360-560 cm, with tallest post able to sit above a 442 cm female Giant shoulder line but not obscure the full 470 cm male Giant silhouette in review composition.
- Overall depth: 180-320 cm, depending on lower brace and leaned weapon silhouettes.
- Primary rail height: 250-390 cm.
- Lower brace or repair shelf height: 90-170 cm.
- Post diameter or broad side width: 45-90 cm.
- Large weapon slot widths: 70-180 cm each, varied by weapon silhouette.
- Longbow lean clearance: 360-460 cm vertical arc reference from the armory kit.
- Double axe and crusher hammer rest zones: sized for 300-430 cm weapon silhouettes without claiming those weapons are included as functional assets.
- Clear front work apron: 420-650 cm for Giant stance and staged visual access.
- Side clearance near camp paths: 500-800 cm when placed along primary camp circulation.

Future DCC validation must compare rack height, rail reach, slot spacing, and clear work apron against both the 442 cm female Giant and 470 cm male Giant baselines before any mesh, collision, Unreal import, or visual approval work. Do not shrink the rack to normal humanoid armory scale.

## Materials and Color Palette

Primary Blood Axe material language:

- Rough raw timber, split logs, and battered field posts.
- Blackened iron, dark steel, and reforged scrap braces aligned with `MI_GIA_BloodAxeReforgedMetal_A01`.
- Scorched leather, rawhide lashings, sinew ties, rope wraps, and repair straps.
- Broken weapon offcuts, bow limbs, quiver shells, arrow bundles, scrap plates, and large repair wedges as static prop references.
- Soot, ash, mud, oil-dark grime, and dull forge wear.
- Deep oxide red cloth tags, crude red paint slashes, and red warning wraps used sparingly.
- Bone or horn markers only as sparse non-graphic accents if needed for Blood Axe camp continuity.

Suggested palette:

- Soot black: `#0B0A09` to `#24201C`
- Raw timber brown: `#3A2418` to `#6A432B`
- Weathered tan wood edge: `#8A6B4A` to `#A6845B`
- Blackened iron: `#151719` to `#2A2C2E`
- Worn dark steel: `#50575A` to `#777B78`
- Scorched leather: `#241611` to `#4A2E20`
- Rawhide lashing: `#7A6040` to `#A58A5A`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Ash and dried mud: `#5A554D` to `#8A8275`

Avoid neutral/civilized Giant blue-gray stoneworker motifs, refined stone carving, warm communal hearth tones, restrained blue runes, orderly weapon-hall display, polished craftsmanship, or shamanic storm glow as the baseline. No default emissive is approved.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeWeaponDressingRack_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant weapon dressing rack, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, massive raw timber posts, a thick weapon rail, crude blackened iron bracing, rawhide lashings, broad lower repair shelf, silhouette slots for double axes, crusher hammers, hook spears, cleavers, longbows, quivers, arrow bundles, broken bow limbs, scrap plates, red warning cloth, soot, ash, grime, Blood Axe hostile sub-faction identity, and a static camp dressing role rather than gameplay inventory. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a static prop production sheet with front, side, back, top-down footprint, scale callouts beside 442 cm female and 470 cm male Giants, material swatches, LOD/collision notes, and labels for non-interactive silhouette slots and prop references. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral/civilized Giant armory language, avoid pickup prompts, avoid loot or inventory UI, avoid weapon stat tags, avoid destructible-state diagrams, avoid first-DCC-target selection, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeCamp.png#Zone_WeaponDressingRack` only through existing intake documentation. It does not inspect, move, copy, crop, embed, or approve external source concept art.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, Blueprint, validator, startup actor, runtime behavior, first DCC target selection, or final visual approval is created or approved here.

Future modeling should prioritize large readable forms:

- Post frame: build two or three massive raw-log posts with uneven tops, wide bases, and rough lean variation.
- Weapon rail: model a thick horizontal rail with broad notches or silhouette slots for huge Blood Axe weapon shapes.
- Lower brace and shelf: create a heavy support shelf for blade slabs, bow parts, quiver shells, wedges, and scrap offcuts.
- Silhouette slots: design broad negative spaces and rest points that imply double axe, hammer, hook spear, cleaver, longbow, quiver, arrow bundle, and bow-part staging without turning the rack into functional equipment storage.
- Metal hardware: model wide blackened bands, corner plates, large clamp blocks, and a small number of oversized rivets where they affect silhouette.
- Lashings: model only the largest rope, sinew, hide, or leather wraps that visually hold the rack together.
- Static prop references: include a small curated set of non-interactive broken blade shapes, bow limbs, arrow bundle silhouettes, repair wedges, chain loops, and red tags.
- Ground contact: include heavy foot blocks, mud-packed bases, or log wedges so the rack sits believably in packed earth or forge-yard dressing.

Use texture, normal maps, or material masks for:

- Fine wood grain.
- Small splinters.
- Tiny cracks.
- Soot streaks.
- Ash dust.
- Leather pores.
- Rope fibers.
- Small rivets.
- Fine scratches.
- Minor hammer marks.
- Dense pitting.
- Red paint chips.

Do not model gameplay affordance geometry such as interact buttons, inventory plates, weapon rarity tags, glowing outlines, pickup handles, loot beams, recipe plaques, vendor signs, resource icons, destructible fracture pieces, objective markers, or UI silhouettes.

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, emissive map, VFX graph, or Unreal import is authored by this package.

Material slot target:

- Slot 0: planned rough Blood Axe timber material for posts, rail, lower brace, shelf, wedges, and ground-contact logs.
- Slot 1: `MI_GIA_BloodAxeReforgedMetal_A01` or matching blackened hardware instance for iron bands, scrap plates, large rivets, chain loops, broken blade silhouettes, and heavy clamps.
- Slot 2: planned scorched leather/rawhide/red-cloth material for lashings, grip wraps, warning strips, and repair ties.
- Optional future slot 3: shared bone/horn accent material only if sparse non-graphic camp marker details are approved during later visual review.

Shared material family alignment:

- `MI_GIA_BloodAxeReforgedMetal_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeRoughTimber_A01`
- `MI_GIA_BloodAxeScorchedLeather_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeSootAsh_A01`
- `MI_GIA_BloodAxeBoneTrophy_A01` only for sparse non-graphic marker accents

Texture naming examples:

- `T_GIA_BloodAxeWeaponDressingRack_A01_BC`
- `T_GIA_BloodAxeWeaponDressingRack_A01_N`
- `T_GIA_BloodAxeWeaponDressingRack_A01_ORM`
- `T_GIA_BloodAxeWeaponDressingRack_Timber_A01_BC`
- `T_GIA_BloodAxeWeaponDressingRack_Hardware_A01_BC`
- `T_GIA_BloodAxeWeaponDressingRack_Lashing_A01_BC`

Texture resolution targets:

- Default camp dressing prop: 2K texture set.
- Repeated background variant: 1K texture set.
- Close-route hero camp variant: 2K, with 4K only if a later hero-review task explicitly approves it.

Packed `ORM` guidance:

- R: strong ambient occlusion under rail notches, metal bands, post bases, lower shelf, weapon slots, lashing wraps, and leaned prop references.
- G: high roughness for raw timber, soot, ash, mud, leather, rawhide, and matte blackened metal; slightly lower roughness only on worn steel edges.
- B: metallic only for iron, steel, scrap plates, rivets, chain loops, and broken blade silhouettes.

No default emissive map is needed. Any forge-heat, magic, shamanic, active repair, or warning glow state must be split into a later approval-gated variant.

## Triangle Budget

Default static rack target:

- LOD0: 8k-16k tris.
- LOD0 hard cap: 20k tris only if a later approved build includes many static prop-reference silhouettes in the same mesh.
- Material slots: 3 target, 4 maximum only for separately approved sparse bone/horn accents.
- Texture target: 2K default.

Variant guidance:

- Compact repeated camp rack: 5k-9k tris, 2-3 material slots.
- Standard weapon dressing rack: 8k-16k tris, 3 material slots.
- Larger forge-yard staging rack with more weapon silhouette slots: 14k-20k tris, 3-4 material slots by approval.
- Far dressing variant: keep under 5k tris and rely on broad timber, black metal, and red-cloth color blocks.

Spend geometry on post mass, rail silhouette, large weapon slots, lower shelf, major hardware, lashing silhouettes, broad prop-reference forms, and red Blood Axe tags. Do not spend geometry on tiny rivets, fine cracks, dense rope strands, hundreds of splinters, small scratches, tiny edge chips, micro hammer marks, loose nails, or cluttered miniature tools.

## LOD Plan

All important rack variants require LOD0-LOD3.

- LOD0: full post frame, rail, lower brace, shelf, major notches, large weapon silhouette slots, broad metal bands, large lashings, selected prop-reference silhouettes, red warning cloth, and grounded base wedges.
- LOD1: 60-70 percent of LOD0; reduce small bevels, secondary notch cuts, minor chain loop detail, small cloth edge cuts, secondary shelf props, and non-silhouette lashing turns.
- LOD2: 35-45 percent of LOD0; simplify post surface variation, metal band bevels, lower shelf underside, small repair wedges, weapon-slot interiors, and back-side prop references while preserving the rack read.
- LOD3: 15-25 percent of LOD0; preserve the giant post-and-rail outline, large slot rhythm, dark hardware blocks, red Blood Axe accents, and a few big leaned weapon-shape references.

LOD reduction order:

1. Tiny cracks, soot speckles, wood-grain cuts, small chips, and minor red paint flakes.
2. Small rivets, minor metal band bevels, fine lashing strands, cloth edge nicks, and small scratches.
3. Secondary repair wedges, small tool pegs, inner shelf clutter, minor chain links, and backside lashing loops.
4. Back-side prop references and underside shelf detail.
5. Secondary post bevels and non-silhouette rail notches.
6. Only after secondary details are reduced, simplify the post frame, weapon rail, major slot rhythm, and red/black faction read.

Never reduce the Giant-scale footprint, tall post silhouette, rail height, slot rhythm, or Blood Axe red/black read before removing small surface and backside detail.

## Collision Notes

Collision remains simple, static, and display-focused.

Recommended future collision:

- Main frame: low-count convex hulls or grouped boxes around the vertical posts, main rail, and lower brace.
- Lower shelf: one simple box or hull if it visibly blocks traversal.
- Leaned static prop-reference silhouettes: collision disabled by default or folded into the main rack hull.
- Chain loops, lashings, cloth tags, small wedges, repair props, and arrow bundles: no individual collision.
- Ground-contact blocks: folded into main hulls; no per-block collision.
- Back side: simplified to broad blocking only if level placement requires it.

Do not add weapon pickup collision, interactable traces, inventory hit shapes, loot outlines, resource harvesting volumes, repair station volumes, crafting trigger volumes, vendor volumes, destructible fracture collision, physics bodies, per-weapon collision, per-arrow collision, per-chain collision, combat trace sockets, damage volumes, navmesh behavior, AI cover behavior, or projectile-blocking gameplay claims in this package.

Walkable collision should be disabled by default on the rack, lower shelf, and prop-reference silhouettes unless a later level-design task explicitly promotes a variant for traversal or cover.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Static mesh visual planning.
- Fixed posts, rail, shelf, hardware, lashings, and prop-reference silhouettes.
- Non-simulated red cloth tags and fixed chain loops.
- No runtime motion claim.

Approval-gated future work:

- Cloth simulation, chain sway, hanging weapon sway, physics-simulated prop references, break states, rack collapse, impact reactions, animated repair states, or material-state animation.
- Interaction prompts, weapon pickup, inventory transfer, loot behavior, repair behavior, crafting behavior, salvage behavior, economy behavior, resource collection, audio cues, objective logic, AI use, encounter behavior, cover behavior, or destructible behavior.

Any moving, usable, or breakable version should be split into a separately named Blueprint or variant so `SM_GIA_BloodAxeWeaponDressingRack_A01` remains lightweight static camp dressing.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, Niagara system, validator, startup actor, runtime source, import script, or first DCC target is created by this package.

Planned future Unreal asset:

- Asset name: `SM_GIA_BloodAxeWeaponDressingRack_A01`
- Asset type: Static Mesh
- Planned folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Props/Dressing/`
- Planned material folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Planned texture folder: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/Dressing/`
- Pivot: ground-contact center between the main posts, centered on the rack footprint.
- Orientation: front staging side faces +X unless a future project import convention overrides it.
- Scale: centimeter-authored source, import at scale 1.0 after future DCC/export approval.
- Collision: simple custom collision or generated primitive collision as described above.
- LODs: import LOD0-LOD3 if and when mesh work is approved.
- Material slot count: 3 target, 4 maximum only by later approval.
- Default material family references: `MI_GIA_BloodAxeRoughTimber_A01`, `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeScorchedLeather_A01`, `MI_GIA_BloodAxeRedCloth_A01`, and optional sparse `MI_GIA_BloodAxeBoneTrophy_A01`.
- Texture list: `T_GIA_BloodAxeWeaponDressingRack_A01_BC`, `T_GIA_BloodAxeWeaponDressingRack_A01_N`, `T_GIA_BloodAxeWeaponDressingRack_A01_ORM`.
- Sockets: none required for the default static prop. Do not add combat trace, pickup, inventory, or interaction sockets in this docs-only package.
- Blueprint behavior: none. This asset is static visual dressing only.
- Performance notes: keep prop-reference density low, merge repeated silhouette forms where practical, and use LODs aggressively for camp-background placement.

Potential future visual-only locator labels for a concept sheet or DCC blockout, not Unreal sockets in this task:

- `slot_double_axe_visual`
- `slot_crusher_hammer_visual`
- `slot_hook_spear_visual`
- `slot_longbow_visual`
- `slot_quiver_visual`
- `slot_arrow_bundle_visual`
- `slot_repair_scrap_visual`

## Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeWeaponDressingRack_A01/`
- Package file: `docs/assets/props/SM_GIA_BloodAxeWeaponDressingRack_A01/PRODUCTION_PACKAGE.md`
- Planned Unreal mesh: `SM_GIA_BloodAxeWeaponDressingRack_A01`
- Planned material instances: `MI_GIA_BloodAxeWeaponDressingRack_Timber_A01`, `MI_GIA_BloodAxeWeaponDressingRack_Hardware_A01`, `MI_GIA_BloodAxeWeaponDressingRack_Lashing_A01`
- Planned textures: `T_GIA_BloodAxeWeaponDressingRack_A01_BC`, `T_GIA_BloodAxeWeaponDressingRack_A01_N`, `T_GIA_BloodAxeWeaponDressingRack_A01_ORM`
- Planned future source root if later approved: `SourceAssets/Props/Giants/BloodAxe/SM_GIA_BloodAxeWeaponDressingRack_A01/`
- Planned future Unreal folder if later approved: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Props/Dressing/`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, validators, material graphs, external source concept copies, or global index entries from this task packet.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Blood Axe visual language remains separate from neutral/civilized Giant culture, including cave-town masonry, hearth, terrace, waterwork, warm civic craft, and restrained blue-rune language.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", with approved Giant ranges documented.
- The asset is a weapon rack as dressing with silhouette slots and prop references, not gameplay inventory.
- The rack supports static camp staging, repair-zone storytelling, armory silhouette references, and forge-yard composition without pickup, loot, economy, crafting, interaction, destructible, or resource behavior.
- Silhouette is readable at MMO camera distance: huge posts, thick weapon rail, lower repair shelf, large slots, blackened hardware, lashings, red warning tags, and a few broad weapon-shape references.
- Materials use raw timber, blackened iron, reforged metal, scorched leather, rawhide, soot, ash, grime, and restrained red Blood Axe accents consistently.
- Tiny rivets, scratches, pitting, stitching, splinters, soot speckles, wood grain, and dense lashing detail are assigned to textures or normals instead of geometry.
- Emissive use is absent by default and approval-gated for any later forge-heat, magic, shamanic, or warning variant.
- Triangle budgets, texture maps, material slot targets, LOD0-LOD3, collision planning, animation notes, Unreal import planning, folder naming, and stop gates are included.
- Source concept remains external and is not copied, moved, edited, cropped, embedded, inspected for final approval, or committed by this package.
- Package makes no DCC, FBX, Unreal Content, runtime source, material graph, validator, startup placement, first DCC target selection, combat behavior, pickup behavior, inventory behavior, loot behavior, economy behavior, resource behavior, interaction behavior, destructible behavior, or final visual approval claim.
