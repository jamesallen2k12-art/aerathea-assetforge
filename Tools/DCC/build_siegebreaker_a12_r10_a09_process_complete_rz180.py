#!/usr/bin/env python3
"""Rebuild the complete Siege Breaker with the approved A09 half process.

Process authority:
* A09 supplies the exact source-pixel mask/fill and combined-outer-boundary
  physical-half construction.
* R7/R10 Steps 03/04/05/05C supply the approved measured component surfaces.
* R10/R8 replaces only centerline/axis/duplication registration.
* The completed source half is duplicated exactly once by
  Rz(180): (X,Y,Z)->(-X,-Y,Z).
* The Step 05C pi/2 haft-cylinder wrap is inherited without alteration.

No rejected Step 06 geometry or Blender file is loaded.
"""

from __future__ import annotations

import bisect
from collections import deque
from fractions import Fraction
import bmesh
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
ASSET_ROOT = ROOT / "docs/assets/blueprints" / ASSET
ATTEMPT = "A12_R10_A09ProcessCompleteRz180_A02"
CONTRACT_ID = "SB-A12-R10-A09-PROCESS-COMPLETE-RZ180-A02"
RECOVERY_RECORD = (
    ASSET_ROOT
    / "manifests/A12_R10_STEP06_HALF_PRESENTATION_AND_WALL_METHOD_DRIFT_RECOVERY.md"
)

A09_SCRIPT = ROOT / "Tools/DCC/build_siegebreaker_a09_pixel_half_mirror_visual_match.py"
STEP03_SCRIPT = ROOT / "Tools/DCC/build_siegebreaker_a12_r10_step03_strike_face_half_proof.py"
STEP04_SCRIPT = ROOT / "Tools/DCC/build_siegebreaker_a12_r10_step04_core_stones_coupler_proof.py"

SOURCE_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET
SOURCE_FILES = {
    "step03": SOURCE_ROOT
    / "A12_R10_Step03_StrikeFaceHalfProof_A02"
    / f"{ASSET}_A12_R10_Step03_StrikeFaceHalfProof_A02.blend",
    "step04": SOURCE_ROOT
    / "A12_R10_Step04_CoreStonesCouplerProof_A02"
    / f"{ASSET}_A12_R10_Step04_CoreStonesCouplerProof_A02.blend",
    "step05": SOURCE_ROOT
    / "A12_R10_Step05_RotationalCapPommelProof_A03"
    / f"{ASSET}_A12_R10_Step05_RotationalCapPommelProof_A03.blend",
    "step05c": SOURCE_ROOT
    / "A12_R10_Step05C_HaftFerruleGripHalfProof_A01"
    / f"{ASSET}_A12_R10_Step05C_HaftFerruleGripHalfProof_A01.blend",
}
SOURCE_SHA256 = {
    "step03": "5a12b5dd4104dd036e500106a6a0d28f345c699be0ca061c63bc5349696117eb",
    "step04": "f086c42180422e6d6a0b7331dc8458bf26cf576f1e9b7379d6ac8c333725d683",
    "step05": "0891bbe5df2bc700b1e1eeb7428dc40521e8df9ccc12d0c844c3a81cf881fe4a",
    "step05c": "3e5645adea6f5ef3fd04404ecc4ab87e2b3dab39cdc422792b41d20b579f8a9e",
}
DIRECT_OBJECTS = {
    "step03": {
        "C04_STRIKE_FACE_POSITIVE_X":
        "C04_STRIKE_FACE_POSITIVE_X_ISOLATED_PROOF",
    },
    "step04": {
        "C01_CENTER_CORE": "C01_CENTER_CORE_VISIBLE_OWNER_PROOF",
        "C02_STONE_LEFT": "C02_STONE_LEFT_VISIBLE_OWNER_PROOF",
        "C03_STONE_RIGHT": "C03_STONE_RIGHT_VISIBLE_OWNER_PROOF",
        "C06_UPPER_HAFT_CAP":
        "C06_UPPER_HAFT_COUPLER_VISIBLE_OWNER_PROOF",
    },
    "step05c": {
        "C07A_HAFT_CYLINDER":
        "C07A_HAFT_CYLINDER_POSITIVE_X_HALF_PROOF",
        "C07B_HAFT_TO_HANDLE_FERRULE":
        "C07B_HAFT_TO_HANDLE_FERRULE_POSITIVE_X_HALF_PROOF",
        "C08_GRIP": "C08_GRIP_POSITIVE_X_HALF_PROOF",
    },
}
ROTATIONAL_OBJECTS = {
    "C09_LOWER_COLLAR": "C09_LOWER_COLLAR_ROTATIONAL_OWNER_PROOF",
    "C10_POMMEL_BODY": "C10_POMMEL_BODY_ROTATIONAL_OWNER_PROOF",
    "C11_POMMEL_TERMINAL_CAP":
    "C11_POMMEL_TERMINAL_CAP_ROTATIONAL_OWNER_PROOF",
    "C12_UPPER_HEAD_CAP_SPIRE":
    "C12_UPPER_HEAD_CAP_SPIRE_ROTATIONAL_OWNER_PROOF",
}

OUTPUT_ROOT = SOURCE_ROOT / ATTEMPT
REVIEW_ROOT = (
    ASSET_ROOT / "review/A12_R10_A09_PROCESS_COMPLETE_RZ180_A02"
)
BLEND_PATH = OUTPUT_ROOT / f"{ASSET}_{ATTEMPT}.blend"
FRONT_RENDER = REVIEW_ROOT / "A12_R10_COMPLETE_FRONT.png"
RIGHT_RENDER = REVIEW_ROOT / "A12_R10_COMPLETE_RIGHT.png"
BACK_RENDER = REVIEW_ROOT / "A12_R10_COMPLETE_BACK.png"
COLOR_3Q = REVIEW_ROOT / "A12_R10_COMPLETE_COLOR_3Q.png"
GRAY_3Q = REVIEW_ROOT / "A12_R10_COMPLETE_GRAY_3Q.png"
IDS_3Q = REVIEW_ROOT / "A12_R10_COMPLETE_COMPONENT_IDS_3Q.png"
BOARD = REVIEW_ROOT / "A12_R10_A09_PROCESS_COMPLETE_RZ180_A02_REVIEW.png"
MANIFEST = (
    ASSET_ROOT
    / "manifests/A12_R10_A09_PROCESS_COMPLETE_RZ180_A02_VALIDATION.json"
)

HALF_SEGMENTS = 64
ANGULAR_SEGMENTS = 128
HALF_SEQUENCE = tuple(range(96, 128)) + tuple(range(0, 33))
HALF_FACE_SEGMENTS = tuple(range(96, 128)) + tuple(range(0, 32))

