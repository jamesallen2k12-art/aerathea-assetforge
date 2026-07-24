# Shared-Depth Recovery Blueprint A01 Decision Approval Record

- Date: `2026-07-24`
- Approving authority: `Flamestrike`
- Assets:
  - `SM_DRW_SiegeBreaker_Hammer_A01` / Siege Breaker
  - `SM_DRW_FoeHammer_Hammer_A01` / Foe Hammer
- Decision: `approved`
- Artifact status: `authoritative approval record`
- Builder authority: `false`
- Blender authority: `false`
- Geometry authority: `false`
- Step 13 authority: `false`
- Unreal authority: `false`

## Exact Approval

Codex asked:

> Do you approve `SHARED_DEPTH_RECOVERY_BLUEPRINT_A01` as the governing
> blueprint?

Flamestrike replied:

> approved

The approval applies to the exact reviewed and independently validated
artifact package below.

## Approved Hash-Locked Package

### Blueprint

- Path:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01.json`
- SHA-256:
  `efdbd8795dff2031fcde9e734868ff4c617dc37ad1e7b3743c3727daea981d58`
- Pre-decision internal status:
  `candidate pending Flamestrike approval`
- Effective status after this decision:
  `authoritative shared-depth recovery blueprint`

### Independent Validation

- Path:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_VALIDATION.json`
- SHA-256:
  `48e53e3ddfff94319927aebaec47fcbe9c40ea7369c20a4b73cdc0c38fa47ff5`
- Status: `proof only; 66/66 PASS`

### Visible Review

- Path:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/review/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_REVIEW.md`
- SHA-256:
  `48f5e748b89682f8297686d409f97909b48468777988a143174d34760faa62c9`
- Status: `reviewed candidate; approval now recorded here`

## Approved Governing Rules

- Both assets have exact overall dimensions:
  `50719500/517681 × 6644212/149985 × 170/1 cm`.
- Decimal XYZ:
  `97.974428267601 × 44.299176584 × 170 cm`.
- The nonvariant shared body must be canonically identical.
- Siege Breaker is double rune sided.
- Foe Hammer is double metal-center-piece sided.
- The rune and metal source spans remain unstretched local `C04` treatments.
- Only the tagged local `C04` treatment may differ.
- `EQ_CANDIDATE_AXIAL_INTERSECTION` is invalid and forbidden.
- The common envelope is a validation bound and may not be used as unowned
  fill geometry.
- Neither quarantined Step 12 mesh may be reused or repaired forward.

## Authority Boundary

This decision approves the governing blueprint only.

It does not authorize:

- changing or running builder code;
- opening Blender;
- creating or modifying geometry;
- creating a standalone Foe Hammer source;
- retopology, UVs, baking, textures, materials, LODs, or collision;
- export;
- Step 13; or
- Unreal work.

## Next Gate

The next production-moving action requires a separate visible fresh-builder
contract and separate Flamestrike approval. No action follows automatically
from this decision record.
