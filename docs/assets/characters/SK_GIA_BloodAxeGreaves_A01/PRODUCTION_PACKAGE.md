# SK_GIA_BloodAxeGreaves_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeGreaves_A01`
- Asset type: Wearable Giant lower-leg armor module production package; planned skeletal gear asset only after later approval
- Source kit: `KIT_GIA_BloodAxeArmory_A01`
- Source child reference: `BloodAxeArmory.png#Armor_RaiderGreavesSabatons`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready
- Source-storage guardrail: the external source concept remains outside the repository. Do not copy, move, edit, embed, or commit it for this package.

`SK_GIA_BloodAxeGreaves_A01` defines hostile Blood Axe lower-leg armor for Giant raiders: huge calf plates, brutal knee guards, broad ankle collars, and heavy sabaton-like boot armor strapped over massive Giant legs and feet. The design should read as stolen blackened metal reforged into raider protection, with soot-dark iron, scorched leather, deep red war marks, and sparse bone trophy anchors.

The armor must preserve Giant leg mass. These greaves are not narrow humanoid boots scaled upward; they need wide calves, thick ankles, long heavy feet, and enough negative space around joints for future clearance review. Blood Axe visual language belongs to a hostile Giant raider sub-faction and must remain separate from neutral/civilized Giant stoneworker, cave-town, hearth, and highland nomad culture.

## Gameplay Purpose

This package prepares lower-leg armor for Blood Axe Giant raider enemies, elite camp guards, heavy archers, and future chieftain-adjacent armor sets. The greaves help identify Blood Axe troops at MMO camera distance by giving the lower body a blackened-metal, red-marked, heavy-footed raider read while preserving the approved Giant leg silhouette.

Expected use cases:

- Standard Blood Axe raider greaves and sabatons.
- Heavier elite variant with larger knee plates and reinforced boot caps.
- Equipment-preview or armory-display variant after a later implementation task.
- Shared material use with Blood Axe reforged metal, scorched leather, red cloth/paint, soot, grime, and sparse bone trophy accents.

Out of scope for this task: DCC geometry, FBX export, Unreal import, skeletal fitting, final wearable validation, gait changes, IK setup, physics setup, cloth simulation, animation authoring, gameplay stats, hit-zone rules, loot behavior, startup placement, and final visual approval.

## Silhouette Notes

The silhouette starts from the Giant leg mass, not from armor ornament:

- Calf armor must be broad, heavy, and slightly asymmetrical while leaving the underlying Giant calf volume readable.
- Knee guards should be oversized and hostile, with blunt jagged plates or a few large teeth-like points that read from distance.
- Ankle collars should look durable and wide enough for Giant ankles, not cinched like normal humanoid boots.
- Sabatons should have a long, heavy foot shape with a broad toe box and thick sole mass.
- Strap bands should be wide and few, wrapping around calf, lower shin, ankle, and boot bridge as readable support forms.
- Red Blood Axe marks should break up the dark metal in broad strokes, not small decals.
- Bone trophies, nails, rings, or hooks should remain sparse and large enough to read without becoming clutter.

Avoid:

- Thin calves, narrow ankles, pointed fashion boots, or normal humanoid leg proportions.
- Dense spikes around the knee or ankle that would confuse the leg outline.
- Tiny modeled rivet fields, dense chain curtains, stitch webs, or repeated dangling trinkets.
- Graphic gore, wet blood treatment, or readable real-world symbols.
- Civilized Giant blue-gray stoneworker motifs, warm hearth identity, restrained blue runes, or neutral highland dress language.

## Scale Notes

Giant scale lock: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

Use the validated `SK_GIA_Base_A01` body as the only scale source for future work. Author in centimeters; 1 Unreal unit = 1 cm. This package does not change the base Giant scale and does not claim completed wearable skeletal fit.

Lower-leg planning targets:

- Female baseline review target: 442 cm tall body with full calf, ankle, and foot mass preserved.
- Male baseline review target: 470 cm tall body with larger calf circumference, ankle width, heel width, and foot length preserved.
- Greave height target: upper shin to above ankle, with the knee guard treated as a separate major plate mass.
- Knee clearance target: knee plate should frame the joint without sealing the front, back, or sides so tightly that future bend review is impossible.
- Calf clearance target: armor shell must allow the full Giant calf volume and avoid squeezing the leg into a narrow column.
- Ankle clearance target: ankle collar must leave visible articulation space and not merge into a rigid stovepipe silhouette.
- Boot/sabaton clearance target: toe box and heel must stay broad enough for Giant feet and must not shorten the foot into a normal humanoid boot.
- Sole/ground planning target: thick sole and heel mass are visual only until a later approved implementation validates contact height.

