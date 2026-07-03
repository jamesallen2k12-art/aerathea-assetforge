# AET-MA-20260630-584 Visual Canon Policy Task Packet

## Task ID

`AET-MA-20260630-584`

## Goal

Codify Flamestrike's concept-first approval process: use provided concept art for guidance, generate grouped visual variants for subjective approval, register selected images as Aerathea visual canon, and require DCC/Unreal work to match the approved canon target.

## Assigned Agent

Lead Producer / Orchestrator + Visual Art Direction + Production Intake + Docs / Index

## Allowed Files

- `AGENTS.md`
- `docs/agents/AGENT_WORKFLOW.md`
- `docs/agents/AGENT_TASK_BOARD.md`
- `docs/agents/AET-MA-20260630_PIPELINE_APPROVAL_POLICY.md`
- `docs/agents/AET-MA-20260630-584_VISUAL_CANON_POLICY_TASK_PACKET.md`
- `docs/agents/AET-MA-20260630-584_VALIDATION_SUMMARY.md`
- `docs/assets/VISUAL_CANON_WORKFLOW.md`
- `docs/assets/VISUAL_CANON_REGISTRY.md`
- `docs/assets/ASSET_CONCEPTS_MANIFEST.md`
- `docs/assets/ASSET_CONCEPTS_INTAKE_QUEUE.md`
- `docs/assets/APPROVAL_QUEUE.md`
- `docs/assets/visual_canon/`
  - `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_CandidateBoard.png`

## Blocked Files

`Content/Aerathea/`, `SourceAssets/`, `Tools/DCC/`, `Tools/Unreal/`, runtime source, binary assets, external source concept folders, Hermes files or configuration.

## Dependencies

- Flamestrike approval on 2026-06-30 to proceed with grouped concept approvals and canonized image selections.
- `AGENTS.md`
- `docs/assets/ASSET_CONCEPTS_MANIFEST.md`
- `docs/assets/ASSET_CONCEPTS_INTAKE_QUEUE.md`
- `docs/agents/AET-MA-20260629-582_VISUAL_REVIEW_DECISION.md`

## Approval Gate

No user approval is required to codify the process. Stop before marking any specific generated or source image as `approved anchor` or `approved variant`; Flamestrike must choose the images.

## Required Validators

- `python Tools/Agents/validate_agent_workflow.py`
- `git diff --check`
- targeted ASCII scan
- targeted trailing-whitespace scan
- targeted canon-status overclaim scan

## Expected Deliverables

- Visual canon workflow doc.
- Visual canon registry.
- Blood Axe cairn stones canon slate.
- Candidate Blood Axe cairn stones concept board for Flamestrike selection.
- Updated pipeline, intake, approval queue, and task-board wording.
- Validation summary.

## Integration Owner

Lead Producer / Orchestrator
