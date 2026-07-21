# A005 Visual Correction A07 Contract

Status: `complete; candidate pending Flamestrike visual approval`

Artifact classification: `authoritative execution contract`

Contract ID: `A005-CR-VISUAL-CORRECTION-A07`

Date: 2026-07-21

## Goal

Correct the A06 top-visible ring projection failure and end with one audited
A07 DCC review image for Flamestrike approval.

## Authority

- Flamestrike's full correction authority and explicit rejection of A06 with
  direction to compare the ring reach against the original top-down view.
- `VISUAL_CORRECTION_A06_TOP_PROJECTION_REJECTION_A07_RESTART_HANDOFF.md`.
- `VISUAL_CORRECTION_A06_TOP_PROJECTION_DRIFT.json`.
- `VISUAL_CORRECTION_A07_TOP_CROWN_AUTHORITY.json`.
- The unchanged A005 source/top panel and A06 exterior-edge measurement record.
- The exact A04 plinth visual construction.
- Non-conflicting Step 11 topology/performance and Step 14 RGB-transfer rules.

## Locked Correction

1. Build isolated A07 outputs. Do not load, modify, or use the A06 Blender/FBX
   package as geometry input.
2. Preserve the exact A04 plinth geometry and UV signatures.
3. C002's top-visible outer crown must reach
   `123.846154 x 92.707424 cm` within `0.01 cm`.
4. C003's top-visible outer crown must reach
   `137.307692 x 105.196507 cm` within `0.01 cm`.
5. C004's top-visible peripheral crown must reach `140 x 110 cm` within
   `0.01 cm`.
6. The three exterior targets may not exist only on lower sidewalls or hidden
   rings, and the visible crowns may not taper inward before their outer edge.
7. Preserve the approved `35 cm` base span, oval masonry construction,
   irregular stone widths, recessed joints, uneven crowns, and non-mechanical
   read.
8. Preserve component-local source routing and byte-exact source-owned RGB.
   No compensating color grade is authorized.
9. Produce a true orthographic top proof and measure each top-band XY extent
   before rendering the final perspective image.

## Technical Gates

- Exact overall bounds `140 x 110 x 220 cm`; pivot `[0,0,0]`; `1 uu = 1 cm`.
- Four disconnected watertight C001-C004 shells; zero boundary,
  non-manifold, and degenerate failures.
- Whole-component C002/C003/C004 bounds match their exterior targets.
- Top-band C002/C003/C004 bounds independently match the same targets.
- True orthographic top proof exists, is unclipped, and shows all three
  exterior crown boundaries.
- Exact A04 plinth geometry/UV signatures remain unchanged.
- One material; Base Color, Normal, ORM; source-owned RGB mismatch count `0`.
- LOD0 `4000-10000` triangles; strictly decreasing LODs; two UV sets; four
  collision hulls; four FBXs; clean FBX re-import.
- Final review is complete, upright, unclipped, and contains no collision,
  markers, proxy geometry, or underside exposure.

## Artifact Boundary

- A06 complete package and final image remain `quarantined`.
- A06 audit is `proof only`; its top-view implication is invalid.
- A06 exterior-edge measurement record remains `authoritative`.
- Passing A07 outputs are `candidate` and at most a `DCC game-ready candidate`
  pending Flamestrike visual approval.
- Preserve all earlier artifacts. Use only A07 output paths.
- Unreal, Step 17, `Fully game-ready`, approved-library, and visual-canon
  promotion remain forbidden.

## Decision Output

End as `candidate`, `blocked`, or `quarantined`. Only the exact final A07
image may be presented for Flamestrike's visual decision.