Approval-sensitive fit areas:

- Knee front, back, and side clearance.
- Calf bulge and shin plate offset.
- Ankle collar and boot bridge clearance.
- Heel, toe, sole, and ground-contact visual height.
- Hip/thigh/tasset overlap with future `SK_GIA_BloodAxeTrophyBelt_A01`.
- Lower-leg overlap with future boot, foot, or ground-dust effects if those are ever approved.

These are planning constraints only. This package makes no gait, IK, physics, cloth, or final wearable skeletal fit claim.

## Materials and Color Palette

Primary material language:

- Blackened iron and dark steel using `MI_GIA_BloodAxeReforgedMetal_A01`.
- Reforged stolen shin plates with broad hammer marks, cut seams, and uneven welded edges.
- Scorched dark leather and hide straps around calf, ankle, heel, and boot bridge.
- Deep oxide red cloth strips or rough war paint used as restrained Blood Axe identifiers.
- Old bone, horn, tooth, or trophy lacing used sparingly on one knee or boot side.
- Soot, ash, dull grime, and worn steel edge exposure.
- Optional rough fur padding only as raider insulation, not civilized highland dress.

Suggested color ranges:

- Blackened metal: `#151719` to `#2A2C2E`
- Worn steel edges: `#555A5C` to `#787B78`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Scorched leather: `#241611` to `#4A2E20`
- Old bone: `#A69578` to `#D0B98C`
- Soot and grime: `#0B0A09` to `#403025`

