#!/usr/bin/env python3
"""Build the P01B geometric primitive bisection board.

This is a shape-training proof only. It cuts each approved P01 primitive once
through its center and separates the halves so the cut surface is readable.
"""

from __future__ import annotations

import math
import shutil
import sys
from pathlib import Path
from typing import Callable

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "P01B_BisectedPrimitiveBoard"
DOC_ROOT = ROOT / "docs" / "assets" / "training" / "geometric_primitives"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "GeometricPrimitives"
TILE_ROOT = REVIEW_ROOT / "bisected_tiles"
BLEND_ROOT = ROOT / "SourceAssets" / "Blender" / "Props" / "Training" / "GeometricPrimitives" / ASSET_NAME
DOC_IMAGE = DOC_ROOT / f"{ASSET_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{ASSET_NAME}.png"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_geometric_primitive_fundamentals import (  # noqa: E402
    add_cone,
    add_cube,
    add_cylinder,
    add_dodecahedron,
    add_ground_plane,
    add_hexagonal_prism,
    add_icosahedron,
    add_octa_cut,
    add_oval_egg,
    add_parallelepiped,
    add_pentagonal_trapezohedron,
    add_rectangular_slab,
    add_sphere,
    add_tetrahedron,
    add_zocchihedron,
    configure_scene,
    ensure_dir,
    load_font,
    look_at,
    make_material,
    render,
)
from Tools.DCC.build_next_slice_assets import clear_scene, setup_scene  # noqa: E402


def build_materials() -> dict[str, bpy.types.Material]:
    materials = {
        "cube": make_material("M_P01B_Cube", (0.58, 0.58, 0.54)),
        "slab": make_material("M_P01B_RectangularSlab", (0.48, 0.53, 0.56)),
        "para": make_material("M_P01B_Parallelepiped", (0.52, 0.47, 0.58)),
        "tetra": make_material("M_P01B_Tetrahedron", (0.58, 0.50, 0.42)),
        "octa": make_material("M_P01B_OctaCut", (0.47, 0.56, 0.48)),
        "hex": make_material("M_P01B_HexagonalPrism", (0.44, 0.54, 0.56)),
        "ico": make_material("M_P01B_Icosahedron", (0.50, 0.58, 0.45)),
        "dodeca": make_material("M_P01B_Dodecahedron", (0.58, 0.52, 0.45)),
        "d10": make_material("M_P01B_PentagonalTrapezohedron", (0.57, 0.44, 0.42)),
        "zocchi": make_material("M_P01B_Zocchihedron", (0.45, 0.48, 0.58)),
        "cone": make_material("M_P01B_Cone", (0.58, 0.48, 0.38)),
        "sphere": make_material("M_P01B_SmoothSphere", (0.46, 0.55, 0.58)),
        "egg": make_material("M_P01B_OvalEgg", (0.55, 0.48, 0.38)),
        "cylinder": make_material("M_P01B_Cylinder", (0.56, 0.52, 0.45)),
        "cut": make_material("M_P01B_WarmCutFace", (0.84, 0.72, 0.48), roughness=0.92),
        "base": make_material("M_P01B_NeutralBase", (0.31, 0.31, 0.30)),
    }
    return materials


def duplicate_object(source: bpy.types.Object, name: str) -> bpy.types.Object:
    obj = source.copy()
    obj.data = source.data.copy()
    obj.name = name
    obj.data.name = f"{name}_Mesh"
    bpy.context.collection.objects.link(obj)
    return obj


def bisect_half(
    obj: bpy.types.Object,
    *,
    plane_co: Vector,
    plane_no: Vector,
    keep_positive_side: bool,
) -> None:
    bpy.ops.object.mode_set(mode="OBJECT") if bpy.context.object and bpy.context.object.mode != "OBJECT" else None
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    normal = plane_no.normalized()
    bpy.ops.mesh.bisect(
        plane_co=(plane_co.x, plane_co.y, plane_co.z),
        plane_no=(normal.x, normal.y, normal.z),
        clear_inner=keep_positive_side,
        clear_outer=not keep_positive_side,
        use_fill=True,
    )
    bpy.ops.object.mode_set(mode="OBJECT")


