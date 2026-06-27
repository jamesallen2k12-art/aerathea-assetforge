# SK_INF_Base_A01 Modeling Handoff

## Purpose

Create the first adult Infernal DCC review source for compact and tall adult bodies. This handoff converts the approved Infernal lore and visual rules into build-ready blockout meshes for scale, wings, tail, horns, claws, sockets, collision, and Unreal review.

## Source References

- Lore: `docs/lore/races/INFERNALS.md`
- Production package: `docs/assets/characters/SK_INF_Base_A01/PRODUCTION_PACKAGE.md`
- Final art direction: `docs/assets/characters/SK_INF_Base_A01/FINAL_ART_DIRECTION.md`
- Visual rules: `docs/assets/characters/SK_INF_Base_A01/VISUAL_RULES.md`
- Lesser lifecycle package: `docs/assets/characters/SK_INF_Lesser_A01/PRODUCTION_PACKAGE.md`

## Production Target

First adult review meshes:

| Body target | Mesh name | Height |
| --- | --- | ---: |
| Compact adult | `SK_INF_Base_Compact_A01` | 165 cm |
| Tall adult | `SK_INF_Base_Tall_A01` | 245 cm |

Adult canon range remains 5'0"-9'0" / 152-274 cm. Final production body bands are Compact, Standard, Greater, and Exalted as defined in `FINAL_ART_DIRECTION.md`.

## Modeling Constraints

- Author at real scale in centimeters.
- Feet at ground origin per exported mesh.
- Main silhouette must include horns, large folded wings, long thick tail, and black claws.
- Natural-weapon identity must read without swords, axes, bows, or polearms.
- Wings need folded review form and tip sockets.
- Tail needs root/mid/tip controls and simplified physics plan.

## Blender Setup

- Collection: `SK_INF_Base_A01`
- Armatures:
  - `SKEL_INF_Base_Compact_A01`
  - `SKEL_INF_Base_Tall_A01`
- Mesh groups per adult: body, head, horns, claws, wings, tail, ritual wraps/brands.

## Modeling Sequence

1. Block compact 165 cm and tall 245 cm adults beside Lesser stages and 180 cm humanoid marker.
2. Establish adult Infernal proportions: predatory upright stance, horn mass, folded wing mass, thick tail, clawed hands.
3. Add minimal ritual wrap/brand geometry to show Balgoroth cult language without weapon dependency.
4. Add sockets for claws, eyes, chest brand, mouth, regeneration core, wing tips, and tail tip.
5. Export one skeletal FBX per adult target.
6. Validate scale and silhouette in Unreal review.

## Triangle Budget

- First blockout: low-poly review geometry.
- Final compact adult target: 28k-40k tris.
- Final tall adult target: 32k-48k tris.
- Hero/class variants may reach 55k tris if wing or ritual detail requires it.

## Texture Deliverables

Review materials:

- `M_INF_Skin_Blockout_A01`
- `M_INF_HornClaw_Blockout_A01`
- `M_INF_Wing_Blockout_A01`
- `M_INF_Wrap_Blockout_A01`
- `M_INF_BrandGlow_Blockout_A01`

Final texture names:

- `T_INF_Base_A01_BC`
- `T_INF_Base_A01_N`
- `T_INF_Base_A01_ORM`
- `T_INF_Base_A01_E`

## Collision Deliverables

- Humanoid movement capsule per body target.
- Simplified wing auxiliary bodies; disabled for default navigation.
- Tail root/mid/tip bodies only when combat or hit reaction needs them.
- Physics bodies: pelvis, spine, chest, head, arms, hands, legs, feet, tail, simplified wings.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Infernals/SK_INF_Base_A01/SK_INF_Base_A01.blend`
- FBX exports:
  - `SourceAssets/Exports/Characters/Infernals/SK_INF_Base_A01/SK_INF_Base_Compact_A01.fbx`
  - `SourceAssets/Exports/Characters/Infernals/SK_INF_Base_A01/SK_INF_Base_Tall_A01.fbx`
- Unreal folder: `/Game/Aerathea/Characters/Infernals/Base/`

## Unreal Validation

- Imports at centimeter scale.
- Compact reads around 165 cm; tall reads around 245 cm.
- Wings, horns, claws, and tail are visible at startup review distance.
- Required sockets exist: `hand_l_claw`, `hand_r_claw`, `tail_tip`, `wing_l_tip`, `wing_r_tip`, `vfx_eye_l`, `vfx_eye_r`, `vfx_brand_chest`, `vfx_mouth`, `vfx_regen_core`.

## Acceptance Checklist

- Adult Infernal range remains within 5'0"-9'0".
- Silhouette is race-readable and not true-Abyss creature silhouette.
- Horns, folded wings, long tail, and black claws are mandatory.
- Natural-weapon doctrine is visually clear.
- Review assets import to Unreal and can be compared beside Lesser stages.
