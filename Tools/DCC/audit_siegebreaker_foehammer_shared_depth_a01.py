#!/usr/bin/env python3
"""Independent saved-file and cross-asset audit for the shared-depth twins.

This auditor does not import the builder and does not read any canonical
geometry emitted by a builder.  It opens each newly saved blend, derives
observed geometry facts from the mesh datablocks, and compares the twins.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import struct
import subprocess
import sys
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
BUILD_ID = "FRESH_TWIN_DCC_SOURCE_BUILDER_A01"
PROOF_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
BLUEPRINT = PROOF_ROOT / "manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01.json"
BLUEPRINT_LOCK = (
    PROOF_ROOT
    / "manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK.json"
)
BUILD_APPROVAL = (
    PROOF_ROOT / "steps/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_APPROVAL_RECORD.md"
)
COMBINED_MANIFEST = (
    PROOF_ROOT / "manifests/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_MANIFEST.json"
)
CROSS_AUDIT = (
    PROOF_ROOT
    / "manifests/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_INDEPENDENT_AUDIT.json"
)
BUILDER = ROOT / "Tools/DCC/build_siegebreaker_foehammer_shared_depth_a01.py"
BLENDER = ROOT / "Tools/External/Blender/blender-4.5.11-linux-x64/blender"

ASSETS = {
    "siege_breaker": {
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "display_name": "Siege Breaker",
        "variant": "rune_side",
        "local_half": Fraction(9435, 548),
        "output_root": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01"
        ),
    },
    "foe_hammer": {
        "asset_id": "SM_DRW_FoeHammer_Hammer_A01",
        "display_name": "Foe Hammer",
        "variant": "metal_center_piece_side",
        "local_half": Fraction(11815, 548),
        "output_root": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01"
        ),
    },
}

EXPECTED_DIMENSIONS = (
    Fraction(50719500, 517681),
    Fraction(6644212, 149985),
    Fraction(170),
)
COMMON_HALF_DEPTH = Fraction(3322106, 149985)
FLOAT32_BOUND_TOLERANCE_CM = 2.0e-5

EXPECTED_HASHES = {
    BLUEPRINT: "efdbd8795dff2031fcde9e734868ff4c617dc37ad1e7b3743c3727daea981d58",
    BLUEPRINT_LOCK: "6889b826481e5e11dd10775f2b81467b1014687b7fda9ebbff62d519bfff09bc",
    BUILD_APPROVAL: "8b59685cf27656805ecf73385ab980c1d96dec2686ac1928f6f547f4dad787ef",
    BLENDER: "dc72290ee8651c93c4a946c012c5f2a034946fd320e6c3ab214fa23181427428",
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


def qstr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def verify_external_authority() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    checks = []
    for path, expected in EXPECTED_HASHES.items():
        observed = sha256(path) if path.is_file() else None
        result = "PASS" if observed == expected else "FAIL"
        checks.append(
            {
                "path": relative(path),
                "expected_sha256": expected,
                "observed_sha256": observed,
                "result": result,
            }
        )
        if result != "PASS":
            raise RuntimeError(f"Authority hash mismatch: {relative(path)}")
    combined = load_json(COMBINED_MANIFEST)
    observed_builder_sha = sha256(BUILDER)
    if combined["builder"]["sha256"] != observed_builder_sha:
        raise RuntimeError(
            "Builder changed after the fresh build; audit is fail-closed"
        )
    if combined["quarantined_geometry_read_count"] != 0:
        raise RuntimeError("Build manifest reports quarantined geometry input")
    if combined["input_geometry_files"]:
        raise RuntimeError("Build manifest reports an input geometry file")
    return combined, checks


def custom_properties(owner: Any) -> dict[str, Any]:
    return {
        key: owner[key]
        for key in owner.keys()
        if key != "_RNA_UI"
    }


def mesh_world_vertices(obj: Any) -> list[tuple[float, float, float]]:
    return [
        tuple(obj.matrix_world @ vertex.co)
        for vertex in obj.data.vertices
    ]


def saved_shared_base_hash(objects: list[Any]) -> str:
    digest = hashlib.sha256()
    shared = sorted(
        (
            obj
            for obj in objects
            if not bool(obj.get("Aerathea.VariantLocalC04", False))
        ),
        key=lambda item: item.name,
    )
    for obj in shared:
        digest.update(obj.name.encode("utf-8") + b"\0")
        for key in (
            "Aerathea.Component",
            "Aerathea.SourceOwner",
            "Aerathea.EquationId",
            "Aerathea.Occurrence",
        ):
            digest.update(
                (key + "=" + str(obj.get(key, "")) + "\n").encode("utf-8")
            )
        for point in mesh_world_vertices(obj):
            digest.update(struct.pack(">ddd", *point))
        for polygon in obj.data.polygons:
            digest.update(struct.pack(">I", len(polygon.vertices)))
            for index in polygon.vertices:
                digest.update(struct.pack(">I", int(index)))
        materials = [
            (
                slot.material.name if slot.material else "",
                tuple(slot.material.diffuse_color)
                if slot.material
                else (),
            )
            for slot in obj.material_slots
        ]
        digest.update(repr(materials).encode("utf-8"))
    return digest.hexdigest()


def inspect_loaded_blend(
    bpy: Any, asset: dict[str, Any], combined: dict[str, Any]
) -> dict[str, Any]:
    scene = bpy.context.scene
    objects = sorted(
        (obj for obj in bpy.data.objects if obj.type == "MESH"),
        key=lambda item: item.name,
    )
    if not objects:
        raise RuntimeError("Saved file contains no mesh objects")
    points = [
        point for obj in objects for point in mesh_world_vertices(obj)
    ]
    minimum = [
        min(point[axis] for point in points) for axis in range(3)
    ]
    maximum = [
        max(point[axis] for point in points) for axis in range(3)
    ]
    dimensions = [
        maximum[axis] - minimum[axis] for axis in range(3)
    ]
    expected_decimal = [float(value) for value in EXPECTED_DIMENSIONS]
    errors = [
        abs(dimensions[axis] - expected_decimal[axis])
        for axis in range(3)
    ]
    bound_result = (
        "PASS"
        if all(error <= FLOAT32_BOUND_TOLERANCE_CM for error in errors)
        else "FAIL"
    )

    local_extent_objects = [
        obj
        for obj in objects
        if bool(obj.get("Aerathea.LocalExtentAuditOwner", False))
    ]
    if len(local_extent_objects) != 2:
        raise RuntimeError(
            "Expected one local-extent face record plus its Rz180 occurrence"
        )
    local_points = [
        point
        for obj in local_extent_objects
        for point in mesh_world_vertices(obj)
    ]
    visible_face_half_observed = max(
        abs(point[1]) for point in local_points
    )
    visible_face_inside_domain = (
        visible_face_half_observed
        <= float(asset["local_half"]) + FLOAT32_BOUND_TOLERANCE_CM
    )
    variant_objects = [
        obj
        for obj in objects
        if bool(obj.get("Aerathea.VariantLocalC04", False))
    ]
    variant_inside = all(
        abs(point[1])
        <= float(COMMON_HALF_DEPTH) + FLOAT32_BOUND_TOLERANCE_CM
        for obj in variant_objects
        for point in mesh_world_vertices(obj)
    )
    provenance_missing = [
        obj.name
        for obj in objects
        if not obj.get("Aerathea.SourceOwner")
        or not obj.get("Aerathea.EquationId")
        or not obj.get("Aerathea.Component")
    ]
    all_properties = json.dumps(
        {
            "scene": custom_properties(scene),
            "objects": {
                obj.name: custom_properties(obj) for obj in objects
            },
        },
        sort_keys=True,
        default=str,
    )
    forbidden_absent = "EQ_CANDIDATE_AXIAL_INTERSECTION" not in all_properties
    shared_objects = [
        obj
        for obj in objects
        if not bool(obj.get("Aerathea.VariantLocalC04", False))
    ]
    shared_has_local_equation = any(
        str(obj.get("Aerathea.EquationId", "")).startswith("EQ_C04_")
        for obj in shared_objects
    )
    scene_checks = {
        "asset_id": scene.get("Aerathea.AssetId") == asset["asset_id"],
        "variant": (
            scene.get("Aerathea.LocalC04Treatment") == asset["variant"]
        ),
        "build_id": scene.get("Aerathea.BuildId") == BUILD_ID,
        "whole_asset_rz180_count": (
            int(scene.get("Aerathea.WholeAssetRz180Count", -1)) == 1
        ),
        "local_y_mirror_count": (
            int(scene.get("Aerathea.C04LocalYMirrorCount", -1)) == 1
        ),
        "quarantined_geometry_read_count": (
            int(scene.get("Aerathea.QuarantinedGeometryReadCount", -1))
            == 0
        ),
        "expected_width_exact": (
            scene.get("Aerathea.ExpectedWidthCmExact")
            == qstr(EXPECTED_DIMENSIONS[0])
        ),
        "expected_depth_exact": (
            scene.get("Aerathea.ExpectedDepthCmExact")
            == qstr(EXPECTED_DIMENSIONS[1])
        ),
        "expected_height_exact": (
            scene.get("Aerathea.ExpectedHeightCmExact")
            == qstr(EXPECTED_DIMENSIONS[2])
        ),
        "common_half_depth_exact": (
            scene.get("Aerathea.CommonHalfDepthCmExact")
            == qstr(COMMON_HALF_DEPTH)
        ),
        "local_c04_domain_half_exact": (
            scene.get("Aerathea.LocalC04DomainHalfCmExact")
            == qstr(asset["local_half"])
        ),
        "local_c04_domain_is_registration_not_fill": bool(
            scene.get("Aerathea.LocalC04DomainIsRegistrationNotFill", False)
        ),
        "local_c04_source_interval": (
            scene.get("Aerathea.LocalC04SourceIntervalHalfOpen")
            == (
                "[557,668)"
                if asset["variant"] == "rune_side"
                else "[418,557)"
            )
        ),
    }
    build_asset = next(
        item
        for item in combined["assets"].values()
        if item["asset_id"] == asset["asset_id"]
    )
    shared_float_hash = saved_shared_base_hash(objects)
    triangle_count = sum(
        sum(max(0, len(polygon.vertices) - 2) for polygon in obj.data.polygons)
        for obj in objects
    )
    checks = {
        "saved_bounds_within_float32_encoding_tolerance": (
            bound_result == "PASS"
        ),
        "visible_face_inside_approved_local_domain": (
            visible_face_inside_domain
        ),
        "variant_inside_common_envelope": variant_inside,
        "surface_provenance_complete": not provenance_missing,
        "forbidden_equation_absent": forbidden_absent,
        "shared_base_contains_no_local_c04_equation": (
            not shared_has_local_equation
        ),
        "no_linked_libraries": len(bpy.data.libraries) == 0,
        "no_external_images": all(
            not image.filepath for image in bpy.data.images
        ),
        "manifest_asset_identity_matches": (
            build_asset["asset_id"] == asset["asset_id"]
        ),
        **scene_checks,
    }
    result = "PASS" if all(checks.values()) else "FAIL"
    return {
        "schema": "AERATHEA_FRESH_TWIN_DCC_SOURCE_SAVED_FILE_AUDIT_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "build_id": BUILD_ID,
        "artifact_status": (
            "proof only; supports DCC source candidate classification"
        ),
        "asset_id": asset["asset_id"],
        "display_name": asset["display_name"],
        "variant": asset["variant"],
        "result": result,
        "checks": checks,
        "expected_dimensions_cm": {
            "exact": [qstr(value) for value in EXPECTED_DIMENSIONS],
            "decimal": expected_decimal,
        },
        "observed_saved_mesh_bounds_cm": {
            "minimum": minimum,
            "maximum": maximum,
            "dimensions": dimensions,
            "absolute_error_from_exact_decimal": errors,
            "encoding_tolerance_cm": FLOAT32_BOUND_TOLERANCE_CM,
        },
        "local_c04_extent": {
            "approved_domain_half_cm_exact": qstr(asset["local_half"]),
            "approved_domain_half_cm_decimal": float(asset["local_half"]),
            "observed_visible_face_half_cm": visible_face_half_observed,
            "visible_face_inside_approved_domain": (
                visible_face_inside_domain
            ),
            "domain_is_registration_not_fill": True,
            "inside_common_envelope": variant_inside,
        },
        "saved_shared_base_canonical_sha256": shared_float_hash,
        "builder_exact_shared_base_canonical_sha256": (
            scene.get("Aerathea.SharedBaseCanonicalSha256")
        ),
        "mesh_object_count": len(objects),
        "shared_mesh_object_count": len(shared_objects),
        "variant_mesh_object_count": len(variant_objects),
        "vertices": sum(len(obj.data.vertices) for obj in objects),
        "polygons": sum(len(obj.data.polygons) for obj in objects),
        "triangles": triangle_count,
        "missing_surface_provenance_objects": provenance_missing,
        "linked_library_count": len(bpy.data.libraries),
        "external_image_count": sum(
            1 for image in bpy.data.images if image.filepath
        ),
        "quarantined_geometry_read_count": 0,
        "expected_and_observed_dimensions_recorded_separately": True,
        "classification_if_pass": "DCC source candidate",
        "step_13_authority": False,
        "retopology_uv_bake_export_authority": False,
        "unreal_authority": False,
    }


def internal_audit_all() -> int:
    import bpy

    combined, authority_checks = verify_external_authority()
    reports: dict[str, Any] = {}
    for asset_key, asset in ASSETS.items():
        output_root: Path = asset["output_root"]
        blend_path = (
            output_root
            / f"{asset['asset_id']}_DCCSource_SharedDepth_A01.blend"
        )
        manifest_path = output_root / "build_manifest.json"
        manifest = load_json(manifest_path)
        if manifest["outputs"]["blend"]["sha256"] != sha256(blend_path):
            raise RuntimeError(
                f"Saved blend hash differs from build manifest: {asset_key}"
            )
        bpy.ops.wm.open_mainfile(filepath=str(blend_path))
        report = inspect_loaded_blend(bpy, asset, combined)
        report["saved_blend"] = {
            "path": relative(blend_path),
            "sha256": sha256(blend_path),
        }
        report["build_manifest"] = {
            "path": relative(manifest_path),
            "sha256": sha256(manifest_path),
        }
        write_json(
            output_root / "independent_saved_file_audit.json", report
        )
        reports[asset_key] = report

    siege = reports["siege_breaker"]
    foe = reports["foe_hammer"]
    dimension_differences = [
        siege["observed_saved_mesh_bounds_cm"]["dimensions"][axis]
        - foe["observed_saved_mesh_bounds_cm"]["dimensions"][axis]
        for axis in range(3)
    ]
    bitwise_equal_dimensions = all(
        struct.pack(
            ">d",
            siege["observed_saved_mesh_bounds_cm"]["dimensions"][axis],
        )
        == struct.pack(
            ">d",
            foe["observed_saved_mesh_bounds_cm"]["dimensions"][axis],
        )
        for axis in range(3)
    )
    shared_hash_equal = (
        siege["saved_shared_base_canonical_sha256"]
        == foe["saved_shared_base_canonical_sha256"]
    )
    builder_exact_shared_hash_equal = (
        siege["builder_exact_shared_base_canonical_sha256"]
        == foe["builder_exact_shared_base_canonical_sha256"]
        == combined["canonical_shared_base_sha256"]
    )
    cross_checks = {
        "siege_breaker_saved_file_audit_pass": siege["result"] == "PASS",
        "foe_hammer_saved_file_audit_pass": foe["result"] == "PASS",
        "saved_shared_base_hash_equal": shared_hash_equal,
        "builder_exact_shared_base_hash_equal": (
            builder_exact_shared_hash_equal
        ),
        "observed_xyz_dimensions_bitwise_equal": (
            bitwise_equal_dimensions
        ),
        "observed_xyz_difference_zero": all(
            difference == 0.0 for difference in dimension_differences
        ),
        "variant_assignments_correct": (
            siege["variant"] == "rune_side"
            and foe["variant"] == "metal_center_piece_side"
        ),
        "both_quarantined_geometry_read_counts_zero": (
            siege["quarantined_geometry_read_count"] == 0
            and foe["quarantined_geometry_read_count"] == 0
        ),
        "step_13_remains_locked": (
            not siege["step_13_authority"]
            and not foe["step_13_authority"]
        ),
        "unreal_remains_locked": (
            not siege["unreal_authority"]
            and not foe["unreal_authority"]
        ),
    }
    result = "PASS" if all(cross_checks.values()) else "FAIL"
    cross = {
        "schema": "AERATHEA_FRESH_TWIN_DCC_SOURCE_INDEPENDENT_AUDIT_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "build_id": BUILD_ID,
        "artifact_status": "proof only",
        "result": result,
        "checks": cross_checks,
        "expected_shared_dimensions_cm_exact": [
            qstr(value) for value in EXPECTED_DIMENSIONS
        ],
        "observed_cross_asset_dimension_difference_cm": (
            dimension_differences
        ),
        "saved_shared_base_canonical_sha256": (
            siege["saved_shared_base_canonical_sha256"]
        ),
        "builder_exact_shared_base_canonical_sha256": (
            combined["canonical_shared_base_sha256"]
        ),
        "authority_checks": authority_checks,
        "auditor": {
            "path": relative(Path(__file__)),
            "sha256": sha256(Path(__file__)),
        },
        "asset_audits": {
            key: {
                "path": relative(
                    asset["output_root"]
                    / "independent_saved_file_audit.json"
                ),
                "sha256": sha256(
                    asset["output_root"]
                    / "independent_saved_file_audit.json"
                ),
            }
            for key, asset in ASSETS.items()
        },
        "classification_if_pass": {
            "SM_DRW_SiegeBreaker_Hammer_A01": "DCC source candidate",
            "SM_DRW_FoeHammer_Hammer_A01": "DCC source candidate",
        },
        "step_13_authority": False,
        "retopology_uv_bake_export_authority": False,
        "unreal_authority": False,
    }
    write_json(CROSS_AUDIT, cross)
    print(json.dumps(cross, indent=2, sort_keys=True))
    if result != "PASS":
        raise RuntimeError("Independent cross-asset audit failed")
    return 0


def external_audit_all() -> int:
    verify_external_authority()
    if CROSS_AUDIT.exists():
        raise RuntimeError(
            f"Fresh independent audit already exists: {relative(CROSS_AUDIT)}"
        )
    command = [
        str(BLENDER),
        "--background",
        "--factory-startup",
        "--python",
        str(Path(__file__).resolve()),
        "--",
        "--internal-audit-all",
    ]
    environment = dict(os.environ)
    environment["PYTHONHASHSEED"] = "0"
    subprocess.run(
        command,
        cwd=ROOT,
        env=environment,
        check=True,
    )
    if load_json(CROSS_AUDIT)["result"] != "PASS":
        raise RuntimeError("Independent audit output is not PASS")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-all", action="store_true")
    parser.add_argument("--internal-audit-all", action="store_true")
    return parser.parse_args(
        sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else None
    )


def main() -> int:
    args = parse_args()
    if args.internal_audit_all:
        return internal_audit_all()
    if args.audit_all:
        return external_audit_all()
    raise RuntimeError("Choose --audit-all or --internal-audit-all")


if __name__ == "__main__":
    raise SystemExit(main())
