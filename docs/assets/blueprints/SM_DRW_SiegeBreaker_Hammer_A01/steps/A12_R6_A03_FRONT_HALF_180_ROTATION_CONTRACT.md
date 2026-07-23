# A12 R6 A03 Front-Half 180-Degree Rotation Contract

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Parent contract: `SB-AXIAL-A12-R6-SINGLE-CLOSED-HALF`
- Contract ID: `SB-AXIAL-A12-R6-A03-FRONT-HALF-ROTATE180`
- Date: `2026-07-22`
- Status: `reference only; superseded after internal attempts by A04 depth mirror`
- Artifact ceiling: `DCC source candidate pending Flamestrike visual decision`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Flamestrike Decision

Flamestrike approved replacing the unexecuted A02 one-pixel reconciliation and
the prior X-half/front-back-intersection method with one complete front
physical half duplicated by an exact `180-degree` rotation around the handle
axis. The objective is one mechanically continuous asset with no independently
scaled front/back seam.

## Exact Construction

1. Start from the six immutable source files and their locked measurements in
   a fresh Blender scene. No R5 geometry, UV, material, texture, composite, or
   Blender data is an input.
2. Construct one coherent physical front half occupying `Y<=0`. Its center
   boundary is the exact `Y=0` plane.
3. Derive the front half's X silhouette from the front source's positive-X
   pixels and mirror those pixels inside the front half around `X=0`. This
   guarantees that its `Y=0` weld loop is exactly invariant under the approved
   rotation.
4. Use the registered right-view front-depth pixels to constrain only the
   front half's Y extent. Preserve the approved circular haft rule as a
   front semicylinder integrated into the same boundary volume.
5. Omit all `Y=0` closure faces. The source half must be manifold except for
   its declared `Y=0` boundary before duplication.
6. Duplicate the complete front half exactly, rotate the duplicate
   `180 degrees` about world Z through the registered handle axis, apply that
   transform, join, and weld corresponding `Y=0` vertices.
7. The back geometry and appearance are the rotated front half. The separate
   back orthographic is `reference only` in A03 and may not rescale, intersect,
   deform, overlay, or texture the result.

## Static UV And Seam Rule

- Use static `UVMap` coordinates only.
- Front- and back-facing exterior surfaces both sample the same verified front
  source pixels under the exact rotation correspondence.
- The complete `+X` strike face uses one continuous right-source world-Y/Z
  mapping across `Y=0`; the complete `-X` strike face uses one continuous
  left-source world-Y/Z mapping across `Y=0`.
- Matching polygons on both sides of the weld must resolve to the same source
  coordinates at the seam.
- UV samples must be clamped to exact selected object pixels. White source
  background may not be sampled by any exterior face.
- No derived composite image, painted seam, texture overlay, procedural
  coordinate node, or independent half-height normalization is allowed.

## Fail-Closed Gates

Before any colored review is valid, prove:

- one front source half exists before duplication;
- all pre-rotation open edges lie on `Y=0` and every other edge has two faces;
- pre-rotation four-face or higher-incidence edges: `0`;
- duplicate transform is exactly `Rz(180 degrees)` with no scale or offset;
- after join/weld, every edge has exactly two incident faces;
- internal `Y=0` faces: `0`;
- duplicate or coplanar exterior faces: `0`;
- missing rotated vertices: `0`;
- source-background UV samples: `0`;
- +X and -X strike-face UV discontinuities at `Y=0`: `0`;
- colored and flat-gray proofs are materially independent.

Any failure makes the attempt `invalid` and stops production. A technical pass
does not grant visual approval.

## Required Review

- standalone high-resolution colored complete three-quarter view emphasizing
  the `+X` strike face;
- independent flat-gray view from the identical camera;
- front, back-as-rotated-front, left, and right comparisons;
- validation manifest, independent audit, and one visible review board;
- stop for Flamestrike approval, revision, rejection, or blocked decision.

## Explicit Exclusions

- no A02 pixel insertion;
- no independent back-source ownership;
- no R5 repair-forward or construction input;
- no image generation, TRELLIS, diffusion, generated view, or image-to-3D;
- no FBX, Unreal, LOD, collision, packaging, or game-ready escalation;
- no technical or visual self-approval.

## Superseding Decision

Flamestrike subsequently approved correcting the duplicate operation to the
proper front/back axis. A03 is preserved as method and defect evidence but is
no longer execution authority. Continue only through
`A12_R6_A04_FRONT_HALF_DEPTH_MIRROR_CONTRACT.md`.
