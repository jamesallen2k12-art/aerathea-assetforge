# SM_MKG_AetherKnife_A01 Modeling Handoff

## Purpose

Create the production DCC source and game-ready static mesh for the compact Mekgineer Aether knife. The asset supports gnome starter weapon identity, workshop display dressing, loot/vendor previews, and future one-handed socket tests.

## Source References

- Production package: `docs/assets/props/SM_MKG_AetherKnife_A01/PRODUCTION_PACKAGE.md`
- Source concept child: `Gnome Armory.png#Weapons_AetherKnife`
- Blender source: `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_AetherKnife_A01/SM_MKG_AetherKnife_A01.blend`
- FBX export: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetherKnife_A01/SM_MKG_AetherKnife_A01.fbx`
- Unreal mesh: `/Game/Aerathea/Weapons/Mekgineer/SM_MKG_AetherKnife_A01`

## Production Target

Small static mesh weapon with a short broad blade, brass/dark-iron guard, leather grip, and one restrained blue Aetherium inset. It must read as a gnome precision field tool, not a human-scale dagger.

## Modeling Constraints

- Target length: 35-45 cm.
- Pivot: centered on grip for future `hand_r_weapon` socketing.
- Model real geometry for blade, guard, grip, pommel, and Aetherium socket.
- Texture tiny screws, grip stitching, scratches, stamped marks, and fine edge wear.
- Keep emissive detail limited to the single Aetherium inset.

## Blender Setup

- Scene scale: centimeters, 1 Unreal unit = 1 cm.
- Origin at grip center.
- Apply transforms before export.
- Keep object and material names aligned to `SM_MKG_AetherKnife_A01`.
- Use flat/weighted normal styling where it improves hand-painted readability.

## Modeling Sequence

1. Block the blade, grip, guard, and pommel in simple readable forms.
2. Add bevels only where they support silhouette and highlight readability.
3. Add the Aetherium socket as a separate framed form.
4. Add large grip-wrap bands as geometry; reserve stitching for texture/normal detail.
5. Verify the side silhouette at MMO camera distance.
6. Export FBX and reimport to Unreal with centimeter scale.

## Triangle Budget

- LOD0: 800-2.5k tris, hard cap 3k.
- LOD1: 50-60 percent of LOD0.
- LOD2: 25-35 percent of LOD0.
- LOD3: blade/grip/pommel silhouette only.

## Texture Deliverables

- `T_MKG_AetherKnife_A01_BC`
- `T_MKG_AetherKnife_A01_N`
- `T_MKG_AetherKnife_A01_ORM`
- `T_MKG_AetherKnife_A01_E`
- Material instance: `MI_MKG_AetherKnife_A01`

## Collision Deliverables

No blocking collision while equipped. Add a simple pickup/display box only if world-placed.

## Export Targets

- FBX: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetherKnife_A01/SM_MKG_AetherKnife_A01.fbx`
- Unreal folder: `/Game/Aerathea/Weapons/Mekgineer/`

## Unreal Validation

- Mesh imports with at least one material slot.
- Pivot aligns to grip center.
- Scale reads as gnome equipment beside the 110 cm gnome startup reference.
- Startup scene validator includes the mesh as a placed review prop.

## Acceptance Checklist

- Compact readable gnome/Mekgineer silhouette.
- Brass, dark iron, leather, and blue Aetherium material language.
- Glow used once and sparingly.
- LOD0-LOD3 plan preserved.
- No copied franchise shapes or markings.
