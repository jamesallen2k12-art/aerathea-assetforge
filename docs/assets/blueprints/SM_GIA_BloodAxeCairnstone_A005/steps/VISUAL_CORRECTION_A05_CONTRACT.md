# A005 Visual Correction A05 Contract

Status: `authorized for complete Steps 01-16 corrective execution`

Artifact classification: `authoritative execution contract`

Contract ID: `A005-CR-VISUAL-CORRECTION-A05`

Date: 2026-07-21

## Goal

Replace the visually rejected A04 base with a source-measured oval masonry
base while preserving the exact A04 plinth visual result. End with one audited
Steps 01-16 DCC game-ready candidate and one final review image, or block.

## Authority

- Flamestrike's 2026-07-21 full approval and authorization to correct the 3D
  image.
- `VISUAL_CORRECTION_A04_VISUAL_REJECTION_A05_RESTART_HANDOFF.md`.
- `VISUAL_CORRECTION_A05_MEASUREMENT_GATE.md` and its authoritative audit.
- The unchanged A005 source image and source-pixel records.
- The exact A04 plinth visual result, classified as an authoritative visual
  reference.
- Non-conflicting Step 11 topology/performance rules and Step 14 exact RGB
  transfer rules.

## Locked Correction

1. Preserve the A04 plinth construction exactly: the A04 profile stations,
   `92` angular segments, exponent `4.5`, source projection, UV placement,
   material response, and displayed source pixels remain unchanged.
2. Do not import, retain, hide, or build on the rejected A04 base geometry.
   C002, C003, and C004 are rebuilt as A05-only shells.
3. C002 upper-course maximum footprint is
   `119.097222 x 77.647059 cm`.
4. C003 lower-course maximum footprint is
   `134.652778 x 96.561086 cm`.
5. C004 remains within the approved `140 x 110 cm` footprint.
6. C002 and C003 use a true elliptical construction basis (`n=2`) with
   source-bounded hand-set block irregularity. The ellipse is an explicitly
   classified construction interpretation; it is not source evidence.
7. Use one visible stone course for C002, one larger visible stone course for
   C003, and a shallow peripheral rubble apron for C004. Their top surfaces
   must contain visible block crowns and recessed joints; they may not read as
   smooth stacked slabs.
8. Allocate the approved `35 cm` base span as C004 `10.5 cm`, C003 `15.0 cm`,
   and C002 `9.5 cm`. Each selection lies inside the authoritative two-view
   measurement interval; the selection is a construction interpretation, not
   a source-exact individual height claim.
9. Use the approved production center/pivot `[0,0,0]` only as a technical
   construction datum. Do not claim it as a source-authored component center.
10. Preserve exact source-owned atlas RGB bytes. Route visible C002/C003 top
    faces to their component-local top-panel annuli and vertical owner faces
    to their corresponding front/left/back/right source bands. Correct
    geometry and face ownership before judging UV placement; no color grade is
    allowed.

## Technical Gates

- Exact overall bounds `140 x 110 x 220 cm`; pivot `[0,0,0]`; `1 uu = 1 cm`.
- Four disconnected, independently watertight primary shells: C001-C004.
- Zero boundary edges, non-manifold edges, and degenerate faces.
- C002/C003 footprint dimensions match the measurement audit to `0.01 cm`.
- C002 and C003 X/Y ratios are greater than A04's rejected ratios and their
  projected widths narrow away from the widest source-owned stations.
- C002/C003/C004 top-face block joints and crowns are present as geometry,
  without exceeding the locked footprints.
- A04 plinth geometry/UV signature for the non-overlap region at `Z >= 36 cm`
  is unchanged.
- One runtime material; Base Color, Normal, ORM; no emissive; metallic `0`.
- Source-owned Base Color texels are byte-exact; top contact witness RGB
  mismatch count `0`; no grading.
- LOD0 `4000-10000` triangles; LOD1-LOD3 strictly decrease; two UV sets; four
  custom collision hulls; Blender source; four FBXs; clean FBX re-import.
- Final review shows the plinth and complete replacement base with no clipping,
  underside view, collision, or proxy geometry.

## Artifact Boundary

- A04 package and base remain `quarantined` / `invalid as A05 construction
  authority`.
- A04 plinth remains `authoritative visual reference`.
- A05 internal attempts are `quarantined` or `proof only`.
- A passing final A05 package is a `candidate` and at most a
  `DCC game-ready candidate` pending Flamestrike visual approval.
- Preserve all A01-A04 files. Use only A05 output paths.
- Unreal/Step 17, `Fully game-ready`, approved-library, and visual-canon
  promotion remain forbidden.

## Decision Output

End as exactly one of:

- `candidate`: all A05 technical and visual gates pass and the exact final
  A05 image is pending Flamestrike review;
- `blocked`: a required gate cannot be met; or
- `quarantined`: an internal attempt fails and remains non-authority.
