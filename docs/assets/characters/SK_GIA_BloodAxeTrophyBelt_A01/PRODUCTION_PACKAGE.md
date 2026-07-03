# SK_GIA_BloodAxeTrophyBelt_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeTrophyBelt_A01`
- Asset type: Wearable Giant hip armor and trophy belt production package; planned skeletal gear asset only after later approval
- Source kit: `KIT_GIA_BloodAxeArmory_A01`
- Source child reference: `BloodAxeArmory.png#Armor_TrophyBeltTassets`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready
- Source-storage guardrail: keep the external source concept outside the repository. Do not copy, move, edit, embed, or commit the source image for this package.

`SK_GIA_BloodAxeTrophyBelt_A01` defines the Blood Axe Giant hip armor, heavy belt, trophy buckle, broad tassets, and controlled trophy accents for hostile raider variants. The belt should read as brutal, field-forged, and Giant-scale from MMO camera distance: a thick scorched-leather belt core, blackened iron plates, broad oxide-red cloth warnings, a few large readable trophies, and heavy side anchors. It must not become a dense curtain of dangling clutter.

Blood Axe visual language stays separate from neutral/civilized Giant culture. This package represents a hostile raider sub-faction marked by red cloth, blackened metal, soot, rough hide, and intimidating trophy display. It does not define civilized Giant stoneworker dress, highland nomad culture, or default Giant identity.

## Gameplay Purpose

This package prepares a visual hip-armor module for Blood Axe Giant raiders, elite camp guards, hunters, and future chieftain-adjacent variants. Its gameplay read is faction identification and silhouette support: players should recognize the wearer as Blood Axe through the heavy belt, tassets, large trophy shapes, red-black material blocks, and Giant-scale construction.

Expected use cases:

- Wearable hip armor module for Blood Axe Giant raider character variants after a separate DCC and wearable-fit task.
- Coordinated lower-body companion to `SK_GIA_BloodAxeRaiderChest_A01`, quivers, sidearms, and Blood Axe weapon packages.
- Optional non-interactive armory display variant only if a later task approves a display mesh.
- Material and scale reference for other Blood Axe belt tools, sidearm sheaths, quiver straps, and trophy-tag modules.

Out of scope:

- No DCC source, mesh, sculpt, retopo, UV, bake, FBX export, Unreal Content asset, validator, startup placement, runtime code, or copied concept art.
- No final wearable skeletal fit claim, skinning claim, physics setup, cloth simulation, or animation clearance claim.
- No loot, pickup, inventory, economy, crafting, armor-stat, weak-point, hit-zone, or encounter behavior.
- No gore escalation, fresh blood, explicit remains, harvesting implication, or graphic trophy treatment.

## Silhouette Notes

The belt should read as a massive Giant hip armor band first, then as Blood Axe trophy gear second. Preserve the base Giant pelvis, waist, hip, and thigh mass rather than hiding it under a noisy skirt.

Primary silhouette goals:

- Thick belt band wrapping the waist and upper hips with a strong central buckle or trophy plate.
- Large front tasset plates hanging from the belt line as broad, readable panels, not many narrow strips.
- Side hip plates or strap anchors that frame the pelvis without blocking leg motion in future review.
- One central trophy form and two to four secondary trophies maximum for the baseline `A01` read.
- Red cloth strips used as large accent blocks, ideally two or three broad pieces, not a shredded fringe curtain.
- Heavy leather strap loops, oversized iron rings, and a few large chain links only where they support the silhouette.

Model as real geometry:

- Belt band, main buckle/trophy plate, major tasset plates, side hip guards, large strap anchors, oversized rings, large chain links, and a few major trophy shapes.

Use texture, normal, or material masks for:

- Small scratches, tiny rivets, leather grain, stitch rows, minor nicks, soot speckles, small cracks, grime streaks, and fine trophy surface detail.

Avoid:

- Dense dangling teeth, tiny skull strings, charm curtains, per-link chain clutter, gore ropes, wet blood, shredded micro-cloth, and trophy clusters that hide the waist/hip read.
- Neutral/civilized Giant blue-gray stoneworker motifs, warm hearth language, refined masonry symbols, or restrained rune accents unless a separate stolen-object variant is approved.

