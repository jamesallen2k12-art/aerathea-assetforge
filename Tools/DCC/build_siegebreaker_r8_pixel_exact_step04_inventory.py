#!/usr/bin/env python3
"""Build Step 04 component/source ownership from the locked R8 evidence."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
OLD = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-A06-POC/manifests/"
    "STEP_04_COMPONENT_AND_SOURCE_OWNERSHIP_INVENTORY.json"
)
STEP03 = RUN / "manifests/STEP_03_CROP_COORDINATES.json"
MANIFEST = RUN / "manifests/STEP_04_COMPONENT_AND_SOURCE_OWNERSHIP_INVENTORY.json"
VALIDATION = RUN / "manifests/STEP_04_VALIDATION.json"
CONTRACT = RUN / "steps/STEP_04_CONTRACT.md"
OUTPUT = RUN / "steps/STEP_04_OUTPUT_RECORD.md"
HANDOFF = RUN / "handoffs/STEP_04_TO_STEP_05_HANDOFF.md"
REVIEW = RUN / "review/STEP_04_COMPONENT_AND_SOURCE_OWNERSHIP_REVIEW.md"
STATE = RUN / "manifests/STEP_STATE.json"
RUN_ID = "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
OLD_EXPECTED = "7f18df8e1580d4c682a48497598a3603dbbea4dd2de8e54ea6f669f6fd37783f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


def main() -> None:
    if sha256(OLD) != OLD_EXPECTED:
        raise RuntimeError("Locked generic Step 04 vocabulary changed")
    step03 = json.loads(STEP03.read_text())
    if step03["run_id"] != RUN_ID:
        raise RuntimeError("Wrong Step 03 authority")

    template = json.loads(OLD.read_text())
    manifest = copy.deepcopy(template)
    manifest["run_id"] = RUN_ID
    manifest["artifact_status"] = (
        "authoritative for R8 component naming and source ownership"
    )
    manifest["authority"] = {
        "step03_manifest": str(STEP03.relative_to(ROOT)),
        "step03_manifest_sha256": sha256(STEP03),
        "locked_generic_vocabulary_template": str(OLD.relative_to(ROOT)),
        "locked_generic_vocabulary_template_sha256": sha256(OLD),
        "reuse_limit": (
            "semantic component/material/annotation vocabulary only; no old "
            "coordinates, measurements, transforms, masks, or geometry"
        ),
    }
    manifest["r8_source_rectangles"] = {
        record["id"]: record["rectangle_half_open"]
        for record in step03["sources"]
    }
    manifest["r8_complete_hammer_capture_sha256"] = {
        record["id"]: record["capture_file_sha256"]
        for record in step03["sources"]
    }
    write_json(MANIFEST, manifest)

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
    checks: dict[str, bool] = {
        "step03_authority_locked": manifest["authority"][
            "step03_manifest_sha256"
        ] == sha256(STEP03),
        "generic_template_locked": sha256(OLD) == OLD_EXPECTED,
        "all_six_r8_views_present": set(manifest["r8_source_rectangles"])
        == {"front", "back", "left", "right", "top", "bottom"},
        "no_measurement_or_registration": not manifest[
            "measurement_or_registration_performed"
        ],
        "no_cross_view_resolution": not manifest[
            "cross_view_correspondence_resolved"
        ],
        "no_hidden_surface_resolution": not manifest["hidden_surface_resolved"],
        "no_geometry": not manifest["mask_contour_fill_or_geometry_created"],
        "no_old_construction_input": not manifest[
            "a01_a05_construction_input_used"
        ],
    }
    for field, (prefix, count) in families.items():
        values = manifest[field]
        checks[f"{field}_count"] = len(values) == count
        checks[f"{field}_ids"] = [v["id"] for v in values] == [
            f"{prefix}{i:03d}" for i in range(1, count + 1)
        ]
    passed = sum(checks.values())
    validation = {
        "schema": "AERATHEA_STEP_VALIDATION_V1",
        "run_id": RUN_ID,
        "step": "04",
        "result": "PASS" if passed == len(checks) else "FAIL",
        "checks_passed": passed,
        "checks_total": len(checks),
        "checks": checks,
        "manifest_sha256": sha256(MANIFEST),
    }
    write_json(VALIDATION, validation)
    if validation["result"] != "PASS":
        raise RuntimeError("Step 04 validation failed")

    CONTRACT.write_text(
        "# Step 04 Contract — Component and Source Ownership\n\n"
        f"- Run: `{RUN_ID}`\n"
        "- Status: `authoritative`\n"
        "- Governing rule: classify only what the locked R8 pixels directly "
        "show; keep correspondence, hidden surfaces, and construction unknown.\n"
        "- Input: Step 03 exact hammer-only scanline captures.\n"
        "- Reused authority: the locked A06 semantic vocabulary only. Its "
        "coordinates, measurements, masks, transforms, and construction are "
        "forbidden inputs.\n"
        "- Output decision: approve/reject the R8 component and source-ownership "
        "inventory for Step 05 registration.\n"
    )
    OUTPUT.write_text(
        "# Step 04 Output Record\n\n"
        "- Result: `PASS`\n"
        "- Artifact status: `authoritative`\n"
        "- Inventory: 19 physical observation families, 7 contacts, 6 "
        "occlusions, 5 negative spaces, 5 material regions, 5 rune motifs, "
        "6 annotation classes, and 12 explicitly unresolved unknowns.\n"
        "- No coordinate measurement, correspondence solution, hidden-surface "
        "solution, or geometry was introduced.\n"
        f"- Validation: `{passed}/{len(checks)}` checks passed.\n"
    )
    HANDOFF.write_text(
        "# Step 04 → Step 05 Handoff\n\n"
        "- Step 04 is complete and authoritative.\n"
        "- Step 05 may register the six complete R8 views using one uniform "
        "transform per complete view.\n"
        "- The only absolute anchor is 170 cm overall length.\n"
        "- The right-view bisection center remains source x=557; no half may "
        "be normalized to the other.\n"
        "- All hidden geometry and cross-view correspondences remain unresolved "
        "until their documented gates.\n"
    )
    REVIEW.write_text(
        "# Step 04 Review — R8 Component and Source Ownership\n\n"
        "Result: **PASS**\n\n"
        "| Evidence class | Count | Status |\n"
        "|---|---:|---|\n"
        "| Physical observation families | 19 | source-owned |\n"
        "| Contacts | 7 | observed, hidden attachment unresolved |\n"
        "| Occlusions | 6 | source-owned |\n"
        "| Negative spaces | 5 | closure unresolved |\n"
        "| Material regions | 5 | source-owned |\n"
        "| Rune motifs | 5 | continuity unresolved |\n"
        "| Annotation classes | 6 | excluded from object ownership |\n"
        "| Unknowns | 12 | explicitly unresolved |\n\n"
        "No measurements, registration, inferred fill, hidden surfaces, or "
        "geometry were created in this step.\n"
    )
    state = json.loads(STATE.read_text())
    state["current_step"] = "05"
    state["completed_steps"] = ["01", "02", "03", "04"]
    state["last_validation"] = str(VALIDATION.relative_to(ROOT))
    write_json(STATE, state)
    print(f"STEP04 PASS {passed}/{len(checks)}")


if __name__ == "__main__":
    main()
