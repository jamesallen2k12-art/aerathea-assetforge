#!/usr/bin/env python3
"""Audit the A002 DCC game-ready candidate package."""

from __future__ import annotations

import json
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_GIA_BloodAxeCairnstone_A002"
PACKAGE_ID = f"{ASSET_ID}_DCCGameReady_A01"

AUTOMATION_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_ID / "DCCGameReadyA01"
SOURCE_ROOT = (
    ROOT
    / "SourceAssets"
    / "Blender"
    / "Props"
    / "Giants"
    / "BloodAxe"
    / "Cairns"
    / PACKAGE_ID
)
EXPORT_ROOT = (
    ROOT
    / "SourceAssets"
    / "Exports"
    / "Props"
    / "Giants"
    / "BloodAxe"
    / "Cairns"
    / PACKAGE_ID
)
PHASE5_AUTOMATION = ROOT / "Saved" / "Automation" / "DCC" / ASSET_ID / "TextureUVMaterialA01"
PHASE5_AUDIT = PHASE5_AUTOMATION / f"{ASSET_ID}_TextureUVMaterialA01Audit.json"
CANDIDATE_BLEND = SOURCE_ROOT / f"{PACKAGE_ID}.blend"
BUILD_MANIFEST = AUTOMATION_ROOT / f"{ASSET_ID}_DCCGameReadyA01Manifest.json"
AUDIT_PATH = AUTOMATION_ROOT / f"{ASSET_ID}_DCCGameReadyA01Audit.json"
HANDOFF_REPORT = AUTOMATION_ROOT / f"{ASSET_ID}_DCCGameReadyA01Handoff.md"

