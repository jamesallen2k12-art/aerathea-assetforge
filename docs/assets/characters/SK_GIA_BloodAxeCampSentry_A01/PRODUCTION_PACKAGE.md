# SK_GIA_BloodAxeCampSentry_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeCampSentry_A01`
- Asset type: Skeletal Mesh character production package / hostile Blood Axe Giant camp perimeter visual candidate
- Parent scale dependency: `SK_GIA_Base_A01`
- Parent kit: `KIT_GIA_BloodAxeWarband_A01`
- Related camp kit: `KIT_GIA_BloodAxeCamp_A01`
- Related armory kit: `KIT_GIA_BloodAxeArmory_A01`
- Related visual dependencies: `SM_GIA_BloodAxeHookSpear_A01`, `SM_GIA_BloodAxeLongbow_A01`, `SM_GIA_BloodAxeLongbow_A02`, `SM_GIA_BloodAxeLongbow_A03`, `KIT_GIA_BloodAxeShortbows_A01`, `KIT_GIA_BloodAxeQuivers_A01`, `SK_GIA_BloodAxeHarness_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, `SK_GIA_BloodAxeGreaves_A01`, and `SM_GIA_BloodAxeWarBanner_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, source asset, runtime, validator, startup placement, final visual approval, or first DCC target selection is included.

`SK_GIA_BloodAxeCampSentry_A01` defines the visual direction for a Blood Axe Giant perimeter sentry: a hostile gate-watch figure built around validated Giant scale, harsh camp utility, lighter but brutal armor, spear or bow readability, rough hide and scorched leather, soot-dark metal, red warning cloth, and sparse non-graphic trophy marks. The sentry is intended to visually frame Blood Axe camp gates, watch points, barricades, shelter edges, and perimeter compositions.

This package is not a gameplay package. It does not define patrol paths, AI perception, aggro radii, encounter scripting, spawn rules, AI classes, combat stats, abilities, loot, projectile behavior, trap behavior, cover behavior, nav behavior, or camp ownership logic.

Blood Axe must remain a hostile Giant sub-faction. Red-black raider materials, trophy markers, rough hide, ash, soot, and territorial warning language must not replace neutral/civilized Giant culture, which remains tied to mountain stonework, hidden cave towns, highland settlements, warm hearth craft, and restrained rune or storm accents.

## Gameplay Purpose

The purpose is visual role planning only: make a Blood Axe camp perimeter read clearly as guarded by hostile Giant sentries at MMO camera distance. This package can support later concept sheets, DCC target discussions, gate/watch composition reviews, and character/gear dependency planning after separate approval.

Allowed visual planning uses:

- Establish a camp sentry silhouette for gate, watch platform, barricade, and perimeter dressing compositions.
- Coordinate the sentry body, outfit, spear/bow read, quiver or tool carry, and red warning cloth with existing Blood Axe armory and camp packages.
- Preserve the Giant scale lock while defining a repeatable non-hero warband row.
- Provide future import, material, LOD, collision, and approval expectations without creating assets.

Out of scope:

- Patrol paths, patrol loops, AI perception, sight cones, hearing ranges, aggro radii, alert states, spawn rules, encounter scripting, wave composition, guard posts as gameplay interactables, combat stats, attacks, abilities, projectile logic, loot, inventory, faction reputation, camp capture, or objective behavior.
- Final wearable skeletal fit, cloth simulation, physics setup, socket transforms, animation timing, montage timing, final pose lock, final weapon lock, final visual approval, DCC source creation, FBX export, Unreal import, runtime source, startup placement, or source concept movement.

## Silhouette Notes

Primary silhouette: a towering Blood Axe Giant watch figure with a grounded gate-guard stance, broad shoulders, heavy hands, thick neck, sturdy legs, large feet, a practical watch helm or brow wrap, one strong shoulder or chest armor read, broad belt and greaves, and one clear perimeter tool or weapon shape.

Sentry-specific silhouette goals:

- Read as a perimeter guard, not a chieftain, shaman, hunter leader, or neutral Giant worker.
- Preserve the Giant body mass before adding gear: height, shoulder breadth, long arms, heavy hands, thick torso, powerful legs, and large feet must remain readable.
- Keep armor lighter than a chieftain but harder-edged than a pure hunter: rough chest strap, one reinforced pauldron, heavy bracers, shin guards, belt plates, and camp-worn boots.
- Include one optional visual carry profile: hook spear or long pole silhouette, bow and quiver silhouette, or shortbow scout profile. This package does not select a final weapon or combat behavior.
- Use gate-watch language through pose-neutral forms: lifted head, squared shoulders, high sightline, watch mantle, horn tag, red cloth warning strip, belt token, or signal marker.
- Keep red cloth in broad readable accents at the shoulder, belt, quiver, spear wrap, or back marker. Do not make the whole character red.
- Use sparse trophies only: one or two horn, bone, broken shield, tooth, or dry marker shapes. Avoid dense skull curtains, graphic remains, fresh gore, or trophy clutter.
- Avoid elite leader silhouettes: no crown-scale trophy helm, no chieftain mantle, no major shaman staff, no large ritual glow, no oversized command banner attached to the character by default.

Model real geometry for the main body, large armor plates, broad straps, major bracers/greaves, large belt plates, optional spear/bow/quiver silhouettes, large buckles, big hide panels, and sparse trophy shapes. Use texture and normal maps for scratches, soot, small stitching, leather pores, small red paint chips, fine pitting, tiny rivets, cloth weave, and minor bone grain.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock without alteration:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Feet at world origin for future skeletal work unless a later approved Giant implementation convention says otherwise.

Planning target:

- Default sentry review should use the 470 cm male baseline for gate and perimeter scale checks.
- The 442 cm female baseline remains required for future variant review and should not be treated as a different race scale.
- This package does not lock final gender, body variant, individual face, final weapon, final stance, or wearable skeletal fit.

Scale and clearance dependencies:

- Gate, watch platform, barricade, shelter, and path scale should remain routed through `KIT_GIA_BloodAxeCamp_A01`.
- Spear, bow, quiver, belt, harness, and greave dimensions should inherit from existing Blood Axe armory planning when selected by a later task.
- Helmet, brow wrap, shoulder armor, quiver straps, bow/spear carry, belt tokens, tassets, greaves, and boots must clear Giant head, neck, shoulder, elbow, pelvis, thigh, knee, ankle, and foot volumes before implementation claims.
- Normal humanoid compatibility is not required. Smallfolk should read as trespassers near this character and its camp modules.

## Materials and Color Palette

Primary Blood Axe sentry materials:

- Weathered Giant skin with ash, sun exposure, scars, dull war paint, and camp grime.
- Blackened iron, dark steel, and rough reforged metal on bracers, shoulder plate, belt plates, buckles, spear hardware, or bow fittings.
- Scorched leather, rough hide, dark fur pads, rawhide wraps, sinew cord, and heavy utility straps.
- Dull Blood Axe red cloth, dirty red wraps, red warning paint, and worn red ties as sub-faction identifiers.
- Bone, horn, teeth, broken shield fragments, or dry territory tokens used sparingly and non-graphically.
- Soot, ash, mud, charcoal smears, oil-dark recesses, and broad hand-painted wear.

Suggested palette:

- Blackened iron: `#151719` to `#2A2C2E`
- Worn dark steel: `#555A5C` to `#787B78`
- Dull Blood Axe red: `#5A1412` to `#8A211A`
- Scorched leather: `#241611` to `#4A2E20`
- Rough hide and fur: `#1D1511` to `#5B4632`
- Old bone and horn: `#A69578` to `#D0B98C`
- Soot, ash, and mud: `#0B0A09` to `#4A3A2B`

No default emissive is approved. Forge heat, ritual glow, shamanic glow, storm glow, faction aura, glowing eyes, alert-state color changes, or animated material states require a separate approval-gated package.

