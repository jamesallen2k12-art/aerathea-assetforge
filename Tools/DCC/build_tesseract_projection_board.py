#!/usr/bin/env python3
"""Build the P01E tesseract projection board.

This is a geometric training proof: a tesseract is a 4D hypercube, so the
visible asset is a 3D projection made from the full 16-vertex, 32-edge graph.
"""

from __future__ import annotations

import math
import shutil
import sys
from pathlib import Path
from typing import Callable

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "P01E_TesseractProjectionBoard"
DOC_ROOT = ROOT / "docs" / "assets" / "training" / "geometric_primitives"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "GeometricPrimitives"
TILE_ROOT = REVIEW_ROOT / "tesseract_tiles"
BLEND_ROOT = ROOT / "SourceAssets" / "Blender" / "Props" / "Training" / "GeometricPrimitives" / ASSET_NAME
DOC_IMAGE = DOC_ROOT / f"{ASSET_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{ASSET_NAME}.png"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_geometric_primitive_bisections import compose_contact_sheet  # noqa: E402
from Tools.DCC.build_geometric_primitive_fundamentals import (  # noqa: E402
    add_ground_plane,
    configure_scene,
    ensure_dir,
    load_font,
    look_at,
    make_material,
    render,
)
from Tools.DCC.build_next_slice_assets import clear_scene, setup_scene  # noqa: E402


Point4 = tuple[float, float, float, float]
Point3 = tuple[float, float, float]


def make_materials() -> dict[str, bpy.types.Material]:
    materials = {
        "edge_xyz": make_material("M_P01E_Tesseract_XYZ_Edges", (0.58, 0.62, 0.62), roughness=0.75),
        "edge_w": make_material("M_P01E_Tesseract_W_Edges", (0.42, 0.62, 0.86), roughness=0.7),
        "vertex_outer": make_material("M_P01E_Tesseract_OuterVertices", (0.76, 0.72, 0.58), roughness=0.65),
        "vertex_inner": make_material("M_P01E_Tesseract_InnerVertices", (0.48, 0.67, 0.90), roughness=0.65),
        "face": make_material("M_P01E_Tesseract_GuideFaces", (0.40, 0.54, 0.70), roughness=0.92),
        "base": make_material("M_P01E_NeutralBase", (0.31, 0.31, 0.30)),
    }
    face = materials["face"]
    face.blend_method = "BLEND"
    face.use_nodes = True
    bsdf = face.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Alpha"].default_value = 0.18
        bsdf.inputs["Roughness"].default_value = 0.96
    face.diffuse_color = (0.40, 0.54, 0.70, 0.18)
    return materials


def tesseract_vertices() -> list[Point4]:
    vertices: list[Point4] = []
    for x in (-1.0, 1.0):
        for y in (-1.0, 1.0):
            for z in (-1.0, 1.0):
                for w in (-1.0, 1.0):
                    vertices.append((x, y, z, w))
    return vertices


def tesseract_edges(vertices: list[Point4]) -> list[tuple[int, int, int]]:
    edges: list[tuple[int, int, int]] = []
    for a, first in enumerate(vertices):
        for b in range(a + 1, len(vertices)):
            second = vertices[b]
            changed = [index for index in range(4) if abs(first[index] - second[index]) > 0.01]
            if len(changed) == 1:
                edges.append((a, b, changed[0]))
    return edges


def rotate4(point: Point4, rotations: list[tuple[int, int, float]]) -> Point4:
    coords = list(point)
    for a, b, angle in rotations:
        ca = math.cos(angle)
        sa = math.sin(angle)
        av = coords[a]
        bv = coords[b]
        coords[a] = av * ca - bv * sa
        coords[b] = av * sa + bv * ca
    return (coords[0], coords[1], coords[2], coords[3])


def perspective_project(point: Point4, distance: float = 4.0) -> Point3:
    x, y, z, w = point
    factor = distance / (distance + w)
    return (x * factor, y * factor, z * factor)


def orthographic_inner_outer_project(point: Point4) -> Point3:
    x, y, z, w = point
    scale = 1.18 if w < 0.0 else 0.54
    offset = -0.10 if w < 0.0 else 0.18
    return (x * scale + offset, y * scale + offset, z * scale + offset)


def rotated_projector(rotations: list[tuple[int, int, float]], distance: float = 4.2) -> Callable[[Point4], Point3]:
    def project(point: Point4) -> Point3:
        return perspective_project(rotate4(point, rotations), distance)

    return project


