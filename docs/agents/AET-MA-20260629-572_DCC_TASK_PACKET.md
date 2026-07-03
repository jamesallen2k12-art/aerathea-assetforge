# AET-MA-20260629-572 DCC Task Packet

## Task ID

`AET-MA-20260629-573`

## Goal

Create the first-pass DCC source, proof render, and FBX export for the approved Blood Axe moved-camp static prop target `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`.

## Assigned Agent

DCC / Modeling Prep

## Skill

`docs/agents/skills/aerathea-dcc-modeling-prep/`

## Source Inputs

- Target-selection approval: `docs/agents/AET-MA-20260629-571_BUILD_TARGET_SELECTION.md`
- Production package: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/PRODUCTION_PACKAGE.md`
- Implementation readiness matrix: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/IMPLEMENTATION_READINESS_MATRIX.md`
- Package closure/readiness note: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/PACKAGE_CLOSURE_AND_DCC_READINESS.md`
- Parent child intake context: `docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/CHILD_ASSET_INTAKE.md`

## Allowed Files

- `Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py`
- `SourceAssets/Blender/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.blend`
- `SourceAssets/Exports/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.fbx`
- `Saved/Automation/DCC/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01_DCCReview.png`
- `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/DCC_BUILD_STATUS.md`
- `docs/agents/AGENT_TASK_BOARD.md`
- `docs/agents/AET-MA-20260629-573_VALIDATION_SUMMARY.md`

## Blocked Files

- `Content/Aerathea/`
- `Source/Aerathea/`
- `Tools/Unreal/`
- Unreal maps, startup scene files, review actors, placement files, validators outside the allowed validation summary, runtime source, Blueprints, material instances, texture assets, external source concept folders, Hermes files or configuration, and unrelated DCC, Blender, FBX, or Saved outputs.

## Dependencies

- `AET-MA-20260629-571` target approval complete.
- Existing package/readiness/closure docs for `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`.
- Validated Giant scale context: female baseline 442 cm / 14 ft 6 in and male baseline 470 cm / 15 ft 5 in.

## DCC Build Requirements

- Build one static mesh review asset only.
- Preserve a 60-180 cm total height; target first-pass height should sit near 110-140 cm unless a better readable variant is documented.
- Use 3-7 large rough stones, with one dominant base stone and a few shifted support stones.
- Include cold ash, trampled mud, soot-dark contacts, and one restrained faded Blood Axe red residue beat.
- Keep all detail broad and production-friendly. Fine cracks, ash flecks, mud streaks, cloth weave, paint chips, and scratches should remain texture/normal planning, not modeled clutter.
- Use 1 material target for the exported static mesh. A second material is not approved for this first DCC pass.
- Create LOD0-LOD3 meshes in source and export them if the local FBX path can preserve them cleanly.
- Do not create sockets, route helpers, gameplay markers, trigger shapes, nav helpers, pickup affordances, VFX/audio locators, cloth simulation, wind setup, physics setup, destructible states, or runtime data.
- Collision correctness is not approved. Do not create UCX collision in this first DCC pass unless this packet is amended; record collision as disabled-by-default / future-gated in the build status.

## Approval Gate

DCC source/proof/export work is approved for the exact files listed above only. Stop before Unreal import, Content edits, material instance creation, texture asset creation, validator scripts outside the allowed summary, startup placement, review actor creation, runtime behavior, final visual approval, or final collision approval.

If the DCC proof render shows the asset reading as a route marker, waypoint, breadcrumb, objective marker, pickup pile, loot cache, salvage pile, neutral/civilized Giant marker, active signal, or final route proof, return to lead before export/import continuation.

## Required Validators

- `python -m py_compile Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py`
- Run the DCC build script through Blender after syntax passes.
- Confirm the Blender source exists at the allowed path.
- Confirm the FBX export exists at the allowed path.
- Confirm the DCC proof render exists at the allowed path.
- Confirm `DCC_BUILD_STATUS.md` records scale, material count, LOD status, collision status, proof render path, export path, and remaining blockers.
- Scan for target identity, Giant scale baselines, Blood Axe/civilized Giant separation, no-Unreal/no-runtime/no-startup/no-final-approval/no-gameplay guardrails, and exact allowed paths.
- Run `git diff --check` on changed text files.
- Run ASCII and trailing-whitespace scans on changed text files.

## Expected Deliverables

- DCC build script for the approved target.
- Blender source file for the approved target.
- FBX export for the approved target.
- DCC proof render for visual review.
- Asset-local DCC build status doc.
- Validation summary with exact pass/fail evidence and residual risks.

## Integration Owner

Lead Producer / Orchestrator

## QA Owner

QA / Validation

## Docs Owner

Docs / Index after DCC validation, not during DCC execution.

## Non-Authorization Statement

This packet does not authorize Unreal Content, runtime source, material instance assets, texture assets, startup placement, review actors, gameplay behavior, collision correctness, final visual approval, final collision approval, route approval, source concept movement, Hermes work, or global docs integration beyond task-board state. Those remain separate lanes after DCC validation.
