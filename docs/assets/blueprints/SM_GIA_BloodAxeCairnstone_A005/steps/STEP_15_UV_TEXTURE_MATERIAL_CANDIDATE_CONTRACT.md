# A005 Step 15 UV And Texture/Material Candidate Contract

Status: approved for complete Step 15 execution by Flamestrike's direct 2026-07-20 authority

Artifact classification: `authoritative execution boundary`

Contract ID: `A005-CR-STEP15-UV-TEXTURE-MATERIAL-CANDIDATE-A01`

Date: 2026-07-20

## Flamestrike Authority

Flamestrike stated:

`resume You have full Approval and Authority to complete step 15 from start to finish regardless of what that requires`

Under Core and the active Blueprint, this authorizes the complete bounded Step
15 lifecycle: contract and input lock, one copied UV-ready Blender candidate,
five deterministic native owner masks, 2K Base Color/DirectX Normal/ORM maps,
one non-emissive material candidate, independent technical and exactness
audits, fixed-camera material proof renders after technical pass, visible
review, status closeout, checkpoints, exact scoped Git closeout, remote
verification, and the mandatory restart.

This authority does not override the Blueprint or authorize Step 16 work.

## Controlling Decision

Create and validate one UV and texture/material candidate from the approved
Step 13 geometry and the authoritative Step 14 plan without changing approved
geometry.

The decision output must be one of:

- `pass_step15_candidate_complete_pending_focused_review`;
- `blocked_step15_candidate_gate_failure`; or
- `invalid_step15_scope_or_geometry_violation`.

## Locked Production Boundary

- Asset: `SM_GIA_BloodAxeCairnstone_A005` only.
- Approved source candidate SHA-256:
  `5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095`.
- The source candidate is opened read-only and copied to
  `SM_GIA_BloodAxeCairnstone_A005_UVTextureMaterialCandidate_A01.blend`.
- Mesh vertex coordinates, face vertex indices, transforms, bounds,
  component identities, watertight topology, and `784` evaluated triangles
  must remain unchanged.
- One UV0 layer named `UVMap` is permitted. UV1 is forbidden in Step 15.
- One shared material slot named `M_GIA_BloodAxeCairnstone_A005` is
  permitted across the four approved component objects.

## Required Candidate Outputs

1. One UV0 layout under `STEP_14_UV_OWNERSHIP_PLAN.json`.
2. Five native-resolution source-owned masks for front, back, left, right,
   and top; perspective owns no texels.
3. `T_GIA_BloodAxeCairnstone_A005_BC.png`, 2048 x 2048, lossless sRGB.
4. `T_GIA_BloodAxeCairnstone_A005_N.png`, 2048 x 2048, linear DirectX
   tangent normal.
5. `T_GIA_BloodAxeCairnstone_A005_ORM.png`, 2048 x 2048, linear packed
   R=AO, G=Roughness, B=Metallic.
6. One opaque, one-sided, non-emissive material candidate in the copied
   Blender file.
7. Candidate and texel-classification manifests with hashes and exact
   evidence-versus-interpretation labels.
8. An independent technical audit against all 18 Step 15 gates.
9. Five owner-view and one perspective fixed-camera material proof render,
   native mask comparisons, and one review board after the technical audit
   passes.

## Evidence And Interpretation Rules

Exact evidence is limited to locked files and hashes, approved geometry data,
and byte-identical source RGB copied at declared mask-owned mip-0 texels.

The following remain approved interpretations and must never be relabeled as
source evidence: source masks, component/face raster coverage, UV placement,
UV seams and packing, authored continuation, dilation, stone palettes, Normal
detail, AO, roughness, bake results, mips, filtering, material response, and
all rendered pixels.

The five masks must use the exact deterministic Step 14 rule. Manual pixel
editing is forbidden. If a mask admits labels/grid/dimensions or excludes the
approved face-owned material surface, execution fails closed; the mask must
not be hand-corrected.

## Texture And Material Rules

- Source panels are ingested at integer texels with nearest/point access only;
  they are never moved, resized, warped, graded, or filtered into Base Color.
- Every mask-owned Base Color mip-0 RGB triplet equals the source triplet at
  the same native panel coordinate plus the fixed atlas-window offset.
- Every other atlas texel is classified as authored continuation, dilation,
  or unused padding.
- Visible authored stone colors use deterministic component-local eight-color
  palettes derived from owned non-red stone pixels. Hidden contacts and the
  underside use bounded dark component-local stone continuation.
- C-005/C-006/C-007 remain separate semantic IDs but share only the approved
  face-owned red Base Color, shallow normal-only incision, and pigment
  roughness response. No hidden or cross-face decoration is permitted.
- Normal is DirectX tangent space. Displacement, parallax, and silhouette
  control are forbidden.
- AO uses the unchanged four-shell candidate and the recorded Step 14 bake
  settings. AO never multiplies into Base Color.
- Roughness stays within the approved stone, pigment, and hidden-stone
  ranges. Metallic is byte value `0` for every texel.
- Emissive texture creation, emissive node linkage, and emitted red markings
  are forbidden.

## Required Audit Sequence

1. Schema-only builder and auditor preflight; no `bpy` import and no writes.
2. Verify every Step 15 locked input and all source pixel identities.
3. Build the candidate once from the approved source copy.
4. Audit geometry identity, UV0, UV1 absence, windows, masks, RGB exactness,
   texel classification, maps, bake, material, classification, and firewall.
5. If any of the 18 gates fails, stop before proof rendering.
6. After all 18 gates pass, render the six fixed material views and package
   native-resolution evidence plus a presentation board.
7. Open the review board and review record visibly.
8. Record the pass, blocked, or invalid classification without self-approval
   beyond this contract's technical candidate decision.

## Fail-Closed Conditions

Step 15 stops if any locked hash changes; geometry differs; a source raster is
modified or resampled into Base Color; a UV is outside its authorized window
or has positive-area overlap; UV1 exists; masks fail their deterministic
rule; exact RGB differs; metallic is nonzero; emissive exists; material slots
exceed one; proof framing is clipped or misoriented; or A001-A004/quarantined
A005 diagnostics enter the input chain.

## Explicitly Forbidden

- geometry repair, retopology, smoothing, sculpting, fitting, or silhouette
  change;
- source-raster warp, resize, grading, filtered Base Color ingestion, or
  manual mask correction;
- cross-face or hidden-face motif copy;
- UV1, LOD, collision, FBX, Unreal, or visual-canon work;
- staging, committing, or pushing unrelated user work; and
- promotion to `DCC game-ready candidate`, `Fully game-ready`, finished
  appearance, or visual canon.

## Acceptance And Closeout

Pass requires all 18 gates in
`STEP_14_TEXTURE_DELIVERY_AND_VALIDATION_PLAN.json`, six clean fixed-camera
proofs, five native mask/source comparisons, one visible review board, exact
artifact hashes, candidate classification, and zero forbidden outputs.

The pass status is `candidate pending focused review; not DCC game-ready`.
After pass and visible review: checkpoint, stage only the dependency-complete
Step 15 scope, audit staged paths/syntax/secrets and unstaged in-scope
differences, commit, push `main` to `assetforge`, verify the remote hash,
record closeout metadata, checkpoint again, and stop for the mandatory
post-Step-15 restart.