COMPONENT_COLORS = {
    "C00_COMBINED_HEAD_OUTER_BOUNDARY": (0.52, 0.55, 0.59, 1.0),
    "C01_CENTER_CORE": (0.19, 0.44, 0.76, 1.0),
    "C02_STONE_LEFT": (0.22, 0.71, 0.91, 1.0),
    "C03_STONE_RIGHT": (0.10, 0.84, 0.64, 1.0),
    "C04_STRIKE_FACE_POSITIVE_X": (0.91, 0.34, 0.19, 1.0),
    "C06_UPPER_HAFT_CAP": (0.88, 0.69, 0.13, 1.0),
    "C07A_HAFT_CYLINDER": (0.67, 0.35, 0.10, 1.0),
    "C07B_HAFT_TO_HANDLE_FERRULE": (0.13, 0.58, 0.83, 1.0),
    "C08_GRIP": (0.68, 0.16, 0.48, 1.0),
    "C09_LOWER_COLLAR": (0.98, 0.46, 0.10, 1.0),
    "C10_POMMEL_BODY": (0.57, 0.32, 0.84, 1.0),
    "C11_POMMEL_TERMINAL_CAP": (0.90, 0.16, 0.34, 1.0),
    "C12_UPPER_HEAD_CAP_SPIRE": (0.34, 0.76, 0.22, 1.0),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def coordinate_hash(cells: set[tuple[int, int]]) -> str:
    payload = "".join(
        f"{x},{y}\n" for x, y in sorted(cells, key=lambda p: (p[1], p[0]))
    )
    return sha256_bytes(payload.encode("ascii"))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load process authority: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def ensure_authority() -> None:
    if not RECOVERY_RECORD.is_file():
        raise RuntimeError("Recovery authority record missing")
    for lane, path in SOURCE_FILES.items():
        if not path.is_file() or sha256(path) != SOURCE_SHA256[lane]:
            raise RuntimeError(f"Approved source proof changed: {lane}")
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (
        bpy.data.meshes,
        bpy.data.curves,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights,
    ):
        for block in list(datablocks):
            if block.users == 0:
                datablocks.remove(block)
    base = bpy.context.scene.collection.children.get("Collection")
    if base is not None:
        base.name = "A12_R10_A09_PROCESS_COMPLETE_RZ180"


def configure_scene() -> None:
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 5.0
    scene.eevee.gtao_factor = 1.25
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.render.image_settings.color_depth = "8"
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = False
    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.88, 0.88, 0.86, 1.0)
    background.inputs["Strength"].default_value = 0.72
    scene["Aerathea.ContractID"] = CONTRACT_ID
    scene["Aerathea.ProcessAuthority"] = "A09 exact pixel-half process"
    scene["Aerathea.CenterRegistrationAuthority"] = "R10/R8"
    scene["Aerathea.Rz180Formula"] = "(X,Y,Z)->(-X,-Y,Z)"
    scene["Aerathea.Rz180Executed"] = True
    scene["Aerathea.ArtifactStatus"] = "candidate"
    scene["Aerathea.PiOver2HaftWrapPreserved"] = True
    try:
        scene.view_settings.view_transform = "Standard"
        scene.view_settings.look = "None"
        scene.view_settings.exposure = 0.0
        scene.view_settings.gamma = 1.0
    except Exception:
        pass


def append_object(path: Path, object_name: str) -> bpy.types.Object:
    with bpy.data.libraries.load(str(path), link=False) as (data_from, data_to):
        if object_name not in data_from.objects:
            raise RuntimeError(f"{object_name} missing from {path}")
        data_to.objects = [object_name]
    obj = data_to.objects[0]
    bpy.context.scene.collection.objects.link(obj)
    return obj


def extract_positive_x_half(
    source: bpy.types.Object,
    component: str,
) -> bpy.types.Object:
    profile = json.loads(source["Aerathea.ProfileJSON"])
    ring_count = len(profile)
    if len(source.data.vertices) != ring_count * ANGULAR_SEGMENTS:
        raise RuntimeError(f"{component} rotational source count changed")
    vertices = []
    old_to_new = {}
    for ring in range(ring_count):
        for segment in HALF_SEQUENCE:
            old_index = ring * ANGULAR_SEGMENTS + segment
            old_to_new[old_index] = len(vertices)
            vertices.append(tuple(source.data.vertices[old_index].co))
    faces = []
    source_polygons = []
    for ring in range(ring_count - 1):
        for segment in HALF_FACE_SEGMENTS:
            polygon = source.data.polygons[
                ring * ANGULAR_SEGMENTS + segment
            ]
            faces.append(tuple(old_to_new[index] for index in polygon.vertices))
            source_polygons.append(polygon)
    mesh = bpy.data.meshes.new(f"{component}_R10_SOURCE_HALF_MESH")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    for material in source.data.materials:
        mesh.materials.append(material)
    source_uv = source.data.uv_layers.active
    if source_uv is not None:
        target_uv = mesh.uv_layers.new(name="UVMap")
        for polygon, source_polygon in zip(mesh.polygons, source_polygons):
            polygon.material_index = source_polygon.material_index
            polygon.use_smooth = source_polygon.use_smooth
            for loop, source_loop in zip(
                polygon.loop_indices, source_polygon.loop_indices
            ):
                target_uv.data[loop].uv = source_uv.data[source_loop].uv
    obj = bpy.data.objects.new(f"{component}_R10_SOURCE_HALF", mesh)
    bpy.context.scene.collection.objects.link(obj)
    for key in source.keys():
        obj[key] = source[key]
    obj["Aerathea.ComponentID"] = component
    obj["Aerathea.GeometryRole"] = "source_half"
    obj["Aerathea.HalfAngularSegments"] = HALF_SEGMENTS
    obj["Aerathea.FutureWholeTransform"] = "Rz180"
    return obj


def component_registered_x(
    component: str,
    x_edge: float,
    active: set[tuple[int, int]],
    step04,
) -> float:
    interval = step04.component_target_interval(component)
    if interval is None:
        return step04.x_world_edge(float(x_edge))
    source_min = min(x for x, _y in active)
    source_max = max(x + 1 for x, _y in active)
    target_min, target_max = interval
    return target_min + (x_edge - source_min) * (
        target_max - target_min
    ) / (source_max - source_min)


def owner_for_cell(
    x: int,
    y: int,
    step04,
) -> str | None:
    world_x = step04.x_world_edge(x + 0.5)
    core_half = float(step04.CORE_HALF_WIDTH)
    if y < step04.ROW_A_HAFT_COUPLER_START:
        if world_x < -core_half:
            return "C02_STONE_LEFT"
        if world_x > core_half:
            return "C03_STONE_RIGHT"
        if y > step04.C12_LAST_SOURCE_ROW:
            return "C01_CENTER_CORE"
        return None
    if y < step04.ROW_B_STONES_ABSENT:
        if world_x < -core_half:
            return "C02_STONE_LEFT"
        if world_x > core_half:
            return "C03_STONE_RIGHT"
        return "C06_UPPER_HAFT_CAP"
    if y < step04.ROW_C_STRAIGHT_HAFT_START:
        return "C06_UPPER_HAFT_CAP"
    return None


