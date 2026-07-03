# SK_GIA_BloodAxeForgeGuard_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeForgeGuard_A01`
- Asset type: Skeletal Mesh character production package / hostile Blood Axe Giant forge-adjacent guard visual candidate
- Task: `AET-MA-20260629-101`
- Parent route: `KIT_GIA_BloodAxeWarband_A01#ForgeGuards`
- Source route references: `BloodAxeForge.png`, `BloodAxeArmory.png`, and `BloodAxeCamp.png` as listed by the Blood Axe warband child intake
- Parent scale dependency: `SK_GIA_Base_A01`
- Related Blood Axe kits: `KIT_GIA_BloodAxeWarband_A01`, `KIT_GIA_BloodAxeArmory_A01`, `KIT_GIA_BloodAxeCamp_A01`, and `KIT_GIA_BloodAxeReforging_A01`
- Related gear/material planning: `SK_GIA_BloodAxeRaiderChest_A01`, `SK_GIA_BloodAxeHarness_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, `SK_GIA_BloodAxeGreaves_A01`, `SM_GIA_BloodAxeTrophyHelm_A01`, `SM_GIA_BloodAxeCrusherHammer_A01`, `SM_GIA_BloodAxeCleaver_A01`, and `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, runtime source, validator, startup placement, wearable skeletal fit, animation timing, final visual approval, or first build target selection is included
- Source-storage guardrail: external source concept images remain outside the repository. Do not copy, move, edit, embed, crop, rename, or commit external source concepts for this package.

`SK_GIA_BloodAxeForgeGuard_A01` defines a hostile Blood Axe Giant guard silhouette for forge yards, armory approaches, camp choke points, and production-area visual dressing. The character should read as a soot-dark, heavy, intimidating Giant tied to Blood Axe forge culture through scorched leather, blackened reforged armor, heavy gloves, apron or waist protection, broad tool/weapon carry shapes, ash staining, and deep red warning cloth.

Forge adjacency is visual production language only. This package does not define a forge workstation, crafting loop, economy object, salvage system, resource loop, heat gameplay, burn hazard, AI role, combat role, encounter behavior, abilities, stats, loot, or interaction behavior.

Blood Axe visuals must remain separate from neutral/civilized Giant culture. This package uses hostile raider language: red cloth, blackened iron, soot, rough hide, field-forged plates, crude trophies, camp intimidation, and forge grime. It must not overwrite neutral Giant mountain stoneworker identity, cave-town craft, blue-gray civic masonry, warm hearth culture, restrained blue runes, or highland nomad presentation.

## Gameplay Purpose

This package prepares a visual-only character direction for a Blood Axe Giant who reads as forge-adjacent security or intimidation in hostile camp compositions. The gameplay purpose is limited to silhouette, faction recognition, material continuity, and future production planning.

Allowed visual planning purpose:

- Establish a readable soot-dark Blood Axe Giant guard silhouette for forge, armory, and camp-adjacent scenes.
- Coordinate body, armor, apron, glove, belt, greave, helm, and optional carried-prop language against existing Blood Axe gear packages.
- Preserve the validated Giant scale lock while differentiating the Forge Guard from chieftain, shaman, hunter, raider, banner bearer, and camp sentry visual lanes.
- Define future DCC/Unreal planning requirements for scale, material slots, LODs, collision intent, sockets, and approval gates.

Out of scope:

- Forge workstation behavior, crafting, salvaging, refining, repair, economy, resource, vendor, inventory, upgrade, heat, burn, or hazard systems.
- AI, patrol logic, guard behavior, aggro logic, perception, encounter role, combat stats, ability kits, damage values, trace timing, attack arcs, loot, rewards, spawn rules, or objective logic.
- Wearable skeletal fit finalization, cloth simulation, physics setup, animation timing, montage authoring, first build target selection, final visual approval, DCC source, FBX export, Unreal Content, runtime source, validators, startup placement, or copied source concepts.

## Silhouette Notes

The Forge Guard must read first as a massive Giant, second as hostile Blood Axe, and third as forge-adjacent through soot, protection gear, and heavy utility shapes. The design should be broader and more industrial than a hunter or camp sentry, but less rank-heavy than a chieftain and less ritualized than a shaman.

