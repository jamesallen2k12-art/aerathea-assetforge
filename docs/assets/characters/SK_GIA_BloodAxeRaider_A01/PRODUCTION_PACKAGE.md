# SK_GIA_BloodAxeRaider_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeRaider_A01`
- Asset type: Skeletal Mesh character production planning package
- Parent kit: `KIT_GIA_BloodAxeWarband_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Planning row: common raider visual baseline
- Source routing: `docs/assets/intake/ACIQ-P02_01_GIANT_BLOODAXE_SLATE.md`
- Primary source references: `BloodAxeGiantMale.png`, `BloodAxeGiantMale2.png`, `GiantBloodAxeMale3.png`, `GiantBloodAxeMale4.png`, `GiantFemaleBloodAxe1.png`, and `GiantBloodAxeMaleandFemale.png`
- Armory planning dependencies: `SK_GIA_BloodAxeRaiderChest_A01`, `SK_GIA_BloodAxeHarness_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, `SK_GIA_BloodAxeGreaves_A01`, optional `SM_GIA_BloodAxeTrophyHelm_A01`, and future attached Blood Axe weapon props only after separate approval
- Status: docs-only production package; no DCC, FBX, Unreal Content, runtime source, startup placement, source concept copy, wearable-fit finalization, animation timing, gameplay behavior, or final visual approval is created or claimed

`SK_GIA_BloodAxeRaider_A01` defines the repeatable hostile Blood Axe Giant raider visual baseline: a towering Giant body in brutal red-black raider gear, broad blackened armor plates, scorched leather harnessing, rough hide, soot, ash, sparse dry trophies, and large readable Blood Axe color blocks. This package is for visual production planning only. It does not make the raider the default Giant culture, does not select the raider as the first character build target, and does not finalize a gameplay class.

Blood Axe language must stay separated from neutral/civilized Giant culture. Civilized Giants remain remote mountain stoneworkers and highland people; this package covers the hostile Blood Axe raider sub-faction marked by enslavement raids, blood-ritual reputation, rough camps, trophy armor, red banners, blackened iron, and intimidation silhouettes.

## Gameplay Purpose

This package defines a visual role only: the common hostile Blood Axe Giant body/outfit read for later concept sheets, character variant planning, warband composition review, and future DCC handoff after approval.

Allowed planning use:

- Establish the repeatable raider silhouette for male and female Giant baselines.
- Align armor, harness, belt, greaves, trophy density, skin treatment, hair/fur treatment, and red Blood Axe accents.
- Document future attachment expectations for Giant-scale weapons and gear without choosing a final loadout.
- Provide a production reference for readable hostile Giant identity at MMO camera distance.

Out of scope:

- No AI behavior, combat stats, encounter role, abilities, damage values, projectile rules, shield rules, patrol logic, spawn logic, loot rules, crafting rules, economy data, inventory behavior, or final troop class.
- No DCC mesh, source asset folder, FBX export, Unreal import, Blueprint, validator, startup actor, or runtime implementation.
- No final wearable skeletal fit, socket transform, animation timing, montage, cloth simulation, physics setup, or visual approval.

## Silhouette Notes

The raider should read first as a Giant, second as Blood Axe, and third as a common repeatable hostile. The silhouette must be massive, upright, broad, and readable, not a normal humanoid scaled upward.

Primary body read:

- Towering Giant height, heavy neck, broad shoulders, thick torso, large hands, wide pelvis, huge calves, and heavy feet.
- Male baseline: wider chest and heavier shoulder/neck mass.
- Female baseline: still massive and dangerous, with slightly narrower torso/hip balance only within the approved Giant range; do not humanize or shrink the body read.
- Face and head should use rough mountain exposure, heavy brow, strong jaw, scars, ash, and controlled war paint. Hair, braids, beard, fur, or shaved sections may support the hostile read but must not create dense strand clutter.

Blood Axe outfit read:

- Upper body: broad chest plate or raider spaulder mass, one heavier asymmetrical shoulder, large reforged metal planes, wide scorched-leather straps, and a few oversized rings or hooks.
- Torso/back: harness bands frame the Giant mass rather than covering it with dangling trophies.
- Waist/hips: thick trophy belt, broad tassets, large central buckle or trophy plate, and red cloth blocks that remain secondary to the hip mass.
- Lower body: wide greaves, blunt knee guards, broad ankle collars, and heavy boot/sabaton armor that preserves Giant calf and foot scale.
- Trophy language: use a few large dry bone, horn, broken shield, or cracked weapon trophies. No graphic gore, wet blood, trophy curtains, or tiny charm fields.
- Weapon read: concept art may show one Giant-scale carried weapon for silhouette context, but final loadout and attachment are not locked by this package.

