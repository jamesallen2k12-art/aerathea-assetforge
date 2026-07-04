#!/usr/bin/env python3
"""Build the P01 geometric primitive fundamentals board.

This is not a Blood Axe cairn asset pass. It is a clean training board for the
primitive forms that will later become stone construction pieces.
"""

from __future__ import annotations

import shutil
import sys
import math
from pathlib import Path

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "P01_BasicPrimitiveBoard"
DOC_ROOT = ROOT / "docs" / "assets" / "training" / "geometric_primitives"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "GeometricPrimitives"
TILE_ROOT = REVIEW_ROOT / "tiles"
BLEND_ROOT = ROOT / "SourceAssets" / "Blender" / "Props" / "Training" / "GeometricPrimitives" / ASSET_NAME
DOC_IMAGE = DOC_ROOT / f"{ASSET_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{ASSET_NAME}.png"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import clear_scene, setup_scene  # noqa: E402


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def make_material(name: str, color: tuple[float, float, float], roughness: float = 0.88) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (color[0], color[1], color[2], 1.0)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = (color[0], color[1], color[2], 1.0)
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = 0.0
    return material


def look_at(obj: bpy.types.Object, target: Vector) -> None:
    direction = target - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def add_cube(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.9, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    obj["Aerathea.PrimitiveStage"] = "P01 basic primitive"
    obj["Aerathea.PrimitiveName"] = "Cube"
    return obj


def add_mesh_object(
    name: str,
    verts: list[tuple[float, float, float]],
    faces: list[tuple[int, ...]],
    location: tuple[float, float, float],
    material: bpy.types.Material,
    primitive_name: str,
) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.location = location
    obj.data.materials.append(material)
    obj["Aerathea.PrimitiveStage"] = "P01 basic primitive"
    obj["Aerathea.PrimitiveName"] = primitive_name
    return obj


def add_rectangular_slab(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = (3.0, 1.15, 1.15)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    obj["Aerathea.PrimitiveStage"] = "P01 basic primitive"
    obj["Aerathea.PrimitiveName"] = "Rectangular Slab"
    return obj


def add_parallelepiped(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    width = 2.35
    depth = 1.35
    height = 2.25
    shear_x = 0.55
    shear_y = 0.15
    x0, x1 = -width / 2, width / 2
    y0, y1 = -depth / 2, depth / 2
    z0, z1 = -height / 2, height / 2
    verts = [
        (x0, y0, z0),
        (x1, y0, z0),
        (x1, y1, z0),
        (x0, y1, z0),
        (x0 + shear_x, y0 + shear_y, z1),
        (x1 + shear_x, y0 + shear_y, z1),
        (x1 + shear_x, y1 + shear_y, z1),
        (x0 + shear_x, y1 + shear_y, z1),
    ]
    faces = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
    return add_mesh_object(name, verts, faces, location, material, "Parallelepiped")


def add_tetra_wedge(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    verts = [
        (-1.25, -0.8, -0.75),
        (1.25, -0.8, -0.75),
        (0.0, 1.05, -0.75),
        (-0.25, -0.05, 1.25),
    ]
    faces = [(0, 1, 2), (0, 3, 1), (1, 3, 2), (2, 3, 0)]
    return add_mesh_object(name, verts, faces, location, material, "Tetra Wedge")


def add_octa_cut(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    verts = [
        (0.0, 0.0, 1.35),
        (1.1, 0.0, 0.0),
        (0.0, 1.1, 0.0),
        (-1.1, 0.0, 0.0),
        (0.0, -1.1, 0.0),
        (0.0, 0.0, -1.35),
    ]
    faces = [
        (0, 1, 2),
        (0, 2, 3),
        (0, 3, 4),
        (0, 4, 1),
        (5, 2, 1),
        (5, 3, 2),
        (5, 4, 3),
        (5, 1, 4),
    ]
    return add_mesh_object(name, verts, faces, location, material, "Octa Cut")


def add_hexagonal_prism(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=1.02, depth=2.15, location=location, rotation=(0.0, 0.0, math.radians(30.0)))
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    obj["Aerathea.PrimitiveStage"] = "P01 basic primitive"
    obj["Aerathea.PrimitiveName"] = "Hexagonal Prism"
    return obj


def icosahedron_data(radius: float = 1.22) -> tuple[list[tuple[float, float, float]], list[tuple[int, int, int]]]:
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    raw = [
        (-1, phi, 0),
        (1, phi, 0),
        (-1, -phi, 0),
        (1, -phi, 0),
        (0, -1, phi),
        (0, 1, phi),
        (0, -1, -phi),
        (0, 1, -phi),
        (phi, 0, -1),
        (phi, 0, 1),
        (-phi, 0, -1),
        (-phi, 0, 1),
    ]
    verts = []
    for vert in raw:
        vec = Vector(vert).normalized() * radius
        verts.append((vec.x, vec.y, vec.z))
    faces = [
        (0, 11, 5),
        (0, 5, 1),
        (0, 1, 7),
        (0, 7, 10),
        (0, 10, 11),
        (1, 5, 9),
        (5, 11, 4),
        (11, 10, 2),
        (10, 7, 6),
        (7, 1, 8),
        (3, 9, 4),
        (3, 4, 2),
        (3, 2, 6),
        (3, 6, 8),
        (3, 8, 9),
        (4, 9, 5),
        (2, 4, 11),
        (6, 2, 10),
        (8, 6, 7),
        (9, 8, 1),
    ]
    return verts, faces


def add_icosahedron(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    verts, faces = icosahedron_data()
    return add_mesh_object(name, verts, faces, location, material, "Icosahedron")


def add_dodecahedron(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    ico_verts_raw, ico_faces = icosahedron_data(1.0)
    ico_verts = [Vector(vert) for vert in ico_verts_raw]
    centers = []
    for face in ico_faces:
        center = (ico_verts[face[0]] + ico_verts[face[1]] + ico_verts[face[2]]) / 3.0
        centers.append(center.normalized() * 1.16)

    faces_by_vertex: list[list[int]] = [[] for _ in ico_verts]
    for face_index, face in enumerate(ico_faces):
        for vertex_index in face:
            faces_by_vertex[vertex_index].append(face_index)

    dodeca_faces: list[tuple[int, ...]] = []
    for vertex, adjacent_faces in zip(ico_verts, faces_by_vertex):
        normal = vertex.normalized()
        reference = Vector((0.0, 0.0, 1.0))
        if abs(normal.dot(reference)) > 0.92:
            reference = Vector((0.0, 1.0, 0.0))
        u_axis = normal.cross(reference).normalized()
        v_axis = normal.cross(u_axis).normalized()

        def angle(face_index: int) -> float:
            projected = centers[face_index] - normal * centers[face_index].dot(normal)
            return math.atan2(projected.dot(v_axis), projected.dot(u_axis))

        ordered = tuple(sorted(adjacent_faces, key=angle))
        dodeca_faces.append(ordered)

    verts = [(center.x, center.y, center.z) for center in centers]
    return add_mesh_object(name, verts, dodeca_faces, location, material, "Dodecahedron")


def add_pentagonal_trapezohedron(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    radius = 1.12
    polar_z = 1.38
    # The local training reference presents the D10 as a simplified five-waist
    # form: top pole, bottom pole, and a pentagonal belt. Match that visual
    # scaffold here instead of using the stricter two-ring deltohedron variant.
    equator: list[tuple[float, float, float]] = []
    for index in range(5):
        angle = (math.tau * index / 5.0) + math.radians(18.0)
        equator.append((math.cos(angle) * radius, math.sin(angle) * radius, 0.0))
    verts = [(0.0, 0.0, polar_z), (0.0, 0.0, -polar_z)] + equator
    faces: list[tuple[int, int, int]] = []
    for index in range(5):
        next_index = (index + 1) % 5
        current = 2 + index
        next_vertex = 2 + next_index
        faces.append((0, current, next_vertex))
        faces.append((1, next_vertex, current))
    return add_mesh_object(name, verts, faces, location, material, "Pentagonal Trapezohedron Reference Form")


def add_zocchihedron(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20, ring_count=10, radius=1.08, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    bpy.ops.object.shade_flat()
    obj["Aerathea.PrimitiveStage"] = "P01 basic primitive"
    obj["Aerathea.PrimitiveName"] = "Zocchihedron"
    return obj


def add_cone(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cone_add(vertices=64, radius1=1.05, radius2=0.0, depth=2.25, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    obj["Aerathea.PrimitiveStage"] = "P01 basic primitive"
    obj["Aerathea.PrimitiveName"] = "Cone"
    return obj


def add_sphere(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, radius=1.08, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    obj["Aerathea.PrimitiveStage"] = "P01 basic primitive"
    obj["Aerathea.PrimitiveName"] = "Smooth Sphere"
    return obj


def add_cylinder(name: str, location: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(vertices=96, radius=0.92, depth=2.2, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    obj["Aerathea.PrimitiveStage"] = "P01 basic primitive"
    obj["Aerathea.PrimitiveName"] = "Cylinder"
    return obj


def add_ground_plane(material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, -0.08))
    plane = bpy.context.object
    plane.name = "P01_NeutralReviewBase"
    plane.dimensions = (18.0, 8.5, 0.08)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    plane.data.materials.append(material)
    return plane


def configure_scene() -> bpy.types.Object:
    world = bpy.context.scene.world or bpy.data.worlds.new("P01_PrimitiveWorld")
    bpy.context.scene.world = world
    world.color = (0.70, 0.70, 0.68)

    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE"
        scene.eevee.use_gtao = True
        scene.eevee.gtao_distance = 2.4
        scene.eevee.gtao_factor = 0.18
        scene.eevee.taa_render_samples = 64
    except (AttributeError, TypeError):
        pass
    try:
        scene.render.use_freestyle = True
        line_set = scene.view_layers[0].freestyle_settings.linesets[0]
        line_set.linestyle.thickness = 1.2
        line_set.linestyle.color = (0.09, 0.09, 0.085)
    except (AttributeError, IndexError):
        pass
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.92
    scene.view_settings.gamma = 1.0
    scene.render.film_transparent = False

    bpy.ops.object.light_add(type="AREA", location=(-4.5, -5.5, 8.5))
    key = bpy.context.object
    key.name = "P01_Key_Area"
    key.data.energy = 520.0
    key.data.size = 5.5

    bpy.ops.object.light_add(type="AREA", location=(4.5, -4.5, 5.5))
    fill = bpy.context.object
    fill.name = "P01_Fill_Area"
    fill.data.energy = 180.0
    fill.data.size = 6.0

    target = Vector((0.0, 0.0, 1.0))
    bpy.ops.object.camera_add(location=(0.0, -12.5, 7.8))
    camera = bpy.context.object
    camera.name = "P01_PrimitiveReviewCamera"
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 11.6
    look_at(camera, target)
    scene.camera = camera
    return camera


def render(camera: bpy.types.Object, path: Path, resolution: tuple[int, int] = (1800, 1200)) -> None:
    ensure_dir(path.parent)
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.resolution_x = resolution[0]
    scene.render.resolution_y = resolution[1]
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    suffix = "-Bold" if bold else ""
    candidates = [
        f"/usr/share/fonts/truetype/dejavu/DejaVuSans{suffix}.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def render_tile(camera: bpy.types.Object, obj: bpy.types.Object, base: bpy.types.Object, path: Path, ortho_scale: float) -> None:
    state = [(item, item.hide_render, item.hide_viewport) for item in bpy.context.scene.objects]
    try:
        for item in bpy.context.scene.objects:
            if item.type == "MESH" and item not in {obj, base}:
                item.hide_render = True
                item.hide_viewport = True
        camera.data.ortho_scale = ortho_scale
        target = Vector((obj.location.x, obj.location.y, 0.88))
        camera.location = (obj.location.x, obj.location.y - 7.4, 4.6)
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
    title_h = 108
    image_w = 390
    image_h = 286
    label_h = 46
    cell_w = image_w
    cell_h = image_h + label_h
    width = cols * cell_w + (cols + 1) * pad
    height = title_h + rows * cell_h + (rows + 1) * pad

    image = Image.new("RGB", (width, height), (31, 31, 32))
    draw = ImageDraw.Draw(image, "RGBA")
    title_font = load_font(42, bold=True)
    label_font = load_font(25, bold=True)
    note_font = load_font(18)

    draw.rectangle((0, 0, width, 96), fill=(34, 34, 34, 214))
    draw.text((34, 18), "P01 Basic Primitive Board", fill=(238, 232, 220, 255), font=title_font)
    draw.text((38, 66), "no cairn, no paint, no texture", fill=(216, 198, 166, 255), font=note_font)

    for index, (label, tile_path) in enumerate(tile_specs):
        col = index % cols
        row = index // cols
        x = pad + col * (cell_w + pad)
        y = title_h + pad + row * (cell_h + pad)
        draw.rectangle((x, y, x + image_w, y + image_h), fill=(48, 48, 48, 255), outline=(98, 92, 82, 255), width=2)
        tile = Image.open(tile_path).convert("RGB")
        tile.thumbnail((image_w - 10, image_h - 10), Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS)
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
    materials = {
        "cube": make_material("M_P01_Cube", (0.58, 0.58, 0.54)),
        "slab": make_material("M_P01_RectangularSlab", (0.48, 0.53, 0.56)),
        "para": make_material("M_P01_Parallelepiped", (0.52, 0.47, 0.58)),
        "tetra": make_material("M_P01_TetraWedge", (0.58, 0.50, 0.42)),
        "octa": make_material("M_P01_OctaCut", (0.47, 0.56, 0.48)),
        "hex": make_material("M_P01_HexagonalPrism", (0.44, 0.54, 0.56)),
        "ico": make_material("M_P01_Icosahedron", (0.50, 0.58, 0.45)),
        "dodeca": make_material("M_P01_Dodecahedron", (0.58, 0.52, 0.45)),
        "d10": make_material("M_P01_PentagonalTrapezohedron", (0.57, 0.44, 0.42)),
        "zocchi": make_material("M_P01_Zocchihedron", (0.45, 0.48, 0.58)),
        "cone": make_material("M_P01_Cone", (0.58, 0.48, 0.38)),
        "sphere": make_material("M_P01_SmoothSphere", (0.46, 0.55, 0.58)),
        "cylinder": make_material("M_P01_Cylinder", (0.56, 0.52, 0.45)),
        "base": make_material("M_P01_NeutralBase", (0.31, 0.31, 0.30)),
    }

    base = add_ground_plane(materials["base"])
    top_x = [-6.25, -3.75, -1.25, 1.25, 3.75, 6.25]
    bottom_x = [-5.0, -2.5, 0.0, 2.5, 5.0]
    top_y = 1.55
    bottom_y = -1.65
    primitives: list[tuple[str, bpy.types.Object, float]] = [
        ("Cube", add_cube("P01_Cube", (top_x[0], top_y, 1.0), materials["cube"]), 3.4),
        ("Slab", add_rectangular_slab("P01_RectangularSlab", (top_x[1], top_y, 0.7), materials["slab"]), 3.9),
        ("Parallelepiped", add_parallelepiped("P01_Parallelepiped", (top_x[2], top_y, 1.2), materials["para"]), 4.0),
        ("Hex Prism", add_hexagonal_prism("P01_HexagonalPrism", (top_x[3], top_y, 1.08), materials["hex"]), 3.5),
        ("Cylinder", add_cylinder("P01_Cylinder", (top_x[4], top_y, 1.1), materials["cylinder"]), 3.5),
        ("Zocchihedron", add_zocchihedron("P01_Zocchihedron", (top_x[5], top_y, 1.1), materials["zocchi"]), 3.4),
        ("Tetra Wedge", add_tetra_wedge("P01_TetraWedge", (bottom_x[0], bottom_y, 0.82), materials["tetra"]), 3.5),
        ("Octa Cut", add_octa_cut("P01_OctaCut", (bottom_x[1], bottom_y, 1.25), materials["octa"]), 3.7),
        ("Icosahedron", add_icosahedron("P01_Icosahedron", (bottom_x[2], bottom_y, 1.25), materials["ico"]), 3.6),
        ("Dodecahedron", add_dodecahedron("P01_Dodecahedron", (bottom_x[3], bottom_y, 1.25), materials["dodeca"]), 3.7),
        (
            "D10 Trapezohedron",
            add_pentagonal_trapezohedron("P01_PentagonalTrapezohedron", (bottom_x[4], bottom_y, 1.25), materials["d10"]),
            3.6,
        ),
        ("Cone", add_cone("P01_Cone", (-6.25, -4.75, 1.12), materials["cone"]), 3.5),
        ("Smooth Sphere", add_sphere("P01_SmoothSphere", (-3.75, -4.75, 1.08), materials["sphere"]), 3.4),
    ]

    for obj in bpy.context.scene.objects:
        obj["Aerathea.TrainingLane"] = "geometric_primitive_to_cairnstone"
        obj["Aerathea.Stage"] = "P01 Basic Primitive Board"
        obj["Aerathea.NotAssetCandidate"] = True

    camera = configure_scene()
    tile_specs: list[tuple[str, Path]] = []
    for index, (label, obj, ortho_scale) in enumerate(primitives, 1):
        tile_path = TILE_ROOT / f"P01_{index:02d}_{label.replace(' ', '_')}.png"
        render_tile(camera, obj, base, tile_path, ortho_scale)
        tile_specs.append((label, tile_path))
    compose_contact_sheet(tile_specs, REVIEW_IMAGE)
    ensure_dir(DOC_IMAGE.parent)
    shutil.copyfile(REVIEW_IMAGE, DOC_IMAGE)

    blend_path = BLEND_ROOT / f"{ASSET_NAME}.blend"
    ensure_dir(blend_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"P01 primitive board written: {DOC_IMAGE}")


if __name__ == "__main__":
    main()
