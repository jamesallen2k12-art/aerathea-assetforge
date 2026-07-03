# SK_GIA_BloodAxeBannerBearer_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeBannerBearer_A01`
- Asset type: Skeletal Mesh character production package / hostile Giant banner-bearer visual planning
- Parent planning kit: `KIT_GIA_BloodAxeWarband_A01`
- Related armory dependency: `SM_GIA_BloodAxeWarBanner_A01`
- Related gear dependencies: `SK_GIA_BloodAxeHarness_A01`, `SK_GIA_BloodAxeRaiderChest_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, and `SK_GIA_BloodAxeGreaves_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Source planning row: `KIT_GIA_BloodAxeWarband_A01#BannerBearers`
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, runtime source, source asset movement, wearable-fit finalization, animation timing, cloth simulation, final visual approval, or implementation work

`SK_GIA_BloodAxeBannerBearer_A01` defines the visual production direction for a Blood Axe Giant who carries a brutal red war banner above the warband line. The design should read first as a towering hostile Giant, then as a banner carrier: massive body scale, broad Blood Axe raider gear, a heavy carry harness, a Giant-scale pole, torn red cloth, blackened iron fittings, soot-dark leather, and sparse non-graphic trophy accents.

This character belongs only to the Blood Axe hostile sub-faction. It must not become neutral/civilized Giant culture. Avoid blue-gray stoneworker pride motifs, warm cave-town hearth identity, restrained civic runes, refined masonry symbols, or highland nomad dress as the primary read.

## Gameplay Purpose

Visual role only. The banner bearer exists to make a Blood Axe warband, camp entrance, armory yard, or formation concept read clearly at MMO camera distance through vertical red banner shape language and hostile Giant scale.

Allowed planning purpose:

- Provide a readable Blood Axe formation silhouette with a carried banner and large Giant body mass.
- Define visual clearance expectations for pole grip, back/shoulder harness, torso armor, belt, greaves, and banner cloth.
- Coordinate with the existing static banner and Blood Axe armor packages without claiming final gear fit.
- Support future concept sheets, DCC handoff, and Unreal import planning after separate approvals.

Out of scope:

- AI behavior, combat stats, encounter role, patrol logic, spawn logic, objective logic, abilities, aura effects, capture mechanics, buffs, debuffs, loot, inventory, economy, crafting, faction-state gameplay, VFX pulses, audio cues, or interaction behavior.
- Final wearable skeletal fit, final socket transforms, final animation timing, cloth simulation, physics setup, DCC source creation, FBX export, Unreal import, validators, startup placement, source concept copying, or final visual approval.

## Silhouette Notes

Primary read:

- Towering Giant body with the validated Blood Axe hostile raider language.
- Tall vertical pole rising above the head and shoulder line for immediate formation readability.
- Torn red banner panel or split-tail pennant kept slightly behind or beside the upper torso so the face, chest, and shoulder mass remain readable.
- Broad raider chest and shoulder armor, heavy carry harness, thick waist belt, reinforced lower-leg armor, and a wide planted stance.
- One dominant banner pole silhouette, not multiple flags, dense streamers, or unreadable pole clusters.
- Large grip wraps, iron collars, carry rings, and harness anchor points that imply weight and scale without final socket claims.
- Sparse large trophy shapes tied to the harness or pole, kept dry, old, symbolic, and non-graphic.

Keep Blood Axe detail bold and readable. Model the Giant body forms, major armor plates, broad straps, oversized rings, pole, crossbar, large cloth planes, main tears, major bindings, and a few large trophies as geometry. Use textures or normals for small scratches, pitting, stitching, leather pores, cloth weave, tiny rivets, soot speckles, red paint chips, hairline bone cracks, and minor cloth fray.

Avoid:

- Turning the character into a scaled-up normal humanoid with a human-size banner.
- Letting the banner hide the head, hands, torso, or shoulder breadth in the main production read.
- Dense dangling chains, many tiny trophies, graphic gore, wet blood, shredded micro-cloth, readable text, or excessive spikes.
- Neutral/civilized Giant culture language as the default visual identity.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Feet at world origin for future skeletal character work unless a later implementation owner approves a different convention.

