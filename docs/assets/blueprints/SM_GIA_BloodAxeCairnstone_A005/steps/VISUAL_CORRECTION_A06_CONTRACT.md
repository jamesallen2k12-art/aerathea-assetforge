# A005 Visual Correction A06 Contract

Status: `complete; candidate pending Flamestrike visual approval`

Artifact classification: `authoritative execution contract`

Contract ID: `A005-CR-VISUAL-CORRECTION-A06`

Date: 2026-07-21

## Goal

Correct the two structural base-piece dimensions that caused the A05 visual rejection, preserve the exact A04 plinth, and end with one audited DCC review image for Flamestrike approval.

## Authority

- Flamestrike's 2026-07-21 full approval and authority to continue correcting the base geometry and present the completed image.
- `VISUAL_CORRECTION_A05_VISUAL_REJECTION_A06_RESTART_HANDOFF.md`.
- `VISUAL_CORRECTION_A06_MEASUREMENT_GATE.md` and its authoritative exterior-edge audit.
- The unchanged A005 source panels and source-pixel records.
- The exact A04 plinth visual result, classified as an authoritative visual reference.
- Non-conflicting Step 11 topology/performance rules and Step 14 exact RGB transfer rules.

## Locked Correction

1. Preserve the exact A04 plinth construction and its geometry/UV signatures.
2. Do not import, retain, hide, or repair forward from the rejected A05 base geometry. C002, C003, and C004 are rebuilt in A06-only outputs.
3. C002 upper-course maximum exterior footprint is `123.846154 x 92.707424 cm`.
4. C003 lower-course maximum exterior footprint is `137.307692 x 105.196507 cm`.
5. C004 remains within the approved `140 x 110 cm` footprint and reads only as a shallow peripheral rubble apron.
6. C002 and C003 remain true oval masonry courses with irregular stone widths, recessed joints, and uneven crowns. They may not read as rectangular slabs, smooth skirts, gears, or a manufactured stepped pedestal.
7. Preserve the approved `35 cm` base span and the A05 course-height allocation: C004 `10.5 cm`, C003 `15.0 cm`, C002 `9.5 cm`.
8. Use component-local source routing and exact source-owned RGB transfer. No source recoloring or compensating grade is authorized.
9. The completed review image must show the entire corrected base and plinth without clipping, underside exposure, collision, or proxy geometry.

## Technical Gates

- Exact overall bounds `140 x 110 x 220 cm`; pivot `[0,0,0]`; `1 uu = 1 cm`.
- Four disconnected, independently watertight primary shells: C001-C004.
- Zero boundary edges, non-manifold edges, and degenerate faces.
- C002/C003 maximum footprints match the A06 audit to `0.01 cm`.
- Positive visible ledges in front, left, and final perspective review.
- Exact A04 plinth geometry and UV signatures remain unchanged.
- One runtime material; Base Color, Normal, ORM; no emissive; metallic `0`.
- Source-owned Base Color texels remain byte-exact; color grading count `0`.
- LOD0 `4000-10000` triangles; LOD1-LOD3 strictly decrease; two UV sets; four custom collision hulls; Blender source; four FBXs; clean FBX re-import.
- Internal visual review must reject any result that remains too shallow, cumulative, mechanically regular, clipped, or source-inconsistent.

## Artifact Boundary

- Complete A05 package remains `quarantined`; its technical evidence remains `proof only`.
- A05 C002/C003 geometry and dimensions remain `invalid as A06 construction authority`.
- A05 stonework treatment remains `reference only`.
- A04 plinth remains `authoritative visual reference`.
- Passing A06 outputs are `candidate` and at most a `DCC game-ready candidate` pending Flamestrike visual approval.
- Preserve A01-A05 files. Use only A06 output paths.
- Unreal, Step 17, `Fully game-ready`, approved-library, and visual-canon promotion remain forbidden.

## Decision Output

End as exactly one of:

- `candidate`: all A06 technical and visual gates pass and the exact final image is pending Flamestrike review;
- `blocked`: a required gate cannot be met; or
- `quarantined`: an internal attempt fails and remains non-authority.
