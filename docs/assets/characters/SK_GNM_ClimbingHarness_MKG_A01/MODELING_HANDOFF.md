# SK_GNM_ClimbingHarness_MKG_A01 Modeling Handoff

## Purpose

Create the production DCC source and game-ready asset for `Gnome Armory.png#Utility_ClimbingHarness` from the Gnome/Mekgineer armory catalog.

## Source References

- Production package: `docs/assets/characters/SK_GNM_ClimbingHarness_MKG_A01/PRODUCTION_PACKAGE.md`
- Parent kit: `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md`
- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Armory.png`

## Production Target

Skeletal/attachable equipment with this primary read: wide waist harness, thigh loops, large belt buckle, hook ring, and sturdy leather straps.

## Modeling Constraints

- fits `SK_GNM_Base_A01`; cloth/strap deformation tied to body approval.
- Block against `SK_GNM_Base_A01` once the body source mesh exists. Model primary armor plates, harness straps, boots, gloves, hardpoints, and core housings as real geometry. Texture tiny rivets, stitching, scratches, and fine seams.
- Preserve compact gnome ergonomics and avoid human-scale proportions.
- Reserve micro-detail for texture/normal maps.

## Blender Setup

- Scene scale: centimeters, 1 Unreal unit = 1 cm.
- Object/collection name: `SK_GNM_ClimbingHarness_MKG_A01`.
- Apply transforms before FBX export.
- Use weighted normals where they support hand-painted bevel readability.

## Modeling Sequence

1. Block the primary silhouette in simple readable forms.
2. Establish grip, attachment, bottom-center, or socket pivot according to the production package.
3. Add large plates, barrels, blades, housings, packs, straps, or armor shells as real geometry.
4. Add only silhouette-relevant bevels, hinges, lenses, core frames, and clamps.
5. Create UVs for a compact BC/N/ORM texture set and optional emissive mask.
6. Build LOD0-LOD3 while preserving the primary profile.
7. Export FBX and validate scale beside the gnome reference.

## Triangle Budget

LOD0 2.5k-5k tris, shared leather/metal material.

## Texture Deliverables

- `T_GNM_ClimbingHarness_MKG_A01_BC`
- `T_GNM_ClimbingHarness_MKG_A01_N`
- `T_GNM_ClimbingHarness_MKG_A01_ORM`
- `T_GNM_ClimbingHarness_MKG_A01_E` only for the explicit blue Aetherium lens/core/window
- Prefer one material slot; use two only when a backpack, rifle, shield, or configuration needs a shared core material split.

## Collision Deliverables

Equipped attachment collision disabled by default. Use gnome capsule/physics asset for character movement and add per-module physics bodies only after the gnome base skeleton is approved.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Gnomes/Gear/SK_GNM_ClimbingHarness_MKG_A01/SK_GNM_ClimbingHarness_MKG_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Gnomes/Gear/SK_GNM_ClimbingHarness_MKG_A01/SK_GNM_ClimbingHarness_MKG_A01.fbx`
- Unreal path: `/Game/Aerathea/Characters/Gnomes/Gear/SK_GNM_ClimbingHarness_MKG_A01`

## Unreal Validation

- Asset imports at centimeter scale.
- Pivot and sockets match the package notes.
- Material slot count remains within budget.
- LOD0-LOD3 preserve the silhouette.
- Equipped collision is disabled unless this is a world prop or display item.

## Acceptance Checklist

- Gnome/Mekgineer identity is clear.
- Primary silhouette reads at MMO distance.
- Material language matches the existing armory slice.
- Glow is restrained and tied to a specific Aetherium part.
- Texture-backed micro-detail replaces excessive modeled rivets, gears, or stitching.
