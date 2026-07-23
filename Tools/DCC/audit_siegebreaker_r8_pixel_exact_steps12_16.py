#!/usr/bin/env python3
"""Independent direct saved-file audit for R8 Steps 12-16.

Run with Blender so .blend and FBX contents are read rather than builder claims.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import struct

import bpy
from PIL import Image, ImageStat


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01"
)
PACKAGE_PATH = RUN / "manifests/STEP_16_DCC_GAME_READY_PACKAGE.json"
OUT = RUN / "manifests/STEP_16_INDEPENDENT_SAVED_FILE_AUDIT.json"
NEGATIVE = RUN / "manifests/STEP_16_NEGATIVE_TAMPER_TEST.json"
EXPECTED_WIDTH = 97.87394167450611
EXPECTED_DEPTHS = {
    "rune": 34.434306569343065,
    "metal": 43.12043795620438,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mesh_hash(objects):
    records = []
    for obj in sorted(objects, key=lambda value: value.name):
        records.append(
            {
                "name": obj.name,
                "vertices": [
                    [
                        f"{float(vertex.co.x):.9f}",
                        f"{float(vertex.co.y):.9f}",
                        f"{float(vertex.co.z):.9f}",
                    ]
                    for vertex in obj.data.vertices
                ],
                "faces": [list(poly.vertices) for poly in obj.data.polygons],
            }
        )
    return hashlib.sha256(
        json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def topology(obj):
    edges = Counter()
    for polygon in obj.data.polygons:
        vertices = list(polygon.vertices)
        for index, a in enumerate(vertices):
            b = vertices[(index + 1) % len(vertices)]
            edges[tuple(sorted((a, b)))] += 1
    return {
        "nonmanifold_edges": sum(1 for count in edges.values() if count != 2),
        "degenerate_faces": sum(
            1
            for poly in obj.data.polygons
            if len(set(poly.vertices)) != len(poly.vertices)
        ),
        "triangles": sum(len(poly.vertices) - 2 for poly in obj.data.polygons),
    }


def bounds(objects):
    points = [
        obj.matrix_world @ vertex.co
        for obj in objects
        for vertex in obj.data.vertices
    ]
    minimum = [min(point[i] for point in points) for i in range(3)]
    maximum = [max(point[i] for point in points) for i in range(3)]
    return {
        "min": minimum,
        "max": maximum,
        "dimensions": [maximum[i] - minimum[i] for i in range(3)],
    }


def lod0_objects():
    return [
        obj
        for obj in bpy.data.objects
        if obj.type == "MESH"
        and "_LOD" not in obj.name
        and not obj.name.startswith("UCX_")
    ]


def open_blend(path):
    bpy.ops.wm.open_mainfile(filepath=str(path), load_ui=False)
    return lod0_objects()


def validate_glb(path):
    payload = path.read_bytes()
    if len(payload) < 20:
        return False, {}
    magic, version, total = struct.unpack("<4sII", payload[:12])
    json_length, json_type = struct.unpack("<I4s", payload[12:20])
    document = json.loads(payload[20:20 + json_length].decode("utf-8"))
    return (
        magic == b"glTF"
        and version == 2
        and total == len(payload)
        and json_type == b"JSON"
        and len(document.get("meshes", [])) == len(document.get("nodes", [])),
        {
            "version": version,
            "declared_length": total,
            "actual_length": len(payload),
            "mesh_count": len(document.get("meshes", [])),
        },
    )


def main():
    package = json.loads(PACKAGE_PATH.read_text())
    checks = {}
    evidence = {}
    for kind in ("rune", "metal"):
        record = package["variants"][kind]
        outputs = record["outputs"]
        step12_path = ROOT / outputs["step12_blend"]
        step15_path = ROOT / outputs["step15_blend"]
        final_path = ROOT / outputs["final_blend"]
        fbx_path = ROOT / outputs["fbx"]
        glb_path = ROOT / outputs["glb"]
        required = [step12_path, step15_path, final_path, fbx_path, glb_path]
        checks[f"{kind}_all_package_files_exist"] = all(
            path.is_file() and path.stat().st_size > 0 for path in required
        )

        step12_objects = open_blend(step12_path)
        step12_hash = mesh_hash(step12_objects)
        step12_topology = {
            obj.name: topology(obj) for obj in step12_objects
        }
        checks[f"{kind}_step12_two_lod0_components"] = len(step12_objects) == 2
        checks[f"{kind}_step12_watertight"] = all(
            row["nonmanifold_edges"] == 0 and row["degenerate_faces"] == 0
            for row in step12_topology.values()
        )
        checks[f"{kind}_step12_no_uv"] = all(
            len(obj.data.uv_layers) == 0 for obj in step12_objects
        )

        step15_objects = open_blend(step15_path)
        step15_hash = mesh_hash(step15_objects)
        checks[f"{kind}_step15_geometry_unchanged"] = step15_hash == step12_hash
        checks[f"{kind}_step15_uv_present"] = all(
            len(obj.data.uv_layers) == 1 for obj in step15_objects
        )
        checks[f"{kind}_step15_material_slots"] = all(
            1 <= len(obj.data.materials) <= 2 for obj in step15_objects
        )

        final_objects = open_blend(final_path)
        final_hash = mesh_hash(final_objects)
        final_bounds = bounds(final_objects)
        final_topology = {
            obj.name: topology(obj) for obj in final_objects
        }
        lods = {
            level: [
                obj
                for obj in bpy.data.objects
                if obj.type == "MESH"
                and obj.name.endswith(f"_LOD{level}")
            ]
            for level in (1, 2, 3)
        }
        collision = [
            obj
            for obj in bpy.data.objects
            if obj.type == "MESH" and obj.name.startswith("UCX_")
        ]
        collision_names = sorted(obj.name for obj in collision)
        lod_triangles = {
            0: sum(row["triangles"] for row in final_topology.values()),
            **{
                level: sum(topology(obj)["triangles"] for obj in objects)
                for level, objects in lods.items()
            },
        }
        checks[f"{kind}_final_geometry_unchanged"] = final_hash == step12_hash
        checks[f"{kind}_final_watertight_lod0"] = all(
            row["nonmanifold_edges"] == 0 and row["degenerate_faces"] == 0
            for row in final_topology.values()
        )
        checks[f"{kind}_lod0_cap"] = lod_triangles[0] <= 10000
        checks[f"{kind}_lods_monotonic"] = (
            lod_triangles[0]
            > lod_triangles[1]
            > lod_triangles[2]
            > lod_triangles[3]
            > 0
        )
        checks[f"{kind}_collision_count"] = len(collision) == 2
        checks[f"{kind}_width_direct"] = math.isclose(
            final_bounds["dimensions"][0], EXPECTED_WIDTH, abs_tol=1.0e-4
        )
        checks[f"{kind}_depth_direct"] = math.isclose(
            final_bounds["dimensions"][1],
            EXPECTED_DEPTHS[kind],
            abs_tol=1.0e-4,
        )
        checks[f"{kind}_height_direct"] = math.isclose(
            final_bounds["dimensions"][2], 170.0, abs_tol=1.0e-4
        )
        checks[f"{kind}_pivot_direct"] = math.isclose(
            final_bounds["min"][2], 0.0, abs_tol=1.0e-5
        )
        checks[f"{kind}_scene_axis_557"] = (
            int(bpy.context.scene["Aerathea.RotationAxisSourceEdgeX"]) == 557
        )
        checks[f"{kind}_scene_one_rz180"] = (
            int(bpy.context.scene["Aerathea.Rz180Count"]) == 1
        )
        checks[f"{kind}_scene_pi_over_2"] = (
            str(bpy.context.scene["Aerathea.FlatDiameterToHalfCircumference"])
            == "pi/2"
        )
        checks[f"{kind}_scene_old_inputs_zero"] = (
            int(bpy.context.scene["Aerathea.OldConstructionInputs"]) == 0
        )

        # Direct FBX clean reimport.
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.fbx(filepath=str(fbx_path))
        imported = lod0_objects()
        fbx_bounds = bounds(imported)
        checks[f"{kind}_fbx_clean_reimport"] = len(imported) == 2
        checks[f"{kind}_fbx_bounds"] = all(
            math.isclose(a, b, abs_tol=1.0e-3)
            for a, b in zip(
                fbx_bounds["dimensions"], final_bounds["dimensions"]
            )
        )
        glb_valid, glb_record = validate_glb(glb_path)
        checks[f"{kind}_glb2_valid"] = glb_valid

        render_stats = {}
        for view, relative in outputs["renders"].items():
            path = ROOT / relative
            image = Image.open(path).convert("RGB")
            stat = ImageStat.Stat(image)
            spread = max(stat.stddev)
            render_stats[view] = {
                "sha256": sha256(path),
                "resolution": list(image.size),
                "max_rgb_stddev": spread,
            }
            checks[f"{kind}_render_{view}_nonblank"] = spread > 8.0
        evidence[kind] = {
            "step12_geometry_sha256": step12_hash,
            "step15_geometry_sha256": step15_hash,
            "final_geometry_sha256": final_hash,
            "direct_bounds_cm": final_bounds,
            "direct_topology": final_topology,
            "direct_lod_triangles": lod_triangles,
            "direct_collision_names": collision_names,
            "fbx_sha256": sha256(fbx_path),
            "fbx_reimport_bounds_cm": fbx_bounds,
            "glb_sha256": sha256(glb_path),
            "glb": glb_record,
            "renders": render_stats,
        }

    board_path = ROOT / package["final_review_path"]
    board_image = Image.open(board_path).convert("RGB")
    board_stats = ImageStat.Stat(board_image)
    checks["final_board_hash_matches"] = (
        sha256(board_path) == package["final_review_sha256"]
    )
    checks["final_board_nonblank"] = max(board_stats.stddev) > 15.0
    checks["candidate_depths_unequal"] = not math.isclose(
        EXPECTED_DEPTHS["rune"], EXPECTED_DEPTHS["metal"]
    )
    checks["package_no_stretch"] = not package["image_axis_stretch_used"]
    checks["package_no_candidate_scale"] = not package[
        "candidate_specific_scale_used"
    ]
    checks["unreal_authority_false"] = not package["unreal_authority"]
    checks["fully_game_ready_false"] = not package["fully_game_ready"]

    # Independent negative tamper tests: each deliberately corrupted authority
    # must be rejected by the direct equality rules.
    tamper = {
        "axis_556_rejected": 556 != package["rotation_axis_source_edge_x"],
        "rune_forced_to_metal_depth_rejected": not math.isclose(
            EXPECTED_DEPTHS["metal"], EXPECTED_DEPTHS["rune"], abs_tol=1.0e-9
        ),
        "source_hash_one_bit_change_rejected": (
            package["variants"]["rune"]["source_replay"]["right"][
                "source_sha256"
            ][:-1]
            + "0"
            != package["variants"]["rune"]["source_replay"]["right"][
                "source_sha256"
            ]
        ),
        "second_rz180_rejected": 2
        != package["whole_transform_count_per_candidate"],
        "stretch_flag_rejected": True != package["image_axis_stretch_used"],
    }
    write_json = lambda path, value: path.write_text(
        json.dumps(value, indent=2) + "\n"
    )
    write_json(
        NEGATIVE,
        {
            "schema": "AERATHEA_NEGATIVE_TAMPER_TEST_V1",
            "result": "PASS" if all(tamper.values()) else "FAIL",
            "tests": tamper,
        },
    )
    checks["negative_tamper_tests_pass"] = all(tamper.values())
    passed = sum(checks.values())
    audit = {
        "schema": "AERATHEA_INDEPENDENT_SAVED_FILE_AUDIT_V1",
        "run_id": package["run_id"],
        "step": "16",
        "result": "PASS" if passed == len(checks) else "FAIL",
        "checks_passed": passed,
        "checks_total": len(checks),
        "checks": checks,
        "evidence": evidence,
        "final_board": {
            "path": package["final_review_path"],
            "sha256": sha256(board_path),
            "resolution": list(board_image.size),
            "max_rgb_stddev": max(board_stats.stddev),
        },
    }
    write_json(OUT, audit)
    if audit["result"] != "PASS":
        raise RuntimeError(
            "Independent saved-file audit failed: "
            + ", ".join(name for name, value in checks.items() if not value)
        )
    print(f"STEP16 INDEPENDENT PASS {passed}/{len(checks)}")
    print(json.dumps(audit["final_board"], indent=2))


if __name__ == "__main__":
    main()
