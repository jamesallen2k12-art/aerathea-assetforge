#!/usr/bin/env python3
"""Independent Step 12 authority, correction, and saved-candidate audit.

This tool intentionally does not import the Step 12 builder and does not read
expected geometry claims from a builder output.  Its preflight mode derives
the expected world orientation directly from the hash-locked Step 11
blueprint, source ownership scanlines, view equations, and the exact additive
Flamestrike-approved amendments.
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
DEFAULT_PARITY_AMENDMENT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/"
    "STEP_11C_BOTTOM_C02_C03_LABEL_CORRECTION_A01.md"
)
VALIDATION_PATH = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/"
    "STEP_11C_BOTTOM_C02_C03_LABEL_CORRECTION_A01_VALIDATION.json"
)

EXPECTED = {
    "blueprint": "2b598497ba5e61a4352c217f3fb20b3545189c710934f3a21d9b7398ddb472c7",
    "amendment": "2e4276ea0adc32d8c6a21fb5bfbd46eacf627a9708c6187e56be1556eee76ba6",
    "parity_amendment": (
        "45cc92d07f90fdb1bb104c8ede5e9fb6e6161454ea91d0923dc6f81cf02512d1"
    ),
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


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


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
    parity_amendment_path: Path,
    blueprint: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Path]]:
    checks: list[dict[str, Any]] = []

    direct = (
        ("blueprint", blueprint_path, EXPECTED["blueprint"]),
        ("amendment", amendment_path, EXPECTED["amendment"]),
        (
            "parity_amendment",
            parity_amendment_path,
            EXPECTED["parity_amendment"],
        ),
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
    bottom_owner_names: dict[str, str] | None = None,
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
    effective_bottom_owner_names = bottom_owner_names or owner_names
    observed: dict[str, dict[str, dict[str, Any]]] = {}
    checks: list[dict[str, Any]] = []

    for component_id, owner_name in owner_names.items():
        observed[component_id] = {}
        for view, mapper in mapping.items():
            source_owner_name = (
                effective_bottom_owner_names[component_id]
                if view == "bottom"
                else owner_name
            )
            record = bounds_for_rows(
                owner_rows(scanlines, view, source_owner_name),
                mapper,
            )
            record["stored_source_owner"] = source_owner_name
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


def parity_amendment_semantic_checks(
    parity_amendment_text: str,
) -> list[dict[str, Any]]:
    normalized_text = " ".join(parity_amendment_text.split())
    required_clauses = {
        "label_only": (
            "corrects the two reversed bottom-view C02/C03 semantic labels only"
        ),
        "coordinate_system_unchanged": "Coordinate-system change: `none`",
        "source_pixels_unchanged": "Source-pixel change: `none`",
        "measurement_unchanged": "Measurement change: `none`",
        "bottom_equation_preserved": "X=(1529/2-x)*52020/517681",
        "logical_c02_uses_stored_c03": (
            "logical evidence reference `OWN_BOTTOM_C02` must therefore "
            "resolve to the exact stored payload and canonical row set of "
            "`OWN_BOTTOM_C03`"
        ),
        "logical_c03_uses_stored_c02": (
            "logical evidence reference `OWN_BOTTOM_C03` must therefore "
            "resolve to the exact stored payload and canonical row set of "
            "`OWN_BOTTOM_C02`"
        ),
        "c02_boundary_payload_swap": (
            "logical boundary reference `BOTTOM_C02_INNER_OWNER_EDGE` must "
            "resolve to the exact stored ordered boundary payload of "
            "`BOTTOM_C03_INNER_OWNER_EDGE`"
        ),
        "c03_boundary_payload_swap": (
            "logical boundary reference `BOTTOM_C03_INNER_OWNER_EDGE` must "
            "resolve to the exact stored ordered boundary payload of "
            "`BOTTOM_C02_INNER_OWNER_EDGE`"
        ),
        "step13_locked": "Step 13 authority: `false`",
        "unreal_locked": "Unreal authority: `false`",
    }
    return [
        {
            "id": f"PARITY-AMENDMENT-{key}",
            "required_clause": clause,
            "result": "pass" if clause in normalized_text else "fail",
        }
        for key, clause in required_clauses.items()
    ]


def correction_payload_checks(
    blueprint: dict[str, Any],
    scanlines: dict[str, Any],
    boundaries: dict[str, Any],
) -> list[dict[str, Any]]:
    evidence = blueprint["evidence_catalog"]
    stored_c02_rows = owner_rows(scanlines, "bottom", "C02_STONE_LEFT")
    stored_c03_rows = owner_rows(scanlines, "bottom", "C03_STONE_RIGHT")
    stored_c02_boundary = boundaries["boundaries"][
        "BOTTOM_C02_INNER_OWNER_EDGE"
    ]
    stored_c03_boundary = boundaries["boundaries"][
        "BOTTOM_C03_INNER_OWNER_EDGE"
    ]

    payloads = {
        "stored_bottom_c02_rows": {
            "observed": canonical_sha256(stored_c02_rows),
            "expected": evidence["OWN_BOTTOM_C02"]["rows_canonical_sha256"],
        },
        "stored_bottom_c03_rows": {
            "observed": canonical_sha256(stored_c03_rows),
            "expected": evidence["OWN_BOTTOM_C03"]["rows_canonical_sha256"],
        },
        "stored_bottom_c02_boundary": {
            "observed": canonical_sha256(stored_c02_boundary),
            "expected": evidence["BOTTOM_C02_INNER_OWNER_EDGE"][
                "record_canonical_sha256"
            ],
        },
        "stored_bottom_c03_boundary": {
            "observed": canonical_sha256(stored_c03_boundary),
            "expected": evidence["BOTTOM_C03_INNER_OWNER_EDGE"][
                "record_canonical_sha256"
            ],
        },
    }
    checks = [
        {
            "id": f"PAYLOAD-{payload_id.upper()}",
            "name": f"{payload_id} remains byte-canonically unchanged",
            "observed_sha256": record["observed"],
            "expected_sha256": record["expected"],
            "result": (
                "pass"
                if record["observed"] == record["expected"]
                else "fail"
            ),
        }
        for payload_id, record in payloads.items()
    ]

    checks.extend(
        [
            {
                "id": "PAYLOAD-CORRECTED-LOGICAL-C02",
                "name": (
                    "logical bottom C02 resolves to the complete stored C03 "
                    "owner and boundary payloads"
                ),
                "owner_source": "OWN_BOTTOM_C03",
                "owner_rows_canonical_sha256": canonical_sha256(
                    stored_c03_rows
                ),
                "boundary_source": "BOTTOM_C03_INNER_OWNER_EDGE",
                "boundary_record_canonical_sha256": canonical_sha256(
                    stored_c03_boundary
                ),
                "result": (
                    "pass"
                    if canonical_sha256(stored_c03_rows)
                    == evidence["OWN_BOTTOM_C03"]["rows_canonical_sha256"]
                    and canonical_sha256(stored_c03_boundary)
                    == evidence["BOTTOM_C03_INNER_OWNER_EDGE"][
                        "record_canonical_sha256"
                    ]
                    else "fail"
                ),
            },
            {
                "id": "PAYLOAD-CORRECTED-LOGICAL-C03",
                "name": (
                    "logical bottom C03 resolves to the complete stored C02 "
                    "owner and boundary payloads"
                ),
                "owner_source": "OWN_BOTTOM_C02",
                "owner_rows_canonical_sha256": canonical_sha256(
                    stored_c02_rows
                ),
                "boundary_source": "BOTTOM_C02_INNER_OWNER_EDGE",
                "boundary_record_canonical_sha256": canonical_sha256(
                    stored_c02_boundary
                ),
                "result": (
                    "pass"
                    if canonical_sha256(stored_c02_rows)
                    == evidence["OWN_BOTTOM_C02"]["rows_canonical_sha256"]
                    and canonical_sha256(stored_c02_boundary)
                    == evidence["BOTTOM_C02_INNER_OWNER_EDGE"][
                        "record_canonical_sha256"
                    ]
                    else "fail"
                ),
            },
        ]
    )
    return checks


def closure_constructibility_checks(
    blueprint: dict[str, Any],
) -> list[dict[str, Any]]:
    instructions = {
        record["id"]: record
        for record in blueprint["closure_and_contact_instructions"]
    }
    equation = blueprint["equation_catalog"]["EQ_ORDERED_RULED_FACE"][
        "formula"
    ]
    checks: list[dict[str, Any]] = []
    for closure_id in ("CLOSURE_C02_INNER", "CLOSURE_C03_INNER"):
        instruction = instructions[closure_id]
        boundary_refs = [
            ref
            for ref in instruction["source_ownership_refs"]
            if ref.startswith(("FRONT_", "TOP_", "BOTTOM_"))
        ]
        explicit_pairings = instruction.get("explicit_pairings")
        if explicit_pairings is None:
            explicit_pairings = instruction.get("pairings")
        checks.append(
            {
                "id": f"CONSTRUCTIBILITY-{closure_id}",
                "name": (
                    f"{closure_id} defines the exact ordered boundary pairs "
                    "consumed by its binary ruled-face equation"
                ),
                "method": instruction["method"],
                "boundary_refs": boundary_refs,
                "boundary_ref_count": len(boundary_refs),
                "ruled_face_formula": equation,
                "formula_arity": 2,
                "explicit_pairings": explicit_pairings,
                "risk_if_inferred": (
                    "An inferred pairing can create a non-manifold duplicate "
                    "wall, omit an owner boundary, or close a protected gap."
                ),
                "result": (
                    "pass"
                    if explicit_pairings is not None
                    and len(explicit_pairings) > 0
                    else "fail"
                ),
            }
        )
    return checks


def build_validation(
    blueprint_path: Path,
    amendment_path: Path,
    parity_amendment_path: Path,
) -> dict[str, Any]:
    blueprint = load_json(blueprint_path)
    amendment_text = amendment_path.read_text(encoding="utf-8")
    parity_amendment_text = parity_amendment_path.read_text(encoding="utf-8")
    authority_checks, authority_paths = verify_authority(
        blueprint_path,
        amendment_path,
        parity_amendment_path,
        blueprint,
    )
    amendment_checks = amendment_semantic_checks(amendment_text)
    parity_amendment_checks = parity_amendment_semantic_checks(
        parity_amendment_text
    )

    scanlines = load_gzip_json(authority_paths["step09a_scanlines"])
    boundaries = load_json(authority_paths["step09a_boundaries"])
    payload_checks = correction_payload_checks(
        blueprint,
        scanlines,
        boundaries,
    )
    constructibility_checks = closure_constructibility_checks(blueprint)
    raw_orientation, raw_orientation_checks = component_orientation_audit(
        blueprint,
        scanlines,
    )
    corrected_bottom_owners = {
        "C02": "C03_STONE_RIGHT",
        "C03": "C02_STONE_LEFT",
    }
    corrected_orientation, corrected_orientation_checks = (
        component_orientation_audit(
            blueprint,
            scanlines,
            bottom_owner_names=corrected_bottom_owners,
        )
    )

    raw_conflict_confirmed = (
        raw_orientation["C02"]["front"]["sign_class"] == "negative_x"
        and raw_orientation["C02"]["top"]["sign_class"] == "negative_x"
        and raw_orientation["C02"]["bottom"]["sign_class"] == "positive_x"
        and raw_orientation["C03"]["front"]["sign_class"] == "positive_x"
        and raw_orientation["C03"]["top"]["sign_class"] == "positive_x"
        and raw_orientation["C03"]["bottom"]["sign_class"] == "negative_x"
    )
    raw_conflict_check = {
        "id": "PARITY-RAW-MISLABEL-EVIDENCE",
        "name": (
            "the stored bottom C02/C03 semantic identities are exactly "
            "reversed relative to front and top"
        ),
        "expected": {
            "C02": {
                "front": "negative_x",
                "top": "negative_x",
                "bottom": "positive_x",
            },
            "C03": {
                "front": "positive_x",
                "top": "positive_x",
                "bottom": "negative_x",
            },
        },
        "result": "pass" if raw_conflict_confirmed else "fail",
    }

    authority_failures = [
        check for check in authority_checks if check["result"] != "pass"
    ]
    amendment_failures = [
        check for check in amendment_checks if check["result"] != "pass"
    ]
    parity_amendment_failures = [
        check
        for check in parity_amendment_checks
        if check["result"] != "pass"
    ]
    payload_failures = [
        check for check in payload_checks if check["result"] != "pass"
    ]
    corrected_orientation_failures = [
        check
        for check in corrected_orientation_checks
        if check["result"] != "pass"
    ]
    constructibility_failures = [
        check
        for check in constructibility_checks
        if check["result"] != "pass"
    ]

    correction_result = (
        "PASS"
        if not authority_failures
        and not amendment_failures
        and not parity_amendment_failures
        and not payload_failures
        and not corrected_orientation_failures
        and raw_conflict_confirmed
        else "FAIL"
    )
    step12_result = (
        "BLOCKED"
        if correction_result == "PASS" and constructibility_failures
        else "PASS"
        if correction_result == "PASS"
        else "LOCKED"
    )

    return {
        "schema": (
            "AERATHEA_STEP11C_BOTTOM_C02_C03_LABEL_CORRECTION_"
            "A01_VALIDATION_V1"
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
                "hash-locked Step 09A ordered boundary records",
                "hash-locked pixel/world equations",
                "asset-specific Flamestrike high-poly/Nanite amendment",
                "Flamestrike-approved bottom C02/C03 label correction",
            ],
            "python": platform.python_version(),
        },
        "internal_failures": [],
        "correction_validation": {
            "result": correction_result,
            "high_poly_amendment_path": relative(amendment_path),
            "high_poly_amendment_sha256": sha256(amendment_path),
            "parity_amendment_path": relative(parity_amendment_path),
            "parity_amendment_sha256": sha256(parity_amendment_path),
            "authority_checks_passed": len(authority_checks)
            - len(authority_failures),
            "authority_checks_failed": len(authority_failures),
            "semantic_checks_passed": (
                len(amendment_checks)
                + len(parity_amendment_checks)
                - len(amendment_failures)
                - len(parity_amendment_failures)
            ),
            "semantic_checks_failed": (
                len(amendment_failures) + len(parity_amendment_failures)
            ),
            "payload_checks_passed": len(payload_checks)
            - len(payload_failures),
            "payload_checks_failed": len(payload_failures),
            "checks": (
                authority_checks
                + amendment_checks
                + parity_amendment_checks
                + payload_checks
                + [raw_conflict_check]
            ),
        },
        "source_conflict_preserved_as_evidence": {
            "result": "PASS" if raw_conflict_confirmed else "FAIL",
            "world_x_owner_bounds": raw_orientation,
            "diagnostic_checks": raw_orientation_checks,
            "interpretation": (
                "The stored source records remain unchanged. Their raw names "
                "demonstrate the approved C02/C03 bottom-view mislabel."
            ),
        },
        "step12_resume_preflight": {
            "result": step12_result,
            "block_code": (
                None
                if step12_result == "PASS"
                else (
                    "Blueprint block: rule missing — three-boundary stone "
                    "closure construction"
                    if step12_result == "BLOCKED"
                    else (
                        "Blueprint block: approved bottom-view C02/C03 label "
                        "correction failed independent validation"
                    )
                )
            ),
            "corrected_world_x_owner_bounds": corrected_orientation,
            "checks": corrected_orientation_checks,
            "passed": (
                len(corrected_orientation_checks)
                - len(corrected_orientation_failures)
            ),
            "failed": len(corrected_orientation_failures),
            "total": len(corrected_orientation_checks),
        },
        "closure_constructibility_preflight": {
            "result": (
                "PASS" if not constructibility_failures else "BLOCKED"
            ),
            "checks": constructibility_checks,
            "passed": len(constructibility_checks)
            - len(constructibility_failures),
            "failed": len(constructibility_failures),
            "total": len(constructibility_checks),
            "missing_authority": (
                "Each stone closure cites ordered front, top, and bottom "
                "boundary sets, while EQ_ORDERED_RULED_FACE consumes only "
                "A(s) and B(s). The blueprint supplies no explicit pairing "
                "graph or three-boundary surface rule."
            ),
        },
        "closed_world_decision": {
            "bottom_x_equation": "X=(1529/2-x)*52020/517681",
            "coordinate_flip_applied": False,
            "source_pixels_changed": False,
            "stored_evidence_changed": False,
            "approved_semantic_resolution": {
                "logical_OWN_BOTTOM_C02": "stored OWN_BOTTOM_C03 payload",
                "logical_OWN_BOTTOM_C03": "stored OWN_BOTTOM_C02 payload",
                "logical_BOTTOM_C02_INNER_OWNER_EDGE": (
                    "stored BOTTOM_C03_INNER_OWNER_EDGE payload"
                ),
                "logical_BOTTOM_C03_INNER_OWNER_EDGE": (
                    "stored BOTTOM_C02_INNER_OWNER_EDGE payload"
                ),
            },
            "builder_creation_allowed": step12_result == "PASS",
            "blender_production_allowed_after_required_checkpoint": (
                step12_result == "PASS"
            ),
            "geometry_created": False,
        },
        "next_authorized_action": {
            "action": (
                "Obtain an additive, exact stone-closure construction rule "
                "that identifies which measured boundaries are paired and "
                "how protected runs remain open without producing an "
                "unwatertight or non-manifold shell."
                if step12_result == "BLOCKED"
                else (
                    "Create the required recovery checkpoint, then implement "
                    "and run the already-approved Step 12 dual-variant "
                    "high-poly build."
                )
            ),
            "step13_authorized": False,
            "unreal_authorized": False,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blueprint", type=Path, default=DEFAULT_BLUEPRINT)
    parser.add_argument("--amendment", type=Path, default=DEFAULT_AMENDMENT)
    parser.add_argument(
        "--parity-amendment",
        type=Path,
        default=DEFAULT_PARITY_AMENDMENT,
    )
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
    parity_amendment_path = args.parity_amendment.resolve()
    result = build_validation(
        blueprint_path,
        amendment_path,
        parity_amendment_path,
    )
    output = args.validation_output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "validation": relative(output),
        "correction_result": result["correction_validation"]["result"],
        "step12_result": result["step12_resume_preflight"]["result"],
        "block_code": result["step12_resume_preflight"]["block_code"],
    }, sort_keys=True))
    return 0 if result["step12_resume_preflight"]["result"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
