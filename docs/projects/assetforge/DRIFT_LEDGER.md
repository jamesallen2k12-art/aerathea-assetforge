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

### 2026-07-05 19:04 EDT - A002 Phase 6C Empty Visual FBX False Pass

- Asset or scope: `SM_GIA_BloodAxeCairnstone_A002` Phase 6C DCC game-ready exports and Phase 7C Unreal import attempt.
- Detected by: Phase 7C Unreal import log reported `There was nothing to import from the provided source data` for `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01.fbx`; shell inspection showed the visual FBXs are `3980` bytes and contain no `Geometry`/`Mesh` strings, while the UCX FBX is `14492` bytes.
- Last known Core-valid state: Phase 5D texture/UV/material candidate audit pass, Phase 6A DCC game-ready plan, and Phase 7A/7B script plans as written constraints. Phase 6C is not valid authority for visual FBX geometry until recovered.
- First drift action: Phase 6C DCC generator exported hidden visual LOD objects, producing empty visual FBX files, and the Phase 6C audit treated file existence as sufficient proof of FBX validity.
- Assumption or interpretation that caused drift: non-empty FBX files were treated as valid geometry exports without evidence of imported mesh contents or triangle counts.
- Affected outputs: Phase 6C visual FBXs `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01.fbx`, `_LOD0.fbx`, `_LOD1.fbx`, `_LOD2.fbx`, `_LOD3.fbx`; Phase 6C manifest/audit/handoff and output record claims about valid FBX exports; Phase 7C partial Unreal texture/material assets created before Static Mesh import failure.
- Artifact statuses: Phase 5D output remains `authoritative` for the pre-FBX DCC source; Phase 6A plan remains `authoritative`; Phase 6B scripts are `candidate` and require correction; Phase 6C visual FBX exports are `invalid`; Phase 6C UCX FBX is `partial/reference only`; Phase 6C audit and output record are `quarantined as FBX-validity authority`; Phase 7B Unreal scripts are `candidate`; Phase 7C partial Unreal texture/material assets are `quarantined` in place and not asset authority.
- Quarantined locations or records: recorded in `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECOVERY_STATUS_20260705_PHASE6C_EMPTY_FBX.md`; files are preserved in place pending approved recovery.
- Recovery decision: pending Flamestrike approval. Proposed smallest sufficient recovery is to correct the Phase 6 generator to export visible visual LOD meshes, correct the Phase 6 audit to re-import or otherwise prove FBX mesh/triangle contents, rerun Phase 6C, then rerun Phase 7C only after the recovered DCC audit passes.
- Flamestrike approval: pending.
- Follow-up Core/Kaizen improvement: all future FBX-producing DCC audits must prove imported mesh contents and triangle counts, not only file presence and size.

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
