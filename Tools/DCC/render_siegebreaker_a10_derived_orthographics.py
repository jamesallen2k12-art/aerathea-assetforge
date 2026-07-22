#!/usr/bin/env python3
"""Render six common-scale orthographics from the unchanged approved A09 blend."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_DRW_SiegeBreaker_Hammer_A01"
CONTRACT_ID = "SB-ORTHO-A10-DERIVED-A01"
MODEL_NAME = f"{ASSET}_A09_CompleteMirroredModel"
BLEND_REL = Path(
    "SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/"
    "A09_PixelHalfMirror_VisualMatch_A01/"
    "SM_DRW_SiegeBreaker_Hammer_A01_A09_PixelHalfMirror_VisualMatch_A01.blend"
)
BLEND_PATH = ROOT / BLEND_REL
EXPECTED_BLEND_SHA256 = "06ffb121d00cddb7b9e30a60067a5036a851d285f15daca3bffe3a663fd6d78f"
EXPECTED_DIMENSIONS_CM = [75.130516, 32.957619, 170.0]
ORTHO_SCALE_CM = 190.0
RENDER_WIDTH = 1200
RENDER_HEIGHT = 1600
CAMERA_DISTANCE_CM = 420.0

DOC_ROOT = ROOT / "docs/assets/blueprints" / ASSET
REVIEW_ROOT = DOC_ROOT / "review"
MANIFEST_PATH = DOC_ROOT / "manifests/A10_DERIVED_ORTHOGRAPHICS_A01_VALIDATION.json"
BOARD_PATH = REVIEW_ROOT / "A10_DERIVED_ORTHOGRAPHICS_A01_REVIEW.png"
VIEW_PATHS = {
    name: REVIEW_ROOT / f"A10_DERIVED_ORTHOGRAPHICS_A01_{name.upper()}.png"
    for name in ("front", "back", "left", "right", "top", "bottom")
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def bounds_world(obj: bpy.types.Object) -> dict[str, list[float]]:
    points = [obj.matrix_world @ vertex.co for vertex in obj.data.vertices]
    minimum = [min(float(point[axis]) for point in points) for axis in range(3)]
    maximum = [max(float(point[axis]) for point in points) for axis in range(3)]
    dimensions = [maximum[axis] - minimum[axis] for axis in range(3)]
    center = [(minimum[axis] + maximum[axis]) * 0.5 for axis in range(3)]
    return {
        "minimum_cm": minimum,
        "maximum_cm": maximum,
        "dimensions_cm": dimensions,
        "center_cm": center,
    }


def vector_close(observed: list[float], expected: list[float], tolerance: float = 0.00001) -> bool:
    return len(observed) == len(expected) and all(
        abs(float(value) - float(target)) <= tolerance
        for value, target in zip(observed, expected)
    )


def configure_scene() -> None:
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 6.0
    scene.eevee.gtao_factor = 1.25
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.render.image_settings.color_depth = "8"
    scene.render.resolution_x = RENDER_WIDTH
    scene.render.resolution_y = RENDER_HEIGHT
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = False
    scene.world.use_nodes = True
    background = scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
    background.inputs["Strength"].default_value = 0.8
    try:
        scene.view_settings.view_transform = "Standard"
        scene.view_settings.look = "None"
        scene.view_settings.exposure = 0.0
        scene.view_settings.gamma = 1.0
    except Exception:
        pass


def create_camera(name: str, location: tuple[float, float, float], target: list[float]) -> bpy.types.Object:
    data = bpy.data.cameras.new(name)
    data.type = "ORTHO"
    data.ortho_scale = ORTHO_SCALE_CM
    camera = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(camera)
    camera.location = location
    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    return camera


def render_view(camera: bpy.types.Object, path: Path) -> None:
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.filepath = str(path)
    scene.view_layers[0].material_override = None
    bpy.ops.render.render(write_still=True)


def font(size: int) -> ImageFont.ImageFont:
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf",
        "/usr/share/fonts/DejaVuSans.ttf",
    ):
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def fit_panel(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    value = image.convert("RGB")
    resampling = getattr(Image, "Resampling", Image)
    value.thumbnail(size, resampling.LANCZOS)
    panel = Image.new("RGB", size, (245, 243, 238))
    panel.paste(value, ((size[0] - value.width) // 2, (size[1] - value.height) // 2))
    return panel


def compose_board(bounds: dict[str, list[float]]) -> None:
    board = Image.new("RGB", (3300, 3300), (226, 222, 214))
    draw = ImageDraw.Draw(board)
    title_font = font(64)
    subtitle_font = font(34)
    label_font = font(42)
    detail_font = font(28)

    draw.rectangle((0, 0, 3300, 230), fill=(31, 35, 41))
    draw.text((80, 38), "SIEGE BREAKER A10 - DERIVED ORTHOGRAPHICS", font=title_font, fill=(244, 241, 232))
    draw.text(
        (82, 132),
        "UNCHANGED APPROVED A09 BLENDER SOURCE | TRUE ORTHOGRAPHIC | COMMON SCALE 190 CM",
        font=subtitle_font,
        fill=(178, 204, 222),
    )

    layout = [
        ("front", "FRONT  (-Y)"),
        ("back", "BACK  (+Y)"),
        ("left", "LEFT  (-X)"),
        ("right", "RIGHT  (+X)"),
        ("top", "TOP  (+Z)"),
        ("bottom", "BOTTOM  (-Z)"),
    ]
    panel_w, panel_h = 1010, 1380
    image_w, image_h = 950, 1266
    for index, (name, label) in enumerate(layout):
        column = index % 3
        row = index // 3
        x = 70 + column * 1080
        y = 280 + row * 1450
        draw.rounded_rectangle((x, y, x + panel_w, y + panel_h), radius=18, fill=(245, 243, 238), outline=(96, 96, 96), width=3)
        draw.text((x + 30, y + 20), label, font=label_font, fill=(30, 34, 40))
        panel = fit_panel(Image.open(VIEW_PATHS[name]), (image_w, image_h))
        board.paste(panel, (x + 30, y + 90))

    dims = bounds["dimensions_cm"]
    footer = (
        f"APPROVED SOURCE SHA {EXPECTED_BLEND_SHA256[:16]}...  |  "
        f"BOUNDS {dims[0]:.6f} x {dims[1]:.6f} x {dims[2]:.6f} CM  |  "
        "RENDER-ONLY DERIVATION"
    )
    draw.rectangle((0, 3190, 3300, 3300), fill=(31, 35, 41))
    draw.text((70, 3225), footer, font=detail_font, fill=(232, 229, 220))
    board.save(BOARD_PATH)


def main() -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    before_hash = sha256_file(BLEND_PATH)
    if before_hash != EXPECTED_BLEND_SHA256:
        raise RuntimeError(f"approved A09 blend hash mismatch before render: {before_hash}")

    model = bpy.data.objects.get(MODEL_NAME)
    if model is None or model.type != "MESH":
        raise RuntimeError(f"required approved model missing: {MODEL_NAME}")
    if bpy.data.filepath and Path(bpy.data.filepath).resolve() != BLEND_PATH.resolve():
        raise RuntimeError(f"unexpected open blend: {bpy.data.filepath}")

    observed_bounds = bounds_world(model)
    if not vector_close(observed_bounds["dimensions_cm"], EXPECTED_DIMENSIONS_CM):
        raise RuntimeError(f"approved dimensions changed: {observed_bounds['dimensions_cm']}")
    if list(model.location) != [0.0, 0.0, 0.0] or list(model.scale) != [1.0, 1.0, 1.0]:
        raise RuntimeError(f"approved object transform changed: location={list(model.location)} scale={list(model.scale)}")

    configure_scene()
    cx, cy, cz = observed_bounds["center_cm"]
    cameras = {
        "front": create_camera("CAM_A10_FRONT", (cx, cy - CAMERA_DISTANCE_CM, cz), observed_bounds["center_cm"]),
        "back": create_camera("CAM_A10_BACK", (cx, cy + CAMERA_DISTANCE_CM, cz), observed_bounds["center_cm"]),
        "left": create_camera("CAM_A10_LEFT", (cx - CAMERA_DISTANCE_CM, cy, cz), observed_bounds["center_cm"]),
        "right": create_camera("CAM_A10_RIGHT", (cx + CAMERA_DISTANCE_CM, cy, cz), observed_bounds["center_cm"]),
        "top": create_camera("CAM_A10_TOP", (cx, cy, cz + CAMERA_DISTANCE_CM), observed_bounds["center_cm"]),
        "bottom": create_camera("CAM_A10_BOTTOM", (cx, cy, cz - CAMERA_DISTANCE_CM), observed_bounds["center_cm"]),
    }

    for name in ("front", "back", "left", "right", "top", "bottom"):
        render_view(cameras[name], VIEW_PATHS[name])

    compose_board(observed_bounds)
    after_hash = sha256_file(BLEND_PATH)
    if after_hash != before_hash:
        raise RuntimeError(f"approved A09 blend changed during render: {before_hash} -> {after_hash}")

    outputs = {name: str(path.relative_to(ROOT)) for name, path in VIEW_PATHS.items()}
    outputs["review_board"] = str(BOARD_PATH.relative_to(ROOT))
    output_hashes = {name: sha256_file(ROOT / relative) for name, relative in outputs.items()}
    manifest = {
        "schema": "aerathea.siegebreaker.a10_derived_orthographics_validation.v1",
        "asset": ASSET,
        "contract_id": CONTRACT_ID,
        "artifact_status": "candidate derived orthographic review pending Flamestrike decision",
        "authority": {
            "approved_a09_blend": str(BLEND_REL),
            "required_sha256": EXPECTED_BLEND_SHA256,
            "hash_before_render": before_hash,
            "hash_after_render": after_hash,
            "unchanged": before_hash == after_hash,
            "model_object": MODEL_NAME,
        },
        "software": {
            "blender": bpy.app.version_string,
            "image_generation": False,
            "trellis": False,
            "image_to_3d": False,
        },
        "model": {
            "bounds": observed_bounds,
            "location": [float(value) for value in model.location],
            "rotation_euler": [float(value) for value in model.rotation_euler],
            "scale": [float(value) for value in model.scale],
            "vertices": len(model.data.vertices),
            "polygons": len(model.data.polygons),
        },
        "camera_contract": {
            "projection": "ORTHO",
            "common_ortho_scale_cm": ORTHO_SCALE_CM,
            "resolution_px": [RENDER_WIDTH, RENDER_HEIGHT],
            "target_cm": observed_bounds["center_cm"],
            "view_directions": {
                "front": "camera -Y looking +Y",
                "back": "camera +Y looking -Y",
                "left": "camera -X looking +X",
                "right": "camera +X looking -X",
                "top": "camera +Z looking -Z",
                "bottom": "camera -Z looking +Z",
            },
            "cameras": {
                name: {
                    "location_cm": [float(value) for value in camera.location],
                    "rotation_euler_rad": [float(value) for value in camera.rotation_euler],
                    "type": camera.data.type,
                    "ortho_scale_cm": float(camera.data.ortho_scale),
                }
                for name, camera in cameras.items()
            },
        },
        "outputs": outputs,
        "output_hashes": output_hashes,
        "source_file_saved": False,
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "complete", "manifest": str(MANIFEST_PATH), "review": str(BOARD_PATH)}, indent=2))


if __name__ == "__main__":
    main()
