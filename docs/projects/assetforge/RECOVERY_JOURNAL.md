# AssetForge Recovery Journal

Status: Active
Started: 2026-07-03

This journal is the short, tracked recovery trail for AssetForge work. Use it to resume after a reboot, reset, crash, power outage, or context loss.

Heavy raw outputs remain in ignored `Saved/AssetForgeResearch/` paths. This file records what matters: timestamp, intent, result, key artifact paths, blockers, and next action.

## Recovery Rules

- Run `Tools/System/aerathea_checkpoint.sh "short note"` before starting a long job, after it finishes, and before stopping for the night.
- Keep journal entries concise enough to commit.
- Keep raw logs, generated meshes, model weights, and large previews out of git unless explicitly promoted.
- Commit tracked notes and manifests at useful checkpoints, even when the research itself is still WIP.
- Do not write tokens, API keys, private URLs, or credentials into the journal.

## Entries

### 2026-07-03 07:10 EDT - Recovery hardening baseline

- Goal: protect AssetForge learning from reset/power loss.
- Local docs now capture the TRELLIS/TRELLIS.2 install, benchmark results, external-tool boundary, and project plan.
- Key tracked docs:
  - `docs/projects/assetforge/ASSETFORGE_PROVENANCE_LOG.md`
  - `docs/projects/assetforge/ASSETFORGE_PROJECT_PLAN.md`
  - `docs/projects/assetforge/reports/ASSETFORGE_CONTROLLED_BENCHMARKS_20260703.md`
  - `docs/projects/assetforge/reports/TRELLIS2_AMD_INSTALL_NOTES_20260702.md`
  - `docs/projects/assetforge/reports/TRELLIS_AMD_SMOKE_TEST_20260702.md`
  - `docs/systems/ASSETFORGE_EXTERNAL_EVALUATION_TOOLS.md`
- Latest verified AssetForge write before this hardening pass: `2026-07-02 23:15:40 EDT`, `ASSETFORGE_PROVENANCE_LOG.md`.
- Latest verified benchmark repair output before this hardening pass: `2026-07-02 23:14:50 EDT`, repaired `50k`, `20k`, and `10k` GLB/PLY variants under `Saved/AssetForgeResearch/benchmarks/.../decimation/repaired/`.
- Immediate next action: add and use an automated checkpoint script, then make a scoped WIP commit containing the tracked recovery/provenance docs.

### 2026-07-03 07:12:00 EDT -0400 - recovery hardening script validation

- Snapshot: `Saved/ProjectRecovery/20260703-071200/`
- Git: branch `main`, HEAD `5d56ba4`, status lines `760`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-071200/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-071200/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-071200/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 07:12:33 EDT -0400 - clean checkpoint validation after sort fix

- Snapshot: `Saved/ProjectRecovery/20260703-071233/`
- Git: branch `main`, HEAD `5d56ba4`, status lines `760`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-071233/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-071233/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-071233/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 07:39:27 EDT -0400 - pre dirty worktree triage

- Snapshot: `Saved/ProjectRecovery/20260703-073927/`
- Git: branch `main`, HEAD `b95c680`, status lines `756`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-073927/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-073927/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-073927/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 07:46:52 EDT -0400 - post GitHub protection clean state

- Snapshot: `Saved/ProjectRecovery/20260703-074652/`
- Git: branch `main`, HEAD `1b55c7f`, status lines `0`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-074652/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-074652/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-074652/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 08:00:09 EDT -0400 - automatic checkpoint timer installed and verified

- Snapshot: `Saved/ProjectRecovery/20260703-080009/`
- Git: branch `main`, HEAD `c43631f`, status lines `5`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-080009/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-080009/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-080009/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 08:02:27 EDT -0400 - pre AssetForge Unreal import validation benchmark

- Snapshot: `Saved/ProjectRecovery/20260703-080227/`
- Git: branch `main`, HEAD `2ed1b4a`, status lines `0`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-080227/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-080227/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-080227/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 08:05:15 EDT -0400 - post AssetForge Unreal import validation benchmark