PROOF_EXPECTED = (
    "FrontProof",
    "BackProof",
    "LeftProof",
    "RightProof",
    "TopProof",
    "AngleProof",
    "CollisionProxyProof",
)
MATERIAL_SLOTS = ("M_A002_SourceTemplate_Closest", "M_A002_TaggedInferredHidden_Neutral")
COMPONENT_OBJECTS = {
    "primary_monolith": "SM_GIA_BloodAxeCairnstone_A002_PrimaryMonolith",
    "upper_socket_ring": "SM_GIA_BloodAxeCairnstone_A002_UpperSocketRing",
    "support_base": "SM_GIA_BloodAxeCairnstone_A002_SupportBase",
}
EXPECTED_TRANSFORMS = {
    "support_base": {"location": [0.0, 0.0, 0.0], "rotation": [0.0, 0.0, 0.0], "scale": [1.0, 1.0, 1.0]},
    "upper_socket_ring": {"location": [0.0, 0.0, 0.0], "rotation": [0.0, 0.0, 0.0], "scale": [1.0, 1.0, 1.0]},
    "primary_monolith": {
        "location": [6.7158670425, 0.4247104228, 0.0],
        "rotation": [0.0, 0.0, 0.0],
        "scale": [1.0, 1.0, 1.0],
    },
}


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_json(path: Path, failures: list[str]) -> dict[str, object]:
    if not path.exists():
        failures.append(f"Missing JSON file: {relative(path)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        failures.append(f"Invalid JSON {relative(path)}: {exc}")
        return {}


def mesh_triangle_count(obj: bpy.types.Object) -> int:
    if obj.type != "MESH":
        return 0
    return sum(max(0, len(poly.vertices) - 2) for poly in obj.data.polygons)


def vector_close(actual: Vector, expected: list[float], tolerance: float = 0.0001) -> bool:
    return all(abs(actual[index] - expected[index]) <= tolerance for index in range(3))


def audit_component_objects(failures: list[str]) -> list[dict[str, object]]:
    if not CANDIDATE_BLEND.exists():
        failures.append(f"Missing DCC game-ready blend: {relative(CANDIDATE_BLEND)}")
        return []
    bpy.ops.wm.open_mainfile(filepath=str(CANDIDATE_BLEND))
    reports: list[dict[str, object]] = []
    for component_id, object_name in COMPONENT_OBJECTS.items():
        obj = bpy.data.objects.get(object_name)
        if obj is None:
            failures.append(f"Missing component object: {object_name}")
            continue
        if obj.type != "MESH":
            failures.append(f"{object_name} is not a mesh")
            continue
        expected = EXPECTED_TRANSFORMS[component_id]
        rotation = Vector((obj.rotation_euler.x, obj.rotation_euler.y, obj.rotation_euler.z))
        if not vector_close(obj.location, expected["location"]):
            failures.append(f"{object_name} location drift")
        if not vector_close(rotation, expected["rotation"]):
            failures.append(f"{object_name} rotation drift")
        if not vector_close(obj.scale, expected["scale"]):
            failures.append(f"{object_name} scale drift")
        uv_layers = [layer.name for layer in obj.data.uv_layers]
        if "A002_SourceOwnedUV" not in uv_layers:
            failures.append(f"{object_name} missing A002_SourceOwnedUV")
        material_names = [mat.name for mat in obj.data.materials if mat]
        for material_name in MATERIAL_SLOTS:
            if material_name not in material_names:
                failures.append(f"{object_name} missing material slot {material_name}")
        reports.append(
            {
                "component_id": component_id,
                "object_name": object_name,
                "triangles": mesh_triangle_count(obj),
                "uv_layers": uv_layers,
                "material_slots": material_names,
            }
        )
    return reports


def audit_manifest(manifest: dict[str, object], phase5_audit: dict[str, object], failures: list[str]) -> None:
    if phase5_audit.get("status") != "pass":
        failures.append("Phase 5D audit status is not pass")
    if manifest.get("status") != "dcc_game_ready_candidate_generated":
        failures.append("Build manifest status mismatch")
    if manifest.get("candidate_blend") != relative(CANDIDATE_BLEND):
        failures.append("Build manifest candidate blend path mismatch")
    if not manifest.get("core_policy", {}).get("no_unreal_output", False):
        failures.append("Manifest does not confirm no Unreal output")
    if manifest.get("core_policy", {}).get("runtime_mesh_merge", True):
        failures.append("Manifest indicates runtime mesh merge occurred")
    if manifest.get("core_policy", {}).get("source_image_pixel_edits", True):
        failures.append("Manifest indicates source image pixel edits")
    if manifest.get("core_policy", {}).get("a001_a02_generated_source_authority", True):
        failures.append("Manifest indicates A001/A02 source authority use")
    lod_reports = manifest.get("lod_reports", {})
    for lod_id in ("LOD0", "LOD1", "LOD2", "LOD3"):
        if lod_id not in lod_reports:
            failures.append(f"Missing LOD report: {lod_id}")
        elif not lod_reports[lod_id]:
            failures.append(f"Empty LOD report: {lod_id}")
    collision = manifest.get("collision_proxies", [])
    if len(collision) < 3:
        failures.append("Expected at least three collision proxy reports")
    for proxy in collision:
        name = str(proxy.get("name", ""))
        if not name.startswith(f"UCX_{PACKAGE_ID}_"):
            failures.append(f"Collision proxy has invalid UCX name: {name}")


def audit_files(manifest: dict[str, object], failures: list[str]) -> None:
    if not HANDOFF_REPORT.exists():
        failures.append(f"Missing handoff report: {relative(HANDOFF_REPORT)}")
    fbx_exports = manifest.get("fbx_exports", {})
    required_keys = ("LOD0", "LOD0_named", "LOD1", "LOD2", "LOD3", "UCX")
    for key in required_keys:
        path_value = fbx_exports.get(key)
        if not path_value:
            failures.append(f"Missing FBX export path in manifest: {key}")
            continue
        path = ROOT / path_value
        if not path.exists():
            failures.append(f"Missing FBX export file: {path_value}")
    proof_paths = set(manifest.get("proof_renders", []))
    for label in PROOF_EXPECTED:
        expected = relative(AUTOMATION_ROOT / "ProofRenders" / f"{ASSET_ID}_DCCGameReady_{label}.png")
        if expected not in proof_paths:
            failures.append(f"Missing proof render in manifest: {expected}")
        elif not (ROOT / expected).exists():
            failures.append(f"Missing proof render file: {expected}")
    blocked_unreal_paths = [
        ROOT / "Content" / "Aerathea" / "Props" / "Giants" / "BloodAxe" / "Cairns" / PACKAGE_ID,
        ROOT / "Content" / "Aerathea" / "Props" / "Giants" / "BloodAxe" / "Cairns" / ASSET_ID,
    ]
    for path in blocked_unreal_paths:
        if path.exists():
            failures.append(f"Blocked Unreal output exists: {relative(path)}")


def main() -> int:
    failures: list[str] = []
    phase5_audit = read_json(PHASE5_AUDIT, failures)
    manifest = read_json(BUILD_MANIFEST, failures)
    component_reports = audit_component_objects(failures)
    if manifest:
        audit_manifest(manifest, phase5_audit, failures)
        audit_files(manifest, failures)
    report = {
        "asset_id": ASSET_ID,
        "package_id": PACKAGE_ID,
        "status": "pass" if not failures else "fail",
        "candidate_blend": relative(CANDIDATE_BLEND),
        "component_reports": component_reports,
        "manifest": relative(BUILD_MANIFEST),
        "handoff_report": relative(HANDOFF_REPORT),
        "failures": failures,
    }
    AUTOMATION_ROOT.mkdir(parents=True, exist_ok=True)
    AUDIT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(AUDIT_PATH)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("A002 DCC game-ready candidate audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
