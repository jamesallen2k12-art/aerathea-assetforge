# SM_INF_TrialBanner_A01 Production Package

## Art Direction Summary

`SM_INF_TrialBanner_A01` is the Balgoroth cult vertical banner/marker prop for trial rooms, gate approaches, Lesser dens, altar walls, and faction-readable encounter dressing. It should read as an Infernal cult banner from MMO camera distance without relying on readable text.

The static-first design uses ash cloth, blood-dark red trim, blackened iron or bone/horn hanging rods, broad Balgoroth sigil print/relief, scorch-worn lower cuts, and restrained ember stitch accents. Cloth animation, skeletal cloth variants, and final banner symbol changes are not part of this package.

## Gameplay Purpose

- Adds faction-readable vertical dressing to Balgoroth cult spaces.
- Provides clear visual markers for trial entrances, witness areas, altar rooms, and den staging.
- Reuses `SM_INF_BalgorothSigil_A01` symbol language to prevent banner variants from drifting.
- Can later support static placement, socketed hanging, or optional cloth animation after approval.

## Silhouette Notes

- Primary shape: tall narrow vertical banner with a heavy top rod and broad lower tear shape.
- Variant options:
  - wall-hung vertical banner
  - freestanding pole banner
  - short altar-side pennant
  - torn trial marker strip
- Main read must be the banner rectangle/tear silhouette plus one large Balgoroth symbol.
- Avoid tiny glyph fields, dense fringe, many small dangling charms, unreadable script, or micro-tears.

## Scale Notes

- Wall banner: 90-140 cm wide x 220-360 cm tall.
- Pole banner: 70-110 cm wide x 260-420 cm tall including rod/pole.
- Pennant: 40-70 cm wide x 90-160 cm tall.
- Height should read beside a 180 cm humanoid and remain imposing near a 274 cm Infernal without clipping low ceilings.

## Materials and Color Palette

- Cloth: `MI_INF_CultStone_AshCloth_A01`, black/ash gray with blood-dark red trim.
- Symbol print/relief: Balgoroth horned crown, split wing, claw slash, ember eye, or broken circle from `SM_INF_BalgorothSigil_A01`.
- Hanging rod/pole: blackened iron or smoke-stained bone/horn.
- Edge wear: ash-gray fray, scorched red-brown burns, low saturation.
- Emissive: tiny ember stitch or sigil pips only; no glowing cloth sheet.

## Concept Image Prompt

Create an original stylized fantasy MMORPG static mesh concept sheet of `SM_INF_TrialBanner_A01`, a Balgoroth cult trial banner for the Infernals of Aerathea. The design should emphasize ash-black cloth, blood-dark red trim, a large readable Balgoroth sigil print using horned crown, split wing, claw slash, ember eye, or broken-circle motifs, blackened iron or smoke-stained bone hanging rods, scorched lower cuts, restrained ember stitch accents, and vertical faction-readable dressing for trial rooms, altar walls, gate approaches, and Lesser dens. Use hand-painted texture detail, readable broad shapes, baked-AO-style depth, normal-map-style cloth weave and wear, sparing emissive accents, and MMO-friendly mid-poly production geometry. Present it as a static mesh production sheet with wall-hung banner, pole banner, altar pennant, and torn trial marker variants, plus symbol callouts, material swatches, pivot notes, and scale beside a 180 cm humanoid and 274 cm Infernal. Apply A03-style cleanup if using Infernal source references: preserve large banner shape, Balgoroth symbol, ash cloth, horns, wings, claws, brands, flame/ember identity, and villain threat while reducing tiny rivets, random speckles, malformed micro-spikes, excessive dangling charms, unreadable script, dense fringe, and photoreal noise. Avoid copied franchise symbols, gore, readable text, watermarks, full-cloth neon glow, and cloth simulation requirements.

## Modeling Notes

- Model the banner sheet as simple static cloth geometry with a few broad folds and tears.
- Model hanging rods, pole caps, large bone/horn end caps, and major symbol relief if using raised variants.
- Use texture/normal maps for cloth weave, soot, ash wear, tiny stitches, frayed fibers, and minor scorch marks.
- Build variants from one shared cloth silhouette family rather than separate unrelated banners.
- Do not create skeletal cloth, real-time cloth simulation, or animated wind behavior in this package.

