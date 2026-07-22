#!/usr/bin/env python3
"""Independently audit A10 orthographics and the unchanged approved A09 source."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
CONTRACT_ID = "SB-ORTHO-A10-DERIVED-A01"
MODEL_NAME = f"{ASSET}_A09_CompleteMirroredModel"
EXPECTED_BLEND_SHA256 = "06ffb121d00cddb7b9e30a60067a5036a851d285f15daca3bffe3a663fd6d78f"
EXPECTED_DIMENSIONS_CM = [75.130516, 32.957619, 170.0]
EXPECTED_VERTICES = 435278
EXPECTED_POLYGONS = 435276
EXPECTED_VIEWS = ("front", "back", "left", "right", "top", "bottom")
MANIFEST_REL = Path("docs/assets/blueprints") / ASSET / "manifests/A10_DERIVED_ORTHOGRAPHICS_A01_VALIDATION.json"
AUDIT_REL = Path("docs/assets/blueprints") / ASSET / "manifests/A10_DERIVED_ORTHOGRAPHICS_A01_INDEPENDENT_AUDIT.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def gate(name: str, passed: bool, evidence: Any) -> Dict[str, Any]:
    return {"name": name, "pass": bool(passed), "evidence": evidence}


def vector_close(observed: List[float], expected: List[float], tolerance: float = 0.00001) -> bool:
    return len(observed) == len(expected) and all(
        abs(float(value) - float(target)) <= tolerance
        for value, target in zip(observed, expected)
    )


def main() -> int:
    import bpy
    from PIL import Image, ImageStat

    manifest = json.loads((ROOT / MANIFEST_REL).read_text(encoding="utf-8"))
    blend_path = ROOT / manifest["authority"]["approved_a09_blend"]
    current_blend_hash = sha256_file(blend_path)
    model = bpy.data.objects.get(MODEL_NAME)
    if model is None or model.type != "MESH":
        raise RuntimeError(f"required approved model missing: {MODEL_NAME}")

    points = [model.matrix_world @ vertex.co for vertex in model.data.vertices]
    minimum = [min(float(point[axis]) for point in points) for axis in range(3)]
    maximum = [max(float(point[axis]) for point in points) for axis in range(3)]
    dimensions = [maximum[axis] - minimum[axis] for axis in range(3)]
    center = [(minimum[axis] + maximum[axis]) * 0.5 for axis in range(3)]

    outputs = manifest["outputs"]
    individual_paths = {name: ROOT / outputs[name] for name in EXPECTED_VIEWS}
    all_paths = {**individual_paths, "review_board": ROOT / outputs["review_board"]}
    observed_hashes = {name: sha256_file(path) for name, path in all_paths.items()}
    image_sizes = {}
    image_stddev = {}
    for name, path in all_paths.items():
        with Image.open(path) as image:
            rgb = image.convert("RGB")
            image_sizes[name] = list(rgb.size)
            image_stddev[name] = [round(float(value), 6) for value in ImageStat.Stat(rgb).stddev]

    target = manifest["camera_contract"]["target_cm"]
    expected_offsets = {
        "front": [0.0, -420.0, 0.0],
        "back": [0.0, 420.0, 0.0],
        "left": [-420.0, 0.0, 0.0],
        "right": [420.0, 0.0, 0.0],
        "top": [0.0, 0.0, 420.0],
        "bottom": [0.0, 0.0, -420.0],
    }
    observed_offsets = {
        name: [
            float(camera["location_cm"][axis]) - float(target[axis])
            for axis in range(3)
        ]
        for name, camera in manifest["camera_contract"]["cameras"].items()
    }

    common_scale = float(manifest["camera_contract"]["common_ortho_scale_cm"])
    resolution = manifest["camera_contract"]["resolution_px"]
    horizontal_span = common_scale * float(resolution[0]) / float(resolution[1])
    projected_extents = {
        "front_back": [dimensions[0], dimensions[2]],
        "left_right": [dimensions[1], dimensions[2]],
        "top_bottom": [dimensions[0], dimensions[1]],
    }
    frame_containment = all(
        extent[0] <= horizontal_span and extent[1] <= common_scale
        for extent in projected_extents.values()
    )

    gates: List[Dict[str, Any]] = [
        gate("schema", manifest.get("schema") == "aerathea.siegebreaker.a10_derived_orthographics_validation.v1", manifest.get("schema")),
        gate("contract_id", manifest.get("contract_id") == CONTRACT_ID, manifest.get("contract_id")),
        gate("candidate_status", manifest.get("artifact_status") == "candidate derived orthographic review pending Flamestrike decision", manifest.get("artifact_status")),
        gate("approved_source_hash_current", current_blend_hash == EXPECTED_BLEND_SHA256, current_blend_hash),
        gate("approved_source_hash_unchanged", manifest["authority"].get("unchanged") is True and manifest["authority"].get("required_sha256") == EXPECTED_BLEND_SHA256 and manifest["authority"].get("hash_before_render") == EXPECTED_BLEND_SHA256 and manifest["authority"].get("hash_after_render") == EXPECTED_BLEND_SHA256, manifest["authority"]),
        gate("approved_model_object", manifest["authority"].get("model_object") == MODEL_NAME and model.name == MODEL_NAME, model.name),
        gate("independent_dimensions", vector_close(dimensions, EXPECTED_DIMENSIONS_CM), dimensions),
        gate("manifest_bounds_match", vector_close(manifest["model"]["bounds"]["minimum_cm"], minimum) and vector_close(manifest["model"]["bounds"]["maximum_cm"], maximum), {"minimum_cm": minimum, "maximum_cm": maximum}),
        gate("mesh_counts", len(model.data.vertices) == EXPECTED_VERTICES and len(model.data.polygons) == EXPECTED_POLYGONS and manifest["model"].get("vertices") == EXPECTED_VERTICES and manifest["model"].get("polygons") == EXPECTED_POLYGONS, {"vertices": len(model.data.vertices), "polygons": len(model.data.polygons)}),
        gate("identity_transform", vector_close(list(model.location), [0.0, 0.0, 0.0]) and vector_close(list(model.rotation_euler), [0.0, 0.0, 0.0]) and vector_close(list(model.scale), [1.0, 1.0, 1.0]), {"location": list(model.location), "rotation_euler": list(model.rotation_euler), "scale": list(model.scale)}),
        gate("six_exact_views", set(EXPECTED_VIEWS).issubset(outputs.keys()), sorted(outputs.keys())),
        gate("all_outputs_exist", all(path.is_file() and path.stat().st_size > 0 for path in all_paths.values()), {name: path.stat().st_size if path.is_file() else 0 for name, path in all_paths.items()}),
        gate("output_hashes", observed_hashes == manifest.get("output_hashes"), observed_hashes),
        gate("individual_hashes_unique", len({observed_hashes[name] for name in EXPECTED_VIEWS}) == len(EXPECTED_VIEWS), {name: observed_hashes[name] for name in EXPECTED_VIEWS}),
        gate("individual_resolution", all(image_sizes[name] == [1200, 1600] for name in EXPECTED_VIEWS), {name: image_sizes[name] for name in EXPECTED_VIEWS}),
        gate("review_board_resolution", image_sizes["review_board"] == [3300, 3300], image_sizes["review_board"]),
        gate("nonblank_images", all(max(image_stddev[name]) >= 3.0 for name in all_paths), image_stddev),
        gate("orthographic_projection", manifest["camera_contract"].get("projection") == "ORTHO" and all(camera.get("type") == "ORTHO" for camera in manifest["camera_contract"]["cameras"].values()), manifest["camera_contract"].get("projection")),
        gate("one_common_metric_scale", common_scale == 190.0 and all(float(camera.get("ortho_scale_cm")) == common_scale for camera in manifest["camera_contract"]["cameras"].values()), common_scale),
        gate("camera_axis_offsets", all(vector_close(observed_offsets[name], expected_offsets[name]) for name in EXPECTED_VIEWS), observed_offsets),
        gate("camera_target_is_bounds_center", vector_close(target, center), {"target_cm": target, "bounds_center_cm": center}),
        gate("common_frame_contains_all_projections", frame_containment, {"horizontal_span_cm": horizontal_span, "vertical_span_cm": common_scale, "projected_extents_cm": projected_extents}),
        gate("source_not_saved", manifest.get("source_file_saved") is False, manifest.get("source_file_saved")),
        gate("no_image_generation_trellis_or_image_to_3d", manifest["software"].get("image_generation") is False and manifest["software"].get("trellis") is False and manifest["software"].get("image_to_3d") is False, manifest["software"]),
        gate("no_unreal_or_game_ready_claim", manifest.get("unreal_authority") is False and manifest.get("fully_game_ready") is False, {"unreal_authority": manifest.get("unreal_authority"), "fully_game_ready": manifest.get("fully_game_ready")}),
    ]

    passed = sum(1 for record in gates if record["pass"])
    report = {
        "schema": "aerathea.siegebreaker.a10_derived_orthographics_independent_audit.v1",
        "asset": ASSET,
        "contract_id": CONTRACT_ID,
        "status": "pass" if passed == len(gates) else "blocked",
        "artifact_status": "proof only",
        "gate_summary": {"passed": passed, "total": len(gates)},
        "independent_bounds_cm": {"minimum": minimum, "maximum": maximum, "dimensions": dimensions},
        "observed_output_hashes": observed_hashes,
        "gates": gates,
        "decision_boundary": "Technical audit cannot approve the revealed orthographic appearance; Flamestrike decision remains required.",
    }
    (ROOT / AUDIT_REL).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
