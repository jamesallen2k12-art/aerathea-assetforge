# SK_GIA_BloodAxeRaiderChest_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeRaiderChest_A01`
- Asset type: Wearable Giant armor module production package; planned skeletal gear asset only after later approval
- Source kit: `KIT_GIA_BloodAxeArmory_A01`
- Source child reference: `BloodAxeArmory.png#Armor_RaiderPlateSpaulder`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready
- Source-storage guardrail: the external source concept remains outside the repository. Do not copy, move, edit, embed, or commit it for this package.

`SK_GIA_BloodAxeRaiderChest_A01` defines a brutal chest, harness, and spaulder armor module for Blood Axe Giant raiders. The design should read as stolen and reforged plates strapped over a massive Giant torso: broad blackened iron planes, oversized shoulder armor, rough leather compression straps, red war-cloth accents, bone or trophy anchors used sparingly, and heavy soot-darkened wear. This is not neutral Giant culture. Blood Axe gear belongs to a hostile raider sub-faction and must stay visually separate from civilized Giant stoneworker and highland nomad packages.

The armor must preserve the approved Giant body mass. It should not turn the Giant into a small humanoid scaled upward, hide the breadth of the chest under dense ornament, or replace the race silhouette with trophy clutter. The primary read is a huge torso and shoulder line with jagged Blood Axe reinforcement, not a wall of tiny spikes.

## Gameplay Purpose

This package prepares a wearable torso/spaulder armor module for Blood Axe Giant raider enemies, elite camp guards, warband variants, and future chieftain-adjacent armor sets. It supports visual identification at MMO camera distance by making the upper body read as hostile Blood Axe while preserving the base Giant scale, posture, and mass.

Expected use cases:

- Standard Blood Axe raider chest and shoulder armor.
- Heavier elite raider variant with more prominent spaulders, still within the same material language.
- Camp, armory, or equipment-preview display once a later task creates actual meshes.
- Shared material dependency for Blood Axe reforged metal, scorched leather, red cloth, and restrained bone trophy accents.

Out of scope for this task: DCC geometry, FBX export, Unreal import, skeletal fit implementation, cloth simulation, physics setup, animation authoring, gameplay stats, loot rules, startup placement, and final visual approval.

## Silhouette Notes

The silhouette should build from a massive Giant torso first:

- Wide upper chest mass remains visible around and between armor plates.
- Main breastplate is broad and asymmetrical, with a broken reforged plate edge and a strong central dark-metal mass.
- Spaulders are large enough for Giant shoulders, but they must clear the neck, upper arm, and weapon-swing envelope in a future fit pass.
- One spaulder may be heavier and more jagged for Blood Axe asymmetry; the opposite side can use layered strap, fur, or smaller plate support.
- Thick leather harness bands wrap over the sternum, ribs, and back as large readable forms.
- Red cloth warning strips or paint marks should break the blackened metal, but remain secondary accents.
- Bone trophies, skull fragments, teeth, or chain hooks should be few, large, and readable, not repeated as dense noise.

Avoid:

- Trophy clusters that hide Giant anatomy.
- Thin normal-humanoid shoulder armor proportions.
- Tiny modeled rivet fields, dense chain curtains, or many dangling charms.
- Civilized Giant blue-gray stoneworker motifs, warm hearth identity, or restrained rune language unless a later stolen-object variant is approved.
- Graphic gore or wet blood treatment.

## Scale Notes

Giant scale lock: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

Use the validated `SK_GIA_Base_A01` body as the only scale source for future work. Author in centimeters; 1 Unreal unit = 1 cm. This package does not change the base Giant scale or claim a completed wearable fit.

Torso and spaulder planning targets:

- Female baseline fit review: 442 cm tall body with full shoulder breadth preserved.
- Male baseline fit review: 470 cm tall body with larger chest depth and shoulder span preserved.
- Chest armor height target: roughly from upper pectoral/clavicle zone to upper abdomen, leaving waist and hip motion readable.
- Main chest plate width target: broad enough to read as Giant armor, but not so wide that the arms look blocked at rest.
- Spaulder width target: oversized and hostile, but with future approval required for neck, clavicle, upper-arm, bow-draw, and two-handed weapon clearance.
- Strap width target: thick Giant-scale bands; small straps should be texture or secondary forms, not a web of fine geometry.
- Trophy scale target: a small number of oversized readable trophies. Normal-sized trinkets should be avoided or painted into texture detail.

