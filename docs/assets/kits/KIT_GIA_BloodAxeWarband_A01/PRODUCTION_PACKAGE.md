# KIT_GIA_BloodAxeWarband_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeWarband_A01`
- Asset type: Production kit / visual warband hierarchy planning package
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Source routing: `docs/assets/intake/ACIQ-P02_01_GIANT_BLOODAXE_SLATE.md`
- Primary source concepts: `Blood Axe Fist Hunting Party.png`, `BloodAxeChieftan.png`, `BloodAxeGiantMale.png`, `BloodAxeGiantMale2.png`, `BloodAxeLeaderMale.png`, `Bloodaxe Army.png`, `GiantBloodAxeHuntersMale.png`, `GiantBloodAxeMale3.png`, `GiantBloodAxeMale4.png`, `GiantBloodAxeMaleShaman.png`, `GiantBloodAxeMaleandFemale.png`, and `GiantFemaleBloodAxe1.png`
- Dependencies: validated `SK_GIA_Base_A01` scale lock, Blood Axe armory planning in `KIT_GIA_BloodAxeArmory_A01`, and later approval for any child character package
- Status: docs-only package planning; no DCC, Unreal, runtime, gameplay, or first build target selection

`KIT_GIA_BloodAxeWarband_A01` establishes the visual production language for Blood Axe Giant hostile groups: chieftain presence, shamanic intimidation, hunters, raiders, shield carriers, banner bearers, forge guards, trophy carriers, camp sentries, and formation dressing. These are planning rows for visual hierarchy and production scheduling only. They are not final troop roles, AI classes, combat-stat definitions, ability kits, encounter waves, loot tables, or a first character build target.

Blood Axe culture must remain a hostile Giant sub-faction. Red banners, blackened iron, trophy armor, ritual scars, rough hide, smoky camp grit, and brutal weapon silhouettes must not replace neutral/civilized Giant stoneworker culture.

## Gameplay Purpose

The kit supports later Blood Axe NPC visual packages, camp population planning, character outfit variants, armory dependency planning, and composition references for warband-scale screenshots or future scene dressing. The purpose is to make a readable hostile Giant roster at MMO camera distance while preserving build boundaries.

Allowed planning purpose:

- Define visual archetype lanes and production dependencies.
- Identify likely child package names and source references.
- Keep scale, silhouette, material, LOD, collision, and import expectations aligned to the Giant base.
- Route camp, forge, gate, shelter, ritual-stone, and stronghold structures to separate environment packages.

Out of scope:

- Final troop roles or encounter composition.
- AI behavior, patrol logic, aggro logic, combat stats, damage values, ability behavior, projectile behavior, buffs, debuffs, loot, crafting, economy, spawn rules, or first character build target selection.

## Silhouette Notes

Blood Axe warband silhouettes should read as towering, heavy, hostile Giant bodies with clear row-to-row visual differences:

- Chieftain: widest authority silhouette, trophy crown or helm, heavier shoulder mass, larger red cloth blocks, and controlled hero-detail density.
- Shaman: ritual staff or talisman read, ash markings, bone/horn accents, restrained shamanic glow only if later approved.
- Hunters: leaner upper silhouette, bow/quiver read, lighter leg obstruction, stalking posture, and fewer armor plates than raiders.
- Raiders: common Blood Axe infantry read with dark iron plates, rough hide, broad weapons, and red paint or cloth accents.
- Shield carriers: broad front-facing shield mass and braced shoulder line without defining shield mechanics.
- Banner bearers: tall vertical banner pole and torn red cloth read, distinct from default Giant banners.
- Forge guards: soot-dark heavy armor, hammer/cleaver carry language, apron or heat-scorched leather accents.
- Trophy carriers: readable trophy racks, belts, or back loads with restrained skull/horn use and no graphic gore.
- Camp sentries: spear, bow, or gate-watch profile for camp and perimeter dressing without patrol AI claims.
- Formation dressing: grouped height, spacing, banner, and weapon read for concept sheets or review scenes without encounter design.

Keep detail density under control. Model primary body forms, armor plates, banners, shields, weapons, large straps, major trophy shapes, and shamanic staff silhouettes as geometry. Use textures and normal maps for scratches, stitches, small symbols, ash, skin weathering, red paint wear, soot, pitting, tiny rivets, and fine cloth tears.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Feet at world origin for future skeletal children unless the implementation owner approves a different import convention.

