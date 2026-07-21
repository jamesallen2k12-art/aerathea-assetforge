# A005 Visual Correction A02 Output Record

Status: technical pass; pending Flamestrike visual approval

Artifact classification: `authoritative technical result record`

Date: 2026-07-20

Contract ID: `A005-CR-VISUAL-CORRECTION-A02`

## Decision

The bounded A02 correction is technically complete. The package passes all
`26/26` independent gates and is classified as a `candidate` with pipeline
status `DCC game-ready candidate`. This result does not self-approve the
appearance, authorize Unreal work, or promote the asset to `Fully game-ready`.

The A01 visual package remains `quarantined`; its technical evidence remains
`proof only`. A01 preservation hashes passed without modification.

## Corrected Result

- The base is four closed primary shells with three independently readable
  projected base bands: apron `49.47 px`, lower tier `64.64 px`, and upper
  tier `60.00 px` in the accepted final camera.
- The exact assembled bounds remain `140 x 110 x 220 cm` with pivot
  `[0,0,0]`.
- LOD triangles remain `8672 / 3988 / 1820 / 692`.
- One material, two UV layers per LOD, four custom collision proxies, and four
  FBXs are present.
- Clean FBX re-import passes `4/4`.
- All `154948` source-owned Base Color pixels match exactly; mismatches are
  `0`.
- The final material uses direct sRGB Base Color, DirectX Normal, ORM
  roughness, zero metallic, and no gamma, grading, or emissive path.
- Neutral presentation uses Standard transform, zero exposure, gamma `1`,
  neutral-white lights, a complete silhouette, and no ground intersection.
- Source-versus-render stone median RGB is `[49,46,43]` versus `[55,53,50]`,
  distance `11.58`; the median luminance delta is `+6`.

## Evidence

- Validation:
  `manifests/VISUAL_CORRECTION_A02_VALIDATION.json`
- Validation result:
  `pass_a02_dcc_game_ready_candidate_pending_flamestrike_visual_approval`
- Blender candidate:
  `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_DCCGameReady_VisualCorrection_A02.blend`
- Blender SHA-256:
  `692b6a34280601153affc6cc665d3fe0dbb0fca1c54340c07bff80242985c509`
- Candidate manifest SHA-256:
  `4ebac1aaeef50eb60fe4e820f07e3d0d3b220c3b86ad38383638dce7bc2fe177`
- Final review image:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A02/SM_GIA_BloodAxeCairnstone_A005_FINAL_CORRECTED_3D_A02.png`
- Final review image SHA-256:
  `511664eb9ea4192f9d86cd1d08f320158b1d70df6a57bfc2130543c80c47247d`

## Artifact Routing

- A02 contract, plan, and this result record: `authoritative` for the bounded
  execution and technical outcome.
- A02 Blender, textures, FBXs, manifest, and final image: `candidate`.
- A02 validation and local audit files: `proof only`.
- Internal Attempts 01-03: `invalid`; local-only and never presented.
- Internal Attempt 04: `proof only`; local-only predecessor of the accepted
  final and never presented separately.
- A01 production package and final image: `quarantined` visual candidates.
- A01 `20/20` validation: `proof only`.
- Unreal outputs: `0`; `Fully game-ready`: `false`.

## Approval Gate

Flamestrike may approve, reject, or block the exact final image and A02 DCC
candidate identified above. Visual approval would not itself authorize Unreal
Step 17; that requires a separate explicit contract.
