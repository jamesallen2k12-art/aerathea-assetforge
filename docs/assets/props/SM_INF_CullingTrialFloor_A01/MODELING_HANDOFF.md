# SM_INF_CullingTrialFloor_A01 Modeling Handoff

## Purpose

Create the first DCC-ready Balgoroth cult static mesh: a modular Infernal culling trial floor that validates symbol readability, material states, collision, snap rules, and scale for the broader cult kit.

## Source References

- Kit package: `docs/assets/kits/KIT_INF_BalgorothCult_A01/PRODUCTION_PACKAGE.md`
- Kit breakdown: `docs/assets/kits/KIT_INF_BalgorothCult_A01/VISUAL_KIT_BREAKDOWN.md`
- Prop package: `docs/assets/props/SM_INF_CullingTrialFloor_A01/PRODUCTION_PACKAGE.md`
- Infernal visual rules: `docs/assets/characters/SK_INF_Base_A01/VISUAL_RULES.md`

## Production Target

| Component | Target | Notes |
| --- | --- | --- |
| Center disc | 220-300 cm diameter | horned crown or split-wing sigil |
| Wedge module | 45 or 60 degree wedge | snap-friendly ring construction |
| Outer rim | 800-1000 cm assembled diameter | optional arena boundary |
| Channel insert | follows ring/sigil | emissive material slot |
| Assembled review mesh | `SM_INF_CullingTrialFloor_A01` | single export acceptable for first pass |

## Modeling Constraints

- Author in centimeters.
- Pivot at center-bottom for assembled mesh, or center-bottom per modular wedge.
- Top walking surface must be flat enough for reliable gameplay collision.
- Use large readable symbol shapes instead of text glyphs.
- Keep raised rim and channel depths visually strong but movement-safe.
- Do not add gore, body parts, or cluttered micro-detail.

## Modeling Sequence

1. Block assembled 800-1000 cm circular or octagonal floor at real scale.
2. Split design into center disc, outer ring wedges, rim, and emissive channel forms.
3. Add horned crown or split-wing central sigil using broad inset geometry.
4. Add broken-circle gap and claw-slash scoring marks around the ring.
5. Add simple socket locators for VFX center, active ring, rejected gap, altar snap, arch snap, and stage positions.
6. Create simple collision proxy or collision-ready geometry for flat top traversal.
7. Export FBX and review beside 180 cm humanoid and 274 cm Infernal scale markers.

## Triangle Budget

- Assembled LOD0: 8k-18k tris.
- LOD1: 55-60 percent.
- LOD2: 25-35 percent.
- LOD3: 10-15 percent.

## Texture Deliverables

- `T_INF_CullingTrialFloor_A01_BC`
- `T_INF_CullingTrialFloor_A01_N`
- `T_INF_CullingTrialFloor_A01_ORM`
- `T_INF_CullingTrialFloor_A01_E`

Material slots:

- Cult stone
- Scorched red stone/channel
- Obsidian or black iron accent
- Emissive ritual channel

## Collision Deliverables

- Flat simple top collision.
- Optional low rim collision if the rim is meant to define arena boundary.
- No collision inside visual channel grooves.
- VFX and stage sockets are non-blocking.

## Export Targets

- Blender source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01/SM_INF_CullingTrialFloor_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01/SM_INF_CullingTrialFloor_A01.fbx`
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/`

## Unreal Validation

- Imports at centimeter scale.
- LOD0-LOD3 generated or authored.
- Simple collision allows smooth walking and tail/wing clearance.
- Material slots are assigned and named.
- Required sockets or locator equivalents exist: `vfx_center`, `vfx_ring_active`, `vfx_rejected_gap`, `snap_altar`, `snap_arch_front`, `stage_spawn`, `stage_blooded`, `stage_elder`.

## Acceptance Checklist

- Reads as Infernal/Balgoroth trial floor at MMO camera distance.
- Supports Spawn through Exalted adult scale.
- Visual channels and symbols remain readable without excess glow.
- Collision is movement-safe.
- Export paths, naming, LODs, textures, sockets, and material slots are ready for DCC work.
