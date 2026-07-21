"""Render A03 against the locked primary source-view camera and review setup."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = "PixelReconstruction_A03"
CONTRACT_ID = "SB-VF-A03-PIXEL"
BLEND_PATH = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID / f"{ASSET_ID}_DCCGameReady_{REVISION}.blend"
OUTPUT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A03"
MATCHED = OUTPUT / "matched_source_view"
ORTHOS = OUTPUT / "orthographic_true"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("preview", "final", "orthos", "all"), default="preview")
    parser.add_argument("--width", type=int, default=1200)
    parser.add_argument("--height", type=int, default=1800)
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    return parser.parse_args(argv)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def look_at(obj, target):
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()


def camera(name, location, target, lens=70.0, ortho_scale=None):
    data = bpy.data.cameras.get(name) or bpy.data.cameras.new(name)
    obj = bpy.data.objects.get(name) or bpy.data.objects.new(name, data)
    if obj.name not in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    look_at(obj, target)
    if ortho_scale is None:
        data.type = "PERSP"
        data.lens = lens
    else:
        data.type = "ORTHO"
        data.ortho_scale = ortho_scale
    return obj


def area(name, location, energy, size, color, target=(0.0, 0.0, 0.95)):
    data = bpy.data.lights.get(name) or bpy.data.lights.new(name, "AREA")
    data.energy = energy
    data.shape = "DISK"
    data.size = size
    data.color = color
    obj = bpy.data.objects.get(name) or bpy.data.objects.new(name, data)
    if obj.name not in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    look_at(obj, target)
    return obj


def ground():
    bpy.ops.mesh.primitive_plane_add(size=12.0, location=(0.0, 0.0, -0.001))
    obj = bpy.context.object
    obj.name = "SB_A03_REVIEW_GROUND"
    material = bpy.data.materials.new("M_SB_A03_ReviewGround")
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (0.78, 0.75, 0.66, 1.0)
    bsdf.inputs["Roughness"].default_value = 0.94
    obj.data.materials.append(material)
    return obj


def configure(scene, width, height, final=False):
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = 56 if final else 24
    scene.cycles.use_denoising = True
    scene.cycles.max_bounces = 5
    scene.cycles.diffuse_bounces = 3
    scene.cycles.glossy_bounces = 3
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.image_settings.color_depth = "8"
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = True
    scene.render.use_compositing = False
    scene.render.use_sequencer = False
    scene.view_settings.view_transform = "Standard"
    # Some review hosts expose only the fallback OCIO "None" look.  Preserve
    # the intended contrast when available without blocking deterministic CPU
    # rendering on those hosts.
    available_looks = {item.identifier for item in scene.view_settings.bl_rna.properties["look"].enum_items}
    scene.view_settings.look = "Medium High Contrast" if "Medium High Contrast" in available_looks else "None"
    scene.view_settings.exposure = -0.15
    scene.view_settings.gamma = 1.0
    scene.world.use_nodes = True
    background = next(node for node in scene.world.node_tree.nodes if node.type == "BACKGROUND")
    background.inputs["Color"].default_value = (0.78, 0.75, 0.67, 1.0)
    background.inputs["Strength"].default_value = 0.28
    scene.camera.data.dof.use_dof = False if scene.camera else False


def source_objects():
    collection = bpy.data.collections["SB_ASSET"]
    collection.hide_render = False
    objects = [obj for obj in collection.all_objects if obj.type == "MESH"]
    for obj in objects:
        obj.hide_render = False
    for name in ("SB_EXPORT", "SB_COLLISION"):
        hidden = bpy.data.collections.get(name)
        if hidden is not None:
            hidden.hide_render = True
    return objects


def render_matched(scene, width, height, final):
    MATCHED.mkdir(parents=True, exist_ok=True)
    matched_camera = camera(
        "CAM_SB_A03_SOURCE_MATCH",
        (-1.82629301, -1.47890292, 1.95628741),
        (0.0, 0.0, 0.91),
        lens=54.56600843,
    )
    scene.camera = matched_camera
    configure(scene, width, height, final)
    area("SB_A03_Key", (-2.7, -3.2, 4.2), 510.0, 3.0, (1.0, 0.72, 0.43))
    area("SB_A03_Fill", (3.2, -2.1, 2.5), 280.0, 4.0, (0.40, 0.58, 1.0))
    area("SB_A03_Rim", (-1.2, 3.2, 3.6), 420.0, 2.8, (0.28, 0.52, 1.0))
    area("SB_A03_FrontSoft", (-0.2, -4.2, 1.1), 160.0, 3.5, (1.0, 0.88, 0.70))
    area("SB_A03_GripFill", (-1.8, -2.8, 0.75), 190.0, 2.2, (1.0, 0.62, 0.34), target=(0.0, 0.0, 0.42))
    area("SB_A03_PommelFill", (1.5, -2.2, 0.30), 120.0, 1.8, (0.50, 0.68, 1.0), target=(0.0, 0.0, 0.09))
    path = MATCHED / (f"{ASSET_ID}_A03_SourceMatched_Final.png" if final else f"{ASSET_ID}_A03_SourceMatched_Preview.png")
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    manifest = {
        "schema": "aerathea.siegebreaker.source_matched_render.v1",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "artifact_status": "candidate",
        "source_blend": str(BLEND_PATH.relative_to(ROOT)),
        "source_blend_sha256": sha256(BLEND_PATH),
        "image": str(path.relative_to(ROOT)),
        "image_sha256": sha256(path),
        "resolution_px": [width, height],
        "camera": {"location": list(matched_camera.location), "target": [0.0, 0.0, 0.91], "lens_mm": matched_camera.data.lens},
        "color_management": {"view_transform": scene.view_settings.view_transform, "look": scene.view_settings.look, "exposure": scene.view_settings.exposure},
        "primary_source_authority": "large 3/4 concept render",
        "final_visual_approval": "pending Flamestrike",
    }
    manifest_path = MATCHED / "render_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(path)
    return path


def render_orthos(scene, resolution=1536):
    ORTHOS.mkdir(parents=True, exist_ok=True)
    configure(scene, resolution, resolution, True)
    target = Vector((0.0, 0.0, 0.85))
    scale = 1.92
    distance = 5.0
    views = {
        "front": Vector((0.0, -distance, 0.85)), "back": Vector((0.0, distance, 0.85)),
        "left": Vector((-distance, 0.0, 0.85)), "right": Vector((distance, 0.0, 0.85)),
        "top": Vector((0.0, 0.0, distance)), "bottom": Vector((0.0, 0.0, -distance)),
    }
    outputs = {}
    for name, location in views.items():
        cam = camera(f"CAM_SB_A03_{name.upper()}", location, target, ortho_scale=scale)
        scene.camera = cam
        path = ORTHOS / f"{name}.png"
        scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)
        outputs[name] = {"path": str(path.relative_to(ROOT)), "sha256": sha256(path)}
    manifest = {
        "schema": "aerathea.fixed_object_orthographic_manifest.v2",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "artifact_status": "proof only",
        "source_blend": str(BLEND_PATH.relative_to(ROOT)),
        "source_blend_sha256": sha256(BLEND_PATH),
        "fixed_object": True,
        "object_rotation_between_views": False,
        "resolution_px": [resolution, resolution],
        "ortho_scale_m": scale,
        "views": outputs,
    }
    path = ORTHOS / "render_manifest.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(path)


def main():
    args = parse_args()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(BLEND_PATH))
    scene = bpy.context.scene
    source_objects()
    # Camera exists before configure accesses its DOF data.
    scene.camera = camera("CAM_SB_A03_BOOT", (-1.82629301, -1.47890292, 1.95628741), (0.0, 0.0, 0.91), 54.56600843)
    if args.mode in ("preview", "final", "all"):
        render_matched(scene, args.width, args.height, args.mode in ("final", "all"))
    if args.mode in ("orthos", "all"):
        render_orthos(scene)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
