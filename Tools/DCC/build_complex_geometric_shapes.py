#!/usr/bin/env python3
"""Build the P01D complex geometric shape board.

This is a shape-training proof only. It collects more advanced geometric
forms that may later inform cairn stone chips, cut logic, negative spaces,
ornamental knots, and stylized magical/mechanical motifs.
"""

from __future__ import annotations

import math
import shutil
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "P01D_ComplexGeometricShapeBoard"
DOC_ROOT = ROOT / "docs" / "assets" / "training" / "geometric_primitives"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "GeometricPrimitives"
TILE_ROOT = REVIEW_ROOT / "complex_shape_tiles"
BLEND_ROOT = ROOT / "SourceAssets" / "Blender" / "Props" / "Training" / "GeometricPrimitives" / ASSET_NAME
DOC_IMAGE = DOC_ROOT / f"{ASSET_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{ASSET_NAME}.png"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_geometric_primitive_bisections import compose_contact_sheet  # noqa: E402
from Tools.DCC.build_geometric_primitive_fundamentals import (  # noqa: E402
    add_ground_plane,
    configure_scene,
    ensure_dir,
    icosahedron_data,
    look_at,
    make_material,
    render,
)
from Tools.DCC.build_next_slice_assets import clear_scene, setup_scene  # noqa: E402


def metadata(obj: bpy.types.Object, name: str, note: str) -> bpy.types.Object:
    obj["Aerathea.TrainingLane"] = "geometric_primitive_to_cairnstone"
    obj["Aerathea.Stage"] = "P01D Complex Geometric Shape Board"
    obj["Aerathea.PrimitiveStage"] = "P01D complex geometric shape"
    obj["Aerathea.PrimitiveName"] = name
    obj["Aerathea.ShapeNote"] = note
    obj["Aerathea.NotAssetCandidate"] = True
    return obj


def make_materials() -> dict[str, bpy.types.Material]:
    return {
        "trunc_ico": make_material("M_P01D_TruncatedIcosahedron", (0.52, 0.58, 0.50)),
        "trunc_dodeca": make_material("M_P01D_TruncatedDodecahedron", (0.55, 0.48, 0.60)),
        "rhombi": make_material("M_P01D_Rhombicuboctahedron", (0.45, 0.56, 0.60)),
        "trunc_cubo": make_material("M_P01D_TruncatedCuboctahedron", (0.60, 0.51, 0.42)),
        "stellated": make_material("M_P01D_StellatedForm", (0.55, 0.44, 0.42)),
        "geodesic": make_material("M_P01D_GeodesicSphere", (0.47, 0.58, 0.48)),
        "torus": make_material("M_P01D_Torus", (0.44, 0.50, 0.60)),
        "mobius": make_material("M_P01D_MobiusStrip", (0.58, 0.53, 0.42)),
        "klein": make_material("M_P01D_KleinBottle", (0.46, 0.57, 0.54)),
        "trefoil": make_material("M_P01D_TrefoilKnot", (0.60, 0.44, 0.50)),
        "helix": make_material("M_P01D_HelixTube", (0.50, 0.45, 0.60)),
        "helicoid": make_material("M_P01D_HelicoidSurface", (0.54, 0.57, 0.46)),
        "base": make_material("M_P01D_NeutralBase", (0.31, 0.31, 0.30)),
    }


def make_mesh_object(
    name: str,
    verts: list[tuple[float, float, float]],
    faces: list[tuple[int, ...]],
    material: bpy.types.Material,
    primitive_name: str,
    note: str,
    *,
    smooth: bool = False,
) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    if smooth:
        for polygon in obj.data.polygons:
            polygon.use_smooth = True
    metadata(obj, primitive_name, note)
    return obj


