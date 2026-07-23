# A12 Internal Rejections

## R0 — Axial Backing/Relief And Bottom Orientation Failure

- Date: `2026-07-22`
- Status: `quarantined; never presented for approval`
- Contract: `SB-AXIAL-A12-RECONSTRUCTION`

The first internal A12 execution correctly reproduced the top head source and
remapped the main head depth, but failed the internal presentation and geometry
gate:

- the bottom head proof was vertically reversed relative to its source;
- the concave source-backing n-gon triangulated across exterior gaps;
- the `2.4 cm` source-luma relief produced visible spikes;
- the backing and relief intersections created horizontal white seams in the
  completed front and three-quarter views.

The attempt is `invalid` as a review candidate. The source scans, A11 authority,
and main depth-remap formula remain valid. The exact rejected artifacts are
preserved locally under
`SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_InternalRejected_R0/`.

Hash locks before correction:

- rejected `.blend`:
  `7a0185a9dab559d434a9c34a4acdeb60abc03b05794a54bcd7141509e5b14b08`;
- rejected review board:
  `13f617070025c7ae7f49b7c88126f452d2a13ee9bfa302a304011152c2646637`;
- rejected colored three-quarter:
  `54d42fd3eba939d38720dae4cd5a5285c3e9de7446afc16e337a16f9fecd7f2f`;
- rejected geometry three-quarter:
  `09e068b0f89557189d027990f20d0a5571fdf3ce3f8da5f4c19efb9df217374c`;
- rejected top proof:
  `02425c8e6cf63d02c982fa55b7505b6073073305546e42ef2d69531022be4ab9`;
- rejected bottom proof:
  `86f7d8250f5adbca1010d01b492b99d6732cd841c4b9936dd539ec56fd3abbb0`;
- rejected validation:
  `2c5964b19f5084a2118846ed52815de12ec005c4f713d101f297e97bec78ccf5`.

Bounded correction: preserve the exact source masks and depth-remapped main
volume; correct bottom orientation; reduce inward relief to `0.45 cm`; close
the sampled relief mesh with Blender Solidify; classify the concave n-gon caps
as head-isolated proof backing and hide them from completed-assembly renders.
No source, scale, ownership, or geometry-envelope rule changes.

## R1 — Owner Views Correct, Completed Assembly Invalid

- Date: `2026-07-22`
- Status: `quarantined; never presented for approval`
- Contract: `SB-AXIAL-A12-RECONSTRUCTION`

The second internal A12 execution corrected the bottom orientation and reduced
the relief depth. Its top and bottom head-isolated owner views matched their
respective source orientation, but the completed assembly failed the internal
geometry and presentation gate:

- constant-Z axial projection sheets extended beyond the remapped main-volume
  boundary when viewed obliquely;
- source-connected negative spaces exposed the white world background instead
  of a continuous underlying head volume;
- the bottom projection sheet created a visible horizontal edge through the
  completed head;
- Solidify expanded the recorded candidate bounds beyond the approved pixel
  footprint.

The attempt is `invalid` as a review candidate. The corrected bottom
orientation, source masks, A11 authority, and main-volume depth-remap remain
valid evidence. The exact rejected artifacts are preserved locally under
`SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_InternalRejected_R1/`.

Hash locks before correction:

- rejected `.blend`:
  `40c0db0bbc8374fa3840a75956a916579a5b8bb604573925269b97d6799718f5`;
- rejected review board:
  `d580c737dc7cf9404100be7c2a5784adc77bfa4622f8c0e31e1cc8e19c82b272`;
- rejected colored three-quarter:
  `d28dac8be42c7815e51d281dff94cdeef4a21552c35e558a412a18247f4a84e5`;
- rejected geometry three-quarter:
  `a2a66d2c5cb57b74e4f0977772e99b723edc192ad0a1864fb81b8fda8d07cf1e`;
- rejected top proof:
  `85f0d521b9d508901a999ca8eb2c0c45cb7ef7d14b55f57a571a5bbf10bf08ea`;
- rejected bottom proof:
  `9629c34f4aad6f94896dddfff8887e68b355b3b6f035a966a2db0b2cd23c3231`;
- rejected validation:
  `05179f17a22d909330667fca89039407fb8d114edcf9f6f395522910c3fceef0`.

Bounded correction: preserve the corrected source orientation and exact
head-isolated proof surfaces, reclassify those constant-Z projection surfaces
as `proof only`, integrate top/bottom source ownership onto the actual
main-volume boundary faces, normalize the remapped head to the approved
centered mean depth, and restore the proven A09 three-quarter camera. No source,
scale, half/mirror, or asset-scope rule changes.

## R2 — Exact Depth Pass Exposes Undefined Z=132 Transition

- Date: `2026-07-22`
- Status: `quarantined; never presented for approval`
- Contract: `SB-AXIAL-A12-RECONSTRUCTION`

