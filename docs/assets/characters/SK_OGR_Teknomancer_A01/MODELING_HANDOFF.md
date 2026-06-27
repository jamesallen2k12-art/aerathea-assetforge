# SK_OGR_Teknomancer_A01 Modeling Handoff

## Purpose

Build the first class-fit Ogre Teknomancer over the approved Ogre male base. This pass validates silhouette, scale, sockets, rough gear placement, Unreal import path, and startup review placement. It is not final sculpted or painted production art.

## Source References

- Production package: `docs/assets/characters/SK_OGR_Teknomancer_A01/PRODUCTION_PACKAGE.md`
- Ogre base status: `docs/assets/characters/SK_OGR_Base_A01/BUILD_IMPORT_STATUS.md`
- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreMaleTek.png`
- Rivalry concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreTekvsGnomeMek.png`

## Build Notes

- Preserve the 330 cm male Ogre review height and broad Ogre mass.
- Keep the gear modular over the base body where final art allows.
- Use a deliberately uneven silhouette: one oversized iron shoulder/upper-arm side, one more exposed working arm, back tanks, belt reactor, large bracers, and a crude powered hammer.
- The visual language must stay Ogre: overbuilt, dangerous, instinctive, forge-hot, and jealous of Gnome engineering without becoming precise Gnome machinery.
- Real geometry should cover the major shoulder slab, skull guard, bracers, belt reactor, back engine, pressure tanks, hammer head, hammer handle, large vents, and readable trophy teeth.
- Texture/normal-map small rivets, micro scratches, tiny runes, small chains, soot, leather stitching, and fine conduit wraps.

## DCC Source

- Builder: `Tools/DCC/build_ogre_teknomancer.py`
- Blender source: `SourceAssets/Blender/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01/SK_OGR_Teknomancer_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01/SK_OGR_Teknomancer_A01.fbx`
- DCC review render: `Saved/Automation/OgreTeknomancerReview/SK_OGR_Teknomancer_A01_DCCReview.png`

## Unreal Contract

- Skeletal mesh: `/Game/Aerathea/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01`
- Physics asset: `/Game/Aerathea/Characters/Ogres/Teknomancer/PHYS_OGR_Teknomancer_A01`
- Animation Blueprint: `/Game/Aerathea/Characters/Ogres/Teknomancer/ABP_OGR_Teknomancer_A01`
- Startup actor: `AET_PROD_OgreTeknomancer_A01`
- Import script: `Tools/Unreal/import_ogre_teknomancer.py`
- Material instances: `/Game/Aerathea/Materials/Instances/MI_OGR_Teknomancer_A01_*`

## Required Sockets

- `hand_r_weapon`
- `hand_l_offhand`
- `hand_r_twohand_grip`
- `hand_l_twohand_grip`
- `spine_teknomancy_pack`
- `vfx_chest_core`
- `vfx_mouth`
- `vfx_stomp_ground`
- `vfx_hammer_core`
- `vfx_bracer_l`
- `vfx_bracer_r`
- `vfx_tek_core`
- `weapon_socket_r`
- `head_fx`

## Final-Art Conversion Notes

- Replace the blockout hammer with a sculpted powered crusher tool in the 190-240 cm range.
- Retopo armor modules so final shoulder/bracer hardware does not clip heavy attack poses.
- Add clear material separation for skin, iron, leather, brass/copper, trophies, and emissive Tek glow.
- Keep emissive forge-orange focused on reactor windows, hammer core, bracer vents, and rune cuts.
- Retain the final gameplay capsule from the Ogre base and use simplified auxiliary collision for hammer/back hardware only if needed.

## Quality Gate

- Reads as an Ogre, not a tall humanoid engineer.
- Gear reads as crude Teknomancy, not precise Gnome Mek craft.
- Scale remains between Minotaur and Giant anchors.
- Primary silhouette is readable from MMO camera distance.
- Sockets, LODs, physics asset, and startup review actor validate before final sculpt work starts.
