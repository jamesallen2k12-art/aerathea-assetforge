#!/usr/bin/env python3
"""Independently audit the Siege Breaker A12 R4 side-owner-face blend."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
CONTRACT_ID = "SB-AXIAL-A12-R4-SIDE-OWNER-FACES"
CORRECTION_ID = "SB-AXIAL-A12-R4-SIDE-OWNER-FACES"
CORE_NAME = f"{ASSET}_A12_CenteredCoreAndShaft"
STONE_NAME = f"{ASSET}_A12_TwoMirroredStoneStrikeMasses"
FACE_NAME = f"{ASSET}_A12_R4_SideOwnerFaces"
PROOF_NAMES = [
    f"{ASSET}_A12_TopClosedSourceCap",
    f"{ASSET}_A12_BottomClosedSourceCap",
    f"{ASSET}_A12_TopSourceRelief",
    f"{ASSET}_A12_BottomSourceRelief",
]
MANIFEST = ROOT / "docs/assets/blueprints" / ASSET / "manifests/A12_AXIAL_PIXEL_RECONSTRUCTION_A01_VALIDATION.json"
AUDIT = ROOT / "docs/assets/blueprints" / ASSET / "manifests/A12_R4_SIDE_OWNER_FACE_INDEPENDENT_AUDIT.json"
EXPECTED_DIMS = [75.13051305130513, 44.299176584325096, 170.0]
EXPECTED_HALF_X = EXPECTED_DIMS[0] * 0.5
EXPECTED_CORE_WIDTH = 34.675621408294674
EXPECTED_STONE_WIDTH = 20.227445821505228
EXPECTED_CORE_HALF = 17.337810704147337
EXPECTED_SIDE_COUNTS = {"left": 118540, "right": 116948}
FRONT_PIXEL_CM = 170.0 / 1111.0


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def gate(name: str, passed: bool, evidence: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "evidence": evidence}


def close(a: float, b: float, tolerance: float = 0.00001) -> bool:
    return abs(float(a) - float(b)) <= tolerance


def close_vector(observed: list[float], expected: list[float], tolerance: float = 0.00001) -> bool:
    return len(observed) == len(expected) and all(close(a, b, tolerance) for a, b in zip(observed, expected))


def world_vertices(obj: Any) -> list[list[float]]:
    return [list(obj.matrix_world @ vertex.co) for vertex in obj.data.vertices]


def symmetry(vertices: list[list[float]]) -> dict[str, Any]:
    coords = {(round(v[0], 5), round(v[1], 5), round(v[2], 5)) for v in vertices}
    missing = sum(1 for x, y, z in coords if (-x, y, z) not in coords)
    return {"unique_vertices": len(coords), "missing_mirrored_vertices": missing, "pass": missing == 0}


def main() -> int:
    import bpy

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    core = bpy.data.objects.get(CORE_NAME)
    stone = bpy.data.objects.get(STONE_NAME)
    owner = bpy.data.objects.get(FACE_NAME)
    candidates = [core, stone, owner]
    if any(obj is None or obj.type != "MESH" for obj in candidates):
        raise RuntimeError(f"required R4 candidates missing: {[CORE_NAME, STONE_NAME, FACE_NAME]}")
    proofs = [bpy.data.objects.get(name) for name in PROOF_NAMES]

    candidate_vertices = [vertex for obj in candidates for vertex in world_vertices(obj)]
    minimum = [min(vertex[axis] for vertex in candidate_vertices) for axis in range(3)]
    maximum = [max(vertex[axis] for vertex in candidate_vertices) for axis in range(3)]
    dimensions = [maximum[axis] - minimum[axis] for axis in range(3)]
    candidate_symmetry = {obj.name: symmetry(world_vertices(obj)) for obj in candidates}
    owner_vertices = world_vertices(owner)
    owner_bounds = {
        "minimum": [min(v[axis] for v in owner_vertices) for axis in range(3)],
        "maximum": [max(v[axis] for v in owner_vertices) for axis in range(3)],
    }
    core_positive_x = [v[0] for v in world_vertices(core) if v[0] > 0.00001]
    stone_positive_x = [v[0] for v in world_vertices(stone) if v[0] > 0.00001]
    component_edges = {
        "core_max_positive_x_cm": max(core_positive_x),
        "stone_min_positive_x_cm": min(stone_positive_x),
        "approved_boundary_cm": EXPECTED_CORE_HALF,
    }

    output_hashes = {name: sha256(ROOT / relative) for name, relative in manifest["outputs"].items()}
    construction = manifest.get("construction", {})
    partition = construction.get("component_partition", {})
    side_stats = construction.get("mirrored_side_owner_faces", {})
    recess = construction.get("superseded_outward_wall_recess", {})
    counts = manifest.get("mesh", {}).get("counts", {})
    manifest_dims = manifest.get("mesh", {}).get("bounds", {}).get("dimensions_cm", [])
    owner_materials = [material.name for material in owner.data.materials if material]
    source_image_suffixes = {
        "siege_breaker_front_view.png",
        "siege_breaker_back_view.png",
        "siege_breaker_left_view.png",
        "siege_breaker_right_view.png",
        "siege_breaker_true_axial_top_view.png",
        "siege_breaker_true_axial_bottom_view.png",
        "A12_R4_left_source_pixels_object_alpha.png",
        "A12_R4_right_source_pixels_object_alpha.png",
    }
    loaded_source_images = sorted(Path(bpy.path.abspath(image.filepath)).name for image in bpy.data.images if image.filepath)
    material_face_counts = side_stats.get("material_face_counts", {})
    owner_z_interval = side_stats.get("owner_face_z_interval_cm", [])
    stone_head_max_abs_x = max(abs(v[0]) for v in world_vertices(stone) if v[2] >= owner_z_interval[0] - 0.00001)
    owner_deepest_visible_abs_x = EXPECTED_HALF_X - float(side_stats.get("inward_relief_max_cm", 0.0))

    gates = [
        gate("manifest_schema", manifest.get("schema") == "aerathea.siegebreaker.a12_axial_pixel_reconstruction_validation.v2", manifest.get("schema")),
        gate("contract_and_correction_ids", manifest.get("contract_id") == CONTRACT_ID and all(obj.get("Aerathea.ContractID") == CONTRACT_ID and obj.get("Aerathea.CorrectionID") == CORRECTION_ID for obj in candidates), {obj.name: [obj.get("Aerathea.ContractID"), obj.get("Aerathea.CorrectionID")] for obj in candidates}),
        gate("candidate_status", manifest.get("artifact_status") == "DCC source candidate pending Flamestrike visual decision" and all(obj.get("Aerathea.ArtifactStatus") == "DCC source candidate pending Flamestrike visual decision" for obj in candidates), manifest.get("artifact_status")),
        gate("three_candidate_components", counts.get("objects") == 3 and len(candidates) == 3, counts),
        gate("component_roles", core.get("Aerathea.ComponentRole") == "centered metal core and shaft" and stone.get("Aerathea.ComponentRole") == "two mirrored stone strike masses" and owner.get("Aerathea.ComponentRole") == "mirrored -X/+X outward strike-face owner geometry", {obj.name: obj.get("Aerathea.ComponentRole") for obj in candidates}),
        gate("pixel_scaled_24_14_14_partition", partition.get("ratio_core_leftstone_rightstone") == [24, 14, 14] and close(partition.get("core_width_cm"), EXPECTED_CORE_WIDTH) and close(partition.get("stone_width_each_cm"), EXPECTED_STONE_WIDTH) and close(partition.get("core_half_width_cm"), EXPECTED_CORE_HALF), partition),
        gate("component_boundary_within_one_front_pixel", abs(component_edges["core_max_positive_x_cm"] - EXPECTED_CORE_HALF) <= FRONT_PIXEL_CM and abs(component_edges["stone_min_positive_x_cm"] - EXPECTED_CORE_HALF) <= FRONT_PIXEL_CM, component_edges),
        gate("exact_candidate_envelope", close_vector(dimensions, EXPECTED_DIMS, 0.00001), dimensions),
        gate("bounds_match_manifest", close_vector(dimensions, manifest_dims, 0.00001), {"observed": dimensions, "manifest": manifest_dims}),
        gate("origin_z_zero", close(minimum[2], 0.0), minimum[2]),
        gate("owner_face_exact_x_envelope", close(owner_bounds["minimum"][0], -EXPECTED_HALF_X, 0.00001) and close(owner_bounds["maximum"][0], EXPECTED_HALF_X, 0.00001), owner_bounds),
        gate("owner_face_exact_z_interval", len(owner_z_interval) == 2 and close(owner_bounds["minimum"][2], owner_z_interval[0], 0.00001) and close(owner_bounds["maximum"][2], owner_z_interval[1], 0.00001) and close(owner_z_interval[1], 170.0, 0.00001), {"observed": owner_bounds, "declared": owner_z_interval}),
        gate("independent_symmetry", all(record["pass"] for record in candidate_symmetry.values()), candidate_symmetry),
        gate("mirrors_applied", all(bool(obj.get("Aerathea.MirrorApplied")) and not any(mod.type == "MIRROR" for mod in obj.modifiers) for obj in candidates), {obj.name: {"property": obj.get("Aerathea.MirrorApplied"), "modifiers": [mod.type for mod in obj.modifiers]} for obj in candidates}),
        gate("no_remaining_candidate_modifiers", all(len(obj.modifiers) == 0 for obj in candidates), {obj.name: [mod.type for mod in obj.modifiers] for obj in candidates}),
        gate("side_membership_counts", manifest.get("source_measurements", {}).get("r4_side_component_pixels") == EXPECTED_SIDE_COUNTS, manifest.get("source_measurements", {}).get("r4_side_component_pixels")),
        gate("side_source_hashes", manifest.get("authority_hashes", {}).get("left") == "1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b" and manifest.get("authority_hashes", {}).get("right") == "04a1e9359d518b1dec35fe161020bd23ab9e2f8d5934f24e4184aecaa91d8330", {"left": manifest.get("authority_hashes", {}).get("left"), "right": manifest.get("authority_hashes", {}).get("right")}),
        gate("nine_profile_anchors", len(side_stats.get("anchor_profile_samples", [])) == 9 and [record.get("z_cm") for record in side_stats.get("anchor_profile_samples", [])] == [132.0, 136.75, 141.5, 146.25, 151.0, 155.75, 160.5, 165.25, 170.0], side_stats.get("anchor_profile_samples", [])),
        gate("one_face_then_mirror_rule", side_stats.get("construction") == "one continuous row-connected +X scanline face; pure-X inward closure; exact X=0 mirror; fixed source-specific -X/+X UV ownership" and owner.get("Aerathea.SourceHalf") == "X>=0", {"construction": side_stats.get("construction"), "source_half": owner.get("Aerathea.SourceHalf")}),
        gate("fixed_source_map_no_yz_offset", side_stats.get("fixed_horizontal_source_mapping") is True and side_stats.get("y_or_z_edge_offset_used") is False, {"fixed_mapping": side_stats.get("fixed_horizontal_source_mapping"), "y_or_z_edge_offset": side_stats.get("y_or_z_edge_offset_used")}),
        gate("continuous_row_connected_surface", side_stats.get("separate_raster_cell_islands") is False and side_stats.get("continuous_row_segments", 0) > 0 and side_stats.get("half_boundary_edges", 0) > 0, {"segments": side_stats.get("continuous_row_segments"), "islands": side_stats.get("separate_raster_cell_islands"), "boundary_edges": side_stats.get("half_boundary_edges")}),
        gate("per_side_pixel_ownership", owner.get("Aerathea.VisiblePixelOwners") == "-X=left source; +X=right source" and any("LeftOwnerPixelsMasked" in name for name in owner_materials) and any("RightOwnerPixelsMasked" in name for name in owner_materials), {"property": owner.get("Aerathea.VisiblePixelOwners"), "materials": owner_materials}),
        gate("source_background_removed_by_exact_alpha", all(record.get("method") == "exact membership plus enclosed regions; exterior flood-fill removed" and record.get("filled_membership_pixels") == record.get("full_canvas_alpha_pixels") for record in manifest.get("source_measurements", {}).get("side_object_alpha", {}).values()), manifest.get("source_measurements", {}).get("side_object_alpha")),
        gate("both_side_materials_used", material_face_counts.get("left_minus_x_faces", 0) > 0 and material_face_counts.get("right_plus_x_faces", 0) > 0, material_face_counts),
        gate("side_owner_uv_present", len(owner.data.uv_layers) == 1 and owner.data.uv_layers.active is not None and owner.data.uv_layers.active.name == "A12_R4_PerSideExactSourceUV", [layer.name for layer in owner.data.uv_layers]),
        gate("superseded_wall_recessed", recess.get("vertices_recessed", 0) > 0 and bool(stone.get("Aerathea.R4SupersededOutwardWallRecessed")), recess),
        gate("legacy_wall_behind_maximum_owner_relief", stone_head_max_abs_x < owner_deepest_visible_abs_x - 0.00001, {"stone_head_max_abs_x_cm": stone_head_max_abs_x, "owner_deepest_visible_abs_x_cm": owner_deepest_visible_abs_x}),
        gate("axial_owner_materials_preserved", bool(core.get("Aerathea.AxialOwnerMaterialsIntegrated")) and bool(stone.get("Aerathea.AxialOwnerMaterialsIntegrated")), {"core": core.get("Aerathea.AxialOwnerMaterialsIntegrated"), "stone": stone.get("Aerathea.AxialOwnerMaterialsIntegrated")}),
        gate("proof_objects_hidden_and_classified", all(obj is not None and obj.hide_render and str(obj.get("Aerathea.ArtifactStatus", "")).startswith("proof only") for obj in proofs), {name: None if obj is None else {"hide_render": obj.hide_render, "status": obj.get("Aerathea.ArtifactStatus")} for name, obj in zip(PROOF_NAMES, proofs)}),
        gate("no_global_transition_blend", construction.get("global_z132_to_z138_transition_used") is False, construction.get("global_z132_to_z138_transition_used")),
        gate("fresh_rebuild_no_prior_geometry", construction.get("prior_candidate_geometry_inputs") == 0, construction.get("prior_candidate_geometry_inputs")),
        gate("a09_immutable", manifest.get("a09_source_unchanged") is True and manifest.get("a09_source_hash_after_build") == manifest.get("authority_hashes", {}).get("a09_blend"), manifest.get("a09_source_hash_after_build")),
        gate("only_authorized_source_images_loaded", set(loaded_source_images).issubset(source_image_suffixes), loaded_source_images),
        gate("output_hashes", output_hashes == manifest.get("output_hashes"), output_hashes),
        gate("side_renders_distinct", output_hashes.get("left") != output_hashes.get("right"), {"left": output_hashes.get("left"), "right": output_hashes.get("right")}),
        gate("geometry_proof_distinct", output_hashes.get("geometry_3q") != output_hashes.get("color_3q"), {"color": output_hashes.get("color_3q"), "geometry": output_hashes.get("geometry_3q")}),
        gate("no_image_generation_trellis_or_unreal", manifest.get("software") == {"blender": bpy.app.version_string, "image_generation": False, "trellis": False, "image_to_3d": False} and manifest.get("unreal_authority") is False and manifest.get("fully_game_ready") is False, {"software": manifest.get("software"), "unreal": manifest.get("unreal_authority"), "game_ready": manifest.get("fully_game_ready")}),
    ]

    passed = sum(1 for record in gates if record["pass"])
    report = {
        "schema": "aerathea.siegebreaker.a12_r4_side_owner_face_independent_audit.v1",
        "asset": ASSET,
        "contract_id": CONTRACT_ID,
        "correction_id": CORRECTION_ID,
        "status": "pass" if passed == len(gates) else "blocked",
        "artifact_status": "proof only",
        "gate_summary": {"passed": passed, "total": len(gates)},
        "observed_bounds_cm": {"minimum": minimum, "maximum": maximum, "dimensions": dimensions},
        "observed_owner_face_bounds_cm": owner_bounds,
        "observed_component_edges": component_edges,
        "observed_symmetry": candidate_symmetry,
        "gates": gates,
        "decision_boundary": "Technical audit cannot grant visual approval; Flamestrike must decide from the visible R4 review board.",
    }
    AUDIT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