Approval-sensitive fit areas:

- Neck and head turn clearance.
- Shoulder raise, swing windup, and two-handed weapon grip clearance.
- Bow draw and quiver reach clearance for archer variants.
- Chest breathing/idle deformation clearance if later implemented.
- Back plate and harness clearance with `back_large_weapon`, `back_shield`, and future quiver attachments.
- Waist bend and upper-spine twist visibility.

## Materials And Color Palette

Primary material language:

- Blackened iron and dark steel using `MI_GIA_BloodAxeReforgedMetal_A01`.
- Reforged stolen plates with broad hammer marks and uneven welded seams.
- Scorched dark leather, hide, and rough strap bindings.
- Deep oxide red cloth strips or red war paint as restrained Blood Axe identifiers.
- Bone, horn, teeth, or skull-fragment trophies used sparingly.
- Soot, ash, dull grime, and worn edge exposure.
- Optional fur trim only as rough raider insulation, not civilized highland dress.

Suggested color ranges:

- Blackened metal: `#151719` to `#2A2C2E`
- Worn steel edges: `#555A5C` to `#787B78`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Scorched leather: `#241611` to `#4A2E20`
- Old bone: `#A69578` to `#D0B98C`
- Soot and grime: `#0B0A09` to `#403025`

No default emissive is approved. Forge heat, shamanic glow, ritual paint glow, or animated material states require a separate approval-gated variant and must not be assumed here.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SK_GIA_BloodAxeRaiderChest_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant raider torso and spaulder armor module, a massive readable Giant chest silhouette, oversized but shoulder-clear spaulders, blackened reforged iron, dark steel, scorched leather harness straps, restrained deep red war cloth and paint, sparse large bone trophies, soot, ash, field-forged brutality, preserved Giant body mass, and a gameplay role as enemy raider armor. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a wearable armor production sheet with front, side, back, three-quarter views, broad fit callouts over female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines, shoulder-clearance callouts, material swatches, and simplified LOD notes on a clean background. Avoid copying any existing franchise, avoid making Blood Axe gear the default Giant culture, avoid graphic gore, avoid dense dangling trophy clutter, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, export, skeletal fit, or Unreal asset is created or approved by this package.

Future modeling should prioritize:

- Main chest plate as a large readable metal mass with broad bevels and asymmetrical reforged edges.
- Separate left and right spaulder forms with clear shoulder mass, few large plate layers, and strong top-down read.
- Heavy back harness, upper-spine strap crossing, and rear plate silhouette that still allows large weapon/back attachment planning.
- Thick leather bands as real geometry only when they define the silhouette or major support structure.
- Large buckles, rings, and plate anchors as sparse geometry.
- A small number of large trophy elements placed where they do not block shoulder/neck motion.
- Optional fur/hide pads under plates as chunky clumps, not hair-strand geometry.

Texture or normal-map:

- Tiny rivets.
- Fine scratches.
- Dense pitting.
- Small hammer marks.
- Thin stitch lines.
- Leather pores.
- Hairline cracks.
- Minor soot speckles.
- Small red paint chips.
- Small chain clutter.

Wearable-fit modeling gates for a later approved implementation:

- Fit over the Giant torso without shrinking the chest, waist, neck, or shoulder proportions.
- Preserve clear negative space around the neck and upper arms.
- Keep spaulder underside simple enough to avoid clipping during shoulder raise.
- Avoid long dangling strips unless a later cloth or rigid secondary pass is approved.
- Separate display-only and worn variants if future review shows incompatible pivot, clearance, or silhouette needs.

## Texture And Material Notes

Texture set targets for a future approved build:

- `T_GIA_BloodAxeRaiderChest_A01_BC`
- `T_GIA_BloodAxeRaiderChest_A01_N`
- `T_GIA_BloodAxeRaiderChest_A01_ORM`
- Optional future approval-gated `T_GIA_BloodAxeRaiderChest_A01_E`

Material slot target:

- Slot 0: `MI_GIA_BloodAxeReforgedMetal_A01` for blackened iron, dark steel, edge wear, hammered plates, and chipped red paint masks.
- Slot 1: `MI_GIA_BloodAxeScorchedLeather_A01` or future equivalent for harness straps, hide pads, and binding.
- Slot 2: `MI_GIA_BloodAxeBoneTrophy_A01` or future equivalent for sparse trophy accents.
- Optional shared red cloth material may be merged into the leather/cloth slot unless later visual approval requires separation.

Packed `ORM` plan:

- R: Ambient occlusion around plate overlaps, strap compression, back harness layers, trophy anchors, and under-spaulder shadow.
- G: Roughness biased high for soot-dark metal and leather; slightly lower on rubbed metal edges and hand-contact strap hardware.
- B: Metallic only for metal plates, buckles, rings, and edge-worn steel.

Texture readability requirements:

- Use broad red marks and edge wear to support the silhouette, not fine random noise.
- Keep soot and grime from flattening the chest plate into a single black shape.
- Paint large hammering and reforged seams at Giant scale.
- Keep trophy material warm and matte so bone accents do not overpower the armor mass.
- Avoid readable text, franchise-like symbols, or repeated tiny decals.

## Triangle Budget

Target budget for a future approved mesh:

- LOD0: 8k-14k tris for the chest, harness, and spaulder module.
- LOD0 hero/elite variant ceiling: 16k tris only if additional spaulder structure or back harness forms are approved.
- Material slots: target 2-3 slots.
- Texture resolution: 2K standard for enemy armor; 4K only for an approved named hero or boss close-up variant.

Budget distribution guidance:

- Chest and back plates: 30-35 percent.
- Spaulders: 25-30 percent.
- Harness straps and buckles: 20-25 percent.
- Trophy accents, fur/hide pads, and secondary plate details: 10-15 percent.

Do not spend geometry on tiny rivets, dense chain links, fine stitches, small chips, or repeated trophy fragments.

## LOD Plan

All important future wearable meshes need LOD0-LOD3.

- LOD0: full primary chest plate, back harness, large spaulders, major straps, sparse trophy anchors, broad bevels, and large Blood Axe shape breaks.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small buckle edges, secondary strap loops, small trophy cuts, and underside spaulder detail.
- LOD2: 35-45 percent of LOD0; simplify back-side harness complexity, merge small plate layers, flatten minor trophy forms, and reduce fur/hide clump cuts.
- LOD3: 15-25 percent of LOD0; preserve chest mass, shoulder width, red/black Blood Axe color blocks, and one or two major silhouette breaks.

LOD reduction order:

1. Tiny rivets, stitches, and surface chips.
2. Minor strap loops and small buckles.
3. Secondary trophy cuts and small bone fragments.
4. Under-spaulder detail.
5. Back-side plate layering.
6. Small cloth tears or fur cuts.
7. Secondary bevels on non-silhouette plates.

Never reduce the Giant shoulder line, chest width, torso mass, or major Blood Axe red/black read before removing small detail.

## Collision Notes

No collision is authored or approved in this docs-only package.

Future collision planning:

- Worn armor should normally rely on the owning Giant character movement and hit setup decided in a later implementation task.
- Do not add separate combat hit zones, weak points, armor bonuses, or damage behavior from this package.
- Preview or display variants, if approved later, should use simple box or low-count convex bounds around the chest display form.
- Avoid per-strap, per-chain, per-trophy, or cloth-strip collision.
- Shoulder and back bounds must be reviewed only after an actual wearable-fit task exists.

## Animation Notes

No animation, skeletal fitting, cloth simulation, secondary motion, or physics setup is authored or approved here.

Future approval-gated motion checks should include:

- Idle breathing and upper-spine twist readability.
- Shoulder raise on both arms.
- One-handed heavy attack windup.
- Two-handed axe or hammer grip.
- Bow draw and quiver reach for archer variants.
- Turn-in-place and upper-body aim offsets if used by Blood Axe raiders.
- Back carry clearance for large weapon, shield, or quiver attachments.

Rigid straps and trophies should be preferred for the first wearable pass. Any cloth strips, dangling trophies, chain swing, or secondary motion require a separate approval and validation pass.