Avoid neutral/civilized Giant material language: carved blue-gray stoneworker motifs, warm civic hearth identity, clean masonry symbols, restrained blue runes, terrace craft, and peaceful highland settlement language.

## Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_GIA_BloodAxeCampSentry_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant camp perimeter sentry, validated Giant scale with female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", towering gate-watch silhouette, broad shoulders, heavy hands, sturdy legs, practical watch helm or brow wrap, lighter camp armor, one reinforced shoulder, bracers, belt plates, greaves, scorched leather harness, rough hide panels, dull red warning cloth, soot-dark blackened iron, dark steel, ash, mud, sparse non-graphic bone or horn territory markers, optional hook spear or bow/quiver visual read, and a gameplay purpose limited to perimeter visual planning. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a clean character production sheet with front, side, back, and three-quarter views, material swatches, scale bars against the approved Giant baselines, camp gate/watch-point context thumbnails, optional weapon silhouette callouts from existing Blood Axe armory packages, and docs-only guardrail notes. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid patrol route diagrams, avoid AI perception cones, avoid aggro radius callouts, avoid spawn or encounter diagrams, avoid combat stat or ability callouts, avoid final wearable-fit claims, avoid final animation timing, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, export, skeletal fit, cloth setup, physics asset, socket authoring, Unreal asset, source asset, or final visual approval is created or approved by this package.

Future modeling should start from the validated Giant base body and build a repeatable camp sentry read with large forms:

- Giant body base: preserve head mass, brow, jaw, thick neck, torso, shoulders, arms, heavy hands, pelvis, sturdy legs, large feet, and grounded stance.
- Head and watch gear: model a practical brow plate, hide hood edge, simple helm cap, cheek guard, or tied head wrap only if face, jaw, and neck remain readable.
- Upper body: model one reinforced pauldron or shoulder guard, a rough chest strap, simple chest plate segments, broad harness bands, and large buckles.
- Arms: model bracers, wrist wraps, hand guards, and spear/bow grip clearance without dense wrist ornaments.
- Belt and lower body: model heavy belt core, sparse warning tokens, side pouches, tasset plates, greaves, ankle straps, and broad boots without narrowing the Giant leg/foot read.
- Perimeter kit: optional signal horn, red warning strip, small field pouch, quiver strap, or gate-marker token may support the sentry read. Keep these visual only.
- Weapon or carry placeholders: if a future concept sheet includes a hook spear, longbow, shortbow, or quiver, keep it removable and governed by the relevant Blood Axe armory package. Do not merge a final weapon into the sentry body mesh by default.

Use texture, normal maps, or material masks for:

- Tiny rivets.
- Fine scratches.
- Dense pitting.
- Leather pores.
- Stitch rows.
- Soot speckles.
- Mud stains.
- Cloth weave.
- Small red paint chips.
- Bone grain.
- Hair or fur strand detail.

Future implementation gates:

- Do not claim wearable skeletal fit until a separate fit lane validates the armor and gear over the approved Giant baselines.
- Do not add swinging trophies, cloth strips, cloak motion, dangling chains, quiver physics, or secondary motion without cloth/physics approval.
- Do not solve patrol logic, alert behavior, attack arcs, projectile logic, weapon traces, or animation timing in this package.
- Keep gate, watch platform, barricade, shelter, and path geometry in camp/environment packages rather than baking them into the character.

## Texture and Material Notes

Required map families for a future approved build:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Optional Emissive (`E`) only for a separately approved material variant, not for baseline `A01`

Target texture names:

- `T_GIA_BloodAxeCampSentry_A01_Body_BC`
- `T_GIA_BloodAxeCampSentry_A01_Body_N`
- `T_GIA_BloodAxeCampSentry_A01_Body_ORM`
- `T_GIA_BloodAxeCampSentry_A01_Gear_BC`
- `T_GIA_BloodAxeCampSentry_A01_Gear_N`
- `T_GIA_BloodAxeCampSentry_A01_Gear_ORM`
- `T_GIA_BloodAxeCampSentry_A01_HairFur_BC`
- `T_GIA_BloodAxeCampSentry_A01_HairFur_N`
- `T_GIA_BloodAxeCampSentry_A01_HairFur_ORM`
- Optional future `T_GIA_BloodAxeCampSentry_A01_E` only after emissive approval

Shared material targets:

- `MI_GIA_BloodAxeReforgedMetal_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeScorchedLeather_A01`
- `MI_GIA_BloodAxeHideFur_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeBoneTrophy_A01`
- `MI_GIA_BloodAxeSootMud_A01`

Material slot target:

- Slot 0: body/head/skin and broad war paint.
- Slot 1: eyes, hair, and fur, or split only if the future Giant base convention requires it.
- Slot 2: blackened iron, dark steel, reforged metal, buckles, bracers, shoulder guard, and belt plates.
- Slot 3: scorched leather, rough hide, red cloth, harness wraps, pouches, and warning strips.
- Slot 4: optional bone/horn/trophy material only if shared atlas readability cannot handle these accents.

Target 4 material slots, 5 maximum. Do not create unique material slots for every strap, token, trophy, paint mark, cloth strip, or weapon wrap.

Packed `ORM` plan:

- R: Ambient occlusion around armor overlaps, belt/tasset layering, bracers, boot cuffs, shoulder guard, neck cloth, hand wraps, and gear anchors.
- G: High roughness for soot, ash, hide, leather, bone, matte blackened metal, and weathered skin; slightly lower roughness only on rubbed metal edges and hand-contact hardware.
- B: Metallic only for iron, steel, buckles, rings, armor plates, spear hardware, bow fittings, and selected reforged-metal surfaces.

Texture readability requirements:

- Use broad value separation between skin, leather, metal, cloth, and trophy accents so the sentry reads from MMO camera distance.
- Keep red cloth and paint broad but sparse.
- Paint large scratches, soot gradients, rubbed edges, and mud stains at Giant scale.
- Avoid readable text, franchise-like symbols, graphic gore, fresh blood, loot-rarity colors, damage-state colors, weak-point colors, or alert-state material masks.

## Triangle Budget

`SK_GIA_BloodAxeCampSentry_A01` is a repeatable Blood Axe warband visual row, not a named hero or boss asset.

Target budget for a future approved fully dressed sentry:

- LOD0 target: 52k-66k tris for body, head, hair/fur, practical armor, harness, belt, greaves, boots, and sparse sentry gear.
- LOD0 hard cap: 70k tris unless a later hero sentry variant receives separate approval.
- Optional equipped weapon budget: use the selected weapon or quiver package budget and do not include it in the character mesh budget by default.
- Material slots: 4 target, 5 maximum.
- Texture resolution: 2K standard for body and gear sets. 4K is not planned for baseline `A01` and would require separate hero or cinematic approval.

Budget distribution guidance:

- Body, head, hands, feet, and base anatomical forms: 50-58 percent.
- Armor plates, bracers, belt, greaves, boots, helm/brow gear, and practical sentry kit: 24-30 percent.
- Harness straps, pouches, red cloth blocks, hair/fur clumps, and broad hide panels: 12-16 percent.
- Sparse trophies, large buckles, and secondary accents: 4-7 percent.

Do not spend geometry on tiny rivets, dense stitch rows, fine leather pores, small scratches, repeated tooth strings, dense fur strands, many minor chain links, or small gore detail.

## LOD Plan

All future character implementations require LOD0-LOD3.