Model as future real geometry only when approved:

- Body forms, head and hand forms, major armor plates, spaulders, harness straps, belt/tasset blocks, greave shells, large rings, large buckles, broad red cloth panels, and a few major trophy shapes.

Texture or normal-map:

- Tiny rivets, fine scratches, leather pores, stitch rows, small red paint chips, soot speckles, small bone cracks, hammered pitting, cloth weave, and minor scars.

Avoid:

- Neutral/civilized Giant blue-gray stoneworker motifs, warm hearth identity, refined masonry symbols, restrained blue runes, and civic craft ornament.
- Dense spikes, dense skull strings, excessive chains, readable text, franchise-like symbols, gore escalation, or over-detailed photorealism.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Feet should sit at world origin for future skeletal planning unless a later DCC/export owner approves a different convention.

This package does not alter `SK_GIA_Base_A01` scale and does not claim a completed male or female wearable fit. Armor thickness, trophy pieces, hair, helmets, weapons, and back gear may extend the silhouette, but they must not redefine the measured Giant body height or require a new race scale.

Future scale review targets:

- Chest/spaulder modules must preserve shoulder breadth, neck clearance, and upper-arm movement space.
- Harness straps and rings must be Giant-scale, with broad bands rather than thin humanoid straps.
- Belt and tassets must preserve pelvis, abdomen, thigh, and stride readability.
- Greaves and boots must preserve calf width, ankle mass, heel width, toe-box breadth, and foot length.
- Headgear, if used, must clear brow, jaw, hair, neck, and shoulder mass before any wearable claim.
- Attached weapons must be validated against Giant hand, back, belt, and two-handed grip assumptions in later tasks.

## Materials and Color Palette

Primary Blood Axe materials:

- Weathered Giant skin with ash, scars, sun and mountain exposure, dry grime, and broad red war paint.
- Blackened iron, dark steel, and reforged stolen metal with broad hammer marks and worn edges.
- Scorched leather, rough hide, rawhide wraps, fur pads, sinew cord, and thick strap construction.
- Torn oxide-red cloth, red paint slashes, and dull red warning marks as sub-faction identifiers.
- Sparse dry bone, horn, tooth, broken shield, or cracked weapon trophies.
- Soot, ash, mud, oil-dark grime, and rubbed metal edge highlights.

Suggested palette:

- Weathered skin: `#7A5F4A` to `#A88463`, varied by later ethnicity and exposure approval.
- Ash and grime: `#0B0A09` to `#403025`.
- Blackened iron: `#151719` to `#2A2C2E`.
- Worn dark steel: `#555A5C` to `#787B78`.
- Scorched leather: `#241611` to `#4A2E20`.
- Rough hide/fur: `#2A2018` to `#6B523D`.
- Oxide red cloth/paint: `#5F1513` to `#8B211B`.
- Old bone/horn: `#A69578` to `#D0B98C`.

