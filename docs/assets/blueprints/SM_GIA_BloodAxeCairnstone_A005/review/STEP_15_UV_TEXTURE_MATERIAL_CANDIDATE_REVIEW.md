# A005 Step 15 UV / Texture / Material Candidate Review

Status: technically complete candidate; pending Flamestrike focused visual review; mandatory restart required

Artifact classification: `candidate review package; proof only`

Contract ID: `A005-CR-STEP15-UV-TEXTURE-MATERIAL-CANDIDATE-A01`

Candidate SHA-256:
`7befa56a10003c2d424de3db40e2bc402075b79644b0944413e97c92db6cab89`

## Technical Decision

`pass_step15_candidate_complete_pending_focused_review`

The clean Step 15 candidate passes all `18/18` independent technical gates.
It is ready for Flamestrike's focused visual decision as a `candidate`; it is
not self-approved appearance, DCC game-ready, fully game-ready, or visual
canon.

## What Is Proven

- The approved source Blender file remains byte-identical at
  `5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095`.
- Geometry changes are `0`; the candidate remains four objects, `400`
  vertices, `464` faces, and `784` evaluated triangles.
- Exactly one UV0 named `UVMap` covers all `464` faces once with zero
  positive-area overlap; UV1 does not exist.
- Five native owner masks match independent reconstruction, contain no manual
  pixel edits, and have zero owned pixels outside the independently selected
  source object or its two-pixel fringe.
- Every declared source-owned mip-0 Base Color RGB texel matches its native
  source RGB byte-for-byte.
- Base Color, DirectX tangent Normal, and ORM are all 2048 by 2048. Metallic
  is identically zero; emissive and displacement are absent.
- One opaque, one-sided material is shared by the four objects.
- Six fixed-camera material renders, five native mask comparisons, and six
  native material comparisons are present and unclipped.

## Core Recovery History

Attempt 01 was rejected internally before visible presentation. Its
three-pixel foreground dilation connected the source object to dimension and
annotation components. The complete invalid family is preserved as
`quarantined` under:

`Saved/AssetForgeResearch/quarantine/SM_GIA_BloodAxeCairnstone_A005/Step15_Attempt01_20260720/`

The clean candidate was rebuilt from the unchanged Step 13 source. Attempt 02
selects the largest raw eight-connected foreground component before any
growth, independently verifies component dominance/density/containment, and
requires zero owner-mask pixels beyond the selected object or approved fringe.
No mask was hand-corrected.

## Visible Evidence

- Review board:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/Step15/SM_GIA_BloodAxeCairnstone_A005_STEP15_UV_TEXTURE_MATERIAL_CANDIDATE_REVIEW_BOARD.png`
- Five native mask comparisons and six native source/material comparisons:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/Step15/`
- Tracked validation summary:
  `manifests/STEP_15_VALIDATION_MANIFEST.json`

The board contains presentation thumbnails only. Native comparisons remain
the review evidence. Rendered pixels are interpretation and do not expand the
exact RGB claim beyond declared source-owned mip-0 texels.

## Focused Visual Decision

Flamestrike retains final authority to:

- approve this candidate for later Step 16 DCC game-ready planning;
- reject it and identify the specific visible UV/material issue; or
- mark it blocked if the visible evidence is insufficient.

The current technical closeout does not infer that decision.

## Still Deferred

- UV1/lightmap implementation;
- LOD0-LOD3 production;
- collision;
- FBX export;
- Unreal import/configuration/placement/validation;
- DCC game-ready and fully game-ready classification;
- visual-canon promotion.

No Step 16 work is authorized by this review package.
