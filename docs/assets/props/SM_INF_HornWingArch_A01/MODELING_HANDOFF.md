# SM_INF_HornWingArch_A01 Modeling Handoff

## Purpose

Create the first DCC-ready Balgoroth cult gate/threshold mesh for `KIT_INF_BalgorothCult_A01`. The arch must validate Infernal cult threshold scale, symbol readability, collision clearance, snap alignment with the accepted culling floor, and active/inactive material channel placement.

## Source References

- Production package: `docs/assets/props/SM_INF_HornWingArch_A01/PRODUCTION_PACKAGE.md`
- Parent kit: `docs/assets/kits/KIT_INF_BalgorothCult_A01/PRODUCTION_PACKAGE.md`
- Kit breakdown: `docs/assets/kits/KIT_INF_BalgorothCult_A01/VISUAL_KIT_BREAKDOWN.md`
- Culling floor package: `docs/assets/props/SM_INF_CullingTrialFloor_A01/PRODUCTION_PACKAGE.md`
- Infernal cleanse standard: `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`
- Source concepts:
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Infernals Guarding a Gate.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Infernals Guarding a Gate2.png`

## Production Target

- Asset: `SM_INF_HornWingArch_A01`
- Type: Static Mesh modular gate/threshold prop.
- Clear opening: at least 360 cm high and 260 cm wide.
- Full arch target: 520-650 cm high, 430-560 cm wide, 120-220 cm deep.
- Unreal path: `/Game/Aerathea/Props/Infernals/BalgorothCult/`
- DCC state: first-pass DCC/Unreal review implementation complete and validated; final sculpt/UV/texture/tuned collision pass pending.

## Modeling Constraints

- Author at real scale in centimeters.
- Pivot at center-bottom of the clear opening.
- Central opening must stay clear for Exalted Infernals with folded wings and tail movement.
- Model major stone, horn, wing, skull/bone, brace, and plinth shapes.
- Use texture/normal maps for fine cracks, tiny symbols, small chips, ash smears, and minor scratches.
- Avoid tiny spike forests, dense chain clutter, random rivets, and unreadable micro-detail.
- Follow A03 visual cleanse guidance for source references.

## Blender Setup

- Collection: `SM_INF_HornWingArch_A01`
- Mesh groups:
  - `Arch_LeftUpright`
  - `Arch_RightUpright`
  - `Arch_CrownWingSpan`
  - `Arch_BasePlinth`
  - `Arch_ObsidianIron`
  - `Arch_BoneHornOrnaments`
  - `Arch_GlowChannels`
  - `UCX_Collision`
  - `Sockets`
- Optional modular split can be exported as separate meshes later if the assembled mesh proves too rigid.

## Modeling Sequence

1. Block the clear opening first: 360 cm high by 260 cm wide minimum.
2. Add two heavy basalt uprights and base plinths.
3. Add the split-wing upper span and horned crown crest.
4. Add hooked tail/claw side curves and large claw grooves.
5. Add major skull/bone ornaments at hierarchy points; keep them large and readable.
6. Add obsidian/iron braces and ember channel cuts.
7. Add sockets and UCX simple collision volumes.
8. Build LOD0-LOD3, preserving the opening, crown, wing silhouette, and glow blocks.
9. Export FBX and validate against `SM_INF_CullingTrialFloor_A01` snap position.

## Triangle Budget

- LOD0: 8k-16k tris.
- Hero variant ceiling: 22k tris only if approved.
- LOD1: 55-60 percent.
- LOD2: 25-35 percent.
- LOD3: 10-15 percent.

## Texture Deliverables

- `T_INF_HornWingArch_A01_BC`
- `T_INF_HornWingArch_A01_N`
- `T_INF_HornWingArch_A01_ORM`
- `T_INF_HornWingArch_A01_E`

Material instances:

- `MI_INF_HornWingArch_A01_CultStone`
- `MI_INF_HornWingArch_A01_ScorchedStone`
- `MI_INF_HornWingArch_A01_ObsidianIron`
- `MI_INF_HornWingArch_A01_BoneHorn`
- `MI_INF_HornWingArch_A01_BrandGlow`

## Collision Deliverables

- `UCX_SM_INF_HornWingArch_A01_00`: left upright/blocker.
- `UCX_SM_INF_HornWingArch_A01_01`: right upright/blocker.
- `UCX_SM_INF_HornWingArch_A01_02`: top span/blocker.
- Optional `UCX_SM_INF_HornWingArch_A01_03`: rear brace or blocked-state helper.
- No collision for small ornaments, chains, banners, or emissive grooves.

## Export Targets

- Blender source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01/SM_INF_HornWingArch_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01/SM_INF_HornWingArch_A01.fbx`
- Unreal static mesh: `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01`

## Unreal Validation

- Imports at centimeter scale with no import scaling.
- Clear opening supports 274 cm Infernal height plus horns/folded wings.
- Snaps cleanly to `SM_INF_CullingTrialFloor_A01` `snap_arch_front`.
- Collision does not snag player, Infernal wing, or tail movement.
- Required sockets exist:
  - `snap_floor`
  - `snap_altar`
  - `guard_l`
  - `guard_r`
  - `banner_l`
  - `banner_r`
  - `vfx_crown`
  - `vfx_eye`
  - `vfx_inner_throat`
  - `vfx_rejected_gap`

## DCC And Unreal Pass - 2026-06-28

- Built first-pass Blender source and FBX export using `Tools/DCC/build_infernal_horn_wing_arch.py`.
- Generated DCC review proof at `Saved/Automation/InfernalHornWingArchReview/SM_INF_HornWingArch_A01_DCCReview.png`.
- Imported to `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01` with `Tools/Unreal/import_infernal_horn_wing_arch.py`.
- Generated LOD0-LOD3 and assigned five blockout material instances: cult stone, scorched stone, obsidian iron, bone/horn, and brand glow.
- Added the required static mesh sockets for floor/altar snapping, guard placement, banners, crown/eye/throat VFX, and rejected-gap VFX.
- Startup review actor: `AET_PROD_INF_HornWingArch_A01`.
- Focused validator passed: `650.00h x 660.00w x 220.87d cm`, bounds radius `476.15 cm`, and `10` sockets.
- Startup validator passed with the arch added to expected assets, actors, LOD checks, socket checks, runtime visibility, and bounds.

## Acceptance Checklist

- Reads as Infernal/Balgoroth architecture at MMO camera distance.
- Is distinct from universal portals and common settlement gates.
- Opening, horn crown, split wing, skull/bone hierarchy, and ember channels remain readable through LODs.
- Uses simple collision and clear pivots/sockets.
- Final sculpt, authored UVs/textures, tuned collision, Blueprint gate behavior, and VFX states remain pending.
