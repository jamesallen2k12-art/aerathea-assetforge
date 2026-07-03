# SK_GIA_BloodAxeChieftain_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeChieftain_A01`
- Asset type: Skeletal Mesh character production package / hostile Blood Axe Giant leader candidate
- Parent scale dependency: `SK_GIA_Base_A01`
- Related Blood Axe kit: `KIT_GIA_BloodAxeArmory_A01`
- Related gear packages: `SK_GIA_BloodAxeRaiderChest_A01`, `SK_GIA_BloodAxeHarness_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, `SK_GIA_BloodAxeGreaves_A01`, `SM_GIA_BloodAxeTrophyHelm_A01`
- Related weapon packages: `SM_GIA_BloodAxeDoubleAxe_A01`, `SM_GIA_BloodAxeCrusherHammer_A01`, `SM_GIA_BloodAxeCleaver_A01`, `SM_GIA_BloodAxeHookSpear_A01`, `SM_GIA_BloodAxeLongbow_A01`, `SM_GIA_BloodAxeLongbow_A02`, `SM_GIA_BloodAxeLongbow_A03`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, runtime, validator, startup placement, final visual approval, or first DCC target selection is included.

`SK_GIA_BloodAxeChieftain_A01` defines a hostile Blood Axe Giant leader production direction: an intimidating warband command silhouette built from massive Giant body language, blackened reforged armor, red warning cloth, rough trophies, and brutal field-forged equipment. This is a leader archetype package for future Blood Axe warband planning, not a finalized named boss encounter.

The Blood Axe Tribe must remain separate from neutral/civilized Giant culture. This package uses hostile raider visual language: soot-dark iron, crude trophies, red cloth markers, scorched leather, heavy scars, and camp-command intimidation. It must not overwrite the neutral Giant identity of remote mountain stoneworkers, hidden cave towns, highland nomads, blue-gray stone craft, warm hearths, or restrained rune/storm accents.

This document is production planning only. It does not copy, move, edit, embed, or commit external source concepts, and it does not authorize final lore naming, combat abilities, boss mechanics, wearable skeletal fit, cloth/physics, animation timing, or first build-target selection.

## Gameplay Purpose

The chieftain package establishes a readable enemy-leader silhouette for future Blood Axe warbands, camps, armory yards, gate holds, and command compositions. The gameplay read is "hostile Giant leader with command presence," not a specific named boss, not a finalized encounter, and not a combat rules package.

Expected future use cases:

- Elite Blood Axe warband leader or camp command NPC visual direction.
- Scale and silhouette reference for future Blood Axe warband packages.
- Character anchor for coordinating existing Blood Axe armor, helm, harness, belt, greaves, banner, and weapon language.
- Future DCC/Unreal planning target only after a separate approval chooses build ownership and source concept direction.
- Optional review pairing with existing Blood Axe weapon packages, without selecting a final weapon or DCC target in this task.

Out of scope:

- Final named lore lock, title lock, personality lock, or story-specific identity.
- Combat abilities, boss mechanics, damage windows, ability telegraphs, encounter phases, loot rules, faction aura behavior, or objective logic.
- DCC source, Blender files, sculpt files, retopo, UVs, bakes, FBX exports, Unreal Content assets, validators, startup placement, or runtime source.
- Wearable skeletal fit, cloth simulation, chain physics, secondary motion, physics asset tuning, authored animation, animation timing, and final visual approval.

## Silhouette Notes

Primary silhouette: a towering Blood Axe Giant command figure with broad shoulders, heavy hands, thick neck, powerful torso, wide stance, aggressive helm or faceguard mass, asymmetrical shoulder armor, heavy chest plates, broad belt/tassets, brutal greaves, and one clear command or weapon read. The chieftain should feel like a dangerous warband leader because of scale, posture, gear mass, and controlled trophy language, not because of dense micro-detail.

Core silhouette requirements:

- Preserve the validated Giant body mass first: height, shoulder breadth, long arms, heavy hands, sturdy legs, large feet, thick neck, and broad torso.
- Use a larger chieftain-grade upper-body read than a common raider: one dominant spaulder, reinforced chest plate, heavier brow/helm line, and a stronger red cloth or trophy mantle shape.
- Keep armor asymmetrical but readable: one side can carry larger plate and trophy mass while the other side preserves arm and weapon clearance.
- The head/helm read should identify command rank through a broad brow, skull-forward faceguard option, high crest, horn/bone caps, or red cloth tabs, but must keep face and neck readability.
- Trophy language should be sparse and large: a few aged bone, horn, broken weapon, shield fragment, or dry token shapes. Avoid trophy curtains, skull carpets, tooth necklaces covering the torso, or graphic remains.
- Red cloth and paint should form bold accents around the shoulder, belt, back, or weapon carry area. Do not turn the character into a one-color red figure.
- Weapons should remain optional visual companions at this package stage. The silhouette can reserve hand/back readability for a double axe, crusher hammer, hook spear, cleaver sidearm, or bow, but this package does not choose a final equipped weapon.

Avoid:

- Making the chieftain a scaled normal humanoid in armor.
- Making Blood Axe brutality the default Giant culture.
- Dense chains, tiny rivet fields, many small dangling charms, fine gore detail, unreadable cloth fringe, or excessive skull repetition.
- Neutral/civilized Giant blue-gray stoneworker motifs, warm hearth symbols, peaceful highland craft language, or restrained blue rune accents as the baseline.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock without alteration:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Feet at world origin and facing the project Giant import convention established by the base package.

Planning target:

- Primary command silhouette review should use the male 470 cm baseline for maximum leader mass.
- Female 442 cm baseline should remain documented for future variant and armor-clearance review.
- This package does not lock the chieftain's final gender, named identity, body variant, or final proportions beyond the approved Giant scale range.

Fit and clearance planning for future tasks:

- Helmet, brow, jaw, hair, neck, and shoulder clearance must be validated against the Giant base before wearable or integrated character claims.
- Shoulder armor must leave enough space for one-handed and two-handed weapon poses, bow-draw review, and upper-body turn poses in a future animation task.
- Belt, tassets, sidearm sheath, and trophy tags must clear pelvis, thigh, knee, stride, crouch, and wide combat stance poses before implementation.
- Greaves must preserve Giant calf width, ankle mass, foot length, heel width, toe-box breadth, and ground-contact read.
- Back silhouette must leave room for `back_large_weapon`, `back_shield`, future `back_quiver`, banner dressing, and harness anchors without collapsing into clutter.
- Normal humanoid compatibility is not required.

## Materials and Color Palette

Primary Blood Axe leader materials:

- Blackened iron and dark steel from the Blood Axe reforged-metal family.
- Hammered stolen plates with broad dents, heavy edge wear, crude repairs, and soot-darkened seams.
- Scorched leather, dark hide, rough fur pads, sinew, rawhide, and heavy cord.
- Deep oxide red cloth, dirty red war paint, and red wrap accents as faction identifiers.
- Aged bone, horn, teeth, broken shield pieces, and cracked weapon trophies used sparingly and non-graphically.
- Soot, ash, mud, dried grime, oil-dark recesses, and worn steel highlights on major edges.
- Weathered Giant skin and hair/fur language inherited from `SK_GIA_Base_A01`, but overridden by hostile Blood Axe war paint and raider wear only where needed.

Suggested palette:

- Blackened iron: `#151719` to `#2A2C2E`
- Worn dark steel: `#555A5C` to `#787B78`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Scorched leather: `#241611` to `#4A2E20`
- Dark hide/fur: `#1D1511` to `#3B2A1E`
- Old bone/horn: `#A69578` to `#D0B98C`
- Soot and grime: `#0B0A09` to `#403025`
- Weathered Giant skin: use the base Giant skin range, dirtied with ash and war paint rather than replacing it with armor color.