No default emissive is approved for the raider baseline. Forge heat, ritual glow, shamanic glow, glowing eyes, animated material states, or VFX hooks require a separate approved variant and must not be assumed here.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SK_GIA_BloodAxeRaider_A01` for the world of Aerathea. The design should emphasize a repeatable hostile Blood Axe Giant raider visual baseline, towering validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" callouts, massive readable body proportions, broad shoulders, heavy hands and feet, blackened reforged iron plates, asymmetrical raider spaulders, scorched leather harness straps, thick trophy belt and broad tassets, heavy greaves and sabaton-like boot armor, sparse dry bone and horn trophies, rough hide and fur, ash, soot, deep oxide-red cloth and war paint, hostile Blood Axe sub-faction identity, and separation from neutral/civilized Giant stoneworker culture. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a character production sheet with male and female front, side, back, and three-quarter views, armor-layer callouts, material swatches, scale bars, optional non-final carried weapon silhouette, LOD notes, and approval-gate notes on a clean background. Avoid copying any existing franchise, avoid graphic gore, avoid making Blood Axe language the default Giant culture, avoid final gameplay class diagrams, avoid AI/combat stat/ability/loot/patrol/spawn callouts, avoid wearable-fit finalization claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This package is a docs-only modeling plan. It does not authorize DCC source creation, mesh work, sculpting, retopo, UVs, bakes, FBX export, Unreal import, runtime files, or source concept movement.

Future modeling should start from the approved Giant base body and layer Blood Axe gear over it:

- Preserve Giant anatomy before outfit detail: head mass, neck, shoulders, chest, back, hands, pelvis, legs, calves, ankles, and feet remain the primary forms.
- Treat male and female baselines as fit targets, not a single completed shared wearable until later review proves it.
- Build the raider as a modular dressed character: body, head/hair/fur, upper armor, harness, belt/tassets, greaves/boots, and optional headgear.
- Reuse the armory planning language from `SK_GIA_BloodAxeRaiderChest_A01`, `SK_GIA_BloodAxeHarness_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, and `SK_GIA_BloodAxeGreaves_A01`.
- Keep weapon props separate wherever practical. Do not bake double axe, cleaver, hammer, spear, bow, banner, or quiver geometry into the core raider body unless a later approval explicitly asks for a posed display mesh.
- Keep shoulder, elbow, wrist, neck, jaw, spine, pelvis, thigh, knee, ankle, and foot deformation zones clean and low-clutter.
- Use asymmetry through one heavier spaulder, uneven plate repair, red cloth placement, scars, soot, and trophy placement without losing the repeatable baseline read.
- Keep dangling cloth, chains, trophies, and straps short and mostly rigid until cloth or physics approval exists.

Model real geometry for:

- Major body forms, head features, broad armor plates, spaulders, harness straps, belt and tasset panels, greave shells, large rings, large buckles, major bone/horn trophies, large cloth blocks, and hair/fur clumps.

Use textures, normals, or masks for:

- Tiny rivets, stitch rows, fine scratches, dense pitting, leather pores, cloth weave, skin pores, small scars, hairline bone cracks, minor hammer marks, soot speckles, and small red paint flakes.

Do not model:

- Dense rivet fields, many small skulls, gore ropes, tooth curtains, dozens of dangling charms, micro chains, readable text, or intricate ornaments that would fail at MMO camera distance.

## Texture and Material Notes

Texture outputs for a future approved build should use standard Aerathea maps:

- `T_GIA_BloodAxeRaider_A01_Body_BC`
- `T_GIA_BloodAxeRaider_A01_Body_N`
- `T_GIA_BloodAxeRaider_A01_Body_ORM`
- `T_GIA_BloodAxeRaider_A01_Outfit_BC`
- `T_GIA_BloodAxeRaider_A01_Outfit_N`
- `T_GIA_BloodAxeRaider_A01_Outfit_ORM`
- `T_GIA_BloodAxeRaider_A01_Gear_BC`
- `T_GIA_BloodAxeRaider_A01_Gear_N`
- `T_GIA_BloodAxeRaider_A01_Gear_ORM`
- Optional future approval-gated `T_GIA_BloodAxeRaider_A01_E`

Recommended material families:

- `MI_GIA_BloodAxeRaiderSkin_A01` for Giant skin, scars, ash, war paint, and non-emissive eye treatment.
- `MI_GIA_BloodAxeHairFur_A01` for hair, beard, fur pads, and rough hide/fur blend areas.
- `MI_GIA_BloodAxeReforgedMetal_A01` for blackened iron, dark steel, edge wear, and hammered plate surfaces.
- `MI_GIA_BloodAxeScorchedLeather_A01` for harness straps, wraps, belt cores, and hide backing.
- `MI_GIA_BloodAxeRedCloth_A01` for torn red cloth only if merged masks cannot keep the read clear.
- `MI_GIA_BloodAxeBoneTrophy_A01` for sparse dry trophies.

Material slot target for a full repeatable raider:

- 3-5 slots total for body, hair/fur, outfit/leather/cloth, armor/metal, and bone/trophy as needed.
- Attached weapon props use their own approved material plans and do not count against the character material target.
- Avoid one-off material slots for every strap, trophy, paint mark, chain, or grime layer.

Texture resolution target:

- 2K sets for repeatable raider body/outfit/gear.
- 4K only if a future named hero, chieftain, boss-adjacent close-up, or cinematic variant is separately approved.

Packed `ORM` guidance:

- R: ambient occlusion around plate overlaps, strap compression, under-spaulder shadows, belt/tasset overlaps, greave joints, trophy anchors, hair clumps, and large skin folds.
- G: high roughness for soot, skin, leather, bone, fur, and matte blackened metal; slightly lower roughness on rubbed steel edges and hand-contact metal.
- B: metallic only for iron, steel, buckles, rings, chain links, plates, and weapon hardware.

Texture readability requirements:

- Use broad red blocks and clear value separation so the character does not collapse into one black shape.
- Keep skin, armor, leather, red cloth, and trophy materials readable from a gameplay camera.
- Keep war paint dry and symbolic, not wet blood.
- Avoid readable text, franchise-like symbols, loot colors, rank icons, or gameplay-state material masks.

## Triangle Budget

`SK_GIA_BloodAxeRaider_A01` is a repeatable large hostile character, not a named boss. Budget should stay aggressive enough for warband use.

LOD0 target:

- Full dressed raider, excluding separate carried weapon props: 58k-74k tris.
- Hard cap: 78k tris only if male/female fit review requires extra broad armor support or hair/fur mass.
- Material slots: 3-5 for the character, excluding attached props.
- Texture sets: 2K standard.

Budget distribution guidance:

- Base Giant body, head, hands, feet, and facial forms: 28k-34k tris.
- Hair, beard, fur pads, and hide clumps: 4k-8k tris.
- Chest, spaulders, harness, belt, tassets, greaves, and boots: 20k-28k tris.
- Rings, buckles, sparse trophies, cloth blocks, and large silhouette accents: 6k-10k tris.

Use individual armory child budgets for separate weapon, banner, quiver, or display props. Do not duplicate those props into the raider mesh unless a later approved display-only task requires it.

Do not spend geometry on tiny rivets, dense chains, fine stitches, pitting, micro scratches, small teeth, repeated small charms, or surface-only scars.

## LOD Plan

All future important raider meshes require LOD0-LOD3.

- LOD0: 58k-74k tris target. Full Giant body, face forms, hands, feet, hair/fur clumps, large armor plates, spaulders, harness, belt/tassets, greaves, major rings, sparse trophies, red cloth blocks, and primary Blood Axe material separation.
- LOD1: 36k-48k tris target. Reduce minor bevels, small strap loops, hair subdivisions, small buckle edges, secondary trophy cuts, cloth fold geometry, under-spaulder detail, and non-silhouette armor support.
- LOD2: 22k-32k tris target. Simplify back-side detail, merge small armor overlaps, reduce finger/face support loops where safe, flatten minor trophy forms, collapse small straps into texture, and simplify boot/tasset undercuts.
- LOD3: 10k-17k tris target. Preserve height, shoulder width, head silhouette, hand/foot scale, waist/hip mass, red/black Blood Axe color blocks, and the major armor outline.

LOD reduction order:

1. Tiny rivets, stitches, scratches, pitting, and small skin pores.
2. Small strap loops, small rings, minor buckles, and little cloth tears.
3. Small trophy chips, tiny bone fragments, and secondary red paint geometry.
4. Under-spaulder, inner belt, underside boot, and back-side non-visible details.
5. Hair/fur subdivision and secondary clumps.
6. Non-silhouette plate bevels and small support loops.
7. Only then reduce the primary Giant body, head, shoulder width, hands, feet, broad armor masses, and Blood Axe color read.

Never destroy the validated Giant scale read or broad hostile raider silhouette before removing small detail.

## Collision Notes

No collision is authored or approved in this docs-only package.

Future collision planning:

- Use Giant-tuned character capsule assumptions inherited from `SK_GIA_Base_A01`, with review against the female 442 cm / 14'6" and male 470 cm / 15'5" baselines.
- Physics asset should remain simplified around pelvis, spine, chest, head, upper arms, forearms, hands, thighs, calves, and feet.
- Worn armor, harness, trophies, belts, tassets, greaves, and headgear should normally rely on the owning character capsule and simplified physics asset, not per-strap or per-trophy collision.
- Attached weapons, quivers, banners, or shields should use their own later-approved display or trace planning where applicable.
- Preview bounds may be documented in a later review task, but this package does not author them.

Not approved here:

- Combat hit zones, weak points, trace arcs, damage volumes, projectile collision, shield volumes, aura zones, nav blockers, spawn blockers, pickup collision, loot interaction, destructible behavior, or trigger volumes.

## Animation Notes

No animation assets, animation timing, montage lists, gait edits, IK, physics setup, cloth simulation, secondary motion, AI states, or behavior trees are authored or approved by this package.