- Snapshot: `Saved/ProjectRecovery/20260703-080515/`
- Git: branch `main`, HEAD `2ed1b4a`, status lines `2`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-080515/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-080515/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-080515/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 08:57:43 EDT -0400 - pre Blood Axe cairn variant batch build

- Snapshot: `Saved/ProjectRecovery/20260703-085743/`
- Git: branch `main`, HEAD `c866930`, status lines `0`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-085743/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-085743/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-085743/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 09:11:20 EDT -0400 - post Blood Axe cairn variant batch build

- Snapshot: `Saved/ProjectRecovery/20260703-091120/`
- Git: branch `main`, HEAD `c866930`, status lines `28`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-091120/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-091120/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-091120/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 09:31:58 EDT -0400 - pre Blood Axe cairn DCC review sheet

- Snapshot: `Saved/ProjectRecovery/20260703-093158/`
- Git: branch `main`, HEAD `4fb91bc`, status lines `0`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-093158/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-093158/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-093158/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 09:39:00 EDT -0400 - post Blood Axe cairn DCC review and revision pass

- Snapshot: `Saved/ProjectRecovery/20260703-093900/`
- Git: branch `main`, HEAD `4fb91bc`, status lines `79`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-093900/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-093900/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-093900/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 10:06:30 EDT -0400 - pre Blood Axe cairn game-ready prep pass

- Snapshot: `Saved/ProjectRecovery/20260703-100630/`
- Git: branch `main`, HEAD `16eb7ec`, status lines `0`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-100630/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-100630/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-100630/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 10:17:08 EDT -0400 - post Blood Axe cairn game-ready prep pass

- Snapshot: `Saved/ProjectRecovery/20260703-101708/`
- Git: branch `main`, HEAD `16eb7ec`, status lines `93`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-101708/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-101708/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-101708/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 10:20:20 EDT -0400 - pre Blood Axe cairn Unreal import pass

- Snapshot: `Saved/ProjectRecovery/20260703-102020/`
- Git: branch `main`, HEAD `c10c8b3`, status lines `0`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-102020/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-102020/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-102020/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 10:45:28 EDT -0400 - post Blood Axe cairn Unreal import pass

- Snapshot: `Saved/ProjectRecovery/20260703-104528/`
- Git: branch `main`, HEAD `c10c8b3`, status lines `117`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-104528/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-104528/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-104528/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 10:50:42 EDT -0400 - post Blood Axe cairn Unreal visual review gate

- Snapshot: `Saved/ProjectRecovery/20260703-105042/`
- Git: branch `main`, HEAD `96c08ea`, status lines `2`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-105042/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-105042/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-105042/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 11:14:57 EDT -0400 - post Blood Axe cairn texture material candidate

- Snapshot: `Saved/ProjectRecovery/20260703-111457/`
- Git: branch `main`, HEAD `5452f72`, status lines `27`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-111457/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-111457/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-111457/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 12:22:38 EDT -0400 - post Blood Axe cairn A1 DCC source candidate

- Snapshot: `Saved/ProjectRecovery/20260703-122238/`
- Git: branch `main`, HEAD `4e71cc5`, status lines `6`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-122238/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-122238/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-122238/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 12:40:24 EDT -0400 - post static prop reference benchmark audit

- Snapshot: `Saved/ProjectRecovery/20260703-124024/`
- Git: branch `main`, HEAD `1f36466`, status lines `3`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-124024/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-124024/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-124024/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.

### 2026-07-03 13:02:19 EDT -0400 - post Blood Axe A1 geometry pass 2

- Snapshot: `Saved/ProjectRecovery/20260703-130219/`
- Git: branch `main`, HEAD `932393a`, status lines `11`
- Recovery files:
  - `Saved/ProjectRecovery/20260703-130219/git_status_short.txt`
  - `Saved/ProjectRecovery/20260703-130219/recent_project_files.txt`
  - `Saved/ProjectRecovery/20260703-130219/assetforge_recent_saved_outputs.txt`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.
