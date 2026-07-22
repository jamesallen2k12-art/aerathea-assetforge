#!/usr/bin/env python3
"""Build the isolated A08 Blender-only Siege Breaker pommel candidate.

This script consumes the immutable concept only as a displayed source reference
and uses the authoritative 18 x 11 cm pommel bounds. It imports no prior Siege
Breaker geometry, textures, masks, or generated views.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
CONTRACT_ID = "SB-BSR-A08-STEP01-POMMEL"
SOURCE_REL = Path("SourceAssets/Concepts/SiegeBreaker/siege_breaker_concept_view.png")
SOURCE_SHA256 = "9f1ac142a5047968bb20c74216c2dccf61470ed9f4e21689ff01934bd849c586"
PLAN_REL = Path("docs/assets/blueprints") / ASSET / f"{ASSET}_BLENDER_ONLY_SOURCE_RECONSTRUCTION_A08_PLAN.md"
CONTRACT_REL = Path("docs/assets/blueprints") / ASSET / "steps/A08_STEP_01_POMMEL_SOURCE_RECONSTRUCTION_CONTRACT.md"
OUTPUT_ROOT_REL = Path("SourceAssets/Blender/Weapons/Dwarven") / ASSET / "A08_BlenderOnly_Pommel_A01"
BLEND_REL = OUTPUT_ROOT_REL / f"{ASSET}_A08_Pommel_A01.blend"
MANIFEST_REL = Path("docs/assets/blueprints") / ASSET / "manifests/A08_STEP_01_POMMEL_A01_VALIDATION.json"
REVIEW_REL = Path("docs/assets/blueprints") / ASSET / "review/A08_STEP_01_POMMEL_A01_REVIEW.png"
SCRIPT_REL = Path("Tools/DCC/build_siegebreaker_a08_pommel_a01.py")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_authority() -> Dict[str, str]:
    required = {
        "source": ROOT / SOURCE_REL,
        "plan": ROOT / PLAN_REL,
        "contract": ROOT / CONTRACT_REL,
    }
    missing = [str(path) for path in required.values() if not path.is_file()]
    if missing:
        raise RuntimeError(f"missing A08 authority inputs: {missing}")
    source_hash = sha256_file(required["source"])
    if source_hash != SOURCE_SHA256:
        raise RuntimeError(f"source hash mismatch: {source_hash}")
    return {name: sha256_file(path) for name, path in required.items()}


def material_principled(
    bpy: Any,
    name: str,
    color: Tuple[float, float, float, float],
    metallic: float,
    roughness: float,
    emission: Tuple[float, float, float, float] | None = None,
    emission_strength: float = 0.0,
) -> Any:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    shader = material.node_tree.nodes.get("Principled BSDF")
    shader.inputs["Base Color"].default_value = color
    shader.inputs["Metallic"].default_value = metallic
    shader.inputs["Roughness"].default_value = roughness
    if emission is not None:
        shader.inputs["Emission"].default_value = emission
        shader.inputs["Emission Strength"].default_value = emission_strength
    return material


def material_emission(bpy: Any, name: str, color: Tuple[float, float, float, float], strength: float = 1.0) -> Any:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    emission = nodes.new("ShaderNodeEmission")
    emission.inputs["Color"].default_value = color
    emission.inputs["Strength"].default_value = strength
    links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return material


def assign_material(obj: Any, material: Any) -> None:
    obj.data.materials.clear()
    obj.data.materials.append(material)


def create_mesh(bpy: Any, name: str, vertices: Sequence[Tuple[float, float, float]], faces: Sequence[Sequence[int]], material: Any, collection: Any) -> Any:
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(list(vertices), [], [list(face) for face in faces])
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    assign_material(obj, material)
    for polygon in mesh.polygons:
        polygon.use_smooth = False
    return obj


def ring_loft(
    bpy: Any,
    name: str,
    profiles: Sequence[Tuple[float, float, float]],
    segments: int,
    material: Any,
    collection: Any,
    phase: float = math.pi / 8.0,
) -> Any:
    vertices: List[Tuple[float, float, float]] = []
    for z_value, radius_x, radius_y in profiles:
        for index in range(segments):
            angle = phase + math.tau * index / segments
            vertices.append((radius_x * math.cos(angle), radius_y * math.sin(angle), z_value))
    faces: List[List[int]] = []
    for ring_index in range(len(profiles) - 1):
        start = ring_index * segments
        next_start = (ring_index + 1) * segments
        for index in range(segments):
            nxt = (index + 1) % segments
            faces.append([start + index, start + nxt, next_start + nxt, next_start + index])
    bottom_center = len(vertices)
    vertices.append((0.0, 0.0, profiles[0][0]))
    top_center = len(vertices)
    vertices.append((0.0, 0.0, profiles[-1][0]))
    top_start = (len(profiles) - 1) * segments
    for index in range(segments):
        nxt = (index + 1) % segments
        faces.append([bottom_center, nxt, index])
        faces.append([top_center, top_start + index, top_start + nxt])
    return create_mesh(bpy, name, vertices, faces, material, collection)


def add_cylinder(bpy: Any, name: str, radius: float, depth: float, z_value: float, material: Any, collection: Any, vertices: int = 16) -> Any:
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, end_fill_type="NGON", location=(0.0, 0.0, z_value))
    obj = bpy.context.active_object
    obj.name = name
    for linked in list(obj.users_collection):
        linked.objects.unlink(obj)
    collection.objects.link(obj)
    assign_material(obj, material)
    for polygon in obj.data.polygons:
        polygon.use_smooth = False
    return obj


def add_torus(bpy: Any, name: str, major_radius: float, minor_radius: float, z_value: float, material: Any, collection: Any) -> Any:
    bpy.ops.mesh.primitive_torus_add(
        align="WORLD",
        location=(0.0, 0.0, z_value),
        major_segments=16,
        minor_segments=4,
        major_radius=major_radius,
        minor_radius=minor_radius,
    )
    obj = bpy.context.active_object
    obj.name = name
    for linked in list(obj.users_collection):
        linked.objects.unlink(obj)
    collection.objects.link(obj)
    assign_material(obj, material)
    for polygon in obj.data.polygons:
        polygon.use_smooth = False
    return obj


def diamond_prism(
    bpy: Any,
    name: str,
    center_z: float,
    width: float,
    height: float,
    y_back: float,
    y_front: float,
    material: Any,
    collection: Any,
) -> Any:
    points = [(-width * 0.5, center_z), (0.0, center_z + height * 0.5), (width * 0.5, center_z), (0.0, center_z - height * 0.5)]
    vertices = [(x, y_back, z) for x, z in points] + [(x, y_front, z) for x, z in points]
    faces = [[0, 3, 2, 1], [4, 5, 6, 7]]
    for index in range(4):
        nxt = (index + 1) % 4
        faces.append([index, nxt, 4 + nxt, 4 + index])
    return create_mesh(bpy, name, vertices, faces, material, collection)


def beam_between_xz(
    bpy: Any,
    name: str,
    point_a: Tuple[float, float],
    point_b: Tuple[float, float],
    y_value: float,
    depth: float,
    thickness: float,
    material: Any,
    collection: Any,
) -> Any:
    ax, az = point_a
    bx, bz = point_b
    dx = bx - ax
    dz = bz - az
    length = math.hypot(dx, dz)
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=((ax + bx) * 0.5, y_value, (az + bz) * 0.5))
    obj = bpy.context.active_object
    obj.name = name
    obj.dimensions = (length, depth, thickness)
    obj.rotation_euler[1] = -math.atan2(dz, dx)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bevel = obj.modifiers.new("Small forged edge", "BEVEL")
    bevel.width = 0.10
    bevel.segments = 1
    for linked in list(obj.users_collection):
        linked.objects.unlink(obj)
    collection.objects.link(obj)
    assign_material(obj, material)
    return obj


def diamond_frame(
    bpy: Any,
    prefix: str,
    center_z: float,
    width: float,
    height: float,
    y_value: float,
    depth: float,
    thickness: float,
    material: Any,
    collection: Any,
) -> List[Any]:
    left = (-width * 0.5, center_z)
    top = (0.0, center_z + height * 0.5)
    right = (width * 0.5, center_z)
    bottom = (0.0, center_z - height * 0.5)
    pairs = [(left, top), (top, right), (right, bottom), (bottom, left)]
    return [beam_between_xz(bpy, f"{prefix}_{index:02d}", a, b, y_value, depth, thickness, material, collection) for index, (a, b) in enumerate(pairs, 1)]


def source_crop_plane(bpy: Any, material: Any, collection: Any) -> Any:
    source_width = 1122.0
    source_height = 1402.0
    crop = {"left": 450.0, "top": 1038.0, "right": 690.0, "bottom": 1332.0}
    display_height = 18.0
    display_width = display_height * (crop["right"] - crop["left"]) / (crop["bottom"] - crop["top"])
    center_x = -10.5
    center_z = 9.0
    half_width = display_width * 0.5
    half_height = display_height * 0.5
    vertices = [
        (center_x - half_width, 1.0, center_z - half_height),
        (center_x + half_width, 1.0, center_z - half_height),
        (center_x + half_width, 1.0, center_z + half_height),
        (center_x - half_width, 1.0, center_z + half_height),
    ]
    obj = create_mesh(bpy, "Immutable_Source_Pommel_Display", vertices, [[0, 1, 2, 3]], material, collection)
    uv_layer = obj.data.uv_layers.new(name="UVMap")
    u0 = crop["left"] / source_width
    u1 = crop["right"] / source_width
    v_bottom = 1.0 - crop["bottom"] / source_height
    v_top = 1.0 - crop["top"] / source_height
    coordinates = [(u0, v_bottom), (u1, v_bottom), (u1, v_top), (u0, v_top)]
    for loop_index, uv in enumerate(coordinates):
        uv_layer.data[loop_index].uv = uv
    obj["aerathea_source_path"] = str(SOURCE_REL)
    obj["aerathea_source_sha256"] = SOURCE_SHA256
    obj["aerathea_display_crop_pixels"] = json.dumps(crop)
    obj["aerathea_source_mutated"] = False
    return obj


def source_material(bpy: Any) -> Any:
    material = bpy.data.materials.new("M_A08_ImmutableSourceDisplay")
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    emission = nodes.new("ShaderNodeEmission")
    texture = nodes.new("ShaderNodeTexImage")
    texture.image = bpy.data.images.load(str(ROOT / SOURCE_REL), check_existing=False)
    texture.image.colorspace_settings.name = "sRGB"
    texture.interpolation = "Linear"
    links.new(texture.outputs["Color"], emission.inputs["Color"])
    links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return material


def add_text(bpy: Any, body: str, location: Tuple[float, float, float], size: float, material: Any, collection: Any) -> Any:
    curve = bpy.data.curves.new(f"{body}_Curve", type="FONT")
    curve.body = body
    curve.align_x = "CENTER"
    curve.align_y = "CENTER"
    curve.size = size
    curve.extrude = 0.0
    obj = bpy.data.objects.new(body.replace(" ", "_"), curve)
    collection.objects.link(obj)
    obj.location = location
    obj.rotation_euler = (math.pi * 0.5, 0.0, 0.0)
    curve.materials.append(material)
    return obj


def configure_camera(bpy: Any, collection: Any) -> Any:
    camera_data = bpy.data.cameras.new("A08_Pommel_Review_Camera")
    camera = bpy.data.objects.new("A08_Pommel_Review_Camera", camera_data)
    collection.objects.link(camera)
    camera.location = (0.0, -60.0, 10.0)
    target = (0.0, 0.0, 10.0)
    direction = tuple(target[index] - camera.location[index] for index in range(3))
    from mathutils import Vector

    camera.rotation_euler = Vector(direction).to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 24.0
    bpy.context.scene.camera = camera
    return camera


def add_area_light(bpy: Any, name: str, location: Tuple[float, float, float], energy: float, size: float, collection: Any, target: Tuple[float, float, float]) -> Any:
    from mathutils import Vector

    light_data = bpy.data.lights.new(name, type="AREA")
    light_data.energy = energy
    light_data.size = size
    light = bpy.data.objects.new(name, light_data)
    collection.objects.link(light)
    light.location = location
    light.rotation_euler = (Vector(target) - light.location).to_track_quat("-Z", "Y").to_euler()
    return light


def candidate_bounds(objects: Iterable[Any]) -> Dict[str, List[float]]:
    from mathutils import Vector

    points = []
    for obj in objects:
        if obj.type != "MESH":
            continue
        for corner in obj.bound_box:
            points.append(obj.matrix_local @ Vector(corner))
    minimum = [min(float(point[index]) for point in points) for index in range(3)]
    maximum = [max(float(point[index]) for point in points) for index in range(3)]
    extent = [maximum[index] - minimum[index] for index in range(3)]
    return {"minimum_cm": minimum, "maximum_cm": maximum, "extent_cm": extent}


def mesh_signature(objects: Iterable[Any]) -> str:
    digest = hashlib.sha256()
    for obj in sorted((item for item in objects if item.type == "MESH"), key=lambda item: item.name):
        digest.update(obj.name.encode("utf-8"))
        digest.update(f"|{len(obj.data.vertices)}|{len(obj.data.polygons)}|".encode("ascii"))
        for vertex in obj.data.vertices:
            digest.update(f"{vertex.co.x:.9f},{vertex.co.y:.9f},{vertex.co.z:.9f};".encode("ascii"))
        digest.update(f"@{obj.location.x:.9f},{obj.location.y:.9f},{obj.location.z:.9f};".encode("ascii"))
        digest.update(f"#{obj.rotation_euler.x:.9f},{obj.rotation_euler.y:.9f},{obj.rotation_euler.z:.9f};".encode("ascii"))
    return digest.hexdigest()


def main() -> int:
    authority_hashes = require_authority()
    import bpy

    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene["aerathea_asset_id"] = ASSET
    scene["aerathea_contract_id"] = CONTRACT_ID
    scene["aerathea_artifact_status"] = "candidate pending Flamestrike visual decision"
    scene["aerathea_historical_geometry_inputs"] = 0
    scene["aerathea_generation_software_used"] = "Blender only"
    scene["aerathea_hidden_surface_authority"] = False
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.01

    candidate_collection = bpy.data.collections.new("A08_POMMEL_CANDIDATE")
    review_collection = bpy.data.collections.new("A08_REVIEW_ONLY")
    scene.collection.children.link(candidate_collection)
    scene.collection.children.link(review_collection)

    bronze = material_principled(bpy, "M_A08_AgedBronze", (0.20, 0.105, 0.035, 1.0), 0.78, 0.28)
    steel = material_principled(bpy, "M_A08_BlackenedSteel", (0.025, 0.032, 0.045, 1.0), 0.88, 0.24)
    recess = material_principled(bpy, "M_A08_Recess", (0.006, 0.009, 0.014, 1.0), 0.55, 0.38)
    rune = material_principled(
        bpy,
        "M_A08_BlueRune",
        (0.015, 0.20, 0.48, 1.0),
        0.18,
        0.18,
        emission=(0.01, 0.22, 1.0, 1.0),
        emission_strength=3.2,
    )
    white = material_emission(bpy, "M_A08_LabelWhite", (0.85, 0.88, 0.92, 1.0), 1.0)
    muted = material_emission(bpy, "M_A08_LabelMuted", (0.42, 0.48, 0.58, 1.0), 1.0)

    candidate_objects: List[Any] = []
    body_profiles = (
        (0.0, 0.0, 0.0),
        (1.3, 1.65, 1.45),
        (3.3, 3.65, 3.10),
        (4.7, 4.45, 3.70),
        (6.6, 5.10, 4.05),
        (9.7, 5.50, 4.25),
        (12.8, 5.18, 4.08),
        (14.8, 4.72, 3.82),
        (16.0, 4.20, 3.45),
        (17.1, 3.30, 2.90),
        (18.0, 2.50, 2.35),
    )
    candidate_objects.append(ring_loft(bpy, "SB_C006_Pommel_FacetedBody_A08", body_profiles, 8, steel, candidate_collection))
    candidate_objects.append(add_torus(bpy, "SB_C006_Pommel_LowerForgedBand_A08", 4.72, 0.34, 5.0, bronze, candidate_collection))
    candidate_objects.append(add_torus(bpy, "SB_C006_Pommel_ShoulderBand_A08", 5.15, 0.35, 14.6, bronze, candidate_collection))
    candidate_objects.append(add_cylinder(bpy, "SB_C006_Pommel_UpperCollar_A08", 4.62, 1.20, 16.25, bronze, candidate_collection, 16))
    candidate_objects.append(add_cylinder(bpy, "SB_C006_Pommel_ShaftReceiver_A08", 2.50, 1.40, 17.30, steel, candidate_collection, 12))

    candidate_objects.append(diamond_prism(bpy, "SB_C006_Pommel_FrontRecess_A08", 10.25, 8.2, 10.8, -4.48, -4.22, recess, candidate_collection))
    candidate_objects.extend(diamond_frame(bpy, "SB_C006_Pommel_BronzeFrame_A08", 10.25, 8.9, 11.6, -4.66, 0.34, 0.72, bronze, candidate_collection))
    candidate_objects.append(diamond_prism(bpy, "SB_C006_Pommel_SteelInset_A08", 10.25, 6.4, 8.5, -4.78, -4.58, steel, candidate_collection))
    candidate_objects.extend(diamond_frame(bpy, "SB_C006_Pommel_SteelFrame_A08", 10.25, 6.8, 8.9, -4.88, 0.26, 0.42, steel, candidate_collection))
    candidate_objects.append(diamond_prism(bpy, "SB_C006_Pommel_RuneCrystal_A08", 10.25, 3.55, 5.25, -5.00, -4.86, rune, candidate_collection))

    candidate_objects.append(beam_between_xz(bpy, "SB_C006_UpperBrace_Left_A08", (-4.15, 14.5), (-2.4, 17.0), -3.65, 0.46, 0.70, bronze, candidate_collection))
    candidate_objects.append(beam_between_xz(bpy, "SB_C006_UpperBrace_Right_A08", (4.15, 14.5), (2.4, 17.0), -3.65, 0.46, 0.70, bronze, candidate_collection))
    candidate_objects.append(beam_between_xz(bpy, "SB_C006_LowerBrace_Left_A08", (-4.35, 6.0), (-2.2, 3.0), -3.45, 0.42, 0.60, bronze, candidate_collection))
    candidate_objects.append(beam_between_xz(bpy, "SB_C006_LowerBrace_Right_A08", (4.35, 6.0), (2.2, 3.0), -3.45, 0.42, 0.60, bronze, candidate_collection))

    root = bpy.data.objects.new("SB_C006_Pommel_A08_ROOT", None)
    candidate_collection.objects.link(root)
    root.location.x = 10.5
    root.rotation_euler.z = math.radians(-5.0)
    root["aerathea_status"] = "candidate"
    root["aerathea_source_owner"] = str(SOURCE_REL)
    root["aerathea_numeric_height_cm"] = 18.0
    root["aerathea_numeric_max_width_cm"] = 11.0
    root["aerathea_depth_status"] = "candidate interpretation; not approved"
    for obj in candidate_objects:
        obj.parent = root

    source_crop_plane(bpy, source_material(bpy), review_collection)
    add_text(bpy, "AUTHORITATIVE SOURCE", (-10.5, -0.4, 20.0), 0.82, white, review_collection)
    add_text(bpy, "UNCHANGED CONCEPT UV WINDOW", (-10.5, -0.4, 18.9), 0.44, muted, review_collection)
    add_text(bpy, "A08 BLENDER POMMEL CANDIDATE", (10.5, -6.0, 20.0), 0.78, white, review_collection)
    add_text(bpy, "18.0 CM H  /  11.0 CM W", (10.5, -6.0, 18.9), 0.48, muted, review_collection)
    add_text(bpy, "DEPTH + REAR: CANDIDATE INTERPRETATION", (10.5, -6.0, -0.9), 0.42, muted, review_collection)

    separator = add_cylinder(bpy, "Review_Separator", 0.035, 22.0, 10.0, muted, review_collection, 8)
    separator.rotation_euler[0] = 0.0

    configure_camera(bpy, review_collection)
    add_area_light(bpy, "A08_Key", (6.0, -18.0, 20.0), 1050.0, 8.0, review_collection, (10.5, 0.0, 9.0))
    add_area_light(bpy, "A08_Fill", (18.0, -8.0, 8.0), 650.0, 7.0, review_collection, (10.5, 0.0, 9.0))
    add_area_light(bpy, "A08_Rim", (9.0, 5.0, 17.0), 900.0, 6.0, review_collection, (10.5, 0.0, 10.0))

    if scene.world is None:
        scene.world = bpy.data.worlds.new("A08_Review_World")
    scene.world.color = (0.008, 0.010, 0.015)
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 3.0
    scene.eevee.gtao_factor = 1.25
    scene.eevee.use_bloom = True
    scene.eevee.bloom_intensity = 0.05
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0

    bounds = candidate_bounds(candidate_objects)
    width_pass = abs(bounds["extent_cm"][0] - 11.0) <= 0.001
    height_pass = abs(bounds["extent_cm"][2] - 18.0) <= 0.001
    origin_pass = abs(bounds["minimum_cm"][2]) <= 0.001
    if not (width_pass and height_pass and origin_pass):
        raise RuntimeError(f"numeric gate failed: {bounds}")

    blend_path = ROOT / BLEND_REL
    review_path = ROOT / REVIEW_REL
    manifest_path = ROOT / MANIFEST_REL
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    scene.render.filepath = str(review_path)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    bpy.ops.render.render(write_still=True)

    manifest = {
        "schema": "aerathea.siegebreaker_a08_pommel_candidate.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT_ID,
        "date": "2026-07-22",
        "status": "candidate_pending_flamestrike_visual_decision",
        "artifact_status": "candidate",
        "software_boundary": {
            "visual_and_geometry_software": "Blender 3.0.1",
            "trellis_used": False,
            "triposr_used": False,
            "generative_image_or_image_to_3d_used": False,
            "historical_geometry_inputs": 0,
        },
        "authority_hashes": authority_hashes,
        "source": {
            "path": str(SOURCE_REL),
            "sha256": SOURCE_SHA256,
            "dimensions_px": [1122, 1402],
            "mutated": False,
            "role": "authoritative visual target",
        },
        "numeric_gate": {
            "required_height_cm": 18.0,
            "required_max_width_cm": 11.0,
            "required_minimum_z_cm": 0.0,
            "measured_local_bounds": bounds,
            "height_pass": height_pass,
            "width_pass": width_pass,
            "origin_pass": origin_pass,
        },
        "visible_groups": {
            "faceted_body": True,
            "upper_and_lower_collars": True,
            "layered_front_diamond": True,
            "forged_bracing": True,
            "restrained_blue_rune": True,
        },
        "interpretation_boundary": {
            "depth": "candidate interpretation",
            "rear_continuation": "unresolved",
            "internal_attachment": "unresolved",
            "approved_hidden_surface_authority": False,
        },
        "mesh_signature_sha256": mesh_signature(candidate_objects),
        "outputs": {
            "blend": {"path": str(BLEND_REL), "sha256": sha256_file(blend_path)},
            "review": {"path": str(REVIEW_REL), "sha256": sha256_file(review_path)},
            "script": {"path": str(SCRIPT_REL), "sha256": sha256_file(ROOT / SCRIPT_REL)},
        },
        "unreal_outputs": 0,
        "fully_game_ready": False,
        "next_decision": "Flamestrike approve, revise, reject, or block the isolated pommel visual candidate",
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