- LOD0: full Giant body mass, face/watch-helm read, hands/feet, hair/fur clumps, shoulder guard, bracers, chest strap, harness, belt/tassets, greaves, boots, red warning cloth, sparse trophy tokens, and optional weapon/quiver silhouette if attached.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small strap loops, hair/fur subdivisions, buckle edges, small trophy cuts, secondary cloth folds, and inner gear details.
- LOD2: 35-45 percent of LOD0; simplify fingers, back-side straps, tasset details, bracer edges, boot straps, trophy forms, fur clump cuts, and optional quiver/weapon dressing details.
- LOD3: 15-25 percent of LOD0; preserve height, shoulders, head/watch-helm outline, heavy hands, stance, red/black Blood Axe material blocks, and spear/bow/quiver read if present.

LOD reduction order:

1. Tiny rivets, scratches, stitches, pitting, leather pores, and paint flakes.
2. Small strap loops, knots, buckle bevels, and minor cloth tears.
3. Small trophy chips, tooth fragments, and non-silhouette tokens.
4. Under-armor and back-side detail.
5. Secondary hair/fur cuts and non-silhouette folds.
6. Minor plate bevels, inner armor cuts, and optional gear interiors.
7. Only after all secondary detail is reduced, simplify the head, shoulders, hands, feet, body mass, stance, and primary weapon/quiver outline.

Never reduce the validated Giant scale read, shoulder line, heavy hands, head/watch profile, broad stance, or Blood Axe color blocks before removing small detail.

## Collision Notes

No collision, physics asset, nav, AI sensing, trace, hit setup, or interaction volume is authored or approved in this docs-only package.

Future collision planning:

- Character collision type: Giant-tuned movement capsule inherited from `SK_GIA_Base_A01` conventions.
- Male 470 cm planning capsule: roughly 470 cm height and 100-125 cm radius, pending future implementation validation.
- Female 442 cm planning capsule, if a variant is approved: roughly 442 cm height and 95-115 cm radius.
- Physics asset should use simplified bodies for pelvis, spine, chest, head, upper/lower arms, hands, grouped fingers, thighs, calves, feet, and only approved large hair/fur/gear bodies.
- Worn armor, trophies, quiver straps, warning cloth, and perimeter kit should normally rely on the owning Giant physics asset and simple bounds, not per-strap or per-token collision.
- Equipped hook spear, bow, shortbow, or quiver should inherit the relevant prop package collision rules after selection. No combat trace rules are authored here.

Do not add AI perception volumes, sight cones, hearing radii, aggro radii, patrol route volumes, spawn blockers, encounter triggers, nav links, projectile collision, weapon traces, damage zones, weak points, loot pickup collision, cover volumes, trap triggers, per-chain collision, per-cloth collision, or per-trophy collision from this package.

## Animation Notes

No animation, Animation Blueprint, montage, authored timing, patrol cycle, alert state, weapon attack, bow draw, projectile release, cloth simulation, secondary motion, physics setup, or final pose set is created or approved here.

Future animation review may evaluate visual clearance only after separate approval:

- Heavy Giant idle and simple watch-ready idle.
- Standing gate-watch pose, head-turn pose, or weight-shift pose as visual checks only.
- Hook spear hold clearance if a spear profile is selected.
- Bow carry, quiver reach, and back/side carry clearance if a ranged profile is selected.
- Belt, tasset, bracer, greave, boot, and warning-cloth clearance during base Giant locomotion.
- Optional signal horn or marker handling as a visual prop clearance task only.

This package does not define patrol timing, patrol routes, alert timing, attack cadence, projectile timing, bow draw/release timing, melee swing timing, ability telegraphs, damage windows, AI states, or encounter behavior. Rigid gear should be preferred for a first pass. Cloth strips, dangling trophies, fur secondary motion, quiver sway, banner cloth, or physics-driven pieces require separate approval and validation.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, physics asset, socket, validator, startup actor, import script, runtime source, source asset, or DCC export is created by this package.

Planned future Unreal asset:

- Asset name: `SK_GIA_BloodAxeCampSentry_A01`
- Asset type: Skeletal Mesh character candidate
- Planned folder: `/Game/Aerathea/Characters/Giants/BloodAxe/CampSentry/`
- Planned skeleton dependency: future approved Giant skeleton convention inherited from `SK_GIA_Base_A01`
- Import scale: centimeter-authored source, import scale 1.0 after future DCC/export validation
- Pivot: feet at world origin, matching the Giant base convention
- Forward orientation: match the Giant base import convention selected by the future implementation task
- Collision type: Giant movement capsule plus simplified physics asset only after implementation approval
- LODs: LOD0, LOD1, LOD2, LOD3 required before production import approval
- Material slot count: 4 target, 5 maximum
- Texture set: 2K standard body/gear/hair-fur maps unless a later hero exception is approved
- Blueprint behavior: none
- Animation list: none authored by this package
- Performance notes: keep baseline `A01` repeatable, reduce straps/tokens before primary silhouette, reuse shared Blood Axe materials, and avoid extra material slots for small accents.

Planned texture names:

- `T_GIA_BloodAxeCampSentry_A01_Body_BC`
- `T_GIA_BloodAxeCampSentry_A01_Body_N`
- `T_GIA_BloodAxeCampSentry_A01_Body_ORM`
- `T_GIA_BloodAxeCampSentry_A01_Gear_BC`
- `T_GIA_BloodAxeCampSentry_A01_Gear_N`
- `T_GIA_BloodAxeCampSentry_A01_Gear_ORM`
- `T_GIA_BloodAxeCampSentry_A01_HairFur_BC`
- `T_GIA_BloodAxeCampSentry_A01_HairFur_N`
- `T_GIA_BloodAxeCampSentry_A01_HairFur_ORM`
- Optional future `T_GIA_BloodAxeCampSentry_A01_E` only for a separately approved emissive variant

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
- `belt_quiver_l`
- `belt_quiver_r`
- `belt_trophy_l`
- `belt_trophy_r`
- `side_hook_l`
- `side_hook_r`
- `watch_horn_l`
- `watch_marker_back`
- `harness_chest_anchor`
- `harness_belt_anchor`

Final socket names, transforms, weapon attachments, trace markers, AI hooks, VFX hooks, cloth setup, physics bodies, Blueprint behavior, and animation links require separate Unreal/animation/gameplay approval.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/characters/SK_GIA_BloodAxeCampSentry_A01/`
- Production package: `docs/assets/characters/SK_GIA_BloodAxeCampSentry_A01/PRODUCTION_PACKAGE.md`
- Parent warband kit: `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/PRODUCTION_PACKAGE.md`
- Parent warband intake: `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/CHILD_ASSET_INTAKE.md`
- Related camp kit: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/PRODUCTION_PACKAGE.md`
- Related armory kit: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- Related base body package: `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md`
- Planned future Unreal folder after approval only: `/Game/Aerathea/Characters/Giants/BloodAxe/CampSentry/`

Planned future names:

- Skeletal Mesh: `SK_GIA_BloodAxeCampSentry_A01`
- Skeleton: inherit from the future approved Giant base skeleton convention; do not create a new skeleton assumption here.
- Physics Asset: `PHYS_GIA_BloodAxeCampSentry_A01`, only after implementation approval.
- Animation Blueprint: `ABP_GIA_BloodAxeCampSentry_A01`, only after animation/runtime approval.
- Material Instance: `MI_GIA_BloodAxeCampSentry_A01`
- Shared material references: `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeScorchedLeather_A01`, `MI_GIA_BloodAxeRedCloth_A01`, `MI_GIA_BloodAxeBoneTrophy_A01`, `MI_GIA_BloodAxeSootMud_A01`

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, FBX exports, Unreal Content assets, runtime source, tools, validators, startup-scene actors, copied source concepts, global index entries, task-board edits, backlog edits, bootstrap edits, final approval captures, or external concept-folder edits from this task.

## Approval Gates and Stop Points

