# A005 Visual Correction A05 Output Record

Status: `technical pass retained as proof only; visually rejected and quarantined`

Artifact classification: `authoritative technical result record`

Date: 2026-07-21

Contract ID: `A005-CR-VISUAL-CORRECTION-A05`

## Result

The A05 correction replaced the rejected A04 base with three newly constructed
oval cairn components while preserving the exact approved A04 plinth. The
candidate passed the independent technical and render audit at `18/18` with
zero failures.

At technical closeout, artifact status was `candidate` and pipeline status was
`DCC game-ready candidate`. That state is superseded by the visible rejection
below. Unreal, Step 17, `Fully game-ready`, approved-library, and visual-canon
promotion remained unauthorized and false.

## Superseding Flamestrike Visual Decision

Rejected on 2026-07-21. The geometry is closer and stonework appearance is
better, but the C002/C003 dimensions are incorrect. A05 treated distances
between internal alignment pixels as the physical widths/depths of the two
base pieces even though those pixels do not sit on the exterior edges.

The complete A05 package is `quarantined`. Its technical audit remains `proof
only`; the C002/C003 physical footprints, G06/G07/G16 implications, and visual
candidate conclusion are `invalid and superseded`. The exact A04 plinth
remains an `authoritative visual reference`; A05 stonework is `reference only`.

## Corrective Construction

- C001: exact A04 plinth geometry and UV signature preserved.
- C002 upper course: A05-derived oval footprint
  `119.097222 x 77.647059 cm`; now invalid as outer-footprint authority.
- C003 lower course: A05-derived oval footprint
  `134.652778 x 96.561086 cm`; now invalid as outer-footprint authority.
- C004 apron: oval footprint `140 x 110 cm`, rebuilt as irregular peripheral
  rubble with varied block widths, recessed joints, and uneven crowns.
- Overall bounds: exact `140 x 110 x 220 cm`; pivot `[0,0,0]`.
- A04 base geometry retained or hidden in A05: `0`.
- Color grading: `0`; source-owned RGB pixels compared: `154948`; mismatches:
  `0`.

## Technical Package

- Blender SHA-256:
  `bfb1a771a2234379d71f8905d04084af1434644fbbf572d8cc1ede6b3bf8eb39`.
- LOD triangles: `8704 / 4002 / 1826 / 696`.
- Primary shells: `4`; boundary, non-manifold, and degenerate failures: `0`.
- UV layers: `UVMap` and `LightmapUV` on all LODs.
- Runtime materials: `1`; collision hulls: `4`.
- Clean FBX re-import: `4/4`.
- Exact A04 plinth geometry SHA-256 in A04 and A05:
  `54ceeba198e8563ea9f92beb0dbdd8f6b22e0ea38fb99591ed0f3b435cc37721`.
- Exact A04 plinth UV SHA-256 in A04 and A05:
  `5633bc68f1a29728764b283fb7b84b6df0d6bc3ec79892a35b6096304298104b`.
- Unreal outputs: `0`.

## Final Review Artifact

`Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A05/SM_GIA_BloodAxeCairnstone_A005_FINAL_CORRECTED_3D_A05.png`

SHA-256:
`5175ffb7c0c1bd5d66f8b1ede17ebc489ab77ade3c5667ac35c3bc3d101bef56`

The final image was internally inspected, passed all render-dependent gates,
and was opened in a visible desktop window. No internal attempt is approval
authority.

## Internal Attempt Disposition

- Attempt01: `quarantined`; corrected proportions but smooth dark apron/skirt.
- Attempt02: `quarantined`; flat gray skirt and weak local material response.
- Attempt03: `quarantined`; oval but gear-like scalloped apron and uniform
  course cadence.
- Attempt04: `proof only`; first acceptable base read, held when the pre-audit
  found an A04 plinth UV-equivalence mismatch.
- Final A05: `quarantined` after visible rejection; component-owned UV repair
  and exact plinth-equivalence audit remain `proof only`.

## Stop Boundary

Flamestrike rejected the exact A05 image identified above. The next bounded
action after resume is the A06 exterior-edge measurement-only gate recorded in
`VISUAL_CORRECTION_A05_VISUAL_REJECTION_A06_RESTART_HANDOFF.md`. No A06
geometry or downstream production action is authorized by this save point.
