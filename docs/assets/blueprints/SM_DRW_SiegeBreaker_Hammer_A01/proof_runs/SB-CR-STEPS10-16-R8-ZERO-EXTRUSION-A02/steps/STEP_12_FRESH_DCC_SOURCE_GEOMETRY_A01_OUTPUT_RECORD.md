# Step 12 A01 Fresh DCC Source Geometry Output Record

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract ID: `SB-CR-R8-STEP12-FRESH-DCC-SOURCE-GEOMETRY-A01`
- Recovery run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Decision: `BLOCKED before builder creation`
- Block code:
  `Blueprint block: rule missing — performance amendment required`
- Artifact status: `authoritative blocked result record`
- DCC source candidate created: `false`
- Step 13 authority: `false`

## Result

The approved Step 12 execution stopped at the pregeometry performance gate.

All `34/34` Step 11 authority-file hashes matched. The approved contract,
approval record, blueprint, authority lock, and execution environment all
verified. The output root was fresh and remained uncreated.

The independent topology replay then found that the current exact R8 rotational
profiles contain:

- `214` radius states;
- `206` required longitudinal transitions; and
- `64` positive-X angular divisions in the only explicit hash-locked angular
  tessellation authority.

The minimum rotational topology is therefore:

`206 * 64 * 2 triangles * 2 whole-Rz180 occurrences = 52,736 triangles`

This lower bound excludes every head surface, contact, cap, closure, and seam.
It already exceeds the Step 11 LOD0 hard cap of `10,000` triangles by at least
`42,736`.

## Closed-World Decision

Both permitted readings block:

1. If the inherited `64` positive-X divisions remain authoritative, exact
   execution is mathematically over the hard cap before head construction.
2. If the inherited count is superseded by the R8 recovery, the authoritative
   Step 11 blueprint contains no replacement angular subdivision count or
   deterministic adaptive rule.

Choosing `6`, `8`, or another subdivision count would change visible
silhouette and topology. It is an authored production decision and cannot be
invented by Codex.

## Files Created

- approved Step 12 contract;
- exact approval record;
- independently verified environment lock;
- event trace;
- blocked validation;
- independent pregeometry audit;
- this output record;
- blocked handoff; and
- final scoped manifest.

## Files Not Created

- Step 12 builder;
- Step 12 Blender validator;
- source output root;
- Blender geometry;
- `.blend` files;
- proof renders;
- review board;
- UVs or materials;
- LODs or collision;
- exports; or
- Unreal artifacts.

## Artifact Status

- Step 12 contract: `authoritative approved scope`.
- Step 12 approval record: `authoritative`.
- Step 12 environment lock: `authoritative within this execution`.
- Performance validation: `proof only`.
- Independent audit: `proof only`.
- Step 12 production result: `blocked`.
- DCC source candidate: `does not exist`.
- DCC game-ready candidate: `does not exist`.
- Fully game-ready: `false`.

No failed geometry exists to quarantine. No execution drift occurred, so no
drift-ledger entry is required.

## Assumptions Or Interpretations

No unapproved assumption was used to continue production.

The audit explicitly tested both possible interpretations of the inherited
`64`-division rule. Both stop. Neither was silently selected as authority.

## Required Next Gate

A separately approved Step 11B angular-tessellation and performance amendment
must lock:

1. the exact positive-X angular division count or adaptive rule;
2. continuous proportional U ownership without nearest-pixel skipping or
   repetition;
3. the exact whole-asset pregeometry triangle estimate;
4. the `8,000` target and `10,000` hard-cap disposition; and
5. the silhouette review requirement for the selected circumference.

Recommended smallest next action:

`draft a measurement-only Step 11B amendment comparing 6 and 8 positive-X
angular divisions, without creating geometry`

That action requires separate Flamestrike authorization.

## Stop

Step 12 remains blocked. Step 13 remains locked. Do not create a builder, open
Blender for production, build geometry, render, or repair forward under the
current authority.

## Additive Completion Supplement — 2026-07-24

This section supersedes the earlier blocked production state while preserving
it as historical evidence. Flamestrike subsequently approved:

1. the Step 11B high-poly/Nanite performance amendment;
2. the Step 11C bottom C02/C03 label correction;
3. the Step 11D exact three-boundary stone stitch; and
4. the Step 11E bounded cross-view silhouette tolerance.

The Step 11E tolerance replaces only exact cross-view width equality. It
requires all three limits:

- no more than `1` source pixel per side;
- no more than `1/400` (`0.25%`) relative difference; and
- no more than `1/5 cm` (`2 mm`) total absolute difference.

The observed difference is `1/2` source pixel per side, `1/974` relative, and
`52020/517681 cm` total. All limits pass. The measured geometry was preserved
without clipping. Pivot, `170 cm` height, depth, axes, owner membership, gaps,
mirrors, one whole-asset Rz180, `64` angular divisions, seams, and topology
remain exact.

## Step 12 Production Result

Both approved high-poly variants now exist and independently pass direct
saved-file validation:

| Candidate | Dimensions W × D × H | Observed triangles | Independent audit | Status |
| --- | --- | ---: | --- | --- |
| Candidate A — rune side | `97.974428267601 × 34.434306569343 × 170 cm` | `2,202,434` | `105/105 PASS` | `DCC source candidate` |
| Candidate B — metal center piece side | `97.974428267601 × 43.120437956204 × 170 cm` | `2,316,748` | `105/105 PASS` | `DCC source candidate` |

Polygon counts are recorded for the UE5 Nanite workflow and are not treated as
limits at this high-poly source stage.

Each candidate includes:

- one saved Blender source;
- canonical geometry;
- pre-save validation;
- an independent direct saved-file audit;
- six fixed silhouette renders;
- seven neutral-clay renders;
- one wire/contact render;
- eight parallax frames plus one strip; and
- a complete candidate-local output inventory with no missing or unexpected
  files.

The first rune-side saved attempt failed `3` of `105` checks on closure
topology, was not rendered or promoted, and remains `invalid` in:

`Saved/ProjectRecovery/Quarantine/20260724-081118/rune_side_saved_audit_topology_failure`

The exact closure-only repair introduced no new source points and the rebuilt
candidate passed all checks. No drift-ledger entry is required because the
fail-closed audit stopped the invalid attempt before presentation or
promotion.

## Review Evidence

- Review board:
  `review/STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_REVIEW_BOARD.png`
- Review board SHA-256:
  `d5fd658eed5c62c8775ed4f53e5478d233ddc47147382f69d87c021c42a9f474`
- Dual-candidate validation:
  `manifests/STEP_12_DUAL_DCC_SOURCE_CANDIDATE_A01_VALIDATION.json`
- Validation SHA-256:
  `4341a7dd0b8218731cc171ed0e1159989f585137b031019a5b8b8920b09dc6f3`
- Event trace SHA-256:
  `47fc61385d71e0f2a391ca65eed6735ec8ae56333c07d4361519395b83d289ee`
- Post-build checkpoint:
  `Saved/ProjectRecovery/20260724-082657`

The board was internally inspected for orientation, framing, and text
legibility, then opened in a visible desktop image viewer.

## Current Gate

Step 12 production is complete only to the dual `DCC source candidate` review
gate. No candidate has been selected or visually approved.

Flamestrike must choose Candidate A or Candidate B, reject both, or mark the
review blocked. Step 13, retopology, UVs, baking, export, and Unreal work remain
unauthorized.
