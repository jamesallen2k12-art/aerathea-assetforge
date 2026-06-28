# SM_INF_HornWingArch_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_INF_HornWingArch_A01`
- Asset type: Static Mesh modular gate/threshold prop
- Parent kit: `KIT_INF_BalgorothCult_A01`
- World: Aerathea
- Theme: Balgoroth cult threshold, horned-wing ritual arch, Infernal gate marker
- Primary source references: `Infernals Guarding a Gate.png`, `Infernals Guarding a Gate2.png`, `SM_INF_CullingTrialFloor_A01`, `KIT_INF_BalgorothCult_A01`
- Current status: production package and modeling handoff ready; DCC build not started

`SM_INF_HornWingArch_A01` is the first gate/threshold child for the Balgoroth cult kit. It should feel old, predatory, judgmental, and ceremonial: a tall black-basalt arch whose silhouette combines horned crown, split wings, hooked tail curves, claw grooves, obsidian insets, bone/horn ornaments, and ember-red brand channels. It is not a universal travel portal. It is an Infernal cult threshold used for dens, proving arenas, altar rooms, and guarded Balgoroth spaces.

## 2. Gameplay Purpose

- Provides a reusable Infernal cult doorway/threshold for trial rooms, gate-guard scenes, Lesser training dens, and mage/cult encounters.
- Defines how `Infernals Guarding a Gate*.png` routes into production without copying noisy background detail.
- Snaps to `SM_INF_CullingTrialFloor_A01` through the `snap_arch_front` socket.
- Establishes clearance rules for horns, folded wings, tail sweeps, guards, and combat movement.
- Supports future `BP_INF_CultGate_A01` behavior if locked/active/passive gate states are approved.

## 3. Silhouette Notes

- Primary silhouette: two heavy basalt uprights, split-wing upper span, horned crown crest, and hooked tail/claw side curves.
- The arch should read as Balgoroth cult architecture from a distance, not a common stone doorway.
- Use broad wing-blade shapes and large horn points; avoid forests of tiny spikes.
- Place major skull/bone ornaments at readable hierarchy points, such as crown center, side braces, or guard sockets.
- Include claw grooves and broken-circle marks as carved or inset graphic forms, not readable text.
- Keep the central opening clear and visibly usable by winged/tail characters.

## 4. Scale Notes

- Clear opening target: at least 360 cm high and 260 cm wide for 274 cm Exalted Infernals plus horns and folded wings.
- Full arch height target: 520-650 cm.
- Full arch width target: 430-560 cm.
- Depth target: 120-220 cm, enough to feel massive without creating navigation problems.
- Step/rim height should stay under movement-snag thresholds unless authored as a deliberate blocker.
- Pivots: center-bottom for standalone placement; optional snap points for floor/ring alignment.

## 5. Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Cult basalt | black, blue-black, ash-gray edge wear | main uprights, arch mass, wing stones |
| Scorched red stone | dark red, burnt umber, heat-worn edges | insets, inner throat, channel slabs |
| Obsidian | near-black, sharp gray highlights | symbol inlays, eye/crown pieces |
| Blackened iron | charcoal metal, dark bronze wear | braces, hinge-like clamps, guard brackets |
| Bone and horn | aged ivory, smoke-stained tan | major skull/bone ornaments, horn trophies |
| Emissive channels | ember orange, deep red, focused violet rejection marks | brands, eye motif, active state channels |

Glow should be localized to channels, eye motifs, and active gate states. The stone mass stays readable in normal lighting.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG static mesh concept sheet of `SM_INF_HornWingArch_A01`, a Balgoroth cult horn-wing arch for the Infernals of Aerathea. The design should emphasize an old predatory Infernal threshold, black basalt uprights, split-wing upper span, horned crown crest, hooked tail side curves, claw-groove marks, obsidian insets, major skull and bone ornaments, scorched red stone channels, focused ember and violet brand glow, guarded cult gate identity, and clearance for 9-foot winged Infernals with folded wings and thick tails. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, focused emissive accents, and MMO-friendly production geometry. Present it as a static mesh production sheet with front view, side depth view, top footprint, snap socket callouts, collision blocks, inactive/smolder/active material states, material swatches, and scale beside a 180 cm humanoid and 274 cm Infernal. Apply A03-style cleanup if using source references: preserve skulls, flame, glowing marks, menace, and villain threat while removing tiny repeated rivets, random speckle artifacts, malformed micro-spikes, broken micro-chains, and unreadable background clutter. Avoid copied franchise designs, gore, excessive particles, readable text, watermarks, and universal portal styling.

## 7. Modeling Notes

