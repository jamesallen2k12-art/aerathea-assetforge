# SK_INF_Warrior_A01 Modeling Handoff

## Purpose

Create the DCC source and class gear for the Infernal Warrior overlay on `SK_INF_Base_A01`.

## Source References

- Production package: `docs/assets/characters/SK_INF_Warrior_A01/PRODUCTION_PACKAGE.md`
- Base package: `docs/assets/characters/SK_INF_Base_A01/PRODUCTION_PACKAGE.md`
- Animation handoff: `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`
- Visual cleanse standard: `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`

## Production Target

- Asset: `SK_INF_Warrior_A01`
- Type: Skeletal Mesh class outfit.
- Fit targets: Standard, Greater, and Exalted Infernal body bands.
- Unreal path: `/Game/Aerathea/Characters/Infernals/Warrior/`
- DCC state: not started.

## Modeling Constraints

- Keep hands free for claws; do not add primary weapons.
- Preserve folded wings, thick tail, and black claw readability.
- Model large armor plates, bracers, wing-root guards, tail-root guard, skull belt, and major bone ornaments.
- Put tiny rivets, scratches, leather grain, scar detail, and minor bone chips in textures.

## Blender Setup

- Collection: `SK_INF_Warrior_A01`
- Mesh groups: `Base_Reference`, `Warrior_Armor`, `Warrior_Bracers`, `Warrior_WingGuards`, `Warrior_TailGuard`, `Warrior_BoneSkull`, `Warrior_GlowMarkers`

## Modeling Sequence

1. Load `SK_INF_Base_A01` Standard/Greater/Exalted references.
2. Block armor silhouette around claw, wing, and tail clearance.
3. Add bracers, chest plate, greaves, wing-root guards, tail-root armor, and skull belt.
4. Add socket markers for claw traces, tail sweep, wing buffet, rage core, and regeneration.
5. Build LOD0-LOD3.
6. Export skeletal FBX.

## Triangle Budget

- Class gear LOD0: 14k-26k tris.
- Full equipped character: 44k-64k tris.
- LOD1: 55-60 percent.
- LOD2: 25-35 percent.
- LOD3: 10-15 percent.

## Texture Deliverables

- `T_INF_Warrior_A01_BC`
- `T_INF_Warrior_A01_N`
- `T_INF_Warrior_A01_ORM`
- `T_INF_Warrior_A01_E`

## Collision Deliverables

- Base capsule inherited.
- Outfit collision disabled.
- Optional simplified bodies for boss wing guards or tail-root armor only.
- Claw/tail gameplay uses sockets and traces.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Infernals/Warrior/SK_INF_Warrior_A01/SK_INF_Warrior_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Infernals/Warrior/SK_INF_Warrior_A01/SK_INF_Warrior_A01.fbx`
- Unreal mesh: `/Game/Aerathea/Characters/Infernals/Warrior/SK_INF_Warrior_A01`

## Unreal Validation

- Imports at centimeter scale.
- Binds to the final Infernal base skeleton.
- Claws, wings, tail, skull belt, and armor blocks read at review distance.
- Clears claw combo, tail sweep, wing buffet, pounce, and hit-react poses.

## Acceptance Checklist

- Warrior reads as a weaponless natural-weapon Infernal.
- Race silhouette stays dominant over armor.
- LODs preserve claw, wing, tail, horn, and skull-belt reads.
- Final sculpt, UVs, textures, skin weighting, physics, and animation remain pending.