## Scale Notes

Validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft and males 14'10"-16'0".

Author all future measurements in centimeters. 1 Unreal unit = 1 cm. Use `SK_GIA_Base_A01` as the only scale source for future build work. This docs-only package does not alter Giant base scale and does not claim the belt already fits either baseline.

Waist and hip planning targets:

- Female baseline review target: belt sized around the 442 cm body with hip breadth preserved and upper-thigh motion unobstructed.
- Male baseline review target: belt sized around the 470 cm body with larger pelvis depth and hip span preserved.
- Belt band height: 38-58 cm, depending on final buckle/tasset proportions.
- Belt thickness/protrusion from body: 8-16 cm for the leather/plate band; central trophy or buckle may project up to 24 cm if it clears crouch, bend, and weapon draw in later review.
- Belt circumference planning: author to the approved Giant pelvis mesh, not from guessed humanoid scale; allow separate male/female fit variants if one shared mesh deforms poorly.
- Front tasset length: 70-115 cm from belt lower edge, ending above or near upper thigh to preserve knee lift.
- Side tasset or hip plate length: 55-95 cm, shorter than front panels when needed to clear stride and sidearm sheaths.
- Individual trophy scale: 30-85 cm for readable large trophies; tiny trinkets should be painted or removed.
- Strap width: 10-22 cm for major leather straps; small binding cords should be texture detail unless they define an anchor point.

Attachment planning:

- Planned worn location: Giant waist, pelvis, upper hip, and upper-thigh armor zone.
- Future fit should account for pelvis, spine base, abdomen bend, thigh raise, knee lift, stride width, sidearm sheath clearance, quiver belt clearance, and two-handed weapon stance.
- Candidate future attachment or skinning ownership may involve pelvis/root alignment, upper-thigh weighted tasset panels, and an approved gear convention from `SK_GIA_Base_A01`.
- No new socket is authorized here. Candidate names such as `pelvis_belt`, `belt_trophy`, `belt_tasset_l`, and `belt_tasset_r` require separate implementation approval if the future DCC/Unreal lane needs them.
- Normal humanoid compatibility is not required.

## Materials and Color Palette

Primary Blood Axe material language:

- Blackened iron and dark steel plates from the Blood Axe reforged-metal family.
- Scorched leather and rough hide for the belt core, strap loops, and tasset backing.
- Deep oxide red cloth or dull red war-paint accents as restrained sub-faction identifiers.
- Old bone, horn, broken shield plates, cracked weapon pieces, or large trophy tokens used sparingly and non-graphically.
- Soot, ash, dried mud, oil-dark grime, rubbed metal edges, and broad hand-painted wear.
- Optional rough fur pads only if they support Giant-scale belt bulk without drifting into neutral highland dress.

Recommended palette:

- Blackened iron: `#151719` to `#2A2C2E`
- Worn dark steel: `#555A5C` to `#787B78`
- Scorched leather: `#241611` to `#4A2E20`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Old bone and horn: `#A69578` to `#D0B98C`
- Soot, ash, and grime: `#0B0A09` to `#403025`

No default emissive is approved. Forge heat, ritual glow, storm markings, or animated material states require a separate approval-gated variant and should not be assumed for `A01`.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SK_GIA_BloodAxeTrophyBelt_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant trophy belt and tasset armor module, a thick Giant-scale waist and hip band, broad readable tasset plates, blackened reforged iron, dark steel, scorched leather, rough hide, restrained deep red cloth warnings, a few large non-graphic trophies, soot, ash, preserved Giant pelvis and thigh mass, and a gameplay role as enemy raider hip armor. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a wearable gear production sheet with front, side, back, three-quarter views, waist/hip scale callouts for female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines, belt thickness callouts, tasset clearance notes, material swatches, and simplified LOD notes on a clean background. Avoid copying any existing franchise, avoid making Blood Axe gear the default Giant culture, avoid graphic gore, avoid loot or inventory imagery, avoid dense dangling trophy clutter, and avoid implying that the belt has already been fitted to a skeleton or approved as wearable.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, export, skeletal fit, or Unreal asset is created or approved by this package.

Future modeling should prioritize:

- A thick belt band with enough volume to feel Giant-made, including broad leather layers and a few blackened iron reinforcing plates.
- A large central buckle or trophy plate that becomes the main Blood Axe read without becoming graphic.
- Two or three broad front tasset panels with chunked metal or hide backing and clear negative space between the legs.
- Shorter side plates or hip anchors that support the silhouette while preserving future thigh motion.
- A small number of large trophies: aged bone/horn shapes, broken shield plate fragments, cracked weapon teeth, or carved warning tokens.
- Large buckles, rings, and chain loops only where they anchor panels or support the Blood Axe read.
- Rear belt structure that remains readable from behind but avoids overloading the lower-back and hip area with props.

Future wearable-fit gates:

- Build male and female fit checks against the validated Giant baselines before any final claim.
- Keep the pelvis and abdomen bend area simple enough for idle breathing, walk, turn, and combat stance review.
- Avoid long rigid danglers that would obviously intersect thighs or knees.
- Separate display-only and worn variants if a later review shows incompatible pivot, clearance, or silhouette needs.
- Coordinate with sidearm, quiver, and chest gear packages so the hip zone does not become overcrowded.

Texture or normal-map:

- Tiny rivets, stitch rows, fine leather pores, small bone cracks, soot speckles, pitting, small red paint flakes, minor hammer marks, and dense grime.

Do not model gore, fresh remains, dangling entrails, dense teeth strands, dozens of charm tags, or high-frequency trophy clutter.

## Texture and Material Notes

Texture set targets for a future approved build:

- `T_GIA_BloodAxeTrophyBelt_A01_BC`
- `T_GIA_BloodAxeTrophyBelt_A01_N`
- `T_GIA_BloodAxeTrophyBelt_A01_ORM`
- Optional future approval-gated `T_GIA_BloodAxeTrophyBelt_A01_E` only for a separate ritual, forge-heat, or shamanic variant

Material slot target:

- Slot 0: `MI_GIA_BloodAxeReforgedMetal_A01` for blackened iron, dark steel, hammered plates, buckles, rings, and edge-worn metal.
- Slot 1: `MI_GIA_BloodAxeScorchedLeather_A01` or future equivalent for belt core, hide backing, straps, and tasset supports.
- Slot 2: `MI_GIA_BloodAxeBoneTrophy_A01` or future equivalent for sparse bone, horn, and trophy accents.
- Optional red cloth may be merged into the leather slot through masks unless later visual approval requires a shared `MI_GIA_BloodAxeRedCloth_A01`.

Packed `ORM` plan:

- R: Ambient occlusion around belt overlaps, buckle cavities, tasset hinge points, side anchors, and trophy attachment points.
- G: Roughness high for scorched leather, old bone, soot, and matte blackened metal; slightly lower on rubbed metal edges and worn buckle contact areas.
- B: Metallic only for iron, steel, buckles, rings, chain links, and plate hardware.

Texture readability requirements:

- Use broad value separation so the belt does not become a black band around the waist.
- Keep red accents large enough to read but secondary to the belt/tasset silhouette.
- Use bone and trophy warmth sparingly so trophies do not overpower the waist armor mass.
- Avoid readable text, franchise-like symbols, loot-rarity colors, fresh blood coloring, economy tags, or inventory-state material masks.

## Triangle Budget

Target budget for a future approved mesh:

- LOD0: 7k-12k tris for the belt, central trophy plate, tassets, side anchors, and sparse trophies.
- LOD0 hero/elite ceiling: 14k tris only if additional tasset structure or a stronger central trophy silhouette is visually approved.
- Material slots: target 2-3.
- Texture resolution: 2K standard for enemy gear; 4K only for an approved named boss or close-up hero variant.

Budget distribution guidance:

- Belt band, buckle, and reinforcing plates: 30-35 percent.
- Tasset panels and hip guards: 30-35 percent.
- Straps, rings, and large chain loops: 15-20 percent.
- Sparse trophy accents and red cloth forms: 10-15 percent.

Do not spend geometry on tiny rivets, fine stitches, dense chain links, repeated small teeth, small cracks, or micro-fringe cloth.

## LOD Plan

All important future wearable meshes require LOD0-LOD3.

