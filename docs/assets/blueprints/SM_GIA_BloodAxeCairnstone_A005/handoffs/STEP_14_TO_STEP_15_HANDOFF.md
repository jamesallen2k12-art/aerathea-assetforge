# A005 Step 14 To Step 15 Handoff

Status: Step 14 complete; authoritative UV/Base Color/material plan approved; mandatory restart required; Step 15 contract preparation only after restart

Artifact classification: `authoritative post-Step-14 routing`

Contract ID: `A005-CR-STEP14-UV-BASECOLOR-MATERIAL-PLAN-A01`

Date: 2026-07-20

## Approved Boundary

The Step 14 planning package is authoritative for later Step 15 candidate
work. The approved geometry remains byte-identical at:

`5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095`.

Pipeline status remains `DCC source candidate`. No UV, source mask, texture,
material, bake, or modified Blender candidate exists.

## Proven Step 14 Result

- `32/32` immutable inputs matched.
- `6/6` source panels retained exact file, dimensions, and decoded RGB hashes.
- Five owner-view source windows and one authored zone are fully bounded.
- Four primary components have complete visible/hidden face-routing rules.
- Base Color evidence/interpretation separation is explicit.
- Normal, ORM, AO, roughness, metallic, bake, mip, and filtering behavior is
  bounded and testable.
- C-005/C-006/C-007 remain face-owned with no cross-face or hidden copy.
- Emissive is rejected and absent.
- First complete read-only planning audit passed `32/32`.
- Production outputs and downstream work: `0`.

## Step 15 Preparation Boundary

After the mandatory restart, Step 15 may prepare and visibly present one
separate UV and Texture/Material Candidate contract. That future contract must
lock the Step 14 package and approved candidate, then implement only:

- one UV0 layout under `STEP_14_UV_OWNERSHIP_PLAN.json`;
- five deterministic owner masks;
- 2K Base Color, DirectX Normal, and ORM maps;
- one non-emissive material candidate;
- exact RGB, UV, bake, map, and material audits; and
- five owner-view plus one perspective proof render after technical pass.

The future candidate must pass all 18 Step 15 gates recorded in
`STEP_14_TEXTURE_DELIVERY_AND_VALIDATION_PLAN.json`.

## Still Unauthorized

- Step 15 execution before a separate contract is prepared and approved;
- geometry repair, retopology, smoothing, sculpting, or silhouette change;
- source raster warp, grading, filtered ingestion, or manual mask correction;
- cross-face or hidden-face motif copy;
- emissive map or emissive material input;
- UV1 implementation before its later authorized DCC game-ready step;
- LOD, collision, FBX, Unreal, or visual-canon work;
- staging or committing unrelated user work.

## Restart Instruction

Stop after Step 14 checkpoint, exact scoped commit/push, remote verification,
and closeout metadata. On resume, inspect the latest checkpoint, Step 14
contract/input lock/plans/validation/review/output/handoff, approved candidate
hash, and reset/resume record before preparing any Step 15 contract.
