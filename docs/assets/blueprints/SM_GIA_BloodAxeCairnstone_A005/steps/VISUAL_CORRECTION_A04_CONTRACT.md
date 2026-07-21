# A005 Visual Correction A04 Core Recovery Contract

Status: `complete; output visually rejected and quarantined`

Artifact classification: `authoritative execution contract`

Contract ID: `A005-CR-VISUAL-CORRECTION-A04`

Date: 2026-07-21

## Goal

Create a fresh A04 Steps 01-16 DCC candidate whose structural read is exactly:

1. one central tapered plinth;
2. one slab directly supporting the plinth; and
3. one visibly larger slab directly below the first slab.

The source-owned ground rubble may remain only as a shallow peripheral apron.
It must not read as a fourth structural slab. A01, A02, and A03 remain
quarantined and must not be modified or used as geometry inputs.

## Authority

- Flamestrike's 2026-07-21 complete Steps 01-16 correction authority and exact
  three-mass structural direction.
- `VISUAL_CORRECTION_A03_SOURCE_TARGET_PROPORTION_CONFLICT_RECOVERY_RECORD.md`.
- Visual source:
  `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`.
- Authoritative front and left source-pixel measurement manifests.
- Non-conflicting Step 11 topology, performance, packaging, and Step 14
  source-owned UV/material requirements.

## A04 Conflict Resolution Rule

The original concept controls visible relative component proportions. The
non-conflicting overall anchors remain `140 x 110 x 220 cm`, a `35 cm` base
span, and bottom-center pivot `[0,0,0]`. The conflicting historical
`120 x 90 cm` C001 physical allocation no longer controls the visible plinth
profile.

The source front owner measurements set the controlling hierarchy:

- upper slab/source footprint ratio: `245 / 288 = 0.8507`;
- lower slab/source footprint ratio: `277 / 288 = 0.9618`;
- plinth-contact/upper-slab ratio: `195 / 245 = 0.7959`.

A04 target widths are therefore `120 cm` for the upper slab, `136 cm` for the
lower slab, and no more than `96 cm` at the plinth/slab contact. The shallow
apron retains the overall `140 cm` footprint.

## Locked Production Scope

1. Overall bounds `140 x 110 x 220 cm`; base span `0-35 cm`; pivot
   `[0,0,0]`; `1 uu = 1 cm`.
2. Four independently closed primary shells remain permitted for technical
   continuity: C001 plinth, C002 upper slab, C003 larger lower slab, and C004
   shallow peripheral rubble apron.
3. The structural hierarchy must pass in both front and three-quarter review:
   `C001 contact < C002 < C003 < C004 footprint`, while only C001-C003 read as
   structural masses.
4. C002 target footprint `120 x 90 cm`; C003 target footprint
   `136 x 104 cm`; C004 maximum footprint `140 x 110 cm`.
5. C001 maximum visible width/depth `108 x 78 cm`, contact footprint no more
   than `96 x 68 cm`, and total assembled height `220 cm`.
6. One runtime material. C005/C006/C007 remain source-owned Base Color/Normal
   consumers with zero decoration geometry.
7. LOD0 `4000-10000` triangles; LOD1-LOD3, two UV layers, four collision
   proxies, Blender source, four FBXs, and clean FBX re-import are required.
8. Intermediate attempts remain internal. Open only the accepted final A04
   review image in a visible desktop window.

## Blocking Visual And Technical Gates

- Plinth contact width `< 0.84 *` upper-slab width.
- Upper-slab width `<= 0.90 *` lower-slab width.
- Lower-slab width `<= 0.98 *` overall apron width.
- Both slabs have positive visible ledges in front and left projections.
- C004 height `<= 9 cm` and reads as peripheral rubble, not a slab.
- Source-owned atlas RGB remains byte-exact.
- Four closed primary shells; zero boundary, non-manifold, or degenerate
  topology failures.
- Exact overall bounds and pivot on all LODs.
- One material, two UV layers, four LODs, four collision hulls, four clean FBX
  re-imports, and no Unreal outputs.
- Final review framing must show the plinth, the first slab, and the larger
  lower slab completely, with no clipping or underside view.

## Forbidden

- Repairing A03 forward or using A01-A03 geometry as construction authority.
- Modifying or deleting A01-A03 artifacts.
- Restoring the conflicting C001 `120 x 90 cm` visible allocation.
- A fourth structural slab, annular support tier, pedestal, or hidden visual
  mass.
- Source editing, color grading, emissive, metallic stone, or extra runtime
  materials.
- Unreal/Step 17 work, `Fully game-ready`, approved-library, or visual-canon
  promotion.

## Decision Output

End as exactly one of:

- `candidate`: every A04 technical and visual gate passes and the exact final
  A04 image is pending Flamestrike review;
- `blocked`: a required gate fails;
- `quarantined`: an internal attempt fails and is preserved as non-authority.

## Final Visual Decision

Flamestrike rejected A04 on 2026-07-21. The exact plinth is approved as an
`authoritative visual reference`, but the complete output is `quarantined`.
The contract's rectangular footprint targets and width-hierarchy gates did
not prove the source's oval base contour or a replacement rather than
cumulative-stack visual read. Recovery authority is recorded in
`VISUAL_CORRECTION_A04_VISUAL_REJECTION_A05_RESTART_HANDOFF.md`.