Primary silhouette goals:

- Preserve validated Giant mass: tall head height, broad shoulders, thick neck, heavy chest, long arms, huge hands, sturdy legs, large feet, and grounded stance.
- Use a soot-dark upper-body profile with heavier chest protection, reinforced shoulder plates, thick forearm guards, and broad heat-scarred gloves.
- Add an apron, waist shield, or scorched hide front panel as a large vertical read, but keep pelvis and thigh movement zones visually clear for future fit review.
- Include heavy belt and harness anchors for tool/weapon carry language without defining inventory behavior.
- Use a crusher-hammer, cleaver, tongs-like visual tool, or heavy hook only as optional carried-prop silhouette language. Do not lock a final equipped weapon or tool in this package.
- Keep the head/helm silhouette blunt and protective: soot-black brow, faceguard or half-mask option, broad cheek plates, and open neck/jaw clearance.
- Use red cloth, red paint, or warning wraps in a few broad blocks at shoulder, belt, forearm, or tool carry zones.
- Use sparse dry trophy accents only where they support Blood Axe intimidation. Avoid trophy curtains, gore displays, dense tooth strings, or graphic remains.
- Forge-adjacent soot should darken edges, hands, apron, and gear, but must not turn the character into a flat black silhouette.

Avoid:

- Neutral/civilized Giant stoneworker motifs, refined cave-town craft symbols, warm hearth marks, blue-gray civic stone language, or restrained blue rune accents.
- Ogre Teknomancy, dwarf smith elegance, clean master-smith presentation, normal humanoid smith proportions, or player-facing crafting-station affordances.
- Tiny modeled rivet fields, many small hooks, dense chain curtains, micro tool clutter, per-link chains, long physics-dependent strips, readable text, loot tags, UI-like symbols, or glowing interaction markers.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Feet at world origin and orientation should follow the future Giant base import convention inherited from `SK_GIA_Base_A01`.

Planning target:

- Primary `A01` silhouette review should use the male 470 cm baseline for maximum forge-yard intimidation and equipment mass.
- Female 442 cm baseline remains required for future variant and gear-clearance review if a female or shared-fit variant is later approved.
- This package does not lock final gender, named identity, body variant, skeleton, proportions beyond the approved Giant range, or wearable fit.

Forge Guard gear scale planning:

- Chest/shoulder armor should preserve the Giant torso breadth and leave neck, upper arm, and two-handed carry zones visually clear.
- Apron or front hide panel target: broad vertical read from lower torso to upper thigh, stopping before knee motion would be obviously blocked.
- Forearm guards and gloves should be oversized enough for a forge-protection read while preserving Giant hand size and finger silhouette.
- Belt and harness bands should use Giant-scale widths consistent with `SK_GIA_BloodAxeHarness_A01`, not thin normal-humanoid straps.
- Optional hammer/cleaver/tool carry must be scaled against Giant hands and existing weapon dimensions, not normal humanoid tools.
- Back and belt carry zones must leave room for `back_large_weapon`, `belt_tool_l`, `belt_tool_r`, future quiver/back carry, and harness anchors without turning the back into clutter.

Future fit and clearance checks before implementation claims:

- Head, brow, jaw, neck, and shoulder clearance for any helm or faceguard.
- Shoulder raise, upper-body turn, two-handed grip, and heavy carry clearance.
- Apron, belt, tasset, and tool-hanger clearance around pelvis, thigh, knee, stride, crouch, and wide stance.
- Forearm guard and glove clearance around wrist rotation and large hand grip poses.
- Back carry and belt carry clearance against existing Blood Axe weapon and gear packages.
- No normal humanoid compatibility is required.

## Materials and Color Palette

Primary Blood Axe Forge Guard materials:

- Weathered Giant skin with soot, ash, scars, hand grime, and broad red war paint only where it supports the Blood Axe read.
- Blackened iron, dark steel, and hammered stolen/reforged plates using or matching `MI_GIA_BloodAxeReforgedMetal_A01`.
- Scorched leather, heat-darkened hide, rough fur pads, rawhide straps, sinew cord, and thick leather apron panels.
- Heavy gloves or wraps with darkened palms, cracked leather, and broad hand-painted wear.
- Deep oxide red cloth, dirty red wraps, chipped red paint, and warning tabs as sub-faction identifiers.
- Matte soot, ash dust, charcoal smears, oil-dark grime, rubbed metal edges, and dull steel exposure.
- Old bone, horn, broken shield fragments, or cracked weapon tokens used sparingly and non-graphically.
- Dull warm forge reflection may appear as painted color on metal or leather, but default emissive and heat-state materials are not approved.

