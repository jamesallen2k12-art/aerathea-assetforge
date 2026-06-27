# SK_GIA_Base_A01 Modeling Handoff

## Purpose

Create the first Aerathea Giant base body DCC source, skeleton target, and Unreal import path. This handoff converts the approved Giant scale into a build-ready character target for body proportions, environment scale, weapon sockets, Blood Axe gear dependency, animation tests, and future named Giant NPCs.

## Source References

- Production package: `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md`
- Approved concept image: `docs/assets/characters/SK_GIA_Base_A01/SK_GIA_Base_A01_ApprovalConcept.png`
- First-pass DCC review render: `Saved/Automation/GiantBaseReview/SK_GIA_Base_A01_DCCReview.png`
- First-pass Unreal close-up capture: `Saved/Automation/StartupReview/AeratheaStartupReview_GiantBase_Closeup_v2.png`
- Intake slate: `docs/assets/intake/ACIQ-P02_01_GIANT_BLOODAXE_SLATE.md`
- Source concepts:
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Giant.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Giant1.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Giant2.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantMale1.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantMale2.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantMale3.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantMale4.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantFemale.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantFemale1.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantFemale3.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantFemale4.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantFemale5.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantFemaleShaman.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantMaleandFemale.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GiantMaleandFemale3.png`

Blood Axe source concepts are scale and sub-faction references only. Do not bake Blood Axe raider identity into the neutral base body.

## Production Target

Skeletal mesh base body for adult Aerathea Giants:

- Female Giants: 14-15 ft / 427-457 cm.
- Male Giants: 14'10"-16'0" / 452-488 cm.
- First production baselines: female 442 cm and male 470 cm.

The current first-pass DCC/Unreal import was produced from older scale assumptions. Treat it as review-only until rebuilt or rescaled against the A04 race-size chart.

The first DCC source should create a neutral Giant base body with starter highland clothing, not a final Blood Axe raider, boss, or named hero. Match the approved concept image for body mass, stance, hand scale, highland clothing, and neutral/civilized material language.

## Modeling Constraints

- Author in centimeters, 1 Unreal unit = 1 cm.
- Feet at world origin, facing +X unless import validation changes the convention.
- Avoid normal human scaling. Build larger hands, heavier joints, broader torso forms, thicker feet, and slower-looking mass into the proportions.
- Keep clothing modular where practical: fur mantle, belt, skirt/kilt panels, wraps, boots, bracers, and stone/iron ornaments.
- Preserve Giant hand scale for future weapons, bows, masonry tools, shields, ritual stones, and Blood Axe armory.
- Separate Blood Axe trophies, red banners, gore, and raider armor into later packages.
- Ensure topology supports heavy shoulder motion, large hand grips, broad stance, and readable facial expression.

## Blender Setup

- Collection: `SK_GIA_Base_A01`
- Mesh objects:
  - `Body_Head`
  - `Body_Torso`
  - `Body_Arms`
  - `Body_Hands`
  - `Body_Legs`
  - `Body_Feet`
  - `Starter_FurMantle`
  - `Starter_HighlandWraps`
  - `Starter_BeltAndPouches`
  - `Starter_HairBraids`
  - `Ornaments_StoneIron`
- Skeleton object: `SKEL_GIA_Base_A01`
- Apply transforms before export.
- Use clean mirrored topology for the base body. Limit asymmetry to optional hair, wraps, ornaments, and later faction variants.

## Modeling Sequence

1. Block female 442 cm and male 470 cm baselines beside 180 cm human, current A04 gnome markers, and current A04 Minotaur markers.
2. Establish primary Giant proportions: shoulders, torso, arm length, hand size, leg mass, foot size, head/brow read, and stance width.
3. Create neutral base forms for male and female variants, keeping Blood Axe identity separate.
4. Add starter highland clothing volumes: fur mantle, leather wraps, belt, pouches, bracers, boots/foot wraps, and simple stone/iron ornaments.
5. Sculpt or model large hair/braid clumps as production-friendly forms, not strand detail.
6. Add socket landmarks for giant weapons, shield, two-hand grips, talismans, and stomp VFX.
7. Retopologize for shoulders, elbows, wrists, fingers, hips, knees, ankles, neck, jaw, and heavy hand grip poses.
8. Create UVs and placeholder material assignments.
9. Build LOD0-LOD3 while preserving height, shoulders, hands, head, and stance.
10. Export skeletal FBX and validate against scale references and early Giant door/stair blockouts.

## Triangle Budget

- Base body LOD0: 35k-55k tris.
- Starter clothing, hair/fur, belts, and ornaments: 8k-18k tris.
- First dressed review mesh: under 70k tris.
- Hero/boss variants: 70k-90k tris only when justified.
- LOD1: 60-70 percent of LOD0.
- LOD2: 35-45 percent of LOD0.
- LOD3: 15-25 percent of LOD0.

Reduce small straps, hair subdivisions, fur cuts, ornament bevels, and inner clothing folds before reducing the primary Giant silhouette.

## Texture Deliverables

- `T_GIA_Base_A01_Body_BC`
- `T_GIA_Base_A01_Body_N`
- `T_GIA_Base_A01_Body_ORM`
- `T_GIA_Base_A01_Eyes_BC`
- `T_GIA_StarterOutfit_A01_BC`
- `T_GIA_StarterOutfit_A01_N`
- `T_GIA_StarterOutfit_A01_ORM`
- `T_GIA_Base_A01_Rune_E` only for shamanic or mystic variants

Material slot target:

- Body/head/skin
- Eyes
- Hair/fur
- Starter outfit/leather/iron/stone ornaments

## Collision Deliverables

- Movement capsule for female baseline: approximately 442 cm high, 95-115 cm radius.
- Movement capsule for male baseline: approximately 470 cm high, 100-125 cm radius.
- Maximum male variant review: up to 490 cm high.
- Physics bodies: pelvis, spine, chest, head, upper/lower arms, hands, simplified finger groups, thighs, calves, feet.
- Optional secondary physics only for large hair/fur pieces after performance review.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_A01.blend`
- Male FBX export: `SourceAssets/Exports/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_Male_A01.fbx`
- Female FBX export: `SourceAssets/Exports/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_Female_A01.fbx`
- Unreal skeletal meshes: `/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01`, `/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01`
- Skeletons: `/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01_Skeleton`, `/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01_Skeleton`
- Physics assets: `/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Male_A01`, `/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Female_A01`
- Animation Blueprint placeholders: `/Game/Aerathea/Characters/Giants/Base/ABP_GIA_Base_Male_A01`, `/Game/Aerathea/Characters/Giants/Base/ABP_GIA_Base_Female_A01`
- Startup review actors: `AET_PROD_GiantMaleBase_A01`, `AET_PROD_GiantFemaleBase_A01`

