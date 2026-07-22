#!/usr/bin/env python3
"""Independently audit the saved A08 Step 01 pommel A06 Blender candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
SOURCE_REL = Path("SourceAssets/Concepts/SiegeBreaker/siege_breaker_concept_view.png")
SOURCE_SHA256 = "9f1ac142a5047968bb20c74216c2dccf61470ed9f4e21689ff01934bd849c586"
MANIFEST_REL = Path("docs/assets/blueprints") / ASSET / "manifests/A08_STEP_01_POMMEL_A06_VALIDATION.json"
AUDIT_REL = Path("docs/assets/blueprints") / ASSET / "manifests/A08_STEP_01_POMMEL_A06_INDEPENDENT_AUDIT.json"
REVIEW_REL = Path("docs/assets/blueprints") / ASSET / "review/A08_STEP_01_POMMEL_A06_REVIEW.png"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def gate(name: str, passed: bool, evidence: Any) -> Dict[str, Any]:
    return {"name": name, "pass": bool(passed), "evidence": evidence}


def main() -> int:
    import bpy
    from bpy_extras.object_utils import world_to_camera_view
    from mathutils import Vector

    scene = bpy.context.scene
    manifest = json.loads((ROOT / MANIFEST_REL).read_text(encoding="utf-8"))
    root = bpy.data.objects.get("SB_C006_Pommel_A08_ROOT")
    collection = bpy.data.collections.get("A08_POMMEL_CANDIDATE")
    review_collection = bpy.data.collections.get("A08_REVIEW_ONLY")
    if root is None or collection is None or review_collection is None:
        raise RuntimeError("required A08 collections or root are missing")

    mesh_objects = [obj for obj in collection.objects if obj.type == "MESH"]
    local_points = [obj.matrix_local @ Vector(corner) for obj in mesh_objects for corner in obj.bound_box]
    minimum = [min(float(point[index]) for point in local_points) for index in range(3)]
    maximum = [max(float(point[index]) for point in local_points) for index in range(3)]
    extent = [maximum[index] - minimum[index] for index in range(3)]

    world_points = [obj.matrix_world @ Vector(corner) for obj in mesh_objects for corner in obj.bound_box]
    projections = [world_to_camera_view(scene, scene.camera, point) for point in world_points]
    frame_min = [min(float(point[index]) for point in projections) for index in range(2)]
    frame_max = [max(float(point[index]) for point in projections) for index in range(2)]

    source_display = bpy.data.objects.get("Immutable_Source_Pommel_Display")
    source_projected = []
    if source_display is not None:
        source_projected = [world_to_camera_view(scene, scene.camera, source_display.matrix_world @ vertex.co) for vertex in source_display.data.vertices]

    object_names = {obj.name for obj in mesh_objects}
    image_paths = []
    for image in bpy.data.images:
        if not image.filepath:
            continue
        path = Path(bpy.path.abspath(image.filepath)).resolve()
        image_paths.append(str(path))

    required_name_fragments = [
        "FacetedBody",
        "UpperCollar",
        "LowerForgedBand",
        "FrontRecess",
        "BronzeFrame",
        "SteelFrame",
        "RuneCrystal",
        "LeftPanelFrame",
        "RightPanelFrame",
        "Rivet",
    ]

    gates: List[Dict[str, Any]] = [
        gate("source_hash", sha256_file(ROOT / SOURCE_REL) == SOURCE_SHA256, sha256_file(ROOT / SOURCE_REL)),
        gate("contract_id", scene.get("aerathea_contract_id") == "SB-BSR-A08-STEP01-POMMEL", scene.get("aerathea_contract_id")),
        gate("blender_only", scene.get("aerathea_generation_software_used") == "Blender only", scene.get("aerathea_generation_software_used")),
        gate("historical_geometry_inputs_zero", scene.get("aerathea_historical_geometry_inputs") == 0, scene.get("aerathea_historical_geometry_inputs")),
        gate("hidden_surface_authority_false", not bool(scene.get("aerathea_hidden_surface_authority")), scene.get("aerathea_hidden_surface_authority")),
        gate("height_18_cm", abs(extent[2] - 18.0) <= 0.001, extent[2]),
        gate("width_11_cm", abs(extent[0] - 11.0) <= 0.001, extent[0]),
        gate("origin_z_zero", abs(minimum[2]) <= 0.001, minimum[2]),
        gate("candidate_fully_in_frame", frame_min[0] >= 0.0 and frame_min[1] >= 0.0 and frame_max[0] <= 1.0 and frame_max[1] <= 1.0, {"minimum": frame_min, "maximum": frame_max}),
        gate(
            "source_display_fully_in_frame",
            bool(source_projected) and min(point.x for point in source_projected) >= 0.0 and min(point.y for point in source_projected) >= 0.0 and max(point.x for point in source_projected) <= 1.0 and max(point.y for point in source_projected) <= 1.0,
            [[float(point.x), float(point.y)] for point in source_projected],
        ),
        gate("source_labels_present", {"AUTHORITATIVE_SOURCE", "UNCHANGED_CONCEPT_UV_WINDOW"}.issubset(set(bpy.data.objects.keys())), sorted(name for name in bpy.data.objects.keys() if "SOURCE" in name or "CONCEPT" in name)),
        gate("required_visible_groups", all(any(fragment in name for name in object_names) for fragment in required_name_fragments), required_name_fragments),
        gate("review_file_exists", (ROOT / REVIEW_REL).is_file(), str(REVIEW_REL)),
        gate("review_hash_matches_manifest", sha256_file(ROOT / REVIEW_REL) == manifest["outputs"]["review"]["sha256"], sha256_file(ROOT / REVIEW_REL)),
        gate("manifest_candidate_status", manifest["status"] == "candidate_pending_flamestrike_visual_decision", manifest["status"]),
        gate("no_external_generated_images_loaded", set(image_paths).issubset({str((ROOT / SOURCE_REL).resolve())}), image_paths),
        gate("unreal_outputs_zero", manifest["unreal_outputs"] == 0, manifest["unreal_outputs"]),
        gate("fully_game_ready_false", manifest["fully_game_ready"] is False, manifest["fully_game_ready"]),
    ]
    passed = sum(1 for record in gates if record["pass"])
    report = {
        "schema": "aerathea.siegebreaker_a08_pommel_a06_independent_audit.v1",
        "asset_id": ASSET,
        "contract_id": "SB-BSR-A08-STEP01-POMMEL",
        "status": "pass" if passed == len(gates) else "blocked",
        "artifact_status": "proof only",
        "gate_summary": {"passed": passed, "total": len(gates)},
        "local_bounds_cm": {"minimum": minimum, "maximum": maximum, "extent": extent},
        "gates": gates,
        "decision_boundary": "Technical pass cannot approve visual fidelity; Flamestrike decision remains required.",
    }
    (ROOT / AUDIT_REL).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
