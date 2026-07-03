# SK_GIA_BloodAxeTrophyCarrier_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeTrophyCarrier_A01`
- Asset type: Skeletal Mesh character production package / hostile Blood Axe Giant visual variant candidate
- Parent route: `KIT_GIA_BloodAxeWarband_A01#TrophyCarriers`
- Parent scale dependency: `SK_GIA_Base_A01`
- Related Blood Axe kit: `KIT_GIA_BloodAxeArmory_A01`
- Related gear packages: `SK_GIA_BloodAxeHarness_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, `SM_GIA_BloodAxeTrophyHelm_A01`, `SK_GIA_BloodAxeRaiderChest_A01`, and `SK_GIA_BloodAxeGreaves_A01`
- Source route references: `BloodAxeChieftan.png`, `Bloodaxe Army.png`, `BloodAxeArmory.png#Armor_TrophyHelmFaceGuard`, and `BloodAxeArmory.png#Armor_TrophyBeltTassets`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Task: `AET-MA-20260629-102`
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, runtime source, validator, startup placement, source asset, final visual approval, or first DCC target selection is included

`SK_GIA_BloodAxeTrophyCarrier_A01` defines a hostile Blood Axe Giant character direction focused on intimidation silhouette and warband visual hierarchy. The character should read as a towering Giant bearing restrained trophy racks, a heavy harness, broad belt/tasset forms, blackened reforged armor, oxide red Blood Axe markers, and sparse dry trophy shapes. The design is meant to communicate Blood Axe brutality through scale, posture, material language, and a few readable symbols, not through graphic gore or dense small detail.

Blood Axe visual language must remain separate from neutral/civilized Giant culture. This package uses hostile raider markers: soot-dark iron, scorched leather, red cloth, ash, rough hide, large carry hardware, and controlled trophy forms. It must not replace the Giant base identity of remote mountain stoneworkers, hidden cave towns, highland nomads, blue-gray stonecraft, warm hearth identity, or restrained civilized rune language.

This document is planning only. It does not authorize source concept movement, DCC creation, mesh creation, wearable skeletal fit, animation timing, physics, cloth, gameplay behavior, or Unreal implementation.

## Gameplay Purpose

The gameplay purpose is visual role only: this character marks a Blood Axe warband or camp composition as more intimidating and trophy-bearing at MMO camera distance. The package defines silhouette, scale, material, readability, and dependency expectations for a future production lane without defining combat role, encounter role, AI class, stats, abilities, loot, equipment behavior, or trophy-collection mechanics.

Expected future visual uses:

- Blood Axe warband roster sheet row for a trophy-bearing Giant variant.
- Camp, gate, formation, or command-area visual dressing reference after separate placement approval.
- Shared character direction for harness, belt, helm, chest, greave, and optional back-load compatibility planning.
- Scale and silhouette reference for restrained trophy density across hostile Blood Axe character packages.
- Future DCC planning target only after lead approval selects build ownership and visual source direction.

Out of scope:

- DCC source, Blender files, sculpt files, retopo, UVs, bakes, collision proxies, FBX exports, Unreal Content, materials, textures, Blueprints, validators, startup-scene placement, runtime source, or external source concept copying.
- AI, combat stats, combat abilities, damage windows, encounter composition, patrol logic, spawn rules, objective logic, loot rules, inventory behavior, pickup behavior, crafting, economy, or trophy collection.
- Final wearable skeletal fit, final socket transforms, cloth simulation, physics setup, secondary motion, animation timing, montage authoring, or final visual approval.
- Graphic gore, dismemberment, fresh remains, or explicit trophy treatment.

## Silhouette Notes

Primary silhouette: a massive hostile Blood Axe Giant with a broad body read, heavy hands, wide stance, visible Giant proportions, and restrained trophy-carry gear layered over the validated base body. The trophy carrier should be recognizable from the back and three-quarter view through a back rack or harness load, but the design must not hide the Giant torso, waist, arms, or head under a curtain of small hanging elements.

Core silhouette requirements:

- Preserve the validated Giant body first: towering height, broad shoulders, thick neck, long arms, heavy hands, sturdy legs, large feet, and weighty stance.
- Use a heavy utility harness as the main carry architecture: broad chest straps, back cross-straps, oversized rings, belt anchors, and a limited number of side hooks.
- Add one clear trophy-carry read: a short back rack, shoulder yoke, side bundle, or belt/back load that can be understood from MMO camera distance.
- Keep trophies large, dry, symbolic, and non-graphic: aged bone plates, horn forms, broken shield plates, cracked weapon fragments, old helm fragments, carved warning tokens, or wrapped bundle shapes.
- Limit baseline `A01` trophy count to a few large forms. Avoid dense strings, curtains, clusters, and tiny repeated fragments.
- Use broad red cloth strips or red paint marks as Blood Axe identifiers, preferably at the harness, belt, shoulder, or rack, without turning the character into a one-color red figure.
- Keep chest, shoulder, belt, and greave forms compatible in language with the existing Blood Axe gear packages, but do not claim final fit or combined wearability.
- Preserve negative space around elbows, wrists, pelvis, thighs, knees, ankles, neck, and jaw so a later implementation review can test clearance.

Avoid:

- Making the trophy carrier a scaled normal humanoid with oversized accessories.
- Making Blood Axe trophy language the default Giant culture.
- Graphic gore, dismemberment, wet shine, explicit remains, harvesting imagery, or trophy collection imagery.
- Dense dangling chains, tiny rivet fields, repeated small teeth, trophy curtains, charm strings, readable text, or small symbols that collapse into noise.
- Neutral/civilized Giant blue-gray stoneworker motifs, hearth ornament, civic masonry patterns, peaceful highland dress, or restrained blue rune accents as the baseline.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Feet at world origin and forward orientation should match the future Giant base import convention.

Planning target:

- `A01` should be planned first as a repeatable Blood Axe character variant against the male 470 cm baseline for maximum read in the warband row.
- Female 442 cm review remains required for any future shared-fit or variant claim.
- This package does not lock final gender, body variant, skeleton split, final proportions, or wearable fit beyond the approved Giant scale range.
- Normal humanoid compatibility is not required.

Carrier gear scale planning:

- Harness strap width: 14-28 cm for main straps; smaller cords should be texture or normal detail unless they define a major anchor.
- Back rack or yoke height: 110-190 cm above the upper back if approved, kept below a height that breaks standard character framing.
- Back rack or yoke width: 80-150 cm, wide enough to read but not wider than the shoulder/weapon clearance envelope without approval.
- Major ring diameter: 24-45 cm for sternum, shoulder, side, belt, or back anchors.
- Trophy shape size: 35-95 cm for large readable forms; tiny trinkets should be removed or painted.
- Belt and tasset dependency: follow `SK_GIA_BloodAxeTrophyBelt_A01` planning for thick belt mass, broad tassets, and restrained trophy density.
- Helm/faceguard dependency: follow `SM_GIA_BloodAxeTrophyHelm_A01` planning if a head silhouette is used, with face, jaw, neck, and shoulder clearance remaining approval-gated.

Required future clearance checks before any implementation claim:

- Neck, jaw, hair, brow, head turn, and shoulder clearance for any helm or faceguard.
- Shoulder raise, elbow bend, wrist rotation, hand reach, and two-handed carry stance around harness and trophy load.
- Back rack clearance with `back_large_weapon`, `back_shield`, future `back_quiver`, and any optional banner or weapon carry planning.
- Belt, side trophy, sidearm, tasset, pelvis, thigh, knee, and stride clearance.
- Rear view and over-shoulder camera read, so the back load does not become an unreadable mass.

## Materials and Color Palette

Primary Blood Axe material language:

- Weathered Giant skin with ash, soot, scars, grime, and broad red war paint or mineral pigment.
- Blackened iron, dark steel, and stolen/reforged metal matching `MI_GIA_BloodAxeReforgedMetal_A01`.
- Scorched leather, rough hide, dark fur pads, rawhide wraps, sinew cord, and heavy straps.
- Deep oxide red cloth, dirty red wraps, chipped red paint, and dull banner fragments as restrained sub-faction identifiers.
- Aged bone, horn, cracked shield pieces, broken weapon fragments, old helm fragments, and carved warning tokens used sparingly and non-graphically.
- Soot, ash, dried mud, oil-dark grime, rubbed steel edges, and broad hand-painted wear.

Suggested palette:

- Blackened iron: `#151719` to `#2A2C2E`
- Worn dark steel: `#555A5C` to `#787B78`
- Scorched leather: `#241611` to `#4A2E20`
- Dark hide/fur: `#1D1511` to `#3B2A1E`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Old bone/horn: `#A69578` to `#D0B98C`
- Soot and grime: `#0B0A09` to `#403025`
- Weathered Giant skin: inherit the base Giant skin direction, dirtied with ash and war paint rather than recolored into armor material.

