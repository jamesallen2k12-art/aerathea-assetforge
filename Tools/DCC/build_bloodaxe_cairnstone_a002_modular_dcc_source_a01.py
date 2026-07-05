#!/usr/bin/env python3
"""Build the A002 modular DCC source candidate in Blender.

Run only after the A002 Phase 3B script record is accepted as the active
production step:

    blender --background --python Tools/DCC/build_bloodaxe_cairnstone_a002_modular_dcc_source_a01.py

This generator is A002-owned. It encodes the A002 Phase 2B/2C formula records
and the Phase 3A modular DCC plan. It does not read, copy, or derive from A001
or A02 generated meshes, renders, textures, materials, exports, or Unreal
assets.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_GIA_BloodAxeCairnstone_A002"
PACKAGE_ID = f"{ASSET_ID}_ModularDCCSource_A01"
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
AUTOMATION_ROOT = ROOT / "Saved" / "Automation" / "DCC" / ASSET_ID / "ModularDCCSourceA01"
PROOF_ROOT = AUTOMATION_ROOT / "ProofRenders"
MANIFEST_PATH = AUTOMATION_ROOT / f"{ASSET_ID}_ModularDCCSourceA01Manifest.json"

SOURCE_TEMPLATE = (
    ROOT
    / "docs"
    / "assets"
    / "reference"
    / "bloodaxe_cairnstone_asset"
    / "REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
)
SCANLINE_MANIFEST = (
    ROOT
    / "docs"
    / "assets"
    / "reference"
    / "bloodaxe_cairnstone_asset"
    / "ScanlineCapture"
    / "REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate_ScanlineManifest.json"
)
BLUEPRINT_ROOT = ROOT / "docs" / "assets" / "blueprints" / ASSET_ID
PHASE_2B_RECORD = BLUEPRINT_ROOT / f"{ASSET_ID}_PHASE_2B_MEASUREMENT_FORMULA_LOCK_DRAFT.md"
PHASE_2C_RECORD = BLUEPRINT_ROOT / f"{ASSET_ID}_PHASE_2C_PRE_GEOMETRY_FORMULA_AUDIT.md"
PHASE_3A_RECORD = BLUEPRINT_ROOT / f"{ASSET_ID}_PHASE_3A_MODULAR_DCC_SOURCE_CANDIDATE_PLAN.md"


@dataclass(frozen=True)
class DirectionalStations:
    front: float
    back: float
    left: float
    right: float

    def value(self, direction: str) -> float:
        return float(getattr(self, direction))


@dataclass(frozen=True)
class ComponentSpec:
    component_id: str
    asset_name: str
    role: str
    center_px: tuple[int, int]
    width_cm: float
    depth_cm: float
    bottom_station_cm: DirectionalStations | float
    top_station_cm: DirectionalStations | float
    cap_top: bool
    cap_bottom: bool
    material_key: str
    source_authority: str
    notes: tuple[str, ...]


PRIMARY_TO_RING_TOP = DirectionalStations(front=43.7811, back=50.3268, left=35.5280, right=37.5610)
RING_TO_SUPPORT_BOTTOM = DirectionalStations(front=22.9851, back=27.3203, left=19.1304, right=20.1220)

COMPONENTS = [
    ComponentSpec(
        component_id="primary_monolith",
        asset_name=f"{ASSET_ID}_PrimaryMonolith",
        role="vertical main Blood Axe stone",
        center_px=(541, 1222),
        width_cm=120.0,
        depth_cm=90.0,
        bottom_station_cm=PRIMARY_TO_RING_TOP,
        top_station_cm=220.0,
        cap_top=True,
        cap_bottom=False,
        material_key="primary",
        source_authority="A002 Phase 2B/2C primary footprint and per-view primary-to-ring contacts",
        notes=(
            "bottom loop uses exact per-view contact stations by cardinal sector",
            "bottom cap remains open to avoid hidden receiver fill",
        ),
    ),
    ComponentSpec(
        component_id="upper_socket_ring",
        asset_name=f"{ASSET_ID}_UpperSocketRing",
        role="independent receiver layer between primary monolith and support base",
        center_px=(528, 1223),
        width_cm=140.0,
        depth_cm=110.0,
        bottom_station_cm=RING_TO_SUPPORT_BOTTOM,
        top_station_cm=PRIMARY_TO_RING_TOP,
        cap_top=False,
        cap_bottom=False,
        material_key="ring",
        source_authority="A002 Phase 2B/2C per-view layered contact interval",
        notes=(
            "top footprint remains diagnostic/shared/occluded",
            "ring mesh is an interval shell with marker loops, not a full cap or bridge fill",
        ),
    ),
    ComponentSpec(
        component_id="support_base",
        asset_name=f"{ASSET_ID}_SupportBase",
        role="lower support and foundation piece",
        center_px=(528, 1223),
        width_cm=140.0,
        depth_cm=110.0,
        bottom_station_cm=0.0,
        top_station_cm=RING_TO_SUPPORT_BOTTOM,
        cap_top=False,
        cap_bottom=True,
        material_key="support",
        source_authority="A002 Phase 2B/2C support footprint and ring-to-support contacts",
        notes=(
            "top loop uses exact per-view contact stations by cardinal sector",
            "top cap remains open to avoid hidden upper-ring receiver fill",
        ),
    ),
]

MATERIALS = {
    "primary": ("M_A002_PrimaryMonolith_FormulaProof", (0.46, 0.18, 0.15, 1.0)),
    "ring": ("M_A002_UpperSocketRing_FormulaProof", (0.64, 0.38, 0.17, 1.0)),
    "support": ("M_A002_SupportBase_FormulaProof", (0.33, 0.35, 0.36, 1.0)),
    "marker": ("M_A002_ContactMarker_Cyan", (0.06, 0.74, 0.82, 1.0)),
    "blocked": ("M_A002_BlockedInferredSurface_Magenta", (0.95, 0.12, 0.58, 1.0)),
    "label": ("M_A002_Label_White", (0.92, 0.92, 0.86, 1.0)),
}

PROOF_VIEWS = ("front", "back", "left", "right", "top", "angle")


def blender_args() -> list[str]:
    if "--" not in sys.argv:
        return []
    return sys.argv[sys.argv.index("--") + 1 :]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--segments", type=int, default=64, help="Oval station segments. Minimum 16.")
    parser.add_argument("--skip-renders", action="store_true", help="Write blends and manifest without proof renders.")
    return parser.parse_args(blender_args())


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    for mesh in list(bpy.data.meshes):
        bpy.data.meshes.remove(mesh)
    for material in list(bpy.data.materials):
        bpy.data.materials.remove(material)
    for image in list(bpy.data.images):
        bpy.data.images.remove(image)
    for camera in list(bpy.data.cameras):
        bpy.data.cameras.remove(camera)
    for light in list(bpy.data.lights):
        bpy.data.lights.remove(light)
    for curve in list(bpy.data.curves):
        bpy.data.curves.remove(curve)


def create_materials() -> dict[str, bpy.types.Material]:
    materials: dict[str, bpy.types.Material] = {}
    for key, (name, color) in MATERIALS.items():
        mat = bpy.data.materials.new(name)
        mat.diffuse_color = color
        mat.use_nodes = False
        materials[key] = mat
    return materials


def direction_for_xy(x: float, y: float) -> str:
    if abs(x) > abs(y):
        return "right" if x >= 0.0 else "left"
    return "back" if y >= 0.0 else "front"


def station_value(station: DirectionalStations | float, direction: str) -> float:
    if isinstance(station, DirectionalStations):
        return station.value(direction)
    return float(station)


def oval_point(width_cm: float, depth_cm: float, index: int, segments: int) -> tuple[float, float]:
    angle = math.tau * index / segments
    return math.cos(angle) * width_cm * 0.5, math.sin(angle) * depth_cm * 0.5


def make_mesh_object(
    name: str,
    verts: list[tuple[float, float, float]],
    faces: list[tuple[int, ...]],
    material: bpy.types.Material,
) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update(calc_edges=True)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj


def build_vertical_shell(
    spec: ComponentSpec,
    material: bpy.types.Material,
    segments: int,
) -> bpy.types.Object:
    verts: list[tuple[float, float, float]] = []
    bottom_loop: list[int] = []
    top_loop: list[int] = []

    for i in range(segments):
        x, y = oval_point(spec.width_cm, spec.depth_cm, i, segments)
        direction = direction_for_xy(x, y)
        bottom_z = station_value(spec.bottom_station_cm, direction)
        top_z = station_value(spec.top_station_cm, direction)
        bottom_loop.append(len(verts))
        verts.append((x, y, bottom_z))
        top_loop.append(len(verts))
        verts.append((x, y, top_z))

    faces: list[tuple[int, ...]] = []
    for i in range(segments):
        j = (i + 1) % segments
        faces.append((bottom_loop[i], bottom_loop[j], top_loop[j], top_loop[i]))
    if spec.cap_top:
        faces.append(tuple(top_loop))
    if spec.cap_bottom:
        faces.append(tuple(reversed(bottom_loop)))

    obj = make_mesh_object(spec.asset_name, verts, faces, material)
    obj["a002_component_id"] = spec.component_id
    obj["a002_asset_name"] = spec.asset_name
    obj["a002_center_px"] = json.dumps(spec.center_px)
    obj["a002_width_cm"] = spec.width_cm
    obj["a002_depth_cm"] = spec.depth_cm
    obj["a002_source_authority"] = spec.source_authority
    obj["a002_geometry_status"] = "DCC source candidate formula shell"
    return obj


def build_ring_interval_shell(
    spec: ComponentSpec,
    material: bpy.types.Material,
    segments: int,
) -> bpy.types.Object:
    outer_w = spec.width_cm
    outer_d = spec.depth_cm
    inner_w = 120.0
    inner_d = 90.0
    verts: list[tuple[float, float, float]] = []
    outer_bottom: list[int] = []
    outer_top: list[int] = []
    inner_bottom: list[int] = []
    inner_top: list[int] = []

    for i in range(segments):
        ox, oy = oval_point(outer_w, outer_d, i, segments)
        ix, iy = oval_point(inner_w, inner_d, i, segments)
        direction = direction_for_xy(ox, oy)
        bottom_z = station_value(spec.bottom_station_cm, direction)
        top_z = station_value(spec.top_station_cm, direction)
        outer_bottom.append(len(verts))
        verts.append((ox, oy, bottom_z))
        outer_top.append(len(verts))
        verts.append((ox, oy, top_z))
        inner_bottom.append(len(verts))
        verts.append((ix, iy, bottom_z))
        inner_top.append(len(verts))
        verts.append((ix, iy, top_z))

    faces: list[tuple[int, ...]] = []
    for i in range(segments):
        j = (i + 1) % segments
        faces.append((outer_bottom[i], outer_bottom[j], outer_top[j], outer_top[i]))
        faces.append((inner_bottom[j], inner_bottom[i], inner_top[i], inner_top[j]))

    obj = make_mesh_object(spec.asset_name, verts, faces, material)
    obj["a002_component_id"] = spec.component_id
    obj["a002_asset_name"] = spec.asset_name
    obj["a002_center_px"] = json.dumps(spec.center_px)
    obj["a002_outer_width_cm"] = outer_w
    obj["a002_outer_depth_cm"] = outer_d
    obj["a002_inner_width_cm"] = inner_w
    obj["a002_inner_depth_cm"] = inner_d
    obj["a002_source_authority"] = spec.source_authority
    obj["a002_geometry_status"] = "DCC source candidate interval shell; top footprint diagnostic"
    return obj


def make_ellipse_marker(
    name: str,
    width_cm: float,
    depth_cm: float,
    station: DirectionalStations | float,
    material: bpy.types.Material,
    segments: int,
    thickness_cm: float = 1.25,
) -> bpy.types.Object:
    verts: list[tuple[float, float, float]] = []
    outer_loop: list[int] = []
    inner_loop: list[int] = []
    outer_w = width_cm + thickness_cm
    outer_d = depth_cm + thickness_cm
    inner_w = max(1.0, width_cm - thickness_cm)
    inner_d = max(1.0, depth_cm - thickness_cm)
    for i in range(segments):
        ox, oy = oval_point(outer_w, outer_d, i, segments)
        ix, iy = oval_point(inner_w, inner_d, i, segments)
        direction = direction_for_xy(ox, oy)
        z = station_value(station, direction)
        outer_loop.append(len(verts))
        verts.append((ox, oy, z + 0.05))
        inner_loop.append(len(verts))
        verts.append((ix, iy, z + 0.05))

    faces: list[tuple[int, ...]] = []
    for i in range(segments):
        j = (i + 1) % segments
        faces.append((outer_loop[i], outer_loop[j], inner_loop[j], inner_loop[i]))
    obj = make_mesh_object(name, verts, faces, material)
    obj["a002_marker_type"] = "contact_station_loop"
    return obj


def make_cube_marker(
    name: str,
    location: tuple[float, float, float],
    size_cm: float,
    material: bpy.types.Material,
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
    obj = make_mesh_object(name, verts, faces, material)
    obj["a002_marker_type"] = "directional_contact_station"
    return obj


def directional_marker_location(
    direction: str,
    width_cm: float,
    depth_cm: float,
    z_cm: float,
) -> tuple[float, float, float]:
    if direction == "front":
        return (0.0, -depth_cm * 0.5, z_cm)
    if direction == "back":
        return (0.0, depth_cm * 0.5, z_cm)
    if direction == "left":
        return (-width_cm * 0.5, 0.0, z_cm)
    if direction == "right":
        return (width_cm * 0.5, 0.0, z_cm)
    raise ValueError(f"Unsupported direction: {direction}")


def add_directional_markers(
    spec: ComponentSpec,
    material: bpy.types.Material,
) -> None:
    for station_name, station in (("bottom", spec.bottom_station_cm), ("top", spec.top_station_cm)):
        if not isinstance(station, DirectionalStations):
            continue
        for direction in ("front", "back", "left", "right"):
            z = station.value(direction)
            make_cube_marker(
                f"MARKER_{spec.component_id}_{station_name}_{direction}_{z:.4f}cm",
                directional_marker_location(direction, spec.width_cm, spec.depth_cm, z),
                4.0,
                material,
            )


def add_component_label(spec: ComponentSpec, material: bpy.types.Material) -> None:
    curve = bpy.data.curves.new(f"LABEL_{spec.component_id}_Curve", "FONT")
    curve.body = spec.component_id
    curve.align_x = "CENTER"
    curve.align_y = "CENTER"
    curve.size = 7.5
    obj = bpy.data.objects.new(f"LABEL_{spec.component_id}", curve)
    obj.location = (0.0, -spec.depth_cm * 0.75, 230.0)
    obj.rotation_euler = (math.radians(90.0), 0.0, 0.0)
    obj.data.materials.append(material)
    bpy.context.collection.objects.link(obj)
    obj["a002_marker_type"] = "visible_component_identity_label"


def add_scene_guides(spec: ComponentSpec, materials: dict[str, bpy.types.Material], segments: int) -> None:
    make_ellipse_marker(
        f"MARKER_{spec.component_id}_center_footprint_{spec.width_cm:.0f}x{spec.depth_cm:.0f}cm",
        spec.width_cm,
        spec.depth_cm,
        0.0,
        materials["blocked"],
        segments,
        thickness_cm=1.0,
    )
    make_ellipse_marker(
        f"MARKER_{spec.component_id}_top_contact_loop",
        spec.width_cm,
        spec.depth_cm,
        spec.top_station_cm,
        materials["marker"],
        segments,
    )
    make_ellipse_marker(
        f"MARKER_{spec.component_id}_bottom_contact_loop",
        spec.width_cm,
        spec.depth_cm,
        spec.bottom_station_cm,
        materials["marker"],
        segments,
    )
    add_directional_markers(spec, materials["marker"])
    add_component_label(spec, materials["label"])


def component_bounds() -> tuple[Vector, Vector]:
    verts: list[Vector] = []
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH":
            continue
        verts.extend(obj.matrix_world @ vert.co for vert in obj.data.vertices)
    if not verts:
        return Vector((-70.0, -55.0, 0.0)), Vector((70.0, 55.0, 220.0))
    return (
        Vector((min(v.x for v in verts), min(v.y for v in verts), min(v.z for v in verts))),
        Vector((max(v.x for v in verts), max(v.y for v in verts), max(v.z for v in verts))),
    )


def add_camera_and_lights(view: str) -> bpy.types.Camera:
    min_v, max_v = component_bounds()
    center = (min_v + max_v) * 0.5
    span = max((max_v - min_v).x, (max_v - min_v).y, (max_v - min_v).z, 1.0)
    distance = span * 2.2
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
    direction = center - cam.location
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    cam.data.lens = 55.0
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = max(span * 1.28, 170.0)
    bpy.context.scene.camera = cam

    light_data = bpy.data.lights.new(f"KEY_{view}", "AREA")
    light = bpy.data.objects.new(f"KEY_{view}", light_data)
    bpy.context.collection.objects.link(light)
    light.location = location + Vector((0.0, 0.0, span * 0.3))
    light.rotation_euler = cam.rotation_euler
    light.data.energy = 420.0
    light.data.size = 4.0
    return cam_data


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
    scene.render.film_transparent = False
    scene.world.color = (0.035, 0.038, 0.04)


def configure_save_policy() -> None:
    bpy.context.preferences.filepaths.save_version = 0


def render_proofs(spec: ComponentSpec) -> list[str]:
    configure_render()
    PROOF_ROOT.mkdir(parents=True, exist_ok=True)
    rendered: list[str] = []
    for view in PROOF_VIEWS:
        for obj in [obj for obj in bpy.context.scene.objects if obj.type in {"CAMERA", "LIGHT"}]:
            bpy.data.objects.remove(obj, do_unlink=True)
        add_camera_and_lights(view)
        path = PROOF_ROOT / f"{spec.asset_name}_{view.title()}Proof.png"
        bpy.context.scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)
        rendered.append(str(path.relative_to(ROOT)))
    return rendered


def purge_internal_render_images() -> None:
    for image in list(bpy.data.images):
        if image.name in {"Render Result", "Viewer Node"}:
            bpy.data.images.remove(image)


def triangle_count() -> int:
    total = 0
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH":
            continue
        total += sum(max(1, len(poly.vertices) - 2) for poly in obj.data.polygons)
    return total


def object_report() -> list[dict[str, object]]:
    reports: list[dict[str, object]] = []
    for obj in sorted(bpy.context.scene.objects, key=lambda item: item.name):
        if obj.type not in {"MESH", "FONT"}:
            continue
        entry: dict[str, object] = {
            "name": obj.name,
            "type": obj.type,
            "location": [round(float(v), 6) for v in obj.location],
        }
        if obj.type == "MESH":
            entry["vertices"] = len(obj.data.vertices)
            entry["polygons"] = len(obj.data.polygons)
            entry["uv_layers"] = len(obj.data.uv_layers)
            entry["materials"] = [mat.name for mat in obj.data.materials if mat is not None]
        reports.append(entry)
    return reports


def build_component(spec: ComponentSpec, segments: int, skip_renders: bool) -> dict[str, object]:
    clear_scene()
    materials = create_materials()
    if spec.component_id == "upper_socket_ring":
        main_obj = build_ring_interval_shell(spec, materials[spec.material_key], segments)
    else:
        main_obj = build_vertical_shell(spec, materials[spec.material_key], segments)
    add_scene_guides(spec, materials, segments)
    main_obj.select_set(True)
    bpy.context.view_layer.objects.active = main_obj

    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    blend_path = SOURCE_ROOT / f"{spec.asset_name}.blend"
    proof_paths = [] if skip_renders else render_proofs(spec)
    purge_internal_render_images()
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    return {
        "component_id": spec.component_id,
        "asset_name": spec.asset_name,
        "role": spec.role,
        "center_px": list(spec.center_px),
        "blend_path": str(blend_path.relative_to(ROOT)),
        "proof_renders": proof_paths,
        "source_authority": spec.source_authority,
        "notes": list(spec.notes),
        "triangle_count_with_markers": triangle_count(),
        "objects": object_report(),
    }


def write_manifest(args: argparse.Namespace, component_reports: list[dict[str, object]]) -> None:
    AUTOMATION_ROOT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "asset_id": ASSET_ID,
        "package_id": PACKAGE_ID,
        "status": "DCC source candidate generated by A002-owned script",
        "script": str(Path(__file__).resolve().relative_to(ROOT)),
        "source_template": str(SOURCE_TEMPLATE.relative_to(ROOT)),
        "scanline_manifest": str(SCANLINE_MANIFEST.relative_to(ROOT)),
        "authority_records": [
            str(PHASE_2B_RECORD.relative_to(ROOT)),
            str(PHASE_2C_RECORD.relative_to(ROOT)),
            str(PHASE_3A_RECORD.relative_to(ROOT)),
        ],
        "core_policy": {
            "no_a001_generated_output_as_source": True,
            "no_a02_generated_output_as_source": True,
            "no_uv_generation": True,
            "no_texture_nodes": True,
            "no_fbx_export": True,
            "no_unreal_output": True,
            "no_component_merge": True,
            "no_cross_view_average": True,
            "cardinal_station_rule": "nearest cardinal sector uses exact per-view source station",
        },
        "formula_constants": {
            "overall_height_cm": 220.0,
            "support_footprint_cm": [140.0, 110.0],
            "primary_footprint_cm": [120.0, 90.0],
            "primary_to_ring_top_cm": asdict(PRIMARY_TO_RING_TOP),
            "ring_to_support_bottom_cm": asdict(RING_TO_SUPPORT_BOTTOM),
            "component_centers_px": {
                "primary_monolith": [541, 1222],
                "upper_socket_ring": [528, 1223],
                "support_base": [528, 1223],
            },
        },
        "arguments": {
            "segments": int(args.segments),
            "skip_renders": bool(args.skip_renders),
        },
        "components": component_reports,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    args.segments = max(16, int(args.segments))
    configure_save_policy()
    component_reports = [build_component(spec, args.segments, args.skip_renders) for spec in COMPONENTS]
    write_manifest(args, component_reports)
    print(MANIFEST_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
