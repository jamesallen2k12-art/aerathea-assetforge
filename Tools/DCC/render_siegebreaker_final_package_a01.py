"""Render Siege Breaker fixed-object orthographic proof and final DCC beauty."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = os.environ.get("AET_SB_REVISION", "FinalPackage_A01")
CONTRACT_ID = os.environ.get("AET_SB_CONTRACT_ID", "SB-CR-STEPS01-16-FINALPKG-A01")
BLEND_PATH = Path(
    os.environ.get(
        "AET_SB_BLEND_PATH",
        str(ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID / f"{ASSET_ID}_DCCGameReady_FinalPackage_A01.blend"),
    )
)
OUTPUT_ROOT = Path(
    os.environ.get(
        "AET_SB_OUTPUT_ROOT",
        str(ROOT / "Saved/Automation/DCC" / ASSET_ID / "FinalPackage_A01"),
    )
)
ORTHO_ROOT = OUTPUT_ROOT / "orthographic_true"
BEAUTY_PATH = OUTPUT_ROOT / os.environ.get("AET_SB_BEAUTY_NAME", f"{ASSET_ID}_FinalReview.png")
RESOLUTION = int(os.environ.get("AET_SB_RENDER_RESOLUTION", "2048"))
RENDER_MODE = os.environ.get("AET_SB_RENDER_MODE", "all").strip().lower()
SAMPLES = int(os.environ.get("AET_SB_RENDER_SAMPLES", "32"))
MARGIN = 1.15
BEAUTY_FOCUS = os.environ.get("AET_SB_BEAUTY_FOCUS", "full").strip().lower()
LIGHT_TARGET_Z = float(os.environ.get("AET_SB_LIGHT_TARGET_Z", "0.95"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def bounds(objects):
    points = [obj.matrix_world @ Vector(corner) for obj in objects for corner in obj.bound_box]
    minimum = Vector(tuple(min(point[index] for point in points) for index in range(3)))
    maximum = Vector(tuple(max(point[index] for point in points) for index in range(3)))
    return minimum, maximum


def ensure_camera(name, center, offset, ortho_scale=None):
    data = bpy.data.cameras.get(name) or bpy.data.cameras.new(name)
    camera = bpy.data.objects.get(name) or bpy.data.objects.new(name, data)
    if camera.name not in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.link(camera)
    camera.location = center + Vector(offset)
    camera.rotation_euler = (center - camera.location).to_track_quat("-Z", "Y").to_euler()
    if ortho_scale is None:
        data.type = "PERSP"
        data.lens = 58.0
    else:
        data.type = "ORTHO"
        data.ortho_scale = ortho_scale
    return camera


def ensure_area(name, location, energy, size, color):
    data = bpy.data.lights.get(name) or bpy.data.lights.new(name, "AREA")
    data.energy = energy
    data.shape = "DISK"
    data.size = size
    data.color = color
    obj = bpy.data.objects.get(name) or bpy.data.objects.new(name, data)
    if obj.name not in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    target = Vector((0.0, 0.0, LIGHT_TARGET_Z))
    obj.rotation_euler = (target - obj.location).to_track_quat("-Z", "Y").to_euler()
    return obj


def configure_render(scene):
    try:
        scene.render.engine = "CYCLES"
    except Exception:
        pass
    if hasattr(scene, "cycles"):
        scene.cycles.device = "CPU"
        scene.cycles.samples = SAMPLES
        scene.cycles.use_denoising = True
        scene.cycles.max_bounces = 5
        scene.cycles.diffuse_bounces = 3
        scene.cycles.glossy_bounces = 3
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = False
    scene.render.use_compositing = False
    scene.render.use_sequencer = False
    scene.render.use_border = False
    scene.render.image_settings.color_depth = "8"
    try:
        scene.view_settings.view_transform = "Standard"
        scene.view_settings.look = "Medium High Contrast"
        scene.view_settings.exposure = 0.0
        scene.view_settings.gamma = 1.0
    except Exception:
        pass


def configure_world(scene, color, strength):
    scene.world.use_nodes = True
    background = next((node for node in scene.world.node_tree.nodes if node.type == "BACKGROUND"), None)
    if background is not None:
        background.inputs["Color"].default_value = (*color, 1.0)
        background.inputs["Strength"].default_value = strength
    scene.world.color = color


def make_ground():
    bpy.ops.mesh.primitive_plane_add(size=12.0, location=(0.0, 0.0, -0.0015))
    ground = bpy.context.object
    ground.name = "SB_REVIEW_GROUND"
    material = bpy.data.materials.new("M_SB_ReviewGround")
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (0.018, 0.026, 0.038, 1.0)
    bsdf.inputs["Metallic"].default_value = 0.0
    bsdf.inputs["Roughness"].default_value = 0.82
    ground.data.materials.append(material)
    return ground


def main() -> int:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    ORTHO_ROOT.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(BLEND_PATH))
    scene = bpy.context.scene
    configure_render(scene)
    collection = bpy.data.collections["SB_ASSET"]
    objects = [obj for obj in collection.objects if obj.type == "MESH"]
    collection.hide_render = False
    for obj in collection.objects:
        obj.hide_render = False
    for hidden_collection_name in ("SB_EXPORT", "SB_COLLISION"):
        hidden_collection = bpy.data.collections.get(hidden_collection_name)
        if hidden_collection is not None:
            hidden_collection.hide_render = True
    minimum, maximum = bounds(objects)
    center = (minimum + maximum) * 0.5
    extent = maximum - minimum
    longest = max(extent)
    ortho_scale = longest * MARGIN
    distance = longest * 3.2

    fidelity_a02 = REVISION == "VisualFidelity_A02"
    ensure_area("SB_Key", Vector((2.6, -3.0, 3.8)), 720 if fidelity_a02 else 1150, 3.2, (1.0, 0.76, 0.55))
    ensure_area("SB_Fill", Vector((-3.0, -1.5, 2.1)), 380 if fidelity_a02 else 760, 4.2, (0.38, 0.58, 1.0))
    ensure_area("SB_Rim", Vector((1.0, 3.2, 3.0)), 650 if fidelity_a02 else 980, 3.0, (0.25, 0.52, 1.0))

    scene.render.resolution_x = RESOLUTION
    scene.render.resolution_y = RESOLUTION
    configure_world(scene, (0.72, 0.72, 0.72), 0.75)
    views = {
        "front": (0, -distance, 0),
        "back": (0, distance, 0),
        "left": (-distance, 0, 0),
        "right": (distance, 0, 0),
        "top": (0, 0, distance),
        "bottom": (0, 0, -distance),
    }
    manifest = {
        "schema": "aerathea.fixed_object_orthographic_manifest.v1",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "artifact_status": "proof only",
        "source_blend": str(BLEND_PATH.relative_to(ROOT)),
        "source_blend_sha256": sha256(BLEND_PATH),
        "collection": "SB_ASSET",
        "resolution_px": [RESOLUTION, RESOLUTION],
        "ortho_scale_m": ortho_scale,
        "pixels_per_meter": RESOLUTION / ortho_scale,
        "pixels_per_centimeter": RESOLUTION / ortho_scale / 100.0,
        "world_bounds_m": {"minimum": list(minimum), "maximum": list(maximum), "extent": list(extent)},
        "fixed_object": True,
        "object_rotation_between_views": False,
        "views": {},
    }
    selected_views = views if RENDER_MODE in {"all", "orthos"} else ({"front": views["front"]} if RENDER_MODE == "front" else {})
    for view, offset in selected_views.items():
        camera = ensure_camera(f"CAM_SB_{view.upper()}", center, offset, ortho_scale)
        scene.camera = camera
        path = ORTHO_ROOT / f"{view}.png"
        scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)
        manifest["views"][view] = {
            "file": path.name,
            "sha256": sha256(path),
            "camera_location": list(camera.location),
            "ortho_scale_m": camera.data.ortho_scale,
            "resolution_px": [RESOLUTION, RESOLUTION],
        }
    manifest_path = ORTHO_ROOT / "render_manifest.json"
    if selected_views:
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    if RENDER_MODE in {"all", "beauty"}:
        make_ground()
        configure_world(scene, (0.006, 0.011, 0.020), 0.09 if fidelity_a02 else 0.18)
        scene.render.resolution_x = 1600 if RESOLUTION == 2048 else RESOLUTION
        scene.render.resolution_y = 2000 if RESOLUTION == 2048 else RESOLUTION
        focus_cameras = {
            "full": (Vector((0.0, 0.0, 0.87)), (2.45, -3.75, 1.45), 58.0),
            "head": (Vector((0.0, 0.0, 1.51)), (0.72, -1.28, 0.32), 70.0),
            "grip": (Vector((0.0, 0.0, 0.39)), (0.42, -0.92, 0.24), 72.0),
            "pommel": (Vector((0.0, 0.0, 0.09)), (0.30, -0.62, 0.16), 72.0),
        }
        if BEAUTY_FOCUS not in focus_cameras:
            raise ValueError(f"Unsupported AET_SB_BEAUTY_FOCUS={BEAUTY_FOCUS!r}")
        beauty_center, beauty_offset, beauty_lens = focus_cameras[BEAUTY_FOCUS]
        beauty = ensure_camera(f"CAM_SB_BEAUTY_{BEAUTY_FOCUS.upper()}", beauty_center, beauty_offset, None)
        beauty.data.lens = beauty_lens
        scene.camera = beauty
        scene.render.filepath = str(BEAUTY_PATH)
        bpy.ops.render.render(write_still=True)

        beauty_manifest = {
            "schema": "aerathea.dcc_review_render.v1",
            "asset_id": ASSET_ID,
            "revision": REVISION,
            "contract_id": CONTRACT_ID,
            "artifact_status": "candidate",
            "pipeline_status": "DCC game-ready candidate",
            "source_blend": str(BLEND_PATH.relative_to(ROOT)),
            "source_blend_sha256": sha256(BLEND_PATH),
            "image": str(BEAUTY_PATH.relative_to(ROOT)),
            "image_sha256": sha256(BEAUTY_PATH),
            "resolution_px": [scene.render.resolution_x, scene.render.resolution_y],
            "camera_location": list(beauty.location),
            "camera_lens_mm": beauty.data.lens,
            "focus": BEAUTY_FOCUS,
            "final_visual_approval": "pending Flamestrike",
        }
        (OUTPUT_ROOT / "beauty_render_manifest.json").write_text(json.dumps(beauty_manifest, indent=2) + "\n", encoding="utf-8")
        print(BEAUTY_PATH)
    if selected_views:
        print(manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