No default emissive is approved. Forge heat, ritual glow, shamanic markings, storm marks, faction aura, animated material states, or glowing eyes require a separate visual/material package and must not be assumed for `A01`.

## Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_GIA_BloodAxeChieftain_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant leader silhouette, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, towering shoulder mass, heavy hands, powerful legs, skull-forward helm or broad command faceguard, asymmetrical reforged armor plates, brutal chest and spaulder mass, heavy trophy belt and greaves, scorched leather harness, deep oxide red cloth markers, blackened iron, dark steel, soot, aged bone trophies used sparingly, preserved Giant body mass, Blood Axe raider command identity, and a gameplay role as a warband leader visual package rather than a finalized named boss encounter. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a character production sheet with front, side, back, three-quarter views, helmet/faceguard callouts, shoulder and belt clearance callouts, material swatches, scale markers against the approved Giant baselines, optional weapon silhouette placeholders from existing Blood Axe weapon packages, and docs-only guardrails on a clean background. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid final named lore lock, avoid combat abilities or boss mechanics, avoid wearable-fit claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, export, skeletal fit, physics asset, cloth setup, socket authoring, Unreal asset, or final visual approval is created or approved by this package.

Future modeling should start from the validated Giant body proportions and build the chieftain read with large forms:

- Giant body base: preserve the head, brow, jaw, thick neck, torso, shoulders, arms, heavy hands, pelvis, sturdy legs, large feet, and grounded stance.
- Head/helm: model a broad command helm, skull-forward faceguard, brow plate, horn/bone caps, cheek guards, or crest only if the face/neck read stays clear.
- Torso armor: model the main chest plate, dominant spaulder, secondary shoulder support, back plate, and large harness straps as bold readable forms.
- Harness and belt: model broad scorched-leather bands, oversized rings, heavy belt core, large tassets, side anchors, and a few command trophies.
- Lower body: model greaves, knee guards, ankle collars, boot/sabaton mass, and major straps without narrowing Giant legs or feet.
- Hair/fur/cloth: use large clumps, pads, and broad strips. Avoid hair strands, micro-fringe, or cloth curtains unless a later cloth/physics task approves them.
- Trophy accents: use a few large dry trophies, broken weapon fragments, horn pieces, or shield fragments where they support rank and silhouette.
- Weapon placeholders: if a future concept sheet includes a weapon, keep it as a removable visual companion from existing Blood Axe weapon packages. Do not merge a weapon into the character mesh by default.

