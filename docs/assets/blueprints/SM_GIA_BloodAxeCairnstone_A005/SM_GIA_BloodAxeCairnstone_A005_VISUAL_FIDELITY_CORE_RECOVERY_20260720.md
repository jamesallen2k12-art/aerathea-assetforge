# SM_GIA_BloodAxeCairnstone_A005 Visual-Fidelity Core Recovery

Status: recovery technically complete; DCC game-ready candidate pending Flamestrike visual approval

Artifact classification: `authoritative recovery record`

Date: 2026-07-20

Contract ID: `A005-CR-STEPS01-16-VISUAL-FIDELITY-RECOVERY-A01`

## Authority

Flamestrike directed Codex to resume, audit Steps 01 through 16, locate and
correct the concept-to-game-ready visual discrepancy, make any required
changes, and open only the final corrected 3D image for approval. This grants
complete authority inside the bounded A005 Steps 01-16 recovery. Unreal import
and `Fully game-ready` promotion remain outside this recovery.

Pre-action checkpoint:
`Saved/ProjectRecovery/20260720-193020/`.

Post-job checkpoint:
`Saved/ProjectRecovery/20260720-201509/`.

## Last Known Core-Valid State

- Steps 01-10 source identity, scanline verification, source-panel evidence,
  measurements, scale recovery, correspondence records, and approved
  interpretation boundaries remain `authoritative`.
- The sole visual/source authority remains
  `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`
  with SHA-256
  `4b953abb87f5f254a5f51c6214e76d3f72c4fc55bc2fa4e4d605b2440d6e53c2`.
- Authoritative production dimensions remain `140 x 110 x 220 cm`; the base
  height remains `35 cm`; the pivot remains bottom center at ground station.

## First Divergent Action

Step 11 planned a large-prop LOD0 target of approximately `8000` triangles,
an approved range of `4000-10000`, four closed primary-shell allocations,
and source-critical silhouette breaks while explicitly keeping C-005/C-006/
C-007 decoration at zero geometry. Step 12 produced only `784`
triangles. Its budget validator enforced only `<=10000` and did not enforce
the approved lower bound, target-deviation rule, or required modeled macro
feature coverage. The under-resolved blockout therefore passed a technical
gate that could not prove visual fidelity.

The first production divergence is Step 12. Step 11 remains valid as source,
dimension, topology, and intended-budget authority but is incomplete as a
validation contract until the recovery override adds the missing lower-bound
and feature-coverage gates.

## Affected Outputs And Classification

- Historical Step 12 Blender geometry and geometry manifest: `quarantined` as
  visual reconstruction; `reference only` for the validator defect and exact
  bounds history.
- Historical Step 13 macro-geometry approval: `authoritative historical
  decision` only; it does not approve visual equivalence and cannot authorize
  the recovery candidate.
- Historical Step 14 plan: `reference only` for the old blockout's UV/material
  route; source-color ownership rules remain reusable evidence.
- Historical Step 15 material candidate and maps: `quarantined` as a complete
  visual candidate; source-owned color data remains `reference only` for the
  corrected rebuild.
- Historical Step 16 Blender/FBX package and final proof: `quarantined` as a
  visual-fidelity candidate; its packaging audit remains `proof only` for the
  old package.
- Steps 01-10 source/evidence records: unchanged and `authoritative`.

No historical file is deleted. The affected production family is preserved
through the pre-action checkpoint and a local-only quarantine snapshot before
replacement outputs are promoted.

## Smallest Sufficient Recovery

1. Preserve Steps 01-10 and all authoritative source files byte-for-byte.
2. Add a Step 11 recovery override requiring `4000-10000` LOD0 triangles,
   concept-critical macro-feature coverage, and a source-to-final visual gate.
3. Rebuild from the authoritative source dimensions, not from historical
   A001-A004 production assets or the under-resolved A005 mesh.
4. Rebuild the rounded irregular monolith, two independent masonry-course
   shells, and rubble-apron shell near the Step 11 triangle target. Keep the
   Blood Axe, runes, fissures, individual course stones, and micro-rubble as
   source-owned Base Color/Normal consumers with zero decoration geometry,
   exactly as Step 11 and Step 14 require.
5. Produce UV0/LightmapUV, Base Color/Normal/ORM material response, LOD0-LOD3,
   four custom collision hulls, Blender source, FBXs, manifest, independent
   audit, and one final approval render.
6. Open only that final 3D render for Flamestrike review.

## Recovery Decision Gate

The replacement may be classified only as `DCC game-ready candidate` after
all technical gates pass and internal source comparison rejects no major
silhouette, component, marking, material, scale, or presentation discrepancy.
It remains a `candidate` pending Flamestrike's review of the single final
image.

## Recovery Result

- Steps 01-10: retained `authoritative` and unchanged.
- Step 11: retained `authoritative`; its four-primary-shell, one-material,
  zero-decoration-geometry, and LOD planning rules are honored.
- Steps 12-16: rebuilt and independently validated.
- LOD triangles: `8672 / 3988 / 1820 / 692`.
- Bounds on all LODs: exact `140 x 110 x 220 cm`, pivot `[0,0,0]`.
- Primary topology: four disconnected closed shells; boundary edges `0`,
  non-manifold edges `0`, degenerate triangles `0`.
- UVs: `UVMap` plus `LightmapUV` on all four LODs.
- Materials/maps: one material; Base Color, DirectX Normal, and ORM.
- Source-owned Base Color audit: `154948` pixels compared across five owner
  views; mismatches `0`.
- Collision: four named UCX proxies.
- FBX clean re-import: `4/4`, exact triangle matches.
- Independent validation: `20/20` gates pass.
- Unreal outputs: `0`; `Fully game-ready`: `false`.
- Current classification: `candidate`; pipeline status: `DCC game-ready
  candidate` pending Flamestrike's review of the single final image.

Candidate paths and hashes are recorded in
`manifests/VISUAL_FIDELITY_RECOVERY_A01_VALIDATION.json`.

## Internal Rejection Record

No rejected image was promoted or opened for Flamestrike. Five early rejected
frames are preserved in the local-only
`Saved/AssetForgeResearch/quarantine/SM_GIA_BloodAxeCairnstone_A005/VisualFidelityRecovery_A01_RejectedFrames/`
family. Later iterations reused the single local final-render path and were
rejected before promotion for material-slot misassignment, oversized relief,
source-atlas seam exposure, padding stretch, or an artificial transition
band. The accepted render is the only review image.
