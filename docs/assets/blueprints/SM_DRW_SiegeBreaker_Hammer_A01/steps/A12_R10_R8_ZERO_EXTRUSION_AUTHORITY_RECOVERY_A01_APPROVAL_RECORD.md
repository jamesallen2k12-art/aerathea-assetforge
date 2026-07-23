# A12 R10 R8 Zero-Extrusion Authority Recovery A01 Approval Record

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Run: `SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01`
- Artifact status: `authoritative`
- Approving authority: `Flamestrike`
- Approval response: `I agree with you ... proceed`
- Scope: `authority-only recovery; no production geometry`

## Approval Context

The immediately preceding recommendation was to:

1. formally lock the current zero-extrusion execution instructions;
2. confirm the newer 180-degree whole-asset completion rule;
3. remove the conflict with the older Y-depth reflection clause; and
4. stop before geometry until that written authority was consistent.

Flamestrike approved that recommendation.

## Approved Decisions

1. The existing file
   `steps/A12_R10_R8_PIXEL_EXACT_STEPS01_16_A01_CONTRACT.md`
   remains byte-for-byte unchanged and is locked at SHA-256:

   `77b0339126388be01f59532cd6b79228450b61e739ebc10c2f849833fd337bd4`.

2. For this R8 pixel-exact run, construct one coherent measured source half
   and complete the whole asset exactly once with:

   `Rz(180 degrees): (X,Y,Z)->(-X,-Y,Z)`.

3. For this R8 run only, Decision 2 supersedes the older final-duplicate
   requirement
   `(X,Y,Z)->(X,-Y,Z)`
   in
   `steps/A12_R10_STEP02_COMPONENT_EQUATION_CONTRACT_DRAFT.md`.

4. The supersession is limited to the whole-asset completion transform. Every
   other approved component equation, source-pixel owner, measurement,
   combined-boundary rule, hidden-closure rule, cylinder-wrap rule, and
   fail-closed gate remains in force.

## Result

- The reset-handoff contract-fingerprint mismatch is resolved.
- The completion-transform conflict is resolved.
- Steps 01-09 retain their existing authoritative measurement scope.
- All rejected Steps 10-16 outputs remain `invalid / quarantined`.
- No old mesh, builder output, or rejected blueprint is restored.
- The next permitted gate is a fresh Step 10 zero-extrusion method-binding
  blueprint based only on valid Step 01-09 evidence and the approved component
  process.

## Authority Ceiling

This approval does not authorize geometry, Blender, rendering, textures,
export, Unreal, or game-ready classification. Those remain behind their
existing gates.
