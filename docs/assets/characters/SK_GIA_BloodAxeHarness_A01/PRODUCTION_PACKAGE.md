# SK_GIA_BloodAxeHarness_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeHarness_A01`
- Asset type: Wearable Giant harness production package; planned skeletal gear asset only after later approval
- Parent source: `KIT_GIA_BloodAxeArmory_A01`
- Source concept region: `BloodAxeArmory.png#Armor_ChainRingHarness`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready
- Source-storage guardrail: the external source concept remains outside the repository. Do not copy, move, edit, embed, or commit it for this package.

`SK_GIA_BloodAxeHarness_A01` defines a brutal Giant-scale torso, back, and belt harness for hostile Blood Axe raiders who need to carry trophies, weapons, hooks, quiver straps, and camp gear without hiding the core Giant body mass. The design should read as a heavy utility harness first: broad scorched-leather bands, oversized iron rings, large chain links, back cross-straps, belt anchors, rough buckles, dull red Blood Axe cloth markers, and sparse trophy tie points.

This is not a neutral Giant harness and must not replace civilized Giant stoneworker, cave-town, or highland nomad language. Blood Axe visual language remains confined to the hostile raider sub-faction: soot-dark metal, rough leather, red warning marks, field-forged hardware, and restrained trophy accents with no graphic gore.

## Gameplay Purpose

The harness supports enemy-readability and future attachment planning for Blood Axe Giant raiders, hunters, camp guards, weapon carriers, and elite warband variants. Its gameplay read is "equipped hostile Giant with carry capacity," not a stat-bearing inventory system.

Expected use cases:

- Torso and back carry harness for Blood Axe raiders.
- Weapon carry support for future axe, hammer, hook spear, cleaver, bow, quiver, and banner variants.
- Trophy and warning-token attachment points used sparingly for silhouette and faction read.
- Camp or armory display variant if a later task needs the harness shown on a rack or mannequin.
- Shared material dependency for Blood Axe scorched leather, blackened iron, dark steel rings, red cloth, and bone or horn accent pieces.

Out of scope for this task: DCC geometry, Blender source, sculpt files, retopo, UVs, bakes, FBX export, Unreal import, skeletal fitting, cloth simulation, physics setup, socket authoring, animation implementation, combat rules, loot rules, inventory behavior, startup placement, source-concept copying, and final visual approval.

## Silhouette Notes

The primary silhouette must preserve the Giant body mass. The harness should frame the torso, shoulders, back, waist, and hips instead of wrapping the character in dense dangling clutter.

Core silhouette read:

- Wide diagonal chest straps that cross the sternum and rib mass as a few large readable bands.
- Broad waist or lower-torso belt that anchors the harness without hiding abdomen and hip scale.
- Heavy back cross or Y-strap structure for future back weapon, quiver, or trophy carry planning.
- Oversized iron rings at sternum, side ribs, belt line, and upper back as large geometry, not many small links.
- Short chain sections only where they define the silhouette or carry logic.
- A small number of large hook, buckle, and tie-point forms for readable attachment planning.
- Dull red cloth strips or paint marks as Blood Axe identifiers, kept secondary to the torso and back structure.
- Sparse bone, horn, tooth, or broken-token accents as dry trophy markers with no gore.

Avoid:

- Hiding the Giant chest, belly, shoulder breadth, spine, or waist behind trophy curtains.
- Normal-humanoid harness proportions scaled up without Giant strap thickness and ring weight.
- Dense dangling chains, tiny repeated rings, tiny rivet fields, charm clusters, or many small skulls.
- Graphic gore, wet blood, fresh remains, or readable text.
- Civilized Giant blue-gray stoneworker motifs, hearth identity, restrained blue runes, or neutral highland craft language.

## Scale Notes

Validated Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Use the validated `SK_GIA_Base_A01` body as the scale source for all future harness work.

This package does not change the Giant base scale and does not claim a completed wearable skeletal fit.

