# Aerathea Asset Review Island

## Purpose

`/Game/Aerathea/Maps/L_Aerathea_ReviewIsland` is the controlled Unreal review map for asset color, silhouette, scale, collision, and walk-around inspection.

Use this map instead of `L_Aerathea_Startup` for future single-asset or batch asset reviews unless the review specifically needs gameplay context.

## Current Layout

- 120m square neutral floor.
- Unlit visible review-floor, pad, grid, axis, and scale-marker materials so the island remains visible even if lighting or exposure fails.
- Pale unlit sky dome plus four pale unlit perimeter sky/backdrop walls so review captures do not fall back to a black void.
- Fixed-exposure post-process volume.
- Sky atmosphere source for SkyLight capture.
- Movable key, sky, and four fill lights to avoid baked-lighting drift and unbuilt-lighting review noise.
- Central current-asset pad.
- 12 labeled empty review slots, `SLOT A` through `SLOT L`.
- 1m, 2m, 5m, 11m, and 10m rail scale references.
- Red X axis and green Y axis ground markers.
- Current placed asset: `AET_REVIEW_CurrentAsset_BloodAxeCairn_A01`.
- Tagged runtime review camera: `AET_REVIEW_Camera_Main_A01`.
- Runtime review director: `AET_REVIEW_ReviewCameraDirector_A01`.

## Tooling

- Build or refresh map: `Tools/Unreal/create_review_island.py`
- Validate map: `Tools/Unreal/validate_review_island.py`
- Apply live editor viewport: `Tools/Unreal/apply_review_island_viewport.py`
- Launch visible editor review: `Tools/Unreal/launch_review_island_editor.sh`
- Unreal map path: `/Game/Aerathea/Maps/L_Aerathea_ReviewIsland`
- Latest stable capture: `Saved/Automation/ReviewIsland/AeratheaReviewIsland_Backdrop_Unlit.png`

`Config/DefaultEngine.ini` sets `EditorStartupMap` to this island so editor review sessions open in the clean review environment. `GameDefaultMap` and `ServerDefaultMap` remain pointed at `/Game/Aerathea/Maps/L_Aerathea_Startup`.

The review launcher also runs `apply_review_island_viewport.py` to force the live editor viewport to the review pad, use `VIEWMODE UNLIT`, and request Play In Editor. The PIE path uses `AET_REVIEW_Camera_Main_A01` through `AET_REVIEW_ReviewCameraDirector_A01`, which is more reliable than the Linux editor perspective viewport when X11/Vulkan restores a stale black camera view.

## Validation Evidence

Validated on `2026-07-01T14:48:30-04:00`.

Focused validator result:

`Aerathea review island validation passed: 83 tagged actors, 13 asset slots, fixed-lighting review map /Game/Aerathea/Maps/L_Aerathea_ReviewIsland.`

Map check result:

`MapCheck: Map check complete: 0 Error(s), 0 Warning(s).`

Additional visibility guard:

- Floor, central pad, and first review slot must use the unlit review material family.
- Sky dome and four sky/backdrop walls must use the unlit sky material family.
- Main review camera must carry the `AET_REVIEW_CAMERA` tag.
- Runtime review director must exist for PIE/game-mode review.

## Review Rule

Future generated assets should be placed on this island for first Unreal visual review. The startup map should stay reserved for integrated scene, gameplay-loop, or milestone review work.
