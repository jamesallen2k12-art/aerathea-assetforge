# A005 Step 14 UV, Base Color, And Material Plan Review

Status: approved; authoritative planning package complete; mandatory restart required

Artifact classification: `authoritative Step 14 planning review`

Contract ID: `A005-CR-STEP14-UV-BASECOLOR-MATERIAL-PLAN-A01`

Candidate SHA-256:
`5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095`

## Decision

`approved`

The Step 14 package is approved as the execution authority for a later Step 15
UV and texture/material candidate. It defines how evidence and interpretation
must be separated without creating a UV layer, image map, bake, material, or
modified Blender file.

The asset remains a `DCC source candidate`. It is not DCC game-ready, fully
game-ready, finished appearance, or visual canon.

## Exact Evidence Versus Interpretation

| Consumer | Exact evidence | Approved interpretation |
|---|---|---|
| Base Color mip 0 | Mask-owned native RGB bytes from front, back, left, right, or top | source matte, UV placement, unowned/hidden continuation, dilation |
| UV0 | approved face/component lineage and normal-owner rules | seams, islands, packing, source-window placement |
| UV1 | four-shell lineage | non-overlap layout, 128 lightmap resolution, four-texel padding |
| Normal | no exact normal data exists | grain, chips, course divisions, shallow red incision |
| ORM | no exact AO/roughness/metallic data exists | bounded AO bake, roughness ranges, metallic zero |
| Mips/filtering | exactness applies only to owned mip-0 RGB texels | all lower mips and rendered filtering are derived consumer behavior |
| Emissive | source proves red appearance only | emissive is rejected and absent |

No physical source-to-target transform, unified pixel scale, cross-panel pixel
pair, or source-authored seam is claimed.

## UV Ownership

UV0 is one unique non-overlapping 0-1 layout with one material slot. Visible
faces route by approved dominant-normal ownership:

| Face owner | View | Atlas window (half-open pixels) | Size |
|---|---|---:|---:|
| `-Y` | front | `[16,16,499,541]` | `483 x 525` |
| `+Y` | back | `[531,16,1053,417]` | `522 x 401` |
| `-X` | left | `[1085,16,1569,417]` | `484 x 401` |
| `+X` | right | `[1601,16,1968,388]` | `367 x 372` |
| `+Z` | top | `[16,573,353,944]` | `337 x 371` |

Perspective remains non-metric corroboration and owns no texels. Hidden
closures, contact-overlap faces, the underside, and source-unowned transitions
route to the authored stone zone `[16,976,2032,2032]`.

Every component boundary, hidden-contact loop, and source-owner transition is
a UV seam. These are production seams only. Minimum mip-0 island dilation is
16 pixels and independent source windows remain at least 32 pixels apart.

## Base Color Ownership

Step 15 must derive five deterministic native-resolution owner masks. An owned
atlas texel copies the matching source-panel RGB triplet at the same integer
panel coordinate plus its fixed atlas offset. Tolerance is zero; resizing,
warping, interpolation, grading, and baked AO in Base Color are forbidden.

The mask method is an approved interpretation:

- paper color is the per-channel median of the outer eight-pixel panel border;
- foreground seeds differ by at least 24 in any channel or satisfy the exact
  red predicate;
- seeds intersect depth-tested coverage for the approved face owner, with only
  a one-pixel antialias-fringe growth;
- tiny isolated components are rejected by the declared connectivity rule;
- manual mask pixel correction is forbidden.

If that deterministic rule includes annotations/grid or excludes material
pixels, Step 15 blocks. It may not silently hand-correct the matte.

All other Base Color texels are authored interpretation. Visible transition
areas use a component-local eight-color stone palette derived from owned
non-red source pixels. Hidden contacts and the underside use bounded flat dark
stone continuation. Red motifs are forbidden in all source-unseen regions.

## C-005 / C-006 / C-007

The three semantic IDs remain separate, but they share one bounded material
consumer rule:

- face-owned exact red Base Color at owned source pixels;
- one shallow `0.15 cm` pigment-filled normal incision with `0.05 cm` bevel;
- pigment roughness nominal `0.64`, bounded to `0.55-0.75`;
- metallic `0`;
- no displacement, silhouette control, cross-face copy, hidden continuation,
  cross-view physical identity, or emissive.

## Texture And Material Package

| Map | Resolution | Color space | Meaning |
|---|---:|---|---|
| `T_GIA_BloodAxeCairnstone_A005_BC` | `2048 x 2048` | sRGB | exact owned RGB plus labeled authored continuation |
| `T_GIA_BloodAxeCairnstone_A005_N` | `2048 x 2048` | linear | DirectX/Unreal tangent normal |
| `T_GIA_BloodAxeCairnstone_A005_ORM` | `2048 x 2048` | linear | R=AO, G=Roughness, B=Metallic |

Material: one opaque, one-sided, Default Lit
`M_GIA_BloodAxeCairnstone_A005` slot. The metallic channel must be zero at
every texel. AO never multiplies into Base Color. The reserved emissive name
`T_GIA_BloodAxeCairnstone_A005_E` must not be created.

## Bake, Mip, And Filtering Boundary

- Base Color is not baked.
- Normal is DirectX tangent space; AO uses 256 samples, 12 cm distance, 0.2 cm
  cage extrusion, and 16-pixel margin from the unchanged approved geometry.
- Source ingestion and exactness audit use point sampling at integer texel
  centers.
- Lower Base Color mips are linear-light box-filter derivatives; normal mips
  are vector-averaged and renormalized; ORM mips are channel averages with
  metallic forced to zero.
- Preview/runtime filtering may be trilinear with 8x anisotropy only after
  mip-0 exactness passes. No rendered-pixel exactness is claimed.

## Step 15 Acceptance Surface

The future Step 15 contract must pass all 18 gates in
`STEP_14_TEXTURE_DELIVERY_AND_VALIDATION_PLAN.json`, including unchanged
geometry, UV overlap/bounds/padding, five native mask reviews, byte-exact
owned RGB, authored-texel labeling, Normal/ORM/bake correctness, non-emissive
material setup, and six clean material proof views.

## Zero-Production Result

- UV layers created: `0`
- texture/source-mask files created: `0`
- materials or bakes created: `0`
- Blender saves: `0`
- geometry, LOD, collision, FBX, Unreal, and visual-canon changes: `0`

## Next Gate

Mandatory restart. After restart, only preparation of a separate Step 15 UV
and Texture/Material Candidate contract is permitted. Step 15 execution is not
authorized by this review.