The third internal execution removed the projection-sheet defect and produced
an exact centered candidate envelope of
`75.130516 x 44.299175 x 170 cm`, with one mirrored main-volume object and zero
missing mirrored vertices. It nevertheless failed the internal completed-model
gate because the approved rule changes the depth boundary abruptly at
`Z=132 cm` while preserving the different A09 depth immediately below that
plane. The resulting connected mesh contains a straight horizontal ledge
through the decorated head in both colored and geometry three-quarter views.

This is a rule conflict rather than a source-measurement failure. The current
contract defines both endpoint authorities but does not define how their
incompatible depths must transition across the head/body interface. Smoothing,
blending, moving the interface, scaling the lower body, or adding connector
geometry would each be an unapproved interpretation.

The attempt is `invalid` as a review candidate. The exact rejected artifacts
are preserved locally under
`SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_InternalRejected_R2/`.

Hash locks:

- rejected `.blend`:
  `827d6e787d077f21e3ffdeee765f2fab6833b91293de6387a8b38f8e81c00eea`;
- rejected review board:
  `c2e18218ff751982daf0333903a1bdbda73cdfa63766037421c05bdb8158a629`;
- rejected colored three-quarter:
  `23472c67352a3c3135b39b0b16675fa4a5eb8c304de3cbe064be67b971aaf75d`;
- rejected geometry three-quarter:
  `c7e844f65a8696f9e74d4ad89122bd1e3fa3d757e1f06a89d0a6b15f49ee740d`;
- rejected top proof:
  `61acbc5238af3a5b7a512e89396d0a94900c901ee12f0f769834b925ce4e0c26`;
- rejected bottom proof:
  `ac4f3077565f63b379babd2c5a838c75e2ea9652d79a2ec1a012c9d7749245ff`;
- rejected validation:
  `ebbffc5c6cd11fd421f8e6f28d50efa867742669ea52551ab8a566e02b1db07e`.

`Blueprint block: rule missing` — a source-authorized transition rule is
required between the unchanged A09 depth below `Z=132 cm` and the A11 centered
mean head depth above it.

## R3 — Component Split Correct, Outward Strike Faces Warped

- Date: `2026-07-22`
- Status: `quarantined after Flamestrike visual rejection`
- Contract: `SB-AXIAL-A12-R3-COMPONENT-SEPARATION`

R3 correctly removed the false center stone and produced separate mirrored
outer stones around the centered metal core/shaft. Its exact component split,
overall envelope, and symmetry audit passed. Flamestrike nevertheless rejected
the colored completed three-quarter view because the two outward strike faces
were visibly warped.

The first invalid assumption was retaining front/back-derived projected side
walls as the visible `-X/+X` strike-face solution. Those walls preserve the
front elevation but do not reproduce the side-view-owned face silhouette,
bevels, rune plate, or surface relief. The exact left/right source views are the
explicit evidence for those outward faces.

The attempt is `invalid` as a visual candidate. Its component-separation ratio,
centered core, exact A11 envelope, and zero-missing-mirror result remain
`proof only` inputs to the bounded R4 correction. The exact rejected artifacts
are preserved locally under
`SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_InternalRejected_R3/`.

Hash locks:

- rejected `.blend`:
  `7490516c746646d095af970836b75283048a3b7dce19d7c262ac8f2a3a7bc706`;
- rejected review board:
  `621c361e809d11d775c3aa7aca476fdad4c3962cd76997cf763d0edb4d1ad5c6`;
- rejected colored three-quarter:
  `6ee475ecf62753c9c28c6d138df7f56801675267e5f460cbcbdcd6725a931eac`;
- rejected geometry three-quarter:
  `ef35847476a2f0bfd1e98b02e997629347266f9c88be805d81bfba863767135a`;
- rejected front:
  `8296fa456a3d6e83d8eca28199903a84ffab000cd7bc97380f518acef9f4bfe1`;
- rejected validation:
  `bf4009a7dde2a191d816a4b83a28fa496fc8535b8a0adc8d5607a37ee08fa1d5`;
- rejected independent audit:
  `5d1a85110e38c1dd47b177793aa38d4bf010847ae1191d88f7041cfd15a5e6f2`.

Bounded correction approved by Flamestrike: keep A09/A11, the centered core,
the R3 component split, and the exact envelope; replace only the visible
outward strike-face solution with pixel-scanned `-X/+X` owner geometry; build
one geometric face solution and mirror it at `X=0`; map each original side
source to its corresponding outward face; show side-source comparisons plus
colored and gray three-quarter proofs; stop at the visual gate.

## R4A — Nonlinear Side UV And Edge-Offset Envelope Failure