def make_curve_segment(
    name: str,
    a: Vector,
    b: Vector,
    material: bpy.types.Material,
    bevel_depth: float,
) -> bpy.types.Object:
    curve = bpy.data.curves.new(f"{name}_Curve", type="CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 2
    curve.bevel_depth = bevel_depth
    curve.bevel_resolution = 4
    spline = curve.splines.new("POLY")
    spline.points.add(1)
    spline.points[0].co = (a.x, a.y, a.z, 1.0)
    spline.points[1].co = (b.x, b.y, b.z, 1.0)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj


def make_face_object(
    name: str,
    projected: list[Vector],
    face_indices: tuple[int, int, int, int],
    material: bpy.types.Material,
) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    verts = [tuple(projected[index]) for index in face_indices]
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    for polygon in obj.data.polygons:
        polygon.use_smooth = False
    return obj


def cube_faces_for_w(vertices: list[Point4], w_value: float) -> list[tuple[int, int, int, int]]:
    lookup = {vertex: index for index, vertex in enumerate(vertices)}
    faces: list[tuple[int, int, int, int]] = []
    for fixed_axis, fixed_value in ((0, -1.0), (0, 1.0), (1, -1.0), (1, 1.0), (2, -1.0), (2, 1.0)):
        variable_axes = [axis for axis in (0, 1, 2) if axis != fixed_axis]
        corners: list[int] = []
        for first, second in ((-1.0, -1.0), (1.0, -1.0), (1.0, 1.0), (-1.0, 1.0)):
            coords = [0.0, 0.0, 0.0, w_value]
            coords[fixed_axis] = fixed_value
            coords[variable_axes[0]] = first
            coords[variable_axes[1]] = second
            corners.append(lookup[(coords[0], coords[1], coords[2], coords[3])])
        faces.append(tuple(corners))
    return faces


def object_bounds(objects: list[bpy.types.Object]) -> tuple[Vector, Vector]:
    bpy.context.view_layer.update()
    corners = [obj.matrix_world @ Vector(corner) for obj in objects if hasattr(obj, "bound_box") for corner in obj.bound_box]
    minimum = Vector((min(corner.x for corner in corners), min(corner.y for corner in corners), min(corner.z for corner in corners)))
    maximum = Vector((max(corner.x for corner in corners), max(corner.y for corner in corners), max(corner.z for corner in corners)))
    return minimum, maximum


def normalize_group(objects: list[bpy.types.Object], target_radius: float = 1.42) -> None:
    minimum, maximum = object_bounds(objects)
    center = (minimum + maximum) * 0.5
    extents = [corner - center for obj in objects if hasattr(obj, "bound_box") for corner in [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]]
    radius = max(vector.length for vector in extents)
    scale = target_radius / radius if radius > 0.001 else 1.0
    for obj in objects:
        obj.location = (obj.location - center) * scale
        obj.scale *= scale
    bpy.context.view_layer.update()
    minimum, _maximum = object_bounds(objects)
    for obj in objects:
        obj.location.z -= minimum.z - 0.10


def add_tesseract_projection(
    label: str,
    project: Callable[[Point4], Point3],
    materials: dict[str, bpy.types.Material],
    *,
    include_faces: bool,
    vertex_radius: float = 0.075,
    edge_radius: float = 0.025,
) -> list[bpy.types.Object]:
    vertices = tesseract_vertices()
    edges = tesseract_edges(vertices)
    projected = [Vector(project(vertex)) for vertex in vertices]
    objects: list[bpy.types.Object] = []

    if include_faces:
        face_id = 0
        for face in cube_faces_for_w(vertices, -1.0) + cube_faces_for_w(vertices, 1.0):
            obj = make_face_object(f"P01E_{label}_GuideFace_{face_id:02d}", projected, face, materials["face"])
            objects.append(obj)
            face_id += 1

    for edge_index, (a, b, axis) in enumerate(edges):
        material = materials["edge_w"] if axis == 3 else materials["edge_xyz"]
        segment = make_curve_segment(
            f"P01E_{label}_Edge_{edge_index:02d}",
            projected[a],
            projected[b],
            material,
            edge_radius if axis != 3 else edge_radius * 1.18,
        )
        objects.append(segment)

    for index, vertex in enumerate(vertices):
        material = materials["vertex_outer"] if vertex[3] < 0.0 else materials["vertex_inner"]
        bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, radius=vertex_radius, location=projected[index])
        sphere = bpy.context.object
        sphere.name = f"P01E_{label}_Vertex_{index:02d}"
        sphere.data.name = f"{sphere.name}_Mesh"
        sphere.data.materials.append(material)
        objects.append(sphere)

    for obj in objects:
        obj["Aerathea.TrainingLane"] = "geometric_primitive_to_cairnstone"
        obj["Aerathea.Stage"] = "P01E Tesseract Projection Board"
        obj["Aerathea.PrimitiveStage"] = "P01E tesseract projection"
        obj["Aerathea.PrimitiveName"] = "Tesseract"
        obj["Aerathea.ShapeNote"] = "3D projection of a 4D hypercube using 16 vertices and 32 edges."
        obj["Aerathea.NotAssetCandidate"] = True

    normalize_group(objects)
    return objects


