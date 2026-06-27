# SK_INF_Lesser_A01 Modeling Handoff

## Purpose

Create the first DCC lifecycle review source for Lesser Infernals. This is a deterministic blockout for stage naming, height, silhouette, horns, claws, wings, tail, culling temper posture, sockets, material slots, and Unreal import review. It is not final sculpted or painted fantasy art.

## Source References

- Lore: `docs/lore/races/INFERNALS.md`
- Production package: `docs/assets/characters/SK_INF_Lesser_A01/PRODUCTION_PACKAGE.md`
- Visual rules: `docs/assets/characters/SK_INF_Base_A01/VISUAL_RULES.md`
- Cult package: `docs/assets/kits/KIT_INF_BalgorothCult_A01/PRODUCTION_PACKAGE.md`

## Production Target

First-pass stage meshes:

| Stage | Mesh name | Height |
| --- | --- | ---: |
| Spawn | `SK_INF_Lesser_Spawn_A01` | 80 cm |
| 1st Kill | `SK_INF_Lesser_1stKill_A01` | 115 cm |
| Blooded | `SK_INF_Lesser_Blooded_A01` | 150 cm |
| Elder | `SK_INF_Lesser_Elder_A01` | 220 cm |
| Ancient | `SK_INF_Lesser_Ancient_A01` | 250 cm |

The first review focuses on scale and silhouette. Final exact heights remain open until approval.

## Modeling Constraints

- Author in centimeters, 1 Unreal unit = 1 cm.
- Feet at ground origin per exported mesh.
- Use real geometry for horns, claws, wings, tails, body masses, and major ritual marks.
- Use blockout materials for skin, horns/claws, wings, wraps, brands, and scale markers.
- Show culling temper through aggressive posture in Spawn, 1st Kill, and Blooded.
- Elder and Ancient should read controlled and dangerous, not merely bigger.

## Blender Setup

- Collection: `SK_INF_Lesser_A01`
- Armatures:
  - `SKEL_INF_Lesser_Spawn_A01`
  - `SKEL_INF_Lesser_1stKill_A01`
  - `SKEL_INF_Lesser_Blooded_A01`
  - `SKEL_INF_Lesser_Elder_A01`
  - `SKEL_INF_Lesser_Ancient_A01`
- Mesh groups per stage: body, head, horns, claws, wings, tail, wraps/brand markers.

## Modeling Sequence

1. Create stage meshes at the approved first-pass heights.
2. Add stage-specific horns, wing growth, tail length, claw read, and posture.
3. Add minimal ritual/cult details: brand mark, wrap, or bead silhouette.
4. Add sockets for eyes, chest brand, claws, wing tips, and tail tip.
5. Create review scale markers for 180 cm humanoid and adult Infernal targets.
6. Export one skeletal FBX per stage.
7. Render a DCC review board showing all stages together.

## Triangle Budget

- First blockout: intentionally low-poly review geometry.
- Final targets:
  - Spawn/1st Kill: 12k-20k tris.
  - Blooded: 18k-28k tris.
  - Elder/Ancient: 25k-40k tris.

## Texture Deliverables

Review blockout material names:

- `M_INF_Skin_Blockout_A01`
- `M_INF_HornClaw_Blockout_A01`
- `M_INF_Wing_Blockout_A01`
- `M_INF_Wrap_Blockout_A01`
- `M_INF_BrandGlow_Blockout_A01`

Final texture names:

- `T_INF_Lesser_A01_BC`
- `T_INF_Lesser_A01_N`
- `T_INF_Lesser_A01_ORM`
- `T_INF_Lesser_A01_E`

## Collision Deliverables

- Per-stage simplified humanoid capsule.
- Tail and wings use auxiliary simplified bodies only when gameplay needs them.
- Spawn and 1st Kill should not use complex wing collision.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_A01.blend`
- FBX exports:
  - `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_Spawn_A01.fbx`
  - `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_1stKill_A01.fbx`
  - `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_Blooded_A01.fbx`
  - `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_Elder_A01.fbx`
  - `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_Ancient_A01.fbx`
- Unreal folder: `/Game/Aerathea/Characters/Infernals/Lesser/`

## Unreal Validation

- Imports at centimeter scale.
- Review actors appear in order: Spawn, 1st Kill, Blooded, Elder, Ancient.
- Height reads against 180 cm marker and adult Infernal compact/tall markers.
- Required sockets exist: `vfx_eye_l`, `vfx_eye_r`, `vfx_brand_chest`, `claw_l`, `claw_r`, `tail_tip`, `wing_l_tip`, `wing_r_tip`.

## Acceptance Checklist

- Approved stage names are used exactly.
- Stage height progression is readable.
- Culling temper posture is visible in young stages.
- Horn, wing, tail, and claw development is readable.
- Infernals remain mortal-descended race silhouettes, not true Abyss demons.
