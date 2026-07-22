# A09 Full Pixel-Half Mirror Visual-Match Contract

- Contract ID: `SB-PHM-A09-FULL-MIRROR`
- Plan: `SB-PHM-A09`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Status: `approved by Flamestrike direction on 2026-07-22`

## Exact Authorized Step

Create one fresh full-length Siege Breaker half-model in Blender from the
unchanged front, left, and back source pixels; mirror the half at `X=0`; render
the completed candidate; audit it; and open the exact review image visibly.

## Required Inputs

- front source SHA-256:
  `d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95`;
- left source SHA-256:
  `1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b`;
- back source SHA-256:
  `15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799`;
- concept source SHA-256:
  `9f1ac142a5047968bb20c74216c2dccf61470ed9f4e21689ff01934bd849c586`;
- exact source rectangles from A06 Step 03, used as immutable pixel evidence;
- A09 visual-match scale formula from the authoritative A09 plan.

## Output Contract

- one local-only `.blend` containing the source half and applied mirrored half;
- one colored completed-model render;
- one untextured geometry render;
- one source/candidate/difference/geometry review board;
- one validation manifest and one independent audit;
- artifact classification: `DCC source candidate pending Flamestrike visual decision`.

## Prohibited

- estimated crop coordinates or hand-tuned source orientation;
- prior Siege Breaker candidate geometry, masks, textures, or `.blend` input;
- generated imagery, TRELLIS, TripoSR, diffusion, or image-to-3D;
- using source color projection as geometry proof;
- Unreal, FBX/GLB export, LODs, collision, or `Fully game-ready` claims;
- advancing after the visible review gate without Flamestrike approval.

## Decision

The step produces exactly one Flamestrike decision:
`approved`, `revise`, `rejected`, or `blocked` for the complete mirrored A09
visual-match candidate.