- Date: `2026-07-22`
- Status: `quarantined; never presented for approval`
- Contract: `SB-AXIAL-A12-R4-SIDE-OWNER-FACES`

The first internal R4 execution created one `+X` face and mirrored it correctly,
but failed the internal source-map and dimension gates:

- it normalized UV coordinates independently inside each scanline's changing
  member span, visibly wavering straight source features;
- Blender Solidify with even edge offset expanded `Y`, `Z`, and the recorded
  envelope to `75.130516 x 45.648811 x 170.749954 cm`;
- it used only the earlier upper-head sample interval `Z=132..170 cm`, while
  the fresh front-source stone component proves that the complete outward
  strike mass continues to `Z=111.089111 cm`.

The attempt is `invalid` as a review candidate. It is preserved locally under
`SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_InternalRejected_R4A/`.

Hash locks:

- rejected `.blend`:
  `c0f9d15348f0a50d9385b4aa497ae412a342534d84c4474091dfc59229f3afc6`;
- rejected review board:
  `01a97612caa7b2709f3a5232a42171023bd5f763ca2a0979b47a0f004ce1295b`;
- rejected colored three-quarter:
  `b63d0b10a24565756f9781e1c119375f9fd01b0a7bcbde9d487911cabd742d1f`;
- rejected geometry three-quarter:
  `ee5a29b58f1090da079a953080272cc5674773af4decd962ef619f5a1a44475f`;
- rejected `-X` face:
  `0a86b9c385737bdde49e70ca7c13ce027db62bb9437a3086fded0e240be255c4`;
- rejected `+X` face:
  `ac569919149cdfd5cc5c171f42665b877fe7428eb4fe6087f22a159089053105`;
- rejected validation:
  `8fc719799ce22a8dbc26992333c39f533f8a735a019308d83a9ec36f82ef609e`.

Bounded correction: use one fixed crop-to-A11-depth coordinate map for every
source pixel; derive the complete owner-face `Z` interval from the freshly
built front-source stone component; create pure-X inward thickness manually so
no Y/Z offset is possible; preserve all other R4 authority.

## R4B — Exact Envelope, But Background Corners And Raster Seams

- Date: `2026-07-22`
- Status: `quarantined; never presented for approval`
- Contract: `SB-AXIAL-A12-R4-SIDE-OWNER-FACES`

R4B corrected the nonlinear UV error, covered the full measured stone interval
`Z=111.089111..170 cm`, and restored the exact candidate envelope
`75.130516 x 44.299175 x 170 cm`. It still failed the internal visual gate:

- the common mean silhouette can exceed either individual source membership at
  a changing row edge, so opaque white source background appeared at bevel
  corners;
- cell-by-cell raster closure produced small visible discontinuities around
  the central rune plate.

The attempt is `invalid` as a review candidate. It is preserved locally under
`SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_InternalRejected_R4B/`.

Hash locks:

- rejected `.blend`:
  `c93fe431f99ee42f3d5fe8b1ed512aaae45aea7a67e038fb6a1fb36e3d5923b8`;
- rejected review board:
  `ed6ecdf7d67e55ff5b4c28f9a3b5960878805815c656ca9964023b404a4c4437`;
- rejected colored three-quarter:
  `d9e7ae6360dc4a6bfb1f4961b52935e4ce152a01ff950fa4ebef38edf940a3dd`;
- rejected geometry three-quarter:
  `5c12390f3b97449f91a18919bdc11931234dab55b84b8ff0f0553faad4357351`;
- rejected `-X` face:
  `198168a44b7542a044057e38f7adba678857f4660c39571af8f7419a4edc7763`;
- rejected `+X` face:
  `6ba11b87897d0b8dc4b1c5e9cc23213141b1f99f07b487bac8aff2e61bb6fd24`;
- rejected validation:
  `c605ff87d9a34cd1d6d9df4273016cc57c4efeeddefaa3a1d1a9dd7151ebee3a`.

Bounded correction: retain the fixed coordinate map, complete measured Z span,
mean geometry profile, and pure-X thickness; derive alpha solely from the exact
source membership to remove source background; replace discontinuous raster
cell islands with one continuous row-connected face grid.

## R4C — Continuous Masked Face, Legacy-Wall Occlusion

- Date: `2026-07-22`
- Status: `quarantined; never presented for approval`
- Contract: `SB-AXIAL-A12-R4-SIDE-OWNER-FACES`

R4C removed the source-sheet background and raster-cell seams, preserved the
exact envelope, and passed its first independent technical audit `36/36`.
Internal close-up review still found small rectangular patches around the rune
plate. Exact vertex evidence identifies the cause: legacy wall vertices at
`|X|=37.259228 cm` remain outside the new face's deepest relief position
`|X|=37.115258 cm` and therefore occlude the owner pixels.

The attempt is `invalid` as a review candidate despite its technical pass. It
is preserved locally under
`SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_InternalRejected_R4C/`.

