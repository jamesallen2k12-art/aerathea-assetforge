# Step 04 Output Record

Status: Step 04 complete; approved pending scoped closeout

Artifact classification: `authoritative`

Date: 2026-07-15

## Assigned Goal

Identify every visibly separate physical component or layer, assign fresh
neutral component IDs, and record visible contacts, occlusions, and ambiguous
boundaries without solving them.

## Approved Decision

The approved source supports seven neutral source-visible inventory layers or
surface-treatment families, three discontinuous visible contact relationships,
three explicitly occluded interface sectors, and nine blocked unknowns.

The inventory deliberately does not claim that an apparent layer is one mesh,
one material, one stone, or one hidden physical component. Individual masonry
blocks and rubble forms remain unresolved because their hidden interfaces and
cross-view identities are not source-owned.

## Fresh Neutral Inventory

| ID | Minimum source-owned observation | Physical separability |
|---|---|---|
| `C-001` | Central tapered primary body layer above the annular tiers | `ambiguous` |
| `C-002` | First annular masonry tier immediately below `C-001` | `ambiguous` |
| `C-003` | Second lower annular masonry tier below `C-002` | `ambiguous` |
| `C-004` | Irregular peripheral small-stone apron layer | `ambiguous` |
| `C-005` | Large bilateral blade-like red-appearing surface motif family | `ambiguous` |
| `C-006` | Narrow linear inscription-like red-appearing motif family | `ambiguous` |
| `C-007` | Branching red-appearing seam or fissure treatment family | `ambiguous` |

These descriptions were derived from the approved A005 panels. They are not
legacy component names and do not authorize production naming.

## Source-View Ownership Matrix

| ID | Front | Back | Left | Right | Top | Perspective |
|---|---|---|---|---|---|---|
| `C-001` | visible | visible | visible | visible | visible | visible, corroboration only |
| `C-002` | visible | visible | visible | visible | visible | visible, corroboration only |
| `C-003` | visible | visible | visible | visible | visible | visible, corroboration only |
| `C-004` | visible | visible | visible | visible | visible | visible, corroboration only |
| `C-005` | visible | ambiguous | ambiguous | ambiguous | visible | visible, corroboration only |
| `C-006` | visible | visible | visible | visible | visible | visible, corroboration only |
| `C-007` | visible | visible | visible | visible | visible | visible, corroboration only |

Perspective presence is visual corroboration only. No perspective measurement,
registration, or cross-view correspondence was used.

## Initial Contact-Line Inventory

| ID | Visible relation | Classification |
|---|---|---|
| `CL-001` | Exposed segments between `C-001` and `C-002` | `visible_discontinuous` |
| `CL-002` | Exposed segments between `C-002` and `C-003` | `visible_discontinuous` |
| `CL-003` | Exposed segments between `C-003` and `C-004` | `visible_discontinuous`; stops at rubble occlusion |

No contact line is closed through a hidden or ambiguous sector.

## Occluded Sectors

- `OS-001`: the interior and underside interface between `C-001` and `C-002`;
- `OS-002`: the hidden stacked interface between `C-002` and `C-003`;
- `OS-003`: portions of the `C-003` lower edge interrupted by `C-004`.

Only the fact of occlusion is recorded. Hidden extent and construction are not
solved.

## Blocked Unknowns

1. `U-001`: whether `C-001` is one physical stone or an assembly.
2. `U-002`: `C-002` individual stone count, hidden interfaces, and cross-view identities.
3. `U-003`: `C-003` individual stone count, hidden interfaces, and cross-view identities.
4. `U-004`: `C-004` individual form count, hidden placement, and cross-view identities.
5. `U-005`: whether `C-005` through `C-007` are paint, inset material, emissive fill, carved recesses, seams, or multiple treatments.
6. `U-006`: whether `C-005` is absent, occluded, or differently represented on back and side views.
7. `U-007`: bottom surfaces and hidden interfaces among `C-001` through `C-004`.
8. `U-008`: pixel-level seam, corner, block, and contact correspondence across views.
9. `U-009`: whether similar front, top, and perspective motifs are the same physical features.

These remain blocked after any Step 04 decomposition approval. Step 04 does not
authorize their resolution.

## Evidence Produced

