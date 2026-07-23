# Step 10 Output Record A02 — Invalid

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Step: `10`
- Result: `INVALID after final-depth precedence discovery`
- Decision-record disposition:
  `authoritative within the recorded interpretation and numeric-substitution scope`
- Independent validation: `45/45 PASS`
- Geometry / Blender / export / Unreal executed:
  `false / false / false / false`

## Decision

Every parent Step 09 disagreement `DX001` through `DX005` and unknown `UK001`
through `UK012` is resolved by an existing Flamestrike-approved deterministic
rule. No new interpretation was introduced.

The newer R8 data-substitution boundary is also explicit:

- total length remains fixed at `170 cm`;
- all other overall and component dimensions follow the new pixel evidence;
- the older fixed `5/42/18/11 cm` component values are not carried into this
  run because doing so would require forbidden per-component scaling;
- approved equations, source ownership, closure rules, Rz180 completion, and
  the exact `pi/2` cylinder mapping remain unchanged.

## Evidence

- Decision record SHA-256:
  `262919a2d12b7948c4f6dcbf86f157e35af9234db862576c13a4ab4cbddae247`.
- Numeric-substitution record SHA-256:
  `77b579b9f194495898b6e7a44374991ebfdd5258d3803b38181209a476710853`.
- Independent validation SHA-256:
  `8ffd3746cb01fe6e3e876364aec28f4cf0c412ef56c999774f06b369b9fd53dc`.
- Independent validator SHA-256 at execution:
  `8c994cbed168f739ff77db240683c0d034e48b460a7363a364e8de220f404116`.

## Superseding Finding

The A02 audit did not require the record to distinguish the centered
top/bottom axial mean `47.479915237376 cm` from the later approved final
candidate depths `34.434306569343 cm` and `43.120437956204 cm`.

The later candidate rule controls final completed depth. The axial mean remains
comparison and orientation evidence and may not stretch either candidate.

## Disposition

This A02 record is `invalid`. A corrected Step 10 audit must test the final
depth precedence directly before Step 11 can unlock.
