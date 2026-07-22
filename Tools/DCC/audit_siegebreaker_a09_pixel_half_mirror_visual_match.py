#!/usr/bin/env python3
"""Independently audit the saved Siege Breaker A09 mirrored Blender candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ATTEMPT = "A09_PixelHalfMirror_VisualMatch_A01"
CONTRACT_ID = "SB-PHM-A09-FULL-MIRROR"
OBJECT_NAME = f"{ASSET}_A09_CompleteMirroredModel"
DOC_ROOT = ROOT / "docs/assets/blueprints" / ASSET
MANIFEST_REL = Path("docs/assets/blueprints") / ASSET / "manifests/A09_FULL_PIXEL_HALF_MIRROR_A01_VALIDATION.json"
AUDIT_REL = Path("docs/assets/blueprints") / ASSET / "manifests/A09_FULL_PIXEL_HALF_MIRROR_A01_INDEPENDENT_AUDIT.json"

SOURCE_REL = {
    "front": Path("SourceAssets/Concepts/SiegeBreaker/siege_breaker_front_view.png"),
    "back": Path("SourceAssets/Concepts/SiegeBreaker/siege_breaker_back_view.png"),
    "left": Path("SourceAssets/Concepts/SiegeBreaker/siege_breaker_left_view.png"),
    "concept": Path("SourceAssets/Concepts/SiegeBreaker/siege_breaker_concept_view.png"),
}
EXPECTED_SOURCE_SHA256 = {
    "front": "d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95",
    "back": "15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799",
    "left": "1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b",
    "concept": "9f1ac142a5047968bb20c74216c2dccf61470ed9f4e21689ff01934bd849c586",
}
EXPECTED_COMPONENT_PIXELS = {"front": 212765, "back": 238342, "left": 118540}
EXPECTED_DIMENSIONS_CM = [75.13051305130513, 32.95761947700631, 170.0]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def gate(name: str, passed: bool, evidence: Any) -> Dict[str, Any]:
    return {"name": name, "pass": bool(passed), "evidence": evidence}


def close_vector(observed: List[float], expected: List[float], tolerance: float) -> bool:
    return len(observed) == len(expected) and all(
        abs(float(value) - float(target)) <= tolerance
        for value, target in zip(observed, expected)
    )


def mirrored_vertex_audit(vertices: List[List[float]], precision: int = 5) -> Dict[str, Any]:
    unique = {
        (round(float(vertex[0]), precision), round(float(vertex[1]), precision), round(float(vertex[2]), precision))
        for vertex in vertices
    }
    missing = sum(1 for x, y, z in unique if (-x, y, z) not in unique)
    return {
        "precision_decimal_places": precision,
        "unique_vertices": len(unique),
        "missing_mirrored_vertices": missing,
        "pass": missing == 0,
    }


def main() -> int:
    import bpy

    manifest_path = ROOT / MANIFEST_REL
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    model = bpy.data.objects.get(OBJECT_NAME)
    if model is None or model.type != "MESH":
        raise RuntimeError(f"required mesh object missing: {OBJECT_NAME}")

    world_vertices = [list(model.matrix_world @ vertex.co) for vertex in model.data.vertices]
    minimum = [min(vertex[axis] for vertex in world_vertices) for axis in range(3)]
    maximum = [max(vertex[axis] for vertex in world_vertices) for axis in range(3)]
    dimensions = [maximum[axis] - minimum[axis] for axis in range(3)]
    symmetry = mirrored_vertex_audit(world_vertices)

    source_hashes = {name: sha256_file(ROOT / relative) for name, relative in SOURCE_REL.items()}
    output_hashes = {
        name: sha256_file(ROOT / relative)
        for name, relative in manifest["outputs"].items()
        if name != "blend_local_only"
    }
    blend_path = ROOT / manifest["outputs"]["blend_local_only"]
    blend_hash = sha256_file(blend_path)

    material_names = [material.name for material in model.data.materials if material is not None]
    loaded_image_paths = sorted(
        str(Path(bpy.path.abspath(image.filepath)).resolve().relative_to(ROOT))
        for image in bpy.data.images
        if image.filepath and Path(bpy.path.abspath(image.filepath)).resolve().is_relative_to(ROOT)
    )
    allowed_loaded_images = {str(relative) for relative in SOURCE_REL.values()}
    required_material_fragments = {"Front", "Back", "Left"}

    gates: List[Dict[str, Any]] = [
        gate("manifest_schema", manifest.get("schema") == "aerathea.siegebreaker.a09_pixel_half_mirror_validation.v1", manifest.get("schema")),
        gate("contract_id", manifest.get("contract_id") == CONTRACT_ID and model.get("Aerathea.ContractID") == CONTRACT_ID, {"manifest": manifest.get("contract_id"), "blend": model.get("Aerathea.ContractID")}),
        gate("attempt_id", manifest.get("attempt") == ATTEMPT, manifest.get("attempt")),
        gate("candidate_status", manifest.get("artifact_status") == "DCC source candidate pending Flamestrike visual decision" and model.get("Aerathea.ArtifactStatus") == "DCC source candidate pending Flamestrike visual decision", {"manifest": manifest.get("artifact_status"), "blend": model.get("Aerathea.ArtifactStatus")}),
        gate("source_hashes", source_hashes == EXPECTED_SOURCE_SHA256 and manifest.get("source_hashes") == EXPECTED_SOURCE_SHA256, source_hashes),
        gate("component_membership_counts", manifest.get("exact_component_membership_pixels") == EXPECTED_COMPONENT_PIXELS, manifest.get("exact_component_membership_pixels")),
        gate("uniform_source_pixel_authority", manifest.get("visual_match_scale", {}).get("authority") == "uniform source-pixel proportions" and manifest.get("visual_match_scale", {}).get("printed_52cm_width_used") is False, manifest.get("visual_match_scale")),
        gate("dimensions_match_pixel_proportion_target", close_vector(dimensions, EXPECTED_DIMENSIONS_CM, 0.00001), dimensions),
        gate("bounds_match_manifest", close_vector(minimum, manifest.get("mesh_bounds", {}).get("min_cm", []), 0.00001) and close_vector(maximum, manifest.get("mesh_bounds", {}).get("max_cm", []), 0.00001), {"minimum": minimum, "maximum": maximum}),
        gate("origin_z_zero", abs(minimum[2]) <= 0.00001, minimum[2]),
        gate("mesh_counts", len(model.data.vertices) == manifest.get("construction", {}).get("complete_vertices") and len(model.data.polygons) == manifest.get("construction", {}).get("complete_polygons"), {"vertices": len(model.data.vertices), "polygons": len(model.data.polygons)}),
        gate("mirror_applied", bool(model.get("Aerathea.MirrorApplied")) and manifest.get("construction", {}).get("mirror_applied") is True and not any(modifier.type == "MIRROR" for modifier in model.modifiers), {"blend_property": model.get("Aerathea.MirrorApplied"), "remaining_modifiers": [modifier.type for modifier in model.modifiers]}),
        gate("independent_symmetry", symmetry["pass"] and symmetry["missing_mirrored_vertices"] == 0, symmetry),
        gate("fresh_geometry_inputs_zero", model.get("Aerathea.PriorCandidateGeometryInputs") == 0 and manifest.get("construction", {}).get("prior_candidate_geometry_inputs") == 0, {"blend": model.get("Aerathea.PriorCandidateGeometryInputs"), "manifest": manifest.get("construction", {}).get("prior_candidate_geometry_inputs")}),
        gate("source_projection_not_geometry_proof", not bool(model.get("Aerathea.SourceProjectionIsGeometryProof")) and manifest.get("construction", {}).get("source_projection_is_geometry_proof") is False, {"blend": model.get("Aerathea.SourceProjectionIsGeometryProof"), "manifest": manifest.get("construction", {}).get("source_projection_is_geometry_proof")}),
        gate("source_material_roles", all(any(fragment in name for name in material_names) for fragment in required_material_fragments), material_names),
        gate("only_authorized_source_images_loaded", set(loaded_image_paths).issubset(allowed_loaded_images), loaded_image_paths),
        gate("output_files_and_hashes", output_hashes == {name: manifest["output_hashes"][name] for name in output_hashes}, output_hashes),
        gate("blend_hash", blend_hash == manifest.get("output_hashes", {}).get("blend"), blend_hash),
        gate("geometry_proof_is_distinct", manifest.get("output_hashes", {}).get("geometry_3q") != manifest.get("output_hashes", {}).get("color_3q"), {"color_3q": manifest.get("output_hashes", {}).get("color_3q"), "geometry_3q": manifest.get("output_hashes", {}).get("geometry_3q")}),
        gate("no_image_generation_or_trellis", manifest.get("software", {}).get("image_generation") is False and manifest.get("software", {}).get("trellis") is False, manifest.get("software")),
        gate("no_unreal_or_game_ready_claim", manifest.get("unreal_authority") is False and manifest.get("fully_game_ready") is False, {"unreal_authority": manifest.get("unreal_authority"), "fully_game_ready": manifest.get("fully_game_ready")}),
    ]

    passed = sum(1 for record in gates if record["pass"])
    report = {
        "schema": "aerathea.siegebreaker.a09_pixel_half_mirror_independent_audit.v1",
        "asset": ASSET,
        "attempt": ATTEMPT,
        "contract_id": CONTRACT_ID,
        "status": "pass" if passed == len(gates) else "blocked",
        "artifact_status": "proof only",
        "gate_summary": {"passed": passed, "total": len(gates)},
        "independently_observed_bounds_cm": {"minimum": minimum, "maximum": maximum, "dimensions": dimensions},
        "independently_observed_symmetry": symmetry,
        "gates": gates,
        "decision_boundary": "Technical audit cannot approve visual fidelity; Flamestrike must decide approved, revise, rejected, or blocked from the visible review board.",
    }
    (ROOT / AUDIT_REL).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
