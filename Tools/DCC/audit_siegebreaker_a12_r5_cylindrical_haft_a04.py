#!/usr/bin/env python3
"""Independent fail-closed audit for Siege Breaker R5 cylindrical haft A04."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import bpy
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
CONTRACT_ID = "SB-AXIAL-A12-R5-FOUR-VIEW-WHOLE-ASSEMBLY"
MANIFEST_PATH = ROOT / f"docs/assets/blueprints/{ASSET}/manifests/A12_R5_CYLINDRICAL_HAFT_A04_VALIDATION.json"
AUDIT_PATH = ROOT / f"docs/assets/blueprints/{ASSET}/manifests/A12_R5_CYLINDRICAL_HAFT_A04_INDEPENDENT_AUDIT.json"
EXPECTED_SOURCES = {
    "front": "d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95",
    "back": "15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799",
    "left": "1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b",
    "right": "04a1e9359d518b1dec35fe161020bd23ab9e2f8d5934f24e4184aecaa91d8330",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require(checks: list[dict[str, object]], name: str, condition: bool, evidence: object) -> None:
    checks.append({"name": name, "pass": bool(condition), "evidence": evidence})


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    checks: list[dict[str, object]] = []
    require(checks, "contract_id", manifest.get("contract_id") == CONTRACT_ID, manifest.get("contract_id"))
    require(checks, "artifact_ceiling", manifest.get("artifact_status") == "DCC source candidate pending Flamestrike visual decision", manifest.get("artifact_status"))
    require(checks, "source_hash_lock", manifest.get("source_hashes") == EXPECTED_SOURCES, manifest.get("source_hashes"))
    require(checks, "source_membership_counts", manifest.get("source_membership_counts") == {"front": 212765, "back": 238342, "left": 118540, "right": 116948}, manifest.get("source_membership_counts"))
    require(checks, "registered_shaft_axes", manifest.get("registered_shaft_axes_global_px") == {"front": 563.0, "back": 552.5, "left": 549.5, "right": 593.5}, manifest.get("registered_shaft_axes_global_px"))

    outputs = manifest["outputs"]
    blend_path = ROOT / outputs["blend_local_only"]
    require(checks, "blend_hash", sha256(blend_path) == manifest["output_hashes"]["blend_local_only"], sha256(blend_path))
    for key in ("front", "back", "left", "right", "color_3q", "geometry_3q", "review"):
        path = ROOT / outputs[key]
        require(checks, f"output_hash_{key}", path.is_file() and sha256(path) == manifest["output_hashes"][key], str(path))
    color_pixels = Image.open(ROOT / outputs["color_3q"]).convert("RGB").getdata()
    geometry_pixels = Image.open(ROOT / outputs["geometry_3q"]).convert("RGB").getdata()
    color_max_chroma = max(max(pixel) - min(pixel) for pixel in color_pixels)
    geometry_max_chroma = max(max(pixel) - min(pixel) for pixel in geometry_pixels)
    require(checks, "colored_and_geometry_proofs_distinct", manifest["output_hashes"]["color_3q"] != manifest["output_hashes"]["geometry_3q"], [manifest["output_hashes"]["color_3q"], manifest["output_hashes"]["geometry_3q"]])
    require(checks, "geometry_proof_flat_material_only", geometry_max_chroma < 45 and color_max_chroma > 100, {"geometry_max_rgb_chroma": geometry_max_chroma, "color_max_rgb_chroma": color_max_chroma})
    for key in ("front_haft_texture_local_only", "back_haft_texture_local_only"):
        texture_name = "A12_R5_front_haft_15708_static_uv.png" if key.startswith("front") else "A12_R5_back_haft_15708_static_uv.png"
        texture_path = blend_path.parent / texture_name
        require(checks, f"{key}_hash", texture_path.is_file() and sha256(texture_path) == manifest["output_hashes"][key], str(texture_path))

    bpy.ops.wm.open_mainfile(filepath=str(blend_path))
    meshes = [obj for obj in bpy.data.objects if obj.type == "MESH"]
    hafts = [obj for obj in meshes if "CylindricalHaft" in obj.name]
    facades = [obj for obj in meshes if "CompleteMirroredAssembly" in obj.name]
    require(checks, "two_mesh_components", len(meshes) == 2, [obj.name for obj in meshes])
    require(checks, "one_cylindrical_haft", len(hafts) == 1, [obj.name for obj in hafts])
    require(checks, "one_non_haft_assembly", len(facades) == 1, [obj.name for obj in facades])
    haft = hafts[0]
    facade = facades[0]

    require(checks, "prior_geometry_inputs_zero", facade.get("Aerathea.PriorCandidateGeometryInputs") == 0, facade.get("Aerathea.PriorCandidateGeometryInputs"))
    require(checks, "haft_component_property", haft.get("Aerathea.Component") == "true cylindrical haft", haft.get("Aerathea.Component"))
    require(checks, "haft_mirror_applied", bool(haft.get("Aerathea.MirrorApplied")) and len(haft.modifiers) == 0, {"property": haft.get("Aerathea.MirrorApplied"), "modifiers": len(haft.modifiers)})
    require(checks, "registered_axis", haft.get("Aerathea.Axis") == "X=0,Y=0", haft.get("Aerathea.Axis"))
    require(checks, "front_back_degrees", haft.get("Aerathea.FrontFaceSetDegrees") == 180 and haft.get("Aerathea.BackFaceSetDegrees") == 180, [haft.get("Aerathea.FrontFaceSetDegrees"), haft.get("Aerathea.BackFaceSetDegrees")])
    require(checks, "static_uv_property", haft.get("Aerathea.StaticUVMap") == "UVMap" and not bool(haft.get("Aerathea.ProceduralCoordinates")), {"uv": haft.get("Aerathea.StaticUVMap"), "procedural": haft.get("Aerathea.ProceduralCoordinates")})
    require(checks, "widen_factor", abs(float(haft.get("Aerathea.TextureWidenFactor")) - 1.5708) < 1.0e-9, haft.get("Aerathea.TextureWidenFactor"))

    material_names = [slot.material.name if slot.material else None for slot in haft.material_slots]
    require(checks, "two_material_slots", material_names == ["Front_Material", "Back_Material"], material_names)
    uv_names = [layer.name for layer in haft.data.uv_layers]
    require(checks, "one_static_uv_layer", uv_names == ["UVMap"], uv_names)
    uv = haft.data.uv_layers["UVMap"]
    uv_ranges: dict[str, list[float]] = {}
    for material_index, owner in ((0, "front"), (1, "back")):
        values = [uv.data[loop_index].uv[:] for polygon in haft.data.polygons if polygon.material_index == material_index for loop_index in polygon.loop_indices]
        u_values = [value[0] for value in values]
        v_values = [value[1] for value in values]
        uv_ranges[owner] = [min(u_values), max(u_values), min(v_values), max(v_values)]
    require(checks, "front_uv_exact_0_1", all(abs(value - expected) < 1.0e-6 for value, expected in zip(uv_ranges["front"], [0.0, 1.0, 0.0, 1.0])), uv_ranges["front"])
    require(checks, "back_uv_exact_0_1", all(abs(value - expected) < 1.0e-6 for value, expected in zip(uv_ranges["back"], [0.0, 1.0, 0.0, 1.0])), uv_ranges["back"])

    prohibited_node_types = {"TEX_COORD", "MAPPING"}
    prohibited_nodes: list[tuple[str, str]] = []
    texture_projection: list[tuple[str, str, str]] = []
    for material in [slot.material for slot in haft.material_slots if slot.material]:
        for node in material.node_tree.nodes:
            if node.type in prohibited_node_types:
                prohibited_nodes.append((material.name, node.type))
            if node.type == "TEX_IMAGE":
                texture_projection.append((material.name, node.name, node.projection))
    require(checks, "no_procedural_coordinate_nodes", not prohibited_nodes, prohibited_nodes)
    require(checks, "image_nodes_flat_static_uv", texture_projection and all(item[2] == "FLAT" for item in texture_projection), texture_projection)

    rings: dict[float, list[float]] = {}
    coordinate_set = set()
    for vertex in haft.data.vertices:
        coordinate = vertex.co
        coordinate_set.add((round(coordinate.x, 5), round(coordinate.y, 5), round(coordinate.z, 5)))
        radius = math.hypot(coordinate.x, coordinate.y)
        if radius > 0.1:
            rings.setdefault(round(coordinate.z, 5), []).append(radius)
    maximum_ring_delta = max(max(values) - min(values) for values in rings.values())
    require(checks, "circular_cross_sections", maximum_ring_delta < 1.0e-4, maximum_ring_delta)
    missing_mirrors = sum(1 for x, y, z in coordinate_set if (-x, y, z) not in coordinate_set)
    require(checks, "exact_x_mirror", missing_mirrors == 0, missing_mirrors)

    all_coordinates = [obj.matrix_world @ vertex.co for obj in meshes for vertex in obj.data.vertices]
    minimum = [min(value[index] for value in all_coordinates) for index in range(3)]
    maximum = [max(value[index] for value in all_coordinates) for index in range(3)]
    dimensions = [maximum[index] - minimum[index] for index in range(3)]
    require(checks, "bottom_center_z_frame", abs(minimum[2]) < 1.0e-6 and abs(maximum[2] - 170.0) < 1.0e-6, {"min_z": minimum[2], "max_z": maximum[2]})
    require(checks, "identity_transforms", all(all(abs(value - expected) < 1.0e-9 for value, expected in zip(obj.scale, (1.0, 1.0, 1.0))) and all(abs(value) < 1.0e-9 for value in obj.location) for obj in meshes), {obj.name: {"scale": list(obj.scale), "location": list(obj.location)} for obj in meshes})
    require(checks, "manifest_bounds_match", all(abs(value - recorded) < 2.0e-6 for value, recorded in zip(dimensions, manifest["mesh"]["bounds"]["dimensions_cm"])), {"observed": dimensions, "recorded": manifest["mesh"]["bounds"]["dimensions_cm"]})

    for view in ("front", "back"):
        derivation = manifest["haft_texture_derivation"][view]
        expected_width = round(derivation["maximum_source_diameter_px"] * 1.5708)
        require(checks, f"{view}_texture_15708_width", derivation["output_dimensions_px"][0] == expected_width, derivation)
        require(checks, f"{view}_texture_not_generated", derivation["generated_imagery"] is False and derivation["resampling"] == "nearest exact source-pixel sampling", derivation)

    require(checks, "prohibited_software_absent", manifest["software"] == {"blender": bpy.app.version_string, "image_generation": False, "trellis": False, "image_to_3d": False}, manifest["software"])
    require(checks, "no_export_or_unreal_execution", manifest["deferred_export_record"]["executed"] is False and manifest["unreal_authority"] is False and manifest["fully_game_ready"] is False, manifest["deferred_export_record"])
    require(checks, "future_fbx_record", haft.get("Aerathea.FutureFBXApplyScalings") == "FBX All" and not bool(haft.get("Aerathea.FutureFBXAddLeafBones")), {"apply_scalings": haft.get("Aerathea.FutureFBXApplyScalings"), "add_leaf_bones": haft.get("Aerathea.FutureFBXAddLeafBones")})

    passed = sum(1 for check in checks if check["pass"])
    result = {
        "schema": "aerathea.siegebreaker.a12_r5_cylindrical_haft_independent_audit.v1",
        "asset": ASSET,
        "contract_id": CONTRACT_ID,
        "artifact_status": "proof only",
        "result": "pass" if passed == len(checks) else "fail",
        "summary": f"{passed}/{len(checks)} checks passed",
        "checks": checks,
        "visual_approval_granted": False,
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    AUDIT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["result"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
