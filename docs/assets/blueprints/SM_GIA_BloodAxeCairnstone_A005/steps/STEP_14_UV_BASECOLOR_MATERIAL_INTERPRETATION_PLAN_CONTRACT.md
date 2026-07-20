# A005 Step 14 UV, Base Color, And Material-Interpretation Plan Contract

Status: approved for complete Step 14 planning execution by Flamestrike's direct 2026-07-20 authority

Artifact classification: `authoritative execution boundary`

Contract ID: `A005-CR-STEP14-UV-BASECOLOR-MATERIAL-PLAN-A01`

Date: 2026-07-20

## Flamestrike Authority

Flamestrike stated:

`resume    You have full authority and approval to complete step 14 from start to finish regardless of what you need to do to complete it`

Under Core and the active Blueprint, this authorizes the complete bounded Step
14 planning lifecycle: prerequisite closeout verification, contract and input
lock, UV ownership decisions, Base Color ownership decisions, material/map
interpretations, texture delivery and validation planning, fail-closed audit,
visible planning review, status closeout, checkpoints, exact scoped Git
closeout, remote verification, and the mandatory restart.

This authority does not override the Blueprint boundary or turn planning into
Step 15 production.

## Controlling Decision

Approve one executable UV, Base Color, and material-interpretation plan that:

1. preserves exact visible source-owned RGB values without relabeling authored
   continuation or derived maps as source evidence;
2. assigns every future UV0 face to one source-owner view or one authored
   hidden/transition zone;
3. routes C-005, C-006, and C-007 only to their face-owned Base Color, Normal,
   and ORM consumers with no cross-face or hidden-face copy;
4. defines Normal, AO, roughness, metallic, bake, mip, filtering, naming,
   resolution, packing, and validation behavior;
5. makes the default non-emissive boundary final for this asset revision; and
6. creates no UV, image map, material, bake, or modified DCC artifact.

## Evidence / Interpretation Separation

Exact evidence is limited to the locked source and panel RGB bytes, approved
component/owner records, approved geometry and candidate hashes, and audited
status records.

The following are approved Step 14 interpretations, not source evidence:

- UV seam placement and island packing;
- normal-owner face routing for texture consumption;
- source-foreground mask derivation and mask-to-face placement;
- hidden and source-unowned Base Color continuation;
- shallow normal-only relief and stone microdetail;
- AO, roughness, metallic, bake, mip, and filtering behavior;
- texture compression/import intent; and
- the explicit decision to omit emissive.

Every future manifest and proof must retain those classifications.

## Required Outputs

- `manifests/STEP_14_INPUT_LOCK.json`
- `manifests/STEP_14_UV_OWNERSHIP_PLAN.json`
- `manifests/STEP_14_BASE_COLOR_OWNERSHIP_MANIFEST.json`
- `manifests/STEP_14_MATERIAL_INTERPRETATION_MANIFEST.json`
- `manifests/STEP_14_TEXTURE_DELIVERY_AND_VALIDATION_PLAN.json`
- `manifests/STEP_14_VALIDATION_MANIFEST.json`
- `review/STEP_14_UV_BASECOLOR_MATERIAL_PLAN_REVIEW.md`
- `steps/STEP_14_OUTPUT_RECORD.md`
- `handoffs/STEP_14_TO_STEP_15_HANDOFF.md`
- `Tools/DCC/audit_bloodaxe_cairnstone_a005_step14_plan.py`
- bounded updates to the A005 approval log, artifact index, reset/resume state,
  project drift ledger, and recovery journal.

## Required Planning Decisions

### UV0

- one unique, non-overlapping 0-1 UV0 layout;
- one material slot;
- source-owner views limited to front, back, left, right, and top;
- perspective remains non-metric corroboration and owns no texels;
- cardinal face ownership follows the approved R5/R7/R9 normal-owner routing;
- +Z-visible faces use top ownership;
- hidden closures, overlap faces, underside, and source-unowned transitions use
  authored stone zones;
- owner changes and component boundaries are UV seams, not claimed source
  seams;
- 16-pixel dilation per island and at least 32 pixels between independent
  source windows at 2048 resolution.

### UV1

- unique, non-overlapping lightmap channel;
- 128 planned lightmap resolution;
- minimum four-texel island padding at 128;
- component shells remain independently identifiable.

### Base Color

- 2048 x 2048, 8-bit RGB or opaque RGBA, sRGB;
- native source RGB is copied only at declared source-owned mask pixels;
- no resize, warp, interpolation, grading, hue/value change, baked AO, or
  lighting cleanup of those pixels;
- source masks and UV placement are interpreted routing data, not source
  evidence;
- source-unowned and hidden regions use explicitly authored stone
  continuation with no hidden red motif;
- exactness is asserted only for masked mip-0 RGB texels, never for rendered
  pixels, compression output, filtered samples, or lower mips.

### Normal / ORM / Material

- tangent-space DirectX/Unreal normal map; no displacement, parallax, or
  silhouette effect;
- C-005/C-006/C-007 share one shallow pigment-filled-incision treatment while
  retaining separate semantic IDs and face ownership;
- individual-course divisions, stone fissure depth, grain, chips, and
  micro-rubble are authored normal/Base Color consumers only;
- ORM packing is R=AO, G=Roughness, B=Metallic;
- metallic is zero for every texel;
- Base Color contains no added AO;
- emissive map and emissive material input are absent.

## Fail-Closed Rules

Step 14 blocks if any of the following occurs:

- an immutable input hash changes or is missing;
- the candidate `.blend` differs from the approved Step 13 hash;
- a source panel file or decoded RGB pixel hash differs;
- any source RGB is planned to be warped, filtered, graded, or relabeled;
- perspective becomes a UV/Base Color owner;
- an owner-view or hidden face class is unassigned or multiply assigned;
- a C-005/C-006/C-007 motif is copied across faces or onto a source-unseen
  face;
- emissive is enabled or an emissive texture is planned;
- UV, texture, material, bake, geometry, LOD, collision, FBX, Unreal, or
  visual-canon production occurs;
- the planning review is not opened visibly;
- an output lacks an artifact-status label; or
- scoped Git closeout includes unrelated user work.

## Validation Gates

The independent auditor must fail closed on at least these gate families:

1. all input paths and SHA-256 hashes;
2. source panel dimensions, file hashes, and decoded RGB hashes;
3. approved candidate and geometry-manifest identity;
4. UV0/UV1 ownership completeness, source-window bounds, and non-overlap;
5. exact-source versus authored Base Color separation;
6. C-005/C-006/C-007 face ownership and non-emissive routing;
7. map names, resolution, color spaces, channel packing, and material slot;
8. Normal, AO, roughness, metallic, bake, mip, filter, and validation rules;
9. zero Step 14 production outputs and unchanged DCC source;
10. review/output/handoff/status completeness; and
11. exact changed-path allowlist and JSON/Python syntax.

## Git And Restart Boundary

After a complete pass and visible review:

1. create a manual checkpoint;
2. stage only the dependency-complete Step 14 scope;
3. audit staged paths, secrets, JSON, Python syntax, and unstaged in-scope
   differences;
4. commit, push `main` to `assetforge`, and verify the remote hash;
5. record the proven closeout without self-embedding the metadata commit hash;
6. checkpoint again; and
7. stop for the mandatory post-Step-14 restart.

No Step 15 UV or texture/material candidate work may begin in this session.