Hash locks:

- rejected `.blend`:
  `ab30971e2f57fade7eaacb4898eed5b4378b117010fcadde20c84986876d1d61`;
- rejected review board:
  `f1709fe64a4eda77cf71384890fb63a4578ffe04a6512f36ab31e7f595090c2f`;
- rejected colored three-quarter:
  `e59f7f451c18b459263d5f99ff1b5afbae3d6324c620f72c24bc1d5781f37664`;
- rejected geometry three-quarter:
  `d5bd260a7c0277dc0bcdba751bd8dd404e03f7cd3cb24af2d54537e805ca76d8`;
- rejected `-X` face:
  `cc8e3dcc93f1cc7f239ce978bab705f87222a6e5f6f4db2854a99e2639548673`;
- rejected `+X` face:
  `9a39cd18de2b55acad86815e75f024475c44d12abfddc7067bfa09de11c61ed9`;
- rejected validation:
  `079a8a0f82074c4ead9376620722deb56138310242db783ea50b081ac51a7e17`;
- rejected technical audit:
  `22a23107131c311e436c15b9f43846935fee19d0ecc5bc0e0f1a3101c81a0d38`.

Bounded correction: enlarge only the already-authorized inward recess so every
superseded wall vertex is behind the new maximum relief. Do not alter source
pixels, owner-face profile, UV mapping, relief, mirror, or outer envelope.

## R4D — Side-Face Audit Pass, Whole-Assembly Registration Failure

- Date: `2026-07-22`
- Status: `quarantined after Flamestrike visual rejection/revision`
- Contract: `SB-AXIAL-A12-R4-SIDE-OWNER-FACES`

R4D corrected the R4C owner-face occlusion and passed its expanded technical
audit `37/37`. Flamestrike then identified defects outside that audit's
coverage: the handle reads as differently scaled front/side/back facets, rock
remains visibly between the apparent haft surfaces, and the handle is not
aligned.

The first invalid inherited assumption is A09's use of the whole left-view head
crop midpoint as the Y origin for every Z row. Exact stable-shaft measurements
show the left handle axis approximately `44 px` away from that midpoint. The
second invalid assumption is that front/back pixel sheets plus side-wall
projection form one registered volume. They do not establish common local
component landmarks across the four views.

R4D is `invalid` as a complete visual candidate despite its side-face technical
pass. Its exact strike-face measurements remain `proof only`; its mesh is
forbidden as R5 construction geometry. Exact preserved hashes:

- `.blend`:
  `d44778864febf225019ba2a256ae22af87d8fc091ed2fc515b1ab0010c9fff96`;
- review board:
  `eb0b41930a012ef014e2962daef697d5733942cc231b22b8775dbb24a77a7520`;
- colored three-quarter:
  `9e053ae4a72410d7160a8281142963b7c35ff7dae575370e666563f88917a374`;
- geometry three-quarter:
  `913a953212c97e96b8c68136f9ff107afb1b50446c05d351a8dc8b87e649c511`;
- validation:
  `beeb035e780a65a7af1461888ecefe4e227219b0844ec9bef6ab62dda98021fa`;
- independent audit:
  `cea705dbe7407ee2fd7ebf1205cb8b5cc0d280a5abc4293d4d4ecb0c4aa1c559`.

Approved recovery: preserve R4D only as quarantined evidence; return to the
original four source views, register them to the shaft centerline and common Z
landmarks, trace physical components and empty space separately, and rebuild
fresh only if the opposite views pass the R5 source-consistency gate.

## R5A01 — Registered Assembly With Source-Gap And Proof-Material Failure

- Date: `2026-07-22`
- Status: `quarantined; never presented for approval`
- Contract: `SB-AXIAL-A12-R5-FOUR-VIEW-WHOLE-ASSEMBLY`

R5A01 rebuilt from immutable front/back/left/right source pixels on measured
shaft axes and used one `X>=0` half plus an exact mirror. Internal review found
source-sheet background gaps on the left/back surfaces, a geometry proof that
still displayed source color, and a rectangular faceted haft. The attempt is
`invalid` as a review candidate.

Preserved local hashes:

- `.blend`: `9e52c422fc8ec6efade3c7112b0dda4e0b1d9ed5b9c20d04c3cd9446a8c64071`;
- validation: `425019c4860fe2deea43836e9d9fdc848b61435fe3dea952ce55dd30cf90126c`;
- review board: `a220982155d31c9a25cc9cbbde7a5e51cdd7dfed9bcff3d9ba40f8813f561b47`.

## R5A02 — Registration Improved, Slab Haft And Endpoint Loss Remain

- Date: `2026-07-22`
- Status: `quarantined; never presented for approval`
- Contract: `SB-AXIAL-A12-R5-FOUR-VIEW-WHOLE-ASSEMBLY`