Torso, back, and belt planning targets:

- Chest strap width: broad Giant-scale bands, roughly 14-24 cm wide depending on position and variant.
- Main waist belt width: roughly 24-40 cm, with thickness readable from MMO camera distance.
- Back carry strap width: roughly 16-28 cm for major diagonal or vertical support bands.
- Major ring diameter: roughly 22-42 cm for sternum, side, belt, and back rings.
- Major buckle or hook size: roughly 18-38 cm, large enough to read as Giant utility hardware.
- Chain links: use only large readable links where needed, with small chain clutter moved to texture detail or removed.
- Trophy/tie points: keep to a few oversized anchors on side ribs, belt, or back; avoid full body coverage.

Future fit review must check:

- Neck, clavicle, and shoulder clearance.
- Chest breathing and idle deformation clearance if a later skeletal pass uses deformation.
- Spine twist and upper-body aim offset readability.
- Belt, abdomen, pelvis, and thigh clearance during walk, run, turn, crouch, and heavy attack poses.
- Back clearance for `back_large_weapon`, `back_shield`, future `back_quiver`, and future Blood Axe weapon carry.
- Side clearance for `belt_tool_l`, `belt_tool_r`, future `belt_trophy`, and future sidearm carry.
- Compatibility with `SK_GIA_BloodAxeRaiderChest_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, quiver packages, and major Blood Axe weapons must be approval-gated.

## Materials and Color Palette

Primary material language:

- Scorched dark leather, rough hide, thick cord, and worn strap edges.
- Blackened iron and dark steel for rings, buckles, hooks, chain links, and strap plates.
- Reforged stolen metal using or matching `MI_GIA_BloodAxeReforgedMetal_A01` where appropriate.
- Dull oxide red cloth, red paint slashes, or dirty red wraps as restrained Blood Axe identifiers.
- Bone, horn, tooth, or broken-token trophy accents used sparingly.
- Soot, ash, grime, mud, rubbed edge wear, and broad hand-painted strap compression.

Suggested color ranges:

- Blackened metal: `#151719` to `#2A2C2E`
- Worn iron edges: `#555A5C` to `#777A76`
- Scorched leather: `#241611` to `#4A2E20`
- Dark hide: `#1D1511` to `#3B2A1E`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Old bone/horn: `#A69578` to `#D0B98C`
- Soot and grime: `#0B0A09` to `#403025`

No default emissive is approved. Forge heat, shamanic glow, ritual paint glow, animated materials, or VFX hooks require a separate approval-gated variant.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SK_GIA_BloodAxeHarness_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant torso, back, and belt carry harness, preserved Giant body mass, broad scorched-leather straps, oversized blackened-iron rings, large buckles, short heavy chain sections, back cross-straps, side and belt attachment anchors, dull red Blood Axe cloth and paint accents, sparse dry bone or horn trophy markers, soot-dark field-forged utility, and a gameplay role as trophy and weapon carry gear for Blood Axe raiders. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a wearable gear production sheet with front, side, back, three-quarter views, strap/ring layout callouts, back and belt attachment callouts, material swatches, and scale callouts against female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines on a clean background. Avoid copying any existing franchise, avoid making Blood Axe gear the default Giant culture, avoid graphic gore, avoid dense dangling clutter, avoid tiny rivet or chain noise, and avoid overclaiming final skeletal fit or implementation readiness.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, export, skeletal fit, physics asset, cloth setup, socket, or Unreal asset is created or approved by this package.

Future modeling should prioritize the main carry architecture:

