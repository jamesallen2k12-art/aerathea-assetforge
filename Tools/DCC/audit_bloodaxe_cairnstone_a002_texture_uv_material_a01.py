#!/usr/bin/env python3
"""Audit the A002 texture/UV/material candidate."""

from __future__ import annotations

import json
from pathlib import Path

import bpy


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_GIA_BloodAxeCairnstone_A002"
PACKAGE_ID = f"{ASSET_ID}_TextureUVMaterial_A01"
AUTOMATION_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_ID / "TextureUVMaterialA01"
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
OWNERSHIP_MANIFEST = AUTOMATION_ROOT / f"{ASSET_ID}_TextureUVMaterialA01OwnershipManifest.json"
BUILD_MANIFEST = AUTOMATION_ROOT / f"{ASSET_ID}_TextureUVMaterialA01Manifest.json"
AUDIT_PATH = AUTOMATION_ROOT / f"{ASSET_ID}_TextureUVMaterialA01Audit.json"
CANDIDATE_BLEND = SOURCE_ROOT / f"{ASSET_ID}_TextureUVMaterial_A01.blend"
SOURCE_IMAGE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"

COMPONENT_OBJECTS = {
    "primary_monolith": "SM_GIA_BloodAxeCairnstone_A002_PrimaryMonolith",
    "upper_socket_ring": "SM_GIA_BloodAxeCairnstone_A002_UpperSocketRing",
    "support_base": "SM_GIA_BloodAxeCairnstone_A002_SupportBase",
}
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


def source_texture_nodes() -> list[dict[str, str]]:
    reports: list[dict[str, str]] = []
    for mat in bpy.data.materials:
        if not mat.use_nodes or not mat.node_tree:
            continue
        for node in mat.node_tree.nodes:
            if node.type == "TEX_IMAGE" and node.image:
                reports.append(
                    {
                        "material": mat.name,
                        "node": node.name,
                        "image": node.image.filepath or node.image.filepath_raw or node.image.name,
                        "interpolation": getattr(node, "interpolation", ""),
                    }
                )
    return reports


def audit_blend(failures: list[str]) -> list[dict[str, object]]:
    if not CANDIDATE_BLEND.exists():
        failures.append(f"Missing candidate blend: {relative(CANDIDATE_BLEND)}")
        return []
    bpy.ops.wm.open_mainfile(filepath=str(CANDIDATE_BLEND))
    component_reports: list[dict[str, object]] = []
    for component_id, object_name in COMPONENT_OBJECTS.items():
        obj = bpy.data.objects.get(object_name)
        if obj is None:
            failures.append(f"Missing component object: {object_name}")
            continue
        if obj.type != "MESH":
            failures.append(f"{object_name} is not a mesh")
            continue
        uv_layers = [layer.name for layer in obj.data.uv_layers]
        if "A002_SourceOwnedUV" not in uv_layers:
            failures.append(f"{object_name} missing A002_SourceOwnedUV layer")
        if obj.get("a002_uv_ownership_manifest") != relative(OWNERSHIP_MANIFEST):
            failures.append(f"{object_name} missing ownership manifest metadata")
        component_reports.append(
            {
                "component_id": component_id,
                "object_name": object_name,
                "uv_layers": uv_layers,
                "material_slots": [mat.name for mat in obj.data.materials if mat],
            }
        )
    texture_nodes = source_texture_nodes()
    source_node_paths = [report["image"] for report in texture_nodes]
    if not any(str(SOURCE_IMAGE) in path or SOURCE_IMAGE.name in path for path in source_node_paths):
        failures.append("No source template image texture node found")
    for report in texture_nodes:
        if report["interpolation"] != "Closest":
            failures.append(f"Texture node {report['node']} is not Closest interpolation")
    return component_reports


def audit_files(build_manifest: dict[str, object], failures: list[str]) -> None:
    if build_manifest.get("ownership_manifest") != relative(OWNERSHIP_MANIFEST):
        failures.append("Build manifest ownership manifest path mismatch")
    for view in PROOF_VIEWS:
        proof = AUTOMATION_ROOT / "ProofRenders" / f"{ASSET_ID}_TextureUVMaterial_{view.title()}Proof.png"
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
    ownership = read_json(OWNERSHIP_MANIFEST, failures)
    build_manifest = read_json(BUILD_MANIFEST, failures)
    component_reports = audit_blend(failures)
    audit_files(build_manifest, failures)
    report = {
        "asset_id": ASSET_ID,
        "package_id": PACKAGE_ID,
        "status": "pass" if not failures else "fail",
        "ownership_status": ownership.get("status") if ownership else None,
        "candidate_blend": relative(CANDIDATE_BLEND),
        "component_reports": component_reports,
        "texture_nodes": source_texture_nodes() if CANDIDATE_BLEND.exists() else [],
        "failures": failures,
    }
    AUTOMATION_ROOT.mkdir(parents=True, exist_ok=True)
    AUDIT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(AUDIT_PATH)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("A002 texture/UV/material candidate audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
