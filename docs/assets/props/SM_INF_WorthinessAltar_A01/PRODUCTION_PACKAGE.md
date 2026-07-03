# SM_INF_WorthinessAltar_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_INF_WorthinessAltar_A01`
- Asset type: Static Mesh ritual altar prop
- Parent kit: `KIT_INF_BalgorothCult_A01`
- World: Aerathea
- Theme: Balgoroth worthiness judgment altar, culling-trial focus point, sacrifice-state prop without gore
- Status: first-pass DCC/Unreal review implementation complete and validated; native Blueprint wrapper implemented and validated; final art, authored textures, and tuned collision pending

`SM_INF_WorthinessAltar_A01` is the ritual focal prop that snaps to `SM_INF_CullingTrialFloor_A01` and gives `VFX_INF_WorthinessJudgment_A01` a readable altar target. It should feel severe, predatory, old, and judgmental: a black-basalt and obsidian altar with a horned crown backplate, split-wing side geometry, ember channels, a central offering/sigil basin, and clear VFX sockets for accepted and rejected states.

The altar must not depend on gore, body parts, or excessive flame. It should communicate Balgoroth's judgment through shape language, material contrast, and restrained ember/violet state effects.

Approved readability reference: `Saved/ReferenceAdjustments/Infernals_Guarding_a_Gate2_Bright20_A04_RivetReduced_Stronger.png`. The first-pass implementation preserves the cleaned reference rule: large horn/wing/stone/glow forms are modeled, while rivets, speckle, heat stress, ash, fine cracks, and small scratches remain texture/normal-map work.

## Implementation Status

