#!/usr/bin/env python3
"""Validate the approved twin-hammer centered-face recovery amendment."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
RECOVERY_ID = "TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_RECOVERY_A01"
PROOF_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
AMENDMENT = PROOF_ROOT / f"manifests/{RECOVERY_ID}.json"
VALIDATION = PROOF_ROOT / f"manifests/{RECOVERY_ID}_VALIDATION.json"
STEP_STATE = PROOF_ROOT / "manifests/STEP_STATE.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> int:
    if VALIDATION.exists():
        raise RuntimeError(f"Validation output already exists: {VALIDATION}")
    amendment = load_json(AMENDMENT)
    step_state = load_json(STEP_STATE)
    checks: list[dict[str, Any]] = []

    def check(check_id: str, condition: bool, observed: Any) -> None:
        checks.append(
            {
                "check_id": check_id,
                "result": "PASS" if condition else "FAIL",
                "observed": observed,
            }
        )

    check(
        "AMENDMENT-SCHEMA",
        amendment["schema"]
        == "AERATHEA_TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_RECOVERY_A01_V1",
        amendment["schema"],
    )
    check("RECOVERY-ID", amendment["recovery_id"] == RECOVERY_ID, amendment["recovery_id"])
    check("RUN-ID", amendment["run_id"] == RUN_ID, amendment["run_id"])
    check("DECISION-APPROVED", amendment["decision"] == "approved", amendment["decision"])
    check(
        "FLAMESTRIKE-APPROVED",
        amendment["flamestrike_approval"]["decision"] == "approved",
        amendment["flamestrike_approval"]["decision"],
    )

    authority = amendment["governing_authority"]
    locked_inputs = [
        authority["shared_depth_blueprint"],
        authority["approved_mirror_visual_contract"],
        authority["approved_mirror_visual_decision"],
        authority["front_measurement"],
        authority["component_scanlines"],
        *authority["source_images"].values(),
    ]
    for record in locked_inputs:
        path = ROOT / record["path"]
        observed = sha256(path) if path.is_file() else None
        check(
            f"HASH-{Path(record['path']).name}",
            observed == record["sha256"],
            {"expected": record["sha256"], "observed": observed},
        )

    preserved = amendment["preserved_failed_sources"]
    check(
        "FAILED-SOURCES-NOT-GEOMETRY-INPUT",
        preserved["read_as_geometry_input"] is False,
        preserved["read_as_geometry_input"],
    )
    check(
        "FAILED-SOURCES-IMMUTABLE",
        preserved["save_or_modify_allowed"] is False,
        preserved["save_or_modify_allowed"],
    )
    for asset_key in ("siege_breaker", "foe_hammer"):
        record = preserved[asset_key]
        path = ROOT / record["path"]
        observed = sha256(path) if path.is_file() else None
        check(
            f"FAILED-SOURCE-HASH-{asset_key.upper()}",
            observed == record["sha256"],
            {"expected": record["sha256"], "observed": observed},
        )

    evidence = amendment["proven_alignment_evidence"]
    shared_min = Fraction(evidence["shared_body_z_cm_exact"]["minimum"])
    shared_max = Fraction(evidence["shared_body_z_cm_exact"]["maximum"])
    face_min = Fraction(evidence["unshifted_local_c04_z_cm_exact"]["minimum"])
    face_max = Fraction(evidence["unshifted_local_c04_z_cm_exact"]["maximum"])
    shift = Fraction(evidence["centered_positive_z_translation_cm_exact"])
    shifted_min = Fraction(evidence["shifted_local_c04_z_cm_exact"]["minimum"])
    shifted_max = Fraction(evidence["shifted_local_c04_z_cm_exact"]["maximum"])
    expected_shift = (shared_min + shared_max - face_min - face_max) / 2

    check("CENTER-SHIFT-EXACT", shift == expected_shift, str(shift))
    check("SHIFTED-MIN-EXACT", shifted_min == face_min + shift, str(shifted_min))
    check("SHIFTED-MAX-EXACT", shifted_max == face_max + shift, str(shifted_max))
    check(
        "CENTERED-MIDPOINTS-EQUAL",
        (shifted_min + shifted_max) / 2 == (shared_min + shared_max) / 2,
        str((shifted_min + shifted_max) / 2),
    )
    check(
        "NO-C04-SCALE-CHANGE",
        shifted_max - shifted_min == face_max - face_min,
        str(shifted_max - shifted_min),
    )
    check(
        "SHIFTED-C04-WITHIN-ASSET-Z",
        shifted_min >= 0 and shifted_max <= 170,
        [str(shifted_min), str(shifted_max)],
    )

    construction = amendment["construction_rule"]
    check("FRESH-ONLY", construction["fresh_only"] is True, construction["fresh_only"])
    check(
        "ONE-POSITIVE-X-HALF",
        construction["one_positive_x_half"] is True,
        construction["one_positive_x_half"],
    )
    check("MIRROR-PLANE-X0", construction["mirror_plane"] == "X=0", construction["mirror_plane"])
    check(
        "MIRROR-TRANSFORM",
        construction["mirror_transform"] == "(X,Y,Z)->(-X,Y,Z)",
        construction["mirror_transform"],
    )
    check(
        "RZ180-FORBIDDEN",
        construction["whole_asset_rz180_count"] == 0,
        construction["whole_asset_rz180_count"],
    )
    check("ONE-MIRROR", construction["mirror_count"] == 1, construction["mirror_count"])
    check(
        "CENTER-SEAM-WELD",
        construction["center_seam_join_and_weld_required"] is True,
        construction["center_seam_join_and_weld_required"],
    )
    check(
        "INTEGRATED-END-FACE",
        construction["strike_end_face_integrated_into_head_solid"] is True,
        construction["strike_end_face_integrated_into_head_solid"],
    )
    check(
        "NO-FLOATING-END-PANEL",
        construction["separate_floating_or_hanging_end_panel_allowed"] is False,
        construction["separate_floating_or_hanging_end_panel_allowed"],
    )
    check(
        "SHARED-XYZ",
        construction["shared_dimensions_xyz_cm_exact"]
        == ["50719500/517681", "6644212/149985", "170/1"],
        construction["shared_dimensions_xyz_cm_exact"],
    )

    gates = amendment["mandatory_pre_save_and_independent_saved_file_gates"]
    for key in (
        "open_boundary_edges",
        "edge_incidence_greater_than_two",
        "winding_mismatch_edges",
        "loose_edges",
        "zero_area_faces",
        "duplicate_faces",
        "center_seam_unwelded_vertices",
    ):
        check(f"ZERO-GATE-{key.upper()}", gates[key] == 0, gates[key])
    check(
        "SOURCE-HASH-GATE",
        gates["source_hashes_unchanged"] is True,
        gates["source_hashes_unchanged"],
    )
    check(
        "CONTACT-GATE",
        gates["declared_contacts"] == "PASS",
        gates["declared_contacts"],
    )
    check(
        "NEGATIVE-SPACE-GATE",
        gates["protected_negative_spaces"] == "PASS",
        gates["protected_negative_spaces"],
    )

    exclusions = amendment["explicit_exclusions"]
    for required in (
        "modify or resave either failed source",
        "read geometry from either failed source",
        "repair forward the failed surface-patch assembly",
        "use whole-asset Rz180",
        "Unreal work",
        "Step 14 advancement",
    ):
        check(f"EXCLUSION-{required.upper().replace(' ', '-')}", required in exclusions, required)

    check(
        "PRIOR-STATE-WAITING-FEEDBACK",
        step_state["state"]
        == "step_13_technical_fail_diagnostic_render_complete_waiting_feedback",
        step_state["state"],
    )
    check(
        "PRIOR-PRODUCTION-AUTHORITY-FALSE",
        step_state["production_authority"] is False,
        step_state["production_authority"],
    )

    failures = [item for item in checks if item["result"] != "PASS"]
    result = "PASS" if not failures else "FAIL"
    output = {
        "schema": "AERATHEA_TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_RECOVERY_A01_VALIDATION_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "recovery_id": RECOVERY_ID,
        "artifact_status": f"proof only; {result}",
        "result": result,
        "amendment": {
            "path": relative(AMENDMENT),
            "sha256": sha256(AMENDMENT),
        },
        "checks_passed": len(checks) - len(failures),
        "checks_failed": len(failures),
        "checks": checks,
        "assumptions": [],
        "geometry_created": False,
        "blender_opened": False,
        "failed_sources_modified": False,
        "next_gate": (
            "record the approved fresh-build execution boundary"
            if result == "PASS"
            else "stop and correct the amendment"
        ),
    }
    VALIDATION.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "result": result,
                "checks_passed": output["checks_passed"],
                "checks_failed": output["checks_failed"],
                "validation": relative(VALIDATION),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