- LOD0: full belt band, central trophy/buckle plate, broad tassets, side hip anchors, large straps, oversized rings, sparse large trophies, red cloth blocks, broad bevels, and major Blood Axe shape breaks.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, secondary strap loops, small buckle edges, small trophy cuts, underside tasset detail, and chain-loop segmentation.
- LOD2: 35-45 percent of LOD0; simplify rear belt layering, merge small plate overlaps, flatten minor trophy forms, reduce tasset panel cuts, and collapse small straps into texture planes.
- LOD3: 15-25 percent of LOD0; preserve the thick Giant belt mass, central trophy/buckle silhouette, broad tasset read, red/black Blood Axe color blocks, and hip-width scale.

LOD reduction order:

1. Tiny rivets, stitches, scratches, pitting, and small paint flakes.
2. Minor strap loops, small knots, and secondary buckle edges.
3. Small trophy chips, little bone fragments, and minor cloth tears.
4. Under-tasset and back-side detail.
5. Secondary plate layering.
6. Chain-loop segmentation and non-silhouette bevels.
7. Small red cloth folds.

Never reduce the Giant waist/hip scale, belt thickness, central buckle/trophy read, broad tasset shape, or core Blood Axe material blocks before removing small detail.

## Collision Notes

No collision is authored or approved in this docs-only package.

Future collision planning:

- Worn gear should normally rely on the owning Giant character movement capsule and physics asset decided in a later implementation task.
- Do not add separate combat hit zones, weak points, armor bonuses, loot collision, pickup collision, or inventory interaction from this package.
- Avoid per-strap, per-chain, per-trophy, per-cloth-strip, or per-tasset collision.
- If a display-only variant is approved later, use one simple box or a few low-count convex bounds around the belt/tasset display form.
- If a wearable implementation later needs cloth or secondary motion, collision must be reviewed against pelvis, abdomen, thighs, knees, sidearm sheath, quiver, and chest-armor overlap.

Collision is a planning note only and does not validate a final wearable fit.

## Animation Notes

No animation, skeletal fitting, cloth simulation, secondary motion, physics setup, or skin-weight validation is authored or approved here.

Future approval-gated motion checks should include:

- Idle breathing and abdomen/pelvis micro-motion.
- Walk, jog, turn in place, and wide-stance combat idle.
- Hip twist, upper-body turn, and two-handed weapon windup.
- Knee lift, step-up, crouch/sit review if used by Giant animations.
- Sidearm draw, belt-tool access, quiver reach, and back-weapon clearance.
- Front tasset and side plate clearance against thighs and knees.
- Interaction between the belt, `SK_GIA_BloodAxeRaiderChest_A01`, quivers, sidearm sheaths, and future harness modules.

Rigid panels and limited weighted tassets are preferred for the first wearable pass. Any cloth strips, swinging trophies, chain motion, or physics-driven secondary movement require separate approval and focused validation.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, skeletal mesh, material instance, texture, physics asset, Blueprint, validator, or startup actor is created by this package.

Planned Unreal asset:

- Asset name: `SK_GIA_BloodAxeTrophyBelt_A01`
- Asset type: Skeletal Mesh gear candidate / wearable hip armor module after later approval
- Planned folder: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`
- Planned docs folder: `docs/assets/characters/SK_GIA_BloodAxeTrophyBelt_A01/`
- Import scale: centimeter-authored source; Unreal scale 1.0 only after future DCC/export validation
- Pivot: align to the approved Giant base body origin or future pelvis gear convention after implementation ownership is assigned
- Forward orientation: match the Giant base import convention selected by the future DCC/export task
- Collision: no separate collision by default; future display variant may use simple static bounds only
- LODs: LOD0-LOD3 required before production import approval
- Material slot count: target 2-3
- Texture list: `T_GIA_BloodAxeTrophyBelt_A01_BC`, `T_GIA_BloodAxeTrophyBelt_A01_N`, `T_GIA_BloodAxeTrophyBelt_A01_ORM`
- Optional texture: `T_GIA_BloodAxeTrophyBelt_A01_E` only for a separately approved emissive variant
- Sockets: none authored or approved here; future pelvis or belt sockets require separate approval
- Animation list: none
- Blueprint behavior: none
- Performance notes: preserve the large belt/tasset silhouette and reduce trophy clutter before adding geometry; keep material count low and avoid collision on dangling elements

Import planning constraints for a later task:

- Validate against both female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines before any wearable statement is made.
- Do not import as final wearable gear until DCC fit, skin weights, LODs, materials, and animation clearance receive their own approval.
- Do not create armor stats, equipment rules, loot behavior, inventory hooks, economy metadata, or interactive pickup logic from this package.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/characters/SK_GIA_BloodAxeTrophyBelt_A01/`
- Production package: `docs/assets/characters/SK_GIA_BloodAxeTrophyBelt_A01/PRODUCTION_PACKAGE.md`
- Related kit package: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- Related child intake: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/CHILD_ASSET_INTAKE.md`
- Related base body package: `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md`
- Related chest package: `docs/assets/characters/SK_GIA_BloodAxeRaiderChest_A01/PRODUCTION_PACKAGE.md`
- Related material package: `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/PRODUCTION_PACKAGE.md`
- Planned Unreal folder after approval only: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`

