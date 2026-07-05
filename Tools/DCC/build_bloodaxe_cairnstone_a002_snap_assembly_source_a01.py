#!/usr/bin/env python3
"""Build the A002 snap assembly source candidate in Blender.

Run only after Phase 4D script creation is complete:

    blender --background --python Tools/DCC/build_bloodaxe_cairnstone_a002_snap_assembly_source_a01.py

This script consumes the A002 assembly-ready snap-anchor manifest. It does not
create UVs, texture nodes, FBX exports, Unreal output, or a final runtime merge.
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
PROOF_ROOT = AUTOMATION_ROOT / "ProofRenders"
ANCHOR_MANIFEST = AUTOMATION_ROOT / f"{ASSET_ID}_SnapAssemblySourceA01AnchorManifest.json"
BUILD_MANIFEST = AUTOMATION_ROOT / f"{ASSET_ID}_SnapAssemblySourceA01Manifest.json"
ASSEMBLY_BLEND = SOURCE_ROOT / f"{ASSET_ID}_Assembled_Proof.blend"

COMPONENT_ORDER = ("support_base", "upper_socket_ring", "primary_monolith")
PROOF_VIEWS = ("front", "back", "left", "right", "top", "angle")
COMPONENT_COLORS = {
    "support_base": (0.31, 0.34, 0.36, 1.0),
    "upper_socket_ring": (0.68, 0.42, 0.18, 1.0),
    "primary_monolith": (0.50, 0.16, 0.14, 1.0),
    "anchor": (0.06, 0.78, 0.86, 1.0),
    "label": (0.92, 0.92, 0.86, 1.0),
}


def blender_args() -> list[str]:
    if "--" not in sys.argv:
        return []
    return sys.argv[sys.argv.index("--") + 1 :]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-renders", action="store_true", help="Write blend and manifest without proof renders.")
    return parser.parse_args(blender_args())


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    for datablocks in (
        bpy.data.meshes,
        bpy.data.materials,
        bpy.data.images,
        bpy.data.cameras,
        bpy.data.lights,
        bpy.data.curves,
    ):
        for item in list(datablocks):
            datablocks.remove(item)


def configure_save_policy() -> None:
    bpy.context.preferences.filepaths.save_version = 0


def material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    mat.use_nodes = False
    return mat


def materials() -> dict[str, bpy.types.Material]:
    return {key: material(f"M_A002_Assembly_{key}", color) for key, color in COMPONENT_COLORS.items()}


def append_object(blend_path: Path, object_name: str) -> bpy.types.Object:
    directory = blend_path / "Object"
    bpy.ops.wm.append(directory=str(directory), filename=object_name)
    obj = bpy.data.objects.get(object_name)
    if obj is None:
        raise RuntimeError(f"Object {object_name} was not appended from {blend_path}")
    return obj


def transform_component(obj: bpy.types.Object, transform: dict[str, object]) -> None:
    obj.location = tuple(float(v) for v in transform["location"])
    obj.rotation_euler = tuple(math.radians(float(v)) for v in transform["rotation_degrees"])
    obj.scale = tuple(float(v) for v in transform["scale"])


def make_cube_marker(
    name: str,
    location: tuple[float, float, float],
    size_cm: float,
    mat: bpy.types.Material,
) -> bpy.types.Object:
    sx = sy = sz = size_cm * 0.5
    cx, cy, cz = location
    verts = [
        (cx - sx, cy - sy, cz - sz),
        (cx + sx, cy - sy, cz - sz),
        (cx + sx, cy + sy, cz - sz),
        (cx - sx, cy + sy, cz - sz),
        (cx - sx, cy - sy, cz + sz),
        (cx + sx, cy - sy, cz + sz),
        (cx + sx, cy + sy, cz + sz),
        (cx - sx, cy + sy, cz + sz),
    ]
    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (3, 7, 4, 0),
    ]
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(mat)
    obj["a002_marker_type"] = "snap_anchor_contact_marker"
    return obj


def contact_location(direction: str, footprint_cm: list[float], station_cm: float) -> tuple[float, float, float]:
    width, depth = float(footprint_cm[0]), float(footprint_cm[1])
    if direction == "front":
        return (0.0, -depth * 0.5, station_cm)
    if direction == "back":
        return (0.0, depth * 0.5, station_cm)
    if direction == "left":
        return (-width * 0.5, 0.0, station_cm)
    if direction == "right":
        return (width * 0.5, 0.0, station_cm)
    raise ValueError(f"Unsupported direction: {direction}")


def add_anchor_markers(manifest: dict[str, object], mats: dict[str, bpy.types.Material]) -> list[str]:
    created: list[str] = []
    components = manifest["approved_component_sources"]
    transforms = manifest["assembly_transforms_cm"]
    for pair in manifest["anchor_pairs"]:
        direction = str(pair["pair_id"]).rsplit("_", 1)[-1].lower()
        component_id = str(pair["component_a"])
        footprint = components[component_id]["footprint_cm"]
        station = float(pair["contact_station_cm"])
        local = Vector(contact_location(direction, footprint, station))
        offset = Vector(tuple(float(v) for v in transforms[component_id]["location"]))
        obj = make_cube_marker(f"MARKER_{pair['pair_id']}", tuple(local + offset), 3.5, mats["anchor"])
        obj["a002_anchor_pair_id"] = pair["pair_id"]
        created.append(obj.name)
    return created


def add_label(text: str, location: tuple[float, float, float], mat: bpy.types.Material) -> bpy.types.Object:
    curve = bpy.data.curves.new(f"LABEL_{text}_Curve", "FONT")
    curve.body = text
    curve.align_x = "CENTER"
    curve.align_y = "CENTER"
    curve.size = 7.0
    obj = bpy.data.objects.new(f"LABEL_{text}", curve)
    obj.location = location
    obj.rotation_euler = (math.radians(90.0), 0.0, 0.0)
    obj.data.materials.append(mat)
    bpy.context.collection.objects.link(obj)
    obj["a002_marker_type"] = "assembly_component_identity_label"
    return obj


def object_bounds() -> tuple[Vector, Vector]:
    verts: list[Vector] = []
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH":
            continue
        verts.extend(obj.matrix_world @ vert.co for vert in obj.data.vertices)
    if not verts:
        return Vector((-80.0, -70.0, 0.0)), Vector((80.0, 70.0, 230.0))
    return (
        Vector((min(v.x for v in verts), min(v.y for v in verts), min(v.z for v in verts))),
        Vector((max(v.x for v in verts), max(v.y for v in verts), max(v.z for v in verts))),
    )


def configure_render() -> None:
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_WORKBENCH"
    except TypeError:
        pass
    scene.render.resolution_x = 1400
    scene.render.resolution_y = 1400
    try:
        scene.view_settings.view_transform = "Standard"
    except TypeError:
        pass
    try:
        scene.view_settings.look = "Medium High Contrast"
    except TypeError:
        scene.view_settings.look = "None"
    scene.world.color = (0.035, 0.038, 0.04)


def add_camera_and_lights(view: str) -> None:
    min_v, max_v = object_bounds()
    center = (min_v + max_v) * 0.5
    span = max((max_v - min_v).x, (max_v - min_v).y, (max_v - min_v).z, 1.0)
    distance = span * 2.35
    if view == "front":
        location = Vector((center.x, center.y - distance, center.z + span * 0.22))
    elif view == "back":
        location = Vector((center.x, center.y + distance, center.z + span * 0.22))
    elif view == "left":
        location = Vector((center.x - distance, center.y, center.z + span * 0.22))
    elif view == "right":
        location = Vector((center.x + distance, center.y, center.z + span * 0.22))
    elif view == "top":
        location = Vector((center.x, center.y, center.z + distance))
    elif view == "angle":
        location = Vector((center.x + distance * 0.85, center.y - distance * 0.95, center.z + distance * 0.55))
    else:
        raise ValueError(f"Unsupported proof view: {view}")
    cam_data = bpy.data.cameras.new(f"CAM_{view}")
    cam = bpy.data.objects.new(f"CAM_{view}", cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = location
    cam.rotation_euler = (center - location).to_track_quat("-Z", "Y").to_euler()
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = max(span * 1.35, 180.0)
    bpy.context.scene.camera = cam
    light_data = bpy.data.lights.new(f"KEY_{view}", "AREA")
    light = bpy.data.objects.new(f"KEY_{view}", light_data)
    bpy.context.collection.objects.link(light)
    light.location = location + Vector((0.0, 0.0, span * 0.3))
    light.rotation_euler = cam.rotation_euler
    light.data.energy = 420.0
    light.data.size = 4.0


def purge_render_images() -> None:
    for image in list(bpy.data.images):
        if image.name in {"Render Result", "Viewer Node"}:
            bpy.data.images.remove(image)


def render_proofs() -> list[str]:
    configure_render()
    PROOF_ROOT.mkdir(parents=True, exist_ok=True)
    rendered: list[str] = []
    for view in PROOF_VIEWS:
        for obj in [obj for obj in bpy.context.scene.objects if obj.type in {"CAMERA", "LIGHT"}]:
            bpy.data.objects.remove(obj, do_unlink=True)
        add_camera_and_lights(view)
        path = PROOF_ROOT / f"{ASSET_ID}_SnapAssembly_{view.title()}Proof.png"
        bpy.context.scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)
        rendered.append(str(path.relative_to(ROOT)))
    return rendered


def build_assembly(manifest: dict[str, object], skip_renders: bool) -> dict[str, object]:
    clear_scene()
    configure_save_policy()
    mats = materials()
    components = manifest["approved_component_sources"]
    transforms = manifest["assembly_transforms_cm"]
    component_reports: list[dict[str, object]] = []

    for component_id in COMPONENT_ORDER:
        spec = components[component_id]
        obj = append_object(ROOT / spec["blend_path"], spec["asset_name"])
        obj.name = spec["asset_name"]
        obj.data.materials.clear()
        obj.data.materials.append(mats[component_id])
        transform_component(obj, transforms[component_id])
        obj["a002_assembly_component_id"] = component_id
        obj["a002_assembly_transform_manifest"] = str(ANCHOR_MANIFEST.relative_to(ROOT))
        component_reports.append(
            {
                "component_id": component_id,
                "object_name": obj.name,
                "location": [round(float(v), 10) for v in obj.location],
                "rotation_degrees": [round(math.degrees(float(v)), 10) for v in obj.rotation_euler],
                "scale": [round(float(v), 10) for v in obj.scale],
            }
        )

    add_label("support_base", (0.0, -76.0, 24.0), mats["label"])
    add_label("upper_socket_ring", (0.0, -76.0, 66.0), mats["label"])
    add_label("primary_monolith", (6.7158671593, -76.0, 220.0), mats["label"])
    marker_names = add_anchor_markers(manifest, mats)
    proof_paths = [] if skip_renders else render_proofs()
    purge_render_images()
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(ASSEMBLY_BLEND))
    return {
        "assembly_blend": str(ASSEMBLY_BLEND.relative_to(ROOT)),
        "component_reports": component_reports,
        "anchor_markers": marker_names,
        "proof_renders": proof_paths,
    }


def write_manifest(anchor_manifest: dict[str, object], build_report: dict[str, object]) -> None:
    AUTOMATION_ROOT.mkdir(parents=True, exist_ok=True)
    output = {
        "asset_id": ASSET_ID,
        "package_id": PACKAGE_ID,
        "status": "snap assembly source candidate generated",
        "script": str(Path(__file__).resolve().relative_to(ROOT)),
        "anchor_manifest": str(ANCHOR_MANIFEST.relative_to(ROOT)),
        "core_policy": {
            "no_uv_generation": True,
            "no_texture_nodes": True,
            "no_fbx_export": True,
            "no_unreal_output": True,
            "no_runtime_merge": True,
            "no_manual_visual_fit": True,
        },
        "assembly_transforms_cm": anchor_manifest["assembly_transforms_cm"],
        **build_report,
    }
    BUILD_MANIFEST.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    anchor_manifest = read_json(ANCHOR_MANIFEST)
    if anchor_manifest.get("assembly_generation_authorized") is not True:
        raise SystemExit("Assembly generation is not authorized by the anchor manifest.")
    build_report = build_assembly(anchor_manifest, bool(args.skip_renders))
    write_manifest(anchor_manifest, build_report)
    print(BUILD_MANIFEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
