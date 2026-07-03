# AET-MA-20260629-571 Build Target Selection

## Decision

- Task: `AET-MA-20260629-571`
- Decision date: 2026-06-30
- Approved first build target: `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- Approval source: Flamestrike approved the recommendation to proceed with `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` as the first controlled Blood Axe moved-camp build target.
- Source package: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/PRODUCTION_PACKAGE.md`
- Readiness matrix: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/IMPLEMENTATION_READINESS_MATRIX.md`
- Closure/readiness note: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/PACKAGE_CLOSURE_AND_DCC_READINESS.md`
- Parent kit context: `docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/`

## Rationale

`SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` is the lowest-risk first build target in the moved-camp static-prop lane. It is a compact static dressing prop with a clear mesh silhouette, no required cloth simulation, no route/decal behavior, no interaction, no VFX/audio, and no gameplay state.

The asset gives the pipeline a controlled first test for DCC source creation, proof render, FBX export, scale validation, LOD planning, material-slot restraint, and later Unreal import validation without starting with terrain residue, cloth behavior, active marker language, route-marker ambiguity, runtime systems, or startup placement.

## Approved Target Constraints

- Build exactly one static prop: `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`.
- Preserve the core read: one low collapsed cairn remnant, 60-180 cm tall, 3-7 large rough stones, one dominant base stone, a few shifted support stones, cold ash, trampled mud, soot-dark contacts, and one restrained old Blood Axe residue beat.
- Use Giant scale context only: female baseline 442 cm / 14 ft 6 in and male baseline 470 cm / 15 ft 5 in.
- Keep Blood Axe hostile Giant residue separate from neutral/civilized Giant culture.
- Keep the asset static environmental storytelling only.
- Treat all first-pass DCC and Unreal outputs as review targets until QA and Flamestrike approval.

## Still Blocked

This decision does not authorize Unreal import, Unreal Content edits, runtime source, material instance creation, texture asset creation, startup placement, review actor creation, final visual approval, final collision approval, route approval, gameplay behavior, pickup behavior, loot behavior, salvage behavior, resource behavior, navigation/pathfinding, waypoint behavior, breadcrumb behavior, tracking behavior, objective logic, VFX/audio, cloth simulation, wind animation, physics behavior, source concept movement, Hermes work, or global docs integration beyond the task-board state needed to create the next packet.

## Next Packet

`AET-MA-20260629-572` creates the DCC task packet for the approved target. DCC work may begin only under that packet's exact allowed paths and validators.

## Validation Checklist

- [x] Target selected from the approved low-risk candidate list.
- [x] Target source package exists.
- [x] Target readiness matrix exists.
- [x] Target closure/readiness note exists.
- [x] Approval source recorded.
- [x] DCC is not started by this decision record.
- [x] Unreal, runtime, startup, validator, and final approval work remain blocked.
