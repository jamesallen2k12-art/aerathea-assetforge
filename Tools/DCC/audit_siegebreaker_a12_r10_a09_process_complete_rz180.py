#!/usr/bin/env python3
"""Independent saved-file audit for the complete A12 R10 Siege Breaker."""

from __future__ import annotations

import gzip
import hashlib
import json
import math
from pathlib import Path

import bpy


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ASSET_ROOT = ROOT / "docs/assets/blueprints" / ASSET
ATTEMPT = "A12_R10_A09ProcessCompleteRz180_A02"
CONTRACT_ID = "SB-A12-R10-A09-PROCESS-COMPLETE-RZ180-A02"
SOURCE_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET
BLEND = (
    SOURCE_ROOT / ATTEMPT / f"{ASSET}_{ATTEMPT}.blend"
)
VALIDATION = (
    ASSET_ROOT
    / "manifests/A12_R10_A09_PROCESS_COMPLETE_RZ180_A02_VALIDATION.json"
)
AUDIT = (
    ASSET_ROOT
    / "manifests/A12_R10_A09_PROCESS_COMPLETE_RZ180_A02_INDEPENDENT_AUDIT.json"
)
MEASUREMENTS = (
    ASSET_ROOT
    / "manifests/A12_R10_STEP01_SOURCE_MEASUREMENT_CENTERLINE_A01.json"
)
SOURCE_FILES = {
    "step03": SOURCE_ROOT
    / "A12_R10_Step03_StrikeFaceHalfProof_A02"
    / f"{ASSET}_A12_R10_Step03_StrikeFaceHalfProof_A02.blend",
    "step04": SOURCE_ROOT
    / "A12_R10_Step04_CoreStonesCouplerProof_A02"
    / f"{ASSET}_A12_R10_Step04_CoreStonesCouplerProof_A02.blend",
    "step05": SOURCE_ROOT
    / "A12_R10_Step05_RotationalCapPommelProof_A03"
    / f"{ASSET}_A12_R10_Step05_RotationalCapPommelProof_A03.blend",
    "step05c": SOURCE_ROOT
    / "A12_R10_Step05C_HaftFerruleGripHalfProof_A01"
    / f"{ASSET}_A12_R10_Step05C_HaftFerruleGripHalfProof_A01.blend",
}
SOURCE_SHA256 = {
    "step03": "5a12b5dd4104dd036e500106a6a0d28f345c699be0ca061c63bc5349696117eb",
    "step04": "f086c42180422e6d6a0b7331dc8458bf26cf576f1e9b7379d6ac8c333725d683",
    "step05": "0891bbe5df2bc700b1e1eeb7428dc40521e8df9ccc12d0c844c3a81cf881fe4a",
    "step05c": "3e5645adea6f5ef3fd04404ecc4ab87e2b3dab39cdc422792b41d20b579f8a9e",
}
DIRECT_OBJECTS = {
    "step03": {
        "C04_STRIKE_FACE_POSITIVE_X":
        "C04_STRIKE_FACE_POSITIVE_X_ISOLATED_PROOF",
    },
    "step04": {
        "C01_CENTER_CORE": "C01_CENTER_CORE_VISIBLE_OWNER_PROOF",
        "C02_STONE_LEFT": "C02_STONE_LEFT_VISIBLE_OWNER_PROOF",
        "C03_STONE_RIGHT": "C03_STONE_RIGHT_VISIBLE_OWNER_PROOF",
        "C06_UPPER_HAFT_CAP":
        "C06_UPPER_HAFT_COUPLER_VISIBLE_OWNER_PROOF",
    },
    "step05c": {
        "C07A_HAFT_CYLINDER":
        "C07A_HAFT_CYLINDER_POSITIVE_X_HALF_PROOF",
        "C07B_HAFT_TO_HANDLE_FERRULE":
        "C07B_HAFT_TO_HANDLE_FERRULE_POSITIVE_X_HALF_PROOF",
        "C08_GRIP": "C08_GRIP_POSITIVE_X_HALF_PROOF",
    },
}
ROTATIONAL_OBJECTS = {
    "C09_LOWER_COLLAR": "C09_LOWER_COLLAR_ROTATIONAL_OWNER_PROOF",
    "C10_POMMEL_BODY": "C10_POMMEL_BODY_ROTATIONAL_OWNER_PROOF",
    "C11_POMMEL_TERMINAL_CAP":
    "C11_POMMEL_TERMINAL_CAP_ROTATIONAL_OWNER_PROOF",
    "C12_UPPER_HEAD_CAP_SPIRE":
    "C12_UPPER_HEAD_CAP_SPIRE_ROTATIONAL_OWNER_PROOF",
}
COMPONENTS = {
    "C00_COMBINED_HEAD_OUTER_BOUNDARY",
    "C01_CENTER_CORE",
    "C02_STONE_LEFT",
    "C03_STONE_RIGHT",
    "C04_STRIKE_FACE_POSITIVE_X",
    "C06_UPPER_HAFT_CAP",
    "C07A_HAFT_CYLINDER",
    "C07B_HAFT_TO_HANDLE_FERRULE",
    "C08_GRIP",
    "C09_LOWER_COLLAR",
    "C10_POMMEL_BODY",
    "C11_POMMEL_TERMINAL_CAP",
    "C12_UPPER_HEAD_CAP_SPIRE",
}
HALF_SEQUENCE = tuple(range(96, 128)) + tuple(range(0, 33))
QUANTUM = 100000


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def qpoint(point) -> tuple[int, int, int]:
    return tuple(int(round(float(value) * QUANTUM)) for value in point)


