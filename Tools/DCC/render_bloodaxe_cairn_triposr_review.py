#!/usr/bin/env python3
"""Render the TripoSR Blood Axe cairn reconstruction for review."""

from pathlib import Path
import os

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png"
GLB = Path(os.environ.get("AET_TRIPOSR_GLB", ROOT / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR/0/mesh.glb"))
REVIEW_ROOT = Path(os.environ.get("AET_TRIPOSR_REVIEW_ROOT", ROOT / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR"))
FRONT = REVIEW_ROOT / "SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR_FrontReview.png"
THREE = REVIEW_ROOT / "SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR_ThreeQuarterReview.png"
SIDE = REVIEW_ROOT / "SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR_SideReview.png"
BACK = REVIEW_ROOT / "SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR_BackReview.png"
BOARD = REVIEW_ROOT / "SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR_ReviewBoard.png"


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def set_camera(name: str, location: tuple[float, float, float], target: tuple[float, float, float], ortho_scale: float) -> None:
    bpy.ops.object.camera_add(location=location)
    camera = bpy.context.object
    camera.name = name
    direction = Vector(target) - Vector(location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = ortho_scale
    camera.data.clip_start = 0.01
    camera.data.clip_end = 5000
    bpy.context.scene.camera = camera


def setup_lighting() -> None:
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_EEVEE"
    try:
        scene.view_settings.view_transform = "Standard"
    except TypeError:
        pass
    scene.view_settings.exposure = 0.45
    scene.view_settings.gamma = 1.0
    if scene.world is not None:
        scene.world.color = (0.54, 0.53, 0.50)
    for name, kind, location, energy, size in [
        ("AET_Tripo_Key", "AREA", (-3.0, -4.0, 5.0), 450.0, 4.0),
        ("AET_Tripo_Fill", "AREA", (3.0, -2.0, 2.5), 180.0, 5.0),
        ("AET_Tripo_Rim", "POINT", (0.0, 3.0, 2.5), 60.0, 0.0),
    ]:
        data = bpy.data.lights.new(name, type=kind)
        data.energy = energy
        if kind == "AREA":
            data.size = size
        obj = bpy.data.objects.new(name, data)
        obj.location = location
        bpy.context.scene.collection.objects.link(obj)


def normalize_import() -> None:
    bpy.ops.import_scene.gltf(filepath=str(GLB))
    meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    if not meshes:
        raise RuntimeError("No mesh imported from TripoSR GLB")
    points = []
    for obj in meshes:
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    min_v = Vector((min(p.x for p in points), min(p.y for p in points), min(p.z for p in points)))
    max_v = Vector((max(p.x for p in points), max(p.y for p in points), max(p.z for p in points)))
    center = (min_v + max_v) * 0.5
    size = max(max_v.x - min_v.x, max_v.y - min_v.y, max_v.z - min_v.z)
    scale = 3.0 / size if size > 0 else 1.0
    for obj in meshes:
        obj.location = (obj.location - center) * scale
        obj.scale = (obj.scale.x * scale, obj.scale.y * scale, obj.scale.z * scale)


def render_views() -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 1100
    scene.render.resolution_y = 850
    views = [
        (FRONT, "TripoFront", (2.4, -4.1, 1.8), (0.0, 0.0, 0.4), 3.9),
        (THREE, "TripoThreeQuarter", (3.0, -3.3, 2.1), (0.0, 0.0, 0.4), 4.0),
        (SIDE, "TripoSide", (4.2, 0.0, 1.7), (0.0, 0.0, 0.35), 3.7),
        (BACK, "TripoBack", (-2.4, 4.1, 1.8), (0.0, 0.0, 0.4), 3.9),
    ]
    for path, name, location, target, scale in views:
        set_camera(name, location, target, scale)
        scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)


def font(size: int) -> ImageFont.ImageFont:
    for candidate in (
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ):
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def build_board() -> None:
    board = Image.new("RGBA", (2200, 1300), (236, 233, 226, 255))
    draw = ImageDraw.Draw(board)
    title = font(34)
    body = font(22)
    draw.text((52, 34), "TripoSR reconstruction proof from A1 concept", fill=(28, 25, 22, 255), font=title)
    draw.text((52, 82), "Generated GLB from single image; this tests reconstruction viability, not final Aerathea art approval.", fill=(58, 52, 45, 255), font=body)
    items = [
        ("Source A1", SOURCE, (70, 160), (340, 406)),
        ("Generated front", FRONT, (480, 150), (500, 386)),
        ("Generated 3/4", THREE, (1030, 150), (500, 386)),
        ("Generated side", SIDE, (480, 660), (500, 386)),
        ("Generated back", BACK, (1030, 660), (500, 386)),
    ]
    for label, path, location, max_size in items:
        image = Image.open(path).convert("RGBA")
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        board.alpha_composite(image, location)
        draw.text((location[0], location[1] + max_size[1] + 16), label, fill=(42, 37, 32, 255), font=body)
    board.save(BOARD)


def main() -> None:
    clear_scene()
    setup_lighting()
    normalize_import()
    render_views()
    build_board()
    print(BOARD.relative_to(ROOT))


if __name__ == "__main__":
    main()
