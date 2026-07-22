#!/usr/bin/env python3
"""Independently audit the Siege Breaker A12 R3 component-separated blend."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
CONTRACT_ID = "SB-AXIAL-A12-RECONSTRUCTION"
CORRECTION_ID = "SB-AXIAL-A12-R3-COMPONENT-SEPARATION"
CORE_NAME = f"{ASSET}_A12_CenteredCoreAndShaft"
STONE_NAME = f"{ASSET}_A12_TwoMirroredStoneStrikeMasses"
PROOF_NAMES = [
    f"{ASSET}_A12_TopClosedSourceCap",
    f"{ASSET}_A12_BottomClosedSourceCap",
    f"{ASSET}_A12_TopSourceRelief",
    f"{ASSET}_A12_BottomSourceRelief",
]
MANIFEST = ROOT / "docs/assets/blueprints" / ASSET / "manifests/A12_AXIAL_PIXEL_RECONSTRUCTION_A01_VALIDATION.json"
AUDIT = ROOT / "docs/assets/blueprints" / ASSET / "manifests/A12_R3_COMPONENT_SEPARATION_INDEPENDENT_AUDIT.json"
EXPECTED_DIMS = [75.13051305130513, 44.299176584325096, 170.0]
EXPECTED_CORE_WIDTH = 34.675621408294674
EXPECTED_STONE_WIDTH = 20.227445821505228
EXPECTED_CORE_HALF = 17.337810704147337
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
    if core is None or stone is None or core.type != "MESH" or stone.type != "MESH":
        raise RuntimeError(f"required candidates missing: {CORE_NAME}, {STONE_NAME}")
    candidates = [core, stone]
    proofs = [bpy.data.objects.get(name) for name in PROOF_NAMES]

    candidate_vertices = [vertex for obj in candidates for vertex in world_vertices(obj)]
    minimum = [min(vertex[axis] for vertex in candidate_vertices) for axis in range(3)]
    maximum = [max(vertex[axis] for vertex in candidate_vertices) for axis in range(3)]
    dimensions = [maximum[axis] - minimum[axis] for axis in range(3)]
    candidate_symmetry = {obj.name: symmetry(world_vertices(obj)) for obj in candidates}
    core_positive_x = [v[0] for v in world_vertices(core) if v[0] > 0.00001]
    stone_positive_x = [v[0] for v in world_vertices(stone) if v[0] > 0.00001]
    component_edges = {
        "core_max_positive_x_cm": max(core_positive_x),
        "stone_min_positive_x_cm": min(stone_positive_x),
        "approved_boundary_cm": EXPECTED_CORE_HALF,
    }

    output_hashes = {
        name: sha256(ROOT / relative)
        for name, relative in manifest["outputs"].items()
    }
    partition = manifest.get("construction", {}).get("component_partition", {})
    counts = manifest.get("mesh", {}).get("counts", {})
    manifest_dims = manifest.get("mesh", {}).get("bounds", {}).get("dimensions_cm", [])
    candidate_materials = {
        obj.name: [material.name for material in obj.data.materials if material]
        for obj in candidates
    }
    source_image_suffixes = {
        "siege_breaker_front_view.png",
        "siege_breaker_back_view.png",
        "siege_breaker_left_view.png",
        "siege_breaker_true_axial_top_view.png",
        "siege_breaker_true_axial_bottom_view.png",
    }
    loaded_source_images = sorted(Path(bpy.path.abspath(image.filepath)).name for image in bpy.data.images if image.filepath)

    gates = [
        gate("manifest_schema", manifest.get("schema") == "aerathea.siegebreaker.a12_axial_pixel_reconstruction_validation.v1", manifest.get("schema")),
        gate("contract_and_correction_ids", manifest.get("contract_id") == CONTRACT_ID and all(obj.get("Aerathea.ContractID") == CONTRACT_ID and obj.get("Aerathea.CorrectionID") == CORRECTION_ID for obj in candidates), {obj.name: [obj.get("Aerathea.ContractID"), obj.get("Aerathea.CorrectionID")] for obj in candidates}),
        gate("candidate_status", manifest.get("artifact_status") == "DCC source candidate pending Flamestrike visual decision" and all(obj.get("Aerathea.ArtifactStatus") == "DCC source candidate pending Flamestrike visual decision" for obj in candidates), manifest.get("artifact_status")),
        gate("two_candidate_components", counts.get("objects") == 2 and len(candidates) == 2, counts),
        gate("component_roles", core.get("Aerathea.ComponentRole") == "centered metal core and shaft" and stone.get("Aerathea.ComponentRole") == "two mirrored stone strike masses", {core.name: core.get("Aerathea.ComponentRole"), stone.name: stone.get("Aerathea.ComponentRole")}),
        gate("pixel_scaled_24_14_14_partition", partition.get("ratio_core_leftstone_rightstone") == [24, 14, 14] and close(partition.get("core_width_cm"), EXPECTED_CORE_WIDTH) and close(partition.get("stone_width_each_cm"), EXPECTED_STONE_WIDTH) and close(partition.get("core_half_width_cm"), EXPECTED_CORE_HALF), partition),
        gate("component_partition_preserves_front_membership", partition.get("core_source_pixels", 0) + partition.get("two_stone_source_pixels", 0) > 0, {"core": partition.get("core_source_pixels"), "stones": partition.get("two_stone_source_pixels")}),
        gate("component_boundary_within_one_front_pixel", abs(component_edges["core_max_positive_x_cm"] - EXPECTED_CORE_HALF) <= FRONT_PIXEL_CM and abs(component_edges["stone_min_positive_x_cm"] - EXPECTED_CORE_HALF) <= FRONT_PIXEL_CM, component_edges),
        gate("exact_candidate_envelope", close_vector(dimensions, EXPECTED_DIMS, 0.00001), dimensions),
        gate("bounds_match_manifest", close_vector(dimensions, manifest_dims, 0.00001), {"observed": dimensions, "manifest": manifest_dims}),
        gate("origin_z_zero", close(minimum[2], 0.0), minimum[2]),
        gate("independent_symmetry", all(record["pass"] for record in candidate_symmetry.values()), candidate_symmetry),
        gate("mirrors_applied", all(bool(obj.get("Aerathea.MirrorApplied")) and not any(mod.type == "MIRROR" for mod in obj.modifiers) for obj in candidates), {obj.name: {"property": obj.get("Aerathea.MirrorApplied"), "modifiers": [mod.type for mod in obj.modifiers]} for obj in candidates}),
        gate("no_remaining_candidate_modifiers", all(len(obj.modifiers) == 0 for obj in candidates), {obj.name: [mod.type for mod in obj.modifiers] for obj in candidates}),
        gate("stone_depth_authority", stone.get("Aerathea.DepthAuthority") == "A11 centered mean axial pixels" and close(stone.get("Aerathea.ApprovedHeadDepthCm"), EXPECTED_DIMS[1]), {"authority": stone.get("Aerathea.DepthAuthority"), "depth": stone.get("Aerathea.ApprovedHeadDepthCm")}),
        gate("core_depth_authority", core.get("Aerathea.DepthAuthority") == "proven A09 front/back/left pixel build", core.get("Aerathea.DepthAuthority")),
        gate("axial_owner_materials_integrated", all(bool(obj.get("Aerathea.AxialOwnerMaterialsIntegrated")) for obj in candidates) and all(any("TopSourcePixels" in name for name in names) and any("BottomSourcePixels" in name for name in names) for names in candidate_materials.values()), candidate_materials),
        gate("proof_objects_hidden_and_classified", all(obj is not None and obj.hide_render and str(obj.get("Aerathea.ArtifactStatus", "")).startswith("proof only") for obj in proofs), {name: None if obj is None else {"hide_render": obj.hide_render, "status": obj.get("Aerathea.ArtifactStatus")} for name, obj in zip(PROOF_NAMES, proofs)}),
        gate("no_global_transition_blend", manifest.get("construction", {}).get("global_z132_to_z138_transition_used") is False, manifest.get("construction", {}).get("global_z132_to_z138_transition_used")),
        gate("fresh_rebuild_no_prior_geometry", manifest.get("construction", {}).get("prior_candidate_geometry_inputs") == 0, manifest.get("construction", {}).get("prior_candidate_geometry_inputs")),
        gate("a09_immutable", manifest.get("a09_source_unchanged") is True and manifest.get("a09_source_hash_after_build") == manifest.get("authority_hashes", {}).get("a09_blend"), manifest.get("a09_source_hash_after_build")),
        gate("only_authorized_source_images_loaded", set(loaded_source_images).issubset(source_image_suffixes), loaded_source_images),
        gate("output_hashes", output_hashes == manifest.get("output_hashes"), output_hashes),
        gate("geometry_proof_distinct", output_hashes.get("geometry_3q") != output_hashes.get("color_3q"), {"color": output_hashes.get("color_3q"), "geometry": output_hashes.get("geometry_3q")}),
        gate("no_image_generation_trellis_or_unreal", manifest.get("software") == {"blender": bpy.app.version_string, "image_generation": False, "trellis": False, "image_to_3d": False} and manifest.get("unreal_authority") is False and manifest.get("fully_game_ready") is False, {"software": manifest.get("software"), "unreal": manifest.get("unreal_authority"), "game_ready": manifest.get("fully_game_ready")}),
    ]

    passed = sum(1 for record in gates if record["pass"])
    report = {
        "schema": "aerathea.siegebreaker.a12_r3_component_separation_independent_audit.v1",
        "asset": ASSET,
        "contract_id": CONTRACT_ID,
        "correction_id": CORRECTION_ID,
        "status": "pass" if passed == len(gates) else "blocked",
        "artifact_status": "proof only",
        "gate_summary": {"passed": passed, "total": len(gates)},
        "observed_bounds_cm": {"minimum": minimum, "maximum": maximum, "dimensions": dimensions},
        "observed_component_edges": component_edges,
        "observed_symmetry": candidate_symmetry,
        "gates": gates,
        "decision_boundary": "Technical audit cannot grant visual approval; Flamestrike must decide from the visible review board.",
    }
    AUDIT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
