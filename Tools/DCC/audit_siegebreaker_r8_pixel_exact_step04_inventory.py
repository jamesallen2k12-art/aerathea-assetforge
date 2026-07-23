#!/usr/bin/env python3
"""Independent direct audit of the Step 04 ownership inventory."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
MANIFEST = RUN / "manifests/STEP_04_COMPONENT_AND_SOURCE_OWNERSHIP_INVENTORY.json"
OUT = RUN / "manifests/STEP_04_INDEPENDENT_AUDIT.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    value = json.loads(MANIFEST.read_text())
    families = {
        "physical_observation_families": ("PV", 19),
        "contacts": ("CT", 7),
        "occlusions": ("OC", 6),
        "negative_spaces": ("NS", 5),
        "material_regions": ("MR", 5),
        "rune_motifs": ("RM", 5),
        "annotation_classes": ("AN", 6),
        "unresolved_unknowns": ("UK", 12),
    }
    checks: dict[str, bool] = {}
    for field, (prefix, count) in families.items():
        rows = value[field]
        checks[f"{field}_count"] = len(rows) == count
        checks[f"{field}_unique"] = len({r["id"] for r in rows}) == count
        checks[f"{field}_sequence"] = [r["id"] for r in rows] == [
            f"{prefix}{i:03d}" for i in range(1, count + 1)
        ]
    forbidden_tokens = (
        "scale_cm_per_pixel",
        "world_coordinate",
        "mesh",
        "vertex",
        "face_index",
    )
    payload = MANIFEST.read_text().lower()
    for token in forbidden_tokens:
        checks[f"forbidden_{token}_absent"] = token not in payload
    checks["all_annotations_excluded"] = all(
        not row["object_ownership"] for row in value["annotation_classes"]
    )
    checks["all_unknowns_unresolved"] = all(
        row["status"] == "unresolved" for row in value["unresolved_unknowns"]
    )
    checks["six_rectangles"] = len(value["r8_source_rectangles"]) == 6
    passed = sum(checks.values())
    audit = {
        "schema": "AERATHEA_INDEPENDENT_AUDIT_V1",
        "step": "04",
        "result": "PASS" if passed == len(checks) else "FAIL",
        "checks_passed": passed,
        "checks_total": len(checks),
        "checks": checks,
        "audited_manifest_sha256": sha256(MANIFEST),
    }
    OUT.write_text(json.dumps(audit, indent=2) + "\n")
    if audit["result"] != "PASS":
        raise RuntimeError("Independent Step 04 audit failed")
    print(f"STEP04 INDEPENDENT PASS {passed}/{len(checks)}")


if __name__ == "__main__":
    main()
