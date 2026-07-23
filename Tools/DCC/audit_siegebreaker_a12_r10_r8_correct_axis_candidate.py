#!/usr/bin/env python3
"""Independently audit one opened A12 R10 R8 correct-axis candidate."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import bpy


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ASSET_ROOT = ROOT / "docs/assets/blueprints" / ASSET
CONTRACT_ID = "SB-A12-R10-R8-CORRECT-AXIS-TWO-HAMMER-A01"
CONTRACT = (
    ASSET_ROOT
    / "steps/A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01_CONTRACT.md"
)
SCAN_MANIFEST = (
    ASSET_ROOT
    / "manifests/A12_R10_R8_FULL_SCANLINE_DIMENSION_COMPATIBILITY_A01.json"
)
COMPARISON_BOARD = (
    ASSET_ROOT
    / "review/A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01"
    / "A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01_REVIEW.png"
)

TARGET_DIMENSIONS = (
    float(Fraction(104040, 1063)),
    float(Fraction(24579450, 517681)),
    170.0,
)
STATIONS = {
    "A": (600, 132.0),
    "C": (
        670,
        float(
            Fraction(132)
            - (670 - 600)
            * (
                (
                    Fraction(132)
                    - (
                        Fraction(18)
                        + (1150 - 1110) * Fraction(18, 1271 - 1150)
                        + Fraction(42)
                    )
                )
                / (955 - 600)
            )
        ),
    ),
    "H1": (
        870,
        float(
            Fraction(132)
            - (870 - 600)
            * (
                (
                    Fraction(132)
                    - (
                        Fraction(18)
                        + (1150 - 1110) * Fraction(18, 1271 - 1150)
                        + Fraction(42)
                    )
                )
                / (955 - 600)
            )
        ),
    ),
    "H8": (
        955,
        float(
            Fraction(18)
            + (1150 - 1110) * Fraction(18, 1271 - 1150)
            + Fraction(42)
        ),
    ),
    "U1": (
        1110,
        float(Fraction(18) + (1150 - 1110) * Fraction(18, 1271 - 1150)),
    ),
    "U3": (1150, 18.0),
    "L4": (1220, float((1271 - 1220) * Fraction(18, 1271 - 1150))),
    "TERMINAL": (1271, 0.0),
}
CANDIDATES = {
    "rune": {
        "interval": [557, 668],
        "source_top": 166,
        "manifest": "A12_R10_R8_CORRECT_AXIS_RUNE_SIDE_A01_VALIDATION.json",
        "audit": "A12_R10_R8_CORRECT_AXIS_RUNE_SIDE_A01_INDEPENDENT_AUDIT.json",
    },
    "metal": {
        "interval": [418, 557],
        "source_top": 170,
        "manifest": "A12_R10_R8_CORRECT_AXIS_METAL_CENTER_A01_VALIDATION.json",
        "audit": "A12_R10_R8_CORRECT_AXIS_METAL_CENTER_A01_INDEPENDENT_AUDIT.json",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(a: float, b: float, tolerance: float = 1.0e-6) -> bool:
    return abs(a - b) <= tolerance


def bounds(objects: list[bpy.types.Object]) -> dict[str, list[float]]:
    points = [
        obj.matrix_world @ vertex.co
        for obj in objects
        for vertex in obj.data.vertices
    ]
    minimum = [min(point[axis] for point in points) for axis in range(3)]
    maximum = [max(point[axis] for point in points) for axis in range(3)]
    return {
        "minimum_cm": minimum,
        "maximum_cm": maximum,
        "dimensions_cm": [
            maximum[index] - minimum[index] for index in range(3)
        ],
    }


def rz180_vertex_symmetry(
    objects: list[bpy.types.Object],
) -> dict[str, object]:
    failures: list[dict[str, object]] = []
    checked = 0
    for obj in objects:
        coordinates = {
            tuple(round(value, 6) for value in (obj.matrix_world @ vertex.co))
            for vertex in obj.data.vertices
        }
        for x, y, z in coordinates:
            checked += 1
            target = (round(-x, 6), round(-y, 6), round(z, 6))
            if target not in coordinates:
                if len(failures) < 20:
                    failures.append(
                        {"object": obj.name, "vertex": [x, y, z], "missing": target}
                    )
    return {
        "pass": not failures,
        "vertices_checked": checked,
        "failure_count_reported": len(failures),
        "failures": failures,
    }


def profile_station_audit(handle: bpy.types.Object) -> dict[str, object]:
    profile = json.loads(handle["Aerathea.ProfileJSON"])
    by_edge = {int(record["source_edge"]): record for record in profile}
    stations: dict[str, object] = {}
    station_pass = True
    for name, (edge, expected_z) in STATIONS.items():
        record = by_edge.get(edge)
        actual_z = None if record is None else float(record["z_cm"])
        passed = actual_z is not None and close(actual_z, expected_z, 1.0e-7)
        stations[name] = {
            "source_edge": edge,
            "sampled_source_row": (
                None if record is None else int(record["source_row"])
            ),
            "expected_z_cm": expected_z,
            "actual_z_cm": actual_z,
            "pass": passed,
        }
        station_pass = station_pass and passed

    edges = [int(record["source_edge"]) for record in profile]
    z_values = [float(record["z_cm"]) for record in profile]
    source_ordered = edges == sorted(edges)
    z_ordered = all(
        z_values[index] >= z_values[index + 1] - 1.0e-9
        for index in range(len(z_values) - 1)
    )
    shaft_records = [
        record
        for record in profile
        if 670 <= int(record["source_edge"]) <= 870
    ]
    shaft_radius_error = max(
        abs(float(record["radius_cm"]) - 2.5) for record in shaft_records
    )
    maximum_radius = max(float(record["radius_cm"]) for record in profile)
    checks = {
        "station_z_values_exact": station_pass,
        "profile_starts_at_A_edge_600": edges[0] == 600,
        "profile_ends_at_terminal_edge_1271": edges[-1] == 1271,
        "source_edges_monotonic": source_ordered,
        "z_values_monotonic": z_ordered,
        "shaft_C_to_H1_radius_2_5_cm": shaft_radius_error <= 1.0e-7,
        "grip_H8_to_U1_is_42_cm": close(
            float(by_edge[955]["z_cm"]) - float(by_edge[1110]["z_cm"]),
            42.0,
            1.0e-7,
        ),
        "pommel_U3_to_terminal_is_18_cm": close(
            float(by_edge[1150]["z_cm"]) - float(by_edge[1271]["z_cm"]),
            18.0,
            1.0e-7,
        ),
        "lower_maximum_diameter_is_11_cm": close(
            2.0 * maximum_radius, 11.0, 1.0e-7
        ),
    }
    return {
        "checks": checks,
        "stations": stations,
        "profile_ring_count": len(profile),
        "shaft_maximum_radius_error_cm": shaft_radius_error,
        "profile_maximum_radius_cm": maximum_radius,
        "pass": all(checks.values()),
    }


def main() -> None:
    scene = bpy.context.scene
    kind = str(scene.get("Aerathea.CandidateKind", ""))
    if kind not in CANDIDATES:
        raise RuntimeError(f"Unknown or absent candidate kind: {kind!r}")
    candidate = CANDIDATES[kind]
    manifest_path = ASSET_ROOT / "manifests" / candidate["manifest"]
    audit_path = ASSET_ROOT / "manifests" / candidate["audit"]
    manifest = json.loads(manifest_path.read_text())
    scan = json.loads(SCAN_MANIFEST.read_text())

    objects = [
        obj for obj in scene.objects if obj.type == "MESH"
    ]
    components = {
        str(obj.get("Aerathea.ComponentID", "")): obj for obj in objects
    }
    head = components.get("C00_CORRECT_AXIS_HEAD")
    handle = components.get("C06_C11_CORRECTED_HANDLE")
    if head is None or handle is None:
        raise RuntimeError("Required head or handle component is absent")

    measured_bounds = bounds(objects)
    symmetry = rz180_vertex_symmetry(objects)
    profile = profile_station_audit(handle)

    source_checks: dict[str, bool] = {}
    for view in ("front", "back", "right"):
        record = manifest["source_authority"]["sources"][view]
        scan_record = scan["sources"][view]
        source_path = ROOT / record["path"]
        capture_path = ROOT / record["capture_path"]
        source_checks[f"{view}_source_exists"] = source_path.is_file()
        source_checks[f"{view}_source_hash_matches_manifest"] = (
            source_path.is_file() and sha256(source_path) == record["sha256"]
        )
        source_checks[f"{view}_source_hash_matches_scan_authority"] = (
            record["sha256"] == scan_record["file_sha256"]
        )
        source_checks[f"{view}_scanline_capture_exists"] = capture_path.is_file()
        source_checks[f"{view}_scanline_capture_hash_matches"] = (
            capture_path.is_file()
            and sha256(capture_path) == record["capture_sha256"]
        )
        source_checks[f"{view}_exact_rgba_replay_declared"] = bool(
            record["exact_rgba_replay"]
        )

    output_checks: dict[str, bool] = {}
    for name, relative_path in manifest["outputs"].items():
        output_path = ROOT / relative_path
        output_checks[f"{name}_exists"] = output_path.is_file()
        output_checks[f"{name}_hash_matches"] = (
            output_path.is_file()
            and sha256(output_path) == manifest["output_hashes"][name]
        )

    dimensions = measured_bounds["dimensions_cm"]
    cameras = [obj for obj in scene.objects if obj.type == "CAMERA"]
    camera_scales = sorted(float(camera.data.ortho_scale) for camera in cameras)
    checks = {
        "contract_exists": CONTRACT.is_file(),
        "contract_id_exact": str(scene.get("Aerathea.ContractID", "")) == CONTRACT_ID,
        "candidate_kind_exact": manifest["candidate_kind"] == kind,
        "two_mesh_components_only": len(objects) == 2 and len(components) == 2,
        "source_axis_is_right_depth_Y": (
            str(scene.get("Aerathea.SourceHalfAxis", ""))
            == "right-image depth half Y<=0"
            and str(head.get("Aerathea.SourceHalfAxis", "")) == "Y<=0"
        ),
        "bisection_source_edge_is_557": (
            int(scene.get("Aerathea.BisectionSourceEdge", -1)) == 557
            and int(head.get("Aerathea.BisectionSourceEdge", -1)) == 557
        ),
        "source_interval_exact": json.loads(head["Aerathea.SourceInterval"])
        == candidate["interval"],
        "source_top_exact": int(head["Aerathea.SourceTopRow"])
        == candidate["source_top"],
        "one_Rz180_completion": (
            int(scene.get("Aerathea.WholeTransformCount", 0)) == 1
            and all(
                int(obj.get("Aerathea.WholeTransformCount", 0)) == 1
                and bool(obj.get("Aerathea.Rz180Executed", False))
                for obj in objects
            )
        ),
        "Rz180_vertex_symmetry": bool(symmetry["pass"]),
        "no_prior_candidate_geometry": (
            int(scene.get("Aerathea.PriorCandidateGeometryInputs", -1)) == 0
            and all(
                int(obj.get("Aerathea.PriorCandidateGeometryInputs", -1)) == 0
                for obj in objects
            )
        ),
        "handle_top_is_A_132_cm": (
            close(float(scene.get("Aerathea.HandleTopZCm", -1.0)), 132.0)
            and close(float(handle["Aerathea.HandleTopZCm"]), 132.0)
            and bool(handle["Aerathea.HandleIncludesUpperCoupler"])
        ),
        "previous_missing_span_is_recorded": close(
            float(handle["Aerathea.PreviousMissingSpanCm"]),
            float(Fraction(33432, 1111)),
            1.0e-7,
        ),
        "cylinder_wrap_formula_exact": (
            bool(scene.get("Aerathea.PiOver2HaftWrap", False))
            and bool(handle["Aerathea.PiOver2CylinderWrap"])
            and str(handle["Aerathea.ThetaFormula"]) == "-pi/2+pi*U"
            and str(handle["Aerathea.SurfaceFormula"])
            == "X=r(z)cos(theta);Y=r(z)sin(theta)"
        ),
        "handle_profile_pass": bool(profile["pass"]),
        "width_exact": close(dimensions[0], TARGET_DIMENSIONS[0], 3.0e-5),
        "depth_exact": close(dimensions[1], TARGET_DIMENSIONS[1], 3.0e-5),
        "height_exact": close(dimensions[2], TARGET_DIMENSIONS[2], 3.0e-5),
        "three_review_cameras_exact": camera_scales == [188.0, 188.0, 198.0],
        "no_mesh_modifiers": all(len(obj.modifiers) == 0 for obj in objects),
        "all_builder_gates_declared_pass": (
            manifest["technical_result"] == "PASS"
            and all(manifest["technical_gates"].values())
        ),
        "comparison_board_exists": COMPARISON_BOARD.is_file(),
        "comparison_board_hash_matches": (
            COMPARISON_BOARD.is_file()
            and sha256(COMPARISON_BOARD)
            == manifest["comparison_board_sha256"]
        ),
        "no_Unreal_authority": (
            manifest["unreal_authority"] is False
            and manifest["fully_game_ready"] is False
        ),
        **source_checks,
        **output_checks,
    }
    result = "PASS" if all(checks.values()) else "FAIL"
    audit = {
        "schema": "aerathea.siegebreaker.r8_correct_axis_independent_audit.v1",
        "asset": ASSET,
        "candidate_kind": kind,
        "contract_id": CONTRACT_ID,
        "artifact_status": (
            "DCC source candidate pending Flamestrike comparison"
            if result == "PASS"
            else "invalid"
        ),
        "audit_independence": {
            "opened_blend": bpy.data.filepath,
            "builder_script_not_imported": True,
            "geometry_bounds_recomputed": True,
            "Rz180_symmetry_recomputed_from_vertices": True,
            "handle_station_formula_recomputed_from_exact_fractions": True,
            "output_hashes_recomputed": True,
        },
        "measured_bounds": measured_bounds,
        "expected_dimensions_cm": list(TARGET_DIMENSIONS),
        "Rz180_symmetry": symmetry,
        "handle_profile": profile,
        "checks": checks,
        "pass_count": sum(checks.values()),
        "check_count": len(checks),
        "result": result,
    }
    audit_path.write_text(json.dumps(audit, indent=2) + "\n")
    print(json.dumps({
        "result": result,
        "candidate_kind": kind,
        "audit": str(audit_path),
        "gates": f"{audit['pass_count']}/{audit['check_count']}",
        "failures": [name for name, passed in checks.items() if not passed],
    }, indent=2))
    if result != "PASS":
        raise RuntimeError(
            "Independent audit failed: "
            + ", ".join(name for name, passed in checks.items() if not passed)
        )


if __name__ == "__main__":
    main()