- one paired exact-pixel source/marked board for each approved panel;
- untouched source on the left and an exact-resolution marked copy on the
  right;
- neutral unfilled component point marks;
- short contact segments only where a source-visible relationship is present;
- no masks, closed contours, candidate fills, smoothing, hidden boundaries,
  or geometry.

## Focused Validation Result

- Aggregate technical result: pass.
- Fresh neutral component/layer IDs: `7`.
- Initial contact relationships: `3`.
- Explicit occluded sectors: `3`.
- Blocked unknowns: `9`.
- Evidence boards: `6`.
- Every untouched left source tile is pixel-exact to its approved Step 03 crop.
- Resampling: none.
- Candidate fills or closed component contours: none.
- Perspective use: corroboration only.
- A005 production roots: absent.
- Legacy asset-specific access: false.
- Unrelated staged files: none.

Evidence board paths:

- `evidence/STEP_04/SM_GIA_BloodAxeCairnstone_A005_STEP_04_FRONT_OWNERSHIP_EVIDENCE.png`
- `evidence/STEP_04/SM_GIA_BloodAxeCairnstone_A005_STEP_04_BACK_OWNERSHIP_EVIDENCE.png`
- `evidence/STEP_04/SM_GIA_BloodAxeCairnstone_A005_STEP_04_LEFT_OWNERSHIP_EVIDENCE.png`
- `evidence/STEP_04/SM_GIA_BloodAxeCairnstone_A005_STEP_04_RIGHT_OWNERSHIP_EVIDENCE.png`
- `evidence/STEP_04/SM_GIA_BloodAxeCairnstone_A005_STEP_04_TOP_OWNERSHIP_EVIDENCE.png`
- `evidence/STEP_04/SM_GIA_BloodAxeCairnstone_A005_STEP_04_PERSPECTIVE_OWNERSHIP_EVIDENCE.png`

## Internal Candidate Correction

The first internal evidence pass placed one back-view `CL-003` segment and the
top-view right-side contact marks beyond the source-owned visible object. A
second top-view check showed that the first shortening still entered the
annotation field.

Those back and top boards were internally rejected, classified `invalid`, and
overwritten before validation or Flamestrike presentation. The final marks stop
on source-owned visible contacts. This was a pre-review candidate correction,
not a Core drift event.

Invalid overwritten file hashes are recorded in the component-ownership
inventory.

## Assumptions And Interpretations

No hidden construction, physical separability, individual block count,
cross-view registration, or material identity is asserted. Course-level and
surface-family descriptions are observational labels only. All unsupported
questions are recorded as blocked unknowns.

## Access Declaration

- No A001-A004 asset-specific artifact was opened or used.
- No old component name, count, mask, formula, coordinate, script, or output
  was used.
- No source crop was modified.
- No A005 production root was created.
- No DCC, texture, export, or Unreal artifact was created.

## Artifact Status

- Step 04 contract: `authoritative`.
- Component-ownership inventory: `authoritative`.
- This output record: `authoritative`.
- Evidence boards: `proof only`.
- Validation manifest: `proof only` after focused validation.
- Interpretation authority: none.
- Step 05 authority: none.

## Checkpoint

- Pre-action checkpoint: `Saved/ProjectRecovery/20260715-131308/`.
- Validated-candidate review checkpoint:
  `Saved/ProjectRecovery/20260715-133027/`.
- Approved pre-closeout checkpoint:
  `Saved/ProjectRecovery/20260715-133530/`.

## Output Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Visible review: approved crops, all six paired source/mark evidence boards,
  complete inventory, source-view matrix, contact inventory, blocked unknowns,
  and this record
- Result: pass and authority promotion
- Exclusion: blocked unknowns remain unresolved; Step 05 remains unauthorized

## Next Gate

Stop for the mandatory restart. The next agent may present a Step 05 contract
only after the Core resume handshake. Step 05 remains unauthorized.

## Commit And Push

- Scoped content commit: `e7860d6`
- Commit message: `Lock BloodAxe Cairn Stone A005 component inventory`
- Push: success; `assetforge/main` advanced from `f2fb2b8` to `e7860d6`
- Scoped files: fourteen A005 Step 04 records and images
- Unrelated changes: preserved and unstaged
