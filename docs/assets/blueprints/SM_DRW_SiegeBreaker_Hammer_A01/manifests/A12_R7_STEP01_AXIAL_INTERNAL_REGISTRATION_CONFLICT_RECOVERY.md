# A12 R7 Step 01 Axial Internal-Registration Conflict Recovery

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: `2026-07-22`
- Detected by: `Flamestrike visual review`
- Recovery status: `authoritative recovery boundary`
- Step 01 candidate status: `quarantined; revision requested`
- Step 02 / DCC / Unreal authority: `false / false / false`

## Flamestrike Finding

The true axial bottom sheet does not register its center assembly to the
approved outer-object center: the center section is above the horizontal
centerline, slightly right of the vertical centerline, and visibly rotated.
Its center-section diamond landmarks do not align like the corresponding top
view landmarks. This finding excludes the separate center diamonds on the
outward hammer faces, whose orientation also appears incorrect in both axial
sheets.

## Proven Pixel Evidence

- Top full-object rectangle: `[94,330,1106,921)`; center edge
  `(600.0,625.5) px`.
- Bottom full-object rectangle: `[93,330,1106,933)`; center edge
  `(599.5,631.5) px`.
- In the bottom center crop, the three largest connected blue members of the
  central emissive motif use the declared Step 01 blue rule and have union
  `[560,551,659,647)`; center edge `(609.5,599.0) px`.
- That exact motif landmark is therefore `+10.0 px` right and `-32.5 px`
  above the bottom full-object center edge.
- These values prove translation of the central emissive landmark. They do not
  by themselves define the center assembly's structural pivot or rotation
  angle; those require declared rail/corner landmarks in a replacement pass.
- Both axial sheets show a broad, face-on blue diamond on each outward
  `+X/-X` strike face. A feature on a vertical strike plane must project
  edge-on in a true `+Z/-Z` orthographic view. The visible face-on treatment is
  therefore projection-composite evidence, not valid axial orientation
  authority for those diamonds.

## First Drift Action

The Step 01 axial panel repeated the A11 full-object bounding-box centerlines
under the label `APPROVED CENTER REGISTRATION`. It treated an approved
outer-footprint alignment rule as proof that the internal center assembly and
decorative landmarks were registered.

## Assumption That Caused Drift

Codex assumed that:

1. the full-object rectangle center was also every internal component's
   centerline; and
2. each axial sheet was one physically coherent orthographic projection, so
   its visible surface decoration could be accepted without component-local
   orientation checks.

Neither assumption was approved or proven.

## Affected Outputs And Status

- `A12_R7_STEP01_COMPONENT_REGISTRATION_A01.json`:
  `quarantined as a complete candidate measurement record`; source hashes,
  exact rectangles, front/back component stations, side landmark coordinates,
  and negative-space measurements remain narrow `proof only` evidence.
- Step 01 review board and review markdown: `quarantined; revision requested`.
- Independent audit `40/40`: remains `proof only` for deterministic replay and
  firewall checks; it did not audit internal axial landmark registration or
  physical projection consistency.
- A11 centered-mean rule: remains `authoritative only for the approved outer
  full-object footprint and scale consequence`; it is not internal component
  centerline, rotation, diamond-placement, or strike-face-orientation
  authority.
- The six source images and hashes: preserved unchanged as `authoritative
  source pixels`; the conflicted internal axial details are evidence of a
  source-authority conflict, not correction-ready geometry authority.

## Smallest Sufficient Recovery

Do not repair the source images or infer corrected placements. A replacement
measurement-only contract must, before any Step 02 work:

1. declare structural center-assembly landmarks independently of the outer
   footprint;
2. measure top/bottom translation and rotation from exact corresponding rails,
   corners, or axes;
3. identify which non-strike-face diamond landmarks physically correspond
   across top and bottom;
4. exclude the face-on outward strike-face diamonds from axial orientation
   authority and retain left/right sources for those faces; and
5. present every remaining contradiction as a blocked rule for Flamestrike.

## Stop Gate

`Blueprint block: axial internal component registration and projection-consistency rule missing.`

Flamestrike must approve or revise a bounded replacement measurement contract.
No source correction, interpretation preview, Step 02 contract, geometry,
Blender, texture, Unreal, or cone-sector UV work is authorized.
