# A12 R6 A04 Front-Half Depth-Mirror Contract

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Parent contract: `SB-AXIAL-A12-R6-SINGLE-CLOSED-HALF`
- Supersedes: `SB-AXIAL-A12-R6-A03-FRONT-HALF-ROTATE180`
- Contract ID: `SB-AXIAL-A12-R6-A04-FRONT-HALF-DEPTH-MIRROR`
- Date: `2026-07-22`
- Status: `historical transform authority; execution stopped after A01 visual failure`
- Artifact ceiling: `DCC source candidate pending Flamestrike visual decision`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Flamestrike Decision

Flamestrike approved correcting the A03 duplicate operation to the proper
front/back axis. In the locked Blender frame, `X` is left/right, `Y` is
front/back, and `Z` is vertical. The required duplicate is therefore the exact
depth reflection `(X,Y,Z) -> (X,-Y,Z)` across `Y=0`. This moves the front
physical half to the back while preserving left/right and top/bottom.

A second rigid `180-degree` rotation is not applied: rotation about X would
invert top/bottom, and rotation about Z would swap left/right. The approved
result is the exact depth-mirror equivalent of copying the completed front
half to the back and orienting its exterior outward.

## Exact Construction

1. Start from the six immutable source files and locked R6 measurements in a
   fresh Blender scene. No R5 or prior R6 geometry, UV, material, texture,
   composite, or Blender data is an input.
2. Construct one coherent physical front half occupying `Y<=0`, with its open
   center boundary exactly on `Y=0`.
3. Derive its X silhouette from the front source's positive-X pixels mirrored
   around `X=0` inside that front half. Use registered right-view front-depth
   pixels for its Y extent. Preserve the integrated circular-haft rule.
4. Omit all `Y=0` closure faces. Before duplication, every open edge must lie
   on `Y=0` and every other edge must have exactly two incident faces.
5. Duplicate that exact half, apply the depth reflection
   `(X,Y,Z) -> (X,-Y,Z)`, recalculate outward normals, join, and weld the
   corresponding `Y=0` boundary vertices.
6. The back geometry and appearance are the mirrored front half. The
   independent back orthographic remains `reference only` and may not rescale,
   intersect, deform, overlay, or texture the result.

## Static UV And Seam Rule

- Use static `UVMap` coordinates only.
- Front- and back-facing exterior surfaces both sample verified front-source
  pixels under the depth-mirror correspondence.
- The complete `+X` strike face uses the right source. Its mirrored halves use
  `Ysample=-abs(Yworld)` with one shared Z registration.
- The complete `-X` strike face uses the left source. Because that source's
  horizontal screen axis is reversed, its mirrored halves use
  `Ysample=+abs(Yworld)` with one shared Z registration.
- Matching polygons on both sides of `Y=0` must resolve to the same source
  coordinate at the seam.
- Every UV must resolve to an exact selected object pixel. White source
  background, derived composites, painted seams, overlays, procedural
  coordinate nodes, and independent half-height normalization are forbidden.

## Fail-Closed Gates

Before any colored review is valid, prove:

- one front source half exists before duplication;
- all pre-mirror open edges lie on `Y=0`, with no four-face edge;
- duplicate transform is exactly `(X,Y,Z) -> (X,-Y,Z)` with no offset;
- normals are outward after the negative-determinant transform is applied;
- after join/weld, every edge has exactly two incident faces;
- internal `Y=0` faces: `0`;
- duplicate or coplanar exterior faces: `0`;
- missing depth-mirrored vertices: `0`;
- source-background UV samples: `0`;
- +X and -X strike-face UV discontinuities at `Y=0`: `0`;
- colored and flat-gray proofs are materially independent.

Any failure makes the attempt `invalid` and stops production. A technical
pass does not grant visual approval.

## Required Review

- standalone high-resolution colored complete three-quarter view emphasizing
  the `+X` strike face;
- independent flat-gray view from the identical camera;
- front, back-as-depth-mirrored-front, left, and right comparisons;
- validation manifest, independent audit, and one visible review board;
- stop for Flamestrike approval, revision, rejection, or blocked decision.

## Explicit Exclusions

- no A03 Z-axis rotation;
- no X-axis rotation or vertical inversion;
- no independent back-source geometry, scale, or UV ownership;
- no prior candidate repair-forward or construction input;
- no image generation, TRELLIS, diffusion, generated view, or image-to-3D;
- no FBX, Unreal, LOD, collision, packaging, or game-ready escalation;
- no technical or visual self-approval.

## A01 Visual Failure And Recovery Boundary

Flamestrike found that the A12 haft cylinders do not connect visibly, the
vertical design is misaligned, and the collar below the head lacks correct
pixel ownership. Inspection proved the mesh is one connected closed component,
but the UV rule mixed front, left, and right source owners around the haft and
collar. A01 is invalid/quarantined. Do not execute A04 again or repair its saved
blend. Further Blender authority requires approval of
`A12_R6_A05_HAFT_COLLAR_CYLINDRICAL_UV_RECOVERY_CONTRACT.md`.
