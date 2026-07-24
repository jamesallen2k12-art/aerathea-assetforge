# Shared-Depth Recovery Blueprint A01 Approved Handoff

- Date: `2026-07-24`
- Assets:
  - `SM_DRW_SiegeBreaker_Hammer_A01` / Siege Breaker
  - `SM_DRW_FoeHammer_Hammer_A01` / Foe Hammer
- Blueprint status: `authoritative`
- Blueprint validation: `proof only; 66/66 PASS`
- Authority-lock validation: `proof only; 43/43 PASS`
- Current action: `stop`
- Builder authority: `false`
- Blender authority: `false`
- Geometry authority: `false`
- Step 13 authority: `false`
- Unreal authority: `false`

## Approval Outcome

Flamestrike approved `SHARED_DEPTH_RECOVERY_BLUEPRINT_A01` as the governing
blueprint.

The exact reviewed blueprint remains byte-identical:

- Blueprint SHA-256:
  `efdbd8795dff2031fcde9e734868ff4c617dc37ad1e7b3743c3727daea981d58`.
- Decision approval record SHA-256:
  `94b30875014cfbf088568cb2b2305fd64449166c3617b8524c8ad5346f4ca7aa`.
- Authority lock SHA-256:
  `6889b826481e5e11dd10775f2b81467b1014687b7fda9ebbff62d519bfff09bc`.
- Authority-lock validation SHA-256:
  `154ac1ed96c437fe971dfd27c415141f70ea08ae8ee43ae72251d1b30a016739`.

## Governing Twin Rule

Both assets must have exact overall dimensions:

`50719500/517681 × 6644212/149985 × 170/1 cm`

Decimal XYZ:

`97.974428267601 × 44.299176584 × 170 cm`

The shared body must be canonically identical. Only the tagged local `C04`
treatment may differ:

- Siege Breaker: double rune sided.
- Foe Hammer: double metal-center-piece sided.

The rune and metal source spans remain local, unstretched treatments. They do
not own or clip global depth.

## Locked Recovery Guards

- `EQ_CANDIDATE_AXIAL_INTERSECTION` is invalid and forbidden.
- Candidate-specific global body depth is forbidden.
- The common envelope is a validation bound, not unowned fill geometry.
- Both quarantined Step 12 meshes are forbidden as construction input.
- A future build must create one canonical shared base and prove its hash
  equality across both variants.
- Cross-asset XYZ bounds tolerance is exactly `0/1 cm`.

## Governing Records

- Blueprint:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01.json`
- Decision approval:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_DECISION_APPROVAL_RECORD.md`
- Authority lock:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK.json`
- Authority-lock validation:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK_VALIDATION.json`

## Next Gate

No production action is active.

The next production-moving action requires a separately stated visible
fresh-builder contract and separate Flamestrike approval. Blueprint approval
does not authorize code changes, Blender, geometry, a Foe Hammer source fork,
Step 13, retopology, UVs, baking, export, or Unreal.
