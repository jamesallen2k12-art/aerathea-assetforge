# SK_OGR_Necromancer_A01 Build And Import Status

## Current Status

- Build/import status: production package and modeling handoff complete; DCC build not started.
- Source mesh status: no Blender source or FBX export yet.
- Unreal state: not imported.
- Review scope: class art direction, modeling constraints, material plan, sockets, collision, LODs, and Unreal path are ready for approval.

## Planned Source Outputs

- Blender source: `SourceAssets/Blender/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01/SK_OGR_Necromancer_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01/SK_OGR_Necromancer_A01.fbx`
- DCC review render: `Saved/Automation/OgreNecromancerReview/SK_OGR_Necromancer_A01_DCCReview.png`

## Planned Unreal Assets

- `/Game/Aerathea/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01`
- `/Game/Aerathea/Characters/Ogres/Necromancer/PHYS_OGR_Necromancer_A01`
- `/Game/Aerathea/Characters/Ogres/Necromancer/ABP_OGR_Necromancer_A01`
- `/Game/Aerathea/Materials/Instances/MI_OGR_Necromancer_A01_GraveCloth`
- `/Game/Aerathea/Materials/Instances/MI_OGR_Necromancer_A01_BoneTrophies`
- `/Game/Aerathea/Materials/Instances/MI_OGR_Necromancer_A01_TombMetal`
- `/Game/Aerathea/Materials/Instances/MI_OGR_Necromancer_A01_NecroGlow`

## Completed Prerequisites

- Production package: `docs/assets/characters/SK_OGR_Necromancer_A01/PRODUCTION_PACKAGE.md`
- Modeling handoff: `docs/assets/characters/SK_OGR_Necromancer_A01/MODELING_HANDOFF.md`
- Source concepts visually inspected: `OgreNecromancer.png`, `OgreNecropolis.png`, `OgreMale2.png`

## Blocking Items

- Needs approval before DCC build.
- Depends on the final shared Ogre skeleton direction after `SK_OGR_Base_A01` final rig review.
- Final sculpt, retopo, UVs, authored textures, skin weighting, tuned physics, and real animation are not started.

## Remaining To Finalize

1. Approve final Necromancer class silhouette and green-black grave material language.
2. Build first-pass DCC class-fit source over Ogre male base.
3. Export FBX and import to Unreal.
4. Generate material instances, LOD0-LOD3, sockets, physics asset, and ABP placeholder.
5. Validate scale and class readability against `SK_OGR_Teknomancer_A01`, `SK_OGR_Warrior_Rival_A01`, and `SK_OGR_Shaman_A01`.