def rz(point: tuple[int, int, int]) -> tuple[int, int, int]:
    return (-point[0], -point[1], point[2])


def append_source(path: Path, name: str) -> bpy.types.Object:
    existing = set(bpy.data.objects)
    with bpy.data.libraries.load(str(path), link=False) as (data_from, data_to):
        if name not in data_from.objects:
            raise RuntimeError(f"Missing source object {name} in {path}")
        data_to.objects = [name]
    obj = data_to.objects[0]
    bpy.context.scene.collection.objects.link(obj)
    if obj in existing:
        raise RuntimeError(f"Source append did not create {name}")
    return obj


def target_source_object(
    meshes: list[bpy.types.Object],
    component: str,
) -> bpy.types.Object:
    candidates = [
        obj for obj in meshes
        if obj.get("Aerathea.ComponentID") == component
        and "_R10_SOURCE_COMPLETE_RZ180" in obj.name
    ]
    if len(candidates) != 1:
        raise RuntimeError(
            f"Expected one source-complete target for {component}; "
            f"observed {[obj.name for obj in candidates]}"
        )
    return candidates[0]


def vertex_set(obj: bpy.types.Object) -> set[tuple[int, int, int]]:
    return {
        qpoint(obj.matrix_world @ vertex.co)
        for vertex in obj.data.vertices
    }


def exact_source_replay(
    meshes: list[bpy.types.Object],
) -> tuple[bool, dict[str, object]]:
    result = {}
    passed = True
    for lane, records in DIRECT_OBJECTS.items():
        for component, source_name in records.items():
            source = append_source(SOURCE_FILES[lane], source_name)
            expected = vertex_set(source)
            target = vertex_set(target_source_object(meshes, component))
            missing_source = len(expected - target)
            missing_rotated = len({rz(point) for point in expected} - target)
            record = {
                "source_vertices": len(expected),
                "missing_original_vertices": missing_source,
                "missing_exact_rz180_vertices": missing_rotated,
            }
            record["pass"] = missing_source == 0 and missing_rotated == 0
            result[component] = record
            passed &= record["pass"]
            bpy.data.objects.remove(source, do_unlink=True)

    for component, source_name in ROTATIONAL_OBJECTS.items():
        source = append_source(SOURCE_FILES["step05"], source_name)
        profile = json.loads(source["Aerathea.ProfileJSON"])
        expected = {
            qpoint(
                source.matrix_world
                @ source.data.vertices[ring * 128 + segment].co
            )
            for ring in range(len(profile))
            for segment in HALF_SEQUENCE
        }
        target = vertex_set(target_source_object(meshes, component))
        missing_source = len(expected - target)
        missing_rotated = len({rz(point) for point in expected} - target)
        record = {
            "source_positive_x_half_vertices": len(expected),
            "missing_original_vertices": missing_source,
            "missing_exact_rz180_vertices": missing_rotated,
        }
        record["pass"] = missing_source == 0 and missing_rotated == 0
        result[component] = record
        passed &= record["pass"]
        bpy.data.objects.remove(source, do_unlink=True)
    return passed, result