Future approval-gated visual clearance checks may include:

- Heavy Giant idle and breathing posture.
- Walk, run, turn-in-place, and broad stance readability.
- Shoulder raise, elbow bend, wrist rotation, neck turn, jaw clearance, hip twist, knee bend, ankle flex, and foot contact review.
- Two-handed weapon hold, one-handed carry, back carry, belt carry, bow/quiver reach, and banner carry poses only as visual clearance checks.
- Chest armor, harness, trophy belt, tassets, greaves, headgear, hair/fur, and sparse trophies checked for clipping.

Rigid gear should be preferred for the first approved wearable pass. Any loose cloth strips, swinging chains, dangling trophies, hair physics, fur physics, or simulated secondary motion requires separate approval and validation.

No motion note in this package defines a final combat move, ability, patrol state, encounter behavior, or animation timing.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset is created or authorized by this task.

Planned Unreal asset:

- Asset name: `SK_GIA_BloodAxeRaider_A01`
- Asset type: Skeletal Mesh character candidate
- Planned folder: `/Game/Aerathea/Characters/Giants/BloodAxe/Warband/`
- Planned material folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Planned texture folder: `/Game/Aerathea/Textures/Giants/BloodAxe/Characters/Raider_A01/`
- Import scale: centimeter-authored source; Unreal import scale 1.0 only after future DCC/export validation
- Pivot: feet at world origin / Giant base body origin unless the future export convention says otherwise
- Forward orientation: match the approved Giant base import convention in a later implementation task
- Collision: Giant character capsule and simplified physics asset planning only; no separate gear collision by default
- LODs: LOD0-LOD3 required before production import approval
- Material slots: target 3-5 for the character, excluding attached props
- Nanite: off by default for skeletal character use unless a future platform/performance review approves a specific exception

Planned texture list:

- `T_GIA_BloodAxeRaider_A01_Body_BC`
- `T_GIA_BloodAxeRaider_A01_Body_N`
- `T_GIA_BloodAxeRaider_A01_Body_ORM`
- `T_GIA_BloodAxeRaider_A01_Outfit_BC`
- `T_GIA_BloodAxeRaider_A01_Outfit_N`
- `T_GIA_BloodAxeRaider_A01_Outfit_ORM`
- `T_GIA_BloodAxeRaider_A01_Gear_BC`
- `T_GIA_BloodAxeRaider_A01_Gear_N`
- `T_GIA_BloodAxeRaider_A01_Gear_ORM`
- Optional future approval-gated `T_GIA_BloodAxeRaider_A01_E`

Socket and attachment planning:

- Inherit Giant base socket policy where applicable: `hand_r_weapon`, `hand_l_offhand`, `hand_r_twohand_grip`, `hand_l_twohand_grip`, `back_large_weapon`, `back_shield`, `belt_tool_l`, `belt_tool_r`, `head_hair_ornament`, and `chest_talisman`.
- Future Blood Axe references may include `back_quiver`, `belt_trophy`, `banner_carry`, `weapon_trace_start`, and `weapon_trace_end`, but no new socket names, transforms, or attachment rules are authorized by this package.

Animation list:

- None authored or finalized here.
- Future locomotion and carry-pose compatibility must be approved by a separate animation or implementation task.

Blueprint behavior:

- None.
- No AI, combat, encounter, patrol, spawn, loot, crafting, economy, interaction, pickup, or equipment behavior is defined.

Performance notes:

- Preserve primary Giant scale and Blood Axe silhouette before adding gear detail.
- Keep material slots low for repeated warband use.
- Keep baseline emissive, particles, dynamic lights, and complex collision absent.
- Validate the raider at MMO camera distance before any final visual approval.

## Folder and Naming Recommendation

Docs:

- Package folder: `docs/assets/characters/SK_GIA_BloodAxeRaider_A01/`
- Package file: `docs/assets/characters/SK_GIA_BloodAxeRaider_A01/PRODUCTION_PACKAGE.md`

Related docs:

- Parent warband package: `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/PRODUCTION_PACKAGE.md`
- Warband child intake: `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/CHILD_ASSET_INTAKE.md`
- Armory package: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- Related gear packages: `docs/assets/characters/SK_GIA_BloodAxeRaiderChest_A01/`, `docs/assets/characters/SK_GIA_BloodAxeHarness_A01/`, `docs/assets/characters/SK_GIA_BloodAxeTrophyBelt_A01/`, and `docs/assets/characters/SK_GIA_BloodAxeGreaves_A01/`

