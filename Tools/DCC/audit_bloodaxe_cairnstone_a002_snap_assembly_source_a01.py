#!/usr/bin/env python3
"""Audit the A002 snap assembly source candidate."""

from __future__ import annotations

import json
import math
from pathlib import Path

import bpy


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_GIA_BloodAxeCairnstone_A002"
PACKAGE_ID = f"{ASSET_ID}_SnapAssemblySource_A01"
AUTOMATION_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_ID / "SnapAssemblySourceA01"
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
ANCHOR_MANIFEST = AUTOMATION_ROOT / f"{ASSET_ID}_SnapAssemblySourceA01AnchorManifest.json"
BUILD_MANIFEST = AUTOMATION_ROOT / f"{ASSET_ID}_SnapAssemblySourceA01Manifest.json"
AUDIT_PATH = AUTOMATION_ROOT / f"{ASSET_ID}_SnapAssemblySourceA01Audit.json"
ASSEMBLY_BLEND = SOURCE_ROOT / f"{ASSET_ID}_Assembled_Proof.blend"
PROOF_ROOT = AUTOMATION_ROOT / "ProofRenders"

COMPONENT_IDS = ("support_base", "upper_socket_ring", "primary_monolith")
PROOF_VIEWS = ("front", "back", "left", "right", "top", "angle")


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


def material_uses_texture_nodes(material: bpy.types.Material) -> bool:
    if not material.use_nodes or not material.node_tree:
        return False
    return any(node.type == "TEX_IMAGE" for node in material.node_tree.nodes)


def external_images() -> list[str]:
    return sorted(image.name for image in bpy.data.images if image.name not in {"Render Result", "Viewer Node"})


def nearly_equal(actual: float, expected: float) -> bool:
    return abs(float(actual) - float(expected)) <= 0.0001


def audit_blend(anchor_manifest: dict[str, object], failures: list[str]) -> list[dict[str, object]]:
    if not ASSEMBLY_BLEND.exists():
        failures.append(f"Missing assembly blend: {relative(ASSEMBLY_BLEND)}")
        return []
    bpy.ops.wm.open_mainfile(filepath=str(ASSEMBLY_BLEND))
    transforms = anchor_manifest.get("assembly_transforms_cm", {})
    components = anchor_manifest.get("approved_component_sources", {})
    reports: list[dict[str, object]] = []

    for component_id in COMPONENT_IDS:
        spec = components.get(component_id, {})
        expected_name = spec.get("asset_name")
        obj = bpy.data.objects.get(str(expected_name))
        if obj is None:
            failures.append(f"Missing assembly component object: {expected_name}")
            continue
        expected_transform = transforms.get(component_id, {})
        expected_location = expected_transform.get("location", [])
        expected_rotation = expected_transform.get("rotation_degrees", [])
        expected_scale = expected_transform.get("scale", [])
        if len(expected_location) != 3 or len(expected_rotation) != 3 or len(expected_scale) != 3:
            failures.append(f"{component_id}: incomplete expected transform")
            continue
        for axis, actual, expected in zip("XYZ", obj.location, expected_location):
            if not nearly_equal(actual, expected):
                failures.append(f"{component_id}: location {axis} mismatch, got {actual}, expected {expected}")
        for axis, actual, expected in zip("XYZ", obj.rotation_euler, expected_rotation):
            actual_degrees = math.degrees(float(actual))
            if not nearly_equal(actual_degrees, expected):
                failures.append(f"{component_id}: rotation {axis} mismatch, got {actual_degrees}, expected {expected}")
        for axis, actual, expected in zip("XYZ", obj.scale, expected_scale):
            if not nearly_equal(actual, expected):
                failures.append(f"{component_id}: scale {axis} mismatch, got {actual}, expected {expected}")
        if obj.get("a002_assembly_component_id") != component_id:
            failures.append(f"{component_id}: missing or wrong assembly component metadata")
        reports.append(
            {
                "component_id": component_id,
                "object_name": obj.name,
                "location": [round(float(v), 10) for v in obj.location],
                "rotation_degrees": [round(math.degrees(float(v)), 10) for v in obj.rotation_euler],
                "scale": [round(float(v), 10) for v in obj.scale],
            }
        )

    uv_violations: list[str] = []
    texture_node_violations: list[str] = []
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        if obj.name.startswith("MARKER_"):
            continue
        if len(obj.data.uv_layers) != 0:
            uv_violations.append(obj.name)
        for mat in obj.data.materials:
            if mat is not None and material_uses_texture_nodes(mat):
                texture_node_violations.append(mat.name)
    if uv_violations:
        failures.append(f"UV layers found on assembly meshes: {uv_violations}")
    if texture_node_violations:
        failures.append(f"Texture nodes found on materials: {texture_node_violations}")
    images = external_images()
    if images:
        failures.append(f"External image datablocks found: {images}")
    marker_count = len([obj for obj in bpy.data.objects if obj.name.startswith("MARKER_A002_")])
    if marker_count < len(anchor_manifest.get("anchor_pairs", [])):
        failures.append("Not all snap anchor pairs have marker objects")
    return reports


def audit_files(anchor_manifest: dict[str, object], build_manifest: dict[str, object], failures: list[str]) -> None:
    if anchor_manifest.get("assembly_generation_authorized") is not True:
        failures.append("Anchor manifest does not authorize assembly generation")
    if build_manifest.get("anchor_manifest") != relative(ANCHOR_MANIFEST):
        failures.append("Build manifest anchor manifest path mismatch")
    for view in PROOF_VIEWS:
        proof = PROOF_ROOT / f"{ASSET_ID}_SnapAssembly_{view.title()}Proof.png"
        if not proof.exists():
            failures.append(f"Missing proof render: {relative(proof)}")
    blocked_paths = [
        ROOT / "SourceAssets" / "FBX" / ASSET_ID,
        ROOT / "Content" / "Props" / "Giants" / "BloodAxe" / "Cairns" / ASSET_ID,
    ]
    for path in blocked_paths:
        if path.exists():
            failures.append(f"Blocked downstream output exists: {relative(path)}")


def main() -> int:
    failures: list[str] = []
    anchor_manifest = read_json(ANCHOR_MANIFEST, failures)
    build_manifest = read_json(BUILD_MANIFEST, failures)
    component_reports = audit_blend(anchor_manifest, failures) if anchor_manifest else []
    audit_files(anchor_manifest, build_manifest, failures)
    report = {
        "asset_id": ASSET_ID,
        "package_id": PACKAGE_ID,
        "status": "pass" if not failures else "fail",
        "assembly_blend": relative(ASSEMBLY_BLEND),
        "component_reports": component_reports,
        "failures": failures,
    }
    AUTOMATION_ROOT.mkdir(parents=True, exist_ok=True)
    AUDIT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(AUDIT_PATH)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("A002 snap assembly source audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
