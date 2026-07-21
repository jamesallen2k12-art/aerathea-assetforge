# Siege Breaker Visual Fidelity A03 Output Record

- Contract: `SB-VF-A03-PIXEL`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: 2026-07-21
- Artifact status: `candidate`
- Pipeline status: `DCC game-ready candidate pending Flamestrike visual approval`

## Decision Produced

A fresh A03 DCC candidate now exists under the approved pixel-reconstruction
authority. It preserves the exact physical dimensions, uses no A01/A02
geometry, passes the declared pixel comparison, and passes independent DCC and
clean-reimport validation. This record does not self-approve visual quality.

## Core Evidence

- Exact envelope: `52 x 32 x 170 cm`.
- Grip interval and outer diameter: `18-60 cm`, `4.994 cm` observed against `5.00 cm` authority.
- Source components / source triangles: `224 / 14264`.
- LOD triangles: `9794 / 6228 / 4264 / 1839`.
- Materials: `5`.
- Texture maps: `20`, all `2048 x 2048`, hashes verified.
- Collision: `3` named UCX proxies.
- Export audit: four FBXs and one GLB cleanly reimported with expected triangles and bounds.
- Pixel comparison: `5/5 pass`.
- Technical audit: `36/36 pass`.
- Final matched-render SHA-256: `023fc8f0bd90ed2091e2b3ceba69f32f3a348c60ec2f3bb7c865d436886498ac`.
- Final review-board SHA-256: `c109f986ee027996792505c5a8517e7efaee5925ae83bd1cf1c194725c41adf4`.

## Required Visual Decision

Flamestrike must classify the opened A03 review board as approved, rejected, or
blocked. Until that decision, the asset remains a `candidate`. Unreal import is
not authorized by this contract and `Fully game-ready` remains false.