R5A02 corrected most source-background gaps and produced a valid gray geometry
proof. It still represented the haft as front/back facade slabs with side
walls, so the handle read as multiple differently scaled surfaces instead of
one aligned round object. Front/back membership intersection also removed the
lowest source row, reducing the evaluated height to `169.846985 cm`, and a
small side-view background sliver remained. Flamestrike's later explicit
cylinder/static-UV method supersedes this haft construction.

Preserved local hashes:

- `.blend`: `e3e4e9d492760b693857b7fc8cf1c84fe309967f54126bdd59e48a5e9f8d8264`;
- validation: `9818083f34a1c0250a6f76978d13cf35dc8b8db7a6337c893934612d727c4f2c`;
- review board: `8d6b5dd598eaf3f841c6ae85f86fb4644562d915a05554cb695f6f7581191961`;
- colored three-quarter: `a73fb7f3c0078f79df0ec0191237a3f6420cfcec0cb119246b835d347eb52586`;
- geometry three-quarter: `fd968bedcfb108630eb916f57c71dcc34bc1e9b1a72782d1b86ad65ee2db18d9`.

Approved recovery: preserve the shared shaft registration and one-half mirror
rule, remove the slab haft, build a true cylinder on that axis, assign separate
front/back 180-degree material sets, and store all mapping in a static UV map.
Do not export or enter Unreal at this gate.

## R5A03 — Cylinder Correct, Back Head-Transition Row Included

- Date: `2026-07-22`
- Status: `quarantined; never presented for approval`
- Contract: `SB-AXIAL-A12-R5-FOUR-VIEW-WHOLE-ASSEMBLY`

R5A03 replaced the slab haft with the approved true circular cylinder, exact
half/mirror construction, two 180-degree material sets, and static `UVMap`
islands spanning `U=0..1`. Internal review confirmed that the handle now reads
as one centered round component. The first top endpoint nevertheless used
`Z=111 cm`; the back source has already entered its head-owned interval by that
row, so the back haft texture normalized head pixels into its top row and left
a thin white join gap. This pass is `invalid` as a review candidate.

Preserved local hashes:

- `.blend`: `933491a21589afb89726b1f51d18b1e390b3076fcef65d190a59d4c2533a52c0`;
- validation: `43f81fda0c0995d8ebee7ebc0e38d372fd26c35da6b304cafde75cc0e2677e2b`;
- review board: `2576608b94ebea7661dc145ae136540da57fbea49a56275ba00bf38455a0576f`;
- colored three-quarter: `f58489a0ba24d5450d74cfec3b58530600e2e79a1df685bca417375afc737e07`;
- back proof: `afc98bb40473b2366b1b0a6ffaf5e5df41b67af405933512a0ae1cc298cdac27`.

Bounded correction: retain the cylinder, its front-derived circular profile,
static UVs, materials, mirror, and all source hashes; move only its top endpoint
to `Z=109.25 cm`, the last measured row where both front and back remain
haft-owned, so the facade resumes before the back head transition.

## R5A04 Pre-Audit Board — Material Override Did Not Cover Both Meshes

- Date: `2026-07-22`
- Status: `invalid proof artifact; never presented for approval`
- Candidate geometry status: `unchanged`

The first A04 board used Blender view-layer material override for the gray
proof, but the render retained source-color materials on the two-object
assembly. The colored proof was therefore duplicated into the geometry panel.
This was a review-artifact failure, not a geometry or source change. The invalid
proof and board are preserved locally under
`A12_InternalRejected_R5A04_PreProofFix/`.

- invalid geometry-proof SHA:
  `ac8ee5cbc8fc798447d0b3a5db2ffc20b2731d184dfe2f6e64e1a3d688ced473`;
- invalid board SHA:
  `7070a11f402dbf6936b75532bb3d27e6138d0da55ba0fd66657ca92db89216cb`.

Bounded correction: temporarily replace both mesh objects' material arrays
with the one geometry-proof material, render, then restore their exact material
slots and polygon indices before saving. No mesh, UV, texture, source, camera,
or ownership value changes.

## R5A04 — Circular Geometry Pass, Front/Back Texture Seam Misregistration

- Date: `2026-07-22`
- Status: `quarantined after Flamestrike visual rejection/revision`
- Contract: `SB-AXIAL-A12-R5-FOUR-VIEW-WHOLE-ASSEMBLY`

Flamestrike identified a vertical mismatch in both side renders where the two
haft halves should meet exactly. The independent audit proves that the cylinder
rings are circular within `0.000000406 cm`, the X mirror has zero missing
counterparts, and both UV islands span exact `0..1`. Therefore the defect is not
a rotation, mirror, or geometric join failure.