Planned future naming after approval only:

- Skeletal Mesh: `SK_GIA_BloodAxeRaider_A01`
- Material Instance: `MI_GIA_BloodAxeRaider_A01`
- Optional body material: `MI_GIA_BloodAxeRaiderSkin_A01`
- Optional display/static review mesh only if separately approved: `SM_GIA_BloodAxeRaider_Display_A01`

Planned future Unreal folders after approval only:

- Character: `/Game/Aerathea/Characters/Giants/BloodAxe/Warband/`
- Gear dependencies: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`
- Weapons: `/Game/Aerathea/Weapons/Giants/BloodAxe/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/Characters/Raider_A01/`

Do not add `Content/Aerathea`, `SourceAssets`, Blender files, FBX exports, Unreal Content assets, runtime source, validators, startup-scene actors, copied concept files, global index entries, task-board edits, backlog edits, bootstrap edits, or external source edits from this task.

## Approval and Stop Gates

- Lead approval is required before selecting `SK_GIA_BloodAxeRaider_A01` as a first Blood Axe character build target.
- Visual approval is required before locking final raider silhouette, male/female presentation, armor density, red cloth placement, trophy density, head treatment, hair/fur treatment, or optional weapon display.
- Culture approval is required if Blood Axe raider language starts replacing neutral/civilized Giant stoneworker or highland nomad culture.
- DCC approval is required before creating source folders, Blender files, sculpt files, retopo files, UVs, bakes, LOD sources, collision proxies, proof renders, or FBX exports.
- Unreal approval is required before importing Skeletal Meshes, Static Meshes, material instances, textures, physics assets, LODs, Blueprints, validators, or startup actors.
- Wearable-fit approval is required before claiming the chest, harness, belt, greaves, headgear, weapons, quivers, or trophies fit either Giant baseline, clear motion, deform correctly, or share a final skeletal contract.
- Attachment approval is required before authoring final socket names, socket transforms, carry offsets, weapon placements, quiver placements, banner placements, or trophy placements.
- Animation approval is required before authoring locomotion edits, attack motion, carry timing, bow draw/release, banner movement, cloth motion, physics motion, or montage timing.
- Source-storage approval is required before copying, moving, editing, embedding, committing, or otherwise relocating any external source concept image.
- Gameplay approval is required before defining AI, combat stats, encounter role, abilities, damage, projectile behavior, trace behavior, shield behavior, aura effects, loot, crafting, economy, inventory, patrol paths, spawn rules, interaction, pickup behavior, or final troop class.
- Stop if the package starts to imply final visual approval, final wearable skeletal fit, implementation completion, source concept movement, or gameplay class finalization.

## Quality Gate Checklist

- `SK_GIA_BloodAxeRaider_A01` is documented as a docs-only production package.
- Blood Axe remains a hostile Giant sub-faction, not the default Giant culture.
- Neutral/civilized Giant stoneworker, cave-town, hearth, blue-gray masonry, and restrained rune language are excluded from the raider baseline.
- The raider is a repeatable hostile Giant visual baseline, not a finalized gameplay class or first build target.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Silhouette preserves Giant body mass, height, shoulders, hands, pelvis, calves, ankles, and feet before gear detail.
- Materials use weathered skin, ash, scars, blackened iron, dark steel, reforged metal, scorched leather, rough hide, fur, oxide-red cloth/paint, soot, grime, and sparse dry trophies consistently.
- Emissive is absent by default and approval-gated for any later ritual, forge, shamanic, eye, or VFX variant.
- Tiny rivets, scratches, pitting, stitching, cloth weave, small scars, and minor paint chips are assigned to texture, normals, or masks.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision planning, animation limits, Unreal import planning, folder naming, and approval gates are included.
- Package does not claim DCC work, FBX export, Unreal import, runtime code, validators, startup placement, copied source concepts, final visual approval, final wearable fit, final sockets, animation timing, AI, combat stats, abilities, loot, crafting, economy, patrol logic, spawn logic, or encounter behavior.
- Source concepts remain external and are not copied, moved, edited, embedded, or committed by this package.
- The package is useful for later DCC/Unreal handoff without requiring reinterpretation of Blood Axe culture separation, Giant scale, trophy-density limits, or docs-only guardrails.