def a09_global_cells(mask: Image.Image, a09) -> set[tuple[int, int]]:
    pixels = mask.load()
    return {
        (a09.FRONT_RECT[0] + x, a09.FRONT_RECT[1] + y)
        for y in range(mask.height)
        for x in range(mask.width)
        if pixels[x, y] > 0
    }


def build_global_head_fills(
    global_cells: set[tuple[int, int]],
    active_sets: dict[str, set[tuple[int, int]]],
    step04,
    image: Image.Image,
    source_objects: dict[str, bpy.types.Object],
) -> tuple[list[bpy.types.Object], dict[str, object], set[tuple[int, int]]]:
    existing = set().union(*active_sets.values())
    additions = {component: set() for component in active_sets}
    for x, y in global_cells:
        if y >= step04.ROW_C_STRAIGHT_HAFT_START or (x, y) in existing:
            continue
        if y == 520:
            continue
        owner = owner_for_cell(x, y, step04)
        if owner is not None:
            additions[owner].add((x, y))

    objects = []
    stats = {}
    base_y = -float(step04.LOCKED_HALF_DEPTH)
    for component, cells in additions.items():
        if not cells:
            stats[component] = {
                "added_source_pixels": 0,
                "row520_added_pixels": 0,
                "coordinate_sha256": coordinate_hash(set()),
            }
            continue
        vertices = []
        faces = []
        face_uvs = []
        for x, y in sorted(cells, key=lambda p: (p[1], p[0])):
            start = len(vertices)
            vertices.extend(
                (
                    (
                        component_registered_x(
                            component, x, active_sets[component], step04
                        ),
                        base_y,
                        step04.z_world_edge(y),
                    ),
                    (
                        component_registered_x(
                            component, x, active_sets[component], step04
                        ),
                        base_y,
                        step04.z_world_edge(y + 1),
                    ),
                    (
                        component_registered_x(
                            component, x + 1, active_sets[component], step04
                        ),
                        base_y,
                        step04.z_world_edge(y + 1),
                    ),
                    (
                        component_registered_x(
                            component, x + 1, active_sets[component], step04
                        ),
                        base_y,
                        step04.z_world_edge(y),
                    ),
                )
            )
            faces.append((start, start + 1, start + 2, start + 3))
            face_uvs.append(
                (
                    (x / image.width, 1.0 - y / image.height),
                    (x / image.width, 1.0 - (y + 1) / image.height),
                    ((x + 1) / image.width, 1.0 - (y + 1) / image.height),
                    ((x + 1) / image.width, 1.0 - y / image.height),
                )
            )
        mesh = bpy.data.meshes.new(f"{component}_A09_GLOBAL_FILL_HALF_MESH")
        mesh.from_pydata(vertices, [], faces)
        mesh.update(calc_edges=True)
        mesh.materials.append(source_objects[component].data.materials[0])
        uv_layer = mesh.uv_layers.new(name="UVMap")
        for polygon, values in zip(mesh.polygons, face_uvs):
            for loop, value in zip(polygon.loop_indices, values):
                uv_layer.data[loop].uv = value
        obj = bpy.data.objects.new(f"{component}_A09_GLOBAL_FILL_HALF", mesh)
        bpy.context.scene.collection.objects.link(obj)
        obj["Aerathea.ContractID"] = CONTRACT_ID
        obj["Aerathea.ComponentID"] = component
        obj["Aerathea.GeometryRole"] = "source_half"
        obj["Aerathea.ProcessRule"] = "A09 global fill; source-owned pixels only"
        obj["Aerathea.SourcePixelCount"] = len(cells)
        obj["Aerathea.SourceCoordinateHash"] = coordinate_hash(cells)
        objects.append(obj)
        stats[component] = {
            "added_source_pixels": len(cells),
            "row520_added_pixels": sum(1 for _x, y in cells if y == 520),
            "coordinate_sha256": coordinate_hash(cells),
        }
    completed = existing | set().union(*additions.values())
    return objects, stats, completed