- Build as a modular static mesh with optional left upright, right upright, crown span, rear brace, and base plinth pieces.
- Model real geometry for the main stone masses, wing span, horn crown, major skull/bone ornaments, large iron braces, broad claw grooves, and snap plinth.
- Use texture/normal maps for fine cracks, ash smears, small scratches, heat stress, small chips, and tiny symbol wear.
- Keep opening collision simple and clear.
- Avoid tiny spike forests, dangling micro-chains, or per-rivet geometry.
- Include sockets for guard placement, VFX channels, banners, and snap alignment.

## 8. Texture And Material Notes

Texture targets:

- `T_INF_HornWingArch_A01_BC`
- `T_INF_HornWingArch_A01_N`
- `T_INF_HornWingArch_A01_ORM`
- `T_INF_HornWingArch_A01_E`

Material slots:

1. `MI_INF_HornWingArch_A01_CultStone`
2. `MI_INF_HornWingArch_A01_ScorchedStone`
3. `MI_INF_HornWingArch_A01_ObsidianIron`
4. `MI_INF_HornWingArch_A01_BoneHorn`
5. Optional `MI_INF_HornWingArch_A01_BrandGlow`

Reuse `T_INF_CultStone_A01_*`, `T_INF_BlackIron_A01_*`, `T_INF_ObsidianBone_A01_*`, and `T_INF_BrandGlow_A01_E` where practical.

## 9. Triangle Budget

- LOD0 target: 8k-16k tris for the assembled arch.
- Hero/raid-room variant: up to 22k tris if crown/wing silhouette needs extra mass.
- Material slot target: 4-5.

Geometry priority goes to arch silhouette, wing span, horn crown, opening clearance, major skull/bone ornaments, and large stone breaks. Fine cracks and small ornaments stay in maps.

## 10. LOD Plan

- LOD0: full arch mass, horn crown, split-wing span, skull/bone ornaments, braces, broad claw grooves, emissive channel geometry.
- LOD1: reduce bevels, secondary cracks, small brace geometry, and small ornaments.
- LOD2: simplify wing span cuts, merge ornament clusters, flatten minor grooves, reduce underside detail.
- LOD3: preserve main arch outline, horn crown, wing silhouette, clear opening, skull/bone mass, and glow blocks.

Never reduce the opening, horn crown, split-wing silhouette, or readable Balgoroth symbol before small surface detail.

## 11. Collision Notes

- Use simple collision volumes for left upright, right upright, top span, and optional rear brace.
- Keep the central opening passable unless a locked-state Blueprint intentionally blocks it.
- Do not use complex-as-simple for final gameplay.
- Small skulls, chains, banners, and ornaments should be non-blocking.
- Validate wing/tail character movement against the arch after final collision tuning.

## 12. Animation Notes

- Static mesh is not animated by default.
- Optional future states:
  - Inactive: no channel pulse.
  - Smolder: low ember channels.
  - Active threshold: eye/crown and inner throat channel pulse.
  - Rejected/unworthy: short violet-red broken-circle snap.
  - Locked: blackened iron/branded barrier VFX from future Blueprint.
- Optional hanging banners can become separate skeletal/static cloth assets later.

## 13. Unreal Import Notes

- Asset type: Static Mesh.
- Primary mesh: `SM_INF_HornWingArch_A01`.
- Folder path: `/Game/Aerathea/Props/Infernals/BalgorothCult/`.
- Pivot: center-bottom of the clear opening.
- Scale: centimeters, no import scaling.
- Collision: authored UCX simple volumes or generated simple collision.
- Material slot count: 4-5.
- Suggested sockets:
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

## 14. Folder And Naming Recommendation

- Package folder: `docs/assets/props/SM_INF_HornWingArch_A01/`
- Source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01/`
- Export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01/`
- Unreal: `/Game/Aerathea/Props/Infernals/BalgorothCult/`
- Materials: `MI_INF_HornWingArch_A01_*`
- Textures: `T_INF_HornWingArch_A01_*`

Related follow-up assets:

- `SM_INF_WorthinessAltar_A01`
- `SM_INF_TrialBanner_A01`
- `SM_INF_WitnessChains_A01`
- `BP_INF_CultGate_A01`

## 15. Quality Gate Checklist

- Reads as a Balgoroth cult threshold, not a common arch or universal portal.
- Clear opening supports 274 cm Infernals with horns, folded wings, and tail movement.
- Horned crown, split wing, claw grooves, skull/bone hierarchy, and ember channels are readable.
- Major forms are real geometry; tiny cracks, rivets, scratches, and micro-symbols stay in maps.
- LOD, collision, texture maps, sockets, pivots, material slots, and Unreal paths are included.
