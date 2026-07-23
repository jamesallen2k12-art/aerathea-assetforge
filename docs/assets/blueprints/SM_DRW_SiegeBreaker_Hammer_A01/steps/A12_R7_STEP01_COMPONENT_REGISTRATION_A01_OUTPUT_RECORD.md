# A12 R7 Step 01 Component Registration A01 Output Record

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract: `SB-AXIAL-A12-R7-STEP01-COMPONENT-REGISTRATION`
- Date: `2026-07-22`
- Artifact status: `quarantined; revision requested after axial internal-registration conflict`
- Independent audit: `pass 40/40; proof only`
- Step 02 authority: `false`
- DCC / Unreal authority: `false / false`

## Outcome

Step 01 registered all twelve required component IDs against the six immutable
source images without creating a filled shape, connected contour, smoothed
envelope, hidden closure, candidate geometry, Blender file, texture, or
material. Exact source rows, half-open pixel spans, discrete centerlines,
negative-space gaps, visible envelope samples, formulas, and blocked unknowns
are preserved in the measurement manifest and review board.

The independent replay passed `40/40` source, formula, component-ledger,
firewall, authority, and output-hash checks. This technical result cannot
approve the measurements or grant Step 02 authority.

## Key Evidence

- Front separated station at source row `220`: left stone `114 px`, centered
  core/cap `48 px`, right stone `114 px`.
- Front separated station at source row `520`: left stone `139 px`, centered
  core/cap `102 px`, right stone `140 px`.
- The source-visible strike-mass center edges move inward by `4.5 px` and
  `5 px`; the mean 2D pitch consequence is `0.907107 degrees`. This is not a
  3D rotation rule.
- Right strike-face landmark band: `547.5..550.0 px`; right shaft axis:
  `593.5 px`.
- Left strike-face landmark band: `473.0..473.75 px`; left shaft axis:
  `549.5 px`.
- Exact upper-cap negative gaps: front `36/34 px`; back `34/32 px`.
- Pommel, terminal-cap, and upper-cap/spire measurements remain discrete
  visible-envelope samples, not approved revolution radii.

## Preserved Evidence

- Measurement manifest SHA:
  `54fbf54f074a1931cc82f37c257336dd70f8f2c97ae46a848d0ac09ab6513682`.
- Independent audit SHA:
  `aae45a5539fa250d2121e3a0f2c7c7f8036b588d5e26b1ee3d694cd4940a5107`.
- Review markdown SHA:
  `fffc65f4a2b89608412b2efda4deb1e7aff0bf75992165deee89b78796fb80d0`.
- Review-board SHA:
  `2f9bc9f724329baac4db7275cc3ab5c48975e44cee1bd9da58decf751d75705b`.

## Blocked Decisions

1. `R7-S01-B01`: select the controlling strike-face centerline landmark for
   each side view.
2. `R7-S01-B02`: declare the source-visible strike-face/backing-stone boundary.
3. `R7-S01-B03`: select the front/back rotational-envelope reconciliation rule.
4. `R7-S01-B04`: declare whether visible outer envelopes are revolution radii
   or containment bounds.
5. `R7-S01-B05`: assign decorative collar ownership among C06-C10.

## Stop Gate

Flamestrike's visual review supersedes the pending-approval state. The complete
record is quarantined because the axial panel equated outer-footprint center
registration with internal component registration and did not flag impossible
face-on strike diamonds in the `+Z/-Z` sheets.

Recovery authority is recorded in
`manifests/A12_R7_STEP01_AXIAL_INTERNAL_REGISTRATION_CONFLICT_RECOVERY.md`.
The original five rules remain unresolved, and a new axial internal-registration
rule is also blocked. The supplied cone-sector texture-mapping method remains
`reference only`; it authorizes no UV, material, Blender, or Unreal work.