def normalize_mesh(obj: bpy.types.Object, target_radius: float = 1.24) -> bpy.types.Object:
    bpy.context.view_layer.update()
    corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    center = sum(corners, Vector()) / len(corners)
    extents = [corner - center for corner in corners]
    radius = max(vector.length for vector in extents)
    if radius > 0.001:
        obj.scale *= target_radius / radius
    bpy.context.view_layer.update()
    corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    center = sum(corners, Vector()) / len(corners)
    minimum_z = min(corner.z for corner in corners)
    obj.location -= Vector((center.x, center.y, minimum_z - 0.06))
    return obj


def recalc_normals(obj: bpy.types.Object) -> None:
    bpy.ops.object.mode_set(mode="OBJECT") if bpy.context.object and bpy.context.object.mode != "OBJECT" else None
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode="OBJECT")


def dodecahedron_data(radius: float = 1.0) -> tuple[list[tuple[float, float, float]], list[tuple[int, ...]]]:
    ico_verts_raw, ico_faces = icosahedron_data(1.0)
    ico_verts = [Vector(vert) for vert in ico_verts_raw]
    centers: list[Vector] = []
    for face in ico_faces:
        center = (ico_verts[face[0]] + ico_verts[face[1]] + ico_verts[face[2]]) / 3.0
        centers.append(center.normalized() * radius)

    faces_by_vertex: list[list[int]] = [[] for _ in ico_verts]
    for face_index, face in enumerate(ico_faces):
        for vertex_index in face:
            faces_by_vertex[vertex_index].append(face_index)

    faces: list[tuple[int, ...]] = []
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

        faces.append(tuple(sorted(adjacent_faces, key=angle)))

    verts = [(center.x, center.y, center.z) for center in centers]
    return verts, faces


def truncate_polyhedron(
    verts_raw: list[tuple[float, float, float]],
    faces: list[tuple[int, ...]],
    amount: float,
) -> tuple[list[tuple[float, float, float]], list[tuple[int, ...]]]:
    verts = [Vector(vert) for vert in verts_raw]
    directed_edges: dict[tuple[int, int], int] = {}
    new_verts: list[tuple[float, float, float]] = []

    def edge_index(a: int, b: int) -> int:
        key = (a, b)
        if key not in directed_edges:
            point = verts[a].lerp(verts[b], amount)
            directed_edges[key] = len(new_verts)
            new_verts.append((point.x, point.y, point.z))
        return directed_edges[key]

    new_faces: list[tuple[int, ...]] = []
    neighbors_by_vertex: dict[int, set[int]] = {index: set() for index in range(len(verts))}
    for face in faces:
        face_indices: list[int] = []
        for index, a in enumerate(face):
            b = face[(index + 1) % len(face)]
            face_indices.append(edge_index(a, b))
            face_indices.append(edge_index(b, a))
            neighbors_by_vertex[a].add(b)
            neighbors_by_vertex[b].add(a)
        new_faces.append(tuple(face_indices))

    for vertex_index, neighbors in neighbors_by_vertex.items():
        origin = verts[vertex_index]
        normal = origin.normalized()
        reference = Vector((0.0, 0.0, 1.0))
        if abs(normal.dot(reference)) > 0.92:
            reference = Vector((0.0, 1.0, 0.0))
        u_axis = normal.cross(reference).normalized()
        v_axis = normal.cross(u_axis).normalized()

        def angle(neighbor_index: int) -> float:
            point = Vector(new_verts[edge_index(vertex_index, neighbor_index)])
            projected = point - normal * point.dot(normal)
            return math.atan2(projected.dot(v_axis), projected.dot(u_axis))

        ordered = tuple(edge_index(vertex_index, neighbor_index) for neighbor_index in sorted(neighbors, key=angle))
        if len(ordered) >= 3:
            new_faces.append(ordered)

    return new_verts, new_faces


