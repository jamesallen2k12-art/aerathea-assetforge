# A005 Step 12 DCC Source Geometry Candidate Output Record

Status: Step 12 complete; DCC source candidate and proof package validated;
dependency snapshot pushed and remotely verified; mandatory restart required

Artifact classification: `authoritative Step 12 result record`; candidate asset remains `candidate`

Contract ID: `A005-CR-STEP12-DCC-SOURCE-GEOMETRY-A01`

Date: 2026-07-20

## Decision

Pass for the bounded Step 12 production decision. One fresh A005-only Blender
source exists and satisfies the registered numeric, authority-lineage,
topology, contact, holdout, and hard-cap gates. Its correct status is `DCC
source candidate`.

This is not visual-fidelity approval, DCC game-ready status, fully game-ready
status, or visual canon. The paired board visibly shows that the macro geometry
is much simpler than the source. Approval, rejection, or a blocked finding on
that fidelity belongs only to Step 13 after the mandatory restart.

## Candidate Outputs

- Blender source candidate:
  `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_DCCSource_A01.blend`
- Geometry/VAG sidecar:
  `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_GEOMETRY_MANIFEST.json`
- Fresh generator:
  `Tools/DCC/build_bloodaxe_cairnstone_a005_step12_dcc_source.py`
- Independent auditor/proof packager:
  `Tools/DCC/audit_bloodaxe_cairnstone_a005_step12_dcc_source.py`

The `.blend`, generator, and geometry manifest are classified `candidate`.

## Technical Result

`pass_step12_dcc_source_candidate_complete_pending_step13_review`

- Locked immutable inputs: `52/52` matched.
- Schema-only generator and auditor preflights: passed; `bpy` imported `false`;
  filesystem writes `0`.
- Primary mesh objects: `4/4` in the required C-004, C-003, C-002, C-001
  construction order.
- Vertices: `400`; faces: `464`; evaluated triangles: `784`; LOD0 hard cap:
  `10,000`.
- Step 11 VAG groups accounted: `14/14`; vertices with zero or multiple
  primary assignments: `0`.
- Each of four primary objects is independently watertight; open,
  non-manifold, loose, duplicate, and degenerate topology counts: `0`.
- Assembled height: `220 cm`; C-001: `120 x 90 cm` maximum; C-004:
  `140 x 110 cm`; pivot/origin: `(0,0,0)`.
- Hidden Z ranges: C-004 `[0,10.5]`, C-003 `[9.5,23.5]`, C-002
  `[22.5,35.5]`, C-001 `[34.5,220]` cm.
- CL-001/002/003 hidden intersection thickness: exactly `1 cm` each; shared
  source loops: `0`; numeric visible-overlap proxy pixels: `0`.
- Back/right validation: passed only as the approved exact non-metric taper,
  nested-order, and contact-order invariants; construction coordinates read
  from holdouts: `0`; physical pixel pairing claimed: `0`.
- C-005/C-006/C-007 geometry, UVs, materials, LODs, collision, FBX, and Unreal
  outputs: `0`.

## Audit History And Bounded Corrections

The first complete pre-proof audit failed closed at `14/16` and created no
proof renders.

1. The authority phrase check did not normalize the approved statement across
   a Markdown line wrap.
2. The coordinate equivalence check used `0.000001 cm`, below Blender's
   observed float32 serialization delta of `0.00000694 cm`.

The smallest sufficient read-only correction normalized Markdown whitespace
and set the recorded coordinate tolerance to `0.00001 cm`. Geometry, geometry
manifest, source evidence, locked authority, and construction decisions
changed `0`. The complete rerun passed `16/16`.

All six authorized renders then completed. Board packaging stopped twice
before board creation on old-Pillow presentation compatibility: first on a
non-ASCII title glyph, then on the unavailable `Image.Resampling` namespace.
The bounded packaging corrections used an ASCII title and the equivalent
legacy LANCZOS constant. Geometry, source, and six hashed renders changed `0`.
The third package attempt passed all `4/4` post-proof gates.

## Proof Outputs

Artifact classification: `proof only`.

- Local numeric audit:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/Step12/STEP_12_NUMERIC_AUDIT.json`
- Six clean front/back/left/right/top/perspective renders under the same local
  Step 12 proof root.
- Review board:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/Step12/SM_GIA_BloodAxeCairnstone_A005_STEP12_DCC_SOURCE_CANDIDATE_REVIEW_BOARD.png`
- Tracked audit: `manifests/STEP_12_DCC_SOURCE_GEOMETRY_AUDIT.json`.
- Visible review: `review/STEP_12_DCC_SOURCE_GEOMETRY_CANDIDATE_REVIEW.md`.

All six source panels remained byte-identical. The review board and Markdown
record were automatically opened in visible desktop applications.

## Blocked Boundary Preserved

- no Step 12 visual-fidelity self-approval or repair;
- no old builder or A001-A004 asset-specific input;
- no A005 `CoreRecovery/` diagnostic input;
- no source-sheet plane, projection shell, detached carrier, mask geometry,
  smoothing, fitting, averaging, or local warp;
- no C-005/C-006/C-007 geometry;
- no UV, texture, final material, LOD, collision, FBX, Unreal, or Step 13 work.

## Git Closeout

- Exact dependency-complete staged scope: `13/13` paths; outside scope `0`.
- JSON parse: `3/3`; Python compile: `2/2`; locked hashes: `52/52`; proof
  hashes: `6/6`; review-board hash: passed.
- Secret matches and unstaged in-scope differences: `0`.
- Dependency snapshot commit:
  `e2282f057d45b190cd58f7d4da7907d7c19e869b`.
- Push to `assetforge/main`: passed.
- Remote verification: local and remote hashes matched exactly at the
  dependency snapshot commit.
- Pre-metadata checkpoint: `Saved/ProjectRecovery/20260720-155609/`.
- The immediate metadata commit records this proven result and intentionally
  does not self-embed its own hash.
- Unrelated user work and local-only proof/recovery outputs remained unstaged.

## Required Next Action

Stop for the mandatory post-Step-12 restart. After resume, the next permitted
action is preparation only of a separate Step 13 DCC Geometry Audit and
Flamestrike Review contract. Do not repair geometry or begin downstream work
in this session.