No default emissive is approved. Forge heat, ritual glow, shamanic glow, animated material states, glowing eyes, faction aura, or VFX hooks require separate visual/material approval and are not part of this `A01` baseline.

## Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_GIA_BloodAxeTrophyCarrier_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant trophy carrier silhouette, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, towering shoulder mass, heavy hands, sturdy legs, preserved Giant body proportions, broad scorched-leather harness straps, oversized blackened-iron rings, a restrained back rack or shoulder yoke, broad trophy belt and tassets, optional skull-forward helm influence only if face and neck readability remain clear, blackened reforged iron, dark steel, oxide red cloth markers, soot, ash, rough hide, sparse dry non-graphic trophy shapes such as aged bone, horn, broken shield, old helm, and cracked weapon fragments, and a visual role as Blood Axe warband intimidation and camp dressing rather than a gameplay system. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a character production sheet with front, side, back, three-quarter views, back-load callouts, harness and belt clearance callouts, material swatches, scale markers against the approved Giant baselines, and docs-only guardrail notes on a clean background. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid dismemberment, avoid trophy collection imagery, avoid loot or inventory callouts, avoid AI/combat/encounter/ability diagrams, avoid wearable-fit claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, export, skeletal fit, physics asset, cloth setup, socket authoring, Unreal asset, source asset, or final visual approval is created or approved by this package.

Future modeling should start from the validated Giant base proportions and add the trophy carrier read with large forms:

- Giant body base: preserve the head, brow, jaw, thick neck, torso, shoulders, arms, heavy hands, pelvis, sturdy legs, large feet, and grounded stance.
- Harness architecture: build a few broad chest, back, shoulder, and belt straps as real geometry where they define the carry system.
- Back load: if approved, model a compact rack, yoke, or strapped bundle as a clean silhouette with only a few major crossbars, hooks, and tied forms.
- Trophies: model only large production-readable forms such as horn pieces, old bone plates, broken shield fragments, old helm fragments, cracked weapon plates, and carved warning tokens.
- Armor dependency: coordinate visual layering with raider chest, harness, trophy belt, greaves, and optional trophy helm packages without merging them into an assumed final wearable set.
- Red cloth: use two or three broad cloth strips, wraps, or paint blocks. Avoid shredded fringe and tiny flags.
- Rings and chains: use oversized rings and very short chain sections only where they support the silhouette or attachment logic.
- Hair/fur/hide: use large clumps and pads, not strand geometry.
- Trophy rack underside and back view should remain clean because this character is likely to be seen from behind in future review scenes.

Texture, normal maps, or material masks should handle:

- Tiny rivets.
- Fine scratches.
- Dense pitting.
- Stitch rows.
- Leather pores.
- Fur texture.
- Soot speckles.
- Small red paint chips.
- Hairline cracks in bone or horn.
- Minor chips on broken shield or old metal fragments.

Do not model:

- Graphic gore, explicit remains, dismemberment, harvesting imagery, dangling gore ropes, fresh wet material, dense tooth strings, dozens of small charms, readable tally text, interactable trophy objects, particle cards, spell meshes, aura rings, loot markers, inventory tags, or source-concept overlays.

Future implementation gates:

- Do not claim wearable skeletal fit until a separate character/gear fit lane validates the combined harness, belt, chest, helm, greaves, and trophy load over the approved Giant baselines.
- Do not add cloth strips, swinging trophies, chain motion, secondary physics, or moving rack parts without cloth/physics approval.
- Do not solve animation timing, carry pose timing, combat motion, AI behavior, or encounter placement in the model package.
- Split display-only gear, optional wearable gear, and integrated character elements if later pivot, socket, clearance, or silhouette needs diverge.

## Texture and Material Notes

Target texture families for a future approved character build:

- `T_GIA_BloodAxeTrophyCarrier_A01_Body_BC`
- `T_GIA_BloodAxeTrophyCarrier_A01_Body_N`
- `T_GIA_BloodAxeTrophyCarrier_A01_Body_ORM`
- `T_GIA_BloodAxeTrophyCarrier_A01_Gear_BC`
- `T_GIA_BloodAxeTrophyCarrier_A01_Gear_N`
- `T_GIA_BloodAxeTrophyCarrier_A01_Gear_ORM`
- `T_GIA_BloodAxeTrophyCarrier_A01_HairFur_BC`
- `T_GIA_BloodAxeTrophyCarrier_A01_HairFur_N`
- `T_GIA_BloodAxeTrophyCarrier_A01_HairFur_ORM`
- Optional future approval-gated `T_GIA_BloodAxeTrophyCarrier_A01_E`