Planned future naming:

- Skeletal gear mesh: `SK_GIA_BloodAxeTrophyBelt_A01`
- Optional display mesh, if later approved: `SM_GIA_BloodAxeTrophyBelt_Display_A01`
- Material instance: `MI_GIA_BloodAxeTrophyBelt_A01`
- Shared material references: `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeScorchedLeather_A01`, `MI_GIA_BloodAxeBoneTrophy_A01`
- Textures: `T_GIA_BloodAxeTrophyBelt_A01_BC`, `T_GIA_BloodAxeTrophyBelt_A01_N`, `T_GIA_BloodAxeTrophyBelt_A01_ORM`

Do not add SourceAssets folders, Blender files, FBX exports, Unreal Content assets, runtime source, startup-scene actors, validators, copied concept files, external source edits, global index entries, task-board edits, backlog edits, or bootstrap edits from this task.

## Approval Gates

- DCC approval is required before creating meshes, Blender sources, sculpt files, retopo files, UVs, bakes, collision proxies, proof renders, or exports.
- Unreal approval is required before importing skeletal gear, display meshes, material instances, textures, LODs, physics assets, validators, or startup-scene actors.
- Wearable-fit approval is required before claiming the belt fits either Giant baseline, clears pelvis/thigh motion, supports sidearm/quiver attachments, or deforms correctly.
- Cloth and physics approval is required before adding moving cloth strips, swinging chains, dangling trophies, secondary motion, or physics setup.
- Visual approval is required before locking final belt thickness, tasset length, central trophy shape, red cloth placement, trophy density, or elite/chieftain variant language.
- Culture approval is required if Blood Axe trophy language starts replacing neutral/civilized Giant stoneworker or highland nomad language.
- Source-storage approval is required before copying, embedding, editing, or committing any external source concept.
- Gameplay approval is required before armor stats, hit zones, weak points, loot rules, inventory behavior, economy data, pickup behavior, or encounter behavior are defined.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, or bootstrap file.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Waist/hip scale, belt thickness, tasset length, trophy scale, and attachment planning are documented as future planning constraints, not final fit proof.
- Package does not claim skeletal fit, authored animation, skinning, cloth simulation, physics setup, final visual approval, or implementation completion.
- Primary forms are a thick belt, central trophy/buckle, broad tassets, hip anchors, large straps, and sparse trophies, not dense dangling clutter.
- No gore escalation, fresh blood, explicit remains, harvesting implication, loot behavior, inventory claim, economy behavior, armor stats, hit zones, or pickup logic is included.
- Materials use blackened iron, dark steel, scorched leather, oxide red cloth/paint, soot, ash, and sparse non-graphic bone/horn trophies consistently.
- Default emissive, forge heat, shamanic glow, animated material states, cloth, and physics are not claimed.
- Texture maps include `BC`, `N`, `ORM`, and optional future `E` only behind approval.
- Triangle budget, LOD0-LOD3 plan, collision planning, animation clearance checks, Unreal import planning, folder naming, approval gates, and quality checklist are included.
- The package is useful for future DCC/Unreal work without requiring reinterpretation of Giant scale, Blood Axe culture separation, trophy-density limits, or docs-only guardrails.