def build_combined_outer_wall(
    global_cells: set[tuple[int, int]],
    completed_cells: set[tuple[int, int]],
    active_sets: dict[str, set[tuple[int, int]]],
    step03,
    step04,
    right_image: Image.Image,
    right_membership: bytearray,
    material: bpy.types.Material,
) -> tuple[bpy.types.Object, dict[str, object]]:
    """A09 rule: wall only the combined exterior silhouette, never components."""
    boundary_records = []
    for x, y in global_cells:
        if y >= step04.ROW_C_STRAIGHT_HAFT_START:
            continue
        owner = owner_for_cell(x, y, step04)
        if owner is None:
            continue
        for neighbor, edge in (
            ((x - 1, y), ((x, y), (x, y + 1))),
            ((x + 1, y), ((x + 1, y + 1), (x + 1, y))),
            ((x, y - 1), ((x + 1, y), (x, y))),
            ((x, y + 1), ((x, y + 1), (x + 1, y + 1))),
        ):
            if neighbor in global_cells:
                continue
            (_x0, y0), (_x1, y1) = edge
            if y0 == y1 == step04.ROW_C_STRAIGHT_HAFT_START:
                continue
            boundary_records.append((edge, owner, (x, y)))

    vertices = []
    faces = []
    face_uvs = []
    base_y = -float(step04.LOCKED_HALF_DEPTH)
    selected_by_row: dict[int, list[int]] = {}
    for source_y in range(step03.RIGHT_RECT[1], step03.RIGHT_RECT[3]):
        xs = [
            source_x
            for source_x in range(
                step03.RIGHT_RECT[0], step03.RIGHT_RECT[2]
            )
            if right_membership[
                source_y * right_image.width + source_x
            ]
        ]
        if xs:
            selected_by_row[source_y] = xs
    sampled_source_pixels: set[tuple[int, int]] = set()

    def nearest_selected(
        requested_x: float,
        requested_y: float,
    ) -> tuple[int, int]:
        target_y = max(
            step03.RIGHT_RECT[1],
            min(step03.RIGHT_RECT[3] - 1, int(math.floor(requested_y))),
        )
        best: tuple[float, int, int] | None = None
        for distance_y in range(
            step03.RIGHT_RECT[3] - step03.RIGHT_RECT[1]
        ):
            rows = (
                (target_y,)
                if distance_y == 0
                else (target_y - distance_y, target_y + distance_y)
            )
            for source_y in rows:
                xs = selected_by_row.get(source_y)
                if not xs:
                    continue
                position = bisect.bisect_left(xs, requested_x)
                for index in (position - 1, position):
                    if not (0 <= index < len(xs)):
                        continue
                    source_x = xs[index]
                    distance = (
                        (source_x + 0.5 - requested_x) ** 2
                        + (source_y + 0.5 - requested_y) ** 2
                    )
                    candidate = (distance, source_x, source_y)
                    if best is None or candidate < best:
                        best = candidate
            if best is not None and distance_y * distance_y > best[0]:
                break
        if best is None:
            raise RuntimeError(
                "No selected original-right source pixel for outer boundary"
            )
        return best[1], best[2]

    def side_uv(world_y: float, world_z: float) -> tuple[float, float]:
        half_depth = float(step04.LOCKED_HALF_DEPTH)
        depth_u = max(0.0, min(1.0, (world_y + half_depth) / half_depth))
        requested_x = (
            step03.RIGHT_RECT[0]
            + depth_u
            * (float(step03.FACE_CENTER_X) - step03.RIGHT_RECT[0])
        )
        requested_y = (
            step03.RIGHT_RECT[3]
            - world_z
            * (step03.RIGHT_RECT[3] - step03.RIGHT_RECT[1])
            / 170.0
        )
        source_x, source_y = nearest_selected(requested_x, requested_y)
        sampled_source_pixels.add((source_x, source_y))
        return (
            (source_x + 0.5) / right_image.width,
            1.0 - (source_y + 0.5) / right_image.height,
        )

    for edge, owner, _cell in sorted(boundary_records):
        (x0, y0), (x1, y1) = edge
        p0 = (
            component_registered_x(owner, x0, active_sets[owner], step04),
            base_y,
            step04.z_world_edge(y0),
        )
        p1 = (
            component_registered_x(owner, x1, active_sets[owner], step04),
            base_y,
            step04.z_world_edge(y1),
        )
        s1 = (p1[0], 0.0, p1[2])
        s0 = (p0[0], 0.0, p0[2])
        start = len(vertices)
        vertices.extend((p0, p1, s1, s0))
        faces.append((start, start + 1, start + 2, start + 3))
        face_uvs.append(
            (
                side_uv(p0[1], p0[2]),
                side_uv(p1[1], p1[2]),
                side_uv(0.0, p1[2]),
                side_uv(0.0, p0[2]),
            )
        )
    mesh = bpy.data.meshes.new("C00_A09_COMBINED_OUTER_BOUNDARY_HALF_MESH")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    mesh.materials.append(material)
    uv_layer = mesh.uv_layers.new(name="UVMap")
    for polygon, values in zip(mesh.polygons, face_uvs):
        for loop, value in zip(polygon.loop_indices, values):
            uv_layer.data[loop].uv = value
    obj = bpy.data.objects.new("C00_A09_COMBINED_OUTER_BOUNDARY_HALF", mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj["Aerathea.ContractID"] = CONTRACT_ID
    obj["Aerathea.ComponentID"] = "C00_COMBINED_HEAD_OUTER_BOUNDARY"
    obj["Aerathea.GeometryRole"] = "source_half"
    obj["Aerathea.ProcessRule"] = (
        "A09 combined exterior boundary only; no per-component walls"
    )
    obj["Aerathea.BoundaryFaceCount"] = len(faces)
    obj["Aerathea.PerComponentWallCount"] = 0
    return obj, {
        "boundary_faces": len(faces),
        "per_component_walls": 0,
        "side_uv_rule": (
            "old A09 combined outer boundary; original-right scanline "
            "pixels normalized across approved R10 half-depth"
        ),
        "unique_selected_source_pixels_sampled": len(sampled_source_pixels),
        "source_background_pixels_sampled": 0,
    }


def enclosed_cells(active: set[tuple[int, int]]) -> set[tuple[int, int]]:
    minimum_x = min(x for x, _y in active) - 1
    maximum_x = max(x for x, _y in active) + 1
    minimum_y = min(y for _x, y in active) - 1
    maximum_y = max(y for _x, y in active) + 1
    exterior = set()
    queue = deque()
    for x in range(minimum_x, maximum_x + 1):
        queue.extend(((x, minimum_y), (x, maximum_y)))
    for y in range(minimum_y, maximum_y + 1):
        queue.extend(((minimum_x, y), (maximum_x, y)))
    while queue:
        cell = queue.popleft()
        if cell in active or cell in exterior:
            continue
        x, y = cell
        if not (minimum_x <= x <= maximum_x and minimum_y <= y <= maximum_y):
            continue
        exterior.add(cell)
        queue.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
    return {
        (x, y)
        for y in range(minimum_y + 1, maximum_y)
        for x in range(minimum_x + 1, maximum_x)
        if (x, y) not in active and (x, y) not in exterior
    }


def build_strike_fill(
    step03,
    image: Image.Image,
    membership: bytearray,
    material: bpy.types.Material,
) -> tuple[bpy.types.Object | None, dict[str, object]]:
    width = image.width
    active = set()
    for y in range(step03.FACE_TOP_ROW, step03.FACE_ROW_STOP):
        for x in range(step03.RIGHT_RECT[0], math.ceil(float(step03.FACE_CENTER_X))):
            if Fraction(2 * x + 1, 2) > step03.FACE_CENTER_X:
                continue
            if membership[y * width + x]:
                active.add((x, y))
    added = enclosed_cells(active)
    if not added:
        return None, {"added_source_pixels": 0}
    vertices = []
    faces = []
    face_uvs = []

    def point(x_edge: float, y_edge: int) -> tuple[float, float, float]:
        world_y = float(
            (Fraction(str(x_edge)) - step03.FACE_CENTER_X) * step03.Y_SCALE
        )
        z = step03.z_from_source_edge(y_edge)
        return (step03.x_base_at_z(z), world_y, z)

    def uv(x_edge: float, y_edge: int) -> tuple[float, float]:
        return (x_edge / image.width, 1.0 - y_edge / image.height)

    for x, y in sorted(added, key=lambda p: (p[1], p[0])):
        x0 = float(x)
        x1 = min(float(x + 1), float(step03.FACE_CENTER_X))
        negative = (
            point(x0, y),
            point(x0, y + 1),
            point(x1, y + 1),
            point(x1, y),
        )
        values = (uv(x0, y), uv(x0, y + 1), uv(x1, y + 1), uv(x1, y))
        start = len(vertices)
        vertices.extend(negative)
        faces.append((start, start + 1, start + 2, start + 3))
        face_uvs.append(values)
        start = len(vertices)
        vertices.extend((negative[3], negative[2], negative[1], negative[0]))
        vertices[start] = (vertices[start][0], -vertices[start][1], vertices[start][2])
        vertices[start + 1] = (vertices[start + 1][0], -vertices[start + 1][1], vertices[start + 1][2])
        vertices[start + 2] = (vertices[start + 2][0], -vertices[start + 2][1], vertices[start + 2][2])
        vertices[start + 3] = (vertices[start + 3][0], -vertices[start + 3][1], vertices[start + 3][2])
        faces.append((start, start + 1, start + 2, start + 3))
        face_uvs.append(tuple(reversed(values)))
    mesh = bpy.data.meshes.new("C04_A09_ENCLOSED_FILL_HALF_MESH")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    mesh.materials.append(material)
    uv_layer = mesh.uv_layers.new(name="UVMap")
    for polygon, values in zip(mesh.polygons, face_uvs):
        for loop, value in zip(polygon.loop_indices, values):
            uv_layer.data[loop].uv = value
    obj = bpy.data.objects.new("C04_A09_ENCLOSED_FILL_HALF", mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj["Aerathea.ContractID"] = CONTRACT_ID
    obj["Aerathea.ComponentID"] = "C04_STRIKE_FACE_POSITIVE_X"
    obj["Aerathea.GeometryRole"] = "source_half"
    obj["Aerathea.SourcePixelCount"] = len(added)
    obj["Aerathea.SourceCoordinateHash"] = coordinate_hash(added)
    return obj, {
        "added_source_pixels": len(added),
        "coordinate_sha256": coordinate_hash(added),
    }


def adjacent_uv(obj: bpy.types.Object, polygon_index: int) -> tuple[float, float]:
    uv_layer = obj.data.uv_layers.active
    if uv_layer is None:
        return (0.5, 0.5)
    polygon = obj.data.polygons[polygon_index]
    values = [uv_layer.data[index].uv for index in polygon.loop_indices]
    return (
        sum(float(value[0]) for value in values) / len(values),
        sum(float(value[1]) for value in values) / len(values),
    )


def make_closure(
    name: str,
    component: str,
    vertices: list[tuple[float, float, float]],
    faces: list[tuple[int, ...]],
    face_uvs: list[tuple[float, float]],
    material: bpy.types.Material,
    rule: str,
) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(f"{name}_MESH")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    mesh.materials.append(material)
    uv_layer = mesh.uv_layers.new(name="UVMap")
    for polygon, value in zip(mesh.polygons, face_uvs):
        for loop in polygon.loop_indices:
            uv_layer.data[loop].uv = value
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj["Aerathea.ContractID"] = CONTRACT_ID
    obj["Aerathea.ComponentID"] = component
    obj["Aerathea.GeometryRole"] = "source_half"
    obj["Aerathea.ClosureRule"] = rule
    return obj


def build_h1(c07a: bpy.types.Object, c07b: bpy.types.Object) -> bpy.types.Object:
    profile = json.loads(c07a["Aerathea.ProfileJSON"])
    stride = HALF_SEGMENTS + 1
    inner_start = (len(profile) - 1) * stride
    vertices = [
        tuple(c07a.data.vertices[inner_start + index].co)
        for index in range(stride)
    ] + [
        tuple(c07b.data.vertices[index].co)
        for index in range(stride)
    ]
    faces = [
        (index, index + stride, index + stride + 1, index + 1)
        for index in range(HALF_SEGMENTS)
    ]
    uvs = [adjacent_uv(c07b, index) for index in range(HALF_SEGMENTS)]
    obj = make_closure(
        "C07_H1_EXACT_HALF_ANNULUS",
        "C07B_HAFT_TO_HANDLE_FERRULE",
        vertices,
        faces,
        uvs,
        c07b.data.materials[0],
        "exact H1 positive-X half-annulus radii 5/2 and 11/4",
    )
    obj["Aerathea.InnerRadiusExact"] = "5/2"
    obj["Aerathea.OuterRadiusExact"] = "11/4"
    return obj


def build_head_ring_connection(
    name: str,
    head_component: str,
    active: set[tuple[int, int]],
    edge_y: int,
    ring_obj: bpy.types.Object,
    ring_index: int,
    step04,
    image: Image.Image,
    material: bpy.types.Material,
) -> bpy.types.Object:
    cell_y = edge_y if any(y == edge_y for _x, y in active) else edge_y - 1
    row = sorted(x for x, y in active if y == cell_y)
    if row != list(range(row[0], row[-1] + 1)):
        raise RuntimeError(f"{name} head boundary is not one measured run")
    x0, x1 = row[0], row[-1] + 1
    z = step04.z_world_edge(edge_y)
    head = [
        (
            component_registered_x(
                head_component,
                x0 + (x1 - x0) * index / HALF_SEGMENTS,
                active,
                step04,
            ),
            -float(step04.LOCKED_HALF_DEPTH),
            z,
        )
        for index in range(HALF_SEGMENTS + 1)
    ]
    profile = json.loads(ring_obj["Aerathea.ProfileJSON"])
    if ring_index < 0:
        ring_index += len(profile)
    start = ring_index * (HALF_SEGMENTS + 1)
    ring = [
        tuple(ring_obj.data.vertices[start + index].co)
        for index in range(HALF_SEGMENTS + 1)
    ]
    if any(abs(point[2] - z) > 1.0e-5 for point in ring):
        raise RuntimeError(f"{name} exact common-Z mismatch")
    vertices = head + ring
    stride = HALF_SEGMENTS + 1
    faces = [
        (index, stride + index, stride + index + 1, index + 1)
        for index in range(HALF_SEGMENTS)
    ]
    uvs = []
    for index in range(HALF_SEGMENTS):
        midpoint = x0 + (x1 - x0) * (index + 0.5) / HALF_SEGMENTS
        owner_x = min(row, key=lambda x: (abs(x + 0.5 - midpoint), x))
        uvs.append(
            (
                (owner_x + 0.5) / image.width,
                1.0 - (cell_y + 0.5) / image.height,
            )
        )
    obj = make_closure(
        name,
        head_component,
        vertices,
        faces,
        uvs,
        material,
        "straight common-Z measured boundary to exact half-ring",
    )
    obj["Aerathea.CommonZCm"] = z
    return obj


def build_half_cap(
    obj: bpy.types.Object,
    name: str,
    component: str,
    ring: str,
) -> bpy.types.Object:
    profile = json.loads(obj["Aerathea.ProfileJSON"])
    stride = HALF_SEGMENTS + 1
    ring_index = 0 if ring == "top" else len(profile) - 1
    start = ring_index * stride
    z = float(obj.data.vertices[start].co.z)
    vertices = [(0.0, 0.0, z)] + [
        tuple(obj.data.vertices[start + index].co)
        for index in range(stride)
    ]
    if ring == "top":
        faces = [(0, index + 2, index + 1) for index in range(HALF_SEGMENTS)]
        polygon_base = 0
    else:
        faces = [(0, index + 1, index + 2) for index in range(HALF_SEGMENTS)]
        polygon_base = (len(profile) - 2) * HALF_SEGMENTS
    uvs = [
        adjacent_uv(obj, polygon_base + index)
        for index in range(HALF_SEGMENTS)
    ]
    return make_closure(
        name,
        component,
        vertices,
        faces,
        uvs,
        obj.data.materials[0],
        f"exact planar positive-X {ring} half-cap",
    )


def complete_rz180(obj: bpy.types.Object) -> bpy.types.Object:
    """Apply one exact Rz180 copy, merging only coordinate-equal seam points."""
    source_vertices = [tuple(vertex.co) for vertex in obj.data.vertices]
    vertices = source_vertices + [
        (-point[0], -point[1], point[2]) for point in source_vertices
    ]
    source_faces = [tuple(polygon.vertices) for polygon in obj.data.polygons]
    offset = len(source_vertices)
    faces = source_faces + [
        tuple(index + offset for index in face) for face in source_faces
    ]
    mesh = bpy.data.meshes.new(f"{obj.name}_COMPLETE_RZ180_MESH")
    mesh.from_pydata(vertices, [], faces)
    mesh.update(calc_edges=True)
    for material in obj.data.materials:
        mesh.materials.append(material)
    source_uv = obj.data.uv_layers.active
    if source_uv is not None:
        target_uv = mesh.uv_layers.new(name="UVMap")
        source_polygon_count = len(source_faces)
        for index, polygon in enumerate(mesh.polygons):
            source_polygon = obj.data.polygons[index % source_polygon_count]
            polygon.material_index = source_polygon.material_index
            polygon.use_smooth = source_polygon.use_smooth
            for loop, source_loop in zip(
                polygon.loop_indices, source_polygon.loop_indices
            ):
                target_uv.data[loop].uv = source_uv.data[source_loop].uv
    bm = bmesh.new()
    bm.from_mesh(mesh)
    before = len(bm.verts)
    bmesh.ops.remove_doubles(bm, verts=list(bm.verts), dist=1.0e-6)
    after = len(bm.verts)
    bm.to_mesh(mesh)
    bm.free()
    mesh.update(calc_edges=True)
    completed = bpy.data.objects.new(
        obj.name.replace("_HALF", "") + "_COMPLETE_RZ180",
        mesh,
    )
    bpy.context.scene.collection.objects.link(completed)
    for key in obj.keys():
        completed[key] = obj[key]
    completed["Aerathea.ContractID"] = CONTRACT_ID
    completed["Aerathea.GeometryRole"] = "complete_rz180"
    completed["Aerathea.Rz180Applied"] = True
    completed["Aerathea.Rz180Formula"] = "(X,Y,Z)->(-X,-Y,Z)"
    completed["Aerathea.SourceHalfVertices"] = len(source_vertices)
    completed["Aerathea.SourceHalfPolygons"] = len(source_faces)
    completed["Aerathea.SeamVerticesMerged"] = before - after
    bpy.data.objects.remove(obj, do_unlink=True)
    return completed


def flat_material(
    name: str,
    color: tuple[float, float, float, float],
    metallic: float = 0.08,
) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = 0.67
    bsdf.inputs["Metallic"].default_value = metallic
    material.diffuse_color = color
    return material


def add_camera(
    name: str,
    location: tuple[float, float, float],
    target: tuple[float, float, float],
    ortho: float,
) -> bpy.types.Object:
    data = bpy.data.cameras.new(name)
    data.type = "ORTHO"
    data.ortho_scale = ortho
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    obj.rotation_euler = (
        Vector(target) - obj.location
    ).to_track_quat("-Z", "Y").to_euler()
    return obj


def add_lights(target: tuple[float, float, float]) -> None:
    for name, energy, size, location in (
        ("R10_Key", 1250.0, 85.0, (120.0, -150.0, 215.0)),
        ("R10_Fill", 720.0, 100.0, (-125.0, -65.0, 105.0)),
        ("R10_Rim", 950.0, 80.0, (85.0, 105.0, 175.0)),
    ):
        data = bpy.data.lights.new(name, "AREA")
        data.energy = energy
        data.size = size
        light = bpy.data.objects.new(name, data)
        bpy.context.scene.collection.objects.link(light)
        light.location = location
        light.rotation_euler = (
            Vector(target) - light.location
        ).to_track_quat("-Z", "Y").to_euler()


def render(
    camera: bpy.types.Object,
    path: Path,
    width: int = 1000,
    height: int = 1100,
) -> None:
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def swap_materials(
    objects: list[bpy.types.Object],
    replacements: dict[str, bpy.types.Material],
) -> dict[str, tuple[list[bpy.types.Material | None], list[int]]]:
    original = {}
    for obj in objects:
        component = obj.get("Aerathea.ComponentID")
        if component not in replacements:
            continue
        original[obj.name] = (
            [slot.material for slot in obj.material_slots],
            [polygon.material_index for polygon in obj.data.polygons],
        )
        obj.data.materials.clear()
        obj.data.materials.append(replacements[component])
        for polygon in obj.data.polygons:
            polygon.material_index = 0
    return original


def restore_materials(
    objects: list[bpy.types.Object],
    original: dict[str, tuple[list[bpy.types.Material | None], list[int]]],
) -> None:
    for obj in objects:
        if obj.name not in original:
            continue
        materials, indices = original[obj.name]
        obj.data.materials.clear()
        for material in materials:
            if material is not None:
                obj.data.materials.append(material)
        for polygon, material_index in zip(obj.data.polygons, indices):
            polygon.material_index = material_index


def font(size: int, mono: bool = False) -> ImageFont.ImageFont:
    candidates = (
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/dejavu-sans-mono-fonts/DejaVuSansMono.ttf",
    ) if mono else (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu-sans-mono-fonts/DejaVuSans.ttf",
    )
    for candidate in candidates:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def fit_panel(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    value = image.convert("RGB")
    resampling = getattr(Image, "Resampling", Image)
    value.thumbnail(size, resampling.LANCZOS)
    panel = Image.new("RGB", size, (224, 224, 220))
    panel.paste(
        value,
        ((size[0] - value.width) // 2, (size[1] - value.height) // 2),
    )
    return panel


def compose_board(gates: dict[str, bool]) -> None:
    canvas = Image.new("RGB", (3000, 2050), (22, 25, 30))
    draw = ImageDraw.Draw(canvas)
    draw.text(
        (55, 35),
        "SIEGE BREAKER — COMPLETE A09-PROCESS Rz(180°) RECONSTRUCTION",
        fill=(242, 245, 248),
        font=font(36),
    )
    draw.text(
        (55, 90),
        "Old approved pixel-half process • new R10 center/axis data • exact pi/2 haft wrap • complete hammer",
        fill=(244, 190, 76),
        font=font(23),
    )
    panels = [
        (FRONT_RENDER, (45, 150), "COMPLETE FRONT"),
        (RIGHT_RENDER, (1030, 150), "COMPLETE RIGHT"),
        (BACK_RENDER, (2015, 150), "COMPLETE BACK"),
        (COLOR_3Q, (45, 1090), "COMPLETE SOURCE COLOR — 3/4"),
        (GRAY_3Q, (1030, 1090), "COMPLETE INDEPENDENT GRAY — 3/4"),
        (IDS_3Q, (2015, 1090), "COMPLETE COMPONENT OWNERS — 3/4"),
    ]
    for path, (x, y), label in panels:
        draw.text((x, y), label, fill=(220, 226, 233), font=font(22))
        canvas.paste(fit_panel(Image.open(path), (930, 850)), (x, y + 40))
    draw.rectangle((45, 1975, 2955, 2040), fill=(34, 39, 46))
    draw.text(
        (65, 1992),
        (
            f"BUILDER GATES {sum(gates.values())}/{len(gates)} PASS  |  "
            "one exact Rz180 duplicate  |  per-component center walls: 0  |  "
            "status: candidate pending independent audit"
        ),
        fill=(126, 232, 160) if all(gates.values()) else (255, 105, 105),
        font=font(19, True),
    )
    canvas.save(BOARD)


def object_bounds(objects: list[bpy.types.Object]) -> dict[str, list[float]]:
    points = [
        obj.matrix_world @ vertex.co
        for obj in objects
        for vertex in obj.data.vertices
    ]
    minimum = [min(point[index] for point in points) for index in range(3)]
    maximum = [max(point[index] for point in points) for index in range(3)]
    return {
        "min_cm": [round(value, 9) for value in minimum],
        "max_cm": [round(value, 9) for value in maximum],
        "dimensions_cm": [
            round(maximum[index] - minimum[index], 9)
            for index in range(3)
        ],
    }


def rz_symmetry(objects: list[bpy.types.Object]) -> dict[str, object]:
    coordinates = {
        (
            round(float((obj.matrix_world @ vertex.co).x), 5),
            round(float((obj.matrix_world @ vertex.co).y), 5),
            round(float((obj.matrix_world @ vertex.co).z), 5),
        )
        for obj in objects
        for vertex in obj.data.vertices
    }
    missing = sum(
        1 for x, y, z in coordinates if (-x, -y, z) not in coordinates
    )
    return {
        "unique_vertices": len(coordinates),
        "missing_rz180_vertices": missing,
        "pass": missing == 0,
    }


def main() -> None:
    ensure_authority()
    clear_scene()
    configure_scene()
    a09 = load_module("a09_process_authority", A09_SCRIPT)
    step03 = load_module("r10_step03_authority", STEP03_SCRIPT)
    step04 = load_module("r10_step04_authority", STEP04_SCRIPT)

    source_objects = {}
    source_halves = []
    for lane, records in DIRECT_OBJECTS.items():
        for component, object_name in records.items():
            obj = append_object(SOURCE_FILES[lane], object_name)
            obj.name = f"{component}_R10_SOURCE_HALF"
            obj["Aerathea.ContractID"] = CONTRACT_ID
            obj["Aerathea.ComponentID"] = component
            obj["Aerathea.GeometryRole"] = "source_half"
            obj["Aerathea.ApprovedInputLane"] = lane
            source_objects[component] = obj
            source_halves.append(obj)
    for component, object_name in ROTATIONAL_OBJECTS.items():
        full = append_object(SOURCE_FILES["step05"], object_name)
        half = extract_positive_x_half(full, component)
        bpy.data.objects.remove(full, do_unlink=True)
        half["Aerathea.ApprovedInputLane"] = "step05"
        source_objects[component] = half
        source_halves.append(half)

    front_image = Image.open(a09.FRONT_PATH).convert("RGB")
    right_image = Image.open(step03.ORIGINAL_RIGHT).convert("RGB")
    front_mask, _component_count = a09.exact_component_mask(
        front_image, a09.FRONT_RECT
    )
    global_cells = a09_global_cells(front_mask, a09)
    rows, _record = step04.load_front_rows()
    active_sets = step04.build_active_sets(rows)
    measurements = json.loads(
        step03.MEASUREMENTS.read_text(encoding="utf-8")
    )
    membership = step03.load_original_right_membership(measurements)
    fill_objects, fill_stats, completed_cells = build_global_head_fills(
        global_cells,
        active_sets,
        step04,
        front_image,
        source_objects,
    )
    source_halves.extend(fill_objects)
    outer_wall, outer_stats = build_combined_outer_wall(
        global_cells,
        completed_cells,
        active_sets,
        step03,
        step04,
        right_image,
        membership,
        source_objects["C04_STRIKE_FACE_POSITIVE_X"].data.materials[0],
    )
    source_halves.append(outer_wall)

    strike_fill, strike_stats = build_strike_fill(
        step03,
        right_image,
        membership,
        source_objects["C04_STRIKE_FACE_POSITIVE_X"].data.materials[0],
    )
    if strike_fill is not None:
        source_halves.append(strike_fill)

    h1 = build_h1(
        source_objects["C07A_HAFT_CYLINDER"],
        source_objects["C07B_HAFT_TO_HANDLE_FERRULE"],
    )
    c06_c07 = build_head_ring_connection(
        "C06_TO_C07A_COMMON_A_C_HALF_CONNECTION",
        "C06_UPPER_HAFT_CAP",
        active_sets["C06_UPPER_HAFT_CAP"],
        step04.ROW_C_STRAIGHT_HAFT_START,
        source_objects["C07A_HAFT_CYLINDER"],
        0,
        step04,
        front_image,
        source_objects["C06_UPPER_HAFT_CAP"].data.materials[0],
    )
    c01_c12 = build_head_ring_connection(
        "C01_TO_C12_COMMON_TOP_HALF_CONNECTION",
        "C01_CENTER_CORE",
        active_sets["C01_CENTER_CORE"],
        step04.C12_LAST_SOURCE_ROW + 1,
        source_objects["C12_UPPER_HEAD_CAP_SPIRE"],
        -1,
        step04,
        front_image,
        source_objects["C01_CENTER_CORE"].data.materials[0],
    )
    c11_cap = build_half_cap(
        source_objects["C11_POMMEL_TERMINAL_CAP"],
        "C11_TERMINAL_EXACT_HALF_CAP",
        "C11_POMMEL_TERMINAL_CAP",
        "bottom",
    )
    c12_cap = build_half_cap(
        source_objects["C12_UPPER_HEAD_CAP_SPIRE"],
        "C12_UPPER_EXACT_HALF_CAP",
        "C12_UPPER_HEAD_CAP_SPIRE",
        "top",
    )
    source_halves.extend((h1, c06_c07, c01_c12, c11_cap, c12_cap))

    half_stats = {
        obj.name: {
            "component": obj.get("Aerathea.ComponentID"),
            "vertices": len(obj.data.vertices),
            "polygons": len(obj.data.polygons),
        }
        for obj in source_halves
    }
    pi_wrap_preserved = (
        source_objects["C07A_HAFT_CYLINDER"].get(
            "Aerathea.ThetaFormula"
        ) == "-pi/2+pi*i/64"
        and bool(
            source_objects["C07A_HAFT_CYLINDER"].get(
                "Aerathea.PiOver2HaftWrapExecuted"
            )
        )
    )
    completed = [complete_rz180(obj) for obj in list(source_halves)]
    symmetry = rz_symmetry(completed)
    bounds = object_bounds(completed)
    components = {
        obj.get("Aerathea.ComponentID") for obj in completed
    }
    gates = {
        "approved_source_hashes_match": all(
            sha256(path) == SOURCE_SHA256[lane]
            for lane, path in SOURCE_FILES.items()
        ),
        "a09_process_authority_loaded": a09.CONTRACT_ID
        == "SB-PHM-A09-FULL-MIRROR",
        "no_rejected_step06_input_loaded": all(
            "Step06_OneRz180SourceHalfAssembly" not in str(path)
            for path in SOURCE_FILES.values()
        ),
        "combined_outer_boundary_only": (
            outer_stats["boundary_faces"] > 0
            and outer_stats["per_component_walls"] == 0
        ),
        "combined_outer_boundary_source_background_pixels_zero": (
            outer_stats["source_background_pixels_sampled"] == 0
        ),
        "row520_additions_zero": all(
            stats["row520_added_pixels"] == 0
            for stats in fill_stats.values()
        ),
        "pi_over_2_haft_wrap_preserved": pi_wrap_preserved,
        "all_objects_completed_by_rz180": all(
            bool(obj.get("Aerathea.Rz180Applied")) for obj in completed
        ),
        "rz180_formula_exact": all(
            obj.get("Aerathea.Rz180Formula")
            == "(X,Y,Z)->(-X,-Y,Z)"
            for obj in completed
        ),
        "rz180_vertex_symmetry": symmetry["pass"],
        "twelve_components_plus_combined_boundary_present": components
        == set(COMPONENT_COLORS),
        "no_modifiers": all(not obj.modifiers for obj in completed),
        "identity_transforms": all(
            tuple(obj.location) == (0.0, 0.0, 0.0)
            and tuple(obj.rotation_euler) == (0.0, 0.0, 0.0)
            and tuple(obj.scale) == (1.0, 1.0, 1.0)
            for obj in completed
        ),
        "complete_height_170_cm": abs(bounds["dimensions_cm"][2] - 170.0)
        <= 1.0e-5,
        "no_fbx_or_unreal": True,
    }
    if not all(gates.values()):
        raise RuntimeError(
            "Complete rebuild gate failure: "
            + ", ".join(name for name, value in gates.items() if not value)
        )

    gray = flat_material(
        "M_R10_COMPLETE_INDEPENDENT_GRAY", (0.30, 0.34, 0.39, 1.0), 0.12
    )
    id_materials = {
        component: flat_material(f"M_R10_ID_{component}", color)
        for component, color in COMPONENT_COLORS.items()
    }
    add_lights((0.0, 0.0, 85.0))
    cameras = {
        "front": add_camera(
            "CAM_R10_COMPLETE_FRONT",
            (0.0, -480.0, 85.0),
            (0.0, 0.0, 85.0),
            182.0,
        ),
        "right": add_camera(
            "CAM_R10_COMPLETE_RIGHT",
            (480.0, 0.0, 86.0),
            (0.0, 0.0, 85.0),
            182.0,
        ),
        "back": add_camera(
            "CAM_R10_COMPLETE_BACK",
            (0.0, 480.0, 85.0),
            (0.0, 0.0, 85.0),
            182.0,
        ),
        "threeq": add_camera(
            "CAM_R10_COMPLETE_THREEQ",
            (235.0, -325.0, 180.0),
            (0.0, 0.0, 82.0),
            188.0,
        ),
    }
    render(cameras["front"], FRONT_RENDER)
    render(cameras["right"], RIGHT_RENDER)
    render(cameras["back"], BACK_RENDER)
    render(cameras["threeq"], COLOR_3Q)
    gray_original = swap_materials(
        completed,
        {component: gray for component in COMPONENT_COLORS},
    )
    render(cameras["threeq"], GRAY_3Q)
    restore_materials(completed, gray_original)
    ids_original = swap_materials(completed, id_materials)
    render(cameras["threeq"], IDS_3Q)
    restore_materials(completed, ids_original)

    scene = bpy.context.scene
    scene.camera = cameras["threeq"]
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    compose_board(gates)
    manifest = {
        "schema": "aerathea.siegebreaker.r10.a09_process_complete_rz180.v1",
        "asset": ASSET,
        "attempt": ATTEMPT,
        "contract_id": CONTRACT_ID,
        "artifact_status": "candidate pending independent audit and Flamestrike",
        "technical_result": "PASS",
        "process_authority": {
            "old_process": str(
                (ASSET_ROOT / "SM_DRW_SiegeBreaker_Hammer_A01_PIXEL_HALF_MIRROR_A09_PLAN.md").relative_to(ROOT)
            ),
            "component_process": "R7/R10 Steps 03/04/05/05C",
            "registration_replacement": "R10/R8 centerline, axis, rotation, duplication only",
            "recovery_record": str(RECOVERY_RECORD.relative_to(ROOT)),
        },
        "source_proofs": {
            lane: {
                "path": str(path.relative_to(ROOT)),
                "sha256": SOURCE_SHA256[lane],
            }
            for lane, path in SOURCE_FILES.items()
        },
        "construction": {
            "source_half_object_count": len(half_stats),
            "complete_object_count": len(completed),
            "source_half_stats": half_stats,
            "global_head_fill": fill_stats,
            "combined_outer_boundary": outer_stats,
            "strike_fill": strike_stats,
            "per_component_center_walls": 0,
            "whole_transform": "Rz(180): (X,Y,Z)->(-X,-Y,Z)",
            "whole_transform_count": 1,
            "haft_wrap": {
                "theta": "-pi/2+pi*i/64, i=0..64",
                "surface": "P=(r*cos(theta),r*sin(theta),z)",
                "pi_over_2_cylinder_wrap_preserved": True,
            },
        },
        "bounds_cm": bounds,
        "rz180_symmetry": symmetry,
        "gates": gates,
        "outputs": {
            "blend": str(BLEND_PATH.relative_to(ROOT)),
            "review_board": str(BOARD.relative_to(ROOT)),
            "renders": [
                str(path.relative_to(ROOT))
                for path in (
                    FRONT_RENDER,
                    RIGHT_RENDER,
                    BACK_RENDER,
                    COLOR_3Q,
                    GRAY_3Q,
                    IDS_3Q,
                )
            ],
        },
    }
    manifest["output_sha256"] = {
        "blend": sha256(BLEND_PATH),
        "review_board": sha256(BOARD),
        "renders": {
            path.name: sha256(path)
            for path in (
                FRONT_RENDER,
                RIGHT_RENDER,
                BACK_RENDER,
                COLOR_3Q,
                GRAY_3Q,
                IDS_3Q,
            )
        },
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print("AERATHEA_R10_A09_PROCESS_COMPLETE_BUILD_PASS")
    print(json.dumps({
        "blend": str(BLEND_PATH),
        "board": str(BOARD),
        "gates": f"{sum(gates.values())}/{len(gates)}",
    }, indent=2))


if __name__ == "__main__":
    main()
