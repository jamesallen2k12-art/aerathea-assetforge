# Aerathea Task Packet Template

Copy this structure into `docs/agents/AGENT_TASK_BOARD.md` for each new task.

```markdown
## AET-MA-YYYYMMDD-###

- Status: Proposed
- Goal:
- Assigned Agent:
- Skill:
- Priority:
- Allowed Files:
- Blocked Files:
- Dependencies:
- Approval Gate:
- Required Validators:
- Preflight:
- Expected Deliverables:
- Integration Owner:
- QA Owner:
- Docs Owner:
- Notes:
```

## Preflight Field

Use the `Preflight` field to record the required initial checks, usually:

- `git status --short <assigned paths>`
- source-of-truth docs read
- approval gate checked
- validator list confirmed

## Status Values

- `Proposed`
- `Ready`
- `In Progress`
- `Blocked`
- `Validation`
- `Needs Approval`
- `Complete`
