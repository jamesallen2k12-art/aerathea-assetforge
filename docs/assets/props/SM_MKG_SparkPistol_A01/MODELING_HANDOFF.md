# SM_MKG_SparkPistol_A01 Modeling Handoff

## Purpose

Create the production DCC source and game-ready static mesh for a compact Mekgineer spark pistol. The asset supports gnome ranged weapon identity, rack/display dressing, loot previews, and future muzzle/socket tests.

## Source References

- Production package: `docs/assets/props/SM_MKG_SparkPistol_A01/PRODUCTION_PACKAGE.md`
- Source concept child: `Gnome Armory.png#Pistols_SparkPistol`
- Blender source: `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_SparkPistol_A01/SM_MKG_SparkPistol_A01.blend`
- FBX export: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_SparkPistol_A01/SM_MKG_SparkPistol_A01.fbx`
- Unreal mesh: `/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SparkPistol_A01`

## Production Target

Short, heavy, gnome-scale static mesh firearm with a thick barrel, dark-iron muzzle ring, brass chamber, leather grip, and one small blue Aetherium capacitor. It should read as a rugged field tool, not a modern handgun.

## Modeling Constraints

- Target length: 30-42 cm.
- Pivot: grip center.
- Socket targets: `Muzzle`, `AetheriumCore`, optional `Grip`.
- Model real geometry for barrel, chamber, grip, trigger guard, muzzle ring, and capacitor housing.
- Texture soot, tiny gauge marks, grip stitching, screws, and fine scratches.

## Blender Setup

- Scene scale: centimeters.
- Origin at grip center.
- Keep side-view silhouette clean; pistol should read from third-person MMO distance.
- Apply transforms before FBX export.

## Modeling Sequence

1. Block a thick barrel, short grip, large chamber, and visible muzzle.
2. Add the trigger guard and capacitor housing as large readable forms.
3. Add bevels to chamber and muzzle edges.
4. Mark socket helper positions for `Muzzle` and `AetheriumCore`.
5. Check that the silhouette is compact and not sleek or modern.
6. Export FBX and verify in Unreal.

## Triangle Budget

- LOD0: 1.5k-3k tris.
- LOD1: 50-60 percent of LOD0.
- LOD2: 25-35 percent of LOD0.
- LOD3: simplified side silhouette.

## Texture Deliverables

- `T_MKG_SparkPistol_A01_BC`
- `T_MKG_SparkPistol_A01_N`
- `T_MKG_SparkPistol_A01_ORM`
- `T_MKG_SparkPistol_A01_E`
- Material instance: `MI_MKG_SparkPistol_A01`

## Collision Deliverables

No blocking collision while equipped. World pickup/display uses simple box collision.

## Export Targets

- FBX: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_SparkPistol_A01/SM_MKG_SparkPistol_A01.fbx`
- Unreal folder: `/Game/Aerathea/Weapons/Mekgineer/`

## Unreal Validation

- Mesh imports with material slots.
- Pivot aligns to grip center.
- Future `Muzzle` and `AetheriumCore` socket positions are documented.
- Startup scene validator includes the mesh as a placed review prop.

## Acceptance Checklist

- Compact gnome-scale firearm silhouette.
- Does not read as a modern handgun.
- Blue Aetherium accent is restrained.
- LOD0-LOD3, sockets, and collision plan preserved.
- No copied franchise weapon language.