- Build the front chest harness from two or three broad strap forms with clear intersections and compression points.
- Build the rear harness from a large cross, Y, or ladder-like strap structure that leaves the spine and shoulder mass readable.
- Build the waist belt as a heavy anchor band with a few large plates, loops, and side attachment points.
- Model major rings, buckles, hooks, and large chain links as real geometry where they define the silhouette or attachment logic.
- Place side-rib and hip anchors so future tools, sidearms, or trophy ties can hang without covering the thigh or waist motion read.
- Keep back-mounted carry plates and rings clear enough for future weapon, bow, quiver, or shield review.
- Use a few large hard-surface strap plates to break up leather spans without turning the harness into dense armor.
- Add sparse trophy anchors as dry bone, horn, tooth, or broken-token shapes; do not add graphic remains.

Texture or normal-map:

- Tiny rivets.
- Fine scratches.
- Leather pores.
- Stitching.
- Small cord fibers.
- Minor soot speckles.
- Small red paint chips.
- Tiny chain scuffs.
- Hairline cracks in bone or horn.
- Small hammer marks on metal.

Future wearable-fit gates:

- Harness must fit over the Giant torso without shrinking chest, belly, waist, shoulders, or back proportions.
- Harness must not claim compatibility with the Giant skeleton until a later implementation task validates deformation and clearance.
- Display-only and worn variants should be split if pivot, clearance, or visual needs diverge.
- Long cloth strips, swinging chains, and dangling trophies should be avoided in the first pass unless a separate cloth or physics task approves them.
- Any overlap with chest armor, trophy belt, greaves, quivers, or weapons must be resolved through a later attachment review.

## Texture and Material Notes

Texture set targets for a future approved build:

- `T_GIA_BloodAxeHarness_A01_BC`
- `T_GIA_BloodAxeHarness_A01_N`
- `T_GIA_BloodAxeHarness_A01_ORM`
- Optional future approval-gated `T_GIA_BloodAxeHarness_A01_E`

Material slot target:

- Slot 0: `MI_GIA_BloodAxeScorchedLeather_A01` or future equivalent for straps, hide pads, cord, and red cloth if combined.
- Slot 1: `MI_GIA_BloodAxeReforgedMetal_A01` or future equivalent for blackened iron, dark steel rings, buckles, hooks, links, and plates.
- Slot 2: `MI_GIA_BloodAxeBoneTrophy_A01` or future equivalent for sparse bone, horn, tooth, and broken-token accents.
- Optional red cloth may remain inside the leather material unless final art approval requires a separate shared `MI_GIA_BloodAxeRedCloth_A01`.

Packed `ORM` plan:

- R: Ambient occlusion around strap crossings, ring seats, belt overlap, back harness compression, hook mounts, and trophy anchors.
- G: High roughness for scorched leather, hide, soot, and matte bone; slightly lower roughness on rubbed metal edges and hand-worn rings.
- B: Metallic only for rings, buckles, hooks, chain links, strap plates, and dark steel hardware.

Texture readability requirements:

- Use broad strap compression, rubbed edges, and soot gradients to show how the harness sits over the Giant body.
- Keep red accents large and sparse enough to identify Blood Axe allegiance without creating a one-color read.
- Use large metal wear patterns and hand-painted AO at Giant scale.
- Avoid tiny repeated decals, readable text, dense tally marks, and franchise-like symbols.
- Keep gore out of the texture language; trophies are dry, old, and symbolic.

## Triangle Budget

Target budget for a future approved wearable mesh:

- LOD0: 6k-11k tris for the full torso, back, and belt harness.
- LOD0 elite variant ceiling: 13k tris only if additional large rings, carry plates, or back attachment structures are approved.
- Material slots: target 2-3 slots.
- Texture resolution: 2K standard for enemy gear; 4K only for an approved named boss or close-up hero variant.

Budget distribution guidance:

- Major straps and belt forms: 35-45 percent.
- Rings, buckles, hooks, and large chain links: 25-30 percent.
- Back carry structure and side anchors: 15-20 percent.
- Sparse trophy accents and red cloth markers: 8-12 percent.
- Secondary bevels and support plates: 5-10 percent.

Do not spend geometry on tiny rivets, repeated small chain links, fine stitches, minor cracks, small chips, or dense trophy fragments.

## LOD Plan

