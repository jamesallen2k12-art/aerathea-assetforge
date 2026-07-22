# A12 R4 Side-Owner Strike-Face Output Record

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract: `SB-AXIAL-A12-R4-SIDE-OWNER-FACES`
- Date: `2026-07-22`
- Artifact status: `quarantined after Flamestrike identified whole-assembly registration defects`
- Technical evidence status: `proof only`
- Unreal authority: `false`
- Fully game-ready: `false`

## Result

R4 preserves the approved A09/A11 frame and the R3 `24:14:14`
core/stone/stone split, while replacing only the warped outward strike-face
solution. The `+X` face is one continuous row-connected mesh reconstructed
from the exact right-view scan; its geometry is mirrored at `X=0` for the
`-X` face. Each outward face retains the exact original source pixels owned by
its side:

- `-X`: `siege_breaker_left_view.png`;
- `+X`: `siege_breaker_right_view.png`.

The side-source sheet background is removed by exact scan membership and
exterior flood-fill only. No painted or generated replacement pixels are used.
The superseded projected wall is recessed only far enough to prevent it from
occluding the new owner faces.

## Technical Evidence

- candidate mesh objects: `3`;
- vertices: `520818`;
- polygons: `520808`;
- evaluated bounds:
  `75.130516052 x 44.299175262 x 170.000000000 cm`;
- owner-face Z interval: `111.089111328..170.000000000 cm`;
- exact side membership: left `118540 px`, right `116948 px`;
- missing mirrored vertices: `0` for all three candidate components;
- recessed legacy-wall vertices: `5472`;
- maximum legacy stone-wall `|X|`: `35.882087708 cm`;
- deepest visible owner relief `|X|`: `37.115256526 cm`;
- independent audit: `pass 37/37`;
- A09 source hash after build: unchanged at
  `06ffb121d00cddb7b9e30a60067a5036a851d285f15daca3bffe3a663fd6d78f`;
- image generation: `false`;
- TRELLIS/image-to-3D: `false`;
- Unreal/export/LOD/collision work: `false`.

## Internal Recovery

R4A, R4B, and R4C were rejected internally and quarantined before presentation:

- R4A used nonlinear per-row UV normalization and expanded the envelope;
- R4B restored the exact envelope but exposed source-background corners and
  raster-cell seams;
- R4C produced a continuous masked face and passed `36/36`, but close review
  found legacy-wall vertices occluding owner pixels around the rune plate.

Their hashes and recovery boundaries are recorded in
`manifests/A12_INTERNAL_REJECTIONS.md`. The presented R4 result is the bounded
R4D correction: only the already-authorized legacy-wall recess changed after
R4C.

## Hash Locks

- builder:
  `1a8128c0f78cd920f6f53eed4ac064294c465c596039e32b92f97a6861651731`;
- independent auditor:
  `f476e8b0bed327e869ce5fb12efae25b2d80a886c52e80acc1621b99994537a4`;
- R4 contract:
  `ae1179b5e4e58cd86b473d363b8808b3814e3d0b106d4307ff570149bda4feb6`;
- local Blender candidate:
  `d44778864febf225019ba2a256ae22af87d8fc091ed2fc515b1ab0010c9fff96`;
- review board:
  `eb0b41930a012ef014e2962daef697d5733942cc231b22b8775dbb24a77a7520`;
- colored three-quarter:
  `9e053ae4a72410d7160a8281142963b7c35ff7dae575370e666563f88917a374`;
- gray geometry three-quarter:
  `913a953212c97e96b8c68136f9ff107afb1b50446c05d351a8dc8b87e649c511`;
- `-X` owner face:
  `4cc052091778d7cc0a239baab6727a9394ef1e87f3c0d0c734c4f13f67d4c5ec`;
- `+X` owner face:
  `0f89602c93467a6800082eea0346797dbdb5f1e5dde8cfa8ff59533654ed0ca4`;
- validation:
  `beeb035e780a65a7af1461888ecefe4e227219b0844ec9bef6ab62dda98021fa`;
- independent audit:
  `cea705dbe7407ee2fd7ebf1205cb8b5cc0d280a5abc4293d4d4ecb0c4aa1c559`.

## Visual Gate

Technical audit success does not approve visual fidelity. The review board,
completed colored three-quarter render, gray geometry proof, and both exact
side-owner views must be shown visibly. Flamestrike alone may classify R4 as
`approved`, `revise`, `rejected`, or `blocked`.

Flamestrike subsequently identified two differently scaled handle facets,
residual rock between the apparent haft surfaces, and handle misalignment. R4D
is therefore `quarantined` as a complete visual candidate. Its strike-face and
measurement evidence may be referenced, but its mesh is forbidden as R5
construction geometry. R5 supersedes this gate.
