# SK_OGR_Base_A01 Modeling Handoff

## Purpose

Create the first Aerathea Ogre base body DCC source, skeleton target, and Unreal import path. This handoff converts the approved Ogre scale chart and source approval board into a build-ready character target for scale validation, body proportions, class outfit fit, Teknomancy sockets, collision tests, and future Warrior, Teknomancer, Shaman, and Necromancer variants.

## Source References

- Production package: `docs/assets/characters/SK_OGR_Base_A01/PRODUCTION_PACKAGE.md`
- Source concept intake: `docs/assets/characters/SK_OGR_Base_A01/SOURCE_CONCEPT_INTAKE.md`
- Approved approval board: `docs/assets/characters/SK_OGR_Base_A01/OGRE_APPROVAL_BOARD_A01.png`
- Approved scale chart: `docs/assets/reference/AET_Race_Size_Comparison_A05_OgreReview.png`
- Primary body sources:
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Ogre Female.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreFemale2.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreMale1.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreMale2.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Ogremale4.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreMaleTek.png`
- Encounter scale references:
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreTekvsGnomeMek.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GnomevsOgre1.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GnomevsOgre10.png`

## Production Target

Skeletal mesh base body for adult Aerathea Ogres:

- Female Ogres: 10'0"-10'6" / 305-320 cm.
- Male Ogres: 10'4"-11'0" / 315-335 cm.
- First production baselines: female 315 cm and male 330 cm.

The first DCC source should create neutral male and female Ogre base bodies with simple starter wraps, belts, boots, bracers, and readable broad anatomy. It is not a final Teknomancer, Warrior, Shaman, Necromancer, or named hero. Keep the body clean enough for later class outfits and gear sockets.

## Modeling Constraints

- Author in centimeters, 1 Unreal unit = 1 cm.
- Feet at world origin, facing +X unless import validation changes the convention.
- Ogres must read larger than Minotaurs and Anubisath/Sutekh, but clearly smaller than Giants.
- Avoid scaled-human proportions. Build the silhouette around huge shoulders, barrel chest, thick neck, large jaw, heavy forearms, slab hands, dense legs, and broad feet.
- Keep posture powerful and forward-driving, not hunched caricature.
- Keep base clothing simple and modular: loincloth/skirt panels, belts, bracers, boots/wraps, shoulder straps, and optional small metal plates.
- Leave Teknomancy tanks, cannons, coils, backpacks, shamanic charms, and necromantic trophies for later class packages except for socket landmarks.
- Ensure topology supports heavy shoulder motion, large hand grips, braced cannon poses, stomp, shoulder bash, and two-handed heavy weapon swings.

## Blender Setup

- Collection: `SK_OGR_Base_A01`
- Mesh objects:
  - `Male_Body`
  - `Male_Head`
  - `Male_Hands`
  - `Male_Feet`
  - `Male_Starter_Wraps`
  - `Male_Starter_Belts`
  - `Female_Body`
  - `Female_Head`
  - `Female_Hands`
  - `Female_Feet`
  - `Female_Starter_Wraps`
  - `Female_Starter_Belts`
  - `Scale_Markers`
- Skeleton object: `SKEL_OGR_Base_A01`
- Apply transforms before export.
- Use mirrored production topology for the base body. Limit asymmetry to starter wraps and later class outfit variants.

## Modeling Sequence

1. Block female 315 cm and male 330 cm baselines beside Minotaur, Anubisath/Sutekh, and Giant markers from the A05 scale chart.
2. Establish primary Ogre proportions: shoulder width, barrel chest, long heavy arms, hand scale, neck/head mass, leg density, foot size, and stance width.
3. Create neutral male and female body forms without class-specific gear.
4. Add simple starter wraps, belts, bracers, and boots that can be replaced by class outfits.
5. Add socket landmarks for weapons, offhand, back weapon, Teknomancy pack, shoulder gear, belt gear, mouth/eye/chest VFX, and ground stomp VFX.
6. Retopologize for shoulders, elbows, wrists, fingers, hips, knees, ankles, neck, jaw, and large grip poses.
7. Create UVs and placeholder material assignments.
8. Build LOD0-LOD3 while preserving height, shoulder width, hands, head, feet, and stance.
9. Export male and female skeletal FBX files.
10. Validate in Unreal beside Minotaur, Anubisath/Sutekh, and Giant scale references.

## Triangle Budget

- Base body LOD0: 35k-55k tris per sex-specific body.
- Starter clothing/wraps/belts/boots: 6k-14k tris.
- First dressed review mesh: under 65k tris per body.
- LOD1: 55-60 percent of LOD0.
- LOD2: 25-35 percent of LOD0.
- LOD3: 10-15 percent of LOD0.