def assign_cut_face_material(obj: bpy.types.Object, cut_material: bpy.types.Material, plane_co: Vector, plane_no: Vector) -> None:
    obj.data.materials.append(cut_material)
    cut_index = len(obj.data.materials) - 1
    normal = plane_no.normalized()
    for polygon in obj.data.polygons:
        distances = [(obj.data.vertices[index].co - plane_co).dot(normal) for index in polygon.vertices]
        if distances and max(abs(value) for value in distances) < 0.02:
            polygon.material_index = cut_index


def default_bisect_plane(source: bpy.types.Object) -> tuple[Vector, Vector, str]:
    return Vector((0.0, 0.0, 0.0)), Vector((1.0, 0.0, 0.0)), "center symmetry plane"


def parallelepiped_bisect_plane() -> tuple[Vector, Vector, str]:
    depth = 1.35
    height = 2.25
    shear_x = 0.55
    shear_y = 0.15
    z0 = -height / 2.0
    z1 = height / 2.0
    y0 = -depth / 2.0
    y1 = depth / 2.0
    bottom_front_mid = Vector((0.0, y0, z0))
    bottom_back_mid = Vector((0.0, y1, z0))
    top_front_mid = Vector((shear_x, y0 + shear_y, z1))
    plane_no = (bottom_back_mid - bottom_front_mid).cross(top_front_mid - bottom_front_mid).normalized()
    return bottom_front_mid, plane_no, "slanted center plane parallel to side faces"


def tetrahedron_bisect_plane() -> tuple[Vector, Vector, str]:
    return Vector((0.0, 0.0, 0.0)), Vector((1.0, 0.0, 0.0)), "mirror plane through apex edge and opposite midpoint"


def mesh_world_bounds(objects: tuple[bpy.types.Object, ...]) -> tuple[Vector, Vector]:
    corners = [obj.matrix_world @ Vector(corner) for obj in objects for corner in obj.bound_box]
    minimum = Vector((min(corner.x for corner in corners), min(corner.y for corner in corners), min(corner.z for corner in corners)))
    maximum = Vector((max(corner.x for corner in corners), max(corner.y for corner in corners), max(corner.z for corner in corners)))
    return minimum, maximum


def make_bisected_pair(
    source: bpy.types.Object,
    label: str,
    cut_material: bpy.types.Material,
    plane_fn: Callable[[bpy.types.Object], tuple[Vector, Vector, str]] = default_bisect_plane,
) -> tuple[bpy.types.Object, bpy.types.Object]:
    plane_co, plane_no, plane_note = plane_fn(source)
    negative = duplicate_object(source, f"P01B_{label.replace(' ', '')}_NegativeHalf")
    positive = duplicate_object(source, f"P01B_{label.replace(' ', '')}_PositiveHalf")
    bisect_half(negative, plane_co=plane_co, plane_no=plane_no, keep_positive_side=False)
    bisect_half(positive, plane_co=plane_co, plane_no=plane_no, keep_positive_side=True)
    assign_cut_face_material(negative, cut_material, plane_co, plane_no)
    assign_cut_face_material(positive, cut_material, plane_co, plane_no)

    gap = 0.78
    turn = math.radians(30.0)
    separation = Vector((plane_no.x, plane_no.y, 0.0))
    if separation.length < 0.001:
        separation = Vector((1.0, 0.0, 0.0))
    separation.normalize()
    negative.location -= separation * gap
    positive.location += separation * gap
    negative.rotation_euler.z -= turn
    positive.rotation_euler.z += turn
    for obj in (negative, positive):
        obj["Aerathea.PrimitiveStage"] = "P01B center bisection"
        obj["Aerathea.PrimitiveName"] = label
        obj["Aerathea.BisectionPlane"] = plane_note
        obj["Aerathea.PresentationNote"] = "Halves opened 30 degrees for cut-face review."
        obj["Aerathea.NotAssetCandidate"] = True
    bpy.data.objects.remove(source, do_unlink=True)
    return negative, positive