Suggested palette:

- Blackened iron: `#151719` to `#2A2C2E`
- Worn dark steel: `#555A5C` to `#787B78`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Scorched leather: `#241611` to `#4A2E20`
- Dark hide/fur: `#1D1511` to `#3B2A1E`
- Old bone/horn: `#A69578` to `#D0B98C`
- Soot and grime: `#0B0A09` to `#403025`
- Muted ember reflection: `#8A3A19` to `#B45A24`, painted only as restrained reflected color unless a future material approval creates a heat variant

No default emissive is approved. Forge heat glow, heated metal, material pulsing, shamanic marks, glowing eyes, interaction highlights, or heat shimmer require a separate visual/material/VFX approval and are not part of this package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_GIA_BloodAxeForgeGuard_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant forge-adjacent guard silhouette, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, towering broad Giant anatomy, soot-dark heavy armor, blackened reforged iron, dark steel, scorched leather apron or waist shield, massive forearm guards and gloves, rough hide harness, deep oxide red cloth warnings, chipped red war paint, ash, charcoal grime, restrained dry bone trophies, optional heavy hammer or cleaver carry silhouette, and a gameplay role limited to visual faction recognition and forge-yard presence rather than behavior. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, sparing painted warm forge reflection only where it clarifies materials, and MMO-friendly mid-poly production design. Present it as a character production sheet with front, side, back, three-quarter views, scale markers, apron/glove/helmet callouts, material swatches, optional carried-prop silhouette callouts, LOD simplification notes, and explicit docs-only guardrails on a clean background. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid neutral/civilized Giant stoneworker motifs, avoid graphic gore, avoid forge workstation behavior, avoid crafting/economy/salvage/heat gameplay diagrams, avoid AI/combat stats/abilities/loot callouts, avoid wearable-fit claims, avoid readable text, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, sculpt, retopo, UV, bake, FBX export, Unreal Content asset, skeletal fit, cloth setup, physics setup, socket authoring, runtime behavior, or final visual approval is created or approved by this package.

Future modeling should prioritize large readable forms:

- Giant body base: preserve the head, brow, jaw, thick neck, torso, shoulders, arms, heavy hands, pelvis, sturdy legs, large feet, and grounded stance inherited from `SK_GIA_Base_A01`.
- Head/helm: model a blunt protective brow, half-faceguard, cheek plates, or soot-black helm only if eye, jaw, neck, and shoulder clearance remains visibly plausible.
- Torso armor: model broad chest protection, soot-dark shoulder plates, large leather/hide support layers, and heavy harness straps as bold forms.
- Apron/front protection: model one broad scorched leather or hide panel, optional blackened metal lower plate, and simple large ties. Avoid many small hanging tool strips.
- Arms/hands: model large forearm guards, glove cuffs, palm wraps, and wrist bands as clear protection shapes that do not hide Giant hand scale.
- Belt and lower body: coordinate with `SK_GIA_BloodAxeTrophyBelt_A01` and `SK_GIA_BloodAxeGreaves_A01` language for broad belt, tassets, knee guards, ankle collars, and heavy foot read.
- Harness/carry architecture: use large rings, hooks, straps, and belt anchors sparingly. These are visual carry markers, not inventory systems.
- Optional carried prop: if a future concept includes a hammer, cleaver, tongs-like tool, or hook, keep it separable from the character mesh and aligned to existing Blood Axe armory package rules.
- Trophy accents: use only a few large dry tokens, broken metal pieces, horn fragments, or old bone markers away from deformation zones.

Use texture, normal maps, or material masks for:

- Tiny rivets.
- Fine scratches.
- Dense pitting.
- Small hammer marks.
- Stitch rows.
- Leather pores.
- Fur strand texture.
- Minor chain scuffs.
- Soot speckles.
- Ash smears.
- Small red paint chips.
- Fine apron cracking.
- Hairline bone or metal cracks.