- Blender source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/SM_INF_WorthinessAltar_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/SM_INF_WorthinessAltar_A01.fbx`
- DCC proof: `Saved/Automation/InfernalWorthinessAltarReview/SM_INF_WorthinessAltar_A01_DCCReview.png`
- Unreal mesh: `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01`
- Blueprint wrapper: `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01`
- Native class: `AAETInfernalRitualAltarActor`
- Startup actor: `AET_PROD_INF_WorthinessAltar_A01`, now placed as the Blueprint wrapper and snapped to `SM_INF_CullingTrialFloor_A01` `snap_altar`
- Focused Blueprint validation: passed at `356.00h x 404.00w x 346.00d cm`, bounds radius `320.03 cm`, 9 components, 6 state materials, 6 Niagara systems.
- Mesh-level validation: passed at `356.00h x 404.00w x 346.00d cm`, bounds radius `320.03 cm`, 9 sockets.
- Startup validation: passed with `233 assets`, `55 expected actors`, and `25 ground tiles`.

## 2. Gameplay Purpose

- Provides the mesh dependency for the implemented `BP_INF_RitualAltar_A01`.
- Snaps to the accepted culling floor through `snap_altar`.
- Hosts worthiness trial states: inactive, smolder, trial active, accepted, rejected, judgment pulse, and cooldown.
- Gives encounter and quest designers a readable ritual interaction point for Lesser Infernal blooding scenes, cult rooms, and trial arenas.
- Supports future audio, VFX, interaction prompts, state materials, and scripted failure/success responses.

## 3. Silhouette Notes

- Primary read: low heavy altar mass, raised horned crown backplate, split-wing side slabs, and central ember basin.
- Keep the front interaction side open and readable.
- Use broad angular stone masses, not thin spike forests.
- Include one large broken-circle or claw-scratch rejection channel that can carry violet-red VFX.
- The altar should read as Balgoroth cult architecture, not a generic stone table, forge, or throne.
- Avoid hanging micro-chains, tiny repeated skulls, dense rivets, and unreadable carved text.

## 4. Scale Notes

- Footprint target: 260-340 cm wide, 160-240 cm deep.
- Front interaction height: 100-130 cm.
- Rear horned backplate height: 240-340 cm.
- Side wing slabs should stay below wing-snag height unless deliberately used as blockers.
- Pivot: center-bottom at the snap point, aligned so the front faces the culling floor center.
- Must work beside 70-90 cm Lesser Spawn and 274 cm Exalted adult Infernals.

## 5. Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Cult basalt | black, blue-black, ash-gray edge wear | main altar body, plinth, backplate |
| Scorched red stone | dark red, burnt umber, heat-worn edges | top slab, channel insets |
| Obsidian/black iron | near-black, charcoal metal, bronze edge wear | offering basin, braces, sigil insets |
| Bone and horn | aged ivory, smoke-stained tan | large horn/crown ornaments only |
| Brand glow | ember orange, deep red, restrained violet-red | ring link, altar core, rejected crack |

Glow must stay localized to sockets, channels, and the central basin.

## 6. Visual Exploration Prompts

1. Create an original stylized fantasy MMORPG concept image of `SM_INF_WorthinessAltar_A01` for Aerathea as a low black-basalt judgment altar with a horned crown backplate, split-wing side slabs, ember core basin, and restrained violet rejection crack.
2. Create an original stylized fantasy MMORPG concept image of `SM_INF_WorthinessAltar_A01` as a broad obsidian-and-basalt altar built into the edge of a Balgoroth culling floor, with heavy claw grooves, scorched red stone channels, and no gore.
3. Create an original stylized fantasy MMORPG concept image of `SM_INF_WorthinessAltar_A01` as a compact ritual platform for Lesser Infernal trials, with a low offering slab, angular horned crest, ember ring link, and readable MMO-scale silhouette.
4. Create an original stylized fantasy MMORPG concept image of `SM_INF_WorthinessAltar_A01` as a tall ceremonial altar with a split-wing rear silhouette, blackened iron braces, bone horn accents, and a central accepted/rejected VFX socket callout.
5. Create an original stylized fantasy MMORPG concept image of `SM_INF_WorthinessAltar_A01` as a modular altar that snaps to `SM_INF_CullingTrialFloor_A01`, showing front, side, top footprint, sockets, simple collision, and material swatches.
6. Create an original stylized fantasy MMORPG concept image of `SM_INF_WorthinessAltar_A01` as an altar for Balgoroth cult priests, with severe angular basalt slabs, a broken-circle rejection channel, smoldering ember lines, and restrained ash motes.
7. Create an original stylized fantasy MMORPG concept image of `SM_INF_WorthinessAltar_A01` as a trial-state prop with inactive, smolder, trial active, accepted, rejected, and cooldown frames on a clean production board.
8. Create an original stylized fantasy MMORPG concept image of `SM_INF_WorthinessAltar_A01` as an old predatory altar with a horned crown crest and split-wing silhouette, scaled beside a 180 cm humanoid and a 274 cm Infernal.
9. Create an original stylized fantasy MMORPG concept image of `SM_INF_WorthinessAltar_A01` as a black basalt and obsidian ritual object with large readable bone/horn accents, red-orange emissive channels, and simple MMO-safe geometry.
10. Create an original stylized fantasy MMORPG concept image of `SM_INF_WorthinessAltar_A01` as the mesh anchor for implemented `BP_INF_RitualAltar_A01`, showing VFX sockets for altar core, sacrifice mark, brand transfer, ring link, and rejected gap.

## 7. Concept Image Prompt

Create an original stylized fantasy MMORPG concept sheet of `SM_INF_WorthinessAltar_A01`, a Balgoroth cult worthiness judgment altar for the Infernals of Aerathea. The design should emphasize a heavy black-basalt altar mass, horned crown backplate, split-wing side slabs, obsidian offering basin, scorched red stone channels, large readable claw grooves, restrained ember-orange ritual glow, a short violet-red rejected-state crack, clear snap alignment to `SM_INF_CullingTrialFloor_A01`, and MMO-friendly production geometry. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and mid-poly Unreal-safe construction. Present it as a static mesh production sheet with front view, side view, top footprint, material swatches, socket callouts, collision blocks, inactive/smolder/trial-active/accepted/rejected state notes, and scale beside a 180 cm humanoid, a Lesser Spawn, and a 274 cm Infernal. Avoid copied franchise designs, gore, excessive particles, readable text, watermarks, photoreal fire simulation, tiny spike forests, and cluttered micro-detail.

## 8. Modeling Notes

- Model real geometry for the altar body, top slab, horned crown backplate, split-wing side slabs, central basin, large claw grooves, major cracks, and large bone/horn accents.
- Use texture/normal maps for fine stone cracks, ash smears, heat stress, small chips, tiny scratches, and subtle brand wear.
- Build the front interaction side open and obvious.
- Use a modular base footprint that can snap cleanly to `SM_INF_CullingTrialFloor_A01`.
- Keep channels and symbols broad enough to read from MMO camera distance.
- Do not add gore, readable glyph text, dense chains, or per-rivet geometry.

## 9. Texture And Material Notes

Texture targets:

- `T_INF_WorthinessAltar_A01_BC`
- `T_INF_WorthinessAltar_A01_N`
- `T_INF_WorthinessAltar_A01_ORM`
- `T_INF_WorthinessAltar_A01_E`

Material slots:

1. `MI_INF_WorthinessAltar_A01_CultStone`
2. `MI_INF_WorthinessAltar_A01_ScorchedStone`
3. `MI_INF_WorthinessAltar_A01_ObsidianIron`
4. `MI_INF_WorthinessAltar_A01_BoneHorn`
5. `MI_INF_WorthinessAltar_A01_BrandGlow`

Reuse the Balgoroth cult stone, obsidian/black iron, and BrandGlow material language where practical. Final authored textures should use 1K-2K sets; 4K is not justified for this reusable prop.

## 10. Triangle Budget

- LOD0 target: 6k-14k tris.
- Hero room ceiling: 18k tris only if a larger backplate variant is approved.
- Material slot target: 4-5.
- Optional helper planes/ribbons for VFX should stay under 300 tris total and be shared or removable.

## 11. LOD Plan

- LOD0: full altar mass, horned crown, split-wing side slabs, top basin, broad claw grooves, major cracks, large horn/bone accents, emissive channels.
- LOD1: 55-60 percent; reduce bevels, small stone chips, secondary cracks, and minor brace cuts.
- LOD2: 25-35 percent; simplify horn/bone accents, flatten channel bevels, merge secondary slab cuts.
- LOD3: 10-15 percent; preserve altar footprint, horned backplate, split-wing side read, central basin, and glow blocks.

Never reduce the primary altar silhouette, snap footprint, or central VFX basin before small surface detail.

## 12. Collision Notes

- Use simple UCX boxes or convex hulls for base plinth, side slabs, top slab, and rear backplate.
- Do not use complex-as-simple for final gameplay.
- Keep front interaction space unobstructed.
- Small horns, ornaments, cracks, and channels should be non-blocking unless the silhouette requires a broad blocker.
- Validate tail and wing clearance with 274 cm Infernals after DCC import.

## 13. Animation Notes

- Static mesh is not animated by default.
- `BP_INF_RitualAltar_A01` drives:
  - Inactive: no VFX, dark channels.
  - Smolder: low ember in basin and ring link.
  - Trial active: ring-to-core pulse.
  - Accepted: warm focused ember pulse.
  - Rejected: short violet-red snap through broken-circle channel.
  - Judgment pulse: horned crown and basin pulse, then cooldown.
- Optional moving parts are not required for first pass.

## 14. Unreal Import Notes

- Asset type: Static Mesh.
- Primary mesh: `SM_INF_WorthinessAltar_A01`.
- Folder path: `/Game/Aerathea/Props/Infernals/BalgorothCult/`.
- Pivot: center-bottom at snap alignment point.
- Scale: centimeters, no import scaling.
- Collision: authored UCX simple volumes or generated simple collision.
- Material slot count: 4-5.
- Suggested sockets:
  - `snap_floor`
  - `snap_arch_back`
  - `interact_front`
  - `stage_offering`
  - `vfx_altar_core`
  - `vfx_sacrifice_mark`
  - `vfx_brand_transfer`
  - `vfx_ring_link`
  - `vfx_rejected_gap`
- VFX dependency: `/Game/Aerathea/VFX/Infernals/WorthinessJudgment/`
- Material-state dependency: `/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_*`
- Blueprint wrapper: `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01`

## 15. Folder And Naming Recommendation

- Package folder: `docs/assets/props/SM_INF_WorthinessAltar_A01/`
- Source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/`
- Export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/`
- Unreal mesh: `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01`
- Materials: `MI_INF_WorthinessAltar_A01_*`
- Textures: `T_INF_WorthinessAltar_A01_*`
- Modeling handoff: `docs/assets/props/SM_INF_WorthinessAltar_A01/MODELING_HANDOFF.md`

## 16. Quality Gate Checklist

- Reads as Balgoroth/Infernal cult altar, not common stone furniture.
- Supports worthiness judgment without gore.
- Snaps cleanly to `SM_INF_CullingTrialFloor_A01`.
- Supports implemented `BP_INF_RitualAltar_A01` and `VFX_INF_WorthinessJudgment_A01`.
- Horned crown, split wing, central basin, and rejected-state channel are readable at gameplay camera distance.
- Materials match the cult kit: basalt, scorched red stone, obsidian/black iron, bone/horn, restrained ember/violet glow.
- Major forms are real geometry; fine cracks, scratches, and micro-brands stay in maps.
- Triangle budget, LODs, collision, sockets, material slots, texture maps, pivot, and Unreal paths are defined.
- Visual direction is approved; first-pass DCC/Unreal and native Blueprint validations are complete.