Material slot target:

- Slot 0: body/head/skin with soot, scars, and broad red paint masks.
- Slot 1: eyes, hair, and fur, or split eyes if the future Giant base convention requires it.
- Slot 2: `MI_GIA_BloodAxeReforgedMetal_A01` or a consuming character gear instance for blackened iron, dark steel, buckles, rings, rack hardware, and chipped paint.
- Slot 3: scorched leather, dark hide, oxide red cloth, harness straps, and wraps.
- Slot 4: optional bone/horn/trophy material only if shared atlas readability cannot handle the trophy forms.

Target 4 material slots, 5 maximum only if eyes/hair or trophy readability must remain separate. Do not create unique material slots for every strap, ring, trophy, cloth strip, paint mark, or rack piece.

Packed `ORM` plan:

- R: Ambient occlusion around body folds, harness intersections, back rack mounts, belt/tasset hinges, trophy attachment points, armor overlaps, and greave undercuts.
- G: High roughness for soot, ash, leather, hide, matte bone, hair/fur, and blackened metal; slightly lower roughness on rubbed steel edges and hand-contact hardware.
- B: Metallic only for iron, steel, rings, buckles, chain links, rack hardware, armor plates, and old weapon fragments.

Texture readability requirements:

- Keep red accents broad and sparse so Blood Axe identity reads without flattening the character into a red mass.
- Use value separation between skin, blackened metal, leather, red cloth, bone/horn, and dark hide.
- Paint broad hammer marks, soot gradients, strap compression, red paint wear, and Giant-scale scratches rather than noise.
- Keep trophy material dry, matte, aged, and symbolic.
- Avoid readable text, franchise-like symbols, loot-rarity colors, gore coloring, wet shine, material masks that imply weak points, or any inventory/collection state.
- `E` map is absent by default and allowed only for a separately approved material variant.

## Triangle Budget

`SK_GIA_BloodAxeTrophyCarrier_A01` is a repeatable hostile Blood Axe character variant, not a named boss, final encounter asset, or hero cinematic target.

Target budget for a future approved fully dressed character:

- LOD0 target: 58k-74k tris for body, head, hair/fur, integrated Blood Axe gear, harness, belt/tassets, greaves, optional helm influence, compact trophy load, and restrained trophy forms.
- LOD0 hard cap: 76k tris unless a later named hero or boss-adjacent variant receives separate approval.
- Optional carried weapon budget: use the weapon's own package budget and do not include it in the character mesh budget.
- Optional separate rack or display prop budget: 4k-9k tris if a later task splits it from the character.
- Material slots: 4 target, 5 maximum.
- Texture resolution: 2K standard for enemy use; 4K only for an approved close-up hero or named variant.

Budget distribution guidance:

- Body, head, hands, feet, and base anatomical forms: 45-55 percent.
- Armor plates, helm influence, belt, greaves, boots, and rack/yoke forms: 22-30 percent.
- Harness straps, rings, buckles, red cloth, hair/fur clumps, and carry architecture: 14-20 percent.
- Sparse trophy forms, short chain sections, and secondary accents: 5-8 percent.

Do not spend geometry on tiny rivets, dense chain links, fine stitches, hair strands, micro scratches, small tally marks, repeated tooth strings, or graphic detail.

## LOD Plan

All future character implementations require LOD0-LOD3.

- LOD0: full Giant body mass, face/helm read if used, hands/feet, hair/fur clumps, chest or harness architecture, belt/tassets, greaves, compact rack/yoke or back load, broad red cloth markers, sparse large trophies, and primary carrier silhouette.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small strap loops, hair/fur subdivisions, small buckle edges, secondary trophy cuts, inner rack detail, and underside armor details.
- LOD2: 35-45 percent of LOD0; simplify fingers, inner clothing folds, back-side strap complexity, tasset details, trophy forms, fur clump cuts, rack mounts, and secondary cloth folds while preserving the carrier read.
- LOD3: 15-25 percent of LOD0; preserve height, shoulders, head/helm mass, heavy hands, back-load silhouette, belt/tasset read, red/black Blood Axe material blocks, and broad stance.

