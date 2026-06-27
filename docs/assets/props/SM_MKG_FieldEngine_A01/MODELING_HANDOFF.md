# SM_MKG_FieldEngine_A01 Modeling Handoff

## Purpose

Create the production DCC source and game-ready asset for `Gnome Armory.png#Backpack_FieldEngine` from the Gnome/Mekgineer armory catalog.

## Source References

- Production package: `docs/assets/props/SM_MKG_FieldEngine_A01/PRODUCTION_PACKAGE.md`
- Parent kit: `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md`
- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Armory.png`

## Production Target

Static Mesh backpack/power module with this primary read: boxy engine housing with side cylinders, square blue display, top carry handle, and exhaust-free restrained profile.

## Modeling Constraints

- 45-70 cm tall; `back_pack` attachment pivot required.
- Model the primary body, grips, barrels, blades, housings, sockets, lenses, plates, large hinges, and major straps as real geometry. Fake tiny rivets, screws, edge scratches, leather stitching, fine wood/metal wear, and small stamped marks in texture/normal maps.
- Preserve compact gnome ergonomics and avoid human-scale proportions.
- Reserve micro-detail for texture/normal maps.

## Blender Setup

- Scene scale: centimeters, 1 Unreal unit = 1 cm.
- Object/collection name: `SM_MKG_FieldEngine_A01`.
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

LOD0 3.5k-7k tris, 1-2 material slots.

## Texture Deliverables

- `T_MKG_FieldEngine_A01_BC`
- `T_MKG_FieldEngine_A01_N`
- `T_MKG_FieldEngine_A01_ORM`
- `T_MKG_FieldEngine_A01_E` only for the explicit blue Aetherium lens/core/window
- Prefer one material slot; use two only when a backpack, rifle, shield, or configuration needs a shared core material split.

## Collision Deliverables

Attachment collision disabled while equipped. World display uses simple box collision. Avoid complex-as-simple collision.

## Export Targets

- Blender source: `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_FieldEngine_A01/SM_MKG_FieldEngine_A01.blend`
- FBX export: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_FieldEngine_A01/SM_MKG_FieldEngine_A01.fbx`
- Unreal path: `/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_FieldEngine_A01`

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
