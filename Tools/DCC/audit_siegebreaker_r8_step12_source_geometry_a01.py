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
import math
import platform
import sys
from collections import Counter, defaultdict
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
DEFAULT_STITCH_AMENDMENT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/"
    "STEP_11D_THREE_BOUNDARY_STONE_STITCH_AMENDMENT_A01.md"
)
VALIDATION_PATH = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/"
    "STEP_11D_THREE_BOUNDARY_STONE_STITCH_AMENDMENT_A01_VALIDATION.json"
)

EXPECTED = {
    "blueprint": "2b598497ba5e61a4352c217f3fb20b3545189c710934f3a21d9b7398ddb472c7",
    "amendment": "2e4276ea0adc32d8c6a21fb5bfbd46eacf627a9708c6187e56be1556eee76ba6",
    "parity_amendment": (
        "45cc92d07f90fdb1bb104c8ede5e9fb6e6161454ea91d0923dc6f81cf02512d1"
    ),
    "stitch_amendment": (
        "850fd42808be667da1d24f1dbccc8ff192ac8b2ccddadb0b714256637849b61a"
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

ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
CANDIDATES = ("rune_side", "metal_center_piece_side")
ANGULAR_DIVISIONS = 64
FRONT_SCALE = Fraction(170, 1063)
AXIAL_SCALE = Fraction(52020, 517681)
RIGHT_SCALE = Fraction(85, 548)
FRONT_AXIS_X = Fraction(562)
FRONT_Z_ORIGIN_Y = Fraction(1271)
TOP_CENTER_X = Fraction(1533, 2)
TOP_CENTER_Y = Fraction(1093, 2)
BOTTOM_CENTER_X = Fraction(1529, 2)
BOTTOM_CENTER_Y = Fraction(539)
RIGHT_AXIS_X = Fraction(557)
RIGHT_Z_ORIGIN_Y = Fraction(1262)

ROTATIONAL_COMPONENTS = {
    "SURF_C06_ROTATIONAL_HALF": (
        "C06_UPPER_HAFT_CAP",
        600,
        670,
    ),
    "SURF_C07_ROTATIONAL_HALF": ("C07_HAFT", 670, 870),
    "SURF_C07B_ROTATIONAL_HALF": (
        "C07B_HAFT_TO_HANDLE_FERRULE",
        870,
        955,
    ),
    "SURF_C08_ROTATIONAL_HALF": ("C08_GRIP", 955, 1110),
    "SURF_C09_ROTATIONAL_HALF": ("C09_LOWER_COLLAR", 1110, 1150),
    "SURF_C10_ROTATIONAL_HALF": ("C10_POMMEL_BODY", 1150, 1220),
    "SURF_C11_ROTATIONAL_HALF": (
        "C11_POMMEL_TERMINAL_CAP",
        1220,
        1271,
    ),
    "SURF_C12_ROTATIONAL_HALF": (
        "C12_UPPER_HEAD_CAP_SPIRE",
        208,
        295,
    ),
}

TRANSITION_TO_INSTRUCTION = {
    "TR_C01_C06": "CONTACT_C01_C06",
    "TR_C06_C07": "CONTACT_C06_C07",
    "TR_C07_C07B": "CONTACT_C07_C07B",
    "TR_C07B_C08": "CONTACT_C07B_C08",
    "TR_C08_C09": "CONTACT_C08_C09",
    "TR_C09_C10": "CONTACT_C09_C10",
    "TR_C10_C11": "CONTACT_C10_C11",
    "TR_C12_C01": "CONTACT_C12_C01",
}


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
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


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
    stitch_amendment_path: Path,
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
            "stitch_amendment",
            stitch_amendment_path,
            EXPECTED["stitch_amendment"],
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


def stitch_amendment_semantic_checks(
    stitch_amendment_text: str,
) -> list[dict[str, Any]]:
    normalized_text = " ".join(stitch_amendment_text.split())
    required_clauses = {
        "closed_completed_perimeter": (
            "For each finished stone, the approved front, top, and "
            "corrected-bottom inner owner edges form one closed perimeter "
            "after the one approved whole-asset `Rz180` completion."
        ),
        "straight_triangles": (
            "Fill that perimeter with deterministic straight triangles"
        ),
        "no_free_vertices": (
            "No free interior point, center point, Steiner point, averaged "
            "point, projected point, smoothed point, resampled point, "
            "tolerance weld, backing plate, or added thickness is permitted."
        ),
        "logical_bottom_c02": (
            "logical `BOTTOM_C02_INNER_OWNER_EDGE` consumes the exact stored "
            "`BOTTOM_C03_INNER_OWNER_EDGE` payload"
        ),
        "logical_bottom_c03": (
            "logical `BOTTOM_C03_INNER_OWNER_EDGE` consumes the exact stored "
            "`BOTTOM_C02_INNER_OWNER_EDGE` payload"
        ),
        "bottom_equation_preserved": "X=(1529/2-x)*52020/517681",
        "one_rz180": "apply the existing whole-asset `Rz180` exactly once",
        "ear_clipping": (
            "run deterministic constrained ear clipping in "
            "counter-clockwise parameter order"
        ),
        "diagonal_choice": (
            "choose the one with the shortest new 3D diagonal by exact "
            "squared length"
        ),
        "no_blender_fill": (
            "No triangle fan center, Blender automatic ngon fill, Delaunay "
            "resampling, beautify pass, remesh, voxelization, shrinkwrap, "
            "solidify, or freehand repair is permitted."
        ),
        "protected_vertex_guard": (
            "Never create a vertex inside a `protected_runs_half_open` "
            "interval."
        ),
        "protected_triangle_guard": (
            "Any triangle entering an approved protected source pixel "
            "invalidates that candidate before its `.blend` file is accepted."
        ),
        "raw_seam_not_welded": (
            "The raw center endpoints are intentionally not "
            "tolerance-welded."
        ),
        "step13_locked": "Step 13 authority: `false`",
        "unreal_locked": "Unreal authority: `false`",
    }
    return [
        {
            "id": f"STITCH-AMENDMENT-{key}",
            "required_clause": clause,
            "result": "pass" if clause in normalized_text else "fail",
        }
        for key, clause in required_clauses.items()
    ]


def boundary_owner_key(boundary_id: str) -> str:
    if "_C02_" in boundary_id:
        return "c02_owner_edge_x"
    if "_C03_" in boundary_id:
        return "c03_owner_edge_x"
    raise KeyError(boundary_id)


def interpolate_owner_x(
    boundary_id: str,
    record: dict[str, Any],
    source_y: Fraction,
) -> tuple[Fraction, list[str]]:
    samples = record["samples"]
    owner_key = boundary_owner_key(boundary_id)
    for sample in samples:
        if Fraction(int(sample["y"])) == source_y:
            return Fraction(int(sample[owner_key])), [sample["mode"]]
    for lower, upper in zip(samples, samples[1:]):
        y0 = Fraction(int(lower["y"]))
        y1 = Fraction(int(upper["y"]))
        if y0 < source_y < y1:
            alpha = (source_y - y0) / (y1 - y0)
            x0 = Fraction(int(lower[owner_key]))
            x1 = Fraction(int(upper[owner_key]))
            return x0 + alpha * (x1 - x0), [
                lower["mode"],
                upper["mode"],
            ]
    raise ValueError(
        f"{boundary_id} does not cover source y={source_y}"
    )


def boundary_record_checks(
    boundaries: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    expected = {
        "FRONT_C02_INNER_OWNER_EDGE": (
            "front",
            "C02_STONE_LEFT",
            "source_y_ascending_world_z_descending",
        ),
        "FRONT_C03_INNER_OWNER_EDGE": (
            "front",
            "C03_STONE_RIGHT",
            "source_y_ascending_world_z_descending",
        ),
        "TOP_C02_INNER_OWNER_EDGE": (
            "top",
            "C02_STONE_LEFT",
            "source_y_ascending",
        ),
        "TOP_C03_INNER_OWNER_EDGE": (
            "top",
            "C03_STONE_RIGHT",
            "source_y_ascending",
        ),
        "BOTTOM_C02_INNER_OWNER_EDGE": (
            "bottom",
            "C02_STONE_LEFT",
            "source_y_ascending",
        ),
        "BOTTOM_C03_INNER_OWNER_EDGE": (
            "bottom",
            "C03_STONE_RIGHT",
            "source_y_ascending",
        ),
    }
    allowed_modes = {"protected_gap", "shared_contact_cut"}
    for boundary_id, (view, owner, order) in expected.items():
        record = boundaries["boundaries"].get(boundary_id)
        samples = record.get("samples", []) if record else []
        observed_modes = (
            sorted({sample.get("mode") for sample in samples})
            if samples
            else []
        )
        source_y = [int(sample["y"]) for sample in samples]
        result = (
            record is not None
            and record.get("view") == view
            and record.get("owner") == owner
            and record.get("order") == order
            and len(samples) >= 2
            and source_y == sorted(source_y)
            and len(source_y) == len(set(source_y))
            and set(observed_modes).issubset(allowed_modes)
        )
        checks.append(
            {
                "id": f"STITCH-BOUNDARY-{boundary_id}",
                "name": (
                    f"{boundary_id} is a nonempty, uniquely ordered exact "
                    "owner-edge polyline with only approved contact modes"
                ),
                "view": record.get("view") if record else None,
                "owner": record.get("owner") if record else None,
                "order": record.get("order") if record else None,
                "sample_count": len(samples),
                "source_y_half_open": (
                    [source_y[0], source_y[-1] + 1] if source_y else None
                ),
                "modes": observed_modes,
                "result": "pass" if result else "fail",
            }
        )

    groups = {
        record["id"]: record
        for record in boundaries["correspondence_groups"]
    }
    for component_id in ("C02", "C03"):
        group_id = (
            f"CORR_{component_id}_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES"
        )
        expected_ids = [
            f"FRONT_{component_id}_INNER_OWNER_EDGE",
            f"TOP_{component_id}_INNER_OWNER_EDGE",
            f"BOTTOM_{component_id}_INNER_OWNER_EDGE",
        ]
        record = groups.get(group_id)
        result = (
            record is not None
            and record.get("ordered_boundary_ids") == expected_ids
            and record.get("scope")
            == "ordered exact source-edge sets only; no point pairing or surface created"
        )
        checks.append(
            {
                "id": f"STITCH-CORRESPONDENCE-{component_id}",
                "name": (
                    f"{group_id} preserves the approved front/top/bottom "
                    "source order"
                ),
                "observed_boundary_ids": (
                    record.get("ordered_boundary_ids") if record else None
                ),
                "expected_boundary_ids": expected_ids,
                "result": "pass" if result else "fail",
            }
        )
    return checks


def center_bridge_checks(
    boundaries: dict[str, Any],
) -> list[dict[str, Any]]:
    records = boundaries["boundaries"]
    top_y0 = Fraction(1093, 2)
    bottom_y0 = Fraction(539)

    top_c02_x_source, top_c02_modes = interpolate_owner_x(
        "TOP_C02_INNER_OWNER_EDGE",
        records["TOP_C02_INNER_OWNER_EDGE"],
        top_y0,
    )
    top_c03_x_source, top_c03_modes = interpolate_owner_x(
        "TOP_C03_INNER_OWNER_EDGE",
        records["TOP_C03_INNER_OWNER_EDGE"],
        top_y0,
    )
    bottom_logical_c02_x_source, bottom_c02_modes = interpolate_owner_x(
        "BOTTOM_C03_INNER_OWNER_EDGE",
        records["BOTTOM_C03_INNER_OWNER_EDGE"],
        bottom_y0,
    )
    bottom_logical_c03_x_source, bottom_c03_modes = interpolate_owner_x(
        "BOTTOM_C02_INNER_OWNER_EDGE",
        records["BOTTOM_C02_INNER_OWNER_EDGE"],
        bottom_y0,
    )

    axial_scale = Fraction(52020, 517681)
    top_c02_x = (top_c02_x_source - Fraction(1533, 2)) * axial_scale
    top_c03_x = (top_c03_x_source - Fraction(1533, 2)) * axial_scale
    bottom_c02_x = (
        Fraction(1529, 2) - bottom_logical_c02_x_source
    ) * axial_scale
    bottom_c03_x = (
        Fraction(1529, 2) - bottom_logical_c03_x_source
    ) * axial_scale

    checks: list[dict[str, Any]] = []
    for name, c02_x, c03_x, modes in (
        (
            "TOP",
            top_c02_x,
            top_c03_x,
            top_c02_modes + top_c03_modes,
        ),
        (
            "BOTTOM",
            bottom_c02_x,
            bottom_c03_x,
            bottom_c02_modes + bottom_c03_modes,
        ),
    ):
        bridge = abs(c02_x + c03_x)
        checks.append(
            {
                "id": f"STITCH-Y0-{name}-ENDPOINT-BRIDGE",
                "name": (
                    f"{name.lower()} Y=0 source and Rz180 counterpart "
                    "endpoints remain distinct evidence and require the "
                    "approved straight endpoint edge"
                ),
                "logical_c02_x_cm_exact": (
                    f"{c02_x.numerator}/{c02_x.denominator}"
                ),
                "rz180_logical_c03_x_cm_exact": (
                    f"{-c03_x.numerator}/{c03_x.denominator}"
                ),
                "bridge_length_cm_exact": (
                    f"{bridge.numerator}/{bridge.denominator}"
                ),
                "bridge_length_cm": f"{float(bridge):.12f}",
                "endpoint_modes": modes,
                "tolerance_weld_allowed": False,
                "result": (
                    "pass"
                    if bridge > 0
                    and set(modes) == {"shared_contact_cut"}
                    else "fail"
                ),
            }
        )
    return checks


def candidate_clip_checks(
    blueprint: dict[str, Any],
    boundaries: dict[str, Any],
) -> list[dict[str, Any]]:
    records = boundaries["boundaries"]
    scale = exact(
        blueprint["measurement_catalog"]["MEAS_AXIAL_SCALE"]["value"][
            "scale_y"
        ]
    )
    candidates = {
        "rune_side": exact(
            blueprint["measurement_catalog"]["MEAS_RUNE_DEPTH"][
                "half_value_cm"
            ]
        ),
        "metal_center_piece_side": exact(
            blueprint["measurement_catalog"]["MEAS_METAL_DEPTH"][
                "half_value_cm"
            ]
        ),
    }
    checks: list[dict[str, Any]] = []
    for candidate, half_depth in candidates.items():
        top_front_y = Fraction(1093, 2) - half_depth / scale
        bottom_front_y = Fraction(539) + half_depth / scale
        for plane, target_y, boundary_ids in (
            (
                "top",
                top_front_y,
                (
                    "TOP_C02_INNER_OWNER_EDGE",
                    "TOP_C03_INNER_OWNER_EDGE",
                ),
            ),
            (
                "bottom",
                bottom_front_y,
                (
                    "BOTTOM_C02_INNER_OWNER_EDGE",
                    "BOTTOM_C03_INNER_OWNER_EDGE",
                ),
            ),
        ):
            covered = True
            ranges: dict[str, list[int]] = {}
            for boundary_id in boundary_ids:
                samples = records[boundary_id]["samples"]
                minimum = int(samples[0]["y"])
                maximum = int(samples[-1]["y"])
                ranges[boundary_id] = [minimum, maximum]
                covered = covered and Fraction(minimum) <= target_y <= Fraction(
                    maximum
                )
            checks.append(
                {
                    "id": (
                        f"STITCH-CLIP-{candidate.upper()}-{plane.upper()}"
                    ),
                    "name": (
                        f"{candidate} {plane} owner edges cover the exact "
                        "front candidate-depth intersection"
                    ),
                    "target_source_y_exact": (
                        f"{target_y.numerator}/{target_y.denominator}"
                    ),
                    "source_ranges_inclusive": ranges,
                    "result": "pass" if covered else "fail",
                }
            )
    return checks


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
    boundaries: dict[str, Any],
    stitch_amendment_text: str,
) -> list[dict[str, Any]]:
    instructions = {
        record["id"]: record
        for record in blueprint["closure_and_contact_instructions"]
    }
    normalized_text = " ".join(stitch_amendment_text.split())
    checks: list[dict[str, Any]] = []
    for component_id in ("C02", "C03"):
        closure_id = f"CLOSURE_{component_id}_INNER"
        instruction = instructions[closure_id]
        expected_refs = [
            f"CORR_{component_id}_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES",
            f"FRONT_{component_id}_INNER_OWNER_EDGE",
            f"TOP_{component_id}_INNER_OWNER_EDGE",
            f"BOTTOM_{component_id}_INNER_OWNER_EDGE",
        ]
        amendment_scope_present = (
            "`CLOSURE_C02_INNER`, `CLOSURE_C03_INNER`" in normalized_text
        )
        checks.append(
            {
                "id": f"CONSTRUCTIBILITY-{closure_id}",
                "name": (
                    f"{closure_id} is resolved by the approved completed-"
                    "perimeter straight-triangle rule"
                ),
                "method": instruction["method"],
                "observed_source_ownership_refs": instruction[
                    "source_ownership_refs"
                ],
                "expected_source_ownership_refs": expected_refs,
                "approved_resolution": (
                    "one completed closed perimeter; deterministic straight "
                    "triangles; existing or exact intersection vertices only"
                ),
                "amendment_scope_present": amendment_scope_present,
                "result": (
                    "pass"
                    if instruction["source_ownership_refs"] == expected_refs
                    and instruction["method"]
                    == "ordered_straight_ruled_faces"
                    and instruction["fills_protected_negative_space"] is False
                    and instruction["duplicate_wall_created"] is False
                    and amendment_scope_present
                    else "fail"
                ),
            }
        )
    checks.extend(boundary_record_checks(boundaries))
    checks.extend(center_bridge_checks(boundaries))
    checks.extend(candidate_clip_checks(blueprint, boundaries))
    return checks


def build_validation(
    blueprint_path: Path,
    amendment_path: Path,
    parity_amendment_path: Path,
    stitch_amendment_path: Path,
) -> dict[str, Any]:
    blueprint = load_json(blueprint_path)
    amendment_text = amendment_path.read_text(encoding="utf-8")
    parity_amendment_text = parity_amendment_path.read_text(encoding="utf-8")
    stitch_amendment_text = stitch_amendment_path.read_text(
        encoding="utf-8"
    )
    authority_checks, authority_paths = verify_authority(
        blueprint_path,
        amendment_path,
        parity_amendment_path,
        stitch_amendment_path,
        blueprint,
    )
    amendment_checks = amendment_semantic_checks(amendment_text)
    parity_amendment_checks = parity_amendment_semantic_checks(
        parity_amendment_text
    )
    stitch_amendment_checks = stitch_amendment_semantic_checks(
        stitch_amendment_text
    )

    scanlines = load_gzip_json(authority_paths["step09a_scanlines"])
    boundaries = load_json(authority_paths["step09a_boundaries"])
    payload_checks = correction_payload_checks(
        blueprint,
        scanlines,
        boundaries,
    )
    constructibility_checks = closure_constructibility_checks(
        blueprint,
        boundaries,
        stitch_amendment_text,
    )
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
    stitch_amendment_failures = [
        check
        for check in stitch_amendment_checks
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
        and not stitch_amendment_failures
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
            "AERATHEA_STEP11D_THREE_BOUNDARY_STONE_STITCH_"
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
                "hash-locked Step 09A ordered boundary records",
                "hash-locked pixel/world equations",
                "asset-specific Flamestrike high-poly/Nanite amendment",
                "Flamestrike-approved bottom C02/C03 label correction",
                "Flamestrike-approved completed-perimeter stone stitch rule",
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
            "stitch_amendment_path": relative(stitch_amendment_path),
            "stitch_amendment_sha256": sha256(stitch_amendment_path),
            "authority_checks_passed": len(authority_checks)
            - len(authority_failures),
            "authority_checks_failed": len(authority_failures),
            "semantic_checks_passed": (
                len(amendment_checks)
                + len(parity_amendment_checks)
                + len(stitch_amendment_checks)
                - len(amendment_failures)
                - len(parity_amendment_failures)
                - len(stitch_amendment_failures)
            ),
            "semantic_checks_failed": (
                len(amendment_failures)
                + len(parity_amendment_failures)
                + len(stitch_amendment_failures)
            ),
            "payload_checks_passed": len(payload_checks)
            - len(payload_failures),
            "payload_checks_failed": len(payload_failures),
            "checks": (
                authority_checks
                + amendment_checks
                + parity_amendment_checks
                + stitch_amendment_checks
                + payload_checks
                + [raw_conflict_check]
            ),
        },
        "stitch_validation": {
            "result": (
                "PASS"
                if not stitch_amendment_failures
                and not constructibility_failures
                else "FAIL"
            ),
            "amendment_path": relative(stitch_amendment_path),
            "amendment_sha256": sha256(stitch_amendment_path),
            "semantic_checks_passed": (
                len(stitch_amendment_checks)
                - len(stitch_amendment_failures)
            ),
            "semantic_checks_failed": len(stitch_amendment_failures),
            "constructibility_checks_passed": (
                len(constructibility_checks)
                - len(constructibility_failures)
            ),
            "constructibility_checks_failed": len(
                constructibility_failures
            ),
            "approved_surface_rule": (
                "one completed closed perimeter per stone; deterministic "
                "straight triangles; no interior or tolerance-derived vertices"
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
                        "Blueprint block: approved additive Step 11B/11C/11D "
                        "authority failed independent validation"
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
                None
                if not constructibility_failures
                else (
                    "The approved completed-perimeter rule, its exact "
                    "boundary records, center endpoint bridges, or candidate "
                    "clip coverage failed independent validation."
                )
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
            "approved_stitch_resolution": {
                "closure_ids": [
                    "CLOSURE_C02_INNER",
                    "CLOSURE_C03_INNER",
                ],
                "perimeter_timing": (
                    "after the one approved whole-asset Rz180 completion"
                ),
                "triangle_vertices": (
                    "measured owner-edge vertices, exact authorized "
                    "intersection vertices, and their one Rz180 occurrences"
                ),
                "triangulation": (
                    "deterministic constrained ear clipping; no Steiner "
                    "vertices"
                ),
                "protected_gap_fill_allowed": False,
                "tolerance_weld_allowed": False,
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


def _float_close(
    observed: float,
    expected_value: float,
    tolerance: float = 1.0e-5,
) -> bool:
    return math.isclose(
        observed,
        expected_value,
        rel_tol=0.0,
        abs_tol=tolerance,
    )


def _coordinate_key(
    point: Iterable[float],
    digits: int = 7,
) -> tuple[float, float, float]:
    values = tuple(round(float(value), digits) for value in point)
    return values  # type: ignore[return-value]


def _owner_row_lookup(
    rows: Iterable[dict[str, Any]],
) -> dict[int, list[tuple[int, int]]]:
    return {
        int(row.get("y", row.get("source_y"))): [
            (int(start), int(stop))
            for start, stop in row.get(
                "owner_runs_half_open",
                row.get("runs_half_open", []),
            )
        ]
        for row in rows
    }


def _owner_cell_count(rows: Iterable[dict[str, Any]]) -> int:
    return sum(
        int(stop) - int(start)
        for row in rows
        for start, stop in row.get(
            "owner_runs_half_open",
            row.get("runs_half_open", []),
        )
    )


def _clipped_owner_cell_count(
    rows: Iterable[dict[str, Any]],
    minimum_y: Fraction,
    maximum_y: Fraction,
) -> int:
    count = 0
    for row in rows:
        source_y = Fraction(int(row.get("y", row.get("source_y"))))
        if max(source_y, minimum_y) >= min(source_y + 1, maximum_y):
            continue
        count += sum(
            int(stop) - int(start)
            for start, stop in row.get(
                "owner_runs_half_open",
                row.get("runs_half_open", []),
            )
        )
    return count


def _owner_contains(
    lookup: dict[int, list[tuple[int, int]]],
    source_x: float,
    source_y: float,
) -> bool:
    source_row = math.floor(source_y + 1.0e-7)
    source_column = math.floor(source_x + 1.0e-7)
    return any(
        start <= source_column < stop
        for start, stop in lookup.get(source_row, [])
    )


def _polygon_center(mesh: Any, polygon: Any) -> tuple[float, float, float]:
    count = len(polygon.vertices)
    return tuple(
        sum(float(mesh.vertices[index].co[axis]) for index in polygon.vertices)
        / count
        for axis in range(3)
    )  # type: ignore[return-value]


def _visible_surface_audit(
    obj: Any,
    plane: str,
    rows: list[dict[str, Any]],
    expected_polygons: int,
    half_depth: Fraction,
    world_z: Fraction | None = None,
    c04_candidate: str | None = None,
) -> dict[str, Any]:
    lookup = _owner_row_lookup(rows)
    owner_failures = 0
    plane_failures = 0
    for polygon in obj.data.polygons:
        x, y, z = _polygon_center(obj.data, polygon)
        if plane == "front":
            source_x = float(FRONT_AXIS_X) + x / float(FRONT_SCALE)
            source_y = float(FRONT_Z_ORIGIN_Y) - z / float(FRONT_SCALE)
            plane_ok = _float_close(y, -float(half_depth))
        elif plane == "top":
            source_x = float(TOP_CENTER_X) + x / float(AXIAL_SCALE)
            source_y = float(TOP_CENTER_Y) + y / float(AXIAL_SCALE)
            plane_ok = world_z is not None and _float_close(z, float(world_z))
        elif plane == "bottom":
            source_x = float(BOTTOM_CENTER_X) - x / float(AXIAL_SCALE)
            source_y = float(BOTTOM_CENTER_Y) - y / float(AXIAL_SCALE)
            plane_ok = world_z is not None and _float_close(z, float(world_z))
        elif plane == "right":
            source_y = float(RIGHT_Z_ORIGIN_Y) - z / float(RIGHT_SCALE)
            if c04_candidate == "rune_side":
                source_x = float(RIGHT_AXIS_X) + abs(y) / float(RIGHT_SCALE)
            elif c04_candidate == "metal_center_piece_side":
                source_x = float(RIGHT_AXIS_X) - abs(y) / float(RIGHT_SCALE)
            else:
                raise ValueError("right-plane audit requires a candidate")
            plane_ok = _float_close(
                x,
                float(Fraction(52020, 1063)),
            )
        else:
            raise ValueError(plane)
        if not plane_ok:
            plane_failures += 1
        if not _owner_contains(lookup, source_x, source_y):
            owner_failures += 1
    observed_polygons = len(obj.data.polygons)
    return {
        "expected_polygons": expected_polygons,
        "observed_polygons": observed_polygons,
        "owner_cell_failures": owner_failures,
        "plane_failures": plane_failures,
        "result": (
            "PASS"
            if observed_polygons == expected_polygons
            and owner_failures == 0
            and plane_failures == 0
            else "FAIL"
        ),
    }


def _rotational_rows(
    component: str,
    start: int,
    stop: int,
    scanlines: dict[str, Any],
    step06_front: dict[str, Any],
) -> list[dict[str, Any]]:
    if component == "C06_UPPER_HAFT_CAP":
        rows = owner_rows(scanlines, "front", component)
    elif component == "C12_UPPER_HEAD_CAP_SPIRE":
        rows = [
            row
            for row in step06_front["row_profiles"]
            if start <= int(row["source_y"]) < 221
        ]
        rows.extend(
            owner_rows(
                scanlines,
                "front",
                "C12_RESERVED_EXISTING_OWNER",
            )
        )
    else:
        rows = [
            row
            for row in step06_front["row_profiles"]
            if start <= int(row["source_y"]) < stop
        ]
    return sorted(
        rows,
        key=lambda row: int(row.get("y", row.get("source_y"))),
    )


def _positive_radius(row: dict[str, Any]) -> Fraction:
    runs = row.get("owner_runs_half_open", row.get("runs_half_open", []))
    positive_edge = max(int(stop) for _, stop in runs)
    return Fraction(positive_edge - int(FRONT_AXIS_X)) * FRONT_SCALE


def _rotational_surface_audit(
    obj: Any,
    rows: list[dict[str, Any]],
    start: int,
    stop: int,
) -> dict[str, Any]:
    observed_source_rows = [
        int(row.get("y", row.get("source_y"))) for row in rows
    ]
    row_sequence_ok = observed_source_rows == list(range(start, stop))
    radii = [_positive_radius(row) for row in rows]
    ring_records = [
        (
            (FRONT_Z_ORIGIN_Y - Fraction(source_y)) * FRONT_SCALE,
            radius,
        )
        for source_y, radius in zip(observed_source_rows, radii)
    ]
    if radii:
        ring_records.append(
            (
                (FRONT_Z_ORIGIN_Y - Fraction(stop)) * FRONT_SCALE,
                radii[-1],
            )
        )
    expected_vertices = len(ring_records) * (ANGULAR_DIVISIONS + 1)
    expected_polygons = max(0, len(ring_records) - 1) * ANGULAR_DIVISIONS
    vertex_failures = 0
    endpoint_failures = 0
    for ring_index, (expected_z, expected_radius) in enumerate(ring_records):
        offset = ring_index * (ANGULAR_DIVISIONS + 1)
        ring = obj.data.vertices[offset : offset + ANGULAR_DIVISIONS + 1]
        if len(ring) != ANGULAR_DIVISIONS + 1:
            vertex_failures += ANGULAR_DIVISIONS + 1 - len(ring)
            continue
        for vertex in ring:
            x, y, z = (float(value) for value in vertex.co)
            radius = math.hypot(x, y)
            if (
                x < -1.0e-6
                or not _float_close(z, float(expected_z), 2.0e-5)
                or not _float_close(radius, float(expected_radius), 2.0e-5)
            ):
                vertex_failures += 1
        first = ring[0].co
        last = ring[-1].co
        if not (
            abs(float(first.x)) <= 1.0e-5
            and _float_close(float(first.y), -float(expected_radius), 2.0e-5)
            and abs(float(last.x)) <= 1.0e-5
            and _float_close(float(last.y), float(expected_radius), 2.0e-5)
        ):
            endpoint_failures += 1
    passed = (
        row_sequence_ok
        and len(obj.data.vertices) == expected_vertices
        and len(obj.data.polygons) == expected_polygons
        and vertex_failures == 0
        and endpoint_failures == 0
    )
    return {
        "source_rows_half_open": [start, stop],
        "source_row_sequence_exact": row_sequence_ok,
        "angular_divisions_positive_x": ANGULAR_DIVISIONS,
        "expected_rings": len(ring_records),
        "expected_vertices": expected_vertices,
        "observed_vertices": len(obj.data.vertices),
        "expected_polygons": expected_polygons,
        "observed_polygons": len(obj.data.polygons),
        "vertex_measurement_failures": vertex_failures,
        "half_ring_endpoint_failures": endpoint_failures,
        "result": "PASS" if passed else "FAIL",
    }


def _rz180_pair_audit(source: Any, rotated: Any) -> dict[str, Any]:
    count_ok = (
        len(source.data.vertices) == len(rotated.data.vertices)
        and len(source.data.polygons) == len(rotated.data.polygons)
    )
    vertex_failures = 0
    if count_ok:
        for source_vertex, rotated_vertex in zip(
            source.data.vertices,
            rotated.data.vertices,
        ):
            expected = (
                -float(source_vertex.co.x),
                -float(source_vertex.co.y),
                float(source_vertex.co.z),
            )
            observed = tuple(float(value) for value in rotated_vertex.co)
            if not all(
                _float_close(actual, target, 2.0e-5)
                for actual, target in zip(observed, expected)
            ):
                vertex_failures += 1
    face_index_failures = 0
    if count_ok:
        for source_face, rotated_face in zip(
            source.data.polygons,
            rotated.data.polygons,
        ):
            if tuple(source_face.vertices) != tuple(rotated_face.vertices):
                face_index_failures += 1
    passed = count_ok and vertex_failures == 0 and face_index_failures == 0
    return {
        "source": source.name,
        "rotated": rotated.name,
        "vertex_count": len(source.data.vertices),
        "polygon_count": len(source.data.polygons),
        "vertex_transform_failures": vertex_failures,
        "face_index_failures": face_index_failures,
        "result": "PASS" if passed else "FAIL",
    }


def _mesh_topology(mesh: Any) -> dict[str, Any]:
    edge_uses: Counter[tuple[int, int]] = Counter()
    adjacency: dict[int, set[int]] = defaultdict(set)
    for polygon in mesh.polygons:
        indices = list(polygon.vertices)
        for start, stop in zip(indices, indices[1:] + indices[:1]):
            edge = (min(start, stop), max(start, stop))
            edge_uses[edge] += 1
            adjacency[start].add(stop)
            adjacency[stop].add(start)
    active_vertices = set(adjacency)
    components = 0
    remaining = set(active_vertices)
    while remaining:
        components += 1
        stack = [remaining.pop()]
        while stack:
            current = stack.pop()
            neighbours = adjacency[current] & remaining
            stack.extend(neighbours)
            remaining.difference_update(neighbours)
    vertices = len(active_vertices)
    edges = len(edge_uses)
    faces = len(mesh.polygons)
    return {
        "active_vertices": vertices,
        "stored_vertices": len(mesh.vertices),
        "edges": edges,
        "faces": faces,
        "euler_characteristic": vertices - edges + faces,
        "connected_components": components,
        "boundary_edges": sum(count == 1 for count in edge_uses.values()),
        "nonmanifold_edges_over_two": sum(
            count > 2 for count in edge_uses.values()
        ),
        "maximum_edge_face_use": max(edge_uses.values(), default=0),
        "triangle_faces": sum(
            len(polygon.vertices) == 3 for polygon in mesh.polygons
        ),
        "quad_faces": sum(
            len(polygon.vertices) == 4 for polygon in mesh.polygons
        ),
    }


def _bridge_edge_present(
    obj: Any,
    world_z: Fraction,
    expected_length: Fraction,
) -> bool:
    for edge in obj.data.edges:
        a = obj.data.vertices[edge.vertices[0]].co
        b = obj.data.vertices[edge.vertices[1]].co
        if (
            abs(float(a.y)) <= 2.0e-5
            and abs(float(b.y)) <= 2.0e-5
            and _float_close(float(a.z), float(world_z), 2.0e-5)
            and _float_close(float(b.z), float(world_z), 2.0e-5)
            and _float_close(
                abs(float(a.x) - float(b.x)),
                float(expected_length),
                2.0e-5,
            )
        ):
            return True
    return False


def _expected_object_names(
    blueprint: dict[str, Any],
    candidate: str,
) -> tuple[set[str], list[str]]:
    surface_names = [
        record["id"]
        for record in blueprint["surface_instructions"]
        if candidate in record["candidate_variants"]
    ]
    contact_names = [
        TRANSITION_TO_INSTRUCTION[transition_id]
        for transition_id, transition in blueprint[
            "transition_catalog"
        ].items()
        if not transition["same_radius"]
    ]
    source_names = surface_names + contact_names + [
        "CAP_C11_BOTTOM",
        "CAP_C12_TOP",
    ]
    outer = (
        "CLOSURE_C03_TO_C04_RUNE"
        if candidate == "rune_side"
        else "CLOSURE_C03_TO_C04_METAL"
    )
    expected = set(source_names)
    expected.update(f"{name}__RZ180" for name in source_names)
    expected.update(
        {
            "CLOSURE_C02_INNER_COMPLETED_PERIMETER",
            "CLOSURE_C03_INNER_COMPLETED_PERIMETER",
            outer,
            f"{outer}_RZ180",
        }
    )
    return expected, source_names


def build_saved_candidate_audit(
    blueprint_path: Path,
    amendment_path: Path,
    parity_amendment_path: Path,
    stitch_amendment_path: Path,
    saved_candidate: Path,
    candidate: str,
) -> dict[str, Any]:
    import bpy  # type: ignore

    checks: list[dict[str, Any]] = []

    def add_check(
        check_id: str,
        passed: bool,
        expected_value: Any,
        observed: Any,
        category: str,
    ) -> None:
        checks.append(
            {
                "id": check_id,
                "category": category,
                "expected": expected_value,
                "observed": observed,
                "result": "PASS" if passed else "FAIL",
            }
        )

    blueprint = load_json(blueprint_path)
    authority_checks, authority_paths = verify_authority(
        blueprint_path,
        amendment_path,
        parity_amendment_path,
        stitch_amendment_path,
        blueprint,
    )
    for record in authority_checks:
        add_check(
            record["id"],
            record["result"] == "pass",
            record["expected_sha256"],
            record["observed_sha256"],
            "authority",
        )

    scanlines = load_gzip_json(authority_paths["step09a_scanlines"])
    boundaries = load_json(authority_paths["step09a_boundaries"])
    step06_front = load_json(authority_paths["step06_front"])
    scene = bpy.context.scene
    mesh_objects = sorted(
        (obj for obj in scene.objects if obj.type == "MESH"),
        key=lambda obj: obj.name,
    )
    objects = {obj.name: obj for obj in mesh_objects}

    opened_path = Path(bpy.data.filepath).resolve()
    add_check(
        "SAVED-FILE-EXACT-PATH",
        opened_path == saved_candidate,
        relative(saved_candidate),
        relative(opened_path) if opened_path.is_relative_to(ROOT) else str(opened_path),
        "saved-file identity",
    )
    add_check(
        "SCENE-ONLY-MESH-OBJECTS",
        len(scene.objects) == len(mesh_objects),
        "all saved scene objects are mesh records",
        {
            "scene_objects": len(scene.objects),
            "mesh_objects": len(mesh_objects),
            "non_mesh": [
                obj.name for obj in scene.objects if obj.type != "MESH"
            ],
        },
        "scene structure",
    )

    expected_names, source_names = _expected_object_names(
        blueprint,
        candidate,
    )
    observed_names = set(objects)
    add_check(
        "OBJECT-INVENTORY-EXACT",
        observed_names == expected_names,
        sorted(expected_names),
        {
            "missing": sorted(expected_names - observed_names),
            "unexpected": sorted(observed_names - expected_names),
            "count": len(observed_names),
        },
        "closed-world inventory",
    )

    unit_observed = {
        "system": scene.unit_settings.system,
        "length_unit": scene.unit_settings.length_unit,
        "scale_length": scene.unit_settings.scale_length,
    }
    add_check(
        "SCENE-METRIC-CENTIMETERS",
        scene.unit_settings.system == "METRIC"
        and scene.unit_settings.length_unit == "CENTIMETERS"
        and _float_close(scene.unit_settings.scale_length, 0.01, 1.0e-9),
        {
            "system": "METRIC",
            "length_unit": "CENTIMETERS",
            "scale_length": 0.01,
        },
        unit_observed,
        "scene configuration",
    )
    render_observed = {
        "engine": scene.render.engine,
        "device": scene.cycles.device,
        "samples": scene.cycles.samples,
        "adaptive": scene.cycles.use_adaptive_sampling,
        "denoising": scene.cycles.use_denoising,
        "view_transform": scene.view_settings.view_transform,
    }
    add_check(
        "SCENE-DETERMINISTIC-RENDER-SETTINGS",
        scene.render.engine == "CYCLES"
        and scene.cycles.device == "CPU"
        and scene.cycles.samples == 32
        and scene.cycles.use_adaptive_sampling is False
        and scene.cycles.use_denoising is False
        and scene.view_settings.view_transform == "Standard",
        {
            "engine": "CYCLES",
            "device": "CPU",
            "samples": 32,
            "adaptive": False,
            "denoising": False,
            "view_transform": "Standard",
        },
        render_observed,
        "scene configuration",
    )

    transform_failures = []
    modifier_failures = []
    uv_failures = []
    material_failures = []
    nonfinite_vertices = 0
    zero_area_faces = 0
    degenerate_index_faces = 0
    total_vertices = 0
    total_polygons = 0
    total_triangles = 0
    minimum = [math.inf, math.inf, math.inf]
    maximum = [-math.inf, -math.inf, -math.inf]
    for obj in mesh_objects:
        transform_ok = (
            all(abs(float(value)) <= 1.0e-8 for value in obj.location)
            and all(
                abs(float(value)) <= 1.0e-8 for value in obj.rotation_euler
            )
            and all(
                _float_close(float(value), 1.0, 1.0e-8)
                for value in obj.scale
            )
        )
        if not transform_ok:
            transform_failures.append(obj.name)
        if obj.modifiers:
            modifier_failures.append(
                {
                    "object": obj.name,
                    "modifiers": [
                        f"{modifier.name}:{modifier.type}"
                        for modifier in obj.modifiers
                    ],
                }
            )
        if obj.data.uv_layers:
            uv_failures.append(obj.name)
        material_names = [slot.name for slot in obj.data.materials if slot]
        has_image_node = any(
            material.use_nodes
            and any(
                node.type == "TEX_IMAGE"
                for node in material.node_tree.nodes
            )
            for material in obj.data.materials
            if material is not None
        )
        if (
            len(material_names) != 1
            or not material_names[0].startswith("M_STEP12_PROOF_")
            or has_image_node
        ):
            material_failures.append(
                {
                    "object": obj.name,
                    "materials": material_names,
                    "image_texture_node": has_image_node,
                }
            )
        total_vertices += len(obj.data.vertices)
        total_polygons += len(obj.data.polygons)
        total_triangles += sum(
            max(0, len(polygon.vertices) - 2)
            for polygon in obj.data.polygons
        )
        for vertex in obj.data.vertices:
            coordinates = tuple(float(value) for value in vertex.co)
            if not all(math.isfinite(value) for value in coordinates):
                nonfinite_vertices += 1
                continue
            for axis in range(3):
                minimum[axis] = min(minimum[axis], coordinates[axis])
                maximum[axis] = max(maximum[axis], coordinates[axis])
        for polygon in obj.data.polygons:
            if len(set(polygon.vertices)) != len(polygon.vertices):
                degenerate_index_faces += 1
            if float(polygon.area) <= 1.0e-12:
                zero_area_faces += 1

    add_check(
        "OBJECT-IDENTITY-TRANSFORMS",
        not transform_failures,
        [],
        transform_failures,
        "geometry invariants",
    )
    add_check(
        "OBJECT-NO-MODIFIERS",
        not modifier_failures,
        [],
        modifier_failures,
        "forbidden methods",
    )
    add_check(
        "OBJECT-NO-UV-LAYERS",
        not uv_failures,
        [],
        uv_failures,
        "stage boundary",
    )
    add_check(
        "OBJECT-PROOF-MATERIALS-ONLY",
        not material_failures,
        "one M_STEP12_PROOF_* material and no image textures per object",
        material_failures,
        "stage boundary",
    )
    add_check(
        "MESH-FINITE-NONDEGENERATE",
        nonfinite_vertices == 0
        and zero_area_faces == 0
        and degenerate_index_faces == 0,
        {
            "nonfinite_vertices": 0,
            "zero_area_faces": 0,
            "degenerate_index_faces": 0,
        },
        {
            "nonfinite_vertices": nonfinite_vertices,
            "zero_area_faces": zero_area_faces,
            "degenerate_index_faces": degenerate_index_faces,
        },
        "geometry invariants",
    )

    dimensions_record = blueprint["candidate_variants"][candidate][
        "completed_dimensions_cm"
    ]
    expected_dimensions = [
        float(exact(dimensions_record[axis]))
        for axis in ("width", "depth", "height")
    ]
    observed_dimensions = [
        maximum[axis] - minimum[axis] for axis in range(3)
    ]
    expected_minimum = [
        -expected_dimensions[0] / 2.0,
        -expected_dimensions[1] / 2.0,
        0.0,
    ]
    expected_maximum = [
        expected_dimensions[0] / 2.0,
        expected_dimensions[1] / 2.0,
        expected_dimensions[2],
    ]
    bounds_ok = all(
        _float_close(observed, expected, 3.0e-5)
        for observed, expected in zip(
            minimum + maximum,
            expected_minimum + expected_maximum,
        )
    )
    add_check(
        "GEOMETRY-BOUNDS-PIVOT-SCALE",
        bounds_ok,
        {
            "minimum_cm": expected_minimum,
            "maximum_cm": expected_maximum,
            "dimensions_cm": expected_dimensions,
        },
        {
            "minimum_cm": minimum,
            "maximum_cm": maximum,
            "dimensions_cm": observed_dimensions,
        },
        "scale and pivot",
    )

    half_depth = exact(
        blueprint["candidate_variants"][candidate]["source_half_depth_cm"]
    )
    stone_top_z = exact(
        blueprint["measurement_catalog"]["MEAS_C02"]["world_z_top_cm"]
    )
    stone_bottom_z = exact(
        blueprint["measurement_catalog"]["MEAS_C02"]["world_z_bottom_cm"]
    )
    visible_specs = [
        (
            "SURF_C01_FRONT",
            "front",
            owner_rows(scanlines, "front", "C01_CENTER_CORE"),
            None,
            None,
        ),
        (
            "SURF_C02_FRONT",
            "front",
            owner_rows(scanlines, "front", "C02_STONE_LEFT"),
            None,
            None,
        ),
        (
            "SURF_C03_FRONT",
            "front",
            owner_rows(scanlines, "front", "C03_STONE_RIGHT"),
            None,
            None,
        ),
        (
            "SURF_C02_TOP_HALF",
            "top",
            owner_rows(scanlines, "top", "C02_STONE_LEFT"),
            stone_top_z,
            None,
        ),
        (
            "SURF_C03_TOP_HALF",
            "top",
            owner_rows(scanlines, "top", "C03_STONE_RIGHT"),
            stone_top_z,
            None,
        ),
        (
            "SURF_C02_BOTTOM_HALF",
            "bottom",
            owner_rows(scanlines, "bottom", "C03_STONE_RIGHT"),
            stone_bottom_z,
            None,
        ),
        (
            "SURF_C03_BOTTOM_HALF",
            "bottom",
            owner_rows(scanlines, "bottom", "C02_STONE_LEFT"),
            stone_bottom_z,
            None,
        ),
    ]
    for name, plane, rows, world_z, c04_candidate in visible_specs:
        if plane == "front":
            expected_polygons = _owner_cell_count(rows)
        elif plane == "top":
            expected_polygons = _clipped_owner_cell_count(
                rows,
                TOP_CENTER_Y - half_depth / AXIAL_SCALE,
                TOP_CENTER_Y,
            )
        else:
            expected_polygons = _clipped_owner_cell_count(
                rows,
                BOTTOM_CENTER_Y,
                BOTTOM_CENTER_Y + half_depth / AXIAL_SCALE,
            )
        if name not in objects:
            audit = {
                "result": "FAIL",
                "reason": "object missing",
            }
        else:
            audit = _visible_surface_audit(
                objects[name],
                plane,
                rows,
                expected_polygons,
                half_depth,
                world_z,
                c04_candidate,
            )
        add_check(
            f"SOURCE-OWNER-REPLAY-{name}",
            audit["result"] == "PASS",
            "every polygon belongs to the exact approved owner cell and plane",
            audit,
            "source ownership",
        )

    c04_name = (
        "SURF_C04_RUNE_FACE_HALF"
        if candidate == "rune_side"
        else "SURF_C04_METAL_FACE_HALF"
    )
    c04_owner = (
        "C04_RUNE_SIDE"
        if candidate == "rune_side"
        else "C04_METAL_CENTER_PIECE_SIDE"
    )
    c04_rows = owner_rows(scanlines, "right", c04_owner)
    if c04_name in objects:
        c04_audit = _visible_surface_audit(
            objects[c04_name],
            "right",
            c04_rows,
            2 * _owner_cell_count(c04_rows),
            half_depth,
            None,
            candidate,
        )
        coordinates = Counter(
            _coordinate_key(vertex.co)
            for vertex in objects[c04_name].data.vertices
        )
        mirror_coordinates = Counter(
            (x, round(-y, 7), z)
            for x, y, z in coordinates.elements()
        )
        local_mirror_ok = coordinates == mirror_coordinates
        c04_audit["local_y_mirror_coordinate_exact"] = local_mirror_ok
        c04_audit["result"] = (
            "PASS"
            if c04_audit["result"] == "PASS" and local_mirror_ok
            else "FAIL"
        )
    else:
        c04_audit = {"result": "FAIL", "reason": "object missing"}
    add_check(
        f"SOURCE-OWNER-REPLAY-{c04_name}",
        c04_audit["result"] == "PASS",
        (
            "every polygon belongs to the exact candidate C04 owner; "
            "one coordinate-exact local Y mirror"
        ),
        c04_audit,
        "source ownership",
    )

    for name, (component, start, stop) in ROTATIONAL_COMPONENTS.items():
        if name not in objects:
            audit = {"result": "FAIL", "reason": "object missing"}
        else:
            rows = _rotational_rows(
                component,
                start,
                stop,
                scanlines,
                step06_front,
            )
            audit = _rotational_surface_audit(
                objects[name],
                rows,
                start,
                stop,
            )
        add_check(
            f"ROTATIONAL-REPLAY-{name}",
            audit["result"] == "PASS",
            (
                "exact source-row radii and Z stations with 64 positive-X "
                "angular divisions"
            ),
            audit,
            "source ownership",
        )

    for source_name in source_names:
        rotated_name = f"{source_name}__RZ180"
        if source_name in objects and rotated_name in objects:
            pair = _rz180_pair_audit(
                objects[source_name],
                objects[rotated_name],
            )
        else:
            pair = {
                "result": "FAIL",
                "source_present": source_name in objects,
                "rotated_present": rotated_name in objects,
            }
        add_check(
            f"RZ180-{source_name}",
            pair["result"] == "PASS",
            "one index-preserving (-X,-Y,+Z) occurrence",
            pair,
            "single whole-asset completion",
        )

    inner_pairs = (
        (
            "CLOSURE_C02_INNER_COMPLETED_PERIMETER",
            "CLOSURE_C03_INNER_COMPLETED_PERIMETER",
        ),
        (
            (
                "CLOSURE_C03_TO_C04_RUNE"
                if candidate == "rune_side"
                else "CLOSURE_C03_TO_C04_METAL"
            ),
            (
                "CLOSURE_C03_TO_C04_RUNE_RZ180"
                if candidate == "rune_side"
                else "CLOSURE_C03_TO_C04_METAL_RZ180"
            ),
        ),
    )
    for source_name, rotated_name in inner_pairs:
        if source_name in objects and rotated_name in objects:
            pair = _rz180_pair_audit(
                objects[source_name],
                objects[rotated_name],
            )
        else:
            pair = {
                "result": "FAIL",
                "source_present": source_name in objects,
                "rotated_present": rotated_name in objects,
            }
        add_check(
            f"CLOSURE-RZ180-{source_name}",
            pair["result"] == "PASS",
            "coordinate-exact Rz180 closure counterpart",
            pair,
            "closure topology",
        )

    bridge_records = center_bridge_checks(boundaries)
    bridge_lengths = {
        "TOP": Fraction(
            next(
                record["bridge_length_cm_exact"]
                for record in bridge_records
                if record["id"] == "STITCH-Y0-TOP-ENDPOINT-BRIDGE"
            )
        ),
        "BOTTOM": Fraction(
            next(
                record["bridge_length_cm_exact"]
                for record in bridge_records
                if record["id"] == "STITCH-Y0-BOTTOM-ENDPOINT-BRIDGE"
            )
        ),
    }
    for name in (
        "CLOSURE_C02_INNER_COMPLETED_PERIMETER",
        "CLOSURE_C03_INNER_COMPLETED_PERIMETER",
    ):
        if name in objects:
            topology = _mesh_topology(objects[name].data)
            top_bridge = _bridge_edge_present(
                objects[name],
                stone_top_z,
                bridge_lengths["TOP"],
            )
            bottom_bridge = _bridge_edge_present(
                objects[name],
                stone_bottom_z,
                bridge_lengths["BOTTOM"],
            )
            topology_ok = (
                topology["stored_vertices"] == topology["active_vertices"]
                and topology["euler_characteristic"] == 1
                and topology["connected_components"] == 1
                and topology["nonmanifold_edges_over_two"] == 0
                and topology["triangle_faces"] == topology["faces"]
                and topology["faces"] == topology["active_vertices"] - 2
                and top_bridge
                and bottom_bridge
            )
            topology["top_distinct_endpoint_bridge_present"] = top_bridge
            topology["bottom_distinct_endpoint_bridge_present"] = (
                bottom_bridge
            )
        else:
            topology = {"result": "FAIL", "reason": "object missing"}
            topology_ok = False
        add_check(
            f"STONE-STITCH-TOPOLOGY-{name}",
            topology_ok,
            (
                "one connected triangulated disk, no Steiner center, no "
                "non-manifold edge, and both measured Y=0 bridges preserved"
            ),
            topology,
            "closure topology",
        )

    outer_name = (
        "CLOSURE_C03_TO_C04_RUNE"
        if candidate == "rune_side"
        else "CLOSURE_C03_TO_C04_METAL"
    )
    for name in (outer_name, f"{outer_name}_RZ180"):
        if name in objects:
            topology = _mesh_topology(objects[name].data)
            topology_ok = (
                topology["stored_vertices"] == topology["active_vertices"]
                and topology["euler_characteristic"] == 0
                and topology["connected_components"] == 1
                and topology["nonmanifold_edges_over_two"] == 0
                and topology["quad_faces"] == topology["faces"]
                and topology["boundary_edges"] > 0
            )
        else:
            topology = {"result": "FAIL", "reason": "object missing"}
            topology_ok = False
        add_check(
            f"OUTER-CLOSURE-TOPOLOGY-{name}",
            topology_ok,
            "one connected ruled annular strip with two open boundary loops",
            topology,
            "closure topology",
        )

    output_root = saved_candidate.parent
    canonical_path = output_root / "canonical_geometry.json.gz"
    pre_save_path = output_root / "pre_save_validation.json"
    build_manifest_path = output_root / "build_manifest.json"
    inventory_path = output_root / "OUTPUT_INVENTORY.json"
    canonical_hash = sha256(canonical_path) if canonical_path.is_file() else None
    pre_save_hash = sha256(pre_save_path) if pre_save_path.is_file() else None
    add_check(
        "CANONICAL-GEOMETRY-INTEGRITY",
        canonical_hash is not None
        and canonical_hash == scene.get("Aerathea.CanonicalGeometrySHA256"),
        scene.get("Aerathea.CanonicalGeometrySHA256"),
        canonical_hash,
        "saved-file integrity",
    )
    add_check(
        "PRE-SAVE-VALIDATION-INTEGRITY",
        pre_save_hash is not None
        and pre_save_hash == scene.get("Aerathea.PreSaveValidationSHA256"),
        scene.get("Aerathea.PreSaveValidationSHA256"),
        pre_save_hash,
        "saved-file integrity",
    )
    pre_save = load_json(pre_save_path) if pre_save_path.is_file() else {}
    add_check(
        "DIRECT-COUNTS-MATCH-PRE-SAVE-RECORD",
        pre_save.get("result") == "PASS"
        and pre_save.get("mesh_records") == len(mesh_objects)
        and pre_save.get("vertices") == total_vertices
        and pre_save.get("polygons") == total_polygons
        and pre_save.get("triangles_observed_not_gated") == total_triangles,
        {
            "result": "PASS",
            "mesh_records": len(mesh_objects),
            "vertices": total_vertices,
            "polygons": total_polygons,
            "triangles_observed_not_gated": total_triangles,
        },
        {
            key: pre_save.get(key)
            for key in (
                "result",
                "mesh_records",
                "vertices",
                "polygons",
                "triangles_observed_not_gated",
            )
        },
        "saved-file integrity",
    )
    build_manifest = (
        load_json(build_manifest_path)
        if build_manifest_path.is_file()
        else {}
    )
    add_check(
        "BUILD-MANIFEST-SAVED-BLEND-HASH",
        build_manifest.get("candidate") == candidate
        and build_manifest.get("files", {}).get("blend", {}).get("sha256")
        == sha256(saved_candidate),
        {
            "candidate": candidate,
            "blend_sha256": sha256(saved_candidate),
        },
        {
            "candidate": build_manifest.get("candidate"),
            "blend_sha256": build_manifest.get("files", {})
            .get("blend", {})
            .get("sha256"),
        },
        "saved-file integrity",
    )
    inventory = load_json(inventory_path) if inventory_path.is_file() else {}
    allowed = set(inventory.get("allowed_relative_files", []))
    existing = {
        str(path.relative_to(output_root))
        for path in output_root.rglob("*")
        if path.is_file()
    }
    add_check(
        "OUTPUT-INVENTORY-CLOSED-WORLD",
        inventory.get("candidate") == candidate
        and existing.issubset(allowed),
        "all existing files are members of the predeclared candidate inventory",
        {
            "unexpected": sorted(existing - allowed),
            "existing_files": len(existing),
            "allowed_files": len(allowed),
        },
        "closed-world inventory",
    )

    lock_observed = {
        "asset": scene.get("Aerathea.Asset"),
        "run_id": scene.get("Aerathea.RunID"),
        "candidate": scene.get("Aerathea.Candidate"),
        "artifact_status": scene.get("Aerathea.ArtifactStatus"),
        "high_poly_nanite_stage": scene.get(
            "Aerathea.HighPolyNaniteStage"
        ),
        "step13_authorized": scene.get("Aerathea.Step13Authorized"),
        "unreal_authorized": scene.get("Aerathea.UnrealAuthorized"),
        "network_operations": scene.get("Aerathea.NetworkOperations"),
    }
    add_check(
        "SAVED-STAGE-LOCKS",
        lock_observed
        == {
            "asset": ASSET,
            "run_id": RUN_ID,
            "candidate": candidate,
            "artifact_status": "DCC source candidate",
            "high_poly_nanite_stage": True,
            "step13_authorized": False,
            "unreal_authorized": False,
            "network_operations": 0,
        },
        {
            "asset": ASSET,
            "run_id": RUN_ID,
            "candidate": candidate,
            "artifact_status": "DCC source candidate",
            "high_poly_nanite_stage": True,
            "step13_authorized": False,
            "unreal_authorized": False,
            "network_operations": 0,
        },
        lock_observed,
        "stage boundary",
    )

    failed = [record for record in checks if record["result"] != "PASS"]
    return {
        "schema": "AERATHEA_R8_STEP12_INDEPENDENT_SAVED_CANDIDATE_AUDIT_A01_V1",
        "asset": ASSET,
        "run_id": RUN_ID,
        "candidate": candidate,
        "date": datetime.now(timezone.utc).isoformat(),
        "artifact_status": "proof only",
        "result": "PASS" if not failed else "FAIL",
        "summary": {
            "passed": len(checks) - len(failed),
            "failed": len(failed),
            "total": len(checks),
        },
        "audit_independence": {
            "builder_imported": False,
            "builder_claims_used_as_geometry_authority": False,
            "saved_blend_geometry_read_directly": True,
            "expected_geometry_derived_from_hash_locked_sources": True,
            "canonical_geometry_used_for_integrity_only": True,
            "scene_custom_properties_used_for_integrity_and_stage_locks_only": True,
        },
        "direct_observations": {
            "mesh_objects": len(mesh_objects),
            "vertices": total_vertices,
            "polygons": total_polygons,
            "triangles_observed_not_gated": total_triangles,
            "bounds_minimum_cm": minimum,
            "bounds_maximum_cm": maximum,
            "polygon_limit_enforced": False,
            "polygon_limit_authority": (
                "Step 11B high-poly/Nanite amendment; count observed only"
            ),
        },
        "checks": checks,
        "failed_check_ids": [record["id"] for record in failed],
        "decision": {
            "saved_candidate_accepted": not failed,
            "proof_render_allowed": not failed,
            "artifact_class_if_pass": "DCC source candidate",
            "step13_authorized": False,
            "selection_authorized": False,
            "retopology_authorized": False,
            "uv_authorized": False,
            "baking_authorized": False,
            "export_authorized": False,
            "unreal_authorized": False,
        },
    }


def parse_args() -> argparse.Namespace:
    raw = sys.argv
    if "--" in raw:
        raw = raw[raw.index("--") + 1 :]
    else:
        raw = raw[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument("--blueprint", type=Path, default=DEFAULT_BLUEPRINT)
    parser.add_argument("--amendment", type=Path, default=DEFAULT_AMENDMENT)
    parser.add_argument(
        "--parity-amendment",
        type=Path,
        default=DEFAULT_PARITY_AMENDMENT,
    )
    parser.add_argument(
        "--stitch-amendment",
        type=Path,
        default=DEFAULT_STITCH_AMENDMENT,
    )
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--saved-candidate", type=Path)
    parser.add_argument("--candidate", choices=CANDIDATES)
    parser.add_argument("--audit-output", type=Path)
    parser.add_argument(
        "--validation-output",
        type=Path,
        default=VALIDATION_PATH,
    )
    return parser.parse_args(raw)


def main() -> int:
    args = parse_args()
    if args.saved_candidate is not None:
        if args.candidate is None or args.audit_output is None:
            raise SystemExit(
                "--candidate and --audit-output are required with "
                "--saved-candidate"
            )
        saved_candidate = args.saved_candidate.resolve()
        audit_output = args.audit_output.resolve()
        try:
            result = build_saved_candidate_audit(
                args.blueprint.resolve(),
                args.amendment.resolve(),
                args.parity_amendment.resolve(),
                args.stitch_amendment.resolve(),
                saved_candidate,
                args.candidate,
            )
        except Exception as error:
            result = {
                "schema": (
                    "AERATHEA_R8_STEP12_INDEPENDENT_SAVED_"
                    "CANDIDATE_AUDIT_A01_V1"
                ),
                "asset": ASSET,
                "run_id": RUN_ID,
                "candidate": args.candidate,
                "date": datetime.now(timezone.utc).isoformat(),
                "artifact_status": "proof only",
                "result": "FAIL",
                "summary": {"passed": 0, "failed": 1, "total": 1},
                "internal_failure": {
                    "type": type(error).__name__,
                    "message": str(error),
                },
                "decision": {
                    "saved_candidate_accepted": False,
                    "proof_render_allowed": False,
                    "step13_authorized": False,
                    "unreal_authorized": False,
                },
            }
        audit_output.parent.mkdir(parents=True, exist_ok=True)
        audit_output.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(
            json.dumps(
                {
                    "audit": relative(audit_output),
                    "candidate": args.candidate,
                    "result": result["result"],
                    "passed": result["summary"]["passed"],
                    "failed": result["summary"]["failed"],
                },
                sort_keys=True,
            )
        )
        return 0 if result["result"] == "PASS" else 2
    if not args.preflight_only:
        raise SystemExit(
            "Choose --preflight-only or provide --saved-candidate"
        )
    blueprint_path = args.blueprint.resolve()
    amendment_path = args.amendment.resolve()
    parity_amendment_path = args.parity_amendment.resolve()
    stitch_amendment_path = args.stitch_amendment.resolve()
    result = build_validation(
        blueprint_path,
        amendment_path,
        parity_amendment_path,
        stitch_amendment_path,
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
        "stitch_result": result["stitch_validation"]["result"],
        "step12_result": result["step12_resume_preflight"]["result"],
        "block_code": result["step12_resume_preflight"]["block_code"],
    }, sort_keys=True))
    return 0 if result["step12_resume_preflight"]["result"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