LOD reduction order:

1. Tiny rivets, scratches, stitches, pitting, leather pores, and small paint flakes.
2. Small strap loops, knots, buckle bevels, and minor chain segments.
3. Small trophy fragments, little bone chips, and cloth tears.
4. Rack underside, back-side harness overlap, and non-visible support detail.
5. Secondary hair/fur cuts and non-silhouette folds.
6. Minor plate bevels, interior armor cuts, and small broken-fragment cuts.
7. Only after all secondary detail is reduced, simplify the helm/head read, shoulder line, chest/harness, back-load silhouette, belt/tasset mass, hands, feet, and stance.

Never reduce the validated Giant scale read, shoulder width, heavy hands, head silhouette, back-load read, broad belt/tasset shape, or Blood Axe color blocks before removing small detail.

## Collision Notes

No collision, physics asset, hit setup, or wearable collision is authored or approved in this docs-only package.

Future collision planning:

- Character collision type: Giant-tuned movement capsule inherited from `SK_GIA_Base_A01` conventions.
- Male 470 cm planning capsule: roughly 470 cm height and 100-125 cm radius, pending future implementation validation.
- Female 442 cm planning capsule, if a variant is approved: roughly 442 cm height and 95-115 cm radius.
- Physics asset should use simplified bodies for pelvis, spine, chest, head, upper/lower arms, hands, grouped fingers, thighs, calves, feet, and only approved large hair/fur/gear bodies.
- Worn armor, harness straps, trophy rack, trophies, cloth, and gear should normally rely on the owning Giant physics asset and simple bounds, not per-strap, per-chain, per-trophy, or per-cloth collision.
- Optional display variants, if later approved, should use simple boxes, capsules, or low-count convex bounds around the main rack or gear volume.

Do not add combat hit zones, weak points, armor-stat collision, aura volumes, loot pickup collision, interactable trophy collision, per-chain collision, per-cloth collision, or per-trophy collision from this package.

## Animation Notes

No animation, Animation Blueprint, montage, authored timing, cloth simulation, secondary motion, physics setup, or final pose set is created or approved here.

Future animation review may evaluate clearance only after separate approval:

- Giant heavy idle, walk, run/jog, turn in place, and broad stance compatibility.
- Back-load and harness clearance during shoulder raise, torso twist, arm reach, and hand overlap.
- Belt, tasset, and side trophy clearance during stride, knee lift, crouch review if used, and wide stance.
- Helm, neck, jaw, and shoulder clearance if a trophy helm influence is used.
- Optional static carry posture or intimidation pose for concept review, without timing, behavior, or encounter implications.

Rigid gear should be preferred for a first pass. Cloth strips, swinging chains, dangling trophies, loose rack elements, fur secondary motion, or physics-driven pieces require separate approval and validation. This package does not define animation timing, AI states, combat moves, encounter behaviors, or trophy interaction behavior.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, skeletal mesh, physics asset, animation Blueprint, Blueprint actor, validator, startup actor, runtime source, socket, import script, or source asset is created by this package.

Planned future Unreal asset:

- Asset name: `SK_GIA_BloodAxeTrophyCarrier_A01`
- Asset type: Skeletal Mesh character candidate
- Planned folder: `/Game/Aerathea/Characters/Giants/BloodAxe/TrophyCarrier/`
- Planned skeleton dependency: future approved Giant skeleton convention inherited from `SK_GIA_Base_A01`
- Import scale: centimeter-authored source, import scale 1.0 after future DCC/export validation
- Pivot: feet at world origin, matching the Giant base convention
- Forward orientation: match the Giant base import convention selected by the future implementation task
- Collision type: Giant movement capsule plus simplified physics asset only after implementation approval
- LODs: LOD0, LOD1, LOD2, LOD3 required before production import approval
- Material slot count: 4 target, 5 maximum
- Blueprint behavior: none
- Animation list: none authored by this package
- Performance notes: keep the fully dressed carrier within repeatable Blood Axe character budgets, reduce trophies and small straps before primary silhouette, avoid extra material slots for small accents, and keep the trophy load readable without dense geometry.

Planned texture names:

- `T_GIA_BloodAxeTrophyCarrier_A01_Body_BC`
- `T_GIA_BloodAxeTrophyCarrier_A01_Body_N`
- `T_GIA_BloodAxeTrophyCarrier_A01_Body_ORM`
- `T_GIA_BloodAxeTrophyCarrier_A01_Gear_BC`
- `T_GIA_BloodAxeTrophyCarrier_A01_Gear_N`
- `T_GIA_BloodAxeTrophyCarrier_A01_Gear_ORM`
- `T_GIA_BloodAxeTrophyCarrier_A01_HairFur_BC`
- `T_GIA_BloodAxeTrophyCarrier_A01_HairFur_N`
- `T_GIA_BloodAxeTrophyCarrier_A01_HairFur_ORM`
- Optional future `T_GIA_BloodAxeTrophyCarrier_A01_E` only for a separately approved emissive variant.

Expected inherited socket dependencies from the Giant base package, referenced only for future validation:

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

- `belt_trophy_l`
- `belt_trophy_r`
- `side_hook_l`
- `side_hook_r`
- `harness_back_anchor`
- `harness_chest_anchor`
- `harness_belt_anchor`
- `back_trophy_rack`
- `shoulder_yoke_anchor_l`
- `shoulder_yoke_anchor_r`

Final socket names, transforms, carry offsets, attachment rules, physics bodies, cloth setup, animation notifies, Blueprint behavior, gameplay behavior, and final wearable fit require separate Unreal/animation/gameplay approval.

## Folder and Naming Recommendation

Docs:

- Package folder: `docs/assets/characters/SK_GIA_BloodAxeTrophyCarrier_A01/`
- Package file: `docs/assets/characters/SK_GIA_BloodAxeTrophyCarrier_A01/PRODUCTION_PACKAGE.md`

Related docs:

- Base body: `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md`
- Parent warband package: `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/PRODUCTION_PACKAGE.md`
- Parent warband child intake: `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/CHILD_ASSET_INTAKE.md`
- Armory kit: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- Harness: `docs/assets/characters/SK_GIA_BloodAxeHarness_A01/PRODUCTION_PACKAGE.md`
- Trophy belt: `docs/assets/characters/SK_GIA_BloodAxeTrophyBelt_A01/PRODUCTION_PACKAGE.md`
- Trophy helm: `docs/assets/props/SM_GIA_BloodAxeTrophyHelm_A01/PRODUCTION_PACKAGE.md`
- Raider chest: `docs/assets/characters/SK_GIA_BloodAxeRaiderChest_A01/PRODUCTION_PACKAGE.md`
- Greaves: `docs/assets/characters/SK_GIA_BloodAxeGreaves_A01/PRODUCTION_PACKAGE.md`

Future naming candidates after separate approval:

- Character: `SK_GIA_BloodAxeTrophyCarrier_A01`
- Optional male split: `SK_GIA_BloodAxeTrophyCarrier_Male_A01`
- Optional female split: `SK_GIA_BloodAxeTrophyCarrier_Female_A01`
- Optional separate rack static mesh: `SM_GIA_BloodAxeTrophyRack_A01`
- Optional display-only rack: `SM_GIA_BloodAxeTrophyRack_Display_A01`
- Material instance: `MI_GIA_BloodAxeTrophyCarrier_A01`
- Shared material references: `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeScorchedLeather_A01`, `MI_GIA_BloodAxeRedCloth_A01`, and `MI_GIA_BloodAxeBoneTrophy_A01`

Planned future Unreal folder after approval only:

- `/Game/Aerathea/Characters/Giants/BloodAxe/TrophyCarrier/`

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, FBX exports, Unreal Content assets, runtime source, tools, validators, startup-scene actors, copied source concepts, embedded concept images, global index entries, task-board edits, backlog edits, bootstrap edits, final approval captures, or external concept-folder edits from this task.

## Docs-Only Guardrails

- Stop before DCC source creation, Blender source creation, sculpt creation, retopo, UVs, bakes, proof renders, collision proxies, FBX export, Unreal Content import, material graph authoring, runtime source changes, validator creation, startup-scene placement, or source asset creation.
- Stop before moving, copying, editing, embedding, or committing external source concept files.
- Stop before final visual approval.
- Stop before first DCC target selection.
- Stop before wearable skeletal fit, skinning, final socket transforms, attachment offsets, physics asset setup, cloth setup, or secondary motion.
- Stop before animation timing, montage authoring, carry-pose timing, animation Blueprint logic, or authored motion finalization.
- Stop before AI behavior, combat stats, combat abilities, encounter role, patrol logic, spawn rules, objective logic, loot rules, inventory behavior, crafting, economy, pickup behavior, or trophy collection mechanics.
- Stop before any graphic gore, dismemberment, explicit remains, harvesting implication, or trophy-density escalation.
- Stop if Blood Axe red-black raider language starts replacing neutral/civilized Giant stoneworker, cave-town, or highland nomad culture.
- Stop if the package appears to require changing the validated `SK_GIA_Base_A01` scale lock, skeleton assumptions, or base socket assumptions.
- Stop if trophies, cloth strips, chains, straps, rivets, cracks, scratches, or symbols become dense enough to hurt mid-poly MMO readability.

