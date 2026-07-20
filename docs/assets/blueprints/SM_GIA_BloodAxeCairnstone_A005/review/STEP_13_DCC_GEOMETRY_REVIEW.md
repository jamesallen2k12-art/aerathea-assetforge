# A005 Step 13 DCC Geometry Review

Status: approved; macro DCC source geometry accepted for later Step 14 planning; mandatory restart required

Artifact classification: `authoritative Step 13 review decision`

Contract ID: `A005-CR-STEP13-DCC-GEOMETRY-REVIEW-A01`

Candidate SHA-256:
`5b4af2275a70e2598e72361382fc7ea6ea318724ac928d71b2c200c768a93095`

## Decision

`approved`

The unchanged A005 Step 12 candidate is approved as the DCC source geometry
for later Step 14 UV, Base Color, and material-interpretation planning. This
decision approves the bounded macro geometry only. The asset remains a `DCC
source candidate`; it is not DCC game-ready, fully game-ready, finished
appearance, or visual canon.

## Why The Geometry Passes

- All `40/40` immutable review inputs matched.
- The read-only Blender audit passed `13/13` gates with no `.blend` save.
- Four required objects remain independently watertight, outward-oriented,
  non-degenerate positive volumes with identity transforms.
- Exact Step 12 bounds/topology still match: `400` vertices, `464` faces,
  `784` evaluated triangles, and the `10,000` hard cap is preserved.
- C-001 retains the approved piecewise-linear faceted envelope; smoothing or
  generic rounded fitting would violate the approved rule.
- C-002/C-003 remain separate nested course envelopes with their approved
  hidden contacts.
- C-004 retains approved N3/K80 containment and source-owned inward anchors.
- All six fixed-camera views are unclipped and corroborate one coherent
  assembled object. Back/right remain holdouts; perspective remains
  non-metric.
- No hidden closure or detached/projection geometry is visible.

## Deferred Appearance Boundary

The source visibly contains much more surface information than the untextured
candidate. That difference is real but is not Step 13 geometry authority.
Under `S11-TR-009`, these remain pending Step 14 planning:

- C-005 bilateral blade motif;
- C-006 inscription-like lines;
- C-007 fissures;
- individual-stone surface divisions not required by the approved silhouette;
- stone grain, small cracks, microchips, and micro-rubble;
- Base Color, Normal, ORM, AO, roughness, metallic, filtering, bake, and any
  emissive decision.

This approval must not be cited as approval of those deferred consumers.

## Audit History

The first review-package audit failed closed at `6/7` because the immutable
Step 12 top proof touched both horizontal frame boundaries. Its 154 cm
vertical orthographic scale implied only 126 cm horizontal span at a 900 by
1100 image aspect, smaller than the 140 cm apron.

The bounded correction changed only the in-memory Step 13 top proof camera to
190 cm and rerendered proof-only views from the unchanged `.blend`. Geometry,
source panels, Step 12 proofs, and authority changed `0`. The render audit then
passed `5/5`; the final review-package audit passed `8/8`; top margins became
44/45 horizontal pixels.

## Visible Evidence

- Review board:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/Step13/SM_GIA_BloodAxeCairnstone_A005_STEP13_GEOMETRY_REVIEW_BOARD.png`
- Six native-resolution fixed-camera/source comparisons exist under the same
  local-only Step 13 proof root.
- Exact source observation marks: `225`; filled source contours: `0`;
  unified source-pixel transforms claimed: `0`.
- Tracked audit:
  `manifests/STEP_13_DCC_GEOMETRY_REVIEW_AUDIT.json`.

The board uses thumbnails only for presentation. The six native-resolution
comparisons are the decision evidence.

## Next Gate

Mandatory restart. After restart, only preparation of a separate Step 14 UV,
Base Color, and Material-Interpretation Plan contract is permitted. Step 14
execution remains unauthorized.
