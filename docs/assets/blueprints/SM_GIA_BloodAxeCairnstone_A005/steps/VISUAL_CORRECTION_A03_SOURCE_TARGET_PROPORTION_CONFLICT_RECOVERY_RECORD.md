# A005 Visual Correction A03 Source/Target Proportion Conflict Recovery Record

Status: `Core stop-line; A03 quarantined; authority decision required`

Artifact classification: `authoritative recovery record`

Date: 2026-07-20

## Detection

Flamestrike identified the original concept sheet as the comparison target and
stated that the 3D image remained very different. Direct source/3D review
confirmed that the discrepancy is structural: the concept keeps the monolith
inside the broad masonry courses, while the A03 target-space construction lets
the C-001 monolith overhang the narrower C-002/C-003 courses.

The authoritative source remains:

`docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`

SHA-256:
`4b953abb87f5f254a5f51c6214e76d3f72c4fc55bc2fa4e4d605b2440d6e53c2`

## Last Known Core-Valid State

The last production boundary is the committed A02 visual-rejection recovery
state at `ea6294076d2e1e2502426ed876e3aa55aef4c5bc`. The source remains
`authoritative`. A01 and A02 remain quarantined visual candidates. Step 11
remains authoritative for its recorded physical-target construction decision,
but it cannot also be treated as proof of source-concept component proportions
after Flamestrike's comparison-target clarification.

## First A03 Divergence

`VISUAL_CORRECTION_A03_CONTRACT.md` allowed Step 11 component-local
target-space normalization to control the visible profile when source ratios
and printed physical targets disagreed. The A03 builder then preserved the
Step 11 allocation of C-001 at up to `120 x 90 cm` while keeping C-002/C-003
inside smaller containments. Gate G21 compared the result to that derived
target-space envelope, not to the raw concept's relative component
proportions.

This repeated a conflict already proven by
`SCALE_AUTHORITY_RECOVERY_A01_OUTPUT_RECORD.md`: every one of the ten tested
within-axis source/target ratio checks conflicts. The source C-004/C-001 ratio
is larger than the target ratio in X and Y, so source proportions and the
Step 11 allocation cannot both be exact without an explicit authority choice.

## Affected Outputs And Classification

- A03 contract and plan: `quarantined as an execution boundary`; useful only
  as reference for the detected source/target conflict.
- A03 builder, renderer, auditor, Blender source, textures, FBXs, manifest,
  final-path render, and validation: `quarantined`; not approval-ready and not
  visual authority.
- A03 internal Attempts 01-18: `proof only / quarantined`; none may be opened
  or presented as the accepted final.
- Attempt16 independent audit: `proof only`; it passed 26/27 gates and blocked
  on masonry/apron recess detection, but the larger source-proportion conflict
  supersedes any technical-pass route.
- Later internal geometry proof: `proof only`; 7 C-002, 8 C-003, and 8 C-004
  recesses were detected without promotion.
- A01, A02, source files, Step 01-10 evidence, and unrelated worktree files:
  unchanged.

## Smallest Sufficient Recovery

Do not repair A03 forward and do not display its final-path image. A fresh A04
contract requires one explicit authority rule:

1. Either retain the Step 11 component allocation and accept that the result
   cannot match the concept's relative component proportions; or
2. Make the concept image authoritative for relative component proportions,
   re-derive C-001/C-002/C-003 visible profiles from source-owner pixels, and
   retain only the non-conflicting overall production anchors that Flamestrike
   explicitly selects (proposed anchors: `140 x 110 x 220 cm`, `35 cm` base,
   bottom-center pivot).

No A04 geometry, texture, Blender, FBX, Unreal, commit, push, or review image is
authorized until that rule is approved. Unreal/Step 17 remains forbidden and
`Fully game-ready` remains `false`.

## Required Flamestrike Decision

`Blueprint block: source authority conflicts with physical-target component allocation.`

Approve or reject the proposed A04 rule: preserve the overall
`140 x 110 x 220 cm` envelope, `35 cm` base span, and pivot, but let the
original concept control all relative C-001/C-002/C-003/C-004 visible
proportions and rebuild from those source-owner measurements.