The package does not alter Giant scale and does not claim completed wearable fit. Future DCC work must validate both female and male baselines before any fit statement is made.

Banner carry planning targets:

- Total visual height from ground to banner top: roughly 650-780 cm depending on pose and variant, so the banner clears the Giant head without becoming an oversized siege mast.
- Pole length: roughly 520-660 cm for a carried variant, subject to hand, shoulder, back, and ground-clearance review.
- Pole diameter: roughly 14-26 cm, heavy enough for Giant scale and readable from MMO camera distance.
- Crossbar width: roughly 220-360 cm for a carried banner; keep slimmer than the static camp marker when needed for animation clearance.
- Cloth width: roughly 180-300 cm.
- Cloth drop: roughly 220-360 cm from crossbar to lowest torn point.
- Lower pole clearance: plan both planted-pose and carried-pose variants, but do not finalize ground contact, locomotion contact, or animation timing in this package.
- Banner offset: keep the cloth slightly rearward or side-offset from the face and upper chest in the primary pose so the character remains readable.

Harness and gear clearance planning:

- The carry harness should preserve Giant chest, back, waist, and shoulder mass.
- The pole should clear neck turn, shoulder raise, upper-body twist, belt/tasset zones, and greave/foot stance in later fit review.
- Compatibility with `SK_GIA_BloodAxeHarness_A01`, `SK_GIA_BloodAxeRaiderChest_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, `SK_GIA_BloodAxeGreaves_A01`, quivers, sidearms, or other Blood Axe props is approval-gated and not finalized here.
- Normal humanoid compatibility is not required.

## Materials and Color Palette

Primary Blood Axe materials:

- Weathered Giant skin with ash smears, scars, sun and mountain exposure, and rough war paint.
- Blackened iron, dark steel, and reforged stolen-metal plates.
- Scorched leather, rough hide, thick cord, rawhide wraps, and soot-dark strap compression.
- Torn deep red banner cloth, red war paint, dull red wraps, and dirty maroon shadowing as sub-faction identifiers.
- Bone, horn, old teeth, broken shield fragments, or dry trophy tokens used sparingly.
- Ash, soot, dried mud, oil-dark grime, rubbed metal edges, and broad hand-painted wear.

Suggested palette:

- Blackened metal: `#151719` to `#2A2C2E`
- Worn steel edges: `#555A5C` to `#787B78`
- Scorched leather: `#241611` to `#4A2E20`
- Dark hide: `#1D1511` to `#3B2A1E`
- Blood Axe red cloth/paint: `#5F1513` to `#8B211B`
- Old bone and horn: `#A69578` to `#D0B98C`
- Soot, ash, and grime: `#0B0A09` to `#403025`

No default emissive is approved. Forge heat, ritual glow, shamanic glow, faction aura, animated material states, VFX pulses, or magical banner states require separate approval and are not part of this package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_GIA_BloodAxeBannerBearer_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant banner bearer, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, towering body mass, broad raider armor, heavy carry harness, a Giant-scale banner pole, torn deep red war cloth, blackened iron collars, scorched leather straps, rough hide, sparse dry bone or horn trophies, soot, ash, red war paint, clear pole and harness clearance callouts, and a visual role as a hostile warband formation marker. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a character production sheet with front, side, back, three-quarter views, banner-pole grip callouts, harness clearance callouts, material swatches, and scale bars beside the 442 cm female and 470 cm male Giant baselines on a clean background. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid graphic gore, avoid readable text, avoid cloth-simulation claims, avoid faction aura or capture mechanic imagery, avoid combat-stat or ability diagrams, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, sculpt, retopo, UV, bake, FBX export, Unreal asset, skeletal fit, socket, cloth setup, animation, physics asset, or final visual approval is created or authorized by this package.

Future modeling should prioritize:

