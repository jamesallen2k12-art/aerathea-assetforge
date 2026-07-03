# Aerathea Visual Canon Registry

Last updated: 2026-07-03

This registry records concept images and selected variants that define Aerathea's visual aesthetic. Source concepts remain in the external concept folder unless a separate storage policy approves copying them into the repository.

## Registry Rules

- Do not treat implementation blockouts, procedural DCC previews, or failed Unreal captures as canon.
- Do not mark a generated board or source image as canon without Flamestrike approval.
- Approved canon entries must be used by production packages, Blender modeling notes, material plans, and Unreal review comparisons.
- If a later image supersedes a canon entry, keep the old entry and mark it `superseded`; do not silently rewrite visual history.

## Canon Entries

| Canon ID | Status | Scope | Source or board | Approved selection | Keeper features | Production use |
| --- | --- | --- | --- | --- | --- | --- |
| `VC-GIA-BloodAxe-Source-Refs-A01` | reference only | Blood Axe camp, ritual, gate, and village material language | External source concepts: `BloodAxeRitual.png`, `BloodAxeCamp.png`, `BloodAxecamp.png`, `BloodAxeGate.png`, `BloodAxe Village.png` | Not a single approved asset target | Dark highland setting, crude timber/stake silhouettes, red banner/paint language, skull/horn trophy shapes, smoke/ash mood, hostile Giant raider identity | Guides Blood Axe concept boards and cleanup requirements; not direct DCC approval |
| `VC-GIA-BloodAxe-CairnStones-A01` | approved source board | Blood Axe cairn stones, low remnants, moved-camp residue | `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_CandidateBoard.png` | `A1` selected as the source direction; the later `Test2Manual` implementation is requested-changes after backside review | Preserve rough dark stone, cold ash/mud grounding, restrained oxide red, rawhide/rope residue, Blood Axe hostility, and separation from civilized Giant stonework | Guides future Blood Axe cairn variants; does not approve gameplay behavior, quest markers, VFX/audio, destruction, or weak 360-degree backsides |
| `VC-GIA-BloodAxe-CairnStones-A01-A1-TurnaroundGuide` | approved rebuild guide | A1 Blood Axe cairn slab cluster turnaround | `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_TurnaroundDraft_A01.png` | Approved by Flamestrike as the multi-angle rebuild guide after the front-only method failed | Low collapsed slab cluster, broken rear slab, rawhide lashings, restrained oxide-red paint, rough ash/mud base, shared landmark points across views | Historical guide for the A1 reconstruction lane; current repair target is `SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair` |
| `VC-GIA-BloodAxe-CairnStones-A01-A1-Test2Manual` | requested changes / historical proof | A1 Blood Axe cairn slab cluster static prop | `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_FinalGameReadyReviewBoard.png` | Brightened Test 2 approved by Flamestrike on 2026-07-01, then later failed backside review | Front-faithful A01 projection, broad dark slab cluster, restrained oxide-red Blood Axe paint, side-stone massing, broad collision; failed requirement is believable authored rear geometry | Retained as historical proof and failure evidence; do not promote to asset-library final without repair |
| `VC-GIA-BloodAxe-CairnTargets-A01` | primary target set | Blood Axe cairn stones A1-A5 and B1-B5 | `docs/assets/visual_canon/BloodAxeCairnTargets_A01/VC_GIA_BloodAxe_CairnTargets_A01_ContactSheet.png`; individual targets in `docs/assets/visual_canon/BloodAxeCairnTargets_A01/` | Flamestrike provided clearer labeled target images on 2026-07-03 and instructed Codex to use them | Per-target multi-angle geometry, stronger stone massing, cloth/rawhide placement, red paint placement, terrain/debris grounding, and distinct A/B target identities | Required source targets for the next Blood Axe cairn rebuild; supersedes generic A1-derived batch comparison for concept-geometry approval |

## Pending Approval Candidates

| Candidate ID | Status | Scope | Source or board | Selection state | Keeper features | Production use |
| --- | --- | --- | --- | --- | --- | --- |
| `VC-GIA-BloodAxe-CairnStones-A01-A1-BacksideRepair` | repair candidate pending approval; not canon | A1 Blood Axe cairn slab cluster static prop repair | `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair_BacksideRepairTurntableReview.png` | Created after Flamestrike requested a complete repair run for the failed backside | Preserve A1 front read while adding real rear counterweight/support stones, rear paint/lashing treatment, deeper mud/ash grounding, and updated collision depth | Pending DCC proof, Unreal import validation, startup capture, and Flamestrike visual approval |
| `SM-GIA-BloodAxeCairnTarget-A1-A01-DCCProof` | DCC source candidate pending concept-geometry review; not canon | Blood Axe cairn target A1 static prop rebuild | `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_ConceptGeometryCompare.png` | Created from the clearer `BloodAxe A1` target set on 2026-07-03 | Establishes a clean A1 rebuild lane with dominant front slab, rear slab, left lashed stack, right supports, and authored 360-degree massing; still too blocky for approval | Use as first DCC source proof and revision base only; not approved visual canon and not ready for Unreal import |

## Rejected Or Requested-Change References

| Reference | Status | Reason | Follow-up |
| --- | --- | --- | --- |
| `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeLowCairnRemnant_Focused_A01.png` | requested changes; not canon | Read as an unpainted rock pile and only partially aligned with Blood Axe lore | Replace with approved concept-board target before further DCC/Unreal visual signoff |
| `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_BackReview.png` | requested changes; not final canon | Backside did not read as properly authored 3D geometry for a successful 360-degree game asset candidate | Repair through `SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair` and require fresh Unreal review approval |
