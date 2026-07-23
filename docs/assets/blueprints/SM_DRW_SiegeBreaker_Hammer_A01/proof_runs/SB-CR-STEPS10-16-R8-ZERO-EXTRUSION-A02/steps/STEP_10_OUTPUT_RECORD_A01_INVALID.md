# Step 10 Output Record A01 — Invalid

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Step: `10`
- Result: `INVALID after incomplete-audit discovery`
- Decision-record disposition:
  `authoritative within the recorded interpretation-rule scope`
- Independent validation: `33/33 PASS`
- Geometry / Blender / export / Unreal executed:
  `false / false / false / false`

## Decision

Every parent Step 09 disagreement `DX001` through `DX005` and unknown `UK001`
through `UK012` is resolved by an existing Flamestrike-approved deterministic
rule. No new interpretation was introduced.

The controlling production consequences are:

- front-owned width `97.873941674506 cm`;
- centered top/bottom depth `47.479915237376 cm`;
- rune-side completed depth `34.434306569343 cm`;
- metal-center-piece completed depth `43.120437956204 cm`;
- right-image construction axis `x=557`;
- front-owned longitudinal stations;
- measured common boundaries and straight ruled hidden closure only;
- exactly one whole-asset Rz180 completion;
- exact radius-versus-Z rotational surfaces;
- exact `theta(U)=-pi/2+pi*U` haft mapping.

## Evidence

- Decision record SHA-256:
  `262919a2d12b7948c4f6dcbf86f157e35af9234db862576c13a4ab4cbddae247`.
- Independent validation SHA-256:
  `f903919fe97cfa9c8d6a4235d19802cce66d0a7232a44d569282fa320d9bc39d`.
- Independent validator SHA-256 at execution:
  `5fb0bb9d4f2a54f29d2c0e98235c0bbd36cd3644f4f834736d9be73d1231df87`.

## Superseding Finding

The A01 audit did not test the newer R8 contract's numeric-substitution
precedence over the older fixed `5/42/18/11 cm` component values. Those older
values would require forbidden per-component normalization under the new
pixel-derived run. This record cannot unlock Step 11.

## Disposition

This A01 record is `invalid`. A corrected Step 10 audit must directly prove
that only total length remains fixed and all other dimensions come from the
new Step 01-09 measurements before Step 11 can unlock.