All important future wearable meshes need LOD0-LOD3.

- LOD0: full broad chest straps, back cross-straps, waist belt, major rings, large buckles, main hooks, short readable chain sections, side anchors, sparse trophy ties, broad bevels, and large Blood Axe color breaks.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small buckle edges, secondary strap loops, small ring cuts, and underside strap thickness.
- LOD2: 35-45 percent of LOD0; simplify back-side strap layering, merge minor anchor plates, flatten small trophy shapes, and reduce chain link count.
- LOD3: 15-25 percent of LOD0; preserve the diagonal chest read, back carry read, waist belt mass, a few major rings, and red/black Blood Axe color blocks.

LOD reduction order:

1. Tiny rivets, stitches, scratches, and leather pores.
2. Small strap loops and minor buckle bevels.
3. Secondary ring cuts and small chain segments.
4. Small trophy fragments and cloth tears.
5. Back-side secondary strap layering.
6. Non-silhouette support plates.
7. Secondary bevels on interior-facing hardware.

Never reduce the Giant torso framing, shoulder/back clearance, waist belt mass, major ring read, or broad Blood Axe red/black identity before removing small detail.

## Collision Notes

No collision is authored or approved in this docs-only package.

Future collision planning:

- Worn harness should normally rely on the owning Giant character movement capsule and physics asset, not separate per-strap collision.
- Equipped carry items should use their own later-approved attachment, trace, or display collision rules.
- Preview or display variants, if approved later, should use simple box or low-count convex bounds around the rack/mannequin or harness display form.
- Avoid per-ring, per-link, per-hook, per-trophy, or cloth-strip collision.
- Back and belt attachment clearance must be reviewed only after actual meshes, sockets, and carry items exist.
- Do not add combat hit zones, weak points, armor bonuses, inventory capacity, or damage behavior from this package.

## Animation Notes

No animation, skeletal fitting, deformation setup, cloth simulation, secondary motion, or physics setup is authored or approved here.

Future approval-gated motion checks should include:

- Idle breathing, heavy breathing, and torso expansion.
- Spine twist and upper-body aim offsets.
- One-handed and two-handed attack windups.
- Bow draw, quiver reach, and back carry reach for archer variants.
- Turn-in-place, walk, run, stagger, and hit reaction clearance.
- Pelvis and thigh clearance for belt anchors during locomotion.
- Back carry clearance for large weapons, shields, banners, bows, and quivers.

Rigid straps, rings, and hooks should be preferred for the first wearable pass. Any swinging chains, loose trophies, cloth strips, or secondary motion require separate approval and validation.

## Unreal Import Notes

This section is planning only. No Unreal Content, skeletal mesh asset, static display asset, material instance, texture, socket, physics asset, Blueprint, validator, or startup actor is created by this package.

Planned Unreal folder after later approval:

- `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`

Planned asset naming:

- Wearable mesh: `SK_GIA_BloodAxeHarness_A01`
- Optional display mesh, if later approved: `SM_GIA_BloodAxeHarness_Display_A01`
- Planned material instances:
  - `MI_GIA_BloodAxeScorchedLeather_A01`
  - `MI_GIA_BloodAxeReforgedMetal_A01`
  - `MI_GIA_BloodAxeBoneTrophy_A01`
  - Optional `MI_GIA_BloodAxeRedCloth_A01`

Planned texture names:

- `T_GIA_BloodAxeHarness_A01_BC`
- `T_GIA_BloodAxeHarness_A01_N`
- `T_GIA_BloodAxeHarness_A01_ORM`
- Optional future `T_GIA_BloodAxeHarness_A01_E`

Import planning constraints for a later task:

- Scale: centimeter-authored, import scale 1.0 only after DCC/export rules are approved.
- Pivot: align to the approved Giant base body origin for a wearable skeletal module, or to a display support origin only for a separately approved static display mesh.
- Material slot count: 2-3 slots target.
- LODs: LOD0-LOD3 required before production import approval.
- Collision: no separate collision unless a later display or gameplay task explicitly approves it.
- Performance: reuse shared Blood Axe material families, avoid unique slots per ring or trophy, and keep chain/ring counts low.

