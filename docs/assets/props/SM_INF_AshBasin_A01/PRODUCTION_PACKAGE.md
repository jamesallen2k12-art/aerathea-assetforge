# SM_INF_AshBasin_A01 Production Package

## Art Direction Summary

`SM_INF_AshBasin_A01` is a low-cost Balgoroth cult dressing prop for Infernal trial rooms, den interiors, altar sides, branding-stone staging, and regeneration rites. It should read as a heavy ash-and-ember vessel, not a generic brazier, campfire, or decorative bowl.

The design language is severe and functional: black basalt bowl mass, scorched red inner channels, claw-groove rim cuts, a small Balgoroth sigil inset, blackened iron support feet, ash accumulation, and restrained ember glow. Smoke and ember VFX are optional future hooks and must stay sparse.

## Gameplay Purpose

- Adds readable cult-room dressing around `SM_INF_WorthinessAltar_A01`, `SM_INF_BrandingStone_A01`, and Lesser trial spaces.
- Provides optional VFX sockets for low ash lift, ember motes, or regeneration staging cues.
- Supports environmental storytelling for culling trials, witness positions, and ritual cooldown states.
- Serves as a reusable prop in den, altar, gate, and proving-area layouts without requiring Blueprint behavior.

## Silhouette Notes

- Primary shape: squat heavy basin with a wide claw-cut rim and thick basalt body.
- Variant options:
  - small floor basin, 55-75 cm wide
  - large altar-side basin, 110-150 cm wide
  - wall-adjacent half-basin, 80-120 cm wide
- Readable features: horned rim points, claw-groove lip, ash mass, small sigil inset, blackened iron feet.
- Avoid delicate filigree, tiny dangling chains, thin spikes, dense little bones, or unreadable ash clutter.

## Scale Notes

- Small basin target: 65 cm wide x 42 cm high x 65 cm deep.
- Large basin target: 130 cm wide x 75 cm high x 130 cm deep.
- Keep rim height low enough for Spawn/Blooded Lesser staging but not toy-like beside adult Infernals.
- Leave enough clearance around the basin for wing, tail, and player capsule movement.

## Materials and Color Palette

- Outer stone: `MI_INF_CultStone_Basalt_A01`, black/ash-gray chipped stone.
- Inner heat channel: `MI_INF_CultStone_ScorchedRed_A01`, dark red-brown heat stress.
- Inset symbol: `MI_INF_BalgorothSigil_A01_Obsidian` or basalt relief.
- Metal supports: `MI_INF_CultStone_BlackIron_A01`, dark bronze edge wear.
- Ash fill: dark ash gray, smoke brown, low saturation.
- Ember accents: restrained ember orange/deep red, no constant flame column.

## Concept Image Prompt

Create an original stylized fantasy MMORPG static mesh concept sheet of `SM_INF_AshBasin_A01`, a Balgoroth cult ash basin for the Infernals of Aerathea. The design should emphasize a squat heavy black basalt basin, claw-cut rim, horned rim points, scorched red inner heat channels, ash fill, small Balgoroth sigil inset, blackened iron support feet, restrained ember glow, sparse ash motes, and reusable ritual-room dressing for worthiness altars, branding stones, den interiors, and culling trial spaces. Use hand-painted texture detail, readable broad shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly mid-poly production geometry. Present it as a static mesh production sheet with small, large, and wall-adjacent variants, top view, side profile, VFX socket callouts, material swatches, and scale beside a 180 cm humanoid and 274 cm Infernal. Apply A03-style cleanup if using Infernal source references: preserve major stone masses, skull/bone menace if used, flame/ember identity, claw grooves, brands, and villain threat while reducing tiny rivets, random speckle artifacts, malformed micro-spikes, broken micro-chains, dense smoke, and photoreal noise. Avoid copied franchise symbols, gore, readable text, watermarks, screen-filling fire, and universal portal styling.

## Modeling Notes

- Model the basin body, rim cuts, horned rim points, major sigil inset, thick feet, and large stone chips as real geometry.
- Use texture/normal maps for fine ash smears, tiny cracks, soot, heat stress, subtle rim scratches, and minor chips.
- Keep the ash fill as a simple interior form or material surface, not thousands of particles or stones.
- Build small and large variants from shared proportions if DCC later needs both.
- Do not add active flames as mesh geometry; use future VFX only if the placement requires it.

## Texture and Material Notes

Texture targets:

- `T_INF_AshBasin_A01_BC`
- `T_INF_AshBasin_A01_N`
- `T_INF_AshBasin_A01_ORM`
- `T_INF_AshBasin_A01_E`

Recommended material slots:

1. `MI_INF_CultStone_Basalt_A01`
2. `MI_INF_CultStone_ScorchedRed_A01`
3. `MI_INF_CultStone_BlackIron_A01`
4. `MI_INF_AshBasin_A01_AshFill`
5. `MI_INF_AshBasin_A01_Emissive`

State notes:

- Inactive: ash fill readable, no obvious flame.
- Smolder: faint ember flecks in ash surface.
- Trial active: low red-orange channel glow under the rim.
- Accepted: short warm ember lift.
- Rejected: brief violet-red ash kick only if driven by a ritual state.
- Cooldown: smoke/ash fades back to dark gray.

## Triangle Budget

- Small basin LOD0: 1k-2.5k tris.
- Large basin LOD0: 2.5k-5k tris.
- Wall-adjacent half-basin LOD0: 1.5k-3.5k tris.
- Material slots: 2-4 preferred, 5 maximum for hero placement.
- Texture set: 1K for small/normal use, 2K only for a hero altar-room basin.

## LOD Plan

- LOD0: full basin silhouette, horned rim points, claw grooves, feet, sigil inset, ash surface.
- LOD1: 55-60 percent; reduce small chips, rim bevel loops, foot detail.
- LOD2: 25-35 percent; flatten minor grooves, simplify ash surface, preserve rim and sigil silhouette.
- LOD3: 10-15 percent; preserve basin mass, rim block, and one ember color block only.

## Collision Notes

- Default collision: simple convex hull or box/rounded hull around the basin body.
- Non-blocking by default for small dressing placements unless used as a cover/obstacle prop.
- If blocking, keep collision below rim and away from decorative horn points to avoid snagging tails or wings.
- VFX sockets do not imply gameplay collision.

## Animation Notes

- Static mesh by default.
- Optional material-scalar pulse for smolder, trial active, accepted, rejected, and cooldown states.
- Optional future VFX sockets:
  - `vfx_ash_lift`
  - `vfx_ember_core`
  - `vfx_rejected_puff`
- No skeletal animation, moving parts, cloth, dynamic lights, or constant smoke simulation in this package.

## Unreal Import Notes

- Asset type: Static Mesh.
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/AshBasin/`
- Naming convention:
  - `SM_INF_AshBasin_Small_A01`
  - `SM_INF_AshBasin_Large_A01`
  - `SM_INF_AshBasin_Wall_A01`
  - `MI_INF_AshBasin_A01_AshFill`
  - `MI_INF_AshBasin_A01_Emissive`
  - `T_INF_AshBasin_A01_BC`
  - `T_INF_AshBasin_A01_N`
  - `T_INF_AshBasin_A01_ORM`
  - `T_INF_AshBasin_A01_E`
- Pivot: center bottom of the basin footprint.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Collision: simple authored collision or generated convex collision.
- LODs: LOD0-LOD3 required for placed mesh variants.
- Socket plan:
  - `vfx_ash_lift`
  - `vfx_ember_core`
  - `vfx_rejected_puff`
  - `snap_floor_center`

## Folder and Naming Recommendation

- Package folder: `docs/assets/props/SM_INF_AshBasin_A01/`
- Related kit: `docs/assets/kits/KIT_INF_BalgorothCult_A01/`
- Related material package: `docs/assets/materials/MI_INF_CultStone_Set_A01/`
- Related symbol package: `docs/assets/props/SM_INF_BalgorothSigil_A01/`
- Source folder: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_AshBasin_A01/`
- Export folder: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_AshBasin_A01/`
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/AshBasin/`

## Quality Gate Checklist

- Reads as Balgoroth cult ash/ember dressing, not a generic brazier or campfire.
- Basin mass, claw rim, sigil inset, ash fill, and ember core are readable at MMO camera distance.
- Materials follow `MI_INF_CultStone_Set_A01` and `SM_INF_BalgorothSigil_A01`.
- Glow and future VFX stay sparse and state-driven.
- Major forms are geometry; ash smears, soot, heat stress, and tiny chips stay in maps.
- Triangle budget, material slots, texture targets, LOD0-LOD3, collision, pivot, sockets, and Unreal path are defined.
- No Niagara assets, Blueprint behavior, dynamic lights, constant smoke, gore, readable text, or copied symbols are claimed by this package.
