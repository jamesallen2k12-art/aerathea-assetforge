# A12 R10 R8 Pixel-Exact Steps 01-16 Final Approval Handoff

- Date: `2026-07-23`
- Run: `SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01`
- Status:
  `invalid / quarantined after Flamestrike visual and method rejection`
- Superseding recovery handoff:
  `A12_R10_R8_ZERO_EXTRUSION_RESET_HANDOFF.md`
- Final review:
  `proof_runs/SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01/review/STEP_16_FINAL/STEP_16_R8_PIXEL_EXACT_TWO_HAMMER_FINAL_REVIEW.png`
- Final review SHA-256:
  `49c787696eefba99a38498b7181342124d0402f48cbac8932c838b77eefc0bfe`

> Flamestrike rejected this image because the reconstruction is an extrusion.
> The documented successful process contains zero extrusions. Every statement
> below that classifies Steps 10-16 as passing or candidate-ready is superseded
> and retained only as defect-history evidence.

## Candidate A

- Source: rune-side right-image half `[557,668)`.
- Completion: one exact `Rz180`.
- Bounds:
  `97.873941674506 x 34.434306569343 x 170.000000000000 cm`.
- LOD0:
  `7,924` triangles.

## Candidate B

- Source: metal-center-piece right-image half `[418,557)`.
- Completion: one exact `Rz180`.
- Bounds:
  `97.873941674506 x 43.120437956204 x 170.000000000000 cm`.
- LOD0:
  `7,888` triangles.

## Technical Decision

- Steps 01-16:
  `PASS`.
- Independent final saved-file audit:
  `66/66 PASS`.
- No horizontal/vertical image stretch:
  `PASS`.
- One uniform scale per complete view:
  `PASS`.
- Exact right-image axis `x=557`:
  `PASS`.
- Unequal half spans retained:
  `PASS`.
- Exact cylinder formula and `pi/2` factor:
  `PASS`.
- LOD0-LOD3, collision, FBX, GLB, and clean FBX reimport:
  `PASS`.
- Unreal authority:
  `false`.

## Flamestrike Decision

`select Hammer A / select Hammer B / revise / reject / blocked`
