# A005 Steps 01-16 Visual-Fidelity Recovery A01 Output Record

Status: technical pass; visually rejected and quarantined by Flamestrike

Artifact classification: `authoritative recovery result record`

Date: 2026-07-20

Contract ID: `A005-CR-STEPS01-16-VISUAL-FIDELITY-RECOVERY-A01`

## Decision

Retain the `20/20` result as technical `proof only`, but reject and quarantine
the A01 package as a visual candidate. Flamestrike found a missing/cut-off read
in the bottom base stack and source-color mismatch. A fresh-context A02
correction pass is authorized. Unreal outputs remain zero.

## Step Results

- Steps 01-10: retained authoritative and unchanged.
- Step 11: retained authoritative and honored. The rebuild uses four closed
  primary shells, one runtime material, and zero C-005/C-006/C-007 decoration
  geometry. The Blood Axe, runes, fissures, individual course stones, and
  micro-rubble remain Base Color/Normal consumers.
- Step 12: first divergent historical `784`-triangle blockout quarantined;
  rebuilt LOD0 has `8672` triangles.
- Step 13: historical macro review superseded for this recovery candidate;
  corrected topology independently audited.
- Step 14: source-owner and authored-zone rules applied to corrected UV0;
  LightmapUV present on all LODs.
- Step 15: corrected one-material Base Color/Normal/ORM package produced;
  `154948` source-owned Base Color pixels compared with `0` mismatches.
- Step 16: corrected Blender, LOD0-LOD3, four UCX proxies, and four FBXs
  produced; clean FBX re-import passes `4/4`.

## Technical Evidence

- LOD triangles: `8672 / 3988 / 1820 / 692`.
- All LOD bounds: `140 x 110 x 220 cm`; pivot `[0,0,0]`.
- LOD0 topology: four connected components, boundary edges `0`, non-manifold
  edges `0`, degenerate triangles `0`.
- UV layers: `UVMap`, `LightmapUV` on all LODs.
- Runtime material slots: `1`.
- Collision: four named UCX proxies.
- Independent audit: `20/20` gates pass.
- Validation: `manifests/VISUAL_FIDELITY_RECOVERY_A01_VALIDATION.json`.

## Rejected Artifacts

Five early rejected frames are preserved in the local-only
`Saved/AssetForgeResearch/quarantine/SM_GIA_BloodAxeCairnstone_A005/VisualFidelityRecovery_A01_RejectedFrames/`
family. Later iterative frames reused the single local render path and were
rejected before promotion for material assignment, relief proportion,
source-atlas seam, padding stretch, or artificial transition-band defects.
No rejected frame was opened for Flamestrike or classified as a candidate.

## Approval Gate

Only this final image is eligible for review:

`Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualFidelityRecovery_A01/SM_GIA_BloodAxeCairnstone_A005_FINAL_GAME_READY_ASSET.png`

Flamestrike may approve, reject, or block this DCC game-ready candidate. A
separate Step 17 authorization and Unreal validation are required before any
`Fully game-ready` claim.