The first invalid assumption was treating common normalized `V=0..1` as common
component registration. The front source strip is `140 x 519 px`; the back is
`148 x 538 px`. Their collars, runes, grip transitions, and other landmarks do
not occupy the same normalized V positions, so the two independently sampled
designs visibly jump at the side-tangent material boundaries.

A04 is `invalid as a visual candidate`. Its source hashes, circular geometry,
exact mirror, and static-UV mechanics remain `proof only`. Its hash locks remain
in `steps/A12_R5_CYLINDRICAL_HAFT_A04_OUTPUT_RECORD.md`.

`Blueprint block: seam reconciliation rule missing` — do not repair forward by
stretching, averaging, painting over the seam, or changing cylinder rotation.
An exact shared component-landmark mapping or alternate material-boundary rule
requires Flamestrike approval.

### Superseding R5A04 Core Finding — The Mirrored Half Is A Projection Composite

Flamestrike's further review supersedes the seam-only diagnosis. The colored
three-quarter image shows one hammer face over another underlying face and
visible white lines because the purported half contains multiple source-owned
projection surfaces: front/back pixel facades, connecting side walls, and
independently mapped side-owner surfaces. Mirroring that assembly exactly does
not turn it into one coherent physical half.

The complete R5A04 blend and visual outputs are `invalid`. The prior `45/45`
audit remains `proof only` for source hashes, circular-ring math, UV extents,
identity transforms, and X symmetry. It is explicitly insufficient because it
did not test duplicate visible faces, overlapping owner surfaces, closed-half
topology, or white source-background exposure.

The first drift action was `build_registered_half`: it converted every front
source pixel into front and back facade faces plus boundary walls, then mapped
separate side sources onto those walls. `build_cylindrical_haft` added another
independently textured component. The later mirror duplicated this composite;
it did not duplicate a single physical half.

Core recovery: do not reuse any R5 geometry, UVs, materials, or composites.
Return to immutable source evidence and define a fresh build in which exactly
one closed `X>=0` physical half exists, every visible surface occurs once, the
center seam is welded, and the opposite half is created only by the approved
duplicate/mirror operation. No new construction is authorized yet.

## R6A01 — Exact Diagonal Pixel Saddle Fails Pre-Mirror Manifold Gate

- Date: `2026-07-22`
- Status: `invalid; no candidate output created`
- Contract: `SB-AXIAL-A12-R6-SINGLE-CLOSED-HALF`

The clean-room R6 builder read only the six immutable source PNGs and created
no R5 geometry, UV, material, texture, or Blender inputs. Before mirror, UV,
material assignment, save, or render, its source-half audit reported:

- `1,074,899` edges with exactly two incident faces;
- `3,198` open edges, all correctly on `X=0` for the later weld;
- `110` edges with four incident faces;
- zero off-center open edges.

All 110 four-face edges are one X/Z checkerboard saddle extruded along valid
right-view Y cells. The shared grid edge is `(X=1,Z=1102)`, equivalent to
`X=0.153015302 cm`, `Z=168.622862286 cm`. Layer `1101` owns `X-cell=1` while
layer `1102` owns `X-cell=0`, so their solids meet only at a corner.

The exact front pixel at the missing centered bridge cell `(X-cell=0,
Z-layer=1101)` is `RGB(212,192,169)`, integer luma `195`, and therefore valid
front-object evidence under the locked `<=234` membership rule. It was absent
from the volume only because the conservative front/back silhouette
intersection rejected it.

The contract did not declare front or back precedence for this one-pixel
topology conflict. The gate therefore stopped without adding or removing any
cell. The builder is quarantined as a diagnostic implementation until an exact
reconciliation is approved.

## R6 A03 Internal Attempts — Z-Rotation Method Superseded Before Approval

- Date: `2026-07-22`
- Status: `quarantined / reference only; never presented as a valid candidate`
- Contract: `SB-AXIAL-A12-R6-A03-FRONT-HALF-ROTATE180`

The A03 lane produced one coherent front physical half and mechanically closed
copies, but none reached the required approved visual gate before Flamestrike
superseded the Z-axis transform with the proper-axis A04 depth mirror.

- A01 stopped before output because Blender 3.0 rejected an unsupported color
  look. No `.blend`, manifest, or review board was created.
- A02 passed geometry construction but was internally rejected: complete-side
  UV reassignment sampled outside the side-source objects, producing broad
  white bands; the gray override repeated the color proof; Pillow review-board
  packaging failed. Preserved local `.blend` SHA:
  `50bf23585544815f342ba3a14dc9c1d64ca7a1cebb17da4a890fae09ca05eb59`.
