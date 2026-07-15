# AssetForge Drift Ledger

Purpose: record Core drift events, recovery points, affected outputs, and approved corrections.

Core authority: `AGENTS.md` Core Principles govern this ledger. Drifted artifacts are not authority unless Flamestrike explicitly reclassifies them.

## Entry Template

```md
### YYYY-MM-DD HH:MM TZ - Short Drift Title

- Asset or scope:
- Detected by:
- Last known Core-valid state:
- First drift action:
- Assumption or interpretation that caused drift:
- Affected outputs:
- Artifact statuses:
- Quarantined locations or records:
- Recovery decision:
- Flamestrike approval:
- Follow-up Core/Kaizen improvement:
```

## Entries

### 2026-07-15 16:04 EDT - A005 Step 04 Top Contact Evidence Source-Ownership Drift

- Asset or scope: `SM_GIA_BloodAxeCairnstone_A005`, approved Step 04 top ownership evidence and the downstream Step 05-08 authority chain.
- Detected by: Codex native-pixel audit during the approved Step 08 pre-action pass. Approved Step 04 top contact coordinates include obvious white background pixels, including `CL-003` points `(140,27) = (248,248,248)`, `(167,27) = (253,253,253)`, `(195,27) = (254,254,254)`, `CL-002` endpoint `(195,38) = (254,254,254)`, and `CL-003` endpoint `(31,130) = (255,255,255)`.
- Last known Core-valid state: approved Step 03 lossless panel decomposition at content commit `2cee686` and final handoff commit `f2fb2b8`; the A02 source, exact scanline evidence, A005 charter/firewall, source lock, and Step 03 crops remain authoritative.
- First drift action: the final Step 04 correction retained top contact marks outside the source-owned object, then the board and validator were accepted as source-bounded.
- Assumption or interpretation that caused drift: visual proximity on the composite board was treated as proof of source ownership instead of a native-pixel coordinate audit against the authoritative top panel.
- Affected outputs: Step 04 top evidence board, component-inventory top review coordinates, Step 04 validation manifest, Step 04 output/approval/handoff completion claims, downstream Step 05-07 authority classification, and the approved but not yet executed Step 08 contract.
- Artifact statuses: Step 04 top board is `quarantined; invalid as source-bounded proof`; embedded top review coordinates are `invalid`; the original Step 04 inventory is `quarantined/superseded for active authority`; the approved Step 04R recovery inventory and exact top-contact manifest are `authoritative`; the recovered board and validation are `proof only`; original Step 04 validation/output/handoff completion authority remains `quarantined`; Step 05-07 authority is `quarantined/suspended pending dependency audit`, not yet declared invalid; Step 08 is stopped with no tracked output.
- Quarantined locations or records: `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_CORE_RECOVERY_STATUS_20260715_STEP04_TOP_CONTACT_EVIDENCE.md`; local diagnostics under `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/CoreRecovery/20260715_STEP04_TopContactEvidenceDrift/`.
- Recovery progress: Flamestrike approved the exact Step 04R recovery contract and then approved the visible recovered package. The authoritative recovery records contain 48 discrete source-owned top-contact pixels; 24 builder validators and 30 independent audit checks pass. The original affected artifacts remain byte-identical and quarantined; Step 05-07 remain suspended; Step 08 has no output.
- Recovery decision: Step 04R recovery is complete. Do not repair forward in Step 08. After the mandatory restart, the next gate is a separately approved Step 05-07 dependency restoration/quarantine audit contract; Step 08 can be renewed only after that audit and an explicit renewed authorization.
- Flamestrike approval: Step 04R execution contract and visible output package approved on 2026-07-15. The earlier approved Step 08 execution boundary remains suspended by Core Recovery.
- Follow-up Core/Kaizen improvement: every evidence mark claiming source ownership must receive a native-pixel coordinate audit against the authoritative panel; composite-board visual review and pixel-exact untouched source tiles do not prove overlay containment.

### 2026-07-05 19:42 EDT - A002 Phase 3 Analytic Proof Shell Dataset Quarantine

