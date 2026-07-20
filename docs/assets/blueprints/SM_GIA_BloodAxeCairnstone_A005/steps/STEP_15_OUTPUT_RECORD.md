# A005 Step 15 UV / Texture / Material Candidate Output Record

Status: technically complete candidate; pending focused visual review; mandatory restart required after closeout

Artifact classification: `authoritative Step 15 technical result record`

Contract ID: `A005-CR-STEP15-UV-TEXTURE-MATERIAL-CANDIDATE-A01`

Date: 2026-07-20

## Decision

`pass_step15_candidate_complete_pending_focused_review`

Step 15 has produced one validated UV, texture, and material candidate from
the approved source without changing geometry. Flamestrike's focused visual
approval remains pending; technical completion does not self-approve the
appearance.

## Candidate Result

- Candidate blend SHA-256:
  `7befa56a10003c2d424de3db40e2bc402075b79644b0944413e97c92db6cab89`.
- Source blend SHA-256 remains:
  `5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095`.
- Geometry changes: `0`; evaluated triangles: `784`.
- UV0: one layer, `464/464` faces assigned, overlaps `0`; UV1 absent.
- Source masks: `5`; annotations owned: `0`; manual edits: `0`.
- Exact source RGB audit: passed at every declared mask-owned mip-0 texel.
- Maps: one 2K sRGB Base Color, one 2K linear DirectX Normal, and one 2K
  linear ORM; metallic zero; emissive absent.
- AO: equivalently audited deterministic BVHTree ray bake, `438272` rays,
  target raster misses `0`.
- Material: one shared opaque, one-sided, non-emissive slot.
- Proofs: six renders, five mask comparisons, six material comparisons, one
  board; clipped views `0`.
- Independent final audit: `18/18`; pending `0`; failures `0`.

## Core Recovery

Attempt 01 was internally rejected before presentation because source-object
selection admitted printed annotations. Its full output family is `invalid`
and `quarantined`. The clean result was rebuilt from the unchanged approved
source; no drifted file was repaired forward or promoted.

Recovery record:
`steps/STEP_15_CORE_RECOVERY_A01_OUTPUT_RECORD.md`.

Drift ledger:
`docs/projects/assetforge/DRIFT_LEDGER.md`.

## Classification Boundary

- Step 15 contract and this technical result record: `authoritative` within
  the completed technical execution scope.
- Candidate blend, candidate manifest, masks, maps, and material:
  `candidate`.
- Validation and all visual evidence: `proof only`.
- Attempt 01 family: `invalid; quarantined`.
- Pipeline status remains `DCC source candidate`.
- DCC game-ready, fully game-ready, finished appearance, and visual canon:
  false.

## Git Closeout

The exact dependency-complete Step 15 snapshot will be committed and pushed
before the mandatory restart. Its verified commit/checkpoint metadata will be
recorded immediately after remote verification without staging unrelated user
work.

## Required Next Action

Open the review board and review record visibly, complete exact scoped Git
closeout, then stop for the mandatory restart. Step 16 is not authorized.