Warband planning must preserve the Giant base body scale. Outfit thickness, trophy racks, shield mass, quivers, banners, and carried weapons may change silhouette width and height, but they must not imply a new race scale or invalidate the `SK_GIA_Base_A01` skeleton/socket contract.

Important scale dependencies:

- Giant hands, back sockets, belt sockets, and shoulder clearance inherit from `SK_GIA_Base_A01`.
- Existing armory packages provide planned weapon, banner, bow, quiver, trophy helm, chest, harness, belt, and greave dependencies.
- Camp, gate, shelter, forge, ritual-stone, and stronghold scale belongs to later Blood Axe camp or ritual packages.
- Normal humanoid compatibility is not required for Blood Axe warband gear unless a future loot/display task explicitly asks for it.

## Materials and Color Palette

Primary Blood Axe materials:

- Weathered Giant skin with ash, scars, war paint, and mountain exposure.
- Blackened iron, dark steel, reforged stolen metal, large hammered plates, and simple brutal fittings.
- Scorched leather, rough hide, fur, sinew cord, rawhide wraps, and dark timber accents.
- Bone, horn, tusk, teeth, skull motifs, and trophy shapes used sparingly and cleanly.
- Torn red cloth, red paint, dull red banner panels, and dried grime as sub-faction identifiers.
- Forge soot, ash, charcoal, smoke stains, and muted ember reflection for forge-adjacent rows.

Shamanic material language may include restrained storm, ritual fire, or dark-red ember glow only after visual/material approval. Default warband rows should use no emissive.

