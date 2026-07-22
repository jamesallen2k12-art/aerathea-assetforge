# A12 Transition Rule Block

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract: `SB-AXIAL-A12-RECONSTRUCTION`
- Date: `2026-07-22`
- Status: `superseded by approved A12 R3 component separation`
- Artifact ceiling: no A12 review candidate exists

## Decision

`Blueprint block: rule missing`

The approved A12 contract applies the A11 centered-mean axial depth throughout
`Z=132..170 cm` and preserves A09 below `Z=132 cm`. Those authorities have
different depths at their shared plane. The exact implementation therefore
creates a connected but visibly stepped head at `Z=132 cm`.

No final review board was opened. R0, R1, and R2 remain internal rejected
artifacts and cannot be approved as the asset.

## Smallest Proposed Rule Change

Allow a continuous transition band entirely inside the approved head interval:

- at `Z=132 cm`, retain the adjoining A09 depth so the mesh is continuous;
- blend only depth, using a deterministic linear interpolation;
- reach the full A11 centered-mean depth at `Z=138 cm`;
- use full A11 depth unchanged from `Z=138..170 cm`;
- keep X positions, front/back pixels, total width, overall length, source
  hashes, top/bottom owner proofs, and exact center mirror unchanged;
- require the completed bounds to remain
  `75.130513051 x 44.299176584 x 170 cm` within Blender float tolerance.

This proposed `6 cm` transition was not approved and is not used. Flamestrike
instead identified the false center stone as the root problem and approved the
component-separated correction recorded in
`steps/A12_R3_COMPONENT_SEPARATION_CORRECTION_CONTRACT.md`.
