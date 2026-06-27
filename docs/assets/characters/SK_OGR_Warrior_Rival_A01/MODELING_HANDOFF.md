# SK_OGR_Warrior_Rival_A01 Modeling Handoff

## Purpose

Create a first-pass Ogre Warrior review mesh for the Gnome/Ogre rivalry kit. This validates melee silhouette, shield/hammer scale, sockets, startup placement, and contrast against `SK_OGR_Teknomancer_A01` and `SK_GNM_HeavyMek_Rivalry_A01`.

## Source References

- `docs/assets/characters/SK_OGR_Warrior_Rival_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_OGR_Base_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/PRODUCTION_PACKAGE.md`
- `OgreWarrior.png`
- `OgreMale1.png`
- `GnomevsOgre*.png`

## Production Target

- Asset: `SK_OGR_Warrior_Rival_A01`
- Type: Skeletal Mesh review asset.
- Height target: 330 cm male Ogre baseline.
- Unreal path: `/Game/Aerathea/Characters/Ogres/Warrior/`
- Startup actor: `AET_PROD_OgreWarrior_Rival_A01`

## Modeling Constraints

- Use existing Ogre base proportions and bone names.
- Model large readable shapes: shield slab, shield frame, shoulder plates, bracers, hammer, belt, skirt plates, knee guards, big spikes.
- Do not spend geometry on tiny rivets, individual small chain links, cloth weave, surface scratches, or micro-runes.
- Keep shield and hammer aligned to hand sockets for later modularization.

## Blender Setup

- Build script: `Tools/DCC/build_ogre_warrior.py`
- Blender source output: `SourceAssets/Blender/Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01/SK_OGR_Warrior_Rival_A01.blend`
- FBX export output: `SourceAssets/Exports/Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01/SK_OGR_Warrior_Rival_A01.fbx`
- DCC review output: `Saved/Automation/OgreWarriorReview/SK_OGR_Warrior_Rival_A01_DCCReview.png`

## Modeling Sequence

1. Generate the Ogre male base skeleton/body at 330 cm.
2. Add warrior armor: shoulders, bracers, belt disk, skirt plates, knee guards.
3. Add tower shield to the left side with large frame, core windows, spikes, and trophy disk.
4. Add chained crusher hammer to the right hand.
5. Add socket empties and export the review FBX.
6. Import, assign material instances, generate LOD0-LOD3, create physics/ABP placeholders, and place the startup actor.

## Acceptance Checklist

- Ogre mass, shield slab, hammer block, and shoulder width are clear from a distance.
- Warrior is visually simpler and more direct than the Teknomancer.
- Startup import validates material slots, LODs, physics, skeleton binding, and sockets.
- Final sculpt/retopo/UVs/textures/animation remain explicitly pending.
