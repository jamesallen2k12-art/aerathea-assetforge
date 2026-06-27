# SM_AET_Palisade_A01 Production Package

## Art Direction Summary

- Asset name: `SM_AET_Palisade_A01`
- Asset type: Static Mesh modular settlement kit
- World: Aerathea
- Faction/theme: Aerathea/Common starter settlement
- Source anchor: approved Aerathea building/prop style; `Gatehouse Approved.png` used only as supporting wall/gate material reference
- Current status: First-pass DCC review sources generated, Unreal imports complete, material instances assigned, LOD0-LOD3 generated, startup placements complete, validation passing

Build status:

- Blender sources:
  - `SourceAssets/Blender/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Wall_A01/SM_AET_Palisade_Wall_A01.blend`
  - `SourceAssets/Blender/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Post_A01/SM_AET_Palisade_Post_A01.blend`
  - `SourceAssets/Blender/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Corner_A01/SM_AET_Palisade_Corner_A01.blend`
  - `SourceAssets/Blender/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Gate_A01/SM_AET_Palisade_Gate_A01.blend`
  - `SourceAssets/Blender/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_EndCap_A01/SM_AET_Palisade_EndCap_A01.blend`
- Unreal assets: `/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_*_A01`
- Startup actors: `AET_PROD_Palisade_Wall_A01`, `AET_PROD_Palisade_Post_A01`, `AET_PROD_Palisade_Corner_A01`, `AET_PROD_Palisade_Gate_A01`, `AET_PROD_Palisade_EndCap_A01`
- Validation: included in `Tools/Unreal/validate_startup_scene.py`
- Technical polish complete: review UVs, weighted normals, per-module material instances, and generated LOD0-LOD3.
- Remaining production work: approved art-model pass, shared UV atlas, BC/N/ORM material set, snap review, collision fit review, and final gate interaction Blueprint only after rules are approved.

Create the first modular Aerathea settlement defense kit: chunky timber palisade walls with stone footings, dark-iron straps, simple blue cloth or painted markers where needed, warm lantern-compatible accents, and broad hand-painted wear. This is a practical starter-settlement asset, not a fortress wall.

## Gameplay Purpose

Supports early settlement layout, collision validation, training-yard boundaries, path gating, town-edge dressing, and modular snapping tests. It gives the startup slice a first building-scale modular asset without the risk of a full house or town hall.

## Silhouette Notes

Primary read:

- Tall uneven timber stakes with broad points.
- Chunky horizontal brace beams.
- Heavy posts at modular joins.
- Simple gate silhouette with readable hinge posts.
- Stone or packed-earth footings that ground the wall.

Avoid thin toothpick logs, dense rope strands, tiny nail fields, and overbuilt fortress detail. The wall should read clearly at MMO camera distance and survive LOD3 as a timber barrier.

## Scale Notes

Recommended modules:

- `SM_AET_Palisade_Wall_A01`: 400 cm wide, 300 cm tall, 50-70 cm deep.
- `SM_AET_Palisade_Post_A01`: 60-80 cm wide/deep, 320 cm tall.
- `SM_AET_Palisade_Corner_A01`: 400 cm x 400 cm footprint, 300 cm tall.
- `SM_AET_Palisade_Gate_A01`: 400 cm wide, 330 cm tall, player-width opening.
- `SM_AET_Palisade_EndCap_A01`: 80-120 cm wide, 300 cm tall.

Pivot per module: bottom center or grid-corner pivot must be chosen consistently in DCC. Recommended for wall spans: center bottom at grid origin, snapping on a 400 cm grid.

## Materials And Color Palette

Primary materials:

- Timber: dark warm brown, hand-hewn, broad grain painted into texture.
- Stone footings: muted gray, low-saturation, broad cracks in normal map.
- Dark iron: charcoal braces, hinge straps, and large nail plates.
- Leather/rope: optional broad bindings only.
- Cloth/paint: muted blue markers only where faction readability helps.
- Lantern warmth: optional attachment sockets, not built into every module.

Texture style uses baked-AO-style depth in plank overlaps and post bases. Do not model tiny grain, nail heads, splinters, or rope fibers.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a modular starter-settlement palisade kit for the world of Aerathea. The design should emphasize chunky uneven timber stakes, broad horizontal braces, heavy join posts, a simple gate module, stone footings, dark-iron straps, restrained blue settlement markers, practical frontier defense culture, grounded MMO town-edge mood, and modular collision gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no unnecessary emissive effects, and MMO-friendly production design. Present it as an asset board with wall span, post, corner, gate, end cap, scale callout, LOD callout, and material swatches on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model real geometry for:

- Main stakes/logs.
- Horizontal braces.
- Gate planks and large hinge blocks.
- Stone footing blocks.
- Major iron straps and large plates.
- Lantern/banner sockets if included.

Fake with texture/normal maps:

- Wood grain.
- Small cracks.
- Fine splinters.
- Nail heads.
- Rope fibers.
- Scratches and mud staining.

Keep each module snap-clean. Decorative edge breaks must not change the gameplay footprint.

## Texture And Material Notes

Texture sets:

- `T_AET_Palisade_A01_BC`
- `T_AET_Palisade_A01_N`
- `T_AET_Palisade_A01_ORM`

Optional shared trim/variant:

- `T_AET_Palisade_A01_Detail_BC`
- `T_AET_Palisade_A01_Detail_N`
- `T_AET_Palisade_A01_Detail_ORM`

Material instances:

- `MI_AET_Palisade_A01`
- Optional: `MI_AET_Palisade_A01_Snow`, `MI_AET_Palisade_A01_Moss`, `MI_AET_Palisade_A01_Worn`

Target 1-2 material slots per module. Use a shared atlas or trim sheet for all modules.

## Triangle Budget

Small building/modular environment target:

- Wall module LOD0: 4k-8k tris.
- Post/end cap LOD0: 1.5k-4k tris.
- Corner module LOD0: 5k-10k tris.
- Gate module LOD0: 6k-12k tris.

Keep the full five-module review set under roughly 35k tris at LOD0.

## LOD Plan

- LOD0: full module silhouettes, broad bevels, major straps, stone footings.
- LOD1: remove small bevel loops, simplify straps, reduce stake side cuts.
- LOD2: merge stakes into broader clusters, simplify stone footing blocks.
- LOD3: preserve wall/gate outline, posts, and large braces only.

Never reduce wall height, gate opening shape, or module footprint first.

## Collision Notes

Use simple collision only:

- Wall: 1-2 boxes matching the barrier, no per-stake collision.
- Post: one box/capsule.
- Corner: two wall boxes plus post box.
- Gate: blocking collision when closed; opening collision disabled or split into side posts when open.

Recommended UCX naming:

- `UCX_SM_AET_Palisade_Wall_A01_00`
- `UCX_SM_AET_Palisade_Post_A01_00`
- `UCX_SM_AET_Palisade_Corner_A01_00`
- `UCX_SM_AET_Palisade_Gate_A01_00`
- `UCX_SM_AET_Palisade_EndCap_A01_00`

Do not use complex-as-simple collision.

## Animation Notes

Static baseline for wall, post, corner, and end cap.

Gate can start as static closed/open mesh variants:

- `SM_AET_Palisade_GateClosed_A01`
- `SM_AET_Palisade_GateOpen_A01`

Create `BP_AET_PalisadeGate_A01` later only when interaction rules are approved.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Buildings/Common/Palisade/`
- Material folder: `/Game/Aerathea/Materials/Buildings/Common/Palisade/`
- Texture folder: `/Game/Aerathea/Textures/Buildings/Common/Palisade/`
- Grid snap: 400 cm.
- Scale: centimeters.
- Pivot: consistent bottom/grid pivot per module.
- Collision: imported UCX or generated simple primitives.
- LODs: LOD0-LOD3 for each important module.
- Nanite: off for this first modular validation kit unless project policy changes.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_AET_Palisade_A01/`
- Source: `SourceAssets/Blender/Buildings/Common/Palisade/SM_AET_Palisade_A01/`
- Export: `SourceAssets/Exports/Buildings/Common/Palisade/SM_AET_Palisade_A01/`

Recommended child asset names:

- `SM_AET_Palisade_Wall_A01`
- `SM_AET_Palisade_Post_A01`
- `SM_AET_Palisade_Corner_A01`
- `SM_AET_Palisade_Gate_A01`
- `SM_AET_Palisade_EndCap_A01`
- `MI_AET_Palisade_A01`

## Quality Gate Checklist

- Original Aerathea/Common settlement identity.
- Modular wall, post, corner, gate, and end cap are defined.
- 400 cm snapping plan is clear.
- Primary timber barrier silhouette survives LOD3.
- Wood/stone/iron material language matches Aerathea settlement assets.
- No excessive modeled nails, splinters, rope fibers, or tiny cracks.
- Triangle budgets, texture maps, material slots, LODs, collision, and Unreal paths are included.
- Gate interaction remains deferred until gameplay rules are approved.
