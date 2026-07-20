# A005 Step 15 Core Recovery A01 Output Record

Status: Core Recovery complete; clean Step 15 rebuild passed all technical gates

Artifact classification: `authoritative recovery record`

Date: 2026-07-20

Contract: `A005-CR-STEP15-UV-TEXTURE-MATERIAL-CANDIDATE-A01`

## Detection And Decision

Internal inspection rejected the first generated Step 15 proof package before
it was presented for review. The front owner mask captured the printed `35cm`
dimension line and text, the top owner mask did not describe the intended
source object region, and the material board showed annotation-contaminated,
nearly black results.

Decision: `invalid_step15_source_owner_interpretation_attempt01`.

## Last Core-Valid State

The unchanged approved Step 13 source candidate remains the last valid
production state:

- path:
  `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_DCCSource_A01.blend`
- SHA-256:
  `5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095`
- pipeline status: `DCC source candidate`

## First Drift Action And Cause

The builder selected an object projection box from a three-pixel-dilated
foreground component. Dilation connected the central object to thin printed
annotations and grid/dimension marks. That contaminated component was then
treated as the UV placement domain.

This was an unproven interpretation of source ownership. The existing Step 14
rule explicitly excludes labels, grid lines, dimensions, arrows, borders, and
background from source-owned masks.

## Affected Outputs

Attempt 01's copied Blender candidate, candidate manifest, five owner masks,
Base Color, DirectX Normal, ORM, AO proof, texel classification, proof renders,
comparisons, audit JSON files, and review board are all `invalid` and
`quarantined`. They were never shown as valid approval evidence.

Quarantine:
`Saved/AssetForgeResearch/quarantine/SM_GIA_BloodAxeCairnstone_A005/Step15_Attempt01_20260720/`

## Recovery Action

1. Preserved the complete invalid output family and key hashes.
2. Verified the original approved Blender source still matches its locked hash.
3. Returned production paths to the pre-Step-15 state.
4. Required the clean rebuild to use a density-and-containment source-object
   selection that rejects thin annotation components before any owner mask is
   accepted.
5. Required an independent annotation-contamination gate and native mask
   inspection before material proof renders.

No geometry, source panel, Step 14 authority, or source Blender file changed.
The recovery does not authorize Step 16.

## Recovered Result

- Clean candidate SHA-256:
  `7befa56a10003c2d424de3db40e2bc402075b79644b0944413e97c92db6cab89`.
- Five independently checked source-object boxes exclude external labels and
  dimensions; owner pixels beyond selected object or two-pixel fringe: `0`.
- Native mask comparisons passed internal inspection before material proof
  rendering.
- Final independent audit: `18/18`; pending `0`; failures `0`.
- Recovered status:
  `pass_step15_candidate_complete_pending_focused_review`.

The recovered output is a new clean `candidate`, not a repaired or promoted
Attempt 01 artifact.
