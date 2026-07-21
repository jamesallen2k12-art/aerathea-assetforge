# A005 Visual Correction A02 Contract

Status: completed; technical pass pending Flamestrike visual approval

Artifact classification: `authoritative execution contract`

Contract ID: `A005-CR-VISUAL-CORRECTION-A02`

## Goal

Correct the visually rejected A01 DCC package without changing the approved
A005 source authority or escalating to Unreal. The accepted A02 image must
show the complete three-band base as a plinth/upper tier, seated lower tier,
and debris-surrounded apron, and its displayed stone and pigment colors must
measure within the declared source-comparison tolerances.

## Authority

- Flamestrike approval on 2026-07-20: full approval and authority to complete
  the active correction.
- Restart handoff:
  `SM_GIA_BloodAxeCairnstone_A005_A02_VISUAL_CORRECTION_RESTART_HANDOFF.md`.
- Source:
  `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`.
- Geometry authority: `manifests/STEP_11_CONSTRUCTION_BLUEPRINT.json`.
- UV/material authority: `manifests/STEP_14_UV_OWNERSHIP_PLAN.json` and
  `manifests/STEP_14_MATERIAL_INTERPRETATION_MANIFEST.json`.

## Locked Scope

1. Preserve `140 x 110 x 220 cm`, bottom-center pivot, `35 cm` base,
   four primary watertight shells, one runtime material, LOD0-LOD3, four
   collision proxies, and source-owned Base Color texels.
2. Correct only the A005 base profiles, authored atlas continuation, Default
   Lit shader chain, neutral review lighting/color management, and camera
   presentation needed to resolve the recorded A01 findings.
3. Create A02-suffixed Blender, FBX, texture, manifest, audit, and final-image
   outputs. Preserve A01 byte-for-byte.
4. Run the inherited technical gates plus explicit base-component bounds,
   projected base-band visibility, A01 preservation, non-metallic material,
   and displayed-color comparison gates.
5. Open only the accepted final A02 image for Flamestrike review.

## Forbidden

- Source modification or source grading.
- A001-A004 production geometry as authority.
- A01 overwrite or deletion.
- Intermediate-image desktop review.
- Unreal/Step 17 work.
- `Fully game-ready`, approved-library, or visual-canon promotion claims.

## Decision Output

The step must end as one of:

- `candidate`: all A02 technical and internal visual gates pass; final image
  is pending Flamestrike approval.
- `blocked`: an authority, technical, projection, or color gate fails.
- `quarantined`: a generated A02 attempt fails internal review and is retained
  only as non-authoritative evidence.
