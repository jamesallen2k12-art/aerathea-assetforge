# Siege Breaker Visual Fidelity A04 Output Record

- Contract: `SB-VF-A04-STRICT-SCANLINE`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: 2026-07-21
- Artifact status: `quarantined`
- Pipeline status: `invalid as a completed 3D asset; superseded by A05 Core Recovery`

> Recovery override: the original result below is preserved as historical
> evidence only. Its candidate implication was invalidated by Flamestrike's
> visible review and `VISUAL_FIDELITY_A04_DRIFT_RECOVERY_A05_RESTART.json`.

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

## Superseding Visual Decision

Flamestrike rejected A04 as a completed 3D solution and directed a reset. The
board is `invalid`; A04 geometry, textures, and exports are `quarantined`; its
technical audits remain `proof only`. A05 must restart from orthographic and
numeric authority. Unreal import remains unauthorized and `Fully game-ready`
remains false.