Future implementation gates:

- Do not claim wearable skeletal fit until a separate character/gear fit lane validates armor, apron, gloves, helm, belt, and greaves over approved Giant baselines.
- Do not merge optional weapons or forge tools into the character mesh unless a later approval chooses that production path.
- Do not author dangling straps, chain swing, apron cloth, glove physics, or secondary motion without cloth/physics approval.
- Do not solve animation timing, tool use, forge work loops, attack arcs, patrols, guard behavior, heat reactions, or workstation interaction in this model package.
- Split display-only gear, worn character elements, and carried prop dependencies if future pivots, sockets, or clearance needs diverge.

## Texture and Material Notes

Target texture families for a future approved build:

- `T_GIA_BloodAxeForgeGuard_A01_Body_BC`
- `T_GIA_BloodAxeForgeGuard_A01_Body_N`
- `T_GIA_BloodAxeForgeGuard_A01_Body_ORM`
- `T_GIA_BloodAxeForgeGuard_A01_Gear_BC`
- `T_GIA_BloodAxeForgeGuard_A01_Gear_N`
- `T_GIA_BloodAxeForgeGuard_A01_Gear_ORM`
- `T_GIA_BloodAxeForgeGuard_A01_ApronGloves_BC`
- `T_GIA_BloodAxeForgeGuard_A01_ApronGloves_N`
- `T_GIA_BloodAxeForgeGuard_A01_ApronGloves_ORM`
- `T_GIA_BloodAxeForgeGuard_A01_HairFur_BC`
- `T_GIA_BloodAxeForgeGuard_A01_HairFur_N`
- `T_GIA_BloodAxeForgeGuard_A01_HairFur_ORM`
- Optional future approval-gated `T_GIA_BloodAxeForgeGuard_A01_E`

Material slot target:

- Slot 0: body/head/skin, scars, soot, ash, and broad red war paint.
- Slot 1: hair, fur, brows, beard/braid elements, or eyes if the future base convention requires separation.
- Slot 2: `MI_GIA_BloodAxeReforgedMetal_A01` or a consuming Forge Guard gear instance for blackened iron, dark steel, chipped red paint masks, hammered plates, buckles, rings, and glove hardware.
- Slot 3: scorched leather, hide, apron, straps, red cloth, and rough wraps.
- Slot 4: optional bone/horn/trophy material only if shared atlas readability cannot support sparse trophy accents.

Target 4 material slots, 5 maximum only if eyes/hair or trophy materials must remain separate for quality and reuse. Attached weapons or separate props use their own package material targets and should not force extra character material slots.

Packed `ORM` plan:

- R: Ambient occlusion around armor overlaps, apron folds, glove cuffs, strap compression, belt/tasset hinges, greave undercuts, soot cavities, and trophy anchors.
- G: High roughness for soot, ash, scorched leather, hide, matte blackened metal, old bone, and weathered skin; slightly lower roughness on rubbed steel edges, palm-contact hardware, and worn buckles.
- B: Metallic only for iron, steel, rings, chain links, buckles, glove plates, armor plates, and weapon/tool hardware.

Texture readability requirements:

- Keep soot and ash broad, directional, and controlled so the character does not collapse into one black shape.
- Use red accents as a few strong Blood Axe markers, not a full red costume.
- Paint large heat wear, leather cracking, hammer marks, grime, and edge wear at Giant scale.
- Keep apron/glove material distinct from skin and armor through value and roughness separation.
- Avoid readable text, franchise-like symbols, loot-rarity colors, interaction highlights, heat-state UI, graphic gore, fresh blood, or material masks that imply damage types, weak points, loot state, forge state, or crafting progress.
- No baseline emissive, pulsing heat, glowing eyes, forge interaction glow, shamanic glow, or animated material state is approved.

## Triangle Budget

`SK_GIA_BloodAxeForgeGuard_A01` is a repeated hostile Giant character candidate, heavier than a common light sentry but not a named boss or chieftain.

Target budget for a future approved fully dressed character:

