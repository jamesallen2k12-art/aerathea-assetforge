# A005 S10R-006-R9-A Git Rollback Closeout A01 Output Record

Status: dependency-complete A005 rollback snapshot committed, pushed, and remote-verified

Artifact classification: `authoritative Git rollback closeout record`

Closeout ID: `A005-GIT-S10R-006-R9-A-ROLLBACK-A01`

Date: 2026-07-20

## Goal And Authority

Flamestrike authorized Codex to proceed uninterrupted to a clean Git rollback
point. This closeout interprets that authority as a dependency-complete,
pushed A005 rollback anchor while preserving unrelated user work outside the
commit.

The Git closeout does not alter the production boundary. The exact R9 rule is
approved only as bounded symbolic interpretation. Evaluation, implementation,
Step 10 closeout, Step 11, DCC, Unreal, and production remain unauthorized.

## Core Reassessment Result

`main` and `assetforge/main` both begin this closeout at
`f5259456b05a95ff5f7422ba2cabf0e288a85d03`, the approved Step 09 audit.
The current approved A005 state depends on the full uncommitted post-Step-09
authority chain through R9. An isolated R9 commit would therefore be an
incomplete rollback point.

The smallest sufficient dependency closure is:

- the current approved `AGENTS.md` used by the post-Step-09 hash locks;
- the complete A005 blueprint directory, including authoritative, candidate,
  proof-only, quarantined, invalid, and reference-only history exactly as
  classified;
- nineteen exact A005-only audit/build scripts; and
- the A005-bearing `DRIFT_LEDGER.md`.

The global recovery journal, local checkpoints, generic workflow edits, other
asset lines, DCC/Unreal products, and every unrelated worktree path are
excluded.

## Pre-Scope Validation

- A005 changed paths before closeout records: `208`.
- A005 current bytes before closeout records: `13,303,466`.
- JSON parse: `111/111` passed.
- A005 script AST parse: `19/19` passed.
- Largest scoped file: `1,995,839` bytes.
- Secret indicator matches: `0`.
- Tracked diff check: passed.
- Staged paths before closeout: `0`.
- Pre-staging checkpoint: `Saved/ProjectRecovery/20260720-135030/`.

## Staged Snapshot Validation

- Exact staged paths: `232/232`; paths outside the approved scope: `0`.
- Required A005 support scripts: `19/19`; missing scripts: `0`.
- Unstaged differences inside the rollback scope: `0`.
- JSON parse: `113/113` passed.
- A005 support-script AST parse: `19/19` passed.
- Secret indicator matches: `0`.
- Local-only or otherwise excluded staged paths: `0`.
- Staged name/status SHA-256:
  `35f2a00922a8fbe9256aee39016157af61a1d7368e46dffec1a5ec6ad191db70`.
- Staged diff summary: `232 files changed, 95,960 insertions(+), 6 deletions(-)`.

`git diff --cached --check` reports fourteen historical `new blank line at
EOF` warnings and no other whitespace errors. Every warning-bearing file is
already referenced by one or more later SHA-256 authority locks. Those bytes
are therefore preserved exactly and the warnings are accepted as explicit
historical-evidence exceptions; no authority record was cosmetically rewritten
to silence them.

## Git Rollback Result

- Dependency snapshot commit:
  `571d9002e3120cf0c383c78e5e37f0b0353a7f71`.
- Commit subject: `Checkpoint BloodAxe A005 authority through R9`.
- Push: passed to `assetforge/main`.
- Remote verification: local `HEAD` and
  `git ls-remote assetforge refs/heads/main` matched exactly at the dependency
  snapshot commit.
- A005 rollback scope after the dependency commit: clean.

The immediate metadata closeout commit records this already-proven snapshot;
its own hash is intentionally not embedded in itself. Unrelated worktree dirt
remains preserved and outside both commits. The production boundary remains
the approved R9 stop for Core reassessment, with no evaluation or
implementation authority.
