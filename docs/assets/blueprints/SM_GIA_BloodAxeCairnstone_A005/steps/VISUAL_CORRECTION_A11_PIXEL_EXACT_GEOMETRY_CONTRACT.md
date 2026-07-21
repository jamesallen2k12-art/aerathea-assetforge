# A005 Visual Correction A11 Pixel-Exact Geometry Contract

Status: `approved active execution contract`

Artifact classification: `authoritative contract`

Date: 2026-07-21

Contract ID: `A005-CR-VISUAL-CORRECTION-A11`

## Goal

Correct the A005 base geometry using the approved A10 pixel-exact component
ratios, retain the exact A04 C001 monolith, and stop at one audited DCC review
image for Flamestrike.

## Execution Authority

Flamestrike resumed the asset on 2026-07-21 and granted full authority and
approval to do what is needed to correct the 3D image. This contract converts
that instruction into the bounded A11 production step below.

## Evidence Authority

- Sole visual source:
  `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`,
  SHA-256 `4b953abb87f5f254a5f51c6214e76d3f72c4fc55bc2fa4e4d605b2440d6e53c2`.
- A10 approved measurement:
  `manifests/VISUAL_CORRECTION_A10_PIXEL_EXACT_BASE_RECONCILIATION.json`,
  SHA-256 `09452319172cdca60f024e106e20eef52a5567eac04e0f2fda73985370b3e156`.
- Exact A04 C001 geometry and UVs remain the monolith construction authority.
- A08 top-stone record remains authority only for the source-visible stone
  counts and angular ordering used to reconstruct C002/C003/C004.

## Approved Visible Geometry

Conditional on retaining the authoritative `140 x 110 cm` C004 production
envelope, A11 must use these A10 footprints:

- C001 contact: `94.305556 x 57.239819 cm`.
- C002 exterior: `118.611111 x 77.149321 cm`.
- C003 exterior: `134.166667 x 96.063348 cm`.
- C004 exterior: `140 x 110 cm`.

C002, C003, and C004 are rebuilt fresh. No A09 assembled course geometry is
an input. The exact A04 C001 component is preserved.

## Bounded Construction Decisions

The following are approved construction interpretations under Flamestrike's
A11 execution authority. They are not reclassified as source evidence.

- C002 visible Z interval: `23.00-34.25 cm`, height `11.25 cm`. This lies
  inside A10's approved `8.235294-11.666667 cm` height interval.
- C003 visible Z interval: `9.75-22.25 cm`, retaining the existing `0.75 cm`
  visible separation from C002.
- C004 visible Z interval: `0.00-9.00 cm`, retaining the existing `0.75 cm`
  visible separation from C003.
- C002 inner construction contour: `92.305556 x 55.239819 cm`, providing
  `1 cm` radial C001 overlap on every side of the A10 contact footprint.
- C003 inner construction contour: `116.611111 x 75.149321 cm`, providing
  `1 cm` radial overlap on every side of the A10 C002 exterior.
- Hidden receiver contours stay fully inset behind measured visible
  silhouettes and overlap all three interfaces. They may close source-hidden
  space only; they may not alter a visible exterior maximum.
- Hidden receiver top loops are closed against the approved owner-view pitch;
  the C004 receiver is vertically limited to `7.75-10.00 cm` behind the
  C003/C004 contact so it cannot become a visible lower skirt.
- Exposed horizontal base-transition faces use source-owned C002/C003/C004
  stone bands from the verified front panel. This is UV placement on existing
  unmodified source texels, not color grading or source mutation.
- All source-hidden receiver faces use the same bounded source-owned
  C002/C003/C004 stone bands, selected by Z level, so no receiver face can
  sample source-background pixels. Receiver closure remains explicitly
  interpreted construction, not measured source geometry.
- The 48 A10 top contacts remain evidence points. A11 does not claim that its
  hidden contour closures were measured from the source.

## Required Outputs And Gates

1. A11 Blender source, assembled LOD0-LOD3 FBXs, component FBXs, textures,
   manifest, internal proofs, one final source-oriented image, and independent
   validation.
2. Exact A10 C002/C003/C004 exterior dimensions and exact `140 x 110 x 220
   cm` overall bounds.
3. Exact A04 C001 geometry and UV signatures.
4. C002 height inside the approved interval.
5. Source-owned RGB mismatches `0`; no compensating color grade.
6. Zero camera-visible background leaks at declared interfaces.
7. LOD0 inside `4000-10000` triangles, descending LODs, four collision
   proxies, UV0 plus LightmapUV, and clean FBX re-import.
8. One final image opened visibly only after all technical and internal visual
   gates pass.

## Stop Boundary

Stop at one A11 `candidate` / `DCC game-ready candidate` image pending
Flamestrike visual approval. Unreal, Step 17, `Fully game-ready`, visual-canon
promotion, and approved-library promotion remain forbidden.
