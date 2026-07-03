# SM_INF_BalgorothSigil_A01 Production Package

## Art Direction Summary

`SM_INF_BalgorothSigil_A01` is the reusable symbol kit for Balgoroth cult props and spaces. It locks the horned crown, split wing, hooked tail crescent, claw slash, ember eye, and broken-circle marks before banners, branding stones, ash basins, witness chains, gates, floors, altar insets, and den dressing create divergent symbol variants.

The symbols must feel severe, predatory, hierarchical, and judgmental without becoming gore marks or readable text glyphs.

## Gameplay Purpose

- Provides readable faction and ritual-state identity across Infernal cult environments.
- Supports trial success, rejection, invisible sight, bloodline hierarchy, and worthiness judgment storytelling.
- Gives DCC, material, VFX, UI, and quest teams one approved symbol standard to reuse.

## Silhouette Notes

Primary symbol shapes:

- Horned crown: 3-5 horn points with a taller center horn.
- Split wing: two severe wing blades divided by a central mark.
- Hooked tail crescent: crescent ending in claw/tail hook.
- Claw slash: three large black cuts or raised grooves.
- Ember eye: angular eye with a small ember core.
- Broken circle: incomplete ritual ring for rejection/unworthy state.

Each symbol must read at MMO camera distance as a graphic silhouette. No tiny rune clusters, unreadable text strokes, or decorative micro-spikes.

## Scale Notes

Package variants:

- Wall relief: 180-320 cm wide.
- Floor insert: 220-420 cm diameter.
- Altar inset: 40-120 cm wide.
- Banner/decal source: scalable 1:1 reference, no readable text.
- UI/reference mark: flattened design guide only, not a UI implementation task.

## Materials And Color Palette

- Basalt relief: black/ash stone using `MI_INF_CultStone_Basalt_A01`.
- Scorched inset: dark red stone using `MI_INF_CultStone_ScorchedRed_A01`.
- Obsidian inlay: near-black glossy highlights using `MI_INF_CultStone_ObsidianInset_A01`.
- Emissive channels: restrained ember/deep red, violet only for rejection.
- Optional bone/horn trim for large hero altar/wall variants only.

## Concept Image Prompt

Create an original stylized fantasy MMORPG symbol kit concept sheet of `SM_INF_BalgorothSigil_A01` for the Infernals of Aerathea. The design should emphasize a horned crown authority mark, split wing bloodline mark, hooked tail crescent hunt mark, three-claw culling slash, angular ember eye judgment mark, broken-circle rejection mark, black basalt relief, scorched red insets, obsidian grooves, smoke-stained bone accents, restrained ember glow, and MMO-readable graphic silhouettes. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and production-friendly mid-poly design. Present it as a clean symbol/relief board with wall relief, floor insert, altar inset, banner print reference, and material callouts. Avoid copied franchise symbols, gore, readable text, watermarks, photoreal over-detail, and dense micro-runes.

## Modeling Notes

- Build wall/floor/altar variants from shared source shapes.
- Model real geometry for large raised relief edges, major grooves, horn points, wing blades, crescent hooks, and deep claw cuts.
- Use texture/normal maps for shallow scratches, small chips, ash stains, fine bevel wear, and minor heat cracks.
- Keep relief bevels broad enough to survive LOD reduction.
- Do not create separate packages for every symbol; this is the shared symbol source.

## Texture And Material Notes

Texture targets:

- `T_INF_BalgorothSigil_A01_BC`
- `T_INF_BalgorothSigil_A01_N`
- `T_INF_BalgorothSigil_A01_ORM`
- `T_INF_BalgorothSigil_A01_E`

Material instances:

- `MI_INF_BalgorothSigil_A01_Basalt`
- `MI_INF_BalgorothSigil_A01_ScorchedInset`
- `MI_INF_BalgorothSigil_A01_Obsidian`
- `MI_INF_BalgorothSigil_A01_Emissive`

Material rules:

- Use `MI_INF_CultStone_Set_A01` language where practical.
- Emissive should appear in channels, eye cores, and active ritual insets only.
- Rejection variants may use short violet-red accents but not constant violet glow.

## Triangle Budget

- Altar inset or small relief: 500-1.5k tris.
- Wall relief: 1.5k-4k tris.
- Floor insert: 2k-6k tris depending channel depth.
- Hero assembled symbol cluster: 6k-10k tris maximum, only if it replaces other detail.

## LOD Plan

- LOD0: full raised relief, grooves, bevels, channel insets.
- LOD1: 55-60 percent; reduce small chips and secondary bevel loops.
- LOD2: 25-35 percent; flatten minor grooves, preserve horn/wing/crescent/claw silhouette.
- LOD3: 10-15 percent; preserve symbol outline and emissive color blocks only.

## Collision Notes

- Wall/decal reference variants: no collision.
- Floor insert: flat simple collision if used as a walkable mesh.
- Raised wall relief: simple non-complex collision only if it can block movement; otherwise no collision.
- No gameplay collision is implied by emissive channels.

## Animation Notes

- Static by default.
- Optional scalar-driven glow states: inactive, smolder, trial active, accepted, rejected, cooldown.
- No cloth, skeletal, or Blueprint animation in this package.
- VFX hooks belong to consuming packages such as WorthinessJudgment, RegenerationBrand, or RitualAltar.

## Unreal Import Notes

- Asset type: Static Mesh / decal source reference.
- Folder path: `/Game/Aerathea/Props/Infernals/BalgorothCult/Sigils/`
- Pivot:
  - Wall relief: center back face.
  - Floor insert: center bottom.
  - Altar inset: center back face.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Collision: none or simple per variant.
- LODs: LOD0-LOD3 required for placed mesh variants.
- Material slots: 1-3; 4 only for hero floor insert if approved.
- Socket plan:
  - `vfx_sigil_core`
  - `vfx_eye_core`
  - `vfx_rejected_break`
  - `snap_floor_center` for floor insert variant

## Folder And Naming Recommendation

- Package folder: `docs/assets/props/SM_INF_BalgorothSigil_A01/`
- Related material package: `docs/assets/materials/MI_INF_CultStone_Set_A01/`
- Related kit: `docs/assets/kits/KIT_INF_BalgorothCult_A01/`
- Source folder: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01/`
- Export folder: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01/`
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/Sigils/`

Recommended Unreal asset names:

- `SM_INF_BalgorothSigil_WallRelief_A01`
- `SM_INF_BalgorothSigil_FloorInsert_A01`
- `SM_INF_BalgorothSigil_AltarInset_A01`
- `MI_INF_BalgorothSigil_A01_Basalt`
- `MI_INF_BalgorothSigil_A01_Emissive`

## Quality Gate Checklist

- Symbols are original to Aerathea.
- Horned crown, split wing, hooked tail crescent, claw slash, ember eye, and broken circle are all readable.
- The design does not rely on readable text or copied glyphs.
- Large relief geometry carries the silhouette; tiny cracks and wear stay in textures/normal maps.
- Materials follow `MI_INF_CultStone_Set_A01`.
- LOD0-LOD3, collision, pivots, sockets, material slots, and Unreal paths are defined.
- Glow remains sparse and state-driven.
