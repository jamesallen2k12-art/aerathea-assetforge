# SM_MKG_AetherKnife_A01 Production Package

## Art Direction Summary

- Asset name: `SM_MKG_AetherKnife_A01`
- Asset type: Static Mesh weapon / small gear prop
- Source: `Gnome Armory.png#Weapons_AetherKnife`
- Faction: Gnome / Mekgineer
- Status: Production package ready

Compact gnome-scale utility knife with a short triangular blade, chunky brass/dark-iron grip, leather wrap, and a restrained blue Aetherium accent at the pommel or blade socket. It should read as precision engineering, not a thin fantasy dagger.

## Gameplay Purpose

Supports gnome starter weapon identity, workshop display props, loot/vendor previews, and future one-handed socket tests.

## Silhouette Notes

Use a stubby, readable blade profile with a broad base and compact handle. The hilt should be oversized enough for gnome readability but not human-scale. Preserve one blue focal point only.

## Scale Notes

- Target length: 35-45 cm.
- Pivot: centered on grip for hand socketing.
- Socket fit: future `hand_r_weapon` and display rack sockets.

## Materials And Color Palette

Dark iron blade, brass guard/pommel, dark leather grip wrap, small blue Aetherium inset. Hand-painted edge highlights and baked-AO-style grip shadowing.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a compact gnome Mekgineer Aether knife for the world of Aerathea. The design should emphasize a short broad precision blade, brass and dark iron engineering, dark leather grip wrap, one small blue Aetherium power inset, practical gnome-scale ergonomics, and a clever field-tool mood. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a small weapon turnaround on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model the blade, guard, grip, pommel, and Aetherium socket as real geometry. Fake tiny screws, leather stitching, blade scratches, and stamped marks through texture/normal detail.

## Texture And Material Notes

- `T_MKG_AetherKnife_A01_BC`
- `T_MKG_AetherKnife_A01_N`
- `T_MKG_AetherKnife_A01_ORM`
- `T_MKG_AetherKnife_A01_E` for the single Aetherium inset only

Use one material slot unless a shared armory trim material is introduced.

## Triangle Budget

LOD0 target: 800-2.5k tris. Keep it under 3k unless used as a hero inventory inspect item.

## LOD Plan

- LOD0: full silhouette, bevels, socket geometry.
- LOD1: remove small bevels and secondary grip cuts.
- LOD2: simplify guard and pommel.
- LOD3: blade/grip/pommel silhouette only.

## Collision Notes

No blocking collision while equipped. Use a simple box pickup/display collision only when placed in the world.

## Animation Notes

Static mesh only. Equip, swing, and sheathe animation belongs to character animation later.

## Unreal Import Notes

- Folder: `/Game/Aerathea/Weapons/Mekgineer/`
- Mesh: `SM_MKG_AetherKnife_A01`
- Material instance: `MI_MKG_AetherKnife_A01`
- Pivot: grip center
- Scale: centimeters
- Collision: simple pickup bounds if world-placed

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_MKG_AetherKnife_A01/`
- Source: `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_AetherKnife_A01/`
- Export: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetherKnife_A01/`

## Quality Gate Checklist

- Original Aerathea gnome/Mekgineer identity.
- Compact readable silhouette.
- Brass, dark iron, leather, and blue Aetherium used consistently.
- Glow limited to one small inset.
- Mid-poly geometry with texture-backed micro-detail.
- LOD0-LOD3, collision, texture maps, and Unreal path defined.