- Reuse the approved Giant base body scale and preserve towering height, shoulder breadth, hand size, heavy feet, and broad stance.
- Build Blood Axe raider gear as large readable modules: chest armor, harness, belt/tassets, greaves, and carry hardware.
- Keep the banner pole as a major silhouette form with large grip wraps, iron collars, crossbar, and optional carry sleeve.
- Treat the carried banner as a separate attached prop candidate where practical, derived from the `SM_GIA_BloodAxeWarBanner_A01` language but adjusted for carried scale only after approval.
- Use static shaped cloth geometry for the banner in this planning package. Do not claim cloth simulation, wind behavior, destructible cloth, or runtime motion.
- Place the pole and cloth so the head, hands, upper torso, and Blood Axe gear read clearly from front and three-quarter camera angles.
- Keep harness anchor geometry large and sparse: a few oversized back rings, shoulder straps, belt ties, or pole sleeves rather than dense hardware.
- Use a few large non-graphic trophy accents, avoiding trophy curtains or skull clutter.
- Separate display-only, worn, and carried variants if a later DCC review shows incompatible pivots, clearance, or performance needs.

Texture or normal-map:

- Tiny rivets, stitch rows, leather pores, cloth weave, small scratches, pitting, soot speckles, paint chips, hairline cracks, minor cloth fray, small nail heads, and fine wood grain.

Future clearance gates:

- The pole must clear neck and shoulder motion, upper-body twist, back carry zones, belt/tasset mass, thigh motion, and lower-leg stance in a later approved fit review.
- Banner cloth must not obscure the character's main read or require simulated cloth to look acceptable.
- Any overlap with chest armor, harness, trophy belt, greaves, quivers, weapons, or sidearms must be resolved in a later attachment review.

## Texture and Material Notes

Use standard Aerathea texture outputs: `BC`, `N`, packed `ORM`, and optional `E` only for a separately approved emissive variant.

Character texture planning:

- `T_GIA_BloodAxeBannerBearer_A01_Body_BC`
- `T_GIA_BloodAxeBannerBearer_A01_Body_N`
- `T_GIA_BloodAxeBannerBearer_A01_Body_ORM`
- `T_GIA_BloodAxeBannerBearer_A01_Gear_BC`
- `T_GIA_BloodAxeBannerBearer_A01_Gear_N`
- `T_GIA_BloodAxeBannerBearer_A01_Gear_ORM`
- Optional future `T_GIA_BloodAxeBannerBearer_A01_E` only for an approved ritual, forge-heat, or shamanic variant

Banner texture planning:

- Reuse `T_GIA_BloodAxeWarBanner_A01_BC`, `T_GIA_BloodAxeWarBanner_A01_N`, and `T_GIA_BloodAxeWarBanner_A01_ORM` if the carried banner remains compatible with the static banner material family.
- Use `T_GIA_BloodAxeBannerBearer_A01_Banner_BC`, `T_GIA_BloodAxeBannerBearer_A01_Banner_N`, and `T_GIA_BloodAxeBannerBearer_A01_Banner_ORM` only if later art approval requires a carried-specific banner texture set.
- No banner emissive texture by default.

Material slot targets:

- Character target: 4-5 slots excluding a separate attached banner prop.
- Slot 0: Giant body/head/skin.
- Slot 1: eyes if inherited from the base character setup.
- Slot 2: hair/fur.
- Slot 3: Blood Axe leather, cloth, hide, and red paint.
- Slot 4: blackened iron, dark steel, bone, horn, and trophy hardware if not merged through shared masks.
- Separate attached banner prop target: 2 slots, `MI_GIA_BloodAxeRedCloth_A01` and `MI_GIA_BloodAxeBannerHardware_A01`.

Shared material family references:

- `MI_GIA_BloodAxeReforgedMetal_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeScorchedLeather_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeBoneTrophy_A01`
- `MI_GIA_BloodAxeSootAsh_A01`

Packed `ORM` plan:

- R: Ambient occlusion around strap crossings, plate overlaps, pole grips, banner bindings, cloth folds, belt anchors, greave straps, and trophy contact points.
- G: High roughness for cloth, leather, hide, soot, and matte bone; medium-high varied roughness for blackened iron and rubbed steel edges.
- B: Metallic only for metal plates, rings, buckles, collars, chain links, pole hardware, and reforged steel.

## Triangle Budget

Target LOD0 budget for a future approved complete character:

- Fully dressed Blood Axe banner bearer excluding separate banner prop: 55k-72k tris.
- Carried banner attachment or carried banner prop candidate: 4k-8k tris.
- Total visual preview target including character and carried banner: 60k-80k tris.
- Hard ceiling: 85k tris only if the character is approved as a hero or close-up showcase variant.
- Material slots: character 4-5 target, separate banner 2 target; avoid exceeding 6 total visible slots without approval.
- Texture resolution: 2K standard for repeated enemy use; 4K only for approved named hero or close-up presentation.

Budget distribution guidance:

- Giant body, head, hands, hair, and base forms: inherited from `SK_GIA_Base_A01` guidance.
- Raider chest, harness, belt, greaves, and carry hardware: prioritize broad silhouettes over ornament.
- Banner pole, crossbar, cloth outline, major tears, and primary bindings: spend geometry only where it affects the read.
- Trophies, chains, red strips, and secondary straps: keep sparse and reduce before adding more detail.

Do not spend geometry on tiny rivets, dense chain links, small cloth fray, repeated trophy fragments, fine stitches, small scratches, pitting, wood grain, or minor paint chips.

## LOD Plan

All important future meshes require LOD0-LOD3.

- LOD0: full Giant body read, face/hands, raider chest, harness, belt/tassets, greaves, pole, crossbar, static cloth shape, major banner tears, large grip wraps, primary Blood Axe red blocks, and sparse trophy accents.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small buckle edges, secondary strap loops, cloth edge cuts, small trophy undercuts, chain segmentation, and back-side hardware.
- LOD2: 35-45 percent of LOD0; simplify rear harness layering, merge smaller armor plates, flatten minor cloth folds, reduce trophy forms, reduce finger and underside detail, and collapse non-silhouette straps into texture.
- LOD3: 15-25 percent of LOD0; preserve Giant height, head/shoulder read, pole line, red banner block, chest/harness mass, wide stance, and broad Blood Axe color identity.

LOD reduction order:

1. Tiny rivets, stitches, scratches, pitting, and cloth weave.
2. Small strap loops, knots, and buckle bevels.
3. Minor cloth holes, small tear cuts, and interior cloth folds.
4. Secondary trophy chips, small bone fragments, and chain segmentation.
5. Back-side harness detail and non-visible pole hardware.
6. Under-spaulder, under-belt, and underside boot detail.
7. Non-silhouette armor bevels.

Never reduce the Giant scale read, broad shoulder line, head silhouette, heavy hands, pole silhouette, torn red banner block, or primary Blood Axe red/black identity before removing small detail.

## Collision Notes

No collision is authored or approved by this docs-only package.

Future collision planning:

- Character movement should inherit the Giant-tuned capsule expectations from `SK_GIA_Base_A01`: female baseline around 442 cm tall and male baseline around 470 cm tall, with radius review for armor and banner offset.
- Worn armor and harness should normally rely on the owning Giant character collision and future physics asset, not per-strap or per-ring collision.
- The carried banner should normally have no gameplay collision while worn. Cloth should not block movement, navigation, traces, or camera.
- Pole and banner preview collision, if ever needed for editor display, should use a simple capsule or low-count bounds only after approval.
- Avoid per-cloth-strip, per-trophy, per-chain, per-ring, per-buckle, or per-pole-hardware collision.

Not authorized here:

- Combat hit shapes, damage zones, weak points, trace arcs, banner objective collision, capture zones, aura volumes, buff/debuff volumes, destructible pieces, nav blockers, interaction boxes, physics bodies, or cloth collision.

## Animation Notes

No animation, montage, timing, cloth simulation, secondary motion, physics setup, AI behavior, or gameplay state is authored or approved here.

