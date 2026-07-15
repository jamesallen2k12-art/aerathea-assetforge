# Step 03 To Step 04 Handoff

Status: authoritative; Step 03 approved and scoped closeout pending

Artifact classification: `authoritative`

Date: 2026-07-15

## Current Step And Decision

Step 03 passed. All six lossless crops are pixel-exact copies of their declared
source regions. Flamestrike approved the boundaries as source ownership on
2026-07-15. The crop formulas and panel images are authoritative for A005.

## Approved Goal

Create one faithful, coherent 360-degree BloodAxe Cairn Stone from the
confirmed A02 multiview source and advance it through all gates to Approved
library asset status.

## Authority Files

1. `AGENTS.md`;
2. authoritative fresh-start plan;
3. approved A005 Step 01 governance package;
4. approved Step 02 source-authority package;
5. approved `steps/STEP_03_CONTRACT.md`;
6. this handoff only after Step 03 output approval;
7. a separately approved Step 04 contract.

## Allowed And Blocked Data

- Authoritative now: A02 source and exact scanline evidence.
- Authoritative: Step 03 crop formulas and six lossless panel crops.
- Proof only: Step 03 validation manifest and boundary evidence board.
- Blocked: all A001-A004 asset-specific artifacts.
- Blocked: component inventory, masks, measurements, interpretation, DCC,
  texture, export, Unreal, and all work outside an approved next-step contract.

## Evidence Produced

- six integer half-open panel formulas;
- six lossless source-region crops;
- per-panel source-region and output pixel hashes;
- zero changed pixels and zero maximum RGB delta for every panel;
- exact source-only boundary board.

## Formulas Used

- crop bounds: `[x0, y0, x1, y1)`;
- width: `x1 - x0`;
- height: `y1 - y0`.

## Assumptions Or Interpretations

None. Perspective is explicitly limited to visual corroboration unless later
calibrated under separate authority.

## Validators And Results

Focused validators passed:

- panel count: `6`;
- aggregate changed pixels: `0`;
- maximum RGB delta: `0`;
- all panels pixel exact: `true`;
- legacy access: false;
- interpretation introduced: false;
- production artifact created: false.

## Artifact Status

- Step 03 crop manifest and crops: `authoritative`;
- Step 03 evidence board and validation manifest: `proof only`;
- this handoff: `authoritative`;
- Step 04 authority: none.

## Last Core-Valid State

The approved Step 03 panel-decomposition package protected by
`Saved/ProjectRecovery/20260715-125003/`. Scoped commit and push remain.

## Remaining Gates

- Step 03 scoped closeout;
- mandatory new-agent restart;
- separate Step 04 contract approval.

## Current Checkpoint

- Step 03 pre-action checkpoint: `Saved/ProjectRecovery/20260715-123416/`;
- validated-candidate review checkpoint:
  `Saved/ProjectRecovery/20260715-124330/`.

## Proposed Next Step

Step 04 - Physical Component And Source-Ownership Inventory.

Decision: identify every visibly separate physical component or layer, assign
fresh neutral component IDs, and record ambiguous or occluded boundaries
without solving them.

Step 04 is not authorized by this handoff or by Step 03 output approval.

## Exact Next Read Order

1. `AGENTS.md`;
2. authoritative fresh-start plan;
3. A005 RESET_RESUME_STATE;
4. approved `steps/STEP_03_OUTPUT_RECORD.md`;
5. approved Step 03 panel crop manifest;
6. this handoff;
7. a separately approved Step 04 contract;
8. only manifests and source evidence named by that contract.

## Next Approval Gate

After scoped Step 03 closeout and the mandatory restart, the next agent may
present a Step 04 contract only. Step 04 is not authorized.
