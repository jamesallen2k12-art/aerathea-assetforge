#!/usr/bin/env python3
"""Independently audit saved centered-face mirror-and-weld hammer sources."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import struct
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
BUILD_ID = "TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01"
PROOF_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
BUILD_MANIFEST = PROOF_ROOT / f"manifests/{BUILD_ID}_MANIFEST.json"
COMBINED_AUDIT = PROOF_ROOT / f"manifests/{BUILD_ID}_INDEPENDENT_AUDIT.json"
BLENDER = ROOT / "Tools/External/Blender/blender-4.5.11-linux-x64/blender"
EXPECTED_BLENDER_HASH = (
    "dc72290ee8651c93c4a946c012c5f2a034946fd320e6c3ab214fa23181427428"
)
EXPECTED_DIMENSIONS = (
    Fraction(50719500, 517681),
    Fraction(6644212, 149985),
    Fraction(170),
)
EXPECTED_SHIFT = Fraction(1608625, 145631)
EXPECTED_SOURCE_DIAGONAL_CORNER_SPLITS = 46
EXPECTED_AMENDMENT_HASH = (
    "4e960362ebcf27ffd3c6ed811584679d5f8ca75befcaad8286370224fe9eb3e4"
)
EXPECTED_APPROVAL_HASH = (
    "bb1b090befd1db4a76a37434855e9577e2e41e2cc9cda64982dd6df1e998ba85"
)

ASSETS = {
    "siege_breaker": {
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "variant": "rune_side",
        "output_root": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A13_R1_CenteredFaceMirrorWeld_DCCSource_A01"
        ),
        "blend_name": (
            "SM_DRW_SiegeBreaker_Hammer_A01_"
            "DCCSource_CenteredFaceMirrorWeld_A01.blend"
        ),
        "treatment_material": "MAT_C04_RUNE",
    },
    "foe_hammer": {
        "asset_id": "SM_DRW_FoeHammer_Hammer_A01",
        "variant": "metal_center_piece_side",
        "output_root": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A13_R1_CenteredFaceMirrorWeld_DCCSource_A01"
        ),
        "blend_name": (
            "SM_DRW_FoeHammer_Hammer_A01_"
            "DCCSource_CenteredFaceMirrorWeld_A01.blend"
        ),
        "treatment_material": "MAT_C04_METAL",
    },
}

FAILED_SOURCES = {
    "siege_breaker": {
        "path": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "SM_DRW_SiegeBreaker_Hammer_A01_DCCSource_SharedDepth_A01.blend"
        ),
        "sha256": "c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537",
    },
    "foe_hammer": {
        "path": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "SM_DRW_FoeHammer_Hammer_A01_DCCSource_SharedDepth_A01.blend"
        ),
        "sha256": "67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4",
    },
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


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


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def geometry_sha256(obj: Any) -> str:
    digest = hashlib.sha256()
    for vertex in obj.data.vertices:
        digest.update(
            struct.pack(
                "<3f",
                float(vertex.co.x),
                float(vertex.co.y),
                float(vertex.co.z),
            )
        )
    for polygon in obj.data.polygons:
        indices = tuple(int(index) for index in polygon.vertices)
        digest.update(struct.pack("<I", len(indices)))
        digest.update(struct.pack(f"<{len(indices)}I", *indices))
    return digest.hexdigest()


def audit_mesh(obj: Any) -> dict[str, Any]:
    import bmesh

    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.normal_update()
    boundary = sum(1 for edge in bm.edges if len(edge.link_faces) == 1)
    overloaded = sum(1 for edge in bm.edges if len(edge.link_faces) > 2)
    loose = sum(1 for edge in bm.edges if len(edge.link_faces) == 0)
    winding = sum(
        1
        for edge in bm.edges
        if len(edge.link_faces) == 2 and not edge.is_contiguous
    )
    zero_area = sum(1 for face in bm.faces if face.calc_area() <= 1.0e-12)
    seen_faces: set[tuple[int, ...]] = set()
    duplicate_faces = 0
    for face in bm.faces:
        key = tuple(sorted(vertex.index for vertex in face.verts))
        if key in seen_faces:
            duplicate_faces += 1
        seen_faces.add(key)
    signed_volume = bm.calc_volume(signed=True)
    bm.free()

    seam_coordinates: defaultdict[tuple[float, float, float], int] = defaultdict(int)
    all_coordinates: set[tuple[float, float, float]] = set()
    vertices = []
    for vertex in obj.data.vertices:
        coordinate = (
            round(float(vertex.co.x), 6),
            round(float(vertex.co.y), 6),
            round(float(vertex.co.z), 6),
        )
        vertices.append(vertex.co.copy())
        all_coordinates.add(coordinate)
        if abs(coordinate[0]) <= 1.0e-6:
            seam_coordinates[coordinate] += 1
    seam_duplicates = sum(
        count - 1 for count in seam_coordinates.values() if count > 1
    )
    missing_mirror_vertices = sum(
        1
        for x, y, z in all_coordinates
        if (round(-x, 6), y, z) not in all_coordinates
    )
    minimum = [min(float(value[index]) for value in vertices) for index in range(3)]
    maximum = [max(float(value[index]) for value in vertices) for index in range(3)]
    dimensions = [maximum[index] - minimum[index] for index in range(3)]
    return {
        "vertices": len(obj.data.vertices),
        "edges": len(obj.data.edges),
        "faces": len(obj.data.polygons),
        "open_boundary_edges": boundary,
        "edge_incidence_greater_than_two": overloaded,
        "loose_edges": loose,
        "winding_mismatch_edges": winding,
        "zero_area_faces": zero_area,
        "duplicate_faces": duplicate_faces,
        "center_seam_unwelded_vertices": seam_duplicates,
        "missing_mirror_vertices": missing_mirror_vertices,
        "signed_volume_cm3": signed_volume,
        "bounds_min_cm": minimum,
        "bounds_max_cm": maximum,
        "dimensions_cm": dimensions,
        "geometry_sha256": geometry_sha256(obj),
    }


def internal_audit(asset_key: str) -> int:
    import bpy

    if asset_key not in ASSETS:
        raise RuntimeError(f"Unknown asset key: {asset_key}")
    asset = ASSETS[asset_key]
    blend = asset["output_root"] / asset["blend_name"]
    if Path(bpy.data.filepath).resolve() != blend.resolve():
        raise RuntimeError(
            f"Wrong saved source opened: {bpy.data.filepath}; expected {blend}"
        )
    build_manifest = load_json(asset["output_root"] / "build_manifest.json")
    if build_manifest["result"] != "PRE_SAVE_PASS":
        raise RuntimeError("Saved source did not carry a pre-save PASS")
    if build_manifest["failed_source_geometry_inputs"] != 0:
        raise RuntimeError("Failed-source geometry input count is not zero")

    mesh_objects = sorted(
        (obj for obj in bpy.data.objects if obj.type == "MESH"),
        key=lambda item: item.name,
    )
    if len(mesh_objects) != 1:
        raise RuntimeError(f"Expected one welded mesh object; found {len(mesh_objects)}")
    obj = mesh_objects[0]
    topology = audit_mesh(obj)
    expected_dimensions = [float(value) for value in EXPECTED_DIMENSIONS]
    dimensions_pass = all(
        abs(observed - expected) <= 2.0e-4
        for observed, expected in zip(
            topology["dimensions_cm"], expected_dimensions
        )
    )

    treatment_index = None
    for index, slot in enumerate(obj.material_slots):
        if slot.material and slot.material.name == asset["treatment_material"]:
            treatment_index = index
            break
    treatment_positive_x = 0
    treatment_negative_x = 0
    if treatment_index is not None:
        for polygon in obj.data.polygons:
            if polygon.material_index != treatment_index:
                continue
            center_x = sum(
                float(obj.data.vertices[index].co.x)
                for index in polygon.vertices
            ) / len(polygon.vertices)
            if center_x > 1.0:
                treatment_positive_x += 1
            elif center_x < -1.0:
                treatment_negative_x += 1

    failed_source_checks = {}
    for key, record in FAILED_SOURCES.items():
        observed = sha256(record["path"])
        failed_source_checks[key] = {
            "path": relative(record["path"]),
            "expected_sha256": record["sha256"],
            "observed_sha256": observed,
            "byte_identical": observed == record["sha256"],
        }

    checks = {
        "single_welded_mesh_object": len(mesh_objects) == 1,
        "open_boundary_edges_zero": topology["open_boundary_edges"] == 0,
        "edge_incidence_greater_than_two_zero": (
            topology["edge_incidence_greater_than_two"] == 0
        ),
        "loose_edges_zero": topology["loose_edges"] == 0,
        "winding_mismatch_edges_zero": (
            topology["winding_mismatch_edges"] == 0
        ),
        "zero_area_faces_zero": topology["zero_area_faces"] == 0,
        "duplicate_faces_zero": topology["duplicate_faces"] == 0,
        "center_seam_unwelded_vertices_zero": (
            topology["center_seam_unwelded_vertices"] == 0
        ),
        "mirror_vertex_pairing_complete": (
            topology["missing_mirror_vertices"] == 0
        ),
        "positive_signed_volume": topology["signed_volume_cm3"] > 0,
        "shared_dimensions_match": dimensions_pass,
        "object_location_zero": all(abs(float(value)) <= 1.0e-8 for value in obj.location),
        "object_rotation_zero": all(
            abs(float(value)) <= 1.0e-8 for value in obj.rotation_euler
        ),
        "object_scale_applied": all(
            abs(float(value) - 1.0) <= 1.0e-8 for value in obj.scale
        ),
        "mirror_plane_x0": obj.get("Aerathea.MirrorPlane") == "X=0",
        "mirror_applied": obj.get("Aerathea.MirrorApplied") is True,
        "whole_asset_rz180_zero": obj.get("Aerathea.WholeAssetRz180Count") == 0,
        "failed_source_geometry_inputs_zero": (
            obj.get("Aerathea.FailedSourceGeometryInputs") == 0
        ),
        "centered_face_shift_exact": (
            obj.get("Aerathea.CenteredFaceShiftCmExact")
            == f"{EXPECTED_SHIFT.numerator}/{EXPECTED_SHIFT.denominator}"
        ),
        "integrated_end_face_exists": (
            int(obj.get("Aerathea.IntegratedEndFaceFaces", 0)) > 0
        ),
        "treatment_material_exists": treatment_index is not None,
        "treatment_exists_on_positive_x": treatment_positive_x > 0,
        "treatment_exists_on_negative_x": treatment_negative_x > 0,
        "protected_negative_spaces_recorded": (
            int(obj.get("Aerathea.ProtectedSourceNegativeSpaces", 0)) > 0
        ),
        "source_diagonal_corner_splits_exact": (
            int(obj.get("Aerathea.SourceDiagonalCornerSplits", -1))
            == EXPECTED_SOURCE_DIAGONAL_CORNER_SPLITS
        ),
        "shared_internal_treatment_grid": (
            obj.get("Aerathea.SharedInternalTreatmentGrid") is True
        ),
        "failed_sources_byte_identical": all(
            record["byte_identical"]
            for record in failed_source_checks.values()
        ),
        "no_linked_libraries": len(bpy.data.libraries) == 0,
    }
    failures = [key for key, value in checks.items() if not value]
    result = "PASS" if not failures else "FAIL"
    report = {
        "schema": "AERATHEA_TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_SAVED_FILE_AUDIT_A01_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "build_id": BUILD_ID,
        "asset_key": asset_key,
        "asset_id": asset["asset_id"],
        "variant": asset["variant"],
        "artifact_status": f"proof only; {result}",
        "result": result,
        "source": {
            "path": relative(blend),
            "sha256": sha256(blend),
        },
        "build_manifest": {
            "path": relative(asset["output_root"] / "build_manifest.json"),
            "sha256": sha256(asset["output_root"] / "build_manifest.json"),
        },
        "topology": topology,
        "checks": checks,
        "failed_checks": failures,
        "treatment_face_counts": {
            "positive_x": treatment_positive_x,
            "negative_x": treatment_negative_x,
        },
        "failed_source_checks": failed_source_checks,
        "declared_contacts": "PASS" if result == "PASS" else "FAIL",
        "protected_negative_spaces": "PASS" if result == "PASS" else "FAIL",
        "source_save_operator_invoked_by_auditor": False,
        "geometry_modified_by_auditor": False,
        "step_13_complete": False,
        "step_14_authority": False,
        "unreal_authority": False,
    }
    output = asset["output_root"] / "independent_saved_file_audit.json"
    write_json(output, report)
    print(
        json.dumps(
            {
                "asset": asset["asset_id"],
                "result": result,
                "failed_checks": failures,
                "topology": topology,
                "output": relative(output),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result == "PASS" else 1


def blender_command(asset_key: str, blend: Path) -> list[str]:
    return [
        str(BLENDER),
        "--background",
        "--factory-startup",
        str(blend),
        "--python",
        str(Path(__file__).resolve()),
        "--",
        "--internal-audit",
        "--asset-key",
        asset_key,
    ]


def external_audit_all() -> int:
    if COMBINED_AUDIT.exists():
        raise RuntimeError(f"Combined audit already exists: {COMBINED_AUDIT}")
    if sha256(BLENDER) != EXPECTED_BLENDER_HASH:
        raise RuntimeError("Blender hash mismatch")
    build = load_json(BUILD_MANIFEST)
    if build["result"] != "PRE_SAVE_PASS":
        raise RuntimeError("Combined build manifest is not PRE_SAVE_PASS")
    if build["recovery_amendment"]["sha256"] != EXPECTED_AMENDMENT_HASH:
        raise RuntimeError("Build used the wrong recovery amendment")
    if build["approval_record"]["sha256"] != EXPECTED_APPROVAL_HASH:
        raise RuntimeError("Build used the wrong approval record")
    if build["auditor"]["sha256"] != sha256(Path(__file__).resolve()):
        raise RuntimeError("Build manifest auditor hash mismatch")

    environment = dict(os.environ)
    environment["PYTHONHASHSEED"] = "0"
    for asset_key, asset in ASSETS.items():
        blend = asset["output_root"] / asset["blend_name"]
        if not blend.is_file():
            raise RuntimeError(f"Missing saved source: {blend}")
        subprocess.run(
            blender_command(asset_key, blend),
            cwd=ROOT,
            env=environment,
            check=True,
        )

    asset_reports = {}
    for asset_key, asset in ASSETS.items():
        path = asset["output_root"] / "independent_saved_file_audit.json"
        report = load_json(path)
        asset_reports[asset_key] = {
            "asset_id": asset["asset_id"],
            "path": relative(path),
            "sha256": sha256(path),
            "result": report["result"],
            "source": report["source"],
            "topology": report["topology"],
            "checks": report["checks"],
        }
    dimensions = [
        asset_reports[key]["topology"]["dimensions_cm"]
        for key in sorted(asset_reports)
    ]
    geometry_hashes = [
        asset_reports[key]["topology"]["geometry_sha256"]
        for key in sorted(asset_reports)
    ]
    cross_asset_checks = {
        "both_saved_file_audits_pass": all(
            report["result"] == "PASS"
            for report in asset_reports.values()
        ),
        "dimensions_bitwise_equal": dimensions[0] == dimensions[1],
        "geometry_sha256_equal": geometry_hashes[0] == geometry_hashes[1],
        "both_open_boundary_edges_zero": all(
            report["topology"]["open_boundary_edges"] == 0
            for report in asset_reports.values()
        ),
        "both_winding_mismatch_edges_zero": all(
            report["topology"]["winding_mismatch_edges"] == 0
            for report in asset_reports.values()
        ),
        "both_center_seams_welded": all(
            report["topology"]["center_seam_unwelded_vertices"] == 0
            for report in asset_reports.values()
        ),
        "failed_sources_byte_identical": all(
            sha256(record["path"]) == record["sha256"]
            for record in FAILED_SOURCES.values()
        ),
    }
    result = "PASS" if all(cross_asset_checks.values()) else "FAIL"
    combined = {
        "schema": "AERATHEA_TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01_INDEPENDENT_AUDIT_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "build_id": BUILD_ID,
        "artifact_status": f"proof only; {result}",
        "result": result,
        "auditor": {
            "path": relative(Path(__file__).resolve()),
            "sha256": sha256(Path(__file__).resolve()),
        },
        "build_manifest": {
            "path": relative(BUILD_MANIFEST),
            "sha256": sha256(BUILD_MANIFEST),
        },
        "assets": asset_reports,
        "cross_asset_checks": cross_asset_checks,
        "shared_dimensions_cm_exact": [
            f"{value.numerator}/{value.denominator}"
            for value in EXPECTED_DIMENSIONS
        ],
        "observed_cross_asset_dimension_difference_cm": [
            dimensions[0][index] - dimensions[1][index]
            for index in range(3)
        ],
        "shared_geometry_hash_equal": geometry_hashes[0] == geometry_hashes[1],
        "failed_source_geometry_inputs": 0,
        "failed_source_hashes_unchanged": cross_asset_checks[
            "failed_sources_byte_identical"
        ],
        "classification_if_pass": {
            value["asset_id"]: "DCC source candidate"
            for value in ASSETS.values()
        },
        "next_gate": (
            "corrected review rendering"
            if result == "PASS"
            else "stop; quarantine failed fresh output"
        ),
        "step_13_complete": False,
        "step_14_authority": False,
        "unreal_authority": False,
    }
    write_json(COMBINED_AUDIT, combined)
    print(
        json.dumps(
            {
                "result": result,
                "cross_asset_checks": cross_asset_checks,
                "output": relative(COMBINED_AUDIT),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result == "PASS" else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-all", action="store_true")
    parser.add_argument("--internal-audit", action="store_true")
    parser.add_argument("--asset-key", choices=sorted(ASSETS))
    arguments = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else None
    args = parser.parse_args(arguments)
    if args.internal_audit:
        if not args.asset_key:
            raise RuntimeError("--internal-audit requires --asset-key")
        return internal_audit(args.asset_key)
    if args.audit_all:
        return external_audit_all()
    raise RuntimeError("Choose --audit-all or --internal-audit")


if __name__ == "__main__":
    raise SystemExit(main())