## Unreal Import Notes

This section is planning only. No Unreal Content, skeletal mesh asset, material instance, Blueprint, physics asset, validator, or startup actor is created by this package.

Planned Unreal folder after later approval:

- `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`

Planned asset naming:

- Wearable mesh: `SK_GIA_BloodAxeRaiderChest_A01`
- Optional display mesh, if later approved: `SM_GIA_BloodAxeRaiderChest_Display_A01`
- Planned material instances:
  - `MI_GIA_BloodAxeReforgedMetal_A01`
  - `MI_GIA_BloodAxeScorchedLeather_A01`
  - `MI_GIA_BloodAxeBoneTrophy_A01`

Planned texture names:

- `T_GIA_BloodAxeRaiderChest_A01_BC`
- `T_GIA_BloodAxeRaiderChest_A01_N`
- `T_GIA_BloodAxeRaiderChest_A01_ORM`
- Optional future `T_GIA_BloodAxeRaiderChest_A01_E`

Import planning constraints for a later task:

- Scale: centimeter-authored, import scale 1.0 only after DCC/export rules are approved.
- Pivot: align to the approved Giant base body origin or future gear attachment convention after implementation ownership is assigned.
- Material slot count: 2-3 slots target.
- Sockets: no new sockets are authorized here. Future fit work must validate against the Giant base torso, shoulder, back, and existing gear attachment assumptions.
- LODs: LOD0-LOD3 required before production import approval.
- Collision: no separate collision unless a later display or gameplay task explicitly approves it.
- Performance: keep the asset within enemy NPC armor budgets and avoid extra material slots for small trophies.

## Folder And Naming Recommendation

- Docs folder: `docs/assets/characters/SK_GIA_BloodAxeRaiderChest_A01/`
- Production package: `docs/assets/characters/SK_GIA_BloodAxeRaiderChest_A01/PRODUCTION_PACKAGE.md`
- Related kit package: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- Related child intake: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/CHILD_ASSET_INTAKE.md`
- Related base body package: `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md`
- Related material package: `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/PRODUCTION_PACKAGE.md`
- Planned Unreal folder after approval only: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`

Do not add SourceAssets folders, Blender files, FBX exports, Unreal Content assets, runtime source, startup-scene actors, validators, copied concept files, or global index entries from this task.

## Approval Gates

- DCC approval is required before creating meshes, Blender sources, sculpt files, retopo files, UVs, bakes, or exports.
- Unreal approval is required before importing skeletal gear, display meshes, material instances, textures, LODs, physics assets, validators, or startup-scene actors.
- Wearable-fit approval is required before claiming the armor fits either Giant baseline, clears shoulders, supports back attachments, or deforms correctly.
- Cloth and physics approval is required before adding moving cloth strips, swinging chains, dangling trophies, secondary motion, or any physics setup.
- Visual approval is required before locking final spaulder size, trophy density, red cloth placement, or elite/chieftain variant language.
- Culture approval is required if Blood Axe red-black raider armor starts replacing neutral/civilized Giant stoneworker or highland nomad language.
- Source-storage approval is required before copying, embedding, or committing any external source concept.
- Gameplay approval is required before armor stats, hit zones, weak points, loot rules, or encounter behavior are defined.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, or global index file.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Armor preserves Giant body mass, chest width, shoulder breadth, neck readability, and upper-body silhouette.
- Torso and spaulder scale notes include shoulder clearance and wearable-fit approval gates.
- Primary forms are broad chest plates, spaulders, harness straps, and sparse trophies, not micro-detail.
- Materials use blackened iron, dark steel, scorched leather, oxide red cloth/paint, soot, ash, and sparse bone trophies consistently.
- `MI_GIA_BloodAxeReforgedMetal_A01` is referenced as the core metal dependency.
- Default emissive, forge heat, shamanic glow, animated material states, cloth, and physics are not claimed.
- Texture maps include BC, N, ORM, and optional future E only behind approval.
- Triangle budget, LOD0-LOD3 plan, collision planning, animation clearance checks, Unreal import planning, folder naming, approval gates, and quality checklist are included.
- Package does not claim skeletal fit, authored animation, cloth simulation, physics setup, final visual approval, or implementation completion.