Future approval-gated visual clearance checks may include:

- Static front, side, back, and three-quarter carry poses.
- Heavy idle posture with the pole held near the shoulder or side of the body.
- Walk, turn-in-place, upper-body twist, hand repositioning, and broad stance checks strictly for visual clearance.
- Shoulder, elbow, wrist, hand, neck, torso, pelvis, thigh, knee, ankle, and foot clearance against the pole, harness, belt, greaves, and banner cloth.
- Banner pole hold and harness support checks against `hand_r_weapon`, `hand_l_offhand`, `back_large_weapon`, and future approval-gated banner attachment references.

The carried cloth remains a static shaped visual plan. No banner waving, cloth simulation, wind animation, vertex sway, destructibility, animation timing, or final pose library is approved by this package.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, socket, physics asset, animation Blueprint, validator, runtime source, or startup actor is created or authorized by this package.

Planned future import target after approval:

- Asset name: `SK_GIA_BloodAxeBannerBearer_A01`
- Asset type: Skeletal Mesh character candidate / hostile Blood Axe Giant banner-bearer visual package
- Planned folder: `/Game/Aerathea/Characters/Giants/BloodAxe/Warband/`
- Gear folder reference: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`
- Prop/banner folder reference: `/Game/Aerathea/Props/Giants/BloodAxeArmory/`
- Material folder reference: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Skeleton policy: inherit the approved Giant base skeleton policy only after a later fit task validates male/female baselines and carried-banner clearance.
- Pivot: feet at world origin for the skeletal character; separate banner prop pivot follows the later approved carried-banner convention.
- Orientation: face +X unless a future DCC/export task confirms another project convention.
- Scale: centimeter-authored source; Unreal import scale 1.0 after DCC/export approval.
- Collision: use Giant character capsule and later physics asset planning; no separate banner gameplay collision by default.
- LODs: LOD0-LOD3 required before production import approval.
- Material slot count: 4-5 for character target, 2 for separate banner target.
- Blueprint behavior: none.
- Animation list: none authored or finalized.

Existing Giant base socket references for later review:

- `hand_r_weapon`
- `hand_l_offhand`
- `hand_r_twohand_grip`
- `hand_l_twohand_grip`
- `back_large_weapon`
- `back_shield`
- `belt_tool_l`
- `belt_tool_r`
- `chest_talisman`

Candidate future banner references, approval-gated only:

- `banner_carry`
- `banner_lower_grip`
- `banner_upper_grip`
- `banner_harness_anchor`
- `banner_pole_top`
- `banner_pole_base`
- `banner_cloth_anchor_l`
- `banner_cloth_anchor_r`

No new socket names, socket transforms, animation offsets, attachment rules, Blueprint behavior, aura logic, capture logic, VFX hooks, cloth setup, or gameplay traces are authorized by this package.

## Folder and Naming Recommendation

Docs:

- `docs/assets/characters/SK_GIA_BloodAxeBannerBearer_A01/PRODUCTION_PACKAGE.md`

Related docs:

- `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/CHILD_ASSET_INTAKE.md`
- `docs/assets/props/SM_GIA_BloodAxeWarBanner_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_GIA_BloodAxeHarness_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_GIA_BloodAxeRaiderChest_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_GIA_BloodAxeTrophyBelt_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_GIA_BloodAxeGreaves_A01/PRODUCTION_PACKAGE.md`

Planned future paths after separate approval only:

- Source: `SourceAssets/Blender/Characters/Giants/BloodAxe/Warband/SK_GIA_BloodAxeBannerBearer_A01/`
- Export: `SourceAssets/Exports/Characters/Giants/BloodAxe/Warband/SK_GIA_BloodAxeBannerBearer_A01.fbx`
- Unreal: `/Game/Aerathea/Characters/Giants/BloodAxe/Warband/`

Planned future naming:

- Skeletal mesh: `SK_GIA_BloodAxeBannerBearer_A01`
- Optional male variant, if later split: `SK_GIA_BloodAxeBannerBearer_Male_A01`
- Optional female variant, if later split: `SK_GIA_BloodAxeBannerBearer_Female_A01`
- Optional separate carried banner prop, if later approved: `SM_GIA_BloodAxeWarBanner_Carried_A01`
- Material instance: `MI_GIA_BloodAxeBannerBearer_A01`
- Character textures: `T_GIA_BloodAxeBannerBearer_A01_Body_BC`, `T_GIA_BloodAxeBannerBearer_A01_Body_N`, `T_GIA_BloodAxeBannerBearer_A01_Body_ORM`, `T_GIA_BloodAxeBannerBearer_A01_Gear_BC`, `T_GIA_BloodAxeBannerBearer_A01_Gear_N`, `T_GIA_BloodAxeBannerBearer_A01_Gear_ORM`
- Optional carried banner textures only if required: `T_GIA_BloodAxeBannerBearer_A01_Banner_BC`, `T_GIA_BloodAxeBannerBearer_A01_Banner_N`, `T_GIA_BloodAxeBannerBearer_A01_Banner_ORM`

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, proof renders, FBX exports, Unreal Content assets, runtime source, tools, validators, startup actors, copied source concepts, external source edits, global index entries, task-board edits, backlog edits, or bootstrap edits from this task.

## Approval and Stop Gates

- Stop before any DCC source, sculpt, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, material instance, texture asset, validator, runtime source, Blueprint, socket authoring, animation asset, or startup placement work.
- Stop before copying, moving, editing, embedding, or committing any external source concept.
- Stop if the character starts reading as neutral/civilized Giant culture instead of hostile Blood Axe sub-faction.
- Stop before final visual approval claims. This package defines production direction, not approved final art.
- Stop before claiming wearable skeletal fit, male/female fit completion, harness compatibility, banner attachment compatibility, final socket transforms, final carry offsets, physics setup, or deformation correctness.
- Stop before cloth simulation, wind animation, vertex sway, cloth collision, destructible cloth, dangling secondary physics, swinging chains, or banner waving.
- Stop before faction aura, capture mechanic, rally effect, buff, debuff, objective logic, interactable behavior, VFX pulse, audio cue, or material-state gameplay.
- Stop before AI, combat stats, encounter role, spawn logic, patrol logic, aggro logic, ability behavior, projectile behavior, damage traces, hit zones, weak points, loot, inventory, economy, crafting, or reward rules.
- Stop if the package would require edits outside `docs/assets/characters/SK_GIA_BloodAxeBannerBearer_A01/PRODUCTION_PACKAGE.md` for this task.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, or bootstrap file.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Gameplay purpose is visual role only: formation readability, hostile camp recognition, and production planning.
- No AI, combat stats, abilities, encounter role, capture mechanic, aura, buffs, debuffs, loot, inventory, economy, objective logic, or interaction behavior is defined.
- Banner carry, pole grip, pole height, and harness clearance remain visual planning only.
- No wearable skeletal fit, final socket transform, final animation timing, cloth simulation, physics setup, or final visual approval is claimed.
- Silhouette reads at MMO camera distance: towering Giant, broad raider gear, vertical pole, torn red banner, heavy harness, and wide planted stance.
- Materials use blackened iron, dark steel, scorched leather, rough hide, oxide red cloth/paint, soot, ash, and sparse non-graphic bone or horn trophies consistently.
- Default emissive, ritual glow, forge heat, shamanic glow, animated material states, faction aura, and gameplay VFX are absent and approval-gated.
- Tiny rivets, stitches, scratches, pitting, cloth weave, fray, soot speckles, and small paint chips are assigned to textures or normals.
- Triangle budget, texture maps, material slot targets, LOD0-LOD3 plan, collision planning, animation limits, Unreal import planning, folder naming, approval gates, and stop gates are included.
- Source concepts remain external and are not copied, moved, edited, embedded, or committed.
- The package is useful for future DCC/Unreal work without requiring reinterpretation of Giant scale, Blood Axe culture separation, banner clearance limits, or docs-only guardrails.
