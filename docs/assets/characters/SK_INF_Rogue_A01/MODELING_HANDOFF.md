# SK_INF_Rogue_A01 Modeling Handoff

## Purpose

Create the DCC source and close-fit stealth gear for the Infernal Rogue overlay on `SK_INF_Base_A01`.

## Source References

- Production package: `docs/assets/characters/SK_INF_Rogue_A01/PRODUCTION_PACKAGE.md`
- Base package: `docs/assets/characters/SK_INF_Base_A01/PRODUCTION_PACKAGE.md`
- Animation handoff: `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`
- Visual cleanse standard: `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`

## Production Target

- Asset: `SK_INF_Rogue_A01`
- Type: Skeletal Mesh class outfit.
- Fit targets: Compact and Standard Infernal body bands.
- Unreal path: `/Game/Aerathea/Characters/Infernals/Rogue/`
- DCC state: not started.

## Modeling Constraints

- Keep hands free for claws; do not add dagger dependency.
- Preserve tight folded wings and tail counterbalance.
- Model large readable wraps, light plates, claw guards, wing anchors, tail-root guard, and collar/hood if approved.
- Put small stitches, cloth texture, tiny brands, and scratches in maps.

## Blender Setup

- Collection: `SK_INF_Rogue_A01`
- Mesh groups: `Base_Reference`, `Rogue_Wraps`, `Rogue_LightArmor`, `Rogue_ClawGuards`, `Rogue_WingAnchors`, `Rogue_TailGuard`, `Rogue_GlowMarkers`

## Modeling Sequence

1. Load Compact/Standard base references.
2. Block low-profile silhouette with folded wings and tail clearance.
3. Add wraps, light plates, claw guards, wing anchors, tail-root guard, and optional collar/hood.
4. Add socket markers for claw rake, pounce, invisible sight, tail balance, and ambush mark.
5. Build LOD0-LOD3.
6. Export skeletal FBX.

## Triangle Budget

- Class gear LOD0: 8k-18k tris.
- Full equipped character: 36k-54k tris.
- LOD1: 55-60 percent.
- LOD2: 25-35 percent.
- LOD3: 10-15 percent.

## Texture Deliverables

- `T_INF_Rogue_A01_BC`
- `T_INF_Rogue_A01_N`
- `T_INF_Rogue_A01_ORM`
- `T_INF_Rogue_A01_E`

## Collision Deliverables

- Base capsule inherited.
- Outfit collision disabled.
- Tail/wing auxiliary bodies inherited and enabled only for authored windows.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Infernals/Rogue/SK_INF_Rogue_A01/SK_INF_Rogue_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Infernals/Rogue/SK_INF_Rogue_A01/SK_INF_Rogue_A01.fbx`
- Unreal mesh: `/Game/Aerathea/Characters/Infernals/Rogue/SK_INF_Rogue_A01`

## Unreal Validation

- Imports at centimeter scale.
- Binds to final Infernal base skeleton.
- Crouch, stalk, pounce, rake, and tail-balance poses do not clip badly.
- Folded wings remain readable at review distance.

## Acceptance Checklist

- Rogue reads as a weaponless Infernal ambusher.
- Compact silhouette remains race-readable.
- Gear is clean for stealth/crouch animation.
- Final sculpt, UVs, textures, skin weighting, physics, and animation remain pending.