## Texture and Material Notes

Texture targets:

- `T_INF_TrialBanner_A01_BC`
- `T_INF_TrialBanner_A01_N`
- `T_INF_TrialBanner_A01_ORM`
- `T_INF_TrialBanner_A01_E`

Recommended material slots:

1. `MI_INF_CultStone_AshCloth_A01`
2. `MI_INF_CultStone_BlackIron_A01` or `MI_INF_CultStone_BoneHorn_A01`
3. `MI_INF_TrialBanner_A01_SigilPrint`
4. `MI_INF_TrialBanner_A01_Emissive`

Material rules:

- Use one large symbol per banner face.
- Keep emissive stitches sparse and mostly inactive.
- Rejection/curse variants may use short violet-red accents on a broken-circle print only after state approval.

## Triangle Budget

- Wall banner LOD0: 800-2k tris.
- Pole banner LOD0: 1.2k-3k tris.
- Altar pennant LOD0: 500-1.2k tris.
- Torn trial marker LOD0: 400-1k tris.
- Hero grouped banner set: 4k-7k tris maximum.
- Material slots: 2-4 maximum.

## LOD Plan

- LOD0: full cloth silhouette, broad folds, rod/pole, symbol print/relief, major tears.
- LOD1: 55-60 percent; reduce fold loops, small tear bevels, end-cap detail.
- LOD2: 25-35 percent; flatten cloth folds, preserve overall banner and symbol silhouette.
- LOD3: 10-15 percent; preserve banner rectangle/tear block and one broad symbol color block.

## Collision Notes

- No collision by default for hanging cloth variants.
- Pole/freestanding variants may use one simple capsule/box around the pole only.
- Do not use cloth surface collision unless a future gameplay task requires it.
- Keep collision clear of wing/tail paths and player capsules.

## Animation Notes

- Static mesh by default.
- Optional future sockets:
  - `snap_wall_hanger`
  - `snap_pole_base`
  - `vfx_sigil_ember`
  - `vfx_rejected_thread`
- Skeletal cloth, wind sway, tear animation, and state-driven cloth motion are approval-gated future tasks.
- Material-only emissive pulse is allowed later if state-driven and restrained.

## Unreal Import Notes

- Asset type: Static Mesh set.
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/TrialBanner/`
- Naming convention:
  - `SM_INF_TrialBanner_Wall_A01`
  - `SM_INF_TrialBanner_Pole_A01`
  - `SM_INF_TrialBanner_Pennant_A01`
  - `SM_INF_TrialBanner_TornMarker_A01`
  - `MI_INF_TrialBanner_A01_SigilPrint`
  - `MI_INF_TrialBanner_A01_Emissive`
  - `T_INF_TrialBanner_A01_BC`
  - `T_INF_TrialBanner_A01_N`
  - `T_INF_TrialBanner_A01_ORM`
  - `T_INF_TrialBanner_A01_E`
- Pivot:
  - wall banner at top-center hanging point
  - pole banner at pole base
  - pennant at top-center hanging point
  - torn marker at center top
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Collision: none or simple pole collision only.
- LODs: LOD0-LOD3 required for placed variants.

## Folder and Naming Recommendation

- Package folder: `docs/assets/props/SM_INF_TrialBanner_A01/`
- Related kit: `docs/assets/kits/KIT_INF_BalgorothCult_A01/`
- Related symbol package: `docs/assets/props/SM_INF_BalgorothSigil_A01/`
- Related material package: `docs/assets/materials/MI_INF_CultStone_Set_A01/`
- Source folder: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_TrialBanner_A01/`
- Export folder: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_TrialBanner_A01/`
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/TrialBanner/`

## Quality Gate Checklist

- Banner reads as Balgoroth cult dressing, not generic medieval cloth.
- One large Balgoroth symbol is readable without text.
- Materials follow `MI_INF_CultStone_Set_A01` and `SM_INF_BalgorothSigil_A01`.
- Cloth folds, rod/pole, and major tears are geometry; weave, soot, fray, and stitches stay in maps.
- No skeletal cloth, simulation, readable script, gore, copied symbols, or all-over glow is claimed.
- Triangle budget, material slots, texture targets, LOD0-LOD3, collision, pivots, sockets, and Unreal paths are defined.
