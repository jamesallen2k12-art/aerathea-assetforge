# SM_MKG_AetheriumGrenade_A01 Modeling Handoff

## Purpose

Create the production DCC source and game-ready static mesh for a Mekgineer Aetherium grenade. The asset supports future throwable tests, inventory icons, vendor/loot display, workshop dressing, and VFX socket planning.

## Source References

- Production package: `docs/assets/props/SM_MKG_AetheriumGrenade_A01/PRODUCTION_PACKAGE.md`
- Source concept child: `Gnome Armory.png#Grenades_AetheriumGrenade`
- Blender source: `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01/SM_MKG_AetheriumGrenade_A01.blend`
- FBX export: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01/SM_MKG_AetheriumGrenade_A01.fbx`
- Unreal mesh: `/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01`

## Production Target

Small round throwable static mesh with brass ribs, dark-iron casing, a protected blue Aetherium core window, and an oversized pull mechanism sized for gnome hands.

## Modeling Constraints

- Target diameter: 18-24 cm.
- Pivot: center of mass.
- Socket targets: `VFX_Core`, `PullRing`.
- Model real geometry for main shell, large ribs, cap, pull ring, and core frame.
- Texture stamped safety runes, scorch marks, small screws, dents, and seam wear.

## Blender Setup

- Scene scale: centimeters.
- Origin at center of mass.
- Keep body, ribs, cap, pull ring, and core frame cleanly separated for review.
- Apply transforms and verify normals before export.

## Modeling Sequence

1. Block the round/oval body and large protective ribs.
2. Add cap and pull ring as oversized readable forms.
3. Frame the Aetherium core window with protective metal.
4. Add a subtle grip band if needed for silhouette.
5. Check inventory-icon readability from a three-quarter view.
6. Export FBX and verify in Unreal.

## Triangle Budget

- LOD0: 1k-2.5k tris.
- LOD1: 50-60 percent of LOD0.
- LOD2: 25-35 percent of LOD0.
- LOD3: round silhouette with core color mark.

## Texture Deliverables

- `T_MKG_AetheriumGrenade_A01_BC`
- `T_MKG_AetheriumGrenade_A01_N`
- `T_MKG_AetheriumGrenade_A01_ORM`
- `T_MKG_AetheriumGrenade_A01_E`
- Material instance: `MI_MKG_AetheriumGrenade_A01`

## Collision Deliverables

Equipped/held collision disabled. World pickup uses simple sphere or capsule collision. Projectile collision belongs to the future throwable Blueprint.

## Export Targets

- FBX: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01/SM_MKG_AetheriumGrenade_A01.fbx`
- Unreal folder: `/Game/Aerathea/Props/Mekgineer/Armory/`

## Unreal Validation

- Mesh imports with material slots.
- Pivot is centered for throw/physics planning.
- Future `VFX_Core` and `PullRing` socket positions are documented.
- Startup scene validator includes the mesh as a placed review prop.

## Acceptance Checklist

- Original gnome/Mekgineer throwable silhouette.
- Protected and restrained Aetherium core.
- Projectile behavior is not baked into mesh.
- LOD0-LOD3, sockets, and pickup collision plan preserved.
- Inventory readability considered.
