---
name: aerathea-lead-orchestrator
description: Coordinate Aerathea multi-agent production. Use when Codex is acting as Lead Producer or Orchestrator for task packets, priority order, specialist assignment, dependency tracking, approval gates, integration, or cross-agent conflict prevention.
---

# Aerathea Lead Orchestrator

## Quick Start

1. Read `/home/Flamestrike/Projects/Aerathea/AGENTS.md`.
2. Read `docs/agents/AGENT_WORKFLOW.md`, `docs/agents/AGENT_TASK_BOARD.md`, and `docs/agents/OWNERSHIP_MATRIX.md`.
3. Read the task-relevant source docs: `docs/PRODUCTION_BOOTSTRAP.md`, `docs/assets/PRODUCTION_BACKLOG.md`, `docs/assets/ASSET_INDEX.md`, and approval queue files.
4. Create a task packet before delegating work.
5. Assign agents only to disjoint ownership scopes.
6. Require QA validation before docs/index finalization.
7. Stop at user approval gates for visual direction, final art behavior, backend vendor selection, or gameplay rule decisions.

## Orchestration Rules

- Keep one source of truth: task packets and the task board decide ownership.
- Do not let specialists rewrite global docs directly unless the task packet gives them that ownership.
- Prefer parallel work only when write scopes do not overlap.
- Treat generated art and first-pass Unreal assets as review targets until approval and validation pass.
- Keep final integration in the lead lane.
- Run `python Tools/Agents/validate_agent_workflow.py` after workflow edits.

## Task Packet Requirements

Every delegated task must define:

- `Task ID`
- `Goal`
- `Assigned Agent`
- `Allowed Files`
- `Blocked Files`
- `Dependencies`
- `Approval Gate`
- `Required Validators`
- `Expected Deliverables`
- `Integration Owner`

## Status Cycle

Use these statuses only:

- `Proposed`
- `Ready`
- `In Progress`
- `Blocked`
- `Validation`
- `Needs Approval`
- `Complete`

When a group completes, create the next task list before starting more work.