No default emissive is approved. Forge heat, shamanic glow, ritual marks, animated material states, or glowing step effects require a separate approval-gated variant and must not be assumed here.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SK_GIA_BloodAxeGreaves_A01` for the world of Aerathea. The design should emphasize hostile Blood Axe Giant raider lower-leg armor, preserved massive Giant calf and foot proportions, wide shin plates, oversized blunt knee guards, broad ankle collars, heavy sabaton-like boot armor, blackened reforged iron, dark steel, scorched leather straps, restrained deep red war paint and cloth, sparse large bone trophy accents, soot, ash, field-forged brutality, and a gameplay role as readable enemy raider gear. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a wearable lower-leg armor production sheet with front, side, back, three-quarter, sole/boot, knee clearance, ankle clearance, and calf mass callouts over female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines on a clean background. Avoid copying any existing franchise, avoid making Blood Axe gear the default Giant culture, avoid narrow humanoid boot proportions, avoid graphic gore, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, export, skeletal fit, or Unreal asset is created or approved by this package.

Future modeling should prioritize:

- Large shin plate shells as broad readable metal masses with thick bevels and uneven reforged edges.
- Oversized knee guards as separate major forms with simple underlap, not dense articulated machinery.
- Wide calf side plates that preserve the Giant leg volume instead of compressing it.
- Broad ankle collars with clear separation from shin plates and boot armor.
- Heavy boot/sabaton forms with thick toe boxes, wide heel mass, and chunky sole silhouette.
- Few large leather straps across calf, ankle, and boot bridge.
- Large buckles, rings, and strap anchors only where they support the silhouette.
- Sparse trophy details placed away from knee and ankle clearance zones.

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
- Repeated micro-nicks on toe plates.

Lower-leg clearance modeling gates for a later approved implementation:

- Fit over the Giant lower leg without narrowing calf, ankle, heel, toe, or sole proportions.
- Keep knee plate depth simple enough to support future static bend-clearance review.
- Keep ankle collar offset visible and avoid sealing the lower leg into a rigid tube.
- Preserve boot footprint and toe-box width so the Giant does not read as a tall normal humanoid.
- Separate display-only and worn variants if future review shows incompatible pivot, stance, or silhouette needs.

## Texture and Material Notes

Texture set targets for a future approved build:

- `T_GIA_BloodAxeGreaves_A01_BC`
- `T_GIA_BloodAxeGreaves_A01_N`
- `T_GIA_BloodAxeGreaves_A01_ORM`
- Optional future approval-gated `T_GIA_BloodAxeGreaves_A01_E`

Material slot target:

- Slot 0: `MI_GIA_BloodAxeReforgedMetal_A01` for blackened iron, dark steel, edge wear, hammered plates, chipped red paint masks, knee guards, shin plates, ankle collars, and sabaton caps.
- Slot 1: `MI_GIA_BloodAxeScorchedLeather_A01` or future equivalent for straps, hide padding, boot bindings, and dark wrap material.
- Slot 2: `MI_GIA_BloodAxeBoneTrophy_A01` or future equivalent for sparse trophy accents.
- Optional red cloth/paint may remain masked inside the metal or leather material unless later visual approval requires a separate slot.

Packed `ORM` plan:

- R: Ambient occlusion around plate overlaps, knee undercuts, calf straps, ankle collars, boot bridge, sole grooves, and trophy anchors.
- G: Roughness biased high for soot-dark metal and leather; slightly lower on rubbed toe edges, heel edges, and knee guard contact points.
- B: Metallic only for metal plates, buckles, rings, toe caps, and edge-worn steel.

Texture readability requirements:

- Use broad red marks, toe scuffs, knee wear, and shin-edge highlights to clarify the lower-leg silhouette.
- Keep dark soot from flattening the boot and greave into one black column.
- Paint hammering and reforged seams at Giant scale.
- Keep bone accents warm and matte so they do not overpower the calf, knee, or boot mass.
- Avoid readable text, franchise-like symbols, repeated tiny decals, or dense ornamental noise.

## Triangle Budget

Target budget for a future approved mesh:

- LOD0: 6k-12k tris for the paired greaves, knee guards, ankle collars, straps, and boot/sabaton armor.
- LOD0 hero/elite variant ceiling: 14k tris only if larger knee plates, boot caps, or display-specific underside forms are approved.
- Material slots: target 2-3 slots.
- Texture resolution: 2K standard for enemy armor; 4K only for an approved named hero or boss close-up variant.

Budget distribution guidance:

- Shin and calf plates: 30-35 percent.
- Knee guards: 18-22 percent.
- Ankle collars and boot/sabaton armor: 25-30 percent.
- Straps, buckles, and anchors: 12-15 percent.
- Trophy accents, fur/hide pads, and secondary cuts: 5-10 percent.

Do not spend geometry on tiny rivets, dense chain links, fine stitches, small chips, leather pores, or repeated trophy fragments.

## LOD Plan

All important future wearable meshes need LOD0-LOD3.

- LOD0: full primary greave shells, large knee guards, broad ankle collars, heavy boot/sabaton forms, major straps, sparse trophy anchors, broad bevels, and large Blood Axe shape breaks.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small buckle edges, secondary strap loops, small trophy cuts, underside boot grooves, and interior ankle detail.
- LOD2: 35-45 percent of LOD0; simplify calf side layering, merge minor boot plates, flatten small trophy forms, reduce knee undercuts, and reduce non-silhouette sole cuts.
- LOD3: 15-25 percent of LOD0; preserve calf width, knee-guard mass, ankle collar width, boot footprint, red/black Blood Axe color blocks, and one or two major silhouette breaks.

LOD reduction order:

1. Tiny rivets, stitches, surface chips, and toe nicks.
2. Minor strap loops and small buckles.
3. Secondary trophy cuts and small bone fragments.
4. Underside sole grooves and non-visible boot interior.
5. Back-side calf plate layering.
6. Small fur, hide, or cloth cuts.
7. Secondary bevels on non-silhouette plates.

Never reduce the Giant calf width, ankle mass, knee-guard read, boot footprint, or major Blood Axe red/black read before removing small detail.

## Collision Notes

No collision is authored or approved in this docs-only package.

Future collision planning:

- Worn greaves should normally rely on the owning Giant character movement and hit setup decided in a later implementation task.
- Do not add separate combat hit zones, weak points, armor bonuses, step damage, footstep triggers, or damage behavior from this package.
- Preview or display variants, if approved later, should use simple boxes or low-count convex bounds around each greave/boot display form.
- Avoid per-strap, per-chain, per-trophy, toe-segment, sole-groove, or cloth-strip collision.
- Knee, ankle, boot, sole, and calf bounds must be reviewed only after an actual wearable implementation task exists.

This package does not authorize gait edits, IK setup, physics bodies, cloth simulation, or final fit collision.

## Animation Notes

No animation, gait changes, IK, skeletal fitting, cloth simulation, secondary motion, or physics setup is authored or approved here.

Future approval-gated clearance checks may include static pose and authored-animation review poses for:

- Knee bend clearance around the knee guard.
- Ankle flex clearance around the ankle collar and boot bridge.
- Calf and shin plate separation under broad lower-leg forms.
- Toe-box, heel, and sole visual clearance against the Giant base foot.
- Overlap review with future belt, tasset, foot armor, or ground-contact visual effects.

Rigid straps and trophies should be preferred for the first wearable planning pass. Any dangling trophies, moving straps, chain swing, cloth strips, secondary motion, or physicalized boot behavior require a separate approval and validation pass.

## Unreal Import Notes

This section is planning only. No Unreal Content, skeletal mesh asset, material instance, Blueprint, physics asset, validator, or startup actor is created by this package.

Planned Unreal folder after later approval:

- `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`

Planned asset naming:

- Wearable mesh: `SK_GIA_BloodAxeGreaves_A01`
- Optional display mesh, if later approved: `SM_GIA_BloodAxeGreaves_Display_A01`
- Planned material instances:
  - `MI_GIA_BloodAxeReforgedMetal_A01`
  - `MI_GIA_BloodAxeScorchedLeather_A01`
  - `MI_GIA_BloodAxeBoneTrophy_A01`

Planned texture names:

- `T_GIA_BloodAxeGreaves_A01_BC`
- `T_GIA_BloodAxeGreaves_A01_N`
- `T_GIA_BloodAxeGreaves_A01_ORM`
- Optional future `T_GIA_BloodAxeGreaves_A01_E`

Import planning constraints for a later task:

- Scale: centimeter-authored, import scale 1.0 only after DCC/export rules are approved.
- Pivot: align to the approved Giant base body origin or future gear attachment convention after implementation ownership is assigned.
- Material slot count: 2-3 slots target.
- Sockets: no new sockets are authorized here. Future fit work must validate against the Giant base lower-leg, knee, ankle, foot, boot, and potential gear attachment assumptions.
- LODs: LOD0-LOD3 required before production import approval.
- Collision: no separate collision unless a later display or gameplay task explicitly approves it.
- Performance: keep the asset within enemy NPC armor budgets and avoid extra material slots for small trophies or red paint.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/characters/SK_GIA_BloodAxeGreaves_A01/`
- Production package: `docs/assets/characters/SK_GIA_BloodAxeGreaves_A01/PRODUCTION_PACKAGE.md`
- Related kit package: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- Related child intake: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/CHILD_ASSET_INTAKE.md`
- Related base body package: `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md`
- Related material package: `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/PRODUCTION_PACKAGE.md`
- Planned Unreal folder after approval only: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`