def render_tile_objects(
    camera: bpy.types.Object,
    objects: tuple[bpy.types.Object, bpy.types.Object],
    base: bpy.types.Object,
    path: Path,
    ortho_scale: float,
) -> None:
    visible = {objects[0], objects[1], base}
    state = [(item, item.hide_render, item.hide_viewport) for item in bpy.context.scene.objects]
    try:
        for item in bpy.context.scene.objects:
            if item.type == "MESH" and item not in visible:
                item.hide_render = True
                item.hide_viewport = True
        minimum, maximum = mesh_world_bounds(objects)
        center = (minimum + maximum) * 0.5
        span = maximum - minimum
        split_axis = objects[1].location - objects[0].location
        if split_axis.length < 0.001:
            split_axis = Vector((1.0, 0.0, 0.0))
        split_axis.z = 0.0
        split_axis.normalize()
        camera.data.ortho_scale = max(ortho_scale, max(span.x, span.y, span.z) * 1.34)
        target = Vector((center.x, center.y, center.z + 0.05))
        camera.location = (
            center.x + split_axis.x * 2.15,
            center.y - 7.25 + split_axis.y * 0.55,
            center.z + 3.7,
        )
        look_at(camera, target)
        render(camera, path, (620, 460))
    finally:
        for item, hide_render, hide_viewport in state:
            item.hide_render = hide_render
            item.hide_viewport = hide_viewport


def compose_contact_sheet(tile_specs: list[tuple[str, Path]], output_path: Path) -> None:
    cols = 4
    rows = math.ceil(len(tile_specs) / cols)
    pad = 24
    title_h = 112
    image_w = 390
    image_h = 286
    label_h = 46
    cell_w = image_w
    cell_h = image_h + label_h
    width = cols * cell_w + (cols + 1) * pad
    height = title_h + rows * cell_h + (rows + 1) * pad

    image = Image.new("RGB", (width, height), (31, 31, 32))
    draw = ImageDraw.Draw(image, "RGBA")
    title_font = load_font(40, bold=True)
    label_font = load_font(25, bold=True)
    note_font = load_font(18)

    draw.rectangle((0, 0, width, 100), fill=(34, 34, 34, 214))
    draw.text((34, 16), "P01B Logical Primitive Bisection Board", fill=(238, 232, 220, 255), font=title_font)
    draw.text((38, 66), "halves opened for review; cuts follow center, symmetry, edge, diagonal, or median paths", fill=(216, 198, 166, 255), font=note_font)

    for index, (label, tile_path) in enumerate(tile_specs):
        col = index % cols
        row = index // cols
        x = pad + col * (cell_w + pad)
        y = title_h + pad + row * (cell_h + pad)
        draw.rectangle((x, y, x + image_w, y + image_h), fill=(48, 48, 48, 255), outline=(98, 92, 82, 255), width=2)
        tile = Image.open(tile_path).convert("RGB")
        resample = Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS
        tile.thumbnail((image_w - 10, image_h - 10), resample)
        tx = x + (image_w - tile.width) // 2
        ty = y + (image_h - tile.height) // 2
        image.paste(tile, (tx, ty))
        bbox = draw.textbbox((0, 0), label, font=label_font)
        label_x = x + (image_w - (bbox[2] - bbox[0])) // 2
        draw.text((label_x, y + image_h + 10), label, fill=(238, 232, 220, 255), font=label_font)

    ensure_dir(output_path.parent)
    image.save(output_path)