## Approval Gates

- Lead approval is required before `SK_GIA_BloodAxeTrophyCarrier_A01` is selected as a first DCC target or promoted from planning row to build work.
- Visual approval is required before final trophy carrier silhouette, rack/yoke shape, trophy density, red cloth placement, helm usage, back-load size, or gear combination is locked.
- Culture approval is required if Blood Axe visual language starts bleeding into neutral/civilized Giant packages.
- DCC approval is required before creating meshes, Blender sources, sculpt files, retopo files, UVs, bakes, collision proxies, proof renders, or exports.
- Unreal approval is required before importing skeletal meshes, static rack meshes, material instances, textures, LODs, physics assets, sockets, validators, Blueprints, or startup-scene actors.
- Wearable-fit approval is required before claiming harness, chest armor, belt, greaves, helm, rack, yoke, trophies, weapon carry, or side attachments fit either Giant baseline.
- Attachment approval is required before adding final socket names, socket transforms, rack offsets, trophy offsets, side-hook offsets, weapon carry offsets, or back-load attachment rules.
- Cloth and physics approval is required before adding moving cloth strips, swinging chains, dangling trophies, loose rack pieces, fur secondary motion, simulated cloth, or physics bodies.
- Animation approval is required before authored locomotion, carry poses, weapon hold poses, attacks, hit reactions, death, montage timing, or animation Blueprint logic.
- Gameplay approval is required before combat behavior, encounter role, abilities, damage values, hit zones, weak points, objective logic, AI behavior, patrol behavior, spawn rules, loot rules, inventory behavior, pickup behavior, crafting, economy, or trophy collection mechanics.
- Source-storage approval is required before copying, embedding, editing, or committing any external source concept.

## Quality Gate Checklist

- Package is docs-only and touches only `docs/assets/characters/SK_GIA_BloodAxeTrophyCarrier_A01/PRODUCTION_PACKAGE.md`.
- `SK_GIA_BloodAxeTrophyCarrier_A01` is a hostile Blood Axe Giant visual production package, not neutral/civilized Giant culture.
- Giant scale lock is explicit and unchanged: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", with approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- The character preserves Giant body mass, shoulder breadth, heavy hands, sturdy legs, large feet, and towering scale instead of becoming a scaled normal humanoid.
- Primary forms are broad harness architecture, compact back rack or yoke, heavy belt/tassets, greaves, red cloth blocks, and sparse non-graphic trophy shapes, not micro-detail.
- Trophy shapes are restrained, implied, dry, symbolic, non-graphic, and production-readable.
- Materials align with blackened iron, dark steel, scorched leather, hide/fur, oxide red cloth/paint, soot, ash, grime, and sparse aged bone/horn or broken-gear trophies.
- `MI_GIA_BloodAxeReforgedMetal_A01` is referenced as the core metal dependency.
- Neutral/civilized Giant stoneworker materials, blue-gray cave-town identity, warm hearth language, and restrained rune accents are excluded from the baseline.
- Default emissive, forge heat, ritual glow, shamanic glow, faction aura, animated material states, cloth, physics, and final socket transforms are not claimed.
- Texture maps include `BC`, `N`, `ORM`, and optional future `E` only behind approval.
- Triangle budget, material slot target, LOD0-LOD3 plan, collision planning, animation scope, Unreal import planning, folder naming, docs-only guardrails, approval gates, and quality checklist are included.
- No source concept file is copied, moved, edited, embedded, or committed.
- No DCC, FBX, Unreal Content, runtime source, validator, startup placement, source asset, wearable skeletal fit, authored animation, animation timing, cloth simulation, physics setup, AI/combat behavior, encounter role, loot rule, inventory behavior, trophy collection mechanic, final visual approval, first DCC target selection, global index edit, task-board edit, backlog edit, or bootstrap edit is claimed.