Use texture, normal maps, or material masks for:

- Tiny rivets.
- Fine scratches.
- Dense pitting.
- Small hammer marks.
- Stitch rows.
- Leather pores.
- Fur strand texture.
- Hairline cracks.
- Small red paint chips.
- Soot speckles.
- Minor chain scuffs.
- Small bone grain.

Future implementation gates:

- Do not claim wearable skeletal fit until a separate character/gear fit lane validates the armor over both approved Giant baselines.
- Do not add chain swing, dangling trophies, cloth strips, capes, banner cloth, or secondary motion without cloth/physics approval.
- Do not solve animation timing, attack arcs, weapon traces, boss phases, or ability telegraphs in the model package.
- Separate display-only gear, optional weapons, and worn/integrated character elements if future pivots, sockets, or clearance needs diverge.

## Texture and Material Notes

Target texture families for a future approved build:

- `T_GIA_BloodAxeChieftain_A01_Body_BC`
- `T_GIA_BloodAxeChieftain_A01_Body_N`
- `T_GIA_BloodAxeChieftain_A01_Body_ORM`
- `T_GIA_BloodAxeChieftain_A01_Gear_BC`
- `T_GIA_BloodAxeChieftain_A01_Gear_N`
- `T_GIA_BloodAxeChieftain_A01_Gear_ORM`
- `T_GIA_BloodAxeChieftain_A01_HairFur_BC`
- `T_GIA_BloodAxeChieftain_A01_HairFur_N`
- `T_GIA_BloodAxeChieftain_A01_HairFur_ORM`
- Optional future approval-gated `T_GIA_BloodAxeChieftain_A01_E`

Material slot target:

- Slot 0: body/head/skin war paint.
- Slot 1: eyes, hair, and fur, or split eyes if the future base convention requires it.
- Slot 2: `MI_GIA_BloodAxeReforgedMetal_A01` or a consuming chieftain gear instance for blackened iron, dark steel, chipped red paint masks, and hammered plates.
- Slot 3: scorched leather, dark hide, red cloth, and harness wraps.
- Slot 4: optional bone/horn/trophy material only if shared atlas readability cannot handle these accents.

Target 4 material slots, 5 maximum only if eyes/hair or trophy materials must remain separate for quality and reuse. Do not create unique material slots for every strap, ring, trophy, paint mark, or cloth strip.

Packed `ORM` plan:

- R: Ambient occlusion around armor overlaps, strap compression, helm cavities, belt/tasset hinges, greave undercuts, trophy anchors, and heavy body folds.
- G: High roughness for soot, leather, hide, bone, matte blackened metal, and weathered skin; slightly lower roughness on rubbed steel edges and hand-contact hardware.
- B: Metallic only for iron, steel, buckles, rings, chain links, weapon hardware, and armor plates.

Texture readability requirements:

- Keep red accents broad and sparse enough to identify Blood Axe rank without flattening the character into a red mass.
- Use skin, armor, leather, cloth, and trophy value separation so the chieftain reads from MMO camera distance.
- Paint broad hammer marks, war paint, soot gradients, large scars, and edge wear at Giant scale.
- Avoid readable text, franchise-like symbols, loot-rarity colors, graphic gore, fresh blood, wet shine, or material masks that imply damage types, weak points, loot state, or boss phase state.
- No baseline emissive, heat, ritual glow, shamanic glow, pulsing eyes, or animated material state is approved.

## Triangle Budget

`SK_GIA_BloodAxeChieftain_A01` should be more elaborate than a common raider, but it is not a finalized named boss or raid encounter asset.

Target budget for a future approved fully dressed character:

- LOD0 target: 55k-68k tris for body, head, hair/fur, integrated leader armor, helm, belt, greaves, harness, and controlled trophies.
- LOD0 hard cap: 70k tris unless a later named hero or boss variant receives separate approval.
- Optional equipped weapon budget: use the weapon's own package budget and do not include it in the character mesh budget.
- Material slots: 4 target, 5 maximum.
- Texture resolution: 2K standard for body and gear sets; 4K only for an approved close-up hero or named boss variant.

Budget distribution guidance:

- Body, head, hands, feet, and base anatomical forms: 45-55 percent.
- Armor plates, helm, spaulders, belt, greaves, and boots: 25-32 percent.
- Harness straps, rings, buckles, red cloth, hair/fur clumps, and command silhouette breaks: 12-18 percent.
- Sparse trophies, large chains, and secondary accents: 5-8 percent.

Do not spend geometry on tiny rivets, dense chain links, fine stitches, hair strands, micro scratches, repeated tooth strands, or small gore detail.

## LOD Plan

All future character implementations require LOD0-LOD3.

- LOD0: full Giant body mass, face/helm read, hands/feet, hair/fur clumps, chest/spaulder armor, harness, belt/tassets, greaves, broad red cloth markers, sparse large trophies, and primary command silhouette.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small strap loops, hair/fur subdivisions, small buckle edges, secondary trophy cuts, and underside armor details.
- LOD2: 35-45 percent of LOD0; simplify fingers, inner armor folds, back-side straps, tasset details, trophy forms, fur clump cuts, and secondary cloth folds while preserving the leader read.
- LOD3: 15-25 percent of LOD0; preserve height, shoulders, head/helm, hands, weapon/carry readable zones, red/black Blood Axe material blocks, and broad stance.

LOD reduction order:

1. Tiny rivets, scratches, stitches, pitting, leather pores, and small paint flakes.
2. Small strap loops, knots, buckle bevels, and minor chain segments.
3. Small trophy fragments, tiny bone chips, and cloth tears.
4. Under-armor and back-side detail.
5. Secondary hair/fur cuts and non-silhouette folds.
6. Minor plate bevels and interior armor cuts.
7. Only after all secondary detail is reduced, simplify the helm, shoulder, chest, belt, hands, feet, and stance.

Never reduce the validated Giant scale read, shoulder line, heavy hands, head/helm silhouette, broad belt/tasset read, or Blood Axe color blocks before removing small detail.

## Collision Notes

No collision, physics asset, or hit setup is authored or approved in this docs-only package.

Future collision planning:

- Character collision type: Giant-tuned movement capsule inherited from `SK_GIA_Base_A01` conventions.
- Male 470 cm planning capsule: roughly 470 cm height and 100-125 cm radius, pending future implementation validation.
- Female 442 cm planning capsule, if a variant is approved: roughly 442 cm height and 95-115 cm radius.
- Physics asset should use simplified bodies for pelvis, spine, chest, head, upper/lower arms, hands, grouped fingers, thighs, calves, feet, and only approved large hair/fur/gear bodies.
- Worn armor, trophies, and gear should normally rely on the owning Giant physics asset and simple bounds, not per-strap or per-trophy collision.
- Equipped weapons should use their own package collision and future approved trace markers; do not add weapon collision rules in this character package.

Do not add separate boss hit zones, weak points, armor-stat collision, stomp damage volumes, command aura volumes, loot pickup collision, per-chain collision, per-cloth collision, or per-trophy collision from this package.

## Animation Notes

No animation, Animation Blueprint, montage, authored timing, cloth simulation, secondary motion, physics setup, or final pose set is created or approved here.

Future animation review may inherit or evaluate Giant-scale motion families only after separate approval:

- Heavy idle and command idle.
- Walk, run/jog, turn in place, and wide-stance combat idle.
- One-handed heavy weapon hold and swing compatibility.
- Two-handed axe, hammer, or hook spear hold compatibility.
- Bow grip and draw clearance only if a future archer/chieftain variant is approved.
- Back carry, sidearm draw, quiver reach, and weapon stow clearance.
- Hit reactions, stagger, and death/collapse only as future animation tasks.

Animation style should sell Giant mass with broad arcs and clear weight shifts, but this package does not define animation timing, attack cadence, ability telegraphs, damage windows, boss mechanics, or encounter phases. Rigid gear should be preferred for a first pass. Cloth strips, swinging chains, dangling trophies, banner cloth, fur secondary motion, or physics-driven pieces require separate approval and validation.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, physics asset, validator, startup actor, runtime source, or import script is created by this package.

Planned future Unreal asset:

- Asset name: `SK_GIA_BloodAxeChieftain_A01`
- Asset type: Skeletal Mesh character candidate
- Planned folder: `/Game/Aerathea/Characters/Giants/BloodAxe/Chieftain/`
- Planned skeleton dependency: future approved Giant skeleton convention inherited from `SK_GIA_Base_A01`
- Import scale: centimeter-authored source, import scale 1.0 after future DCC/export validation
- Pivot: feet at world origin, matching the Giant base convention
- Forward orientation: match the Giant base import convention selected by the future implementation task
- Collision type: Giant movement capsule plus simplified physics asset only after implementation approval
- LODs: LOD0, LOD1, LOD2, LOD3 required before production import approval
- Material slot count: 4 target, 5 maximum
- Blueprint behavior: none
- Animation list: none authored by this package
- Performance notes: keep the fully dressed leader under the non-named-boss target, reduce trophies and straps before primary silhouette, and avoid extra material slots for small accents.

Planned texture names:

- `T_GIA_BloodAxeChieftain_A01_Body_BC`
- `T_GIA_BloodAxeChieftain_A01_Body_N`
- `T_GIA_BloodAxeChieftain_A01_Body_ORM`
- `T_GIA_BloodAxeChieftain_A01_Gear_BC`
- `T_GIA_BloodAxeChieftain_A01_Gear_N`
- `T_GIA_BloodAxeChieftain_A01_Gear_ORM`
- `T_GIA_BloodAxeChieftain_A01_HairFur_BC`
- `T_GIA_BloodAxeChieftain_A01_HairFur_N`
- `T_GIA_BloodAxeChieftain_A01_HairFur_ORM`
- Optional future `T_GIA_BloodAxeChieftain_A01_E` only for a separately approved emissive variant

Expected socket dependencies from the Giant base package, referenced only for future validation:

- `hand_r_weapon`
- `hand_l_offhand`
- `hand_r_twohand_grip`
- `hand_l_twohand_grip`
- `back_large_weapon`
- `back_shield`
- `belt_tool_l`
- `belt_tool_r`
- `head_hair_ornament`
- `chest_talisman`

Candidate future Blood Axe references, not authorized sockets in this package:

- `back_quiver`
- `belt_trophy_l`
- `belt_trophy_r`
- `side_hook_l`
- `side_hook_r`
- `harness_back_anchor`
- `harness_chest_anchor`
- `harness_belt_anchor`
- `banner_carry`

Final socket names, transforms, weapon attachments, trace markers, VFX hooks, cloth setup, physics bodies, and Blueprint behavior require separate Unreal/animation/gameplay approval.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/characters/SK_GIA_BloodAxeChieftain_A01/`
- Production package: `docs/assets/characters/SK_GIA_BloodAxeChieftain_A01/PRODUCTION_PACKAGE.md`
- Related base body package: `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md`
- Related armory kit: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- Related closure/readiness doc: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PACKAGE_CLOSURE_AND_DCC_READINESS.md`
- Planned future Unreal folder after approval only: `/Game/Aerathea/Characters/Giants/BloodAxe/Chieftain/`

Planned future names:

- Skeletal Mesh: `SK_GIA_BloodAxeChieftain_A01`
- Skeleton: inherit from the future approved Giant base skeleton convention; do not create a new skeleton assumption here.
- Physics Asset: `PHYS_GIA_BloodAxeChieftain_A01`, only after implementation approval.
- Animation Blueprint: `ABP_GIA_BloodAxeChieftain_A01`, only after animation/runtime approval.
- Material Instance: `MI_GIA_BloodAxeChieftain_A01`
- Shared material references: `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeScorchedLeather_A01`, `MI_GIA_BloodAxeRedCloth_A01`, `MI_GIA_BloodAxeBoneTrophy_A01`

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, FBX exports, Unreal Content assets, runtime source, tools, validators, startup-scene actors, copied source concepts, global index entries, task-board edits, backlog edits, bootstrap edits, final approval captures, or external concept-folder edits from this task.

## Docs-Only Guardrails

- Stop before final named lore lock.
- Stop before combat abilities.
- Stop before boss mechanics.
- Stop before wearable skeletal fit.
- Stop before cloth/physics.
- Stop before animation timing.
- Stop before final visual approval.
- Stop before first DCC target selection.
- Stop before DCC source creation, Blender source creation, sculpt creation, retopo, UVs, bakes, FBX export, Unreal Content import, material graph authoring, runtime source changes, validator creation, startup-scene placement, or external source concept copying.
- Stop if Blood Axe red-black raider language starts replacing neutral/civilized Giant stoneworker, cave-town, or highland nomad culture.
- Stop if the package appears to require changing the validated `SK_GIA_Base_A01` scale lock, skeleton assumptions, or socket assumptions.
- Stop if trophies, skulls, red cloth, chains, straps, gore, rivets, cracks, or scratches become dense enough to hurt mid-poly MMO readability.

## Approval Gates

- Lead approval is required before `SK_GIA_BloodAxeChieftain_A01` is selected as a first DCC target.
- Visual approval is required before final helm shape, faceguard shape, shoulder mass, trophy density, red cloth placement, weapon pairing, or leader silhouette is locked.
- Culture approval is required if Blood Axe visual language starts bleeding into neutral/civilized Giant packages.
- DCC approval is required before creating meshes, Blender sources, sculpt files, retopo files, UVs, bakes, collision proxies, proof renders, or exports.
- Unreal approval is required before importing skeletal meshes, material instances, textures, LODs, physics assets, sockets, validators, Blueprints, or startup-scene actors.
- Wearable-fit approval is required before claiming armor, helm, harness, belt, greaves, quiver, weapon carry, or trophy attachments fit either Giant baseline.
- Cloth and physics approval is required before adding moving cloth strips, capes, banner cloth, swinging chains, dangling trophies, fur secondary motion, simulated cloth, or physics bodies.
- Animation approval is required before authored locomotion, weapon hold poses, attacks, bow draw, hit reactions, death, montage timing, or animation Blueprint logic.
- Gameplay approval is required before combat abilities, boss mechanics, encounter phases, damage values, hit zones, weak points, loot rules, objective logic, command aura behavior, projectile behavior, or interactable behavior.
- Source-storage approval is required before copying, embedding, editing, or committing any external source concept.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, bootstrap, or source asset file.
- `SK_GIA_BloodAxeChieftain_A01` is a hostile Blood Axe Giant leader production package, not a finalized named boss encounter.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit and unchanged: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", with approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- The character preserves Giant body mass, shoulder breadth, heavy hands, sturdy legs, large feet, and towering scale instead of becoming a scaled normal humanoid.
- Primary forms are broad helm/faceguard mass, chest/spaulder armor, harness, belt/tassets, greaves, red cloth blocks, and sparse trophies, not micro-detail.
- Materials align with blackened iron, dark steel, scorched leather, hide/fur, oxide red cloth/paint, soot, ash, grime, and sparse aged bone/horn trophies.
- `MI_GIA_BloodAxeReforgedMetal_A01` is referenced as the core metal dependency.
- Neutral/civilized Giant stoneworker materials, blue-gray cave-town identity, warm hearth language, and restrained rune accents are excluded from the baseline.
- Default emissive, forge heat, ritual glow, shamanic glow, faction aura, animated material states, cloth, physics, and final socket transforms are not claimed.
- Texture maps include `BC`, `N`, `ORM`, and optional future `E` only behind approval.
- Triangle budget, material slot target, LOD0-LOD3 plan, collision planning, animation scope, Unreal import planning, folder naming, docs-only guardrails, approval gates, and quality checklist are included.
- Package does not claim skeletal fit, authored animation, animation timing, cloth simulation, physics setup, combat abilities, boss mechanics, final named lore lock, final visual approval, first DCC target selection, or implementation completion.