Reduce small straps, minor belt cuts, small metal plates, folds, scars, and secondary clothing detail before reducing the primary Ogre silhouette.

## Texture Deliverables

- `T_OGR_Base_A01_Body_BC`
- `T_OGR_Base_A01_Body_N`
- `T_OGR_Base_A01_Body_ORM`
- `T_OGR_Base_A01_Eyes_BC`
- `T_OGR_StarterOutfit_A01_BC`
- `T_OGR_StarterOutfit_A01_N`
- `T_OGR_StarterOutfit_A01_ORM`
- `T_OGR_Base_A01_E` only for eyes or later approved class emissive accents.

Material slot target:

- Body/head/skin
- Eyes/teeth/nails
- Starter outfit/leather/wraps
- Placeholder class accent, disabled on the neutral base unless needed for review

Use 2K texture sets by default. Reserve 4K for hero variants only.

## Collision Deliverables

- Movement capsule for female baseline: approximately 315 cm high, 65-80 cm radius.
- Movement capsule for male baseline: approximately 330 cm high, 70-85 cm radius.
- Physics bodies: pelvis, spine, chest, head, upper/lower arms, hands, simplified finger groups, thighs, calves, and feet.
- Teknomancy backpacks, cannons, tanks, and shoulder rigs must use simplified auxiliary collision in later class packages, not detailed per-part collision.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Ogres/SK_OGR_Base_A01/SK_OGR_Base_A01.blend`
- Male FBX export: `SourceAssets/Exports/Characters/Ogres/SK_OGR_Base_A01/SK_OGR_Base_Male_A01.fbx`
- Female FBX export: `SourceAssets/Exports/Characters/Ogres/SK_OGR_Base_A01/SK_OGR_Base_Female_A01.fbx`
- Unreal skeletal meshes: `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01`, `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Female_A01`
- Skeletons: `/Game/Aerathea/Characters/Ogres/Base/SKEL_OGR_Base_Male_A01`, `/Game/Aerathea/Characters/Ogres/Base/SKEL_OGR_Base_Female_A01`
- Physics assets: `/Game/Aerathea/Characters/Ogres/Base/PHYS_OGR_Base_Male_A01`, `/Game/Aerathea/Characters/Ogres/Base/PHYS_OGR_Base_Female_A01`
- Animation Blueprint placeholders: `/Game/Aerathea/Characters/Ogres/Base/ABP_OGR_Base_Male_A01`, `/Game/Aerathea/Characters/Ogres/Base/ABP_OGR_Base_Female_A01`
- Startup review actors: `AET_PROD_OgreMaleBase_A01`, `AET_PROD_OgreFemaleBase_A01`

## Unreal Validation

- Imports at centimeter scale with no correction.
- Female baseline reads at roughly 315 cm; male baseline reads at roughly 330 cm.
- Feet sit on the ground plane and pivot at world origin.
- Review placement includes Minotaur, Anubisath/Sutekh, Ogre female, Ogre male, and Giant scale references.
- Skeleton supports idle, walk, run, turn, heavy step, stomp, shoulder bash, one-handed heavy attack, two-handed heavy attack, shield shove, brace cannon, cast/channel placeholder, hit reaction, stagger, and death.
- Required sockets exist:
  - `hand_r_weapon`
  - `hand_l_offhand`
  - `hand_r_twohand_grip`
  - `hand_l_twohand_grip`
  - `back_large_weapon`
  - `back_shield`
  - `spine_teknomancy_pack`
  - `shoulder_l_large`
  - `shoulder_r_large`
  - `belt_front`
  - `belt_back`
  - `vfx_mouth`
  - `vfx_eye_l`
  - `vfx_eye_r`
  - `vfx_chest_core`
  - `vfx_stomp_ground`

## Acceptance Checklist

- Female 10'0"-10'6" and male 10'4"-11'0" scale is preserved.
- Ogres read larger than Minotaurs and Anubisath/Sutekh, smaller than Giants.
- Body is broad, heavily muscled, and war-created, not a tall human.
- Neutral base remains separate from Teknomancer, Warrior, Shaman, and Necromancer class identity.
- Hands, feet, shoulders, jaw/head, and stance remain readable through LODs.
- Sockets support huge weapons, shields, Teknomancy packs, shoulder rigs, belt gear, class VFX, and stomp effects.
- Collision, physics, material slots, texture maps, LODs, export paths, and Unreal import notes are defined.
