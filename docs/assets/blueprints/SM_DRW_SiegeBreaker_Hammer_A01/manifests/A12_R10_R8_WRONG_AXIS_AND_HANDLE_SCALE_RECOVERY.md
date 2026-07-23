# A12 R10 R8 Wrong-Axis And Handle-Scale Recovery

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Rejected attempt:
  `A12_R10_R8ScanlineNewDimensionsRz180_A01`
- Rejection authority:
  `Flamestrike`
- Artifact status:
  `invalid / quarantined`

## Last Core-Valid Evidence

- immutable new R8 images and scanline captures;
- exact new dimension consequence;
- exact right-view diamond center `x=557`;
- exact right-view half-rotation registration;
- approved physical handle locks;
- approved `pi/2` haft wrap formula.

## First Drift

The rejected builder bisected the new front image at its X center and retained
`X>=0`. The explicit right-diamond registration requires a side-image depth
half ending at `x=557`, mapped to `Y<=0`.

## Handle Error

The rejected handle ended at the straight-shaft start `C`,
`Z=113220/1111 cm`, instead of including the upper coupler up to approved
boundary `A`, `Z=132 cm`.

The missing span was:

`33432/1111 = 30.091809180918 cm`.

The handle profile also used a global new-image Z mapping instead of
component-local grip, pommel, and upper-handle registrations.

## Affected Outputs

- rejected A01 Blender source;
- A01 validation and audit;
- A01 front/right/back/color/gray renders;
- A01 review board and output record.

All are `invalid / quarantined`. Their new source hashes, scanline replays,
dimension calculations, and audit mechanics remain `proof only`.

## Quarantine

`Saved/AssetForgeResearch/SiegeBreaker/A12_R10_R8_NewDimensions_WrongAxis_UserReject_20260723/`

## Smallest Sufficient Recovery

Build two fresh candidates from the two exact right-view halves around
`x=557`, map the half into `Y<=0`, complete it once with the documented Rz180
operation, extend the corrected handle through the upper coupler to `Z=132`,
apply the exact physical handle locks and cylinder formula, audit both, and
present one comparison board.

No rejected mesh may be repaired forward or reused.

## Recovery Result

- Rune-side builder / independent audit:
  `26/26 PASS / 52/52 PASS`.
- Metal-center-piece builder / independent audit:
  `26/26 PASS / 52/52 PASS`.
- Correct axis:
  `right-image depth half Y<=0 around x=557`.
- Correct handle top:
  `A=132 cm`.
- Review artifact:
  `review/A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01/A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01_REVIEW.png`.
- Recovered artifact status:
  `two DCC source candidates pending Flamestrike comparison`.
- The quarantined wrong-axis candidate remains:
  `invalid / quarantined`.