- Lead approval is required before `SK_GIA_BloodAxeCampSentry_A01` is selected as a first DCC target.
- Visual approval is required before final sentry silhouette, watch helm, shoulder mass, gear density, red cloth placement, weapon profile, trophy density, or perimeter identity is locked.
- Culture approval is required if Blood Axe visual language starts bleeding into neutral/civilized Giant packages.
- DCC approval is required before creating source folders, Blender sources, sculpt files, retopo files, UVs, bakes, collision proxies, proof renders, LOD sources, or exports.
- Unreal approval is required before importing skeletal meshes, material instances, textures, LODs, physics assets, sockets, validators, Blueprints, or startup-scene actors.
- Wearable-fit approval is required before claiming armor, helm, harness, belt, greaves, quiver, weapon carry, warning cloth, or perimeter kit fits either Giant baseline.
- Cloth and physics approval is required before adding moving cloth strips, cloak pieces, banner cloth, swinging tokens, dangling trophies, fur secondary motion, simulated cloth, or physics bodies.
- Animation approval is required before authored locomotion variants, watch idles, head turns, weapon hold poses, attacks, bow draw, hit reactions, death, montage timing, or Animation Blueprint logic.
- Gameplay approval is required before patrol paths, AI perception, aggro radii, alert states, combat abilities, combat stats, projectile behavior, encounter scripting, spawn rules, guard-post interactions, loot rules, objective logic, cover behavior, trap behavior, camp capture, or interactable behavior.
- Source-storage approval is required before copying, embedding, editing, moving, cropping, or committing any external source concept.

Stop immediately before:

- Any DCC, FBX, Unreal, source asset, runtime source, validator, material graph, Blueprint, startup placement, or source concept work.
- Final visual approval or first playable visual approval.
- Final wearable skeletal fit, final socket transforms, final weapon selection, final animation timing, or final pose lock.
- Any patrol, AI, aggro, encounter, spawn, combat, projectile, loot, economy, crafting, interaction, or objective definition.
- Any change to the validated `SK_GIA_Base_A01` scale lock, skeleton assumptions, or socket assumptions.
- Any shift that makes Blood Axe red-black raider language the default Giant culture.
- Any increase in trophies, skulls, red cloth, chains, straps, rivets, cracks, scratches, or gore detail that hurts mid-poly MMO readability.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, source asset, external concept, validator, global index, task board, backlog, bootstrap, or other package file.
- `SK_GIA_BloodAxeCampSentry_A01` is a hostile Blood Axe Giant camp perimeter visual package, not a neutral/civilized Giant package.
- Giant scale lock is explicit and unchanged: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", with approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- The character preserves Giant body mass, shoulder breadth, heavy hands, sturdy legs, large feet, and towering scale instead of becoming a scaled normal humanoid.
- Gameplay purpose is limited to visual role planning; no patrol paths, AI perception, aggro radii, encounter scripting, spawn rules, combat stats, abilities, loot, or projectile behavior are defined.
- Primary forms are watch profile, practical helm/brow gear, lighter camp armor, bracers, harness, belt/tassets, greaves, boots, red warning cloth, and optional spear/bow/quiver read.
- Materials align with blackened iron, dark steel, scorched leather, hide/fur, dull red cloth/paint, soot, ash, mud, grime, and sparse aged bone/horn trophies.
- `MI_GIA_BloodAxeReforgedMetal_A01` and related Blood Axe shared material families are referenced as planning dependencies only.
- Neutral/civilized Giant stoneworker materials, blue-gray cave-town identity, warm hearth language, and restrained rune accents are excluded from the baseline.
- Default emissive, forge heat, ritual glow, shamanic glow, faction aura, animated material states, cloth, physics, and final socket transforms are not claimed.
- Texture maps include `BC`, `N`, `ORM`, and optional future `E` only behind approval.
- Triangle budget, material slot target, LOD0-LOD3 plan, collision planning, animation scope, Unreal import planning, folder naming, approval gates, and stop points are included.
- Package does not claim skeletal fit, authored animation, animation timing, cloth simulation, physics setup, final weapon selection, final visual approval, first DCC target selection, or implementation completion.
