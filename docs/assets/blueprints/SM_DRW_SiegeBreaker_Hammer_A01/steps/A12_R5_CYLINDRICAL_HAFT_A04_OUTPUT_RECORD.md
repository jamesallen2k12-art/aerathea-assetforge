# A12 R5 Cylindrical Haft A04 Output Record

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract: `SB-AXIAL-A12-R5-FOUR-VIEW-WHOLE-ASSEMBLY`
- Date: `2026-07-22`
- Artifact status: `DCC source candidate pending Flamestrike visual decision`
- Unreal authority: `false`
- Fully game-ready: `false`

## Result

A04 preserves the approved fresh four-view registration and constructs the
complete hammer as one `X>=0` half followed by the exact `X=0` mirror. The haft
is no longer a front/back slab extrusion. It is a separate true circular,
profiled Blender cylinder from `Z=30.0..109.25 cm`, with the endpoint locked to
the last row jointly owned by the front and back haft sources.

The cylinder uses:

- `519` measured profile rings and `32` full angular segments;
- front-positive-half source radius in both X and Y;
- exact center axis `X=0,Y=0`;
- `Front_Material` on the front `180 degrees`;
- `Back_Material` on the back `180 degrees`;
- one static `UVMap` with each material island spanning exact `U=0..1` and
  `V=0..1`;
- deterministic nearest-pixel source strips widened by the declared `1.5708`
  factor;
- zero Generated, Object, Mapping, or Tube procedural coordinate nodes.

The complete two-object candidate has `376814` vertices, `376840` polygons,
and evaluated bounds `74.977501 x 33.132968 x 170.000000 cm`. Its Z frame is
exactly `0..170 cm`, its object transforms are identity, and the cylinder has
zero missing X-mirrored vertices.

## Validation

- Builder validation: source hashes, membership counts, measured shaft axes,
  deterministic texture derivation, separate material ownership, fixed UV
  ranges, geometry counts, bounds, proof hashes, and prohibited-software
  boundary recorded.
- Independent audit: `pass 45/45`; artifact status `proof only`.
- Geometry proof: independently flat-material, with source color excluded.
- Image generation: `false`.
- TRELLIS/image-to-3D: `false`.
- FBX export: not executed.
- Unreal: not executed.

## Hash Locks

- Blender source:
  `085f5b5d873f73c9611f01a90d10dca7768968f4648fb58061d928dd75ea16ec`;
- validation:
  `a10e344644c6d5b676c4c04620c0691fb9027cdac04d40ce3ec800319d1d0c07`;
- independent audit:
  `b6f16364febdd0a35cf61e96f6c36512c094f1599022781ea035bac8bfa03323`;
- review board:
  `2b00b55d28aecbbee5d96e9a6eec5d694139f64c0cbc015f450b1ad05c1dc79f`;
- colored three-quarter proof:
  `902507e5347edf76c2500f50c0942d79c404f30f1911ee4b5bd4390b7a509d13`;
- gray geometry proof:
  `89021d60e98a3b8dce4395a265c9c736b1dfeb5ab2399fef103189fab5e7de24`.

## Current Gate

Technical result: `pass`. This does not grant artistic approval. Flamestrike
must approve, reject, or request revision of the exact visible A04 review board
before any FBX, Unreal, LOD, collision, game-ready, or other production step.
