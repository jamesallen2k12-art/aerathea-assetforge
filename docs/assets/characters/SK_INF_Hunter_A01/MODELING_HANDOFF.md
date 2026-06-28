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
- DCC state: not started.

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
- Unreal mesh: `/Game/Aerathea/Characters/Infernals/Hunter/SK_INF_Hunter_A01`

## Unreal Validation

- Imports at centimeter scale.
- Binds to final Infernal base skeleton.
- Tracking, pounce, wing burst, and tail-balance poses remain readable.
- No modeled weapon dependency appears in the silhouette.

## Acceptance Checklist

- Hunter reads as a weaponless Infernal tracker.
- Invisible-sight and pursuit identity are readable.
- Gear clears pounce, leap, wing burst, and tail movement.
- Final sculpt, UVs, textures, skin weighting, physics, and animation remain pending.
