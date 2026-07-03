---
name: aerathea-qa-validation
description: Validate Aerathea production work. Use for focused validators, startup scene checks, camera/review alignment, asset bounds, sockets, naming, material references, stale docs, regression scans, syntax checks, and acceptance reports.
---

# Aerathea QA Validation

## Quick Start

1. Read the task packet and expected validators.
2. Confirm ownership before editing validator scripts.
3. Prefer focused validators over broad manual inspection.
4. Run syntax checks before Unreal command-line checks.
5. Report exact pass/fail outputs and residual risks.

## Common Checks

- `python -m py_compile ...`
- focused `Tools/Unreal/validate_*.py`
- `Tools/Unreal/validate_startup_scene.py`
- `git diff --check`
- stale wording scans with `rg`
- visual capture orientation checks when approval images are involved

## Failure Handling

When validation fails:

- identify the owning lane
- avoid reverting unrelated work
- fix only the failing contract if ownership allows
- return blockers to the lead if approval or cross-lane changes are needed
