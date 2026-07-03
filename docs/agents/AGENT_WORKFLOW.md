# Aerathea Multi-Agent Production Workflow

Last updated: 2026-06-30

## Purpose

This workflow turns Aerathea production from a single sequential lane into a lead-orchestrated parallel system:

`Lead creates task packet -> specialists work in parallel -> QA validates -> Lead integrates -> Flamestrike approves visual gates`

The lead producer/orchestrator owns priority, dependencies, task packet quality, conflict prevention, final integration, and approval gates.

## Roles

| Role | Skill source | Primary ownership |
| --- | --- | --- |
| Lead Producer / Orchestrator | `docs/agents/skills/aerathea-lead-orchestrator/` | priority, task packets, dependencies, integration, approval gates |
| Visual Cleanse / Art Direction | `docs/agents/skills/aerathea-visual-art-direction/` | reference cleanup, silhouette lock, style direction |
| Production Package | `docs/agents/skills/aerathea-production-package/` | packages, handoffs, LOD/collision/import specs |
| DCC / Modeling Prep | `docs/agents/skills/aerathea-dcc-modeling-prep/` | Blender sources, FBX exports, proof renders |
| Unreal Implementation | `docs/agents/skills/aerathea-unreal-implementation/` | Unreal imports, Blueprints, materials, sockets, placement |
| Gameplay Systems | `docs/agents/skills/aerathea-gameplay-systems/` | combat, interaction, timing, loot, quest, encounter contracts |
| VFX / Materials | `docs/agents/skills/aerathea-vfx-materials/` | state materials, Niagara, VFX readability, scalar contracts |
| QA / Validation | `docs/agents/skills/aerathea-qa-validation/` | validators, startup checks, regressions, review readiness |
| Docs / Index | `docs/agents/skills/aerathea-docs-index/` | indexes, backlog, build status, bootstrap, stale wording cleanup |

## Source Of Truth

- Project rules: `AGENTS.md`
- Active workflow board: `docs/agents/AGENT_TASK_BOARD.md`
- Ownership rules: `docs/agents/OWNERSHIP_MATRIX.md`
- Task template: `docs/agents/TASK_PACKET_TEMPLATE.md`
- Standing pipeline approval policy: `docs/agents/AET-MA-20260630_PIPELINE_APPROVAL_POLICY.md`
- Skill manifest: `docs/agents/AGENT_SKILLS_MANIFEST.md`
- Production bootstrap: `docs/PRODUCTION_BOOTSTRAP.md`
- Unreal baseline: `docs/UNREAL_ENGINE_BASELINE.md`
- Asset index: `docs/assets/ASSET_INDEX.md`
- Production backlog: `docs/assets/PRODUCTION_BACKLOG.md`
- Concept manifest: `docs/assets/ASSET_CONCEPTS_MANIFEST.md`
- Intake queue: `docs/assets/ASSET_CONCEPTS_INTAKE_QUEUE.md`
- Approval queue: `docs/assets/APPROVAL_QUEUE.md`
- Visual canon workflow: `docs/assets/VISUAL_CANON_WORKFLOW.md`
- Visual canon registry: `docs/assets/VISUAL_CANON_REGISTRY.md`
- Race scale reference: `docs/assets/reference/README.md`
- Relevant lore/system anchors: `docs/lore/**`, `docs/systems/**`

## Authority Notes

- Treat `AGENTS.md`, `docs/PRODUCTION_BOOTSTRAP.md`, `docs/assets/ASSET_INDEX.md`, `docs/assets/PRODUCTION_BACKLOG.md`, and per-package docs as higher authority than generic design notes.
- Treat `docs/assets/ASSET_CONCEPTS_MANIFEST.md` as the current concept-count authority when counts conflict.
- Treat source concepts in `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS` as external references; do not bulk-copy them into Git without storage-policy approval.
- Check `git status --short` before assigning or starting any lane. The project may contain unrelated user or agent edits.
- If `docs/PRODUCTION_BOOTSTRAP.md` source-control status conflicts with live `git remote` or branch state, verify with git commands and update through a Docs/Index task.

## Delegation Rules

1. Create a task packet before spawning or assigning a specialist.
2. Use one integration owner per task.
3. Keep write scopes disjoint for parallel work.
4. Assign exclusive ownership for `Content/`, `SourceAssets/`, and startup-scene mutation lanes.
5. Do not let two agents edit the same global index at the same time.
6. Specialists may propose doc updates; the lead or Docs/Index agent applies global index updates.
7. QA validates before Docs/Index marks work complete.
8. Visual changes that affect final look stop at `Needs Approval`.
9. Runtime systems that affect multiplayer authority, backend selection, economy, or combat identity stop at `Needs Approval`.
10. Narrative proposals stop at lead review before becoming production task-board, asset, gameplay, or Unreal work.

## Standing Pipeline Approval

Flamestrike approved the production pipeline on 2026-06-30. Once a task packet names scope, allowed files, blocked files, dependencies, validators, and integration owner, technical production may proceed without repeated approval if it stays inside the approved Aerathea art/style anchors, visual-canon entries, and the packet's write scope.

This approval covers scoped DCC source creation, source/export folder creation, FBX export, Unreal import/configuration, material instance setup, focused validators, build/import status docs, review-capture preparation, and Docs/Index alignment. First-pass assets and captures remain review targets until validation and final subjective approval are complete.

Stop at `Needs Approval` for generated image selection, source-concept approval, visual-canon approval, final visual approval, final silhouette, color language, race/faction identity, hero art direction, major VFX behavior, combat-system identity, playstyle, combat feel, ability pacing, encounter feel, economy, vendor/reward direction, backend or multiplayer authority, source-concept storage policy, or final shipped startup composition.

Every visual/DCC/Unreal/VFX task packet must preserve the visual markers in `AGENTS.md`: readable silhouette, stylized fantasy MMORPG shape language, hand-painted texture intent, mid-poly MMO-safe construction, restrained emissive accents, and no style drift.

When a canon entry exists, DCC and Unreal review work must compare against that canon image before asking for approval. If no canon entry exists for a subjective look, create a grouped concept-board approval task before implementation.

## Required Completion Gate

A task is complete only when:

- deliverables exist in the assigned paths
- focused validators pass
- startup validation passes when startup scene or global assets changed
- docs/indexes reflect the true status
- approval gates are resolved or explicitly listed as blocking
- `python Tools/Agents/validate_agent_workflow.py` passes after workflow edits
