#!/usr/bin/env python3
"""Independent Step 12 authority and cross-view pregeometry audit.

This tool intentionally does not import the Step 12 builder and does not read
expected geometry claims from a builder output.  Its preflight mode derives
the expected world orientation directly from the hash-locked Step 11
blueprint, source ownership scanlines, and view equations.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BLUEPRINT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/"
    "STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json"
)
DEFAULT_AMENDMENT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/"
    "STEP_11B_HIGH_POLY_NANITE_PERFORMANCE_AMENDMENT_A01.md"
)
VALIDATION_PATH = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/"
    "STEP_11B_HIGH_POLY_NANITE_PERFORMANCE_AMENDMENT_A01_VALIDATION.json"
)

EXPECTED = {
    "blueprint": "2b598497ba5e61a4352c217f3fb20b3545189c710934f3a21d9b7398ddb472c7",
    "amendment": "2e4276ea0adc32d8c6a21fb5bfbd46eacf627a9708c6187e56be1556eee76ba6",
    "step11_authority_lock": (
        "3235fcc9480ad246f968b275792aa3a309aa34710b5bfec3fc005980ae3d5069"
    ),
    "step12_contract": (
        "a3f16266da53ed28a0c849818271dea0c07cd8ba8005e05a6778e2a0f6d2935b"
    ),
    "step12_approval": (
        "2b6fedd15020808beb63ff556c66bc52114a06cd69331f72bfe637caea69e7d7"
    ),
}

AUTHORITY_LOCK_PATH = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/"
    "STEP_11_PRODUCTION_BLUEPRINT_A02_AUTHORITY_LOCK.json"
)
STEP12_CONTRACT_PATH = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/"
    "STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_PROPOSED_CONTRACT.md"
)
STEP12_APPROVAL_PATH = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/"
    "STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_APPROVAL_RECORD.md"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_gzip_json(path: Path) -> dict[str, Any]:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def exact(record: dict[str, Any]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def resolve_authority_paths(
    blueprint: dict[str, Any],
) -> dict[str, Path]:
    return {
        key: ROOT / record["path"]
        for key, record in blueprint["authority_files"].items()
    }


def verify_authority(
    blueprint_path: Path,
    amendment_path: Path,
    blueprint: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Path]]:
    checks: list[dict[str, Any]] = []

    direct = (
        ("blueprint", blueprint_path, EXPECTED["blueprint"]),
        ("amendment", amendment_path, EXPECTED["amendment"]),
        (
            "step11_authority_lock",
            AUTHORITY_LOCK_PATH,
            EXPECTED["step11_authority_lock"],
        ),
        ("step12_contract", STEP12_CONTRACT_PATH, EXPECTED["step12_contract"]),
        ("step12_approval", STEP12_APPROVAL_PATH, EXPECTED["step12_approval"]),
    )
    for check_id, path, expected_hash in direct:
        observed = sha256(path) if path.is_file() else None
        checks.append(
            {
                "id": f"AUTH-{check_id}",
                "path": relative(path),
                "expected_sha256": expected_hash,
                "observed_sha256": observed,
                "result": "pass" if observed == expected_hash else "fail",
            }
        )

    paths = resolve_authority_paths(blueprint)
    for key, record in sorted(blueprint["authority_files"].items()):
        path = paths[key]
        observed = sha256(path) if path.is_file() else None
        expected_hash = record["sha256"]
        checks.append(
            {
                "id": f"AUTH-CATALOG-{key}",
                "path": relative(path),
                "expected_sha256": expected_hash,
                "observed_sha256": observed,
                "result": "pass" if observed == expected_hash else "fail",
            }
        )
    return checks, paths


def owner_rows(
    scanlines: dict[str, Any], view: str, component: str
) -> list[dict[str, Any]]:
    return scanlines["views"][view]["component_owners"][component]["rows"]


def all_run_edges(rows: Iterable[dict[str, Any]]) -> Iterable[int]:
    for row in rows:
        for start, stop in row["owner_runs_half_open"]:
            yield int(start)
            yield int(stop)


def front_x(source_x: int) -> Fraction:
    return Fraction((source_x - 562) * 170, 1063)


def top_x(source_x: int) -> Fraction:
    return (Fraction(source_x) - Fraction(1533, 2)) * Fraction(52020, 517681)


def bottom_x(source_x: int) -> Fraction:
    return (Fraction(1529, 2) - Fraction(source_x)) * Fraction(52020, 517681)


def bounds_for_rows(
    rows: list[dict[str, Any]],
    mapper: Any,
) -> dict[str, Any]:
    values = [mapper(edge) for edge in all_run_edges(rows)]
    minimum = min(values)
    maximum = max(values)
    return {
        "minimum_cm_exact": f"{minimum.numerator}/{minimum.denominator}",
        "maximum_cm_exact": f"{maximum.numerator}/{maximum.denominator}",
        "minimum_cm": f"{float(minimum):.12f}",
        "maximum_cm": f"{float(maximum):.12f}",
        "sign_class": (
            "negative_x"
            if maximum < 0
            else "positive_x"
            if minimum > 0
            else "crosses_x0"
        ),
        "_minimum": minimum,
        "_maximum": maximum,
    }


def serializable_bounds(record: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in record.items() if not key.startswith("_")}


def component_orientation_audit(
    blueprint: dict[str, Any],
    scanlines: dict[str, Any],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    mapping = {
        "front": front_x,
        "top": top_x,
        "bottom": bottom_x,
    }
    owner_names = {
        "C02": "C02_STONE_LEFT",
        "C03": "C03_STONE_RIGHT",
    }
    observed: dict[str, dict[str, dict[str, Any]]] = {}
    checks: list[dict[str, Any]] = []

    for component_id, owner_name in owner_names.items():
        observed[component_id] = {}
        for view, mapper in mapping.items():
            record = bounds_for_rows(
                owner_rows(scanlines, view, owner_name),
                mapper,
            )
            observed[component_id][view] = record

        front_sign = observed[component_id]["front"]["sign_class"]
        top_sign = observed[component_id]["top"]["sign_class"]
        bottom_sign = observed[component_id]["bottom"]["sign_class"]
        checks.append(
            {
                "id": f"PARITY-{component_id}-FRONT-TOP",
                "name": (
                    f"{component_id} front and top owners resolve to the same "
                    "world-X side"
                ),
                "observed": {"front": front_sign, "top": top_sign},
                "result": "pass" if front_sign == top_sign else "fail",
            }
        )
        checks.append(
            {
                "id": f"PARITY-{component_id}-BOTTOM",
                "name": (
                    f"{component_id} bottom owner resolves to the same world-X "
                    "side as its front/top owners"
                ),
                "observed": {
                    "front": front_sign,
                    "top": top_sign,
                    "bottom": bottom_sign,
                },
                "result": "pass" if bottom_sign == front_sign == top_sign else "fail",
            }
        )

    half_width = exact(
        blueprint["measurement_catalog"]["MEAS_FRONT_WIDTH"]["half_value_cm"]
    )
    bottom_c03_max = observed["C03"]["bottom"]["_maximum"]
    c03_to_positive_strike_gap = half_width - bottom_c03_max
    checks.append(
        {
            "id": "PARITY-C03-BOTTOM-TO-C04-POSITIVE-X",
            "name": (
                "the named bottom C03 owner can meet the positive-X C04 strike "
                "face without crossing X=0"
            ),
            "authority_instruction": (
                "CLOSURE_C03_TO_C04_RUNE / CLOSURE_C03_TO_C04_METAL"
            ),
            "positive_x_strike_plane_cm_exact": (
                f"{half_width.numerator}/{half_width.denominator}"
            ),
            "bottom_c03_maximum_x_cm_exact": (
                f"{bottom_c03_max.numerator}/{bottom_c03_max.denominator}"
            ),
            "minimum_x_separation_cm_exact": (
                f"{c03_to_positive_strike_gap.numerator}/"
                f"{c03_to_positive_strike_gap.denominator}"
            ),
            "minimum_x_separation_cm": f"{float(c03_to_positive_strike_gap):.12f}",
            "crosses_x0": bottom_c03_max < 0 < half_width,
            "result": "fail" if bottom_c03_max < 0 < half_width else "pass",
        }
    )

    bottom_c02_min = observed["C02"]["bottom"]["_minimum"]
    checks.append(
        {
            "id": "PARITY-BOTTOM-SEMANTIC-SWAP-EVIDENCE",
            "name": (
                "bottom owner signs are the exact opposite of their named "
                "front/top components"
            ),
            "observed": {
                "C02_bottom_minimum_x_cm": f"{float(bottom_c02_min):.12f}",
                "C02_bottom_sign": observed["C02"]["bottom"]["sign_class"],
                "C03_bottom_maximum_x_cm": f"{float(bottom_c03_max):.12f}",
                "C03_bottom_sign": observed["C03"]["bottom"]["sign_class"],
            },
            "result": (
                "fail"
                if observed["C02"]["bottom"]["sign_class"] == "positive_x"
                and observed["C03"]["bottom"]["sign_class"] == "negative_x"
                else "pass"
            ),
        }
    )

    public_observed = {
        component: {
            view: serializable_bounds(bounds)
            for view, bounds in views.items()
        }
        for component, views in observed.items()
    }
    return public_observed, checks


def amendment_semantic_checks(amendment_text: str) -> list[dict[str, Any]]:
    normalized_text = " ".join(amendment_text.split())
    required_clauses = {
        "high_poly_stage": (
            "Step 12 is a high-poly source reconstruction stage"
        ),
        "nanite_target": "Nanite-capable Unreal Engine 5 target",
        "target_superseded": (
            "the Step 11 `8,000`-triangle target is superseded"
        ),
        "cap_superseded": (
            "the Step 11 `10,000`-triangle hard cap is superseded"
        ),
        "angular_divisions_preserved": (
            "retain exactly `64` positive-X angular divisions"
        ),
        "step13_locked": "Step 13 authority: `false`",
        "unreal_locked": "Unreal authority: `false`",
    }
    return [
        {
            "id": f"AMENDMENT-{key}",
            "required_clause": clause,
            "result": "pass" if clause in normalized_text else "fail",
        }
        for key, clause in required_clauses.items()
    ]


def build_validation(
    blueprint_path: Path,
    amendment_path: Path,
) -> dict[str, Any]:
    blueprint = load_json(blueprint_path)
    amendment_text = amendment_path.read_text(encoding="utf-8")
    authority_checks, authority_paths = verify_authority(
        blueprint_path,
        amendment_path,
        blueprint,
    )
    amendment_checks = amendment_semantic_checks(amendment_text)

    scanlines = load_gzip_json(authority_paths["step09a_scanlines"])
    orientation, orientation_checks = component_orientation_audit(
        blueprint,
        scanlines,
    )

    authority_failures = [
        check for check in authority_checks if check["result"] != "pass"
    ]
    amendment_failures = [
        check for check in amendment_checks if check["result"] != "pass"
    ]
    orientation_failures = [
        check for check in orientation_checks if check["result"] != "pass"
    ]

    amendment_result = (
        "PASS" if not authority_failures and not amendment_failures else "FAIL"
    )
    step12_result = (
        "BLOCKED"
        if amendment_result == "PASS" and orientation_failures
        else "PASS"
        if amendment_result == "PASS"
        else "LOCKED"
    )

    return {
        "schema": (
            "AERATHEA_STEP11B_HIGH_POLY_NANITE_PERFORMANCE_"
            "AMENDMENT_A01_VALIDATION_V1"
        ),
        "asset": "SM_DRW_SiegeBreaker_Hammer_A01",
        "run_id": "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02",
        "date": datetime.now(timezone.utc).isoformat(),
        "artifact_status": "proof only",
        "audit_independence": {
            "builder_imported": False,
            "builder_created": False,
            "builder_claims_trusted": False,
            "blender_started": False,
            "geometry_created": False,
            "expected_values_read_from": [
                "hash-locked Step 11 blueprint",
                "hash-locked Step 09A component scanlines",
                "hash-locked pixel/world equations",
                "asset-specific Flamestrike high-poly/Nanite amendment",
            ],
            "python": platform.python_version(),
        },
        "internal_failures": [
            {
                "id": "S11B-AUDIT-A01-IF01",
                "status": "resolved before authoritative result",
                "issue": (
                    "The first validator attempt compared one required clause "
                    "against literal line-wrapped Markdown and returned a false "
                    "negative for the Nanite-target clause."
                ),
                "correction": (
                    "Whitespace is normalized before semantic clause checks; "
                    "no authority file, source evidence, or geometry changed."
                ),
                "production_impact": "none; Blender and geometry were never started",
            }
        ],
        "amendment_validation": {
            "result": amendment_result,
            "amendment_path": relative(amendment_path),
            "amendment_sha256": sha256(amendment_path),
            "authority_checks_passed": len(authority_checks)
            - len(authority_failures),
            "authority_checks_failed": len(authority_failures),
            "semantic_checks_passed": len(amendment_checks)
            - len(amendment_failures),
            "semantic_checks_failed": len(amendment_failures),
            "checks": authority_checks + amendment_checks,
        },
        "step12_resume_preflight": {
            "result": step12_result,
            "block_code": (
                "Blueprint block: source authority conflicting — "
                "bottom-view C02/C03 world-ownership parity"
                if step12_result == "BLOCKED"
                else None
            ),
            "world_x_owner_bounds": orientation,
            "checks": orientation_checks,
            "passed": len(orientation_checks) - len(orientation_failures),
            "failed": len(orientation_failures),
            "total": len(orientation_checks),
        },
        "closed_world_decision": {
            "bottom_x_equation": "X=(1529/2-x)*52020/517681",
            "observed_conflict": (
                "C02 is negative-X in front/top but positive-X in bottom; "
                "C03 is positive-X in front/top but negative-X in bottom. "
                "The Step 11 closure still names bottom C03 as an input to "
                "the positive-X C04 strike-face closure."
            ),
            "silent_owner_swap_allowed": False,
            "silent_bottom_equation_change_allowed": False,
            "builder_creation_allowed_after_block": False,
            "blender_production_allowed_after_block": False,
            "geometry_created": False,
        },
        "required_next_authority": {
            "smallest_candidate_rule": (
                "Approve a bottom-view semantic parity amendment that leaves "
                "all source pixels and equations unchanged but maps "
                "OWN_BOTTOM_C02 to world C03 and OWN_BOTTOM_C03 to world C02, "
                "including their ordered boundary IDs, for construction and "
                "closure correspondence."
            ),
            "alternative": (
                "Approve a different explicit bottom-view world-orientation "
                "rule. Codex may not choose between these options."
            ),
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blueprint", type=Path, default=DEFAULT_BLUEPRINT)
    parser.add_argument("--amendment", type=Path, default=DEFAULT_AMENDMENT)
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument(
        "--validation-output",
        type=Path,
        default=VALIDATION_PATH,
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.preflight_only:
        raise SystemExit(
            "Only --preflight-only is authorized before a saved candidate exists"
        )
    blueprint_path = args.blueprint.resolve()
    amendment_path = args.amendment.resolve()
    result = build_validation(blueprint_path, amendment_path)
    output = args.validation_output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "validation": relative(output),
        "amendment_result": result["amendment_validation"]["result"],
        "step12_result": result["step12_resume_preflight"]["result"],
        "block_code": result["step12_resume_preflight"]["block_code"],
    }, sort_keys=True))
    return 0 if result["step12_resume_preflight"]["result"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