def load_right_membership() -> tuple[bytearray, int, int]:
    data = json.loads(MEASUREMENTS.read_text(encoding="utf-8"))
    record = next(
        item for item in data["lossless_scanline_captures"]
        if item["capture_id"] == "right_complete_object_membership"
    )
    capture = json.loads(gzip.decompress((ROOT / record["path"]).read_bytes()))
    width, height = [int(value) for value in capture["canvas_pixels"]]
    membership = bytearray(width * height)
    for row in capture["rows"]:
        y = int(row["y"])
        for x0, x1 in row["runs_half_open"]:
            membership[y * width + int(x0):y * width + int(x1)] = (
                b"\x01" * (int(x1) - int(x0))
            )
    return membership, width, height


def outer_boundary_uv_audit(
    meshes: list[bpy.types.Object],
) -> dict[str, object]:
    outer = next(
        obj for obj in meshes
        if obj.get("Aerathea.ComponentID")
        == "C00_COMBINED_HEAD_OUTER_BOUNDARY"
    )
    membership, width, height = load_right_membership()
    uv = outer.data.uv_layers.active
    invalid = 0
    samples = set()
    if uv is None:
        invalid = len(outer.data.loops)
    else:
        for loop in uv.data:
            x = max(0, min(width - 1, int(math.floor(loop.uv.x * width))))
            y = max(
                0,
                min(height - 1, int(math.floor((1.0 - loop.uv.y) * height))),
            )
            samples.add((x, y))
            if not membership[y * width + x]:
                invalid += 1
    return {
        "object": outer.name,
        "uv_loop_count": len(outer.data.loops),
        "unique_sampled_pixels": len(samples),
        "source_background_uv_loops": invalid,
        "per_component_wall_count": int(
            outer.get("Aerathea.PerComponentWallCount", -1)
        ),
        "pass": (
            uv is not None
            and invalid == 0
            and int(outer.get("Aerathea.PerComponentWallCount", -1)) == 0
        ),
    }


def coordinate_contacts(
    meshes: list[bpy.types.Object],
    component_a: str,
    component_b: str,
) -> int:
    points_a = set().union(
        *[
            vertex_set(obj)
            for obj in meshes
            if obj.get("Aerathea.ComponentID") == component_a
        ]
    )
    points_b = set().union(
        *[
            vertex_set(obj)
            for obj in meshes
            if obj.get("Aerathea.ComponentID") == component_b
        ]
    )
    return len(points_a & points_b)


def bounds(meshes: list[bpy.types.Object]) -> dict[str, object]:
    points = [
        obj.matrix_world @ vertex.co
        for obj in meshes
        for vertex in obj.data.vertices
    ]
    minimum = [min(point[index] for point in points) for index in range(3)]
    maximum = [max(point[index] for point in points) for index in range(3)]
    return {
        "min_cm": minimum,
        "max_cm": maximum,
        "dimensions_cm": [
            maximum[index] - minimum[index] for index in range(3)
        ],
    }


def face_signature_audit(meshes: list[bpy.types.Object]) -> dict[str, object]:
    signatures = set()
    duplicates = 0
    for obj in meshes:
        world = obj.matrix_world
        for polygon in obj.data.polygons:
            signature = tuple(
                sorted(
                    qpoint(world @ obj.data.vertices[index].co)
                    for index in polygon.vertices
                )
            )
            if signature in signatures:
                duplicates += 1
            signatures.add(signature)
    return {
        "unique_coordinate_faces": len(signatures),
        "duplicate_coordinate_faces": duplicates,
        "pass": duplicates == 0,
    }