def add_truncated_icosahedron(material: bpy.types.Material) -> bpy.types.Object:
    verts, faces = icosahedron_data(1.0)
    new_verts, new_faces = truncate_polyhedron(verts, [tuple(face) for face in faces], 1.0 / 3.0)
    obj = make_mesh_object(
        "P01D_TruncatedIcosahedron",
        new_verts,
        new_faces,
        material,
        "Truncated Icosahedron",
        "Soccer-ball style Archimedean scaffold: pentagon and hexagon rhythm.",
    )
    recalc_normals(obj)
    return normalize_mesh(obj)


def add_truncated_dodecahedron(material: bpy.types.Material) -> bpy.types.Object:
    verts, faces = dodecahedron_data(1.15)
    new_verts, new_faces = truncate_polyhedron(verts, faces, 0.30)
    obj = make_mesh_object(
        "P01D_TruncatedDodecahedron",
        new_verts,
        new_faces,
        material,
        "Truncated Dodecahedron",
        "Dodecahedron-derived scaffold with broader decagonal planes and clipped corners.",
    )
    recalc_normals(obj)
    return normalize_mesh(obj)


def convex_hull_object(
    name: str,
    points: list[tuple[float, float, float]],
    material: bpy.types.Material,
    primitive_name: str,
    note: str,
) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    bm = bmesh.new()
    bm_verts = [bm.verts.new(point) for point in points]
    bm.verts.ensure_lookup_table()
    result = bmesh.ops.convex_hull(bm, input=bm_verts)
    discard = list(result.get("geom_unused", [])) + list(result.get("geom_interior", []))
    if discard:
        bmesh.ops.delete(bm, geom=discard, context="VERTS")
    bm.to_mesh(mesh)
    bm.free()
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    metadata(obj, primitive_name, note)
    recalc_normals(obj)
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.dissolve_limited(angle_limit=math.radians(0.5))
    bpy.ops.object.mode_set(mode="OBJECT")
    return normalize_mesh(obj)


def signed_permutations(values: tuple[float, float, float]) -> list[tuple[float, float, float]]:
    points: set[tuple[float, float, float]] = set()
    for permutation in {
        (values[0], values[1], values[2]),
        (values[0], values[2], values[1]),
        (values[1], values[0], values[2]),
        (values[1], values[2], values[0]),
        (values[2], values[0], values[1]),
        (values[2], values[1], values[0]),
    }:
        for sx in (-1.0, 1.0):
            for sy in (-1.0, 1.0):
                for sz in (-1.0, 1.0):
                    points.add((sx * permutation[0], sy * permutation[1], sz * permutation[2]))
    return sorted(points)


def add_rhombicuboctahedron(material: bpy.types.Material) -> bpy.types.Object:
    root_two = math.sqrt(2.0)
    points = signed_permutations((1.0, 1.0, 1.0 + root_two))
    return convex_hull_object(
        "P01D_Rhombicuboctahedron",
        points,
        material,
        "Rhombicuboctahedron",
        "Expanded cube/octahedron form with square and triangle face language.",
    )


def add_truncated_cuboctahedron(material: bpy.types.Material) -> bpy.types.Object:
    root_two = math.sqrt(2.0)
    points = signed_permutations((1.0, 1.0 + root_two, 1.0 + 2.0 * root_two))
    return convex_hull_object(
        "P01D_TruncatedCuboctahedron",
        points,
        material,
        "Truncated Cuboctahedron",
        "Expanded Archimedean block form with square, hexagonal, and octagonal visual beats.",
    )


def add_stellated_form(material: bpy.types.Material) -> bpy.types.Object:
    verts_raw, faces_raw = icosahedron_data(1.0)
    verts = [Vector(vert) for vert in verts_raw]
    new_verts: list[tuple[float, float, float]] = [(vert.x, vert.y, vert.z) for vert in verts]
    new_faces: list[tuple[int, int, int]] = []
    for face in faces_raw:
        center = (verts[face[0]] + verts[face[1]] + verts[face[2]]) / 3.0
        apex = center.normalized() * 1.92
        apex_index = len(new_verts)
        new_verts.append((apex.x, apex.y, apex.z))
        a, b, c = face
        new_faces.extend([(a, b, apex_index), (b, c, apex_index), (c, a, apex_index)])
    obj = make_mesh_object(
        "P01D_StellatedIcosaForm",
        new_verts,
        new_faces,
        material,
        "Stellated Icosa Form",
        "Great-stellated-dodecahedron reference simplified into readable triangular spikes.",
    )
    recalc_normals(obj)
    return normalize_mesh(obj)


