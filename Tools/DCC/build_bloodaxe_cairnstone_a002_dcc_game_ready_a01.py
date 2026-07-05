#!/usr/bin/env python3
"""Build the A002 DCC game-ready candidate package in Blender.

Run only after Phase 6B script creation is complete:

    blender --background --python Tools/DCC/build_bloodaxe_cairnstone_a002_dcc_game_ready_a01.py

This script consumes the passed Phase 5D texture/UV/material candidate. It may
create a DCC game-ready source blend, FBX exports, LODs, UCX collision proxies,
technical proof renders, a handoff report, and a validation manifest when the
future Phase 6C run is authorized. It does not create Unreal output.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_GIA_BloodAxeCairnstone_A002"
PACKAGE_ID = f"{ASSET_ID}_DCCGameReady_A01"
PHASE5_PACKAGE_ID = f"{ASSET_ID}_TextureUVMaterial_A01"

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
PROOF_ROOT = AUTOMATION_ROOT / "ProofRenders"

PHASE5_AUTOMATION = ROOT / "Saved" / "Automation" / "DCC" / ASSET_ID / "TextureUVMaterialA01"
PHASE5_BLEND = (
    ROOT
    / "SourceAssets"
    / "Blender"
    / "Props"
    / "Giants"
    / "BloodAxe"
    / "Cairns"
    / PHASE5_PACKAGE_ID
    / f"{ASSET_ID}_TextureUVMaterial_A01.blend"
)
PHASE5_MANIFEST = PHASE5_AUTOMATION / f"{ASSET_ID}_TextureUVMaterialA01Manifest.json"
PHASE5_AUDIT = PHASE5_AUTOMATION / f"{ASSET_ID}_TextureUVMaterialA01Audit.json"

CANDIDATE_BLEND = SOURCE_ROOT / f"{PACKAGE_ID}.blend"
BUILD_MANIFEST = AUTOMATION_ROOT / f"{ASSET_ID}_DCCGameReadyA01Manifest.json"
HANDOFF_REPORT = AUTOMATION_ROOT / f"{ASSET_ID}_DCCGameReadyA01Handoff.md"

PROOF_VIEWS = ("front", "back", "left", "right", "top", "angle")
LOD_RATIOS = {"LOD0": 1.0, "LOD1": 0.6, "LOD2": 0.35, "LOD3": 0.15}
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

COLLISION_NAMES = {
    "support_base": f"UCX_{PACKAGE_ID}_00",
    "upper_socket_ring": f"UCX_{PACKAGE_ID}_01",
    "primary_monolith": f"UCX_{PACKAGE_ID}_02",
}


def blender_args() -> list[str]:
    if "--" not in sys.argv:
        return []
    return sys.argv[sys.argv.index("--") + 1 :]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-renders", action="store_true", help="Write package without proof renders.")
    parser.add_argument("--skip-fbx", action="store_true", help="Write blend/manifests without FBX exports.")
    return parser.parse_args(blender_args())


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def configure_save_policy() -> None:
    bpy.context.preferences.filepaths.save_version = 0


def require_phase5_ready() -> dict[str, object]:
    if not PHASE5_BLEND.exists():
        raise RuntimeError(f"Missing Phase 5D blend: {relative(PHASE5_BLEND)}")
    phase5_manifest = read_json(PHASE5_MANIFEST)
    phase5_audit = read_json(PHASE5_AUDIT)
    if phase5_audit.get("status") != "pass":
        raise RuntimeError("Phase 5D audit status is not pass")
    if phase5_manifest.get("candidate_blend") != relative(PHASE5_BLEND):
        raise RuntimeError("Phase 5D manifest candidate blend path mismatch")
    return {"manifest": phase5_manifest, "audit": phase5_audit}


def open_phase5_blend() -> None:
    bpy.ops.wm.open_mainfile(filepath=str(PHASE5_BLEND))
    configure_save_policy()


def mesh_triangle_count(obj: bpy.types.Object) -> int:
    if obj.type != "MESH":
        return 0
    return sum(max(0, len(poly.vertices) - 2) for poly in obj.data.polygons)


def shipping_component_objects() -> dict[str, bpy.types.Object]:
    objects: dict[str, bpy.types.Object] = {}
    for component_id, object_name in COMPONENT_OBJECTS.items():
        obj = bpy.data.objects.get(object_name)
        if obj is None:
            raise RuntimeError(f"Missing component object: {object_name}")
        if obj.type != "MESH":
            raise RuntimeError(f"Component object is not a mesh: {object_name}")
        objects[component_id] = obj
    return objects


def vector_close(actual: Vector, expected: list[float], tolerance: float = 0.0001) -> bool:
    return all(abs(actual[index] - expected[index]) <= tolerance for index in range(3))


def validate_source_components(objects: dict[str, bpy.types.Object]) -> None:
    for component_id, obj in objects.items():
        expected = EXPECTED_TRANSFORMS[component_id]
        if not vector_close(obj.location, expected["location"]):
            raise RuntimeError(f"{obj.name} location drift")
        rotation = Vector((obj.rotation_euler.x, obj.rotation_euler.y, obj.rotation_euler.z))
        if not vector_close(rotation, expected["rotation"]):
            raise RuntimeError(f"{obj.name} rotation drift")
        if not vector_close(obj.scale, expected["scale"]):
            raise RuntimeError(f"{obj.name} scale drift")
        if "A002_SourceOwnedUV" not in [layer.name for layer in obj.data.uv_layers]:
            raise RuntimeError(f"{obj.name} missing A002_SourceOwnedUV")
        material_names = [mat.name for mat in obj.data.materials if mat]
        for material_name in MATERIAL_SLOTS:
            if material_name not in material_names:
                raise RuntimeError(f"{obj.name} missing material slot {material_name}")
        obj["a002_component_id"] = component_id
        obj["a002_phase6_shipping_component"] = True
        obj["a002_source_blend"] = relative(PHASE5_BLEND)


def set_visibility(objects: list[bpy.types.Object], visible: bool) -> None:
    for obj in objects:
        obj.hide_viewport = not visible
        obj.hide_render = not visible


def duplicate_lod_objects(objects: dict[str, bpy.types.Object]) -> dict[str, list[bpy.types.Object]]:
    lod_objects: dict[str, list[bpy.types.Object]] = {}
    for lod_id, ratio in LOD_RATIOS.items():
        lod_objects[lod_id] = []
        for component_id, source in objects.items():
            duplicate = source.copy()
            duplicate.data = source.data.copy()
            duplicate.name = f"{source.name}_{lod_id}"
            duplicate.data.name = duplicate.name
            duplicate["a002_component_id"] = component_id
            duplicate["a002_lod"] = lod_id
            bpy.context.collection.objects.link(duplicate)
            if ratio < 1.0:
                modifier = duplicate.modifiers.new(f"A002_{lod_id}_Decimate", "DECIMATE")
                modifier.ratio = ratio
                bpy.context.view_layer.objects.active = duplicate
                duplicate.select_set(True)
                bpy.ops.object.modifier_apply(modifier=modifier.name)
                duplicate.select_set(False)
            lod_objects[lod_id].append(duplicate)
    set_visibility([obj for group in lod_objects.values() for obj in group], False)
    return lod_objects


def world_bounds(obj: bpy.types.Object) -> tuple[Vector, Vector]:
    coords = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    return (
        Vector((min(v.x for v in coords), min(v.y for v in coords), min(v.z for v in coords))),
        Vector((max(v.x for v in coords), max(v.y for v in coords), max(v.z for v in coords))),
    )


def make_box_mesh(name: str, minimum: Vector, maximum: Vector) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(name)
    x0, y0, z0 = minimum
    x1, y1, z1 = maximum
    verts = [
        (x0, y0, z0),
        (x1, y0, z0),
        (x1, y1, z0),
        (x0, y1, z0),
        (x0, y0, z1),
        (x1, y0, z1),
        (x1, y1, z1),
        (x0, y1, z1),
    ]
    faces = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.display_type = "WIRE"
    obj.hide_render = True
    obj["a002_collision_proxy"] = True
    return obj


def create_collision_proxies(objects: dict[str, bpy.types.Object]) -> list[bpy.types.Object]:
    proxies: list[bpy.types.Object] = []
    for component_id, source in objects.items():
        minimum, maximum = world_bounds(source)
        proxy = make_box_mesh(COLLISION_NAMES[component_id], minimum, maximum)
        proxy["a002_collision_component_id"] = component_id
        proxies.append(proxy)
    return proxies


def select_only(objects: list[bpy.types.Object]) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    if objects:
        bpy.context.view_layer.objects.active = objects[0]


def export_fbx(path: Path, objects: list[bpy.types.Object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    visibility_state = [(obj, obj.hide_viewport, obj.hide_render, obj.hide_get()) for obj in objects]
    try:
        for obj in objects:
            obj.hide_viewport = False
            obj.hide_render = False
            obj.hide_set(False)
        bpy.context.view_layer.update()
        select_only(objects)
        selected_meshes = [obj for obj in bpy.context.selected_objects if obj.type == "MESH"]
        if len(selected_meshes) != len(objects):
            selected_names = sorted(obj.name for obj in selected_meshes)
            expected_names = sorted(obj.name for obj in objects)
            raise RuntimeError(f"FBX export selection mismatch for {path.name}: selected={selected_names} expected={expected_names}")
        bpy.ops.export_scene.fbx(
            filepath=str(path),
            use_selection=True,
            apply_unit_scale=True,
            bake_space_transform=False,
            object_types={"MESH"},
            add_leaf_bones=False,
            path_mode="RELATIVE",
        )
    finally:
        for obj, hide_viewport, hide_render, hidden in visibility_state:
            obj.hide_viewport = hide_viewport
            obj.hide_render = hide_render
            obj.hide_set(hidden)
        bpy.ops.object.select_all(action="DESELECT")


def export_package(lod_objects: dict[str, list[bpy.types.Object]], collision_objects: list[bpy.types.Object]) -> dict[str, str]:
    export_paths: dict[str, str] = {}
    for lod_id, objects in lod_objects.items():
        suffix = "" if lod_id == "LOD0" else f"_{lod_id}"
        path = EXPORT_ROOT / f"{PACKAGE_ID}{suffix}.fbx"
        export_fbx(path, objects)
        export_paths[lod_id] = relative(path)
        if lod_id == "LOD0":
            lod0_path = EXPORT_ROOT / f"{PACKAGE_ID}_LOD0.fbx"
            export_fbx(lod0_path, objects)
            export_paths["LOD0_named"] = relative(lod0_path)
    collision_path = EXPORT_ROOT / f"{PACKAGE_ID}_UCX.fbx"
    export_fbx(collision_path, collision_objects)
    export_paths["UCX"] = relative(collision_path)
    return export_paths


def scene_bounds(objects: list[bpy.types.Object]) -> tuple[Vector, Vector]:
    mins: list[Vector] = []
    maxs: list[Vector] = []
    for obj in objects:
        minimum, maximum = world_bounds(obj)
        mins.append(minimum)
        maxs.append(maximum)
    return (
        Vector((min(v.x for v in mins), min(v.y for v in mins), min(v.z for v in mins))),
        Vector((max(v.x for v in maxs), max(v.y for v in maxs), max(v.z for v in maxs))),
    )


def setup_camera(view: str, objects: list[bpy.types.Object]) -> bpy.types.Camera:
    minimum, maximum = scene_bounds(objects)
    center = (minimum + maximum) * 0.5
    extent = max((maximum - minimum).length, 220.0)
    if view == "front":
        location = center + Vector((0.0, -extent, extent * 0.35))
    elif view == "back":
        location = center + Vector((0.0, extent, extent * 0.35))
    elif view == "left":
        location = center + Vector((-extent, 0.0, extent * 0.35))
    elif view == "right":
        location = center + Vector((extent, 0.0, extent * 0.35))
    elif view == "top":
        location = center + Vector((0.0, 0.0, extent))
    else:
        location = center + Vector((extent * 0.75, -extent * 0.9, extent * 0.55))
    camera_data = bpy.data.cameras.new(f"A002_DCCGameReady_{view}_Camera")
    camera = bpy.data.objects.new(camera_data.name, camera_data)
    bpy.context.collection.objects.link(camera)
    camera.location = location
    direction = center - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.lens = 55
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = max(maximum.x - minimum.x, maximum.y - minimum.y, maximum.z - minimum.z) * 1.25
    return camera


def render_proof(path: Path, camera: bpy.types.Object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 1200
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def render_proofs(lod0_objects: list[bpy.types.Object], collision_objects: list[bpy.types.Object]) -> list[str]:
    proof_paths: list[str] = []
    set_visibility(lod0_objects, True)
    for view in PROOF_VIEWS:
        camera = setup_camera(view, lod0_objects)
        path = PROOF_ROOT / f"{ASSET_ID}_DCCGameReady_{view.title()}Proof.png"
        render_proof(path, camera)
        proof_paths.append(relative(path))
    set_visibility(collision_objects, True)
    camera = setup_camera("angle", lod0_objects + collision_objects)
    collision_path = PROOF_ROOT / f"{ASSET_ID}_DCCGameReady_CollisionProxyProof.png"
    render_proof(collision_path, camera)
    proof_paths.append(relative(collision_path))
    return proof_paths


def write_handoff(manifest: dict[str, object]) -> None:
    lines = [
        "# SM_GIA_BloodAxeCairnstone_A002 DCC Game-Ready A01 Handoff",
        "",
        "Status: `DCC game-ready candidate generated; Unreal import not run`",
        "",
        f"Asset: `{ASSET_ID}`",
        "Asset type: Static Mesh prop / possible Blueprint Actor assembly",
        "Scale: centimeters; `1 Unreal unit = 1 cm`",
        "Pivot/orientation: preserve Phase 4E snap assembly transforms.",
        "",
        "## Source",
        "",
        f"- DCC source: `{manifest['candidate_blend']}`",
        f"- Phase 5D source: `{relative(PHASE5_BLEND)}`",
        "",
        "## Exports",
        "",
    ]
    for key, path in sorted(manifest["fbx_exports"].items()):
        lines.append(f"- `{key}`: `{path}`")
    lines.extend(
        [
            "",
            "## Materials",
            "",
            "- `M_A002_SourceTemplate_Closest`",
            "- `M_A002_TaggedInferredHidden_Neutral`",
            "- No emissive map planned.",
            "",
            "## Collision",
            "",
        ]
    )
    for proxy in manifest["collision_proxies"]:
        lines.append(f"- `{proxy['name']}`: `{proxy['component_id']}`")
    lines.extend(
        [
            "",
            "## Approval Status",
            "",
            "`DCC game-ready candidate` after audit pass. Unreal import and Flamestrike final visual approval remain pending.",
        ]
    )
    HANDOFF_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_manifest(
    phase5: dict[str, object],
    lod_objects: dict[str, list[bpy.types.Object]],
    collision_objects: list[bpy.types.Object],
    fbx_exports: dict[str, str],
    proof_paths: list[str],
    skipped_fbx: bool,
) -> dict[str, object]:
    manifest = {
        "asset_id": ASSET_ID,
        "package_id": PACKAGE_ID,
        "status": "dcc_game_ready_candidate_generated",
        "script": relative(Path(__file__)),
        "phase5_blend": relative(PHASE5_BLEND),
        "phase5_manifest": relative(PHASE5_MANIFEST),
        "phase5_audit": relative(PHASE5_AUDIT),
        "candidate_blend": relative(CANDIDATE_BLEND),
        "fbx_exports": fbx_exports,
        "fbx_export_skipped": skipped_fbx,
        "lod_reports": {
            lod_id: [
                {
                    "object_name": obj.name,
                    "component_id": obj.get("a002_component_id"),
                    "triangles": mesh_triangle_count(obj),
                }
                for obj in objects
            ]
            for lod_id, objects in lod_objects.items()
        },
        "collision_proxies": [
            {"name": obj.name, "component_id": obj.get("a002_collision_component_id"), "triangles": mesh_triangle_count(obj)}
            for obj in collision_objects
        ],
        "proof_renders": proof_paths,
        "material_slots": list(MATERIAL_SLOTS),
        "component_lineage": {
            component_id: {
                "source_object": object_name,
                "phase5_source": relative(PHASE5_BLEND),
                "uv_layer": "A002_SourceOwnedUV",
                "expected_transform": EXPECTED_TRANSFORMS[component_id],
            }
            for component_id, object_name in COMPONENT_OBJECTS.items()
        },
        "core_policy": {
            "no_unreal_output": True,
            "runtime_mesh_merge": False,
            "source_image_pixel_edits": False,
            "a001_a02_generated_source_authority": False,
            "component_lineage_preserved": True,
        },
        "phase5_status": {
            "manifest_status": phase5["manifest"].get("status"),
            "audit_status": phase5["audit"].get("status"),
        },
    }
    return manifest


def main() -> int:
    args = parse_args()
    phase5 = require_phase5_ready()
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    EXPORT_ROOT.mkdir(parents=True, exist_ok=True)
    AUTOMATION_ROOT.mkdir(parents=True, exist_ok=True)
    PROOF_ROOT.mkdir(parents=True, exist_ok=True)

    open_phase5_blend()
    objects = shipping_component_objects()
    validate_source_components(objects)
    collision_objects = create_collision_proxies(objects)
    lod_objects = duplicate_lod_objects(objects)

    fbx_exports: dict[str, str] = {}
    if not args.skip_fbx:
        fbx_exports = export_package(lod_objects, collision_objects)

    proof_paths: list[str] = []
    if not args.skip_renders:
        proof_paths = render_proofs(lod_objects["LOD0"], collision_objects)

    bpy.ops.wm.save_as_mainfile(filepath=str(CANDIDATE_BLEND))
    manifest = build_manifest(phase5, lod_objects, collision_objects, fbx_exports, proof_paths, args.skip_fbx)
    BUILD_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    write_handoff(manifest)
    print(BUILD_MANIFEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
