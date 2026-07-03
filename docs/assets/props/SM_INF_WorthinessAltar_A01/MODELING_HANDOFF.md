# SM_INF_WorthinessAltar_A01 Modeling Handoff

## Purpose

Create the DCC-ready Balgoroth cult worthiness altar that snaps to `SM_INF_CullingTrialFloor_A01`, anchors `VFX_INF_WorthinessJudgment_A01`, and feeds the implemented `BP_INF_RitualAltar_A01` wrapper.

The visual direction approval gate was cleared on 2026-06-28. First-pass DCC/Unreal build, Blueprint wrapping, and validation are complete; use this handoff for final sculpt/retopo, UV, texture, authored LOD, collision, and Blueprint-compatible final-art follow-up.

## Source References

- Production package: `docs/assets/props/SM_INF_WorthinessAltar_A01/PRODUCTION_PACKAGE.md`
- Parent kit: `docs/assets/kits/KIT_INF_BalgorothCult_A01/VISUAL_KIT_BREAKDOWN.md`
- Culling floor package: `docs/assets/props/SM_INF_CullingTrialFloor_A01/PRODUCTION_PACKAGE.md`
- Horn-wing arch package: `docs/assets/props/SM_INF_HornWingArch_A01/PRODUCTION_PACKAGE.md`
- Worthiness VFX package: `docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/PRODUCTION_PACKAGE.md`
- Brand material states: `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md`
- Infernal visual cleanse standard: `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`

## Production Target

| Component | Target | Notes |
| --- | --- | --- |
| Main altar body | 260-340w x 160-240d cm | heavy basalt/obsidian mass |
| Front interaction slab | 100-130 cm high | readable from player-facing side |
| Rear horned backplate | 240-340 cm high | main vertical silhouette |
| Central basin | 70-120 cm diameter | accepted/rejected VFX core |
| Split-wing side slabs | 140-220 cm wide span | broad readable side language |
| First-pass mesh | `SM_INF_WorthinessAltar_A01` | assembled prop for first review |

## Modeling Constraints

- Author at real scale in centimeters.
- Pivot at center-bottom on the floor snap alignment point.
- Front face points toward culling floor center.
- Keep front interaction access clear.
- Model large primary forms; fake small cracks, ash, scratches, micro-brands, and heat stress in textures/normal maps.
- Use Balgoroth symbols as graphic shapes, not readable text.
- No gore, body parts, tiny spike forests, dense hanging chains, or micro-rivet fields.

## Blender Setup

- Collection: `SM_INF_WorthinessAltar_A01`
- Mesh groups:
  - `Altar_BasePlinth`
  - `Altar_TopSlab`
  - `Altar_BackplateHornCrown`
  - `Altar_SplitWingSideSlabs`
  - `Altar_ObsidianBasin`
  - `Altar_BoneHornAccents`
  - `Altar_BrandGlowChannels`
  - `UCX_Collision`
  - `Sockets`

## Modeling Sequence

1. Block the footprint at 260-340 cm wide and 160-240 cm deep.
2. Align the pivot and forward orientation to the culling floor `snap_altar` use case.
3. Build the base plinth, top slab, and central basin.
4. Add the horned crown rear backplate and split-wing side slabs.
5. Add a broad broken-circle or claw-scratch rejection channel.
6. Add large bone/horn accents only at readable hierarchy points.
7. Add sockets for floor snapping, interaction, VFX core, sacrifice mark, brand transfer, ring link, and rejected gap.
8. Add simple UCX collision proxies.
9. Generate LOD0-LOD3 preserving the altar silhouette, backplate, basin, and glow blocks.
10. Export FBX and review beside a 180 cm humanoid, a Lesser Spawn, and a 274 cm Infernal.

## Triangle Budget

- LOD0: 6k-14k tris.
- LOD1: 55-60 percent.
- LOD2: 25-35 percent.
- LOD3: 10-15 percent.

## Texture Deliverables

- `T_INF_WorthinessAltar_A01_BC`
- `T_INF_WorthinessAltar_A01_N`
- `T_INF_WorthinessAltar_A01_ORM`
- `T_INF_WorthinessAltar_A01_E`

Material instances:

- `MI_INF_WorthinessAltar_A01_CultStone`
- `MI_INF_WorthinessAltar_A01_ScorchedStone`
- `MI_INF_WorthinessAltar_A01_ObsidianIron`
- `MI_INF_WorthinessAltar_A01_BoneHorn`
- `MI_INF_WorthinessAltar_A01_BrandGlow`

## Collision Deliverables

- `UCX_SM_INF_WorthinessAltar_A01_00`: base plinth.
- `UCX_SM_INF_WorthinessAltar_A01_01`: top slab.
- `UCX_SM_INF_WorthinessAltar_A01_02`: rear backplate.
- `UCX_SM_INF_WorthinessAltar_A01_03`: left wing slab.
- `UCX_SM_INF_WorthinessAltar_A01_04`: right wing slab.
- No collision for small ornaments, grooves, VFX channels, or fine cracks.

## Socket Deliverables

- `snap_floor`
- `snap_arch_back`
- `interact_front`
- `stage_offering`
- `vfx_altar_core`
- `vfx_sacrifice_mark`
- `vfx_brand_transfer`
- `vfx_ring_link`
- `vfx_rejected_gap`

## Export Targets

- Blender source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/SM_INF_WorthinessAltar_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/SM_INF_WorthinessAltar_A01.fbx`
- Unreal static mesh: `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01`

## Unreal Validation Targets

- Imports at centimeter scale with no import scaling.
- Snaps to `SM_INF_CullingTrialFloor_A01` without rotation mismatch.
- Material slots are assigned and named.
- LOD0-LOD3 exist.
- Required sockets exist.
- Collision does not block floor traversal, front interaction, wing clearance, or tail clearance.
- `BP_INF_RitualAltar_A01` binds to the mesh, sockets, `VFX_INF_WorthinessJudgment_A01`, and BrandGlow material states.

## First-Pass Build Results

- Blender source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/SM_INF_WorthinessAltar_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/SM_INF_WorthinessAltar_A01.fbx`
- DCC proof render: `Saved/Automation/InfernalWorthinessAltarReview/SM_INF_WorthinessAltar_A01_DCCReview.png`
- Unreal static mesh: `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01`
- Blueprint wrapper: `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01`
- Startup actor: `AET_PROD_INF_WorthinessAltar_A01`
- Material lanes: CultStone, ScorchedStone, ObsidianIron, BoneHorn, BrandGlow.
- Required sockets: complete, 9 total.
- Focused Blueprint validation: passed at `356.00h x 404.00w x 346.00d cm`, bounds radius `320.03 cm`, 9 components, 6 state materials, 6 Niagara systems.
- Mesh-level validation: passed at `356.00h x 404.00w x 346.00d cm`, bounds radius `320.03 cm`.
- Startup validation: passed with `233 assets`, `55 expected actors`, and `25 ground tiles`.

## Approval Gate

Cleared on 2026-06-28:

- Altar silhouette: low slab plus horned crown backplate.
- Footprint and height targets.
- Socket list.
- Material slot count.
- Central basin direction: ember bowl/obsidian sigil core for first pass.

## Acceptance Checklist

- Reads as Infernal/Balgoroth ritual altar at MMO camera distance.
- Snaps cleanly to the culling floor.
- Supports accepted/rejected VFX states without excessive particles.
- Avoids gore and over-detailed clutter.
- Exports with clear pivot, material slots, collision, sockets, and LOD targets.