def main() -> None:
    if not BLEND.exists() or not VALIDATION.exists():
        raise RuntimeError("Saved A02 blend or validation is missing")
    validation = json.loads(VALIDATION.read_text(encoding="utf-8"))
    bpy.ops.wm.open_mainfile(filepath=str(BLEND))
    meshes = [
        obj for obj in bpy.context.scene.objects
        if obj.type == "MESH"
    ]
    checks: dict[str, bool] = {}

    checks["approved_source_hashes_match"] = all(
        sha256(path) == SOURCE_SHA256[lane]
        for lane, path in SOURCE_FILES.items()
    )
    checks["saved_contract_exact"] = (
        bpy.context.scene.get("Aerathea.ContractID") == CONTRACT_ID
        and validation["contract_id"] == CONTRACT_ID
    )
    checks["saved_process_authority_exact"] = (
        bpy.context.scene.get("Aerathea.ProcessAuthority")
        == "A09 exact pixel-half process"
        and bpy.context.scene.get("Aerathea.CenterRegistrationAuthority")
        == "R10/R8"
    )
    checks["saved_rz180_execution_exact"] = (
        bool(bpy.context.scene.get("Aerathea.Rz180Executed"))
        and bpy.context.scene.get("Aerathea.Rz180Formula")
        == "(X,Y,Z)->(-X,-Y,Z)"
    )
    checks["all_builder_gates_true"] = (
        validation["technical_result"] == "PASS"
        and all(validation["gates"].values())
    )
    checks["mesh_count_exact"] = len(meshes) == 23
    checks["component_set_exact"] = {
        obj.get("Aerathea.ComponentID") for obj in meshes
    } == COMPONENTS
    checks["all_meshes_complete_rz180"] = all(
        obj.get("Aerathea.GeometryRole") == "complete_rz180"
        and bool(obj.get("Aerathea.Rz180Applied"))
        and obj.get("Aerathea.Rz180Formula")
        == "(X,Y,Z)->(-X,-Y,Z)"
        for obj in meshes
    )
    checks["no_half_only_mesh_remains"] = not any(
        obj.get("Aerathea.GeometryRole") == "source_half"
        for obj in meshes
    )
    checks["identity_transforms_and_no_modifiers"] = all(
        tuple(obj.location) == (0.0, 0.0, 0.0)
        and tuple(obj.rotation_euler) == (0.0, 0.0, 0.0)
        and tuple(obj.scale) == (1.0, 1.0, 1.0)
        and not obj.modifiers
        for obj in meshes
    )

    per_object_symmetry = {}
    symmetry_pass = True
    doubling_pass = True
    for obj in meshes:
        points = vertex_set(obj)
        missing = len({rz(point) for point in points} - points)
        expected_vertices = (
            2 * int(obj["Aerathea.SourceHalfVertices"])
            - int(obj["Aerathea.SeamVerticesMerged"])
        )
        expected_polygons = 2 * int(obj["Aerathea.SourceHalfPolygons"])
        record = {
            "vertices": len(obj.data.vertices),
            "expected_vertices_after_recorded_merge": expected_vertices,
            "polygons": len(obj.data.polygons),
            "expected_polygons": expected_polygons,
            "missing_rz180_vertices": missing,
        }
        record["pass"] = (
            missing == 0
            and len(obj.data.vertices) == expected_vertices
            and len(obj.data.polygons) == expected_polygons
        )
        per_object_symmetry[obj.name] = record
        symmetry_pass &= missing == 0
        doubling_pass &= (
            len(obj.data.vertices) == expected_vertices
            and len(obj.data.polygons) == expected_polygons
        )
    checks["every_object_rz180_symmetric"] = symmetry_pass
    checks["every_object_exact_half_doubling"] = doubling_pass

    source_replay_pass, source_replay = exact_source_replay(meshes)
    checks["approved_source_vertices_replay_exactly"] = source_replay_pass

    uv_audit = outer_boundary_uv_audit(meshes)
    checks["combined_outer_boundary_exact_selected_pixels"] = uv_audit["pass"]
    checks["no_per_component_center_walls"] = (
        sum(
            1 for obj in meshes
            if "straight_ruled_boundary_to_y0"
            in str(obj.get("Aerathea.ProcessRule", ""))
        ) == 0
        and uv_audit["per_component_wall_count"] == 0
    )

    c07a = target_source_object(meshes, "C07A_HAFT_CYLINDER")
    radii = [
        math.hypot(vertex.co.x, vertex.co.y)
        for vertex in c07a.data.vertices
    ]
    checks["haft_true_five_cm_cylinder"] = (
        max(abs(radius - 2.5) for radius in radii) <= 1.0e-5
    )
    checks["haft_pi_over_two_wrap_exact"] = (
        c07a.get("Aerathea.ThetaFormula") == "-pi/2+pi*i/64"
        and bool(c07a.get("Aerathea.PiOver2HaftWrapExecuted"))
    )

    c08 = target_source_object(meshes, "C08_GRIP")
    grip_z = [vertex.co.z for vertex in c08.data.vertices]
    checks["grip_length_42_cm"] = (
        abs(max(grip_z) - min(grip_z) - 42.0) <= 1.0e-5
    )
    c10 = target_source_object(meshes, "C10_POMMEL_BODY")
    c11 = target_source_object(meshes, "C11_POMMEL_TERMINAL_CAP")
    pommel_vertices = list(c10.data.vertices) + list(c11.data.vertices)
    pommel_z = [vertex.co.z for vertex in pommel_vertices]
    pommel_r = [
        math.hypot(vertex.co.x, vertex.co.y)
        for vertex in pommel_vertices
    ]
    checks["pommel_length_18_cm_and_max_width_11_cm"] = (
        abs(max(pommel_z) - min(pommel_z) - 18.0) <= 1.0e-5
        and abs(2.0 * max(pommel_r) - 11.0) <= 1.0e-5
    )

    contacts = {
        "H8_C07B_C08": coordinate_contacts(
            meshes, "C07B_HAFT_TO_HANDLE_FERRULE", "C08_GRIP"
        ),
        "U1_C08_C09": coordinate_contacts(
            meshes, "C08_GRIP", "C09_LOWER_COLLAR"
        ),
        "U3_C09_C10": coordinate_contacts(
            meshes, "C09_LOWER_COLLAR", "C10_POMMEL_BODY"
        ),
        "L4_C10_C11": coordinate_contacts(
            meshes, "C10_POMMEL_BODY", "C11_POMMEL_TERMINAL_CAP"
        ),
    }
    checks["four_approved_full_ring_contacts_128"] = all(
        value >= 128 for value in contacts.values()
    )

    measured_bounds = bounds(meshes)
    checks["complete_height_170_cm"] = (
        abs(measured_bounds["dimensions_cm"][2] - 170.0) <= 1.0e-5
    )
    face_audit = face_signature_audit(meshes)
    checks["no_duplicate_coordinate_faces"] = face_audit["pass"]
    checks["no_rejected_step06_or_voxel_input"] = all(
        "Step06_OneRz180SourceHalfAssembly" not in obj.name
        and "VOXEL" not in obj.name.upper()
        for obj in meshes
    )
    checks["no_fbx_or_unreal_output"] = (
        not (SOURCE_ROOT / ATTEMPT).joinpath(f"{ASSET}.fbx").exists()
        and validation["gates"]["no_fbx_or_unreal"]
    )
    board_path = ROOT / validation["outputs"]["review_board"]
    render_paths = [
        ROOT / path for path in validation["outputs"]["renders"]
    ]
    output_hashes_match = (
        sha256(BLEND) == validation["output_sha256"]["blend"]
        and board_path.exists()
        and sha256(board_path)
        == validation["output_sha256"]["review_board"]
        and all(
            path.exists()
            and sha256(path)
            == validation["output_sha256"]["renders"][path.name]
            for path in render_paths
        )
    )
    checks["saved_output_hashes_match"] = output_hashes_match

    passed = all(checks.values())
    result = {
        "schema": (
            "aerathea.siegebreaker.r10."
            "a09_process_complete_rz180.independent_audit.v1"
        ),
        "asset": ASSET,
        "attempt": ATTEMPT,
        "contract_id": CONTRACT_ID,
        "artifact_status": (
            "candidate pending Flamestrike visual decision"
            if passed else "invalid"
        ),
        "technical_result": "PASS" if passed else "FAIL",
        "checks": checks,
        "check_count": len(checks),
        "passed_check_count": sum(bool(value) for value in checks.values()),
        "per_object_rz180": per_object_symmetry,
        "approved_source_vertex_replay": source_replay,
        "combined_outer_boundary_uv_audit": uv_audit,
        "approved_contacts": contacts,
        "bounds_cm": measured_bounds,
        "coordinate_face_audit": face_audit,
        "outputs": {
            "blend": str(BLEND.relative_to(ROOT)),
            "validation": str(VALIDATION.relative_to(ROOT)),
        },
        "output_sha256": {
            "blend": sha256(BLEND),
            "validation": sha256(VALIDATION),
        },
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    AUDIT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if not passed:
        raise RuntimeError(
            "Independent audit failed: "
            + ", ".join(name for name, value in checks.items() if not value)
        )
    print("AERATHEA_R10_A09_PROCESS_COMPLETE_INDEPENDENT_AUDIT_PASS")
    print(
        json.dumps(
            {
                "audit": str(AUDIT),
                "checks": f"{result['passed_check_count']}/{result['check_count']}",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
