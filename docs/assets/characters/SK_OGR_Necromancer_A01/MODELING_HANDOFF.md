# SK_OGR_Necromancer_A01 Modeling Handoff

## Purpose

Create the DCC source, class gear, grave-lantern staff silhouette, socket plan, material plan, LODs, and Unreal import path for the Ogre Necromancer class package.

## Source References

- Production package: `docs/assets/characters/SK_OGR_Necromancer_A01/PRODUCTION_PACKAGE.md`
- Ogre base package: `docs/assets/characters/SK_OGR_Base_A01/PRODUCTION_PACKAGE.md`
- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreNecromancer.png`
- Environment cue: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreNecropolis.png`
- Body/class cue: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreMale2.png`

## Production Target

- Asset: `SK_OGR_Necromancer_A01`
- Type: Skeletal Mesh class outfit and staff package.
- Height target: 330 cm male Ogre baseline, with later female fit adjustment.
- Unreal path: `/Game/Aerathea/Characters/Ogres/Necromancer/`
- DCC state: first-pass Blender source and FBX export complete; final class art polish pending.

## Modeling Constraints

- Use existing Ogre base proportions and bone names.
- Model large readable shapes: grave-lantern staff, skull belt, tombstone plates, bone trophy clusters, broad cloth strips, bracers, boot bands, and heavy chains.
- Do not model tiny individual chain links, small bone pores, micro-runes, cloth weave, or minor scratches.
- Keep staff, lantern, trophies, and cloth strips clear of locomotion and casting poses.
- Keep necromancer visual language grave green, bone, tomb metal, and black cloth based; do not add Teknomancy tanks or shamanic ember rune wheels.

## Blender Setup

- Collection: `SK_OGR_Necromancer_A01`
- Mesh groups:
  - `Ogre_Base_Reference`
  - `Armor_TombMetal`
  - `Cloth_GraveWraps`
  - `Bone_Trophies`
  - `Staff_GraveLantern`
  - `NecroGlow_Markers`
- Skeleton: inherit Ogre base skeleton.
- Add socket empties for staff lantern, cast hands, skull belt, corpse-raise, and drain markers.

## Modeling Sequence

1. Fit the Ogre male base at 330 cm.
2. Block staff height and grave-lantern size before armor detail.
3. Add skull belt, shoulder tomb plates, bracers, boot bands, and grave cloth.
4. Add large bone trophy clusters as readable grouped forms.
5. Add socket empties and necromantic VFX markers.
6. Build LOD0-LOD3 with staff lantern and skull belt preserved.
7. Export skeletal FBX after scale and silhouette approval.

## Triangle Budget

- Class gear LOD0: 22k-35k tris.
- Full character with base body: 55k-70k tris for hero/NPC review; normal gameplay target 50k-60k.
- LOD1: 55-60 percent.
- LOD2: 25-35 percent.
- LOD3: 10-15 percent.

## Texture Deliverables

- `T_OGR_Necromancer_A01_BC`
- `T_OGR_Necromancer_A01_N`
- `T_OGR_Necromancer_A01_ORM`
- `T_OGR_Necromancer_A01_E`

## Collision Deliverables

- Base Ogre capsule and physics asset inheritance.
- Optional simplified staff body.
- Optional simplified large trophy bodies only if ragdoll readability needs them.
- Socket-driven curse, drain, and corpse-raise traces/volumes.
- No per-chain, per-skull-chip, or per-cloth-strip collision.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01/SK_OGR_Necromancer_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01/SK_OGR_Necromancer_A01.fbx`
- Unreal skeletal mesh: `/Game/Aerathea/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01`
- Physics asset: `/Game/Aerathea/Characters/Ogres/Necromancer/PHYS_OGR_Necromancer_A01`
- Animation Blueprint: `/Game/Aerathea/Characters/Ogres/Necromancer/ABP_OGR_Necromancer_A01`

## Unreal Validation

- Imports at the Ogre base scale.
- Binds to the Ogre base skeleton.
- Staff lantern and skull belt remain visible in LOD2 and LOD3.
- Green-black emissive stays localized to necromantic read points.
- Necromancer silhouette is distinct from Teknomancer and Shaman.

## Acceptance Checklist

- Ogre mass, grave-lantern staff, skull belt, tomb plates, black cloth, and green-black magic read from distance.
- Class gear is modular over the base Ogre body.
- Sockets and spell markers support corpse-raise, drain, curse, command, staff plant, and channel loop poses.
- Final sculpt, retopo, UVs, textures, skin weighting, physics tuning, and animation remain pending.
