# SM_MKG_AetherCoreUnit_A01 Modeling Handoff

## Purpose

Create the production DCC source and game-ready static mesh for a portable Mekgineer Aether core unit. The asset supports backpack attachment planning, powered-device VFX tests, workshop dressing, and future quest/crafting props.

## Source References

- Production package: `docs/assets/props/SM_MKG_AetherCoreUnit_A01/PRODUCTION_PACKAGE.md`
- Source concept child: `Gnome Armory.png#Gear_AetherCoreUnit`
- Blender source: `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01/SM_MKG_AetherCoreUnit_A01.blend`
- FBX export: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01/SM_MKG_AetherCoreUnit_A01.fbx`
- Unreal mesh: `/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01`

## Production Target

Backpack-scale static mesh power module with a squat metal housing, compact side cylinders, leather carry straps, rear mount lugs, and a protected blue Aetherium crystal chamber.

## Modeling Constraints

- Target height: 45-60 cm.
- Pivot: lower rear center for backpack socketing and shelf placement.
- Model real geometry for housing, large tubes, handle loops, core frame, strap blocks, and rear lugs.
- Fake tiny screws, gauge ticks, leather stitching, vents, and panel scratches through texture/normal maps.
- Keep the core glow readable but contained behind framing.

## Blender Setup

- Scene scale: centimeters.
- Origin at lower rear center.
- Keep the core chamber, casing, straps, and tubes as cleanly named objects for review.
- Apply transforms and check face normals before export.

## Modeling Sequence

1. Block the squat rectangular housing and rear attachment plane.
2. Add side cylinders and handle loops as chunky silhouette forms.
3. Frame the central Aetherium core window with protective metal.
4. Add strap blocks and rear lugs for future socket planning.
5. Use bevels on large metal edges only; reserve fine panel seams for textures.
6. Export FBX and reimport to Unreal for scale review.

## Triangle Budget

- LOD0: 3k-6k tris.
- LOD1: 55-65 percent of LOD0.
- LOD2: 30-40 percent of LOD0.
- LOD3: boxed silhouette with simplified core inset.

## Texture Deliverables

- `T_MKG_AetherCoreUnit_A01_BC`
- `T_MKG_AetherCoreUnit_A01_N`
- `T_MKG_AetherCoreUnit_A01_ORM`
- `T_MKG_AetherCoreUnit_A01_E`
- Material instance: `MI_MKG_AetherCoreUnit_A01`

## Collision Deliverables

Attachment collision disabled by default. World placement uses simple box collision plus optional interaction bounds.

## Export Targets

- FBX: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01/SM_MKG_AetherCoreUnit_A01.fbx`
- Unreal folder: `/Game/Aerathea/Props/Mekgineer/Armory/`

## Unreal Validation

- Mesh imports with material slots for Mekgineer metal/leather and optional Aetherium emissive.
- Pivot supports shelf placement and future `back_pack` socket fit.
- Startup scene validator includes the mesh as a placed review prop.

## Acceptance Checklist

- Portable gnome engineering silhouette.
- Core glow restrained and protected by geometry.
- Backpack/display pivots documented.
- LOD0-LOD3 and collision plan preserved.
- No over-modeled micro detail.
