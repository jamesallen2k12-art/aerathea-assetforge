#!/usr/bin/env python3
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
AGENT_DOCS = ROOT / "docs" / "agents"
SKILLS = AGENT_DOCS / "skills"

REQUIRED_DOCS = [
    AGENT_DOCS / "AGENT_WORKFLOW.md",
    AGENT_DOCS / "AGENT_TASK_BOARD.md",
    AGENT_DOCS / "OWNERSHIP_MATRIX.md",
    AGENT_DOCS / "TASK_PACKET_TEMPLATE.md",
    AGENT_DOCS / "AGENT_SKILLS_MANIFEST.md",
]

REQUIRED_SKILLS = [
    "aerathea-lead-orchestrator",
    "aerathea-visual-art-direction",
    "aerathea-production-package",
    "aerathea-dcc-modeling-prep",
    "aerathea-unreal-implementation",
    "aerathea-gameplay-systems",
    "aerathea-vfx-materials",
    "aerathea-qa-validation",
    "aerathea-docs-index",
]

TASK_FIELDS = [
    "Status",
    "Goal",
    "Assigned Agent",
    "Skill",
    "Priority",
    "Allowed Files",
    "Blocked Files",
    "Dependencies",
    "Approval Gate",
    "Required Validators",
    "Preflight",
    "Expected Deliverables",
    "Integration Owner",
    "QA Owner",
    "Docs Owner",
]

VALID_STATUSES = {
    "Proposed",
    "Ready",
    "In Progress",
    "Blocked",
    "Validation",
    "Needs Approval",
    "Complete",
}

UNFINISHED_MARKERS = ("TO" + "DO", "[" + "TO" + "DO")


def frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        return {}
    values = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def validate_docs(failures):
    for path in REQUIRED_DOCS:
        if not path.exists():
            failures.append(f"missing required workflow doc: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in UNFINISHED_MARKERS):
            failures.append(f"{path.relative_to(ROOT)} still contains unfinished template text")


def validate_skills(failures):
    for skill_name in REQUIRED_SKILLS:
        skill_dir = SKILLS / skill_name
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            failures.append(f"missing skill file: {skill_file.relative_to(ROOT)}")
            continue
        text = skill_file.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if meta.get("name") != skill_name:
            failures.append(f"{skill_file.relative_to(ROOT)} name is {meta.get('name')!r}, expected {skill_name!r}")
        if not meta.get("description") or any(marker in meta.get("description", "") for marker in UNFINISHED_MARKERS):
            failures.append(f"{skill_file.relative_to(ROOT)} has missing or unfinished description")
        if any(marker in text for marker in UNFINISHED_MARKERS):
            failures.append(f"{skill_file.relative_to(ROOT)} still contains unfinished template text")
        if not (skill_dir / "agents" / "openai.yaml").exists():
            failures.append(f"missing openai.yaml for {skill_name}")


def task_sections(board_text):
    matches = list(re.finditer(r"^## (AET-MA-\d{8}-\d{3})\n", board_text, flags=re.MULTILINE))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(board_text)
        yield match.group(1), board_text[start:end]


def field_value(section, field):
    match = re.search(rf"^- {re.escape(field)}:\s*(.*)$", section, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def validate_task_board(failures):
    board = AGENT_DOCS / "AGENT_TASK_BOARD.md"
    if not board.exists():
        return
    text = board.read_text(encoding="utf-8")
    tasks = list(task_sections(text))
    if not tasks:
        failures.append("AGENT_TASK_BOARD.md has no task packets")
        return
    for task_id, section in tasks:
        for field in TASK_FIELDS:
            value = field_value(section, field)
            if value is None:
                failures.append(f"{task_id} missing field {field}")
            elif not value:
                failures.append(f"{task_id} field {field} is empty")
        status = field_value(section, "Status")
        if status and status not in VALID_STATUSES:
            failures.append(f"{task_id} has invalid status {status!r}")


def main():
    failures = []
    validate_docs(failures)
    validate_skills(failures)
    validate_task_board(failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    print(f"Aerathea agent workflow validation passed: {len(REQUIRED_SKILLS)} skills, {len(REQUIRED_DOCS)} workflow docs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