Avoid neutral/civilized Giant language in this kit: blue-gray stoneworker motifs, warm cave-town hearth identity, carved civic masonry, restrained blue runes, and civilized workshop ornament belong to separate Giant culture packages unless a stolen-object variant is explicitly approved.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeWarband_A01` for the world of Aerathea. The design should emphasize a hostile Giant Blood Axe warband hierarchy, towering 442 cm female and 470 cm male Giant scale callouts, chieftain presence, shamanic intimidation, hunters, raiders, shield carriers, banner bearers, forge guards, trophy carriers, camp sentries, formation dressing, brutal blackened iron, dark steel, scorched leather, rough hide, controlled bone trophies, torn red banners, soot, ash, red war paint, and clear separation from neutral/civilized Giant stoneworker culture. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a visual production roster and formation planning sheet with front/three-quarter silhouettes, scale bars, material swatches, armory dependency callouts, and non-gameplay composition notes on a clean background. Avoid copying any existing franchise, avoid graphic gore, avoid making Blood Axe language the default Giant culture, avoid readable text dependency, avoid final troop role diagrams, avoid AI/combat stat/ability behavior callouts, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This package does not authorize DCC work. Future character packages should build from the Giant base body and use modular overlays where practical:

- Preserve the massive Giant body read before adding Blood Axe armor or props.
- Reuse approved Blood Axe armory dependencies for weapons, banners, quivers, trophy helm, raider chest, harness, trophy belt, greaves, and reforged material language.
- Separate chieftain, shaman, hunter, raider, shield, banner, forge, trophy, sentry, and formation dressing rows into future packages only after lead approval.
- Keep armor modules and carried props modular enough to swap between male/female Giant baselines after fit review.
- Use clean deformation zones around shoulders, elbows, wrists, hips, pelvis, thighs, knees, ankles, neck, and jaw.
- Keep trophy racks, banner poles, shields, quivers, and forge guard aprons from clipping the locomotion envelope.
- Do not collapse the warband into one baked crowd mesh unless a later distant-dressing task explicitly approves it.

Model real geometry for body forms, major armor plates, shields, banners, weapons, large trophies, staff heads, quiver bodies, broad straps, large chain links, and major cloth panels. Texture or normal-map fine stitches, small scratches, tiny rivets, pitted metal, skin pores, ash smears, cloth weave, minor paint chips, and small ritual marks.

## Texture and Material Notes

Use standard Aerathea texture outputs:

- `T_GIA_BloodAxeWarband_<Child>_BC`
- `T_GIA_BloodAxeWarband_<Child>_N`
- `T_GIA_BloodAxeWarband_<Child>_ORM`
- `T_GIA_BloodAxeWarband_<Child>_E` only for approved shamanic, ritual, or forge-heat variants

Shared material families should align with the armory package:

- `MI_GIA_BloodAxeReforgedMetal_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeScorchedLeather_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeBoneTrophy_A01`
- `MI_GIA_BloodAxeSootAsh_A01`

Character material slot targets:

- Body/skin/head.
- Hair/fur.
- Outfit/armor/leather/cloth.
- Weapons/props as separate attached assets where possible.
- Optional eyes or ritual accent material only when required by the future child package.

Use 2K texture sets for repeatable warband characters. Use 4K only for a named hero, chieftain, boss-scale presentation, or close-up cinematic target after visual approval. Do not create one-off material slots for every strap, trophy, chain, or paint mark.

## Triangle Budget

Future child targets should inherit the `SK_GIA_Base_A01` guidance and remain aggressive about reuse:

- Common raider, hunter, shield carrier, banner bearer, forge guard, trophy carrier, or camp sentry: 55k-75k tris LOD0 total including body, outfit, hair/fur, and major wearable overlays.
- Chieftain or shaman visual variants: 70k-90k tris LOD0 only if approved as hero or boss-adjacent visual packages.
- Modular wearable overlay per major region: 5k-14k tris LOD0, depending on chest, shoulder, belt, greave, trophy rack, or banner harness complexity.
- Carried prop dependencies: use budgets from the Blood Axe armory child packages rather than duplicating geometry into character meshes.
- Formation dressing preview: use instanced/reused child meshes and simple composition markers; do not create a unique high-poly crowd mesh.

Material slot target is 3-5 for a full dressed Giant, excluding attached weapons or separate banner props. Lower is preferred for repeated warband use.

## LOD Plan

All future important warband meshes need LOD0-LOD3:

- LOD0: full body, face planes, hair/fur clumps, major armor plates, banners, shields, large trophy shapes, big straps, quiver forms, readable shamanic props, and primary Blood Axe color blocks.
- LOD1: 60-70 percent of LOD0; reduce small straps, minor trophy cuts, small chain segments, cloth tears, armor bevels, hair subdivisions, and inner outfit folds.
- LOD2: 35-45 percent of LOD0; simplify back-side details, trophy clusters, quiver interiors, banner tears, shield rim bevels, finger detail, and small prop attachments.
- LOD3: 15-25 percent of LOD0; preserve height, shoulder width, head silhouette, banner/shield/weapon outline, red cloth blocks, and row-level visual identity.

Remove small stitches, rivets, scratches, minor hanging pieces, secondary straps, and back-side ornaments before reducing the primary Giant body, shoulder line, head, hands, shields, banners, weapons, or chieftain/shaman silhouette.

## Collision Notes

Future collision should stay character-safe and simple:

- Use Giant-tuned character capsules inherited from `SK_GIA_Base_A01`: female baseline around 442 cm tall and male baseline around 470 cm tall, with variant review for outfit thickness.
- Physics assets should remain simplified around pelvis, spine, chest, head, arms, hands, thighs, calves, feet, and large wearable zones.
- Shields, banners, trophy racks, quivers, and oversized weapons should normally use attachment preview bounds or simple display collision, not per-piece collision.
- Combat hit shapes, damage zones, trace arcs, projectile collision, shield block volumes, aura zones, destructible props, and gameplay triggers are not authored by this docs-only package.
- Formation dressing should use simple editor/review placement bounds only if later approved; no nav blocking, spawn blocking, or encounter logic is defined here.

## Animation Notes

Animation is planning-only. This package does not author animation assets, montages, timing, behavior trees, AI, combat rules, abilities, cloth simulation, or physics setup.

Future visual child packages may need approval-gated animation planning for:

- Giant locomotion and heavy idle inherited from the base.
- Carry/readiness poses for weapons, shields, banners, quivers, trophies, and forge tools.
- Non-final visual stance differences for chieftain, shaman, hunter, raider, sentry, and formation rows.
- Banner hold, trophy carry, shield carry, and shaman staff hold clearance checks.
- Bow draw, melee swing, shield brace, spell cast, banner wave, or forge work only after gameplay and animation approval.

No animation row in this package should be treated as a final combat move, ability behavior, AI state, patrol rule, or encounter script.

## Unreal Import Notes

No Unreal import is authorized by this task. Planned paths and names below are for future package planning only.

Potential Unreal folders:

- Characters: `/Game/Aerathea/Characters/Giants/BloodAxe/Warband/`
- Gear dependencies: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`
- Weapons and banners: `/Game/Aerathea/Weapons/Giants/BloodAxe/` and `/Game/Aerathea/Props/Giants/BloodAxeArmory/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`

