# SM_INF_CullingTrialFloor_A01 Production Package

## Art Direction Summary

`SM_INF_CullingTrialFloor_A01` is the first modular static mesh target from `KIT_INF_BalgorothCult_A01`. It is a circular Infernal proving-floor module used for Lesser Infernal trials, adult worthiness tests, ritual combat, and Balgoroth cult encounter spaces.

The floor should communicate judgment and violence without gore: black basalt slabs, scorched red stone channels, a broken-circle ritual ring, claw-slash scoring marks, horned crown or split-wing sigil geometry, and restrained ember/violet emissive channels.

## Gameplay Purpose

The asset supports cult den interiors, ritual arenas, encounter staging, class training scenes, and future altar/Blueprint work. It is the right first DCC child because it validates scale, modular snapping, collision, material channels, symbol readability, and Infernal VFX color rules before more complex props are built.

## Silhouette Notes

- Circular or octagonal trial-floor read with large readable ring.
- Central sigil must be visible from gameplay camera distance.
- Use broad stone wedge modules, raised rim segments, and inset ritual channels.
- Symbol options: horned crown center, split-wing ring, claw-slash scoring at edges, broken-circle rejection gap.
- Avoid thin fragile spikes that snag characters or disappear at distance.

## Scale Notes

- Target assembled review diameter: 800-1000 cm.
- Center disc: 220-300 cm diameter, large enough for Spawn through Elder stage staging.
- Outer ring should support 9' / 274 cm Infernals with folded wings and tail sweeps.
- Module thickness: 20-45 cm visual depth, with flat collision on top.
- Pivot for the full assembled mesh: center-bottom at floor origin.

## Materials And Color Palette

- Basalt cult stone: black, blue-black, ash-gray worn edges.
- Scorched red stone: deep red-brown, burnt umber.
- Ritual channels: ember orange/deep red emissive, optional restrained violet rejected-state mask.
- Inset marks: obsidian black, blackened iron trims, bone/horn fragments only as large readable accents.
- Surface detail: claw grooves, heat cracks, ash stains, worn paths, broken-circle scratches.

## Concept Image Prompt

Create an original stylized fantasy MMORPG modular ritual floor concept image of `SM_INF_CullingTrialFloor_A01` for the Infernals of Aerathea. The design should emphasize Balgoroth cult judgment, culling temper, a circular proving arena floor, horned crown or split-wing center sigil, claw-slash scoring marks, broken-circle rejection gap, black basalt slabs, scorched red stone channels, obsidian insets, restrained ember and violet emissive grooves, and MMO-friendly modular construction. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and production-friendly geometry. Present it as a clean top-down and low-angle asset sheet with modular wedge callouts, material swatches, scale beside a 180 cm humanoid and 274 cm Infernal, and inactive/smoldering/active state notes. Avoid copied franchise designs, gore, excessive particles, readable text, watermarks, and photoreal micro-detail.

## Modeling Notes

- Build as a modular set or assembled review mesh with wedge, center disc, rim segment, and channel insert components.
- Model real geometry for raised rim, major cracks, large sigil insets, slab separation, and broad claw grooves.
- Use texture/normal maps for fine cracks, ash smears, tiny brands, heat stress lines, and micro chips.
- Keep the top collision flat enough for reliable movement and combat.
- Leave socket or locator positions for altar, VFX center, active channel ring, and stage markers.

## Texture And Material Notes

Texture targets:

- `T_INF_CullingTrialFloor_A01_BC`
- `T_INF_CullingTrialFloor_A01_N`
- `T_INF_CullingTrialFloor_A01_ORM`
- `T_INF_CullingTrialFloor_A01_E`

Material slots:

- Cult stone
- Scorched red stone or channel insets
- Obsidian/black iron accent
- Emissive ritual channels

Use 1K-2K textures for modular pieces. Use trim/atlas reuse where possible for future cult props.

## Triangle Budget

- Individual wedge module LOD0: 800-2k tris.
- Center disc LOD0: 1.5k-4k tris.
- Assembled review mesh LOD0: 8k-18k tris.
- Material slot target: 3-4.

## LOD Plan

- LOD0: full slab separation, large sigil geometry, raised rim, channel depth, major cracks.
- LOD1: 55-60 percent; reduce bevels, secondary cracks, small chips.
- LOD2: 25-35 percent; flatten channel bevels, simplify rim geometry, reduce sigil bevels.
- LOD3: 10-15 percent; preserve circular footprint, center symbol, red/black material read, and emissive ring blocks.

## Collision Notes

- Use simple flat top collision for gameplay.
- Raised rim can block if used as arena boundary; otherwise keep low enough to avoid movement snagging.
- Ritual grooves should not create collision holes.
- VFX and decoration sockets should be non-blocking.

## Animation Notes

- Static mesh is not animated.
- Material/VFX states should support inactive, smoldering, trial active, accepted, and rejected.
- Future Blueprint can drive channel glow, center sigil pulse, altar response, and audio hooks.

## Unreal Import Notes

- Asset type: Static Mesh.
- Asset name: `SM_INF_CullingTrialFloor_A01`.
- Folder path: `/Game/Aerathea/Props/Infernals/BalgorothCult/`.
- Pivot: center-bottom of assembled floor or center-bottom per wedge module.
- Scale: centimeters, no import scaling.
- Collision: simple authored collision or generated simple collision; do not use complex-as-simple for final gameplay.
- Sockets/locators:
  - `vfx_center`
  - `vfx_ring_active`
  - `vfx_rejected_gap`
  - `snap_altar`
  - `snap_arch_front`
  - `stage_spawn`
  - `stage_blooded`
  - `stage_elder`

## Folder And Naming Recommendation

- Package folder: `docs/assets/props/SM_INF_CullingTrialFloor_A01/`
- Blender source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01/SM_INF_CullingTrialFloor_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01/SM_INF_CullingTrialFloor_A01.fbx`
- Unreal mesh: `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01`
- Material instances:
  - `MI_INF_CullingTrialFloor_Inactive_A01`
  - `MI_INF_CullingTrialFloor_Smolder_A01`
  - `MI_INF_CullingTrialFloor_Active_A01`
  - `MI_INF_CullingTrialFloor_Rejected_A01`

## Quality Gate Checklist

- Reads as Balgoroth/Infernal cult kit, not common stone flooring.
- Supports culling trial and worthiness judgment without gore.
- Center symbol is readable from gameplay camera distance.
- Scale supports Spawn through 9' adult Infernal staging.
- Collision is simple and movement-safe.
- LODs, texture maps, material states, sockets, naming, and Unreal path are defined.
