# AET-MA-20260629-581 Startup Capture Task Packet

## Task ID

`AET-MA-20260629-581`

## Goal

Capture a clean offscreen startup review image for `AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01` so Flamestrike can review the startup composition and aesthetic read.

## Assigned Agent

Unreal Implementation + Visual Art Direction + QA / Validation

## Allowed Files

- `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeLowCairnRemnant_A01.png`
- `docs/agents/AET-MA-20260629-581_STARTUP_CAPTURE_TASK_PACKET.md`
- `docs/agents/AET-MA-20260629-581_VALIDATION_SUMMARY.md`
- `docs/agents/AGENT_TASK_BOARD.md`

## Blocked Files

- `Content/Aerathea/`
- `SourceAssets/`
- `Tools/DCC/`
- `Tools/Unreal/`
- `Source/Aerathea/`
- authored texture assets
- gameplay Blueprints/classes
- VFX/audio assets
- source concept folders
- global asset indexes
- Hermes files or configuration

## Dependencies

- `AET-MA-20260629-577`
- `AET-MA-20260629-578`
- `AET-MA-20260629-579`
- `AET-MA-20260629-580`
- DCC proof render: `Saved/Automation/DCC/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01_DCCReview.png`
- Startup review actor: `AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01`

## Approval Gate

This task produces a review capture only. Flamestrike approval is required before claiming final shipped startup composition, final visual art, final collision, runtime behavior, gameplay behavior, combat feel, playstyle, economy/backend direction, VFX/audio, Hermes work, or next implementation target selection.

## Required Validators

- Run `Tools/Unreal/capture_startup_review_offscreen.sh Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeLowCairnRemnant_A01.png`.
- Confirm the capture file exists and is non-empty.
- Confirm image dimensions are 1280 x 720.
- Inspect the capture visually against the DCC proof and the intended startup-review framing.
- Run `python Tools/Agents/validate_agent_workflow.py` if the task board changes.
- Run `git diff --check` for changed docs.
- Run ASCII and trailing-whitespace scans for changed text files.

## Expected Deliverables

- Clean startup review PNG for user aesthetic review.
- Validation summary with capture path, image checks, visual-read notes, and residual approval gates.
- Task board update marking this task `Needs Approval` when the capture is ready for Flamestrike review.

## Integration Owner

Lead Producer / Orchestrator