## Unreal Validation

- Current first-pass import is staged in `/Game/Aerathea/Characters/Giants/Base/` and passes `Tools/Unreal/validate_startup_scene.py`, but it uses older scale assumptions and must be rebuilt or rescaled before final Giant approval.
- Imports at centimeter scale with no correction.
- Final target baselines should read at roughly 442 cm for female Giants and 470 cm for male Giants.
- Feet sit on the ground plane and pivot at world origin.
- Skeleton supports idle, walk, run/jog, turn, step up/down, reach down, one-handed heavy attack, two-handed heavy attack, shield brace, bow draw placeholder, mason/tool loop, shaman channel, stomp, hit reaction, stagger, and death.
- Required sockets exist:
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
  - `vfx_rune_hand_l`
  - `vfx_rune_hand_r`
  - `vfx_stomp_ground`
- Review beside human, gnome, minotaur, Giant door, and Giant stair scale markers.

## Acceptance Checklist

- Female 14-15 ft and male 14'10"-16'0" scale is preserved.
- Base Giant silhouette is massive, highland, and mountain-forged, not a scaled human.
- Civilized/neutral Giant body is separate from Blood Axe raider identity.
- Large hands, feet, shoulders, head, and stance remain readable through LODs.
- Starter clothing supports fur, hide, leather, iron, stone, and shamanic variants without locking in one faction.
- Sockets support giant weapons, bows, shields, tools, talismans, and VFX.
- Collision, physics, material slots, texture maps, LODs, export paths, and Unreal import notes are defined.
