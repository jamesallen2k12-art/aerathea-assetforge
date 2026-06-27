# SM_OGR_CairnBattleGate_A01 Production Package

## Art Direction Summary

`SM_OGR_CairnBattleGate_A01` is the first Ogre cairn fortification slice for `KIT_GNM_OGR_RivalryEncounter_A01`. It converts the Ogre gate and fortress references into a reusable battle-gate module: two heavy cairn-stone tower masses, a central barred gate, crude blackened-iron braces, skull cresting, chain/hoist silhouettes, red war banners, and restrained forge-orange Teknomancy glow.

The asset should read as Ogre-built: massive, practical, intimidating, and crude in a deliberate way. It is not a refined human castle gate and not a full fortress yet. It is the first module that proves the Ogre fortification language beside the Gnome Heavy Mek, Ogre Teknomancer, and Ogre Warrior review actors.

## Gameplay Purpose

- Defines the first reusable Ogre fortification module for battlefield, siege, and encounter staging.
- Frames the Gnome/Ogre rivalry startup scene behind or beside the active combatants.
- Provides snap points for future wall modules, brazier VFX, banners, gate defenders, and portcullis logic.
- Establishes material language for `KIT_OGR_CairnFortifications_A01`.
- Gives designers a large static obstacle with simple collision and readable MMO silhouette.

## Silhouette Notes

- Two compact but heavy side tower masses.
- Broad central double gate with barred iron or portcullis read.
- High skull crest over the gate arch.
- Spiked capstones, chunky crenellations, large iron brace plates, and hanging chain silhouettes.
- Red banner drops on both sides.
- Small forge-orange glow windows/braziers only where useful for readability.

## Scale Notes

- Designed for 10'0"-11'0" Ogres, with enough clearance for male Ogre warriors and Teknomancers.
- Target gate opening: 420-500 cm wide, 430-520 cm tall.
- Full review module width target: 1100-1400 cm.
- Full review module height target: 650-850 cm.
- Pivot: ground center at the middle of the gate opening.
- Startup actor: `AET_PROD_OGR_CairnBattleGate_A01`.

## Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Cairn stone | blue-gray, soot gray, chipped dark stone | towers, wall blocks, arch stones, plinths |
| Blackened iron | soot black, dark steel, worn edges | portcullis, braces, spikes, chain/hoist hardware |
| Rough timber | dark worn timber | inner double doors and cross beams |
| Bone trophies | aged ivory | skull crest, hanging skulls, warning trophies |
| Banner cloth | dirty deep red, red-brown warpaint marks | faction banners and hanging warnings |
| Ogre Tek glow | forge orange, ember yellow | brazier bowls, gate core windows, small runes |

## Concept Image Prompt

Create an original stylized fantasy MMORPG static mesh concept sheet of `SM_OGR_CairnBattleGate_A01`, an Ogre cairn battle gate for the world of Aerathea. The design should emphasize two massive cairn-stone tower masses, a central barred iron-and-timber gate with Ogre-sized clearance, blackened-iron braces, chunky capstones, large spikes, skull cresting, hanging chains, red war banners, crude forge-orange Teknomancy glow, battlefield dust, and brutal defensive purpose for a 10-11 ft Ogre warband. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a static mesh production sheet with front view, side depth view, top footprint, snap sockets, collision blocks, material swatches, and scale beside an Ogre warrior and a Gnome Heavy Mek. Avoid copied franchise designs, excessive micro-rivets, unreadable chain clutter, photoreal over-detail, tiny modeled stones, text, and watermarks.

## Modeling Notes

- Build the first pass as one combined static mesh review module.
- Model real geometry for tower masses, gate bars, doors, large braces, skull crest, banners, brazier bowls, spikes, and big chain silhouettes.
- Use broad stone blocks and bevels; fake individual small chips, tiny cracks, micro chains, rivets, and carved scratches in texture/normal maps later.
- Keep the top crenellations and spikes large enough to read from the startup camera.
- Keep modular snap points centered and easy to align for future wall modules.
- The portcullis and doors can be static in this pass; animated gate Blueprint behavior is future work.

