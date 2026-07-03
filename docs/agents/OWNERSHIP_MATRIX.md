# Aerathea Agent Ownership Matrix

Last updated: 2026-06-28

## Write Ownership

| Path or area | Default owner | Notes |
| --- | --- | --- |
| `docs/agents/` | Lead / Docs Index | Workflow source of truth |
| `docs/narrative/drafts/` | Lead / Docs Index | Draft lore, story, NPC, quest, and dialogue exploration |
| `docs/narrative/packages/` | Lead / Docs Index | Structured narrative packages; production integration requires lead review |
| `docs/narrative/templates/` | Lead / Docs Index | Narrative contract templates |
| `docs/assets/ASSET_INDEX.md` | Docs Index | Lead may edit during integration only |
| `docs/assets/PRODUCTION_BACKLOG.md` | Docs Index | Avoid parallel edits |
| `docs/PRODUCTION_BOOTSTRAP.md` | Docs Index | Avoid parallel edits |
| `docs/assets/**/PRODUCTION_PACKAGE.md` | Production Package | Docs Index may update status after validation |
| `docs/assets/**/MODELING_HANDOFF.md` | Production Package / DCC | DCC may update implementation evidence when assigned |
| `docs/assets/**/BUILD_IMPORT_STATUS.md` | Unreal / VFX / Docs Index | Must be backed by validation output |
| `Tools/DCC/` | DCC Modeling Prep | QA may add focused DCC validators when assigned |
| `SourceAssets/Blender/` | DCC Modeling Prep | Do not overwrite approved sources without task packet |
| `SourceAssets/Exports/` | DCC Modeling Prep | Export output only |
| `Tools/Unreal/` | Unreal Implementation / VFX / QA | Coordinate script naming and validators |
| `Source/Aerathea/` | Gameplay Systems / Unreal Implementation | Requires C++ build validation |
| `Content/Aerathea/` | Unreal Implementation / VFX | Must use Unreal tooling for binary assets |
| `Saved/Automation/` | DCC / Unreal / QA | Review output; do not treat as source art |
| `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS` | Read-only reference | Do not bulk-copy into Git without storage-policy approval |

## Conflict Rules

- No parallel global-index edits.
- Narrative output does not create production ownership until the lead converts it into a task packet.
- No parallel startup-scene edits unless one agent owns map placement and another is read-only QA.
- No agent may revert unrelated changes.
- If a file has user or other-agent edits, adapt or return to lead for integration.
- Binary Unreal assets require explicit task ownership and validation evidence.
- Source concepts outside the repo are read-only unless Flamestrike explicitly approves a storage or curation task.
- Stale global status docs are fixed by Docs/Index tasks, not opportunistic specialist edits.

## Preflight Checklist

Before a specialist starts:

1. Read the task packet.
2. Run `git status --short` for the assigned paths.
3. Confirm no other active task owns the same write scope.
4. Confirm approval gates are clear or that the work is planning-only.
5. Confirm required validators are named.
