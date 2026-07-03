# KIT_GIA_BloodAxeCairnVariantBatch_A01 DCC Preflight Review

## Scope

- Review date: 2026-07-03
- Review type: Codex DCC preflight, not Flamestrike final visual approval
- Contact sheet: `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/BloodAxeCairnVariants_A01_DCCReviewContactSheet.png`
- Source status at preflight: `DCC source candidate`
- Current status after later prep pass: `DCC game-ready candidate`

This review checks whether the twelve cairn variants are worth taking into the next production pass. It does not promote any asset to `DCC game-ready candidate` or `Fully game-ready`.

## Summary Decision

Do not drop any variant. The batch is viable as a twelve-asset DCC source set.

Initial review found four duplicate-risk silhouettes. A same-day DCC differentiation pass was applied, the Blender sources and FBX/LOD exports were rebuilt, and the tracked contact sheet was regenerated. Current recommendation: all twelve variants may advance to game-ready prep after Flamestrike review of the revised DCC contact sheet.

## Revision Pass Completed

The following duplicate-risk variants were revised before game-ready prep:

| Asset | Initial Issue | Revision Applied | Current Recommendation |
| --- | --- | --- | --- |
| `SM_GIA_BloodAxeApproachCairnMarker_A01` | Too similar to the ritual guidepost and path marker. | Rebuilt as a wider/lower approach marker with side-biased cloth and heavier approach-edge grounding. | Advance after Flamestrike contact-sheet review. |
| `SM_GIA_BloodAxeRitualCairnGuidepost_A01` | Too similar to the approach cairn and path marker. | Rebuilt as a taller ceremonial guidepost with a stronger vertical read and restraint on text/VFX. | Advance after Flamestrike contact-sheet review. |
| `SM_GIA_BloodAxeCairnPathMarker_A01` | Too similar to the approach cairn and ritual guidepost. | Rebuilt as a smaller, simpler trail-side marker with lighter cloth density and a clearer lean. | Advance after Flamestrike contact-sheet review. |
| `SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01` | Too close to the collapsed threshold cairn. | Rebuilt with a lower cave-buried read, reduced upright stub, darker grit, and older collapsed massing. | Advance after Flamestrike contact-sheet review. |

## Already Clear In First Pass

These variants read clearly enough in the first contact sheet and did not need a geometry differentiation pass:

| Asset | Reason |
| --- | --- |
| `SM_GIA_BloodAxeLowThresholdCairn_A01` | Good squat threshold read, clear low profile, useful cave-edge dressing. |
| `SM_GIA_BloodAxeCollapsedThresholdCairn_A01` | Strong collapsed silhouette and useful contrast against intact cairns. |
| `SM_GIA_BloodAxeCaveRemnantCairn_A01` | Distinct lower cave-remnant read with useful ash/cave grit potential. |
| `SM_GIA_BloodAxeCaveThresholdCairnPair_A01` | Strong paired threshold composition, readable at review scale. |
| `SM_GIA_BloodAxeMovedCampCairnPair_A01` | Strong abandoned/moved-camp composition and good negative-space rhythm. |
| `SM_GIA_BloodAxePairedCairnClosePair_A01` | Useful compact pair with clear route-dressing value. |
| `SM_GIA_BloodAxePairedCairnStaggeredPair_A01` | Best depth/spacing variation among paired assets. |
| `SM_GIA_BloodAxeCairnScrapCap_A01` | Most distinct single-cairn variant because the scrap-cap language gives it a separate role. |

## Next Production Step

Follow-up completed on 2026-07-03: all twelve variants received the DCC game-ready prep pass recorded in `DCC_GAME_READY_PREP_STATUS.md`.

Next active gate:

1. Run the Unreal import task packet in `UNREAL_IMPORT_TASK_PACKET.md`.
2. Validate the imported static meshes:
   - target Content path exists
   - one material slot is assigned
   - vertex colors drive the review material correctly
   - LOD0-LOD3 are present and switch without disappearing
   - broad simple collision exists and does not snag on small detail
   - no route, waypoint, quest, pickup, loot, destructible, VFX, or audio behavior is added

## Blockers

Unreal import, material instances, authored textures, collision correctness, startup placement, gameplay behavior, route logic, waypoint behavior, quest markers, VFX/audio, and final visual approval remain blocked.

## Decision Boundary

This review approves the batch for continued DCC work only. It does not approve visual canon, final art, gameplay behavior, Unreal use, collision, or `Fully game-ready` status.
