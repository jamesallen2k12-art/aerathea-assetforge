# SM_DEL_DuskspiteBlade_A01 Production Package

## Art Direction Summary

- Asset name: `SM_DEL_DuskspiteBlade_A01`
- Asset type: Static Mesh blade
- Source: `Dark Elven Armory.png#Blade_Duskspite`
- Parent kit: `KIT_DEL_Armory_A01`
- Status: Production package ready; DCC build not started

Original Dark Elven crescent blade with refined obsidian edge, dark silver spine, violet moonlit accent, and oath-bound martial elegance.

## Gameplay Purpose

Shadowblade sidearm for Dark Elven rogues, sentinels, spellblades, NPCs, armory display, and socket testing.

## Silhouette Notes

Curved crescent blade, slim grip, small guard, and clean negative space. It should look dangerous and refined, not jagged or crude.

## Scale Notes

60-90 cm depending on final one-handed or short-sword role. Author in centimeters.

## Materials And Color Palette

Dark silver, obsidian edge, black leather grip, muted violet lunar glow, subtle crescent motifs.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_DEL_DuskspiteBlade_A01` for the world of Aerathea. The design should emphasize an elegant crescent blade silhouette, dark silver spine, obsidian cutting edge, black leather grip, violet lunar glow accents, refined oath-bound Dark Elven identity, shadowblade mood, and rogue or sentinel gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, three-quarter view, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model blade, spine, guard, grip, pommel, and major bevels. Fake tiny crescent etching, scratches, and leather grain in textures.

## Texture And Material Notes

- `T_DEL_DuskspiteBlade_A01_BC`
- `T_DEL_DuskspiteBlade_A01_N`
- `T_DEL_DuskspiteBlade_A01_ORM`
- `T_DEL_DuskspiteBlade_A01_E` for violet accent only

## Triangle Budget

LOD0 1.5k-4k tris, 1 material slot.

## LOD Plan

LOD0 full blade curve; LOD1 removes minor bevels; LOD2 simplifies guard and pommel; LOD3 preserves crescent blade and grip.

## Collision Notes

Equipped collision disabled. World pickup/display uses simple bounds.

## Animation Notes

Static mesh. Combat and spell-channel motions belong to character animation later.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Weapons/DarkElven/SM_DEL_DuskspiteBlade_A01`
- Pivot: grip center.
- Scale: centimeters.
- Sockets: optional `socket_violet_glow`.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_DEL_DuskspiteBlade_A01/`
- Source: `SourceAssets/Blender/Kits/DarkElven/Armory/SM_DEL_DuskspiteBlade_A01/`
- Export: `SourceAssets/Exports/Kits/DarkElven/Armory/SM_DEL_DuskspiteBlade_A01/`
- Unreal: `/Game/Aerathea/Weapons/DarkElven/SM_DEL_DuskspiteBlade_A01`

## Quality Gate Checklist

- Refined Dark Elven identity is clear.
- Crescent silhouette reads at MMO distance.
- Glow is sparing and violet.
- Micro etching is texture detail.
- LOD and collision plans are defined.