- A03 corrected rotated right-side ownership and the independent gray proof,
  but the left orthographic axis sign remained reversed. The left render
  contained broad white bands and was internally rejected. Preserved hashes:
  `.blend` `93207b4c7c7fcc435b19a254e77756efbe76bb51e1b27085f6ee88c7b5c8e93f`,
  validation `ae169b6857b14683514228c0b06121cfe5dd778c6cd31e7b5b02b75119942211`,
  board `00b470a60e22f06f3969098e5001b0af73c5a24d7272d1cfb052a3c7104fc3da`.
- A04 corrected the left sign and removed the broad source-background bands.
  Before independent audit or visible presentation, Flamestrike clarified that
  the copied front half must preserve left/right and top/bottom on the proper
  front/back axis. This output is therefore `reference only` under the
  superseded A03 Z-rotation method, not a visual candidate. Preserved hashes:
  `.blend` `93b82f723ab07a55f42049b6aeda802d7107f7290ed4320c5aedb0e539e20808`,
  validation `29f4e4dcbd7dea139b8df2c4549bbf4fddf85be68167044264a09a0e94e0dd79`,
  board `f6576911e98cb43c50f3345f5a06aca78682a9e3db04eb8653d851bcb359297a`.

The A03 outputs remain local defect/mechanical evidence only. They are
forbidden A04 construction inputs. A04 restarts from the immutable source PNGs
and uses only `(X,Y,Z)->(X,-Y,Z)` before the `Y=0` weld.

## R6 A04 A01 — Depth Mirror Correct, Haft/Collar Ownership Invalid

- Date: `2026-07-22`
- Status: `quarantined after Flamestrike visual revision`
- Contract: `SB-AXIAL-A12-R6-A04-FRONT-HALF-DEPTH-MIRROR`

A04 A01 applied the correct depth reflection, recalculated outward normals,
welded `Y=0`, and produced one closed connected mesh. Numerical inspection
confirmed every one of its `1,210,410` vertices belongs to one connected
component. The final edge-incidence histogram is exactly `{2: 2,420,816}`;
internal center faces, duplicate faces, and missing Y-mirrored vertices are all
zero. These facts remain `proof only`.

Flamestrike identified that the visible haft cylinders do not connect, the
vertical design is misaligned, and part of the collar immediately below the
head lacks correct pixel ownership. The render and material audit confirms the
failure is not an open geometric seam. The builder applied the global head-side
rule to the haft and collar, mixing three independent source projections:

- complete haft interval: `95,664` front-owned faces, `36,766` left-owned
  faces, and `36,766` right-owned faces;
- upper collar interval `Z=106.0..110.324032403 cm`: `6,592` front-owned
  faces, `2,176` left-owned faces, and `2,176` right-owned faces.

Those projections do not define one cylindrical vertical registration. The
side-source pixels produce broken collar ownership and visible stepped light
regions at the cylinder boundaries. This also fails to implement Flamestrike's
explicit static cylindrical-UV rule for the haft.

Preserved hashes:

- `.blend`: `386a532b3fd400ea22b793f6b61ae6133ce7742667e09c2b7da3ac913c68bff3`;
- validation: `d09f202c9880a44f99454bc426c562543edb7907b8a79cf16212e574bad3bf63`;
- review board: `f173c834e51d47728494fa25ffbd3f933070dea2f57cbf60576e51dd82dab6fa`;
- colored three-quarter: `3c10027e66aa29e5c3043ca9bbab6d403f721b2270ac6a270992f9d3b8aa918a`.

Recovery boundary: do not repair the saved A01 blend. Rebuild fresh from the
immutable source files after approving one haft-specific rule that assigns the
complete front semicylinder and its collar to one front-derived static UV
island, preserves that UV through the Y-depth mirror, and forbids left/right
source ownership below the exact head transition.

## R6 A05 A01 — Exact UV Inheritance, Bright Source-Outline Seam

- Date: `2026-07-22`
- Status: `internally rejected; quarantined; not presented as a valid candidate`
- Contract: `SB-AXIAL-A12-R6-A05-HAFT-COLLAR-CYLINDRICAL-UV`

A01 rebuilt fresh, assigned the front-derived `157.08%` cylindrical UV to the
source half before the approved Y-depth duplicate/weld, and passed its numeric
gates. The complete haft/collar contained `169,196` haft-owned faces, zero
left-owned faces, zero right-owned faces, exact `U/V=0..1`, and zero mirrored
UV-coordinate mismatches.

Internal visual inspection rejected the attempt because the enlarged left and
right join renders still contained a bright vertical line at the Y=0 side
seam. The mesh is welded and both halves have identical seam coordinates; the
line is therefore not a geometric gap or scale mismatch. The first and last
texture columns came from the bright exterior pixels of each axis-containing
filled front-source row. Their mean luma values were `180.313075506` and
`185.988950276`, compared with `101.046040516` for the center column. Mapping
those bright silhouette-edge pixels to the cylinder's two side seams exposed
the source outline as a false seam.

