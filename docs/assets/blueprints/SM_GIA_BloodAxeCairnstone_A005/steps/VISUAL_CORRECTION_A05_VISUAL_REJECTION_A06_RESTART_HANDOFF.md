# A005 A05 Visual Rejection / A06 Restart Handoff

Status: `Core Recovery save point complete; A05 rejected; A06 outer-edge remeasurement pending resume`

Artifact classification: `authoritative`

Date: 2026-07-21

Finalized recovery checkpoint:
`Saved/ProjectRecovery/20260721-080648/`

Checkpoint note: `A005 A05 rejection fully recorded; A06 exterior-edge
measurement-only restart boundary active`

## Resume Goal

Correct the dimensions of the two structural base pieces while preserving the
exact A04 plinth. A06 must measure the actual exterior edges of C002 and C003;
it must not treat internal alignment/contact pixels as their outer bounds.

## Flamestrike Decision And Exact Guidance

A05 is not approved. Flamestrike stated:

> This is better ... I still cant approve this the geometry is closer and the
> stonework appearance better but the dimensions of the 2 base pieces are
> incorrect ... I believe the measurements were possibly derived from the
> distance between the alignment pixels ... but this is not the same as the
> width of the actual bases themselves ... as the alignment pixels are within
> the geometry of the 2 bases but is not placed at the edges of those bases
> ... create a save point with this information so we can try again

## Controlling Truths

- The authoritative source image remains unchanged.
- The exact A04 plinth remains an `authoritative visual reference`.
- A05 is visibly closer and its stonework appearance is improved, but neither
  observation approves its base dimensions or complete appearance.
- The A05 values `119.097222 x 77.647059 cm` for C002 and
  `134.652778 x 96.561086 cm` for C003 were derived from source spans that
  were accepted as outer footprint endpoints without proving that their
  alignment pixels lie on the exterior edges.
- Flamestrike has clarified that the alignment pixels lie within the two base
  pieces, not at their exterior edges. Those values are therefore invalid as
  A06 footprint authority.
- A05's `18/18` result remains `proof only` for topology, bounds, LODs,
  collision, package integrity, source-owned atlas bytes, and exact A04 plinth
  preservation. Its footprint and visual-equivalence implications are
  invalid and superseded.

## Artifact Classification

- Source image and explicit source specifications: `authoritative`.
- Exact A04 plinth geometry/UV result: `authoritative visual reference`.
- Complete A05 Blender/FBX/texture/render package: `quarantined`.
- A05 base geometry and C002/C003 dimensions: `invalid as A06 construction
  authority`.
- A05 stonework treatment: `reference only`; improved but not approved.
- A05 measurement audit: raw pixel samples are `proof only`; its derived
  C002/C003 physical footprints and ready-for-build decision are `invalid and
  superseded`.
- A05 validation: `proof only`; G06, G07, G16, and the overall visual-candidate
  conclusion are invalid as approval evidence.

## Required First Action After Resume

Perform an A06 measurement-only exterior-edge audit before any geometry:

1. Reopen the authoritative front, left, and top source panels.
2. Classify every relevant pixel witness as one of: exterior silhouette edge,
   internal alignment/contact, occlusion boundary, shadow/material boundary,
   or unknown.
3. Measure C002 and C003 only between verified exterior silhouette edges.
4. Keep internal alignment/contact spans as separate evidence; never promote
   them to footprint width or depth.
5. Cross-check exterior endpoints across multiple rows and useful views.
6. If an exterior edge is occluded or cannot be distinguished, report
   `Blueprint block: source authority missing`; do not infer a closed extent.
7. Produce a measurement-only approval/blocked decision before an A06 build
   contract or candidate geometry is created.

No candidate fill, inferred contour, new geometry, UV adjustment, color
grading, Unreal work, or Step 17 work is authorized by this handoff.

## Resume Read Order

1. `SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md`
2. this handoff
3. `review/VISUAL_CORRECTION_A05_FINAL_REVIEW.md`
4. `manifests/VISUAL_CORRECTION_A05_MEASUREMENT_AUDIT.json` as quarantined
   evidence, observing its supersession labels
5. the authoritative source panels and relevant Step 11/14 records

## Next Decision Gate

End the first A06 action as exactly one of:

- `authoritative exterior-edge measurement record ready for A06 contract`; or
- `Blueprint block: source authority missing`, identifying the unproven outer
  edge and the smallest proposed rule needed for approval.
