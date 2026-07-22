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
