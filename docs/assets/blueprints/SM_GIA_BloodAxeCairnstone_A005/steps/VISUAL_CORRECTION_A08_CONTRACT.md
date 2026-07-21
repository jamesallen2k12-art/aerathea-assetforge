# A005 Visual Correction A08 Contract

Status: `active authorized correction contract`

Artifact classification: `authoritative`

Contract ID: `A005-CR-VISUAL-CORRECTION-A08`

Date: 2026-07-21

## Goal

Correct the rejected A07 image so the two masonry courses and peripheral
rubble match the authoritative source organization, remain undeformed in all
fixed views, and read as actual individual stones.

## Authority

- Flamestrike: `you have full approval and full authority to correct this
  image no matter what that requires ...present the final image to me for
  visual approval when complete`.
- Fresh-context handoff:
  `VISUAL_CORRECTION_A07_VISUAL_REJECTION_A08_RESTART_HANDOFF.md`.
- Authoritative source/top panel and A06 exterior-edge measurement record.
- Exact A04 C001/plinth construction as the only retained visual
  construction reference.

## Required Sequence

1. Run a measurement-only audit of the authoritative top panel. It may show
   source pixels and exact marks only; no candidate fills or geometry.
2. If the gate passes, checkpoint before Blender work.
3. Build fresh A08-only C002/C003/C004 stone islands. A07 geometry inputs are
   forbidden.
4. Preserve exact A04 C001 geometry and UV signatures.
5. Enforce positive visible Z clearance between C004/C003 and C003/C002 at
   every stone.
6. Use per-stone UV projection/orientation; vertically smeared side faces are
   a hard failure.
7. Produce front, left, right, and true orthographic top proofs before the
   final perspective render.
8. Independently audit source hashes, counts, bounds, clearances, UVs,
   watertightness, LODs, collision, FBX re-import, and render integrity.
9. Open only the accepted final perspective image for Flamestrike visual
   approval.

## Bounded Interpretation Rule

- C002 source-visible neutral stone cores establish 19 stones.
- C003 source-visible neutral stone cores establish 24 stones.
- C004 exact rubble count remains blocked by occlusion and merged
  silhouettes. Use 32 independent rubble stones as a construction-only rule,
  tied to approved Step 11 C004 32-sector sampling. This does not claim an
  exact source count.
- Stone angular widths are derived from adjacent source-visible core-centroid
  midpoints. They are construction boundaries, not claimed source-owned
  closed contours.

## Stop Boundary

The result stops at one `candidate` / `DCC game-ready candidate` image for
Flamestrike approval. Unreal, Step 17, canon promotion, approved-library
promotion, and `Fully game-ready` classification remain forbidden.