Socket and attachment planning is future approval-gated. Candidate documentation references only:

- Existing Giant base references: `back_large_weapon`, `back_shield`, `belt_tool_l`, `belt_tool_r`, `chest_talisman`.
- Future Blood Axe references that may be requested later: `back_quiver`, `belt_trophy_l`, `belt_trophy_r`, `side_hook_l`, `side_hook_r`, `harness_back_anchor`, `harness_chest_anchor`, `harness_belt_anchor`.
- No new sockets are authorized by this package.
- Any final socket names, transforms, attachment rules, weapon carry rules, or trophy placement must be owned by a later Unreal/animation task and validated against the approved Giant baselines.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/characters/SK_GIA_BloodAxeHarness_A01/`
- Production package: `docs/assets/characters/SK_GIA_BloodAxeHarness_A01/PRODUCTION_PACKAGE.md`
- Related kit package: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- Related child intake: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/CHILD_ASSET_INTAKE.md`
- Related base body package: `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md`
- Related chest package: `docs/assets/characters/SK_GIA_BloodAxeRaiderChest_A01/PRODUCTION_PACKAGE.md`
- Related material package: `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/PRODUCTION_PACKAGE.md`
- Planned Unreal folder after approval only: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, FBX exports, Unreal Content assets, runtime source, startup-scene actors, validators, copied concept files, or global index entries from this task.

## Approval Gates

- DCC approval is required before creating meshes, Blender sources, sculpt files, retopo files, UVs, bakes, or exports.
- Unreal approval is required before importing skeletal gear, static display meshes, material instances, textures, LODs, physics assets, validators, sockets, or startup-scene actors.
- Wearable-fit approval is required before claiming the harness fits either Giant baseline, clears torso/shoulder/back movement, supports carry attachments, or deforms correctly.
- Attachment approval is required before adding final socket names, socket transforms, weapon carry offsets, trophy offsets, quiver support, or banner support.
- Cloth and physics approval is required before adding swinging chains, dangling trophies, loose cloth strips, secondary motion, or any physics setup.
- Visual approval is required before locking final strap layout, ring count, trophy density, red cloth placement, elite variant language, or overlap with other Blood Axe armor modules.
- Culture approval is required if Blood Axe red-black raider gear starts replacing neutral/civilized Giant stoneworker or highland nomad language.
- Source-storage approval is required before copying, embedding, or committing any external source concept.
- Gameplay approval is required before armor stats, inventory capacity, combat hit zones, weak points, loot rules, or encounter behavior are defined.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, or global index file.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Harness supports future trophy and weapon carry planning without claiming final attachments or implementation.
- Harness preserves Giant body mass, chest width, shoulder breadth, spine/back readability, waist scale, and hip movement read.
- Strap, ring, back, torso, belt, and side-anchor planning is documented.
- Primary forms are broad straps, waist belt, back carry structure, oversized rings, large buckles, and sparse trophies, not micro-detail.
- Materials use scorched leather, hide, blackened iron, dark steel, reforged metal, oxide red cloth/paint, soot, ash, and sparse dry bone or horn accents consistently.
- `MI_GIA_BloodAxeReforgedMetal_A01` is referenced as the core metal dependency.
- Default emissive, forge heat, shamanic glow, animated material states, cloth, physics, and final socket transforms are not claimed.
- Texture maps include BC, N, ORM, and optional future E only behind approval.
- Triangle budget, LOD0-LOD3 plan, collision planning, animation clearance checks, Unreal import planning, folder naming, approval gates, and quality checklist are included.
- Package does not claim skeletal fit, authored animation, cloth simulation, physics setup, final visual approval, socket implementation, or Unreal implementation completion.
