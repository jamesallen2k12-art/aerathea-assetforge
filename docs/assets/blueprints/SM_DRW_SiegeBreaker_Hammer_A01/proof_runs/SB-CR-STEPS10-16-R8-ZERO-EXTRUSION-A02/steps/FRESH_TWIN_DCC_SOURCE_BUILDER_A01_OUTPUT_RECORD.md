# Fresh Twin DCC Source Builder A01 Output Record

- Date: `2026-07-24`
- Build ID: `FRESH_TWIN_DCC_SOURCE_BUILDER_A01`
- Governing blueprint: `SHARED_DEPTH_RECOVERY_BLUEPRINT_A01`
- Approved scope: two fresh twin DCC source candidates and review evidence
- Build result: `PASS`
- Independent saved-file and cross-asset audit: `PASS`
- Current asset status: `DCC source candidate` for both twins
- Visual status: `candidate pending Flamestrike visual decision`
- Step 13 authority: `false`
- Retopology / UV / bake / export authority: `false`
- Unreal authority: `false`

## Production Decision Produced

The approved fresh-builder contract produced two standalone Blender sources:

- `SM_DRW_SiegeBreaker_Hammer_A01`
  - treatment: double rune sided;
  - Blender SHA-256:
    `c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537`;
  - independent saved-file audit SHA-256:
    `52fa75f4708b95e6b1150ccffb150672f09c6697f5bcd88871440d1a464f28e0`;
  - saved-file audit result: `PASS`.
- `SM_DRW_FoeHammer_Hammer_A01`
  - treatment: double metal-center-piece sided;
  - Blender SHA-256:
    `67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4`;
  - independent saved-file audit SHA-256:
    `9107b943046cfe3373e301e88636ee628817c7e7766892048136de7a70e9b846`;
  - saved-file audit result: `PASS`.

Neither Blender source reads, links, imports, or reuses geometry from either
quarantined Step 12 output family.

## Exact Shared-Dimension Result

Both exact source constructions have:

`50719500/517681 × 6644212/149985 × 170/1 cm`

Decimal XYZ:

`97.974428267601 × 44.299176584 × 170 cm`

The independent saved-file audit observed the same Blender float32-encoded
dimensions in both files:

`97.97442626953125 × 44.29917526245117 × 170 cm`

The observed cross-asset difference is exactly:

`0.0 × 0.0 × 0.0 cm`

Expected rational dimensions and observed Blender-encoded dimensions are
recorded separately. The small expected-versus-observed decimal residual is
only float32 storage encoding; it is identical in both files.

## Canonical Shared-Base Result

- Exact builder canonical shared-base SHA-256:
  `ac0d08252ee71166842779bfb85904c4378ff1a9a4b8328d82dfac9c914e8049`.
- Independently derived saved shared-base SHA-256:
  `f03b975b03141204b4a3c061306d8f48f8668e2a2bdcd214d1f72f555efe86c4`.
- Cross-asset exact builder hash equality: `PASS`.
- Cross-asset independently derived saved hash equality: `PASS`.
- Shared-base local-C04 contamination: `none`.
- Candidate-specific global depth control: `absent`.
- Forbidden `EQ_CANDIDATE_AXIAL_INTERSECTION`: `absent`.
- Surface provenance coverage: `complete`.

## Local C04 Evidence Separation

The approved source intervals remain exact registration domains:

- Rune: `[557,668)`, half domain `9435/548 cm`.
- Metal: `[418,557)`, half domain `11815/548 cm`.

Only selected source-owned pixels create the visible face. The interval
rectangle is not filled. This matters for the metal treatment: its visible
selected face pixels do not touch the registration-domain outer edge. The
builder and auditor record the exact domain and visible-face extent
separately, preventing the interval from becoming unowned geometry.

Both local treatments and their ruled joins remain inside the common
`3322106/149985 cm` half-depth envelope.

## Geometry Counts

- Siege Breaker:
  - mesh objects: `50`;
  - vertices: `1,205,064`;
  - polygons: `1,186,382`;
  - triangles: `2,368,154`.
- Foe Hammer:
  - mesh objects: `50`;
  - vertices: `1,186,812`;
  - polygons: `1,168,246`;
  - triangles: `2,331,882`.

Topology equality is not required for the tagged local C04 treatments. The
canonical nonvariant shared base is equal.

## Governing Outputs

- Builder SHA-256:
  `592a1e49eb45cd93d56b1e883d323cf35114b0124899b1e04d789fbf3c6f3f35`.
- Independent auditor SHA-256:
  `c54c504160f2b82b8f01d952265be78117287972b5819d3f0ff24a94babbcd36`.
- Combined build manifest SHA-256:
  `6e77b264cfceb9233f2f8b4ae8a9844a53069d8bcf724bd6b0699b8416181350`.
- Independent cross-asset audit SHA-256:
  `f2c5434a61b15dcbb616a3c10c23bef0f91f62f4966d46b6d758dbc8dc9cc285`.
- Review board SHA-256:
  `2f88854a58596e104841878c355082a0f9515e95ca634bd0ed31bbbc8d608c65`.
- Review-manifest SHA-256:
  `962c6ebcf29aa5cb397af435fa785b57ef08db13ff5c5ce1f232938343bbfce8`.

## Controlled Packaging Recovery

All eight Blender renders completed successfully. The first board-composition
attempt then failed because the system Pillow version does not expose the
newer `Image.Resampling` name.

The builder was preserved byte-identically. A separate packaging-only script
used the compatible Pillow API and created the final board. No geometry,
saved-file audit, render, or asset status was changed by this packaging
recovery.

## Stop State

The approved fresh-builder contract is complete.

Both assets stop as `DCC source candidate` pending Flamestrike's visual
approval, rejection, or blocked decision. This output does not authorize
Step 13, retopology, UV work, baking, textures, production materials, LODs,
collision, export, Unreal, `DCC game-ready candidate`, or `Fully game-ready`.
