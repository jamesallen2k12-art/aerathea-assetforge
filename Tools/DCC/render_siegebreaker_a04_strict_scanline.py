#!/usr/bin/env python3
"""Render the completed A04 source-owned and fixed-object DCC review views."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = "StrictScanline_A04"
CONTRACT_ID = "SB-VF-A04-STRICT-SCANLINE"
BLEND_PATH = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID / f"{ASSET_ID}_DCCGameReady_{REVISION}.blend"
OUTPUT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A04" / "renders"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def look_at(obj: bpy.types.Object, target: tuple[float, float, float]) -> None:
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()


def camera(name: str, location: tuple[float, float, float], target: tuple[float, float, float], lens=55.0, ortho_scale=None) -> bpy.types.Object:
    data = bpy.data.cameras.new(name)
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    look_at(obj, target)
    if ortho_scale is None:
        data.type = "PERSP"
        data.lens = lens
    else:
        data.type = "ORTHO"
        data.ortho_scale = ortho_scale
    data.dof.use_dof = False
    return obj


def configure(width: int, height: int, transparent=True) -> None:
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 3.0
    scene.eevee.gtao_factor = 1.15
    scene.eevee.taa_render_samples = 96
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.image_settings.color_depth = "8"
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = transparent
    scene.render.use_file_extension = True
    scene.view_settings.view_transform = "Standard"
    available_looks = {item.identifier for item in scene.view_settings.bl_rna.properties["look"].enum_items}
    scene.view_settings.look = "Medium High Contrast" if "Medium High Contrast" in available_looks else "None"
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0


def set_visibility() -> None:
    for lod in range(4):
        collection = bpy.data.collections.get(f"SB_A04_LOD{lod}")
        if collection is not None:
            collection.hide_render = lod != 0
    collision = bpy.data.collections.get("SB_A04_COLLISION")
    if collision is not None:
        collision.hide_render = True
    review = bpy.data.collections.get("SB_A04_REVIEW")
    if review is not None:
        review.hide_render = False
    ground = bpy.data.objects.get("SB_A04_ReviewGround")
    if ground is not None:
        ground.hide_render = True


def set_lod0_render_mode(facade_only: bool) -> None:
    collection = bpy.data.collections.get("SB_A04_LOD0")
    if collection is None:
        raise RuntimeError("SB_A04_LOD0 is missing")
    # Materialize direct collection membership before mutating visibility;
    # Blender 3.0.1 can invalidate the live all_objects iterator here.
    for obj in list(collection.objects):
        if obj.type == "MESH":
            obj.hide_render = facade_only and not obj.name.startswith("A04_SourceFacade_")


def render(name: str, camera_obj: bpy.types.Object, width: int, height: int, facade_only=False) -> dict[str, object]:
    set_lod0_render_mode(facade_only)
    configure(width, height, transparent=True)
    scene = bpy.context.scene
    scene.camera = camera_obj
    path = OUTPUT / f"{name}.png"
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    return {"path": rel(path), "sha256": sha256(path), "resolution": [width, height]}


def main() -> int:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    set_visibility()
    target = (0.0, 0.0, 0.85)
    views: dict[str, dict[str, object]] = {}
    views["authority_front"] = render(
        "SM_DRW_SiegeBreaker_Hammer_A01_A04_AuthorityFront",
        camera("CAM_SB_A04_AUTHORITY_FRONT", (0.0, -4.8, 0.85), target, ortho_scale=1.82),
        900,
        1200,
        facade_only=True,
    )
    views["beauty"] = render(
        "SM_DRW_SiegeBreaker_Hammer_A01_A04_Beauty",
        camera("CAM_SB_A04_BEAUTY", (0.58, -4.25, 1.35), (0.0, 0.0, 0.91), lens=58.0),
        900,
        1200,
    )
    ortho_cameras = {
        "front": camera("CAM_SB_A04_FRONT", (0.0, -5.0, 0.85), target, ortho_scale=1.82),
        "back": camera("CAM_SB_A04_BACK", (0.0, 5.0, 0.85), target, ortho_scale=1.82),
        "left": camera("CAM_SB_A04_LEFT", (-5.0, 0.0, 0.85), target, ortho_scale=1.82),
        "right": camera("CAM_SB_A04_RIGHT", (5.0, 0.0, 0.85), target, ortho_scale=1.82),
        "top": camera("CAM_SB_A04_TOP", (0.0, 0.0, 5.0), (0.0, 0.0, 0.85), ortho_scale=0.62),
        "bottom": camera("CAM_SB_A04_BOTTOM", (0.0, 0.0, -5.0), (0.0, 0.0, 0.85), ortho_scale=0.62),
    }
    for view_name, camera_obj in ortho_cameras.items():
        views[view_name] = render(
            f"SM_DRW_SiegeBreaker_Hammer_A01_A04_{view_name.title()}",
            camera_obj,
            720,
            720,
            facade_only=view_name == "front",
        )

    manifest = {
        "schema": "aerathea.siegebreaker_a04_render_manifest.v1",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "status": "proof only",
        "source_blend": rel(BLEND_PATH),
        "source_blend_sha256": sha256(BLEND_PATH),
        "fixed_object": True,
        "object_rotation_between_views": False,
        "primary_visible_owner": "fresh A04 primary source facade",
        "views": views,
    }
    path = OUTPUT / f"{ASSET_ID}_A04_RenderManifest.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(path)
    print("A04 RENDERS COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
