# Siege Breaker Visual Fidelity A04 Output Record

- Contract: `SB-VF-A04-STRICT-SCANLINE`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: 2026-07-21
- Artifact status: `candidate`
- Pipeline status: `DCC game-ready candidate pending Flamestrike visual approval`

## Decision Produced

A fresh source-only A04 package now exists and satisfies the approved strict-
scanline DCC contract. It preserves the exact numeric envelope, gives each
front/back/left/right visible component its own source-owned pixels, supplies a
closed three-dimensional production mesh, and passes the declared fail-closed
evidence chain. This record does not self-approve visual quality.

## Core Evidence

- Source concept SHA-256:
  `3308a7bd0f0830c9cd1b695b57077d9faf77a839bb3e70edc6afe87c68af8b74`.
- Fresh scanline: zero changed pixels; maximum RGB delta `0`.
- Pregeometry audit: `55/55 pass`.
- Exact envelope: `52 x 32 x 170 cm`; pivot at `Z=0`.
- Source lineage: no A01/A02/A03 geometry or texture inputs.
- Front/back/left/right visible RGB: exact integer-coordinate copy; no filtered
  resampling.
- Top/bottom ownership: inferred closure, because the corresponding drawn panel
  scales conflict with the fixed-object numeric authority.
- LOD triangles: `11592 / 6552 / 3676 / 1676`.
- Materials: `5`.
- Texture maps: `20`, all `2048 x 2048`.
- Collision: `3` named UCX proxies.
- Exports: four FBXs and one GLB; clean reimport passed.
- Independent technical audit: `24/24 pass`.
- Fail-closed strict-pixel gate: `pass`.
- Final review-board SHA-256:
  `86496214ba7b593286e275be0cf4b59a7327baaede8f46563251ab7afdd36710`.

## Required Visual Decision

Flamestrike must classify the opened A04 final completed review board as
`approved`, `rejected`, or `blocked`. Until that decision, the asset remains a
`candidate`. Unreal import is not authorized by this contract and `Fully
game-ready` remains false.
