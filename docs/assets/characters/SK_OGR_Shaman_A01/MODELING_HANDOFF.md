# SK_OGR_Shaman_A01 Modeling Handoff

## Purpose

Create the DCC source, class gear, staff silhouette, socket plan, material plan, LODs, and Unreal import path for the Ogre Shaman class package.

## Source References

- Production package: `docs/assets/characters/SK_OGR_Shaman_A01/PRODUCTION_PACKAGE.md`
- Ogre base package: `docs/assets/characters/SK_OGR_Base_A01/PRODUCTION_PACKAGE.md`
- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreShaman.png`
- Environment cue: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreShamanHut.png`
- Body/class cue: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreFemale2.png`

## Production Target

- Asset: `SK_OGR_Shaman_A01`
- Type: Skeletal Mesh class outfit and staff package.
- Height target: 330 cm male Ogre baseline, with later female fit adjustment.
- Unreal path: `/Game/Aerathea/Characters/Ogres/Shaman/`
- DCC state: not started.

## Modeling Constraints

- Use existing Ogre base proportions and bone names.
- Model large readable shapes: ritual staff, stone rune wheel, fur mantle, belt slabs, bracers, boot bands, large bone charms, and major hide wraps.
- Do not model tiny individual teeth, small stitch loops, micro-runes, cloth weave, or minor scratches.
- Keep staff, charms, and fur clear of locomotion and casting poses.
- Keep shaman visual language warm, rune-stone, hide, and bone based; do not add Teknomancy tanks or necromancer lanterns.

## Blender Setup

- Collection: `SK_OGR_Shaman_A01`
- Mesh groups:
  - `Ogre_Base_Reference`
  - `Armor_HideFur`
  - `Armor_StoneBone`
  - `Staff_RuneWheel`
  - `Charms_Fetishes`
  - `RuneGlow_Markers`
- Skeleton: inherit Ogre base skeleton.
- Add socket empties for staff, cast hands, rune wheel, and totem slam markers.

## Modeling Sequence

1. Fit the Ogre male base at 330 cm.
2. Block staff height and rune-wheel diameter before armor detail.
3. Add hide/fur mantle, belt, bracers, boot bands, and stone plates.
4. Add large bone charms and dangling fetishes as readable clusters.
5. Add socket empties and spell VFX markers.
6. Build LOD0-LOD3 with staff/rune disk preserved.
7. Export skeletal FBX after scale and silhouette approval.

## Triangle Budget

- Class gear LOD0: 18k-30k tris.
- Full character with base body: 50k-65k tris.
- LOD1: 55-60 percent.
- LOD2: 25-35 percent.
- LOD3: 10-15 percent.

## Texture Deliverables

- `T_OGR_Shaman_A01_BC`
- `T_OGR_Shaman_A01_N`
- `T_OGR_Shaman_A01_ORM`
- `T_OGR_Shaman_A01_E`

## Collision Deliverables

- Base Ogre capsule and physics asset inheritance.
- Optional simplified staff body.
- Socket-driven spell traces and area volumes.
- No per-charm, per-fur, or per-stitch collision.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Ogres/Shaman/SK_OGR_Shaman_A01/SK_OGR_Shaman_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Ogres/Shaman/SK_OGR_Shaman_A01/SK_OGR_Shaman_A01.fbx`
- Unreal skeletal mesh: `/Game/Aerathea/Characters/Ogres/Shaman/SK_OGR_Shaman_A01`
- Physics asset: `/Game/Aerathea/Characters/Ogres/Shaman/PHYS_OGR_Shaman_A01`
- Animation Blueprint: `/Game/Aerathea/Characters/Ogres/Shaman/ABP_OGR_Shaman_A01`

## Unreal Validation

- Imports at the Ogre base scale.
- Binds to the Ogre base skeleton.
- Staff and rune disk remain visible in LOD2 and LOD3.
- Warm rune emissive stays localized to spell read points.
- Shaman silhouette is distinct from Teknomancer and Necromancer.

## Acceptance Checklist

- Ogre mass, staff, rune wheel, fur/hide, and cairn charm language read from distance.
- Class gear is modular over the base Ogre body.
- Sockets and spell markers support cairn-channel, totem slam, storm/fire cast, and ritual chant poses.
- Final sculpt, retopo, UVs, textures, skin weighting, physics tuning, and animation remain pending.