def main() -> None:
    clear_scene()
    setup_scene()
    materials = build_materials()
    base = add_ground_plane(materials["base"])
    base.name = "P01B_NeutralReviewBase"

    build_specs = [
        ("Cube", lambda: add_cube("P01B_Cube_Source", (0.0, 0.0, 1.0), materials["cube"]), default_bisect_plane, 3.8),
        ("Slab", lambda: add_rectangular_slab("P01B_RectangularSlab_Source", (0.0, 0.0, 0.7), materials["slab"]), default_bisect_plane, 4.4),
        ("Parallelepiped", lambda: add_parallelepiped("P01B_Parallelepiped_Source", (0.0, 0.0, 1.2), materials["para"]), lambda _obj: parallelepiped_bisect_plane(), 4.4),
        ("Hex Prism", lambda: add_hexagonal_prism("P01B_HexagonalPrism_Source", (0.0, 0.0, 1.08), materials["hex"]), default_bisect_plane, 4.0),
        ("Cylinder", lambda: add_cylinder("P01B_Cylinder_Source", (0.0, 0.0, 1.1), materials["cylinder"]), default_bisect_plane, 4.0),
        ("Zocchihedron", lambda: add_zocchihedron("P01B_Zocchihedron_Source", (0.0, 0.0, 1.1), materials["zocchi"]), default_bisect_plane, 4.0),
        ("Tetrahedron", lambda: add_tetrahedron("P01B_Tetrahedron_Source", (0.0, 0.0, 1.0), materials["tetra"]), lambda _obj: tetrahedron_bisect_plane(), 4.1),
        ("Octa Cut", lambda: add_octa_cut("P01B_OctaCut_Source", (0.0, 0.0, 1.25), materials["octa"]), default_bisect_plane, 4.1),
        ("Icosahedron", lambda: add_icosahedron("P01B_Icosahedron_Source", (0.0, 0.0, 1.25), materials["ico"]), default_bisect_plane, 4.2),
        ("Dodecahedron", lambda: add_dodecahedron("P01B_Dodecahedron_Source", (0.0, 0.0, 1.25), materials["dodeca"]), default_bisect_plane, 4.2),
        ("D10 Trapezohedron", lambda: add_pentagonal_trapezohedron("P01B_PentagonalTrapezohedron_Source", (0.0, 0.0, 1.25), materials["d10"]), default_bisect_plane, 4.1),
        ("Cone", lambda: add_cone("P01B_Cone_Source", (0.0, 0.0, 1.12), materials["cone"]), default_bisect_plane, 4.0),
        ("Smooth Sphere", lambda: add_sphere("P01B_SmoothSphere_Source", (0.0, 0.0, 1.08), materials["sphere"]), default_bisect_plane, 4.0),
        ("Oval Egg", lambda: add_oval_egg("P01B_OvalEgg_Source", (0.0, 0.0, 1.24), materials["egg"]), default_bisect_plane, 4.0),
    ]

    camera = configure_scene()
    tile_specs: list[tuple[str, Path]] = []
    for index, (label, builder, plane_fn, ortho_scale) in enumerate(build_specs, 1):
        source = builder()
        halves = make_bisected_pair(source, label, materials["cut"], plane_fn)
        for obj in halves:
            obj["Aerathea.TrainingLane"] = "geometric_primitive_to_cairnstone"
            obj["Aerathea.Stage"] = "P01B Primitive Bisection Board"
        tile_path = TILE_ROOT / f"P01B_{index:02d}_{label.replace(' ', '_')}_Bisected.png"
        render_tile_objects(camera, halves, base, tile_path, ortho_scale)
        tile_specs.append((label, tile_path))

    compose_contact_sheet(tile_specs, REVIEW_IMAGE)
    ensure_dir(DOC_IMAGE.parent)
    shutil.copyfile(REVIEW_IMAGE, DOC_IMAGE)

    blend_path = BLEND_ROOT / f"{ASSET_NAME}.blend"
    ensure_dir(blend_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"P01B bisection board written: {DOC_IMAGE}")


if __name__ == "__main__":
    main()
