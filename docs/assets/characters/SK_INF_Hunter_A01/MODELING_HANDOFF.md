# SK_INF_Hunter_A01 Modeling Handoff

## Purpose

Create the DCC source and pursuit/tracking gear for the Infernal Hunter overlay on `SK_INF_Base_A01`.

## Source References

- Production package: `docs/assets/characters/SK_INF_Hunter_A01/PRODUCTION_PACKAGE.md`
- Base package: `docs/assets/characters/SK_INF_Base_A01/PRODUCTION_PACKAGE.md`
- Animation handoff: `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`
- Combat VFX: `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/PRODUCTION_PACKAGE.md`
- Visual cleanse standard: `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`

## Production Target

- Asset: `SK_INF_Hunter_A01`
- Type: Skeletal Mesh class outfit.
- Fit targets: Standard and Greater Infernal body bands.
- Unreal path: `/Game/Aerathea/Characters/Infernals/Hunter/`
- DCC state: first-pass Blender source, FBX export, Unreal skeletal import, material instances, LOD0-LOD3, sockets, physics asset, ABP placeholder, startup actor, focused validation, and startup validation complete. Final sculpt/retopo/UVs/textures/animation remain pending.

## Modeling Constraints

- Keep hands free for claws; do not add bow/rifle/spear dependency.
- Preserve folded wing burst silhouette and tail balance.
- Model large readable pursuit armor, wing harness straps, claw guards, tail bands, and worthy-prey markers.
- Put small scars, brands, scratches, leather grain, and minor trophy wear in maps.

## Blender Setup

- Collection: `SK_INF_Hunter_A01`
- Mesh groups: `Base_Reference`, `Hunter_PursuitArmor`, `Hunter_WingHarness`, `Hunter_ClawGuards`, `Hunter_TailBands`, `Hunter_BoneHornMarkers`, `Hunter_GlowMarkers`

## Modeling Sequence

1. Load Standard/Greater base references.
2. Block pursuit silhouette with clear eye/brow, wing, tail, and hand reads.
3. Add light armor, wing harness, claw guards, tail bands, and major bone/horn markers.
4. Add socket markers for target mark, brow sight, pursuit burst, claws, tail, and wing roots.
5. Build LOD0-LOD3.
6. Export skeletal FBX.

## Triangle Budget

- Class gear LOD0: 10k-20k tris.
- Full equipped character: 38k-58k tris.
- LOD1: 55-60 percent.
- LOD2: 25-35 percent.
- LOD3: 10-15 percent.

## Texture Deliverables

- `T_INF_Hunter_A01_BC`
- `T_INF_Hunter_A01_N`
- `T_INF_Hunter_A01_ORM`
- `T_INF_Hunter_A01_E`

## Collision Deliverables

- Base capsule inherited.
- Outfit collision disabled.
- Wing/tail auxiliary bodies inherited and enabled only for authored windows.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Infernals/Hunter/SK_INF_Hunter_A01/SK_INF_Hunter_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Infernals/Hunter/SK_INF_Hunter_A01/SK_INF_Hunter_A01.fbx`
- DCC proof render: `Saved/Automation/InfernalHunterReview/SK_INF_Hunter_A01_DCCReview.png`
- Unreal mesh: `/Game/Aerathea/Characters/Infernals/Hunter/SK_INF_Hunter_A01`
- Shared skeleton: `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton`
- Physics asset: `/Game/Aerathea/Characters/Infernals/Hunter/PHYS_INF_Hunter_A01`
- Animation Blueprint: `/Game/Aerathea/Characters/Infernals/Hunter/ABP_INF_Hunter_A01`
- Startup actor: `AET_PROD_INF_Hunter_A01`

## Validated Runtime Sockets

- `hand_l_claw`
- `hand_r_claw`
- `hand_l_cast`
- `hand_r_cast`
- `vfx_hand_l`
- `vfx_hand_r`
- `vfx_eye_l`
- `vfx_eye_r`
- `vfx_brand_chest`
- `vfx_brand_forearm_l`
- `vfx_brand_forearm_r`
- `vfx_wing_root_l`
- `vfx_wing_root_r`
- `wing_l_tip`
- `wing_r_tip`
- `tail_tip`
- `vfx_tail_tip`
- `vfx_regen_core`
- `vfx_mouth`
- `vfx_target_mark`
- `vfx_brow_sight`
- `vfx_pursuit_burst`
- `pounce_trace`
- `claw_takedown_trace`
- `tail_balance_trace`
- `tracking_center`
- `wing_burst_trace`

## Unreal Validation

- Imports at centimeter scale.
- Binds to the tall Infernal base skeleton.
- Tracking, pounce, wing burst, and tail-balance poses remain readable.
- No modeled weapon dependency appears in the silhouette.
- Focused validator passed: visible height 235.63 cm, bounds radius 174.84 cm, 27 sockets.
- Startup validator passed: 198 assets, 54 expected actors, 25 ground tiles.

## Acceptance Checklist

- Hunter reads as a weaponless Infernal tracker.
- Invisible-sight and pursuit identity are readable.
- Gear clears pounce, leap, wing burst, and tail movement.
- Final sculpt, UVs, textures, skin weighting, physics, and animation remain pending.