Do not add SourceAssets folders, Blender files, FBX exports, Unreal Content assets, runtime source, startup-scene actors, validators, copied concept files, or global index entries from this task.

## Approval Gates

- DCC approval is required before creating meshes, Blender sources, sculpt files, retopo files, UVs, bakes, or exports.
- Unreal approval is required before importing skeletal gear, display meshes, material instances, textures, LODs, physics assets, validators, or startup-scene actors.
- Wearable-fit approval is required before claiming the greaves fit either Giant baseline, clear knees, clear ankles, preserve boot contact, or deform correctly.
- Animation approval is required before any gait, step, knee, ankle, foot, or authored motion claim is made.
- IK approval is required before any foot placement, slope handling, ground alignment, or procedural adjustment claim is made.
- Cloth and physics approval is required before adding moving straps, swinging chains, dangling trophies, secondary motion, simulated cloth, physical assets, or boot-impact behavior.
- Visual approval is required before locking final knee-guard size, sabaton footprint, trophy density, red cloth placement, or elite/chieftain variant language.
- Culture approval is required if Blood Axe red-black raider armor starts replacing neutral/civilized Giant stoneworker, cave-town, or highland nomad language.
- Source-storage approval is required before copying, embedding, or committing any external source concept.
- Gameplay approval is required before armor stats, hit zones, weak points, footstep effects, loot rules, or encounter behavior are defined.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, or global index file.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Greaves preserve Giant calf width, ankle mass, foot length, heel width, toe-box breadth, and lower-leg silhouette.
- Leg, boot, knee, and ankle clearance planning is included without claiming final wearable skeletal fit.
- Primary forms are broad shin plates, knee guards, ankle collars, boot/sabaton armor, major straps, and sparse trophies, not micro-detail.
- Materials use blackened iron, dark steel, scorched leather, oxide red cloth/paint, soot, ash, and sparse bone trophies consistently.
- `MI_GIA_BloodAxeReforgedMetal_A01` is referenced as the core metal dependency.
- Default emissive, forge heat, shamanic glow, animated material states, gait edits, IK, cloth, physics, and final fit are not claimed.
- Texture maps include BC, N, ORM, and optional future E only behind approval.
- Triangle budget, LOD0-LOD3 plan, collision planning, animation clearance checks, Unreal import planning, folder naming, approval gates, and quality checklist are included.
- Package does not claim skeletal fit, authored animation, gait behavior, IK behavior, cloth simulation, physics setup, final visual approval, or implementation completion.
