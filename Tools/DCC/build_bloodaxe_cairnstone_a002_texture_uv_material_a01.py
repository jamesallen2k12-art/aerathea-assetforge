#!/usr/bin/env python3
"""Build the A002 texture/UV/material candidate in Blender.

Run only after Phase 5C script creation is complete:

    blender --background --python Tools/DCC/build_bloodaxe_cairnstone_a002_texture_uv_material_a01.py

This script consumes the Phase 5B ownership manifest. It may create UV layers,
source-sheet material nodes, technical proof renders, and a texture/UV/material
candidate blend when Phase 5D runs. It does not create FBX or Unreal output.
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
PROOF_ROOT = AUTOMATION_ROOT / "ProofRenders"
OWNERSHIP_MANIFEST = AUTOMATION_ROOT / f"{ASSET_ID}_TextureUVMaterialA01OwnershipManifest.json"
BUILD_MANIFEST = AUTOMATION_ROOT / f"{ASSET_ID}_TextureUVMaterialA01Manifest.json"
CANDIDATE_BLEND = SOURCE_ROOT / f"{ASSET_ID}_TextureUVMaterial_A01.blend"
PROOF_VIEWS = ("front", "back", "left", "right", "top", "angle")

SOURCE_IMAGE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
SOURCE_WIDTH = 1055
SOURCE_HEIGHT = 1491

VIEW_BOXES = {
    "front": {
        "object": (648, 156, 946, 558),
        "primary": (666, 156, 922, 494),
        "support_base": (648, 494, 946, 558),
    },
    "back": {
        "object": (142, 684, 422, 990),
        "primary": (162, 684, 402, 941),
        "support_base": (142, 941, 422, 990),
    },
    "left": {
        "object": (674, 680, 888, 1002),
        "primary": (692, 680, 868, 951),
        "support_base": (674, 951, 888, 1002),
    },
    "right": {
        "object": (70, 1090, 314, 1418),
        "primary": (93, 1090, 293, 1366),
        "support_base": (70, 1366, 314, 1418),
    },
    "top": {
        "object": (414, 1108, 685, 1367),
        "primary": (434, 1132, 666, 1344),
        "support_base": (414, 1108, 685, 1367),
    },
}

COMPONENT_DIMS = {
    "primary_monolith": (120.0, 90.0, 220.0),
    "upper_socket_ring": (140.0, 110.0, 60.0),
    "support_base": (140.0, 110.0, 60.0),
}

COMPONENT_OBJECTS = {
    "primary_monolith": "SM_GIA_BloodAxeCairnstone_A002_PrimaryMonolith",
    "upper_socket_ring": "SM_GIA_BloodAxeCairnstone_A002_UpperSocketRing",
    "support_base": "SM_GIA_BloodAxeCairnstone_A002_SupportBase",
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


def configure_save_policy() -> None:
    bpy.context.preferences.filepaths.save_version = 0


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    for datablocks in (bpy.data.meshes, bpy.data.materials, bpy.data.images, bpy.data.cameras, bpy.data.lights, bpy.data.curves):
        for item in list(datablocks):
            datablocks.remove(item)


def open_assembly(path: Path) -> None:
    bpy.ops.wm.open_mainfile(filepath=str(path))
    configure_save_policy()


def make_source_material() -> bpy.types.Material:
    mat = bpy.data.materials.new("M_A002_SourceTemplate_Closest")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    for node in list(nodes):
        nodes.remove(node)
    output = nodes.new("ShaderNodeOutputMaterial")
    shader = nodes.new("ShaderNodeBsdfPrincipled")
    texture = nodes.new("ShaderNodeTexImage")
    texture.name = "A002_ApprovedSourceTemplate"
    texture.image = bpy.data.images.load(str(SOURCE_IMAGE), check_existing=True)
    texture.interpolation = "Closest"
    mat.node_tree.links.new(texture.outputs["Color"], shader.inputs["Base Color"])
    mat.node_tree.links.new(shader.outputs["BSDF"], output.inputs["Surface"])
    return mat


def make_inferred_material() -> bpy.types.Material:
    mat = bpy.data.materials.new("M_A002_TaggedInferredHidden_Neutral")
    mat.diffuse_color = (0.24, 0.23, 0.22, 1.0)
    mat.use_nodes = False
    return mat


def image_uv(pixel_x: float, pixel_y: float) -> tuple[float, float]:
    return pixel_x / SOURCE_WIDTH, 1.0 - (pixel_y / SOURCE_HEIGHT)


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def box_uv(box: tuple[int, int, int, int], sx: float, sy: float) -> tuple[float, float]:
    left, top, right, bottom = box
    pixel_x = left + clamp01(sx) * (right - left)
    pixel_y = top + clamp01(sy) * (bottom - top)
    return image_uv(pixel_x, pixel_y)


def classify_view(normal: Vector) -> str:
    if normal.z > 0.65:
        return "top"
    if normal.z < -0.65:
        return "hidden"
    if abs(normal.x) > abs(normal.y):
        return "right" if normal.x > 0.0 else "left"
    return "back" if normal.y > 0.0 else "front"


def source_box(component_id: str, view: str) -> tuple[int, int, int, int] | None:
    if view == "hidden":
        return None
    if component_id == "primary_monolith":
        return VIEW_BOXES[view]["primary"]
    if component_id == "support_base":
        return VIEW_BOXES[view]["support_base" if view != "top" else "support_base"]
    if component_id == "upper_socket_ring":
        if view == "top":
            return None
        return VIEW_BOXES[view]["object"]
    return None


def normalized_surface_xy(component_id: str, view: str, co: Vector) -> tuple[float, float]:
    width, depth, height = COMPONENT_DIMS[component_id]
    if view in {"front", "back"}:
        return (co.x + width * 0.5) / width, 1.0 - (co.z / height)
    if view in {"left", "right"}:
        return (co.y + depth * 0.5) / depth, 1.0 - (co.z / height)
    if view == "top":
        return (co.x + width * 0.5) / width, (co.y + depth * 0.5) / depth
    return 0.0, 0.0


def assign_uvs(obj: bpy.types.Object, component_id: str, source_mat: bpy.types.Material, inferred_mat: bpy.types.Material) -> dict[str, int]:
    if obj.type != "MESH":
        return {}
    obj.data.materials.clear()
    obj.data.materials.append(source_mat)
    obj.data.materials.append(inferred_mat)
    uv_layer = obj.data.uv_layers.new(name="A002_SourceOwnedUV")
    counts = {"front": 0, "back": 0, "left": 0, "right": 0, "top": 0, "hidden": 0}
    normal_matrix = obj.matrix_world.to_3x3()
    for poly in obj.data.polygons:
        world_normal = (normal_matrix @ poly.normal).normalized()
        view = classify_view(world_normal)
        box = source_box(component_id, view)
        if box is None:
            poly.material_index = 1
            for loop_index in poly.loop_indices:
                uv_layer.data[loop_index].uv = (0.02, 0.02)
            counts["hidden"] += 1
            continue
        poly.material_index = 0
        for loop_index in poly.loop_indices:
            vertex = obj.data.vertices[obj.data.loops[loop_index].vertex_index]
            sx, sy = normalized_surface_xy(component_id, view, vertex.co)
            uv_layer.data[loop_index].uv = box_uv(box, sx, sy)
        counts[view] += 1
    obj["a002_uv_ownership_manifest"] = str(OWNERSHIP_MANIFEST.relative_to(ROOT))
    obj["a002_uv_layer"] = uv_layer.name
    return counts


def object_bounds() -> tuple[Vector, Vector]:
    verts: list[Vector] = []
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH" or obj.name.startswith("MARKER_"):
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
    paths: list[str] = []
    for view in PROOF_VIEWS:
        for obj in [obj for obj in bpy.context.scene.objects if obj.type in {"CAMERA", "LIGHT"}]:
            bpy.data.objects.remove(obj, do_unlink=True)
        add_camera_and_lights(view)
        path = PROOF_ROOT / f"{ASSET_ID}_TextureUVMaterial_{view.title()}Proof.png"
        bpy.context.scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)
        paths.append(str(path.relative_to(ROOT)))
    return paths


def write_manifest(ownership: dict[str, object], uv_reports: dict[str, object], proof_paths: list[str]) -> None:
    BUILD_MANIFEST.write_text(
        json.dumps(
            {
                "asset_id": ASSET_ID,
                "package_id": PACKAGE_ID,
                "status": "texture_uv_material_candidate_generated",
                "script": str(Path(__file__).resolve().relative_to(ROOT)),
                "ownership_manifest": str(OWNERSHIP_MANIFEST.relative_to(ROOT)),
                "source_image": str(SOURCE_IMAGE.relative_to(ROOT)),
                "candidate_blend": str(CANDIDATE_BLEND.relative_to(ROOT)),
                "uv_reports": uv_reports,
                "proof_renders": proof_paths,
                "core_policy": {
                    "no_fbx_export": True,
                    "no_unreal_output": True,
                    "source_template_closest_sampling": True,
                    "hidden_surfaces_tagged_inferred": True,
                },
                "material_slot_strategy": ownership["material_slot_strategy"],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    ownership = read_json(OWNERSHIP_MANIFEST)
    assembly_blend = ROOT / ownership["dcc_lineage"]["approved_assembly_blend"]
    open_assembly(assembly_blend)
    source_mat = make_source_material()
    inferred_mat = make_inferred_material()
    uv_reports = {}
    for component_id, object_name in COMPONENT_OBJECTS.items():
        obj = bpy.data.objects.get(object_name)
        if obj is None:
            raise SystemExit(f"Missing component object: {object_name}")
        uv_reports[component_id] = assign_uvs(obj, component_id, source_mat, inferred_mat)
    proof_paths = [] if args.skip_renders else render_proofs()
    purge_render_images()
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(CANDIDATE_BLEND))
    AUTOMATION_ROOT.mkdir(parents=True, exist_ok=True)
    write_manifest(ownership, uv_reports, proof_paths)
    print(BUILD_MANIFEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