def add_axis_legend(materials: dict[str, bpy.types.Material]) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    edge = make_curve_segment(
        "P01E_Legend_W_Dimension_Edge",
        Vector((-0.85, 0.0, 0.04)),
        Vector((0.85, 0.0, 0.04)),
        materials["edge_w"],
        0.05,
    )
    objects.append(edge)
    for x, material, name in ((-0.85, materials["vertex_outer"], "Outer"), (0.85, materials["vertex_inner"], "Inner")):
        bpy.ops.mesh.primitive_uv_sphere_add(segments=20, ring_count=10, radius=0.13, location=(x, 0.0, 0.04))
        sphere = bpy.context.object
        sphere.name = f"P01E_Legend_{name}_Vertex"
        sphere.data.materials.append(material)
        objects.append(sphere)
    for obj in objects:
        obj["Aerathea.Stage"] = "P01E Tesseract Projection Board"
        obj["Aerathea.PrimitiveName"] = "Tesseract Dimension Legend"
        obj["Aerathea.NotAssetCandidate"] = True
    normalize_group(objects, target_radius=1.0)
    return objects


def render_tile_objects(
    camera: bpy.types.Object,
    objects: list[bpy.types.Object],
    base: bpy.types.Object,
    path: Path,
    ortho_scale: float,
) -> None:
    visible = set(objects + [base])
    state = [(item, item.hide_render, item.hide_viewport) for item in bpy.context.scene.objects]
    try:
        for item in bpy.context.scene.objects:
            if item.type in {"MESH", "CURVE", "FONT"} and item not in visible:
                item.hide_render = True
                item.hide_viewport = True
        minimum, maximum = object_bounds(objects)
        center = (minimum + maximum) * 0.5
        span = maximum - minimum
        camera.data.ortho_scale = max(ortho_scale, max(span.x, span.y, span.z) * 1.46)
        target = Vector((center.x, center.y, center.z + 0.02))
        camera.location = (center.x + 0.28, center.y - 7.25, center.z + 4.7)
        look_at(camera, target)
        render(camera, path, (620, 460))
    finally:
        for item, hide_render, hide_viewport in state:
            item.hide_render = hide_render
            item.hide_viewport = hide_viewport


def write_tesseract_notes(path: Path) -> None:
    ensure_dir(path.parent)
    path.write_text(
        "# P01E Tesseract Projection Notes\n\n"
        "- A tesseract is a 4D hypercube.\n"
        "- The Blender scene represents it as a 3D projection with all 16 vertices and 32 edges.\n"
        "- Gray edges are ordinary X/Y/Z cube edges.\n"
        "- Blue edges are W-dimension connector edges between the paired cubes.\n"
        "- Gold vertices belong to the outer projected cube; blue vertices belong to the inner projected cube.\n"
        "- This is a training proof, not a game-ready asset candidate.\n",
        encoding="utf-8",
    )


def main() -> None:
    clear_scene()
    setup_scene()
    materials = make_materials()
    base = add_ground_plane(materials["base"])
    base.name = "P01E_NeutralReviewBase"

    specs: list[tuple[str, Callable[[], list[bpy.types.Object]], float]] = [
        (
            "Classic Projection",
            lambda: add_tesseract_projection("Classic", orthographic_inner_outer_project, materials, include_faces=True),
            4.1,
        ),
        (
            "4D Rotated Projection",
            lambda: add_tesseract_projection(
                "Rotated",
                rotated_projector([(0, 3, math.radians(28)), (1, 3, math.radians(-22)), (0, 2, math.radians(16))]),
                materials,
                include_faces=False,
            ),
            4.0,
        ),
        (
            "W-Dimension Emphasis",
            lambda: add_tesseract_projection(
                "WDimension",
                rotated_projector([(2, 3, math.radians(34)), (0, 1, math.radians(18))], distance=3.8),
                materials,
                include_faces=False,
                vertex_radius=0.082,
                edge_radius=0.03,
            ),
            4.0,
        ),
        ("W Edge Legend", lambda: add_axis_legend(materials), 3.5),
    ]

    camera = configure_scene()
    tile_specs: list[tuple[str, Path]] = []
    for index, (label, builder, ortho_scale) in enumerate(specs, 1):
        objects = builder()
        tile_path = TILE_ROOT / f"P01E_{index:02d}_{label.replace(' ', '_')}.png"
        render_tile_objects(camera, objects, base, tile_path, ortho_scale)
        tile_specs.append((label, tile_path))

    compose_contact_sheet(
        tile_specs,
        REVIEW_IMAGE,
        title="P01E Tesseract Projection Board",
        subtitle="4D hypercube shown as 3D projections: 16 vertices, 32 edges, W-dimension connectors marked blue",
    )
    ensure_dir(DOC_IMAGE.parent)
    shutil.copyfile(REVIEW_IMAGE, DOC_IMAGE)

    write_tesseract_notes(DOC_ROOT / "P01E_TesseractProjectionNotes.md")

    blend_path = BLEND_ROOT / f"{ASSET_NAME}.blend"
    ensure_dir(blend_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"P01E tesseract projection board written: {DOC_IMAGE}")


if __name__ == "__main__":
    main()