def add_geodesic_sphere(material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, radius=1.08, location=(0.0, 0.0, 1.1))
    obj = bpy.context.object
    obj.name = "P01D_GeodesicSphere"
    obj.data.name = "P01D_GeodesicSphere_Mesh"
    obj.data.materials.append(material)
    metadata(obj, "Geodesic Sphere", "Triangular-facet sphere approximation for dome and faceted stone training.")
    return obj


def add_torus(material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_torus_add(
        major_segments=96,
        minor_segments=24,
        location=(0.0, 0.0, 1.1),
        major_radius=0.82,
        minor_radius=0.22,
    )
    obj = bpy.context.object
    obj.name = "P01D_Torus"
    obj.data.name = "P01D_Torus_Mesh"
    obj.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    metadata(obj, "Torus", "Ring topology for negative-space and portal-silhouette training.")
    return obj


def add_mobius_strip(material: bpy.types.Material) -> bpy.types.Object:
    u_segments = 128
    v_segments = 14
    radius = 1.05
    width = 0.34
    verts: list[tuple[float, float, float]] = []
    faces: list[tuple[int, int, int, int]] = []
    for i in range(u_segments):
        u = math.tau * i / u_segments
        for j in range(v_segments + 1):
            v = -width + (2.0 * width * j / v_segments)
            x = (radius + v * math.cos(u / 2.0)) * math.cos(u)
            y = (radius + v * math.cos(u / 2.0)) * math.sin(u)
            z = v * math.sin(u / 2.0)
            verts.append((x, y, z))

    def index(i: int, j: int) -> int:
        if i == u_segments:
            return j
        return i * (v_segments + 1) + j

    for i in range(u_segments):
        next_i = (i + 1) % u_segments
        for j in range(v_segments):
            a = index(i, j)
            b = index(next_i, j if next_i != 0 else v_segments - j)
            c = index(next_i, j + 1 if next_i != 0 else v_segments - j - 1)
            d = index(i, j + 1)
            faces.append((a, b, c, d))

    obj = make_mesh_object(
        "P01D_MobiusStrip",
        verts,
        faces,
        material,
        "Mobius Strip",
        "One-sided twisted strip reference for continuous bands and carved loops.",
        smooth=True,
    )
    return normalize_mesh(obj)


def add_klein_bottle(material: bpy.types.Material) -> bpy.types.Object:
    u_segments = 96
    v_segments = 36
    verts: list[tuple[float, float, float]] = []
    faces: list[tuple[int, int, int, int]] = []
    for i in range(u_segments):
        u = math.tau * i / u_segments
        for j in range(v_segments):
            v = math.tau * j / v_segments
            if u < math.pi:
                x = 3.0 * math.cos(u) * (1.0 + math.sin(u)) + 2.0 * (1.0 - math.cos(u) / 2.0) * math.cos(u) * math.cos(v)
                z = -8.0 * math.sin(u) - 2.0 * (1.0 - math.cos(u) / 2.0) * math.sin(u) * math.cos(v)
            else:
                x = 3.0 * math.cos(u) * (1.0 + math.sin(u)) + 2.0 * (1.0 - math.cos(u) / 2.0) * math.cos(v + math.pi)
                z = -8.0 * math.sin(u)
            y = -2.0 * (1.0 - math.cos(u) / 2.0) * math.sin(v)
            verts.append((x * 0.13, y * 0.13, z * 0.13))

    def index(i: int, j: int) -> int:
        return (i % u_segments) * v_segments + (j % v_segments)

    for i in range(u_segments):
        for j in range(v_segments):
            faces.append((index(i, j), index(i + 1, j), index(i + 1, j + 1), index(i, j + 1)))

    obj = make_mesh_object(
        "P01D_KleinBottle",
        verts,
        faces,
        material,
        "Klein Bottle",
        "Self-intersecting 3D immersion of a boundaryless non-orientable surface.",
        smooth=True,
    )
    return normalize_mesh(obj)


def make_curve_object(
    name: str,
    points: list[tuple[float, float, float]],
    material: bpy.types.Material,
    primitive_name: str,
    note: str,
    *,
    cyclic: bool,
    bevel_depth: float,
) -> bpy.types.Object:
    curve = bpy.data.curves.new(f"{name}_Curve", type="CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 16
    curve.bevel_depth = bevel_depth
    curve.bevel_resolution = 5
    spline = curve.splines.new("POLY")
    spline.points.add(len(points) - 1)
    for point, co in zip(spline.points, points):
        point.co = (co[0], co[1], co[2], 1.0)
    spline.use_cyclic_u = cyclic
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    metadata(obj, primitive_name, note)
    return normalize_mesh(obj)


def add_trefoil_knot(material: bpy.types.Material) -> bpy.types.Object:
    points: list[tuple[float, float, float]] = []
    for i in range(220):
        t = math.tau * i / 220
        x = math.sin(t) + 2.0 * math.sin(2.0 * t)
        y = math.cos(t) - 2.0 * math.cos(2.0 * t)
        z = -math.sin(3.0 * t)
        points.append((x * 0.42, y * 0.42, z * 0.42))
    return make_curve_object(
        "P01D_TrefoilKnot",
        points,
        material,
        "Trefoil Knot",
        "Simplest non-trivial closed knot, useful for looped ornament and rope logic.",
        cyclic=True,
        bevel_depth=0.055,
    )


def add_helix_tube(material: bpy.types.Material) -> bpy.types.Object:
    points: list[tuple[float, float, float]] = []
    turns = 3.3
    for i in range(220):
        t = math.tau * turns * i / 219
        z = -1.05 + 2.1 * i / 219
        points.append((math.cos(t) * 0.78, math.sin(t) * 0.78, z))
    return make_curve_object(
        "P01D_HelixTube",
        points,
        material,
        "Helix Tube",
        "Spiral tube reference for coils, carved wraps, and rotational rhythm.",
        cyclic=False,
        bevel_depth=0.06,
    )


def add_helicoid_surface(material: bpy.types.Material) -> bpy.types.Object:
    radial_segments = 18
    turn_segments = 96
    verts: list[tuple[float, float, float]] = []
    faces: list[tuple[int, int, int, int]] = []
    for i in range(turn_segments):
        v = math.tau * 2.3 * i / (turn_segments - 1)
        for j in range(radial_segments):
            radius = 0.16 + 0.94 * j / (radial_segments - 1)
            x = radius * math.cos(v)
            y = radius * math.sin(v)
            z = -0.95 + 1.9 * i / (turn_segments - 1)
            verts.append((x, y, z))

    def index(i: int, j: int) -> int:
        return i * radial_segments + j

    for i in range(turn_segments - 1):
        for j in range(radial_segments - 1):
            faces.append((index(i, j), index(i + 1, j), index(i + 1, j + 1), index(i, j + 1)))

    obj = make_mesh_object(
        "P01D_HelicoidSurface",
        verts,
        faces,
        material,
        "Helicoid Surface",
        "Twisting ruled surface for blade, ramp, and spiral-slice studies.",
        smooth=True,
    )
    return normalize_mesh(obj)


def object_world_bounds(obj: bpy.types.Object) -> tuple[Vector, Vector]:
    bpy.context.view_layer.update()
    corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    minimum = Vector((min(corner.x for corner in corners), min(corner.y for corner in corners), min(corner.z for corner in corners)))
    maximum = Vector((max(corner.x for corner in corners), max(corner.y for corner in corners), max(corner.z for corner in corners)))
    return minimum, maximum


def render_complex_tile(
    camera: bpy.types.Object,
    obj: bpy.types.Object,
    base: bpy.types.Object,
    path: Path,
    ortho_scale: float,
) -> None:
    visible = {obj, base}
    state = [(item, item.hide_render, item.hide_viewport) for item in bpy.context.scene.objects]
    try:
        for item in bpy.context.scene.objects:
            if item.type in {"MESH", "CURVE"} and item not in visible:
                item.hide_render = True
                item.hide_viewport = True
        minimum, maximum = object_world_bounds(obj)
        center = (minimum + maximum) * 0.5
        span = maximum - minimum
        camera.data.ortho_scale = max(ortho_scale, max(span.x, span.y, span.z) * 1.48)
        target = Vector((center.x, center.y, center.z + 0.02))
        camera.location = (center.x + 0.25, center.y - 7.4, center.z + 4.65)
        look_at(camera, target)
        render(camera, path, (620, 460))
    finally:
        for item, hide_render, hide_viewport in state:
            item.hide_render = hide_render
            item.hide_viewport = hide_viewport


def main() -> None:
    clear_scene()
    setup_scene()
    materials = make_materials()
    base = add_ground_plane(materials["base"])
    base.name = "P01D_NeutralReviewBase"

    build_specs = [
        ("Truncated Icosahedron", lambda: add_truncated_icosahedron(materials["trunc_ico"]), 4.0),
        ("Truncated Dodecahedron", lambda: add_truncated_dodecahedron(materials["trunc_dodeca"]), 4.2),
        ("Rhombicuboctahedron", lambda: add_rhombicuboctahedron(materials["rhombi"]), 4.0),
        ("Truncated Cuboctahedron", lambda: add_truncated_cuboctahedron(materials["trunc_cubo"]), 4.1),
        ("Stellated Icosa Form", lambda: add_stellated_form(materials["stellated"]), 4.1),
        ("Geodesic Sphere", lambda: add_geodesic_sphere(materials["geodesic"]), 3.7),
        ("Torus", lambda: add_torus(materials["torus"]), 3.5),
        ("Mobius Strip", lambda: add_mobius_strip(materials["mobius"]), 3.6),
        ("Klein Bottle", lambda: add_klein_bottle(materials["klein"]), 3.9),
        ("Trefoil Knot", lambda: add_trefoil_knot(materials["trefoil"]), 3.9),
        ("Helix Tube", lambda: add_helix_tube(materials["helix"]), 3.8),
        ("Helicoid Surface", lambda: add_helicoid_surface(materials["helicoid"]), 3.8),
    ]

    camera = configure_scene()
    tile_specs: list[tuple[str, Path]] = []
    for index, (label, builder, ortho_scale) in enumerate(build_specs, 1):
        obj = builder()
        tile_path = TILE_ROOT / f"P01D_{index:02d}_{label.replace(' ', '_')}.png"
        render_complex_tile(camera, obj, base, tile_path, ortho_scale)
        tile_specs.append((label, tile_path))

    compose_contact_sheet(
        tile_specs,
        REVIEW_IMAGE,
        title="P01D Complex Geometric Shape Board",
        subtitle="reference-built 3D forms: expanded solids, stellation, topology, knots, and spiral surfaces",
    )
    ensure_dir(DOC_IMAGE.parent)
    shutil.copyfile(REVIEW_IMAGE, DOC_IMAGE)

    blend_path = BLEND_ROOT / f"{ASSET_NAME}.blend"
    ensure_dir(blend_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"P01D complex geometric shape board written: {DOC_IMAGE}")


if __name__ == "__main__":
    main()
