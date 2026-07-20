# A005 Step 14 UV, Base Color, And Material Plan Output Record

Status: complete; authoritative Step 14 plan approved; mandatory restart required

Artifact classification: `authoritative Step 14 result record`

Contract ID: `A005-CR-STEP14-UV-BASECOLOR-MATERIAL-PLAN-A01`

Date: 2026-07-20

## Decision

`approved`

The planning package is the authority for later Step 15 UV, Base Color,
Normal, ORM, and material candidate work. Exact source evidence is limited to
declared mask-owned native RGB bytes at mip 0. Every UV, mask, continuation,
relief, response, bake, mip, and filter decision is labeled interpretation.

## Approved Package

- UV0: unique, non-overlapping 0-1; five normal-owner source windows; hidden
  and unowned faces route to authored stone; perspective owns no texels.
- UV1: unique lightmap plan at 128 resolution with four-texel padding;
  implementation deferred to Step 16.
- Base Color: 2K lossless sRGB; byte-exact owned native RGB; no warp,
  resample, grading, or baked AO; deterministic masks; authored continuation
  is never source-labeled.
- Normal: 2K DirectX tangent space; normal-only grain, chips, course divisions,
  and one shallow red pigment incision response.
- ORM: 2K linear R=AO/G=Roughness/B=Metallic; metallic identically zero.
- Material: one opaque Default Lit slot.
- Emissive: rejected and absent for A005 A01.
- Mips/filtering: lower mips and filtered rendering are derived behavior;
  exactness applies only to owned mip-0 RGB texels.
- Step 15 acceptance plan: 18 fail-closed gates.

## Technical Result

`pass_authoritative_step14_plan_complete`

- Locked inputs: `32/32`.
- Source panels: `6/6` file, size, and decoded RGB identities.
- Texture-owner views: `5`; perspective owners: `0`.
- Primary components routed: `4/4`.
- Planned texture maps: `3`; planned emissive maps: `0`.
- First complete independent plan audit: `32/32`; failures: `0`.
- Production outputs, DCC saves, and downstream runs: `0`.
- Approved candidate remains byte-identical at
  `5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095`.

## Classification Boundary

- Step 14 contract, UV/Base Color/material/delivery plans, review, output,
  handoff, and status records: `authoritative` within the planning scope.
- Input lock and validation manifest: `proof only` except the input lock's
  execution-boundary role.
- Blender candidate and geometry manifest: unchanged `candidate`.
- Future UVs, masks, maps, material, and renders: do not exist; later
  `candidate` status only after Step 15 creates and validates them.
- DCC game-ready, fully game-ready, finished appearance, and visual canon:
  false.

## Required Next Action

Finish exact scoped Git closeout, push and remotely verify `assetforge/main`,
record the closeout metadata, checkpoint, and stop for the mandatory restart.
After restart, only preparation of a separate Step 15 contract is permitted.
