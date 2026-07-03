# AET-MA-20260629-582 Focused Capture Task Packet

## Task ID

`AET-MA-20260629-582`

## Goal

Produce a focused offscreen startup review capture for `AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01`, then restore the overview camera so Flamestrike can make a subjective aesthetic/framing decision from a useful image.

## Assigned Agent

Unreal Implementation + Visual Art Direction + QA / Validation

## Allowed Files

- `Tools/Unreal/set_startup_review_camera_preset.py`
- `Content/Aerathea/Maps/L_Aerathea_Startup.umap`
- `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeLowCairnRemnant_Focused_A01.png`
- `docs/agents/AET-MA-20260629-582_FOCUSED_CAPTURE_TASK_PACKET.md`
- `docs/agents/AET-MA-20260629-582_VALIDATION_SUMMARY.md`
- `docs/agents/AGENT_TASK_BOARD.md`

## Blocked Files

- unrelated `Content/Aerathea/` assets
- `SourceAssets/`
- `Tools/DCC/`
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
- `AET-MA-20260629-581`
- DCC proof render: `Saved/Automation/DCC/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01_DCCReview.png`
- Startup review actor: `AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01`

## Approval Gate

This task produces a focused review capture only. Flamestrike approval is required before claiming final shipped startup composition, final visual art, final collision, runtime behavior, gameplay behavior, combat feel, playstyle, economy/backend direction, VFX/audio, Hermes work, or next implementation target selection.

## Required Validators

- Add a focused preset to `Tools/Unreal/set_startup_review_camera_preset.py`.
- Run Python compile for the changed preset script.
- Apply the focused camera preset in Unreal.
- Run `Tools/Unreal/capture_startup_review_offscreen.sh Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeLowCairnRemnant_Focused_A01.png`.
- Confirm the focused capture file exists and is non-empty.
- Confirm image dimensions are 1280 x 720.
- Inspect the focused capture visually against the DCC proof and intended startup-review framing.
- Restore the `overview` review-camera preset.
- Run generic startup scene validation after restoration.
- Run `python Tools/Agents/validate_agent_workflow.py`.
- Run `git diff --check`.
- Run ASCII and trailing-whitespace scans for changed text/script files.

## Expected Deliverables

- Focused startup review PNG for user aesthetic review.
- Restored overview camera after capture.
- Validation summary with exact command evidence, image checks, visual-read notes, and residual approval gates.
- Task board update marking this task `Needs Approval` when the focused capture is ready for Flamestrike review.

## Integration Owner

Lead Producer / Orchestrator