Potential future names:

- `SK_GIA_BloodAxeChieftain_A01`
- `SK_GIA_BloodAxeShaman_A01`
- `SK_GIA_BloodAxeHunter_A01`
- `SK_GIA_BloodAxeRaider_A01`
- `SK_GIA_BloodAxeShieldCarrier_A01`
- `SK_GIA_BloodAxeBannerBearer_A01`
- `SK_GIA_BloodAxeForgeGuard_A01`
- `SK_GIA_BloodAxeTrophyCarrier_A01`
- `SK_GIA_BloodAxeCampSentry_A01`
- `KIT_GIA_BloodAxeFormationDressing_A01`

Expected import assumptions for future work:

- Skeletal mesh children should inherit the Giant base scale and skeleton policy unless a later fit task approves otherwise.
- Pivot: feet at world origin for skeletal characters; prop pivots follow their armory package rules.
- Scale: centimeter authored, Unreal import scale 1.0 after DCC/export rules are established.
- Material slots: 3-5 for complete character variants, with attached weapons and banners kept as separate assets where practical.
- Sockets: use Giant base sockets for hand, back, belt, chest, head, quiver, banner, and weapon attachments; add no new socket contract in this package.
- Blueprint behavior: none.
- AI/combat behavior: none.
- Startup placement: none.

## Folder and Naming Recommendation

- Docs: `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/`
- Kit package: `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/CHILD_ASSET_INTAKE.md`
- Future child package docs only after approval: `docs/assets/characters/SK_GIA_BloodAxeChieftain_A01/`, `docs/assets/characters/SK_GIA_BloodAxeShaman_A01/`, `docs/assets/characters/SK_GIA_BloodAxeHunter_A01/`, and related Blood Axe character rows.

Do not create `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal import files, runtime source, validators, startup placements, global indexes, task-board updates, or external source concept copies from this package.

## Approval Gates

- Lead approval is required before choosing any first Blood Axe warband child build target.
- Visual approval is required before locking chieftain, shaman, hunter, raider, shield carrier, banner bearer, forge guard, trophy carrier, camp sentry, or formation dressing final silhouettes.
- DCC approval is required before creating source folders, Blender files, proof renders, LOD sources, collision proxies, or FBX exports.
- Unreal approval is required before importing Skeletal Meshes, Static Meshes, materials, textures, Blueprints, validators, or startup actors.
- Gameplay approval is required before defining final troop roles, combat stats, AI, abilities, encounter formations, projectile behavior, shield behavior, aura effects, spawn rules, loot, crafting, economy, interaction, or patrol logic.
- Animation approval is required before authoring montage timing, bow draw/release, melee swings, shield brace, banner motion, shaman casting, cloth, physics, or deformation tests.
- Source-storage approval is required before any external source concept file is copied, moved, edited, embedded, or committed.
- Culture approval is required if Blood Axe raider language starts bleeding into neutral/civilized Giant culture.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5".
- Child intake covers chieftain, shaman, hunters, raiders, shield carriers, banner bearers, forge guards, trophy carriers, camp sentries, and formation dressing as planning-only rows.
- Warband composition is visual and production planning only, not gameplay encounter design.
- No final troop roles, AI, combat stats, ability behavior, first build target, DCC, FBX, Unreal, runtime, validator, startup placement, global index, task-board, or source concept copy is claimed.
- Silhouettes stay readable at MMO camera distance.
- Materials use blackened iron, dark steel, scorched leather, hide/fur, controlled bone trophies, red cloth, soot, ash, and rough reforged-metal surfaces consistently.
- Tiny rivets, scratches, stitching, dense trophy clutter, pitting, and minor paint damage are assigned to textures or normals.
- Emissive use is absent by default and approval-gated for shamanic, ritual, or forge-heat variants.
- Triangle budgets, texture maps, material slot targets, LODs, collision, animation limits, Unreal path planning, approval gates, and source-storage guardrails are included.