- Asset or scope: `SM_GIA_BloodAxeCairnstone_A002` Phase 3C through Phase 7D generated dataset lineage.
- Detected by: Flamestrike visual rejection of the Phase 7D Unreal capture followed by Codex root-cause audit of A002 records, generator scripts, manifests, and local strict-pixel evidence.
- Last known Core-valid state: Phase 1 source evidence lock and Phase 2B/2C measurement/formula/audit records before production geometry. Phase 3A remains valid only as a plan boundary, not as proof that analytic shell output satisfied pixel-owned geometry authority.
- First drift action: Phase 3B/3C generated and advanced analytic oval proof-shell geometry as the A002 modular DCC source candidate.
- Assumption or interpretation that caused drift: source-named formula constants, footprint dimensions, centers, and per-view contact station heights were treated as sufficient geometry authority, even though the A002 blueprint required scan-verified source-pixel geometry evidence and blocked generic primitive replacement, old generator behavior, visual fitting, and unapproved inference.
- Affected outputs: A002 Phase 3C modular DCC source output; Phase 3D visual decision as advancement authority; Phase 4 snap assembly; Phase 5 texture/UV/material candidate; Phase 6 DCC game-ready source and exports, including recovered Phase 6C outputs; Phase 7C Unreal import candidate; Phase 7D startup review capture.
- Artifact statuses: Phase 1 source evidence remains `authoritative`; Phase 2B/2C remain `authoritative for recovery analysis` but not output authority alone; Phase 3A remains `authoritative as a boundary plan`; Phase 3B scripts are `evidence only`; Phase 3C through Phase 7D generated outputs are `quarantined`; Phase 7D capture is `proof only; rejected visual evidence`; `Content/Aerathea/Maps/L_Aerathea_Startup.umap` is `tainted/mixed local map state`; A02 StrictPixelA21 is `reference/candidate recovery evidence only`; A02 StrictPixelViewOwnedA24 is `reference only; strict gate failed`.
- Quarantined locations or records: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/CoreRecovery/20260705_Phase3_AnalyticProofShellDataset_Quarantine/`; manifest at `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/CoreRecovery/20260705_Phase3_AnalyticProofShellDataset_Quarantine/QUARANTINE_MANIFEST.md`; local status record at `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECOVERY_STATUS_20260705_PHASE3_ANALYTIC_PROOF_SHELL_DATASET.md`.
- Recovery decision: quarantine completed after Flamestrike approval. Flamestrike then approved `SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21` as the A002 strict-pixel recovery authority. A002 production remains blocked before the A21 handoff plan; no copy, rename, rebuild, import, map repair, or capture is authorized yet.
- Flamestrike approval: approved quarantine scope on 2026-07-05 after Codex identified the wrong A002 analytic/proof-shell dataset and the A21 strict-pixel evidence family. Approved A21 as the A002 strict-pixel recovery authority after quarantine.
- Follow-up Core/Kaizen improvement: future A002 recovery must add a strict-pixel/source-contour gate before any DCC source candidate can advance. Formula constants and proof-shell renders are not enough for source-image visual reconstruction assets.

### 2026-07-05 19:20 EDT - A002 Phase 7D Capture Visual Match Block

- Asset or scope: `SM_GIA_BloodAxeCairnstone_A002` Phase 7D startup review capture and Phase 7C Unreal import candidate visual-readiness gate.
- Detected by: Codex inspection of `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeCairnstone_A002_Phase7D.png` against the recovered Phase 6C DCC game-ready angle/front proof renders.
- Last known Core-valid state: recovered Phase 6C DCC audit and FBX geometry proof passed; Phase 7C Unreal import, placement, and focused technical validator passed for presence, LODs, simple collision, materials, actor placement, and metadata.
- First drift action: Phase 7D offscreen startup capture produced a framed, non-empty image that does not visually match the DCC proof/source authority closely enough for review presentation.
- Assumption or interpretation that caused drift: Phase 7C technical validation was treated as sufficient evidence that the rendered Unreal capture would match the DCC proof; the validator did not prove rendered material/camera/asset match.
- Affected outputs: `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeCairnstone_A002_Phase7D.png`; Phase 7C Unreal Static Mesh/material package as a visual-review candidate; Phase 7C validation scope as a review-readiness authority.
- Artifact statuses: Phase 7D capture PNG is `proof only; blocked evidence`; Phase 7C Unreal import candidate is `candidate; visual-match recovery required before review`; recovered Phase 6C DCC package remains `DCC game-ready candidate`; final visual approval remains `pending`; A002 remains not `Fully game-ready`.
- Quarantined locations or records: blocked capture is preserved in place and recorded in `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_7D_STARTUP_REVIEW_CAPTURE_BLOCKED_RECORD.md`; A002 local recovery status reopened in `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECOVERY_STATUS_20260705_PHASE6C_EMPTY_FBX.md`.
- Recovery decision: blocked pending Flamestrike approval. Proposed smallest sufficient recovery is to inspect the A002 Unreal material/rendered mesh state against the recovered DCC proof and approved source template, identify whether the mismatch is material graph, slot assignment, import, camera targeting, or DCC handoff, then correct only the confirmed cause and strengthen the Phase 7 validator/readiness gate.
- Flamestrike approval: Phase 7D capture rejected by Flamestrike on 2026-07-05 with response `what is this garbage...`; recovery approval remains pending.
- Follow-up Core/Kaizen improvement: Phase 7 visual-readiness gates must include rendered capture/DCC-proof comparison before a capture can be presented as review-ready.

### 2026-07-05 19:04 EDT - A002 Phase 6C Empty Visual FBX False Pass

- Asset or scope: `SM_GIA_BloodAxeCairnstone_A002` Phase 6C DCC game-ready exports and Phase 7C Unreal import attempt.
- Detected by: Phase 7C Unreal import log reported `There was nothing to import from the provided source data` for `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01.fbx`; shell inspection showed the visual FBXs are `3980` bytes and contain no `Geometry`/`Mesh` strings, while the UCX FBX is `14492` bytes.
- Last known Core-valid state: Phase 5D texture/UV/material candidate audit pass, Phase 6A DCC game-ready plan, and Phase 7A/7B script plans as written constraints. Phase 6C is not valid authority for visual FBX geometry until recovered.
- First drift action: Phase 6C DCC generator exported hidden visual LOD objects, producing empty visual FBX files, and the Phase 6C audit treated file existence as sufficient proof of FBX validity.
- Assumption or interpretation that caused drift: non-empty FBX files were treated as valid geometry exports without evidence of imported mesh contents or triangle counts.
- Affected outputs: Phase 6C visual FBXs `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01.fbx`, `_LOD0.fbx`, `_LOD1.fbx`, `_LOD2.fbx`, `_LOD3.fbx`; Phase 6C manifest/audit/handoff and output record claims about valid FBX exports; Phase 7C partial Unreal texture/material assets created before Static Mesh import failure.
- Artifact statuses: Phase 5D output remains `authoritative` for the pre-FBX DCC source; Phase 6A plan remains `authoritative`; Phase 6B scripts are `candidate` and require correction; Phase 6C visual FBX exports are `invalid`; Phase 6C UCX FBX is `partial/reference only`; Phase 6C audit and output record are `quarantined as FBX-validity authority`; Phase 7B Unreal scripts are `candidate`; Phase 7C partial Unreal texture/material assets are `quarantined` in place and not asset authority.
- Quarantined locations or records: recorded in `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECOVERY_STATUS_20260705_PHASE6C_EMPTY_FBX.md`; files are preserved in place pending approved recovery.
- Recovery decision: completed through technical Unreal validation. The invalid Phase 6C FBXs were preserved under `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/CoreRecovery/20260705_Phase6C_EmptyFBX_Quarantine/`; the Phase 6 generator and audit were corrected; recovered Phase 6C audit passed with imported FBX mesh/triangle proof; Phase 7C Unreal import, placement, and validation passed.
- Flamestrike approval: `approved` on 2026-07-05 for the recovery sequence: fix Phase 6 export/audit, rerun Phase 6C, then retry Phase 7C only after recovered audit pass.
- Follow-up Core/Kaizen improvement: all future FBX-producing DCC audits must prove imported mesh contents and triangle counts, not only file presence and size. A002 Phase 6 audit now performs this check.

### 2026-07-05 17:43 EDT - A001 Drift Quarantine And A002 Clean Restart

- Asset or scope: `SM_GIA_BloodAxeCairnstone_A001` recovery and `SM_GIA_BloodAxeCairnstone_A002` clean restart.
- Detected by: Flamestrike direction and Codex Core reassessment during A002 start.
- Last known Core-valid state: approved source template, scanline evidence, written modular component plan, written geometry construction plan, and successful-process recovery lessons.
- First drift action: A001 production advanced from planning/proof stages into generated DCC, void-fill, UV/material, export, and Unreal outputs before Core artifact status and quarantine controls were in place.
- Assumption or interpretation that caused drift: approved technical passes and proof-of-process artifacts were treated too broadly as production authority; generated outputs and adjacent workflow steps were allowed to influence later work instead of returning to the approved source and written blueprint authority.
- Affected outputs: A001 generated Saved/Automation outputs, Blender sources, FBX exports, source textures, Unreal Content assets, material/UV/import/package outputs, and late-pass generated manifests.
- Artifact statuses: approved source/template and current Core/AetherForge/A002 blueprints are `authoritative`; A001 written modular and geometry plans are `authoritative as written constraints`; A001 pre-geometry manifests are `candidate evidence` and must be revalidated before A002 use; A001 generated production outputs are `quarantined` in place; the rejected single-zone void-fill direction is `invalid/superseded`.
- Quarantined locations or records: recorded in `docs/projects/assetforge/BLOODAXE_CAIRNSTONE_A001_CORE_RECOVERY_AND_QUARANTINE_STATUS.md`; files are preserved in place pending any later approved move.
- Recovery decision: begin A002 from approved source evidence, approved written constraints, and clean generator logic. Do not use A001 generated output as A002 source authority unless Flamestrike explicitly reclassifies a specific artifact.
- Flamestrike approval: approved non-destructive quarantine recording on 2026-07-05 after Core classification discussion.
- Follow-up Core/Kaizen improvement: Core Principles, Evidence-Bound Decision Rule, updated AetherForge Blueprint, and A002 Core Reconstruction Asset Blueprint now govern the restart.