- LOD0 target: 58k-76k tris for body, head, hair/fur, integrated forge-guard armor, helm/faceguard, apron/gloves, harness, belt, greaves, and controlled trophies.
- LOD0 hard cap: 80k tris unless a later named hero or boss variant receives separate approval.
- Optional equipped hammer, cleaver, hook, or tool budget: use the prop's own package budget and do not include it in the character mesh budget unless a later task explicitly approves an integrated mesh.
- Material slots: 4 target, 5 maximum.
- Texture resolution: 2K standard for body and gear sets; 4K only for an approved close-up hero or named boss variant.

Budget distribution guidance:

- Body, head, hands, feet, and base anatomical forms: 42-52 percent.
- Armor plates, helm/faceguard, apron, gloves, belt, greaves, and boots: 30-38 percent.
- Harness straps, rings, buckles, red cloth, hair/fur clumps, and forge-guard silhouette breaks: 12-16 percent.
- Sparse trophies, large hooks, and secondary accents: 4-8 percent.

Do not spend geometry on tiny rivets, dense chain links, fine stitches, hair strands, micro scratches, repeated tooth strands, soot flecks, many small tools, or small gore detail.

## LOD Plan

All future character implementations require LOD0-LOD3.

- LOD0: full Giant body mass, face/helm read, hands/feet, hair/fur clumps, chest/shoulder armor, apron/gloves, harness, belt/tassets, greaves, broad red cloth markers, soot gradients, sparse large trophies, and primary Forge Guard silhouette.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small strap loops, glove cuff subdivisions, apron edge cuts, hair/fur subdivisions, small buckle edges, secondary trophy cuts, and underside armor details.
- LOD2: 35-45 percent of LOD0; simplify fingers, inner armor folds, back-side straps, tasset details, glove plate cuts, trophy forms, fur clump cuts, apron lower-edge cuts, and secondary cloth folds while preserving the forge-adjacent read.
- LOD3: 15-25 percent of LOD0; preserve height, shoulders, head/helm, huge hands, apron/glove read, weapon/carry readable zones, red/black Blood Axe material blocks, and broad stance.

LOD reduction order:

1. Tiny rivets, scratches, stitches, pitting, leather pores, soot speckles, and small paint flakes.
2. Small strap loops, knots, buckle bevels, cuff cuts, and minor chain segments.
3. Small trophy fragments, tiny bone chips, cloth tears, and apron edge cuts.
4. Under-armor and back-side detail.
5. Secondary hair/fur cuts and non-silhouette folds.
6. Minor plate bevels, glove panel subdivisions, and interior armor cuts.
7. Only after all secondary detail is reduced, simplify helm, shoulder, chest, apron, gloves, belt, hands, feet, and stance.

Never reduce the validated Giant scale read, shoulder line, heavy hands, head/helm silhouette, apron/glove identity, broad belt/tasset read, or Blood Axe red/black color blocks before removing small detail.

## Collision Notes

No collision, physics asset, hit setup, or gameplay volume is authored or approved in this docs-only package.

Future collision planning:

- Character collision type: Giant-tuned movement capsule inherited from `SK_GIA_Base_A01` conventions.
- Male 470 cm planning capsule: roughly 470 cm height and 100-125 cm radius, pending future implementation validation.
- Female 442 cm planning capsule, if a variant is approved: roughly 442 cm height and 95-115 cm radius.
- Physics asset should use simplified bodies for pelvis, spine, chest, head, upper/lower arms, hands, grouped fingers, thighs, calves, feet, and only approved large hair/fur/gear bodies.
- Worn armor, apron, gloves, trophies, hooks, and harness hardware should normally rely on the owning Giant physics asset and simple bounds, not per-strap, per-hook, per-chain, or per-trophy collision.
- Equipped hammer, cleaver, or tool props should use their own package collision guidance. This character package does not define trace arcs, hit shapes, or interaction targeting.

Do not add separate guard detection zones, combat hit zones, weak points, armor-stat collision, heat volumes, burn hazards, forge interaction volumes, crafting triggers, loot pickup collision, inventory volumes, per-chain collision, per-apron cloth collision, or per-trophy collision from this package.

## Animation Notes

No animation, Animation Blueprint, montage, authored timing, cloth simulation, secondary motion, physics setup, workstation loop, AI behavior, combat behavior, or final pose set is created or approved here.

Future approval-gated animation review may include only visual clearance planning:

- Giant base heavy idle, walk, run/jog, turn in place, and wide-stance review inherited from the base family.
- Static carry/readiness pose checks for optional hammer, cleaver, hook, or tool silhouettes.
- Glove, forearm guard, shoulder, belt, apron, and greave clearance during broad Giant motion.
- Back carry, side carry, and belt carry clearance if a separate task chooses an equipped prop.
- Apron lower-edge and cloth-strip behavior only if a separate cloth/physics task approves it.

This package does not define forge work loops, hammering timing, tool-use timing, attack cadence, damage windows, ability telegraphs, patrol behavior, guard behavior, heat reactions, interact animations, loot pickup, death behavior, or encounter scripting. Rigid gear is preferred for a first pass; dangling trophies, loose straps, apron cloth, chain swing, or glove secondary motion require separate approval and validation.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, physics asset, animation Blueprint, validator, startup actor, runtime source, or import script is created by this package.

Planned future Unreal asset:

- Asset name: `SK_GIA_BloodAxeForgeGuard_A01`
- Asset type: Skeletal Mesh character candidate
- Planned folder: `/Game/Aerathea/Characters/Giants/BloodAxe/ForgeGuard/`
- Planned skeleton dependency: future approved Giant skeleton convention inherited from `SK_GIA_Base_A01`
- Import scale: centimeter-authored source, import scale 1.0 after future DCC/export validation
- Pivot: feet at world origin, matching the Giant base convention
- Forward orientation: match the Giant base import convention selected by the future implementation task
- Collision type: Giant movement capsule plus simplified physics asset only after implementation approval
- LODs: LOD0, LOD1, LOD2, LOD3 required before production import approval
- Material slot count: 4 target, 5 maximum
- Blueprint behavior: none
- Animation list: none authored by this package
- Performance notes: preserve Giant mass, apron/glove read, and Blood Axe red/black blocks; reduce soot noise, straps, hooks, chains, and trophies before primary silhouette; avoid extra material slots for small accents.

Planned texture names:

- `T_GIA_BloodAxeForgeGuard_A01_Body_BC`
- `T_GIA_BloodAxeForgeGuard_A01_Body_N`
- `T_GIA_BloodAxeForgeGuard_A01_Body_ORM`
- `T_GIA_BloodAxeForgeGuard_A01_Gear_BC`
- `T_GIA_BloodAxeForgeGuard_A01_Gear_N`
- `T_GIA_BloodAxeForgeGuard_A01_Gear_ORM`
- `T_GIA_BloodAxeForgeGuard_A01_ApronGloves_BC`
- `T_GIA_BloodAxeForgeGuard_A01_ApronGloves_N`
- `T_GIA_BloodAxeForgeGuard_A01_ApronGloves_ORM`
- `T_GIA_BloodAxeForgeGuard_A01_HairFur_BC`
- `T_GIA_BloodAxeForgeGuard_A01_HairFur_N`
- `T_GIA_BloodAxeForgeGuard_A01_HairFur_ORM`
- Optional future `T_GIA_BloodAxeForgeGuard_A01_E` only for a separately approved emissive variant

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

- `belt_tool_heavy_l`
- `belt_tool_heavy_r`
- `apron_anchor_l`
- `apron_anchor_r`
- `harness_back_anchor`
- `harness_belt_anchor`
- `forge_tool_carry`
- `back_hammer_carry`

Potential companion assets, not selected or integrated by this package:

- `SM_GIA_BloodAxeCrusherHammer_A01`
- `SM_GIA_BloodAxeCleaver_A01`
- Future `SM_GIA_BloodAxeForgeTongs_A01` only if later approved
- Future `SM_GIA_BloodAxeForgeHook_A01` only if later approved

Import guardrails:

