# Blood Axe Cairn Stones Visual Canon Slate A01

Status: `A1 source direction approved; Test2Manual requested changes after backside review; BacksideRepair candidate in progress`

Date: 2026-06-30

Candidate board: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_CandidateBoard.png`

## Scope

This slate prepares a grouped concept-board approval pass for Blood Axe cairn stones, low cairn remnants, and moved-camp residue props. It exists because the first Unreal review of `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` did not read strongly enough as Blood Axe and was not approved as visual canon.

## Source Concepts Inspected

External source concepts remain read-only in:

`/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS`

Relevant guidance images:

- `BloodAxeRitual.png`
- `BloodAxeCamp.png`
- `BloodAxecamp.png`
- `BloodAxeGate.png`
- `BloodAxe Village.png`

## Source Guidance

Keeper features from the inspected Blood Axe references:

- Dark, smoky highland atmosphere.
- Crude timber, stakes, lashings, and harsh camp construction.
- Oxide red banners, paint, cloth, and faction markings.
- Horn/skull/trophy silhouette language, simplified for MMO-safe production.
- Ash, mud, soot, trampled ground, and old ritual residue.
- Hostile Giant raider identity, separate from neutral/civilized Giant craft.

Cleanup requirements:

- Reduce graphic gore into non-graphic trophy or ritual residue.
- Reduce photoreal noise into stylized hand-painted value groups.
- Avoid excessive skull clutter, tiny spikes, micro-bones, text, and dense props.
- Keep Blood Axe red readable but not UI-like, magical, or objective-like.
- Keep cairns from becoming waypoint chains, route markers, loot piles, or interaction props.

## Concept Board Request

Generated one 10-variant concept board for approval:

- Two rows of five Blood Axe cairn stone variants.
- Each variant should be a single readable prop or small prop cluster.
- Variants should explore different silhouettes: low collapsed mound, taller broken guidepost, red cloth-tied slab, ash-sunk stones, horn-token cairn, rawhide-bound pair, broken standing remnant, mud-heavy remnant, ritual-paint stone, and moved-camp memory cluster.
- Present on a clean neutral background with enough spacing for visual selection.
- Use positions `A1-A5` for the top row and `B1-B5` for the bottom row.

## Approval Question

Flamestrike should select preferred positions and note combinations, for example:

`A1 and B3, but add more red cloth from A4 and less skull language.`

Approved selections become `VC-GIA-BloodAxe-CairnStones-A01` canon entries and then drive production package edits, Blender modeling, paint/material work, and Unreal review comparison.

## Candidate Board Notes

- `A1`: low collapsed slab cluster with red paint and low ash/mud grounding.
- `A2`: tall single standing marker with rawhide wraps and small horn token.
- `A3`: large cloth-draped slab with the strongest red fabric read.
- `A4`: jagged ash-sunk standing-stone cluster with restrained paint.
- `A5`: stacked cairn with horn/skull trophy silhouette, highest risk of over-trophy clutter.
- `B1`: paired upright stones with rawhide wrap and a small red cloth beat.
- `B2`: tall painted slab with strong lashings and side stakes.
- `B3`: mud-heavy low remnant with the least faction readability.
- `B4`: painted monolith with side stones and ritual-paint read.
- `B5`: compact low standing cluster with red lashing and broad ground base.

Position `A1` remains the approved Blood Axe cairn source direction. The brightened Test 2 manual implementation is now historical/requested-changes after review showed the backside was not properly generated as a successful 3D candidate. Other positions remain unapproved variants until separately selected.

## Turnaround Guide Update

Flamestrike approved the A1 multi-angle turnaround draft as the corrected rebuild guide after the front-only projection process failed to define believable side/back geometry.

- Approved rebuild guide: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_TurnaroundDraft_A01.png`
- DCC candidate review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild_ConceptVsDCCReview.png`
- Asset status: `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/TURNAROUND_REBUILD_STATUS.md`

Approval scope: A1 is approved as the Blood Axe cairn source direction. The turnaround guide remains useful for front/side/back interpretation, but the Test2Manual implementation no longer carries final visual approval because its backside did not meet the 360-degree DCC candidate requirement. This does not approve gameplay interaction, quest marker behavior, destruction, VFX/audio, or combat use.

## Test 2 Manual Requested-Changes Update

Flamestrike approved `SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual` brightened pass `A01-Test2-Bright-01` on 2026-07-01, then later identified that the backside was not properly generated as a successful 3D candidate during Unreal review. The Test2Manual package is retained as historical proof and failure evidence, not the current final asset target.

- Historical asset status: `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/TEST2_MANUAL_ASSET_STATUS.md`
- Unreal static mesh: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual`
- Startup actor: `AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual`
- Focused validation: 209 cm high x 323 cm wide x 156 cm deep, 4 LODs, 2 materials, 3 textures, broad collision enabled.
- Rejected review issue: backside read as insufficiently authored 3D geometry for final approval.

## BacksideRepair Candidate Update

`SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair` is the active repair candidate. It preserves the A1 front identity but requires a complete 360-degree rebuild pass with authored rear support stones, rear paint/lashing treatment, deeper stone massing, updated collision, LOD0-LOD3, material texture sets, Unreal import validation, startup review capture, and Flamestrike visual approval before it can move beyond candidate status.

- Asset status: `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/BACKSIDE_REPAIR_STATUS.md`
- DCC review folder: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair/`
- Unreal static mesh target: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair`
- Startup actor target: `AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair`
