---
name: aerathea-docs-index
description: Maintain Aerathea production documentation and indexes. Use for ASSET_INDEX, PRODUCTION_BACKLOG, BUILD_IMPORT_STATUS, PRODUCTION_BOOTSTRAP, approval queues, task board updates, package status, validation-result wording, and stale reference cleanup after implementation.
---

# Aerathea Docs Index

## Quick Start

1. Update docs only after implementation or validation evidence exists.
2. Keep `docs/assets/ASSET_INDEX.md`, `docs/assets/PRODUCTION_BACKLOG.md`, and `docs/PRODUCTION_BOOTSTRAP.md` consistent.
3. Add build/import status docs beside asset packages when a build lane completes.
4. Remove stale "future" or "pending" wording only when the validator or asset actually exists.
5. Run `git diff --check` and targeted `rg` scans after edits.

## Documentation Rules

- Do not overclaim final art when only first-pass assets exist.
- Record exact validator names and meaningful result summaries.
- Keep remaining work explicit.
- Link to the production package, handoff, build status, and approval gate where useful.

## Ownership

This role may edit global docs only when assigned by the lead. Specialists should not independently update global indexes unless the task packet names those files.