- Do not import a Skeletal Mesh, Static Mesh, material, texture, animation, physics asset, Blueprint, Niagara system, validator, or startup actor from this docs-only package.
- Do not add forge workstation Blueprint behavior, crafting UI, economy data, salvage data, heat volumes, damage volumes, AI data, combat traces, loot tables, or encounter logic.
- Do not claim final wearable fit, final socket contract, final animation timing, final visual approval, or final source concept approval.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/characters/SK_GIA_BloodAxeForgeGuard_A01/`
- Package: `docs/assets/characters/SK_GIA_BloodAxeForgeGuard_A01/PRODUCTION_PACKAGE.md`
- Future character folder after approval: `/Game/Aerathea/Characters/Giants/BloodAxe/ForgeGuard/`
- Future gear dependencies: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`
- Future weapon/tool dependencies: `/Game/Aerathea/Weapons/Giants/BloodAxe/` or `/Game/Aerathea/Props/Giants/BloodAxeArmory/`
- Future materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`

Recommended future names, if promoted by later tasks:

- Primary skeletal mesh: `SK_GIA_BloodAxeForgeGuard_A01`
- Optional male/female split after approval: `SK_GIA_BloodAxeForgeGuard_Male_A01`, `SK_GIA_BloodAxeForgeGuard_Female_A01`
- Gear material instance: `MI_GIA_BloodAxeForgeGuard_Gear_A01`
- Apron/glove material instance: `MI_GIA_BloodAxeForgeGuard_ApronGloves_A01`
- Optional display-only apron or glove child package only after approval: `SK_GIA_BloodAxeForgeGuardApron_A01`, `SK_GIA_BloodAxeForgeGuardGloves_A01`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, validators, startup placements, external concept folders, global indexes, task-board files, backlog files, bootstrap files, or any package outside this owned docs path from this task.

## Approval Gates and Stop Points

- Stop before final Forge Guard visual approval, final silhouette lock, first playable visual signoff, or first DCC target selection.
- Stop before creating source folders, Blender files, sculpt files, retopo files, UVs, bakes, proof renders, LOD sources, collision proxies, FBX exports, Unreal imports, material graphs, textures, Blueprints, validators, or startup placements.
- Stop before copying, moving, embedding, cropping, editing, renaming, or committing external source concepts.
- Stop before selecting a final equipped hammer, cleaver, hook, tongs, tool, or weapon for the Forge Guard.
- Stop before claiming wearable skeletal fit, male/female shared fit, socket finalization, cloth setup, apron simulation, glove deformation, physics asset tuning, or animation timing.
- Stop before defining forge workstation behavior, crafting, salvage, refining, repair, heat gameplay, burn damage, steam behavior, economy, vendor, inventory, resource, upgrade, loot, pickup, or interaction systems.
- Stop before defining AI, patrol behavior, aggro behavior, guard logic, encounter role, combat stats, abilities, damage values, attack arcs, trace timings, hit reactions, spawn rules, quest logic, or rewards.
- Stop if the asset requires changing the validated Giant scale lock or `SK_GIA_Base_A01` assumptions.
- Stop if Blood Axe red-black raider language starts replacing neutral/civilized Giant culture.
- Stop if soot, forge tools, or forge adjacency start reading as implemented gameplay instead of visual production language.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Validated Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved range females 14-15 ft and males 14'10"-16'0".
- Gameplay purpose is visual-only and does not define AI, combat stats, encounter behavior, abilities, loot, patrols, crafting, economy, salvage, heat gameplay, or workstation behavior.
- Silhouette preserves Giant body mass before adding soot-dark armor, apron/glove read, red cloth, trophies, and optional carried-prop language.
- Forge adjacency is represented through soot, ash, scorched leather, glove/apron protection, blackened metal, and heavy utility shapes only.
- Materials use blackened iron, dark steel, scorched leather, hide/fur, red cloth, soot, ash, and rough reforged-metal surfaces consistently.
- No neutral/civilized Giant stoneworker language, blue-gray civic craft, warm hearth identity, or restrained blue rune language is used as baseline.
- Tiny rivets, scratches, stitching, soot speckles, leather pores, pitting, dense chain clutter, and minor paint damage are assigned to texture or normal detail.
- Emissive use is absent by default and approval-gated for any future forge-heat, ritual, or material-state variant.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision notes, animation limits, Unreal import planning, folder/naming recommendation, approval gates, and source-storage guardrails are included.
- No DCC, FBX, Unreal Content, runtime source, validators, startup placement, final visual approval, wearable skeletal fit finalization, animation timing finalization, source concept movement, index edit, task-board edit, backlog edit, bootstrap edit, or unrelated package edit is claimed.