Bounded A02 correction inside the approved contract: keep the same immutable
front source, geometry, 157.08% widening, nearest sampling, pre-mirror static
UV assignment, transform, and weld. For every registered row, retain the exact
axis-containing filled span but place its first and last exact selected-component
pixels at the strip endpoints. No pixel is invented, painted, averaged, or
borrowed from another view. A01 remains local `proof only` for its passing
mechanical checks and `invalid` as a visual candidate.

## R6 A05 A02 — Selected Endpoints Preserve The Same One-Pixel Outline

- Date: `2026-07-22`
- Status: `internally rejected; quarantined; not presented as a valid candidate`
- Contract: `SB-AXIAL-A12-R6-A05-HAFT-COLLAR-CYLINDRICAL-UV`

A02 replaced filled-span endpoints with the first and last exact pixels in the
locked selected component. The enlarged side renders were visually unchanged:
the bright vertical line remained because those selected endpoints are the
same one-pixel contour captured by the `<=234` component threshold.

Exact inward-column measurement established a finite, one-pixel outline band
across the 543 registered rows:

- offset `0`: left/right mean luma `180.313/185.989`, with `257/317` rows over
  luma `200`;
- offset `1`: left/right mean luma `73.020/64.613`, with `0/0` rows over luma
  `200`.

Bounded A03 correction: exclude exactly the measured exterior one pixel on
each side of every selected source row, then retain the same nearest-source
sampling and `157.08%` widening. This removes no unmeasured interior band and
introduces no new pixel, paint, interpolation, alternate view, geometry, UV,
transform, or material owner. A02 remains local `proof only` for mechanical
checks and `invalid` as a visual candidate.

### A03 Pre-Proof Packaging Rejection — Flat Gray Underlit

The first A03 clean build removed the false white seam and passed the contract
gates, but its independent Principled flat-gray proof rendered too dark for a
useful topology review. The mesh, UVs, source pixels, materials, mirror, weld,
and colored outputs were not rejected or changed. Only the Blender area-light
energy used by the gray proof is corrected before regenerating the declared
review package.

- underlit gray proof SHA:
  `e181fe48f1c2968dabd0094efb0a73224ede3560ac3aecadc832dc2d02b350f8`;
- underlit review board SHA:
  `307d3f5a4cb080245170038a06662f376770f9160e425b7ffb709d4382e27231`.

## R6 A05 A03 — Whole Geometry Invalid After Flamestrike Review

- Date: `2026-07-22`
- Status: `invalid / quarantined; never eligible for approval`
- Contract: `SB-AXIAL-A12-R6-A05-HAFT-COLLAR-CYLINDRICAL-UV`

Flamestrike's visible review identified failures outside the local A05 UV
correction: the head is stretched, the strike-face piece has the wrong
rotation/pitch, stone again fills the space between the upper haft cap and the
head, and the pommel and top cap are not tapered rotational forms. Flamestrike
also clarified that the strike-face division belongs down the vertical middle
of one face and only one half-face should be duplicated. The A03 side view
instead repeats a complete face motif, producing two face diamonds and an
artificially wide head.

The A03 implementation's first invalid construction is the non-haft branch of
`build_row_occupancy_factory`: it forms
`front-row X cells × right-row Y cells` as one solid cross-section. This makes
one monolithic extrusion instead of separate centered core, strike stones,
face half, tapered cap, and pommel volumes. The right/left source is then used
mainly as a material owner on a resulting stair wall; it does not establish the
face's required inward pitch. The strike texture is folded around the global
shaft axis rather than split at the strike face's own centerline.

Preserved A03 hashes before reclassification:

- `.blend`: `e474f79351c1296ff257b225f839a9e6195b71eed51ffb88d651a36eade69f14`;
- validation: `514a4703d790cedca3c8cf5f24afe07233fa1e0138d98031010e4aaab1ba3aa4`;
- review board: `8799af5bfe8d349f71a7586b4b230c40fe75bc52df404d9a05e72dce61d886df`;
- colored three-quarter: `da82a596fd8fdb6891ed258f3cbcb80c68acf1badcb2bd0ef7b02bee6d9f2708`;
- enlarged join 3/4: `2769ff7c6dc009e082c6367ff73e9b1c42d57422a4c05c60f13f8f59633fbbf1`;
- enlarged right: `e453cfff61e845581832c2d0864ac37470eb5fb3b5253206e3fa82561e10eae5`;
- enlarged left: `1897b69afb941182d4a8895b147f2d8c6af1315b01c2994c73c9d3037607000c`.

Narrow proof retained: edge incidence, one connected topology, Y-depth mirror,
weld, outward normals, and haft/collar UV inheritance. None of those mechanics
proves correct component geometry or visual fidelity. No independent candidate
audit will be run. The builder is disabled pending a new approved geometry
contract.