## Texture And Material Notes

- `T_OGR_CairnBattleGate_A01_BC`
- `T_OGR_CairnBattleGate_A01_N`
- `T_OGR_CairnBattleGate_A01_ORM`
- `T_OGR_CairnBattleGate_A01_E`
- Use packed ORM: Occlusion, Roughness, Metallic.
- Emissive only for brazier coals, small gate forge windows, skull-eye glow, or optional Tek runes.
- Prefer a 2K material atlas for common gate pieces; 4K only if promoted to a hero fortress gate.

## Triangle Budget

- Review blockout LOD0 target: under 18k tris.
- Final production LOD0 target: 12k-22k tris.
- Material slot target: 5-7 for first pass, 2-3 after final atlas consolidation.

## LOD Plan

- LOD0: full tower mass, arch, gate bars, door planks, skull crest, banners, spikes, braziers, sockets.
- LOD1: 55-60 percent; reduce stone course cuts, secondary spikes, banner thickness, and brace bevels.
- LOD2: 25-35 percent; merge wall blocks, simplify crest and brazier shapes, reduce portcullis bars.
- LOD3: 10-15 percent; preserve silhouette, gate opening, two towers, skull crest, red banners, and forge glow.

## Collision Notes

- Use simple authored UCX boxes for left tower/wall, right tower/wall, center arch, and closed gate obstruction.
- Do not use complex-as-simple for final gameplay.
- Gate opening can remain blocked for this review slice; later `BP_OGR_CairnBattleGate_A01` can swap open/closed collision.
- Banners, chains, spikes, and braziers should be non-blocking decoration.

## Animation Notes

- Static mesh in this pass.
- Future Blueprint/animation options:
  - Portcullis raise/lower.
  - Door open/close.
  - Brazier flame VFX idle.
  - Gate impact shake.
  - Siege damage state swap.

## Unreal Import Notes

- Asset type: Static Mesh.
- Primary mesh: `SM_OGR_CairnBattleGate_A01`.
- Unreal path: `/Game/Aerathea/Props/Ogres/CairnFortifications/`.
- Collision: simple UCX review collision.
- LODs: generated LOD0-LOD3 in the import script.
- Required static mesh sockets:
  - `snap_wall_l`
  - `snap_wall_r`
  - `gate_center`
  - `portcullis_top`
  - `portcullis_bottom`
  - `vfx_brazier_l`
  - `vfx_brazier_r`
  - `vfx_gate_forge`
  - `vfx_skull_crest`
  - `socket_banner_l`
  - `socket_banner_r`
  - `ai_gate_defender_l`
  - `ai_gate_defender_r`

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_OGR_CairnBattleGate_A01/`
- Source: `SourceAssets/Blender/Props/Ogres/CairnFortifications/SM_OGR_CairnBattleGate_A01/`
- Export: `SourceAssets/Exports/Props/Ogres/CairnFortifications/SM_OGR_CairnBattleGate_A01/`
- Unreal: `/Game/Aerathea/Props/Ogres/CairnFortifications/`
- DCC script: `Tools/DCC/build_ogre_cairn_gate.py`
- Unreal import script: `Tools/Unreal/import_ogre_cairn_gate.py`

## Quality Gate Checklist

- Reads as Ogre cairn fortification, not a human castle wall.
- Gate clearance and overall scale support 10-11 ft Ogres.
- The module is buildable as a mid-poly static mesh.
- Stone, iron, bone, banner, and forge glow materials are separated.
- Glow is sparing and localized.
- LOD0-LOD3, collision, sockets, material slots, and Unreal path are defined.
- Future Blueprint behavior is noted without blocking first-pass static review.
