#!/usr/bin/env python3
"""Stage and publish corrected twin-hammer review boards.

The saved DCC candidates are opened read-only for rendering.  This script
does not save either Blender source, create UVs, create textures, export, or
touch Unreal.  It produces one review board per hammer with a full view,
direct strike-face view, and matched topology view.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
BUILD_ID = "TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01"
RENDER_ID = f"{BUILD_ID}_REVIEW_RENDER_A01"
PROOF_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
BUILD_MANIFEST = PROOF_ROOT / f"manifests/{BUILD_ID}_MANIFEST.json"
COMBINED_AUDIT = (
    PROOF_ROOT / f"manifests/{BUILD_ID}_INDEPENDENT_AUDIT.json"
)
FINAL_REVIEW_ROOT = PROOF_ROOT / f"review/{BUILD_ID}"
FINAL_MANIFEST = PROOF_ROOT / f"manifests/{RENDER_ID}_MANIFEST.json"
BLENDER = ROOT / "Tools/External/Blender/blender-4.5.11-linux-x64/blender"
EXPECTED_BLENDER_HASH = (
    "dc72290ee8651c93c4a946c012c5f2a034946fd320e6c3ab214fa23181427428"
)
FACE_SHIFT_DECIMAL = "11.045896821419"

FAILED_SOURCES = {
    "siege_breaker": {
        "path": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "SM_DRW_SiegeBreaker_Hammer_A01_DCCSource_SharedDepth_A01.blend"
        ),
        "sha256": "c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537",
    },
    "foe_hammer": {
        "path": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "SM_DRW_FoeHammer_Hammer_A01_DCCSource_SharedDepth_A01.blend"
        ),
        "sha256": "67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4",
    },
}

ASSETS = {
    "siege_breaker": {
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "display_name": "Siege Breaker",
        "treatment": "Double rune-sided treatment",
        "accent": (42, 133, 230),
        "blend": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A13_R1_CenteredFaceMirrorWeld_DCCSource_A01/"
            "SM_DRW_SiegeBreaker_Hammer_A01_"
            "DCCSource_CenteredFaceMirrorWeld_A01.blend"
        ),
        "audit": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A13_R1_CenteredFaceMirrorWeld_DCCSource_A01/"
            "independent_saved_file_audit.json"
        ),
    },
    "foe_hammer": {
        "asset_id": "SM_DRW_FoeHammer_Hammer_A01",
        "display_name": "Foe Hammer",
        "treatment": "Double metal-center-piece treatment",
        "accent": (189, 119, 48),
        "blend": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A13_R1_CenteredFaceMirrorWeld_DCCSource_A01/"
            "SM_DRW_FoeHammer_Hammer_A01_"
            "DCCSource_CenteredFaceMirrorWeld_A01.blend"
        ),
        "audit": ROOT
        / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A13_R1_CenteredFaceMirrorWeld_DCCSource_A01/"
            "independent_saved_file_audit.json"
        ),
    },
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def panel_names(asset_key: str) -> dict[str, str]:
    asset_id = ASSETS[asset_key]["asset_id"]
    stem = f"{asset_id}_CENTERED_FACE_MIRROR_WELD"
    return {
        "full": f"{stem}_FULL_ASSET_A01.png",
        "end": f"{stem}_END_FACE_A01.png",
        "topology": f"{stem}_TOPOLOGY_A01.png",
        "board": f"{stem}_REVIEW_A01.png",
        "metadata": f"{stem}_RENDER_METADATA_A01.json",
    }


def clear_render_helpers(bpy: Any) -> None:
    for obj in list(bpy.data.objects):
        if obj.type in {"CAMERA", "LIGHT"}:
            bpy.data.objects.remove(obj, do_unlink=True)
    for data in list(bpy.data.cameras):
        if data.users == 0:
            bpy.data.cameras.remove(data)
    for data in list(bpy.data.lights):
        if data.users == 0:
            bpy.data.lights.remove(data)


def add_camera(
    bpy: Any,
    name: str,
    location: tuple[float, float, float],
    target: tuple[float, float, float],
    ortho_scale: float,
) -> Any:
    from mathutils import Vector

    data = bpy.data.cameras.new(name)
    data.type = "ORTHO"
    data.ortho_scale = ortho_scale
    camera = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(camera)
    camera.location = location
    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    return camera


def configure_workbench(bpy: Any) -> None:
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.render.image_settings.color_depth = "8"
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = False
    shading = scene.display.shading
    shading.light = "STUDIO"
    shading.studio_light = "paint.sl"
    shading.use_world_space_lighting = True
    shading.studiolight_intensity = 1.15
    shading.color_type = "MATERIAL"
    shading.background_type = "VIEWPORT"
    shading.background_color = (0.82, 0.81, 0.78)
    shading.show_shadows = True
    shading.shadow_intensity = 0.42
    shading.show_cavity = True
    shading.cavity_type = "BOTH"
    shading.curvature_ridge_factor = 1.6
    shading.curvature_valley_factor = 1.2
    shading.show_object_outline = True
    shading.object_outline_color = (0.025, 0.03, 0.04)
    shading.show_specular_highlight = True
    try:
        scene.view_settings.view_transform = "Standard"
        scene.view_settings.look = "Medium High Contrast"
        scene.view_settings.exposure = 0.0
        scene.view_settings.gamma = 1.0
    except Exception:
        pass


def render(
    bpy: Any,
    camera: Any,
    path: Path,
    width: int,
    height: int,
) -> None:
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def flat_material(
    bpy: Any,
    name: str,
    color: tuple[float, float, float, float],
) -> Any:
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.82
        bsdf.inputs["Metallic"].default_value = 0.05
    return material


def apply_topology_palette(bpy: Any, obj: Any) -> dict[str, Any]:
    original_materials = [slot.material for slot in obj.material_slots]
    original_indices = [polygon.material_index for polygon in obj.data.polygons]
    obj.data.materials.clear()
    palette = (
        (0.18, 0.22, 0.28, 1.0),
        (0.42, 0.49, 0.58, 1.0),
        (0.68, 0.72, 0.76, 1.0),
        (0.32, 0.39, 0.48, 1.0),
    )
    for index, color in enumerate(palette):
        obj.data.materials.append(
            flat_material(bpy, f"A13_TOPOLOGY_{index:02d}", color)
        )
    for polygon in obj.data.polygons:
        signature = (
            polygon.index * 2654435761
            + sum(int(index) for index in polygon.vertices)
        )
        polygon.material_index = signature % len(palette)
    return {
        "materials": original_materials,
        "indices": original_indices,
    }


def restore_materials(obj: Any, state: dict[str, Any]) -> None:
    obj.data.materials.clear()
    for material in state["materials"]:
        obj.data.materials.append(material)
    for polygon, index in zip(obj.data.polygons, state["indices"]):
        polygon.material_index = index


def internal_render(asset_key: str, output_dir: Path) -> int:
    import bpy

    if asset_key not in ASSETS:
        raise RuntimeError(f"Unknown asset key: {asset_key}")
    output_dir.mkdir(parents=True, exist_ok=True)
    asset = ASSETS[asset_key]
    names = panel_names(asset_key)
    mesh_objects = [
        obj for obj in bpy.context.scene.objects if obj.type == "MESH"
    ]
    if len(mesh_objects) != 1:
        raise RuntimeError(
            f"Expected exactly one mesh object, found {len(mesh_objects)}"
        )
    obj = mesh_objects[0]
    clear_render_helpers(bpy)
    configure_workbench(bpy)

    hero_camera = add_camera(
        bpy,
        "A13_REVIEW_FULL_CAMERA",
        (250.0, -315.0, 215.0),
        (0.0, 0.0, 86.0),
        196.0,
    )
    end_camera = add_camera(
        bpy,
        "A13_REVIEW_END_CAMERA",
        (320.0, 0.0, 132.0),
        (0.0, 0.0, 132.0),
        84.0,
    )

    render(
        bpy,
        hero_camera,
        output_dir / names["full"],
        900,
        1300,
    )
    render(
        bpy,
        end_camera,
        output_dir / names["end"],
        900,
        900,
    )

    topology_state = apply_topology_palette(bpy, obj)
    render(
        bpy,
        end_camera,
        output_dir / names["topology"],
        900,
        900,
    )
    restore_materials(obj, topology_state)

    metadata = {
        "schema": "AERATHEA_TWIN_HAMMER_CENTERED_FACE_REVIEW_RENDER_METADATA_A01_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "build_id": BUILD_ID,
        "render_id": RENDER_ID,
        "asset_key": asset_key,
        "asset_id": asset["asset_id"],
        "artifact_status": "proof only; staged for internal visual inspection",
        "mesh_object_count": len(mesh_objects),
        "source_save_operator_invoked": False,
        "geometry_modified_in_saved_source": False,
        "uv_or_texture_created": False,
        "camera_views": {
            "full_asset": {
                "location_cm": list(hero_camera.location),
                "target_cm": [0.0, 0.0, 86.0],
                "orthographic_scale_cm": 196.0,
            },
            "positive_x_end_face": {
                "location_cm": list(end_camera.location),
                "target_cm": [0.0, 0.0, 132.0],
                "orthographic_scale_cm": 84.0,
            },
            "topology": "matched positive-X end-face camera; temporary face-partition palette",
        },
        "outputs": {
            key: {
                "filename": names[key],
                "sha256": sha256(output_dir / names[key]),
            }
            for key in ("full", "end", "topology")
        },
        "result": "PASS",
    }
    write_json(output_dir / names["metadata"], metadata)
    print(
        json.dumps(
            {
                "asset": asset["asset_id"],
                "result": "PASS",
                "outputs": metadata["outputs"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def font(size: int, bold: bool = False) -> Any:
    from PIL import ImageFont

    candidates = (
        (
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
            if bold
            else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        ),
        (
            "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf"
            if bold
            else "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf"
        ),
        (
            "/usr/share/fonts/DejaVuSans-Bold.ttf"
            if bold
            else "/usr/share/fonts/DejaVuSans.ttf"
        ),
    )
    for path in candidates:
        if Path(path).is_file():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def fit_image(image: Any, box: tuple[int, int], background: tuple[int, int, int]) -> Any:
    from PIL import Image

    value = image.convert("RGB")
    resampling = getattr(Image, "Resampling", Image)
    value.thumbnail(box, resampling.LANCZOS)
    panel = Image.new("RGB", box, background)
    panel.paste(
        value,
        ((box[0] - value.width) // 2, (box[1] - value.height) // 2),
    )
    return panel


def compose_board(asset_key: str, staging_dir: Path) -> Path:
    from PIL import Image, ImageDraw

    asset = ASSETS[asset_key]
    names = panel_names(asset_key)
    audit = load_json(asset["audit"])
    topology = audit["topology"]
    canvas = Image.new("RGB", (3100, 1760), (229, 226, 218))
    draw = ImageDraw.Draw(canvas)
    accent = asset["accent"]
    navy = (22, 30, 42)
    ink = (31, 36, 43)
    muted = (92, 98, 105)
    paper = (247, 246, 242)
    line = (194, 190, 181)

    draw.rectangle((0, 0, 3100, 168), fill=navy)
    draw.rectangle((0, 164, 3100, 174), fill=accent)
    draw.text(
        (64, 34),
        f"{asset['display_name']} — Centered Face, Mirror + Weld",
        fill=(248, 248, 246),
        font=font(54, bold=True),
    )
    draw.text(
        (67, 105),
        "DCC SOURCE CANDIDATE  •  VISUAL REVIEW REQUIRED",
        fill=(202, 209, 218),
        font=font(28, bold=True),
    )
    draw.rounded_rectangle(
        (2465, 48, 3025, 128),
        radius=20,
        fill=(35, 111, 74),
    )
    draw.text(
        (2520, 69),
        "SAVED-FILE AUDIT: PASS",
        fill=(243, 250, 246),
        font=font(25, bold=True),
    )

    panel_x = (55, 1055, 2055)
    panel_width = 990
    panel_top = 215
    panel_bottom = 1588
    for x in panel_x:
        draw.rounded_rectangle(
            (x, panel_top, x + panel_width, panel_bottom),
            radius=24,
            fill=paper,
            outline=line,
            width=3,
        )

    headings = (
        "FULL ASSET / FRESH BUILD",
        "+X STRIKE FACE / CENTERED + WELDED",
        "MATCHED TOPOLOGY VIEW",
    )
    for x, heading in zip(panel_x, headings):
        draw.text(
            (x + 30, panel_top + 28),
            heading,
            fill=ink,
            font=font(27, bold=True),
        )
        draw.line(
            (x + 30, panel_top + 76, x + panel_width - 30, panel_top + 76),
            fill=line,
            width=2,
        )

    full_image = fit_image(
        Image.open(staging_dir / names["full"]),
        (900, 1210),
        (220, 218, 211),
    )
    end_image = fit_image(
        Image.open(staging_dir / names["end"]),
        (900, 900),
        (220, 218, 211),
    )
    topology_image = fit_image(
        Image.open(staging_dir / names["topology"]),
        (900, 900),
        (220, 218, 211),
    )
    canvas.paste(full_image, (100, 320))
    canvas.paste(end_image, (1100, 320))
    canvas.paste(topology_image, (2100, 320))

    body_font = font(26)
    body_bold = font(26, bold=True)
    draw.text(
        (1090, 1245),
        f"Face translation: +{FACE_SHIFT_DECIMAL} cm on Z",
        fill=ink,
        font=body_bold,
    )
    draw.text(
        (1090, 1292),
        "Shared-body perimeter controls containment",
        fill=muted,
        font=body_font,
    )
    draw.text(
        (1090, 1339),
        asset["treatment"],
        fill=accent,
        font=body_bold,
    )
    draw.text(
        (1090, 1386),
        "One positive-X half • exact X=0 mirror • seam welded",
        fill=muted,
        font=body_font,
    )
    draw.text(
        (1090, 1433),
        "No copied-and-rotated second half",
        fill=muted,
        font=body_font,
    )

    metrics = (
        f"Open boundary edges: {topology['open_boundary_edges']}",
        (
            "Edges with >2 faces: "
            f"{topology['edge_incidence_greater_than_two']}"
        ),
        f"Winding mismatches: {topology['winding_mismatch_edges']}",
        f"Loose / zero-area / duplicate: {topology['loose_edges']} / "
        f"{topology['zero_area_faces']} / {topology['duplicate_faces']}",
        (
            "Unwelded center-seam vertices: "
            f"{topology['center_seam_unwelded_vertices']}"
        ),
        f"Geometry hash: {topology['geometry_sha256'][:16]}…",
    )
    for index, value in enumerate(metrics):
        draw.text(
            (2090, 1243 + index * 46),
            value,
            fill=ink if index < 5 else muted,
            font=body_bold if index < 5 else body_font,
        )

    draw.rectangle((0, 1625, 3100, 1760), fill=navy)
    draw.text(
        (62, 1654),
        (
            "Proof only • No failed-source geometry read • No UV/texture "
            "production • No export or Unreal work"
        ),
        fill=(224, 228, 232),
        font=font(27, bold=True),
    )
    draw.text(
        (62, 1705),
        (
            "Decision requested: approve, reject, or describe the end-face "
            "alignment/perimeter change you want."
        ),
        fill=(174, 184, 196),
        font=font(24),
    )

    board = staging_dir / names["board"]
    canvas.save(board, "PNG", optimize=True)
    return board


def blender_command(
    asset_key: str,
    blend: Path,
    output_dir: Path,
) -> list[str]:
    return [
        str(BLENDER),
        "--background",
        "--factory-startup",
        str(blend),
        "--python",
        str(Path(__file__).resolve()),
        "--",
        "--internal-render",
        "--asset-key",
        asset_key,
        "--output-dir",
        str(output_dir),
    ]


def verify_authority() -> tuple[dict[str, Any], dict[str, Any]]:
    if sha256(BLENDER) != EXPECTED_BLENDER_HASH:
        raise RuntimeError("Blender hash mismatch")
    build = load_json(BUILD_MANIFEST)
    audit = load_json(COMBINED_AUDIT)
    if build["result"] != "PRE_SAVE_PASS":
        raise RuntimeError("Fresh build manifest is not PRE_SAVE_PASS")
    if audit["result"] != "PASS":
        raise RuntimeError("Independent twin-hammer audit is not PASS")
    for asset_key, asset in ASSETS.items():
        if sha256(asset["blend"]) != build["assets"][asset_key]["blend"]["sha256"]:
            raise RuntimeError(f"Candidate hash mismatch for {asset_key}")
        individual = load_json(asset["audit"])
        if individual["result"] != "PASS":
            raise RuntimeError(f"Individual saved-file audit failed: {asset_key}")
    for asset_key, record in FAILED_SOURCES.items():
        if sha256(record["path"]) != record["sha256"]:
            raise RuntimeError(f"Failed source hash drift: {asset_key}")
    return build, audit


def render_staging(staging_dir: Path) -> int:
    if not staging_dir.is_dir():
        raise RuntimeError(f"Staging directory does not exist: {staging_dir}")
    if any(staging_dir.iterdir()):
        raise RuntimeError(f"Staging directory is not empty: {staging_dir}")
    if FINAL_REVIEW_ROOT.exists() or FINAL_MANIFEST.exists():
        raise RuntimeError("Final review output path already exists")
    build, audit = verify_authority()
    candidate_hashes_before = {
        key: sha256(asset["blend"]) for key, asset in ASSETS.items()
    }
    failed_hashes_before = {
        key: sha256(record["path"])
        for key, record in FAILED_SOURCES.items()
    }
    environment = dict(os.environ)
    environment["PYTHONHASHSEED"] = "0"
    for asset_key, asset in ASSETS.items():
        subprocess.run(
            blender_command(asset_key, asset["blend"], staging_dir),
            cwd=ROOT,
            env=environment,
            check=True,
        )
        compose_board(asset_key, staging_dir)

    candidate_hashes_after = {
        key: sha256(asset["blend"]) for key, asset in ASSETS.items()
    }
    failed_hashes_after = {
        key: sha256(record["path"])
        for key, record in FAILED_SOURCES.items()
    }
    if candidate_hashes_after != candidate_hashes_before:
        raise RuntimeError("A saved candidate changed during rendering")
    if failed_hashes_after != failed_hashes_before:
        raise RuntimeError("A failed source changed during rendering")

    outputs: dict[str, Any] = {}
    for asset_key in ASSETS:
        names = panel_names(asset_key)
        outputs[asset_key] = {
            key: {
                "filename": names[key],
                "sha256": sha256(staging_dir / names[key]),
            }
            for key in ("full", "end", "topology", "board", "metadata")
        }
    manifest = {
        "schema": "AERATHEA_TWIN_HAMMER_CENTERED_FACE_REVIEW_STAGING_A01_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "build_id": BUILD_ID,
        "render_id": RENDER_ID,
        "artifact_status": "proof only; staged for internal visual inspection",
        "renderer": {
            "path": relative(Path(__file__).resolve()),
            "sha256": sha256(Path(__file__).resolve()),
        },
        "build_manifest": {
            "path": relative(BUILD_MANIFEST),
            "sha256": sha256(BUILD_MANIFEST),
            "result": build["result"],
        },
        "independent_audit": {
            "path": relative(COMBINED_AUDIT),
            "sha256": sha256(COMBINED_AUDIT),
            "result": audit["result"],
        },
        "candidate_hashes_before": candidate_hashes_before,
        "candidate_hashes_after": candidate_hashes_after,
        "failed_source_hashes_before": failed_hashes_before,
        "failed_source_hashes_after": failed_hashes_after,
        "source_save_operator_invoked": False,
        "uv_or_texture_created": False,
        "outputs": outputs,
        "result": "STAGING_PASS",
    }
    write_json(staging_dir / "STAGING_MANIFEST.json", manifest)
    print(
        json.dumps(
            {
                "result": "STAGING_PASS",
                "staging_dir": str(staging_dir),
                "boards": {
                    key: str(staging_dir / panel_names(key)["board"])
                    for key in ASSETS
                },
                "next_gate": "internal visual inspection before publish",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def publish(staging_dir: Path) -> int:
    if FINAL_REVIEW_ROOT.exists() or FINAL_MANIFEST.exists():
        raise RuntimeError("Final review output path already exists")
    verify_authority()
    staging_manifest_path = staging_dir / "STAGING_MANIFEST.json"
    staging = load_json(staging_manifest_path)
    if staging["result"] != "STAGING_PASS":
        raise RuntimeError("Staging manifest is not PASS")
    if staging["renderer"]["sha256"] != sha256(Path(__file__).resolve()):
        raise RuntimeError("Renderer changed after staging")
    for asset_key, records in staging["outputs"].items():
        for record in records.values():
            path = staging_dir / record["filename"]
            if sha256(path) != record["sha256"]:
                raise RuntimeError(f"Staged output hash mismatch: {path}")
    for asset_key, expected in staging["candidate_hashes_after"].items():
        if sha256(ASSETS[asset_key]["blend"]) != expected:
            raise RuntimeError(f"Candidate changed after staging: {asset_key}")
    for asset_key, expected in staging["failed_source_hashes_after"].items():
        if sha256(FAILED_SOURCES[asset_key]["path"]) != expected:
            raise RuntimeError(f"Failed source changed after staging: {asset_key}")

    FINAL_REVIEW_ROOT.mkdir(parents=True, exist_ok=False)
    final_outputs: dict[str, Any] = {}
    for asset_key, records in staging["outputs"].items():
        final_outputs[asset_key] = {}
        for key, record in records.items():
            source = staging_dir / record["filename"]
            destination = FINAL_REVIEW_ROOT / record["filename"]
            shutil.copy2(source, destination)
            final_outputs[asset_key][key] = {
                "path": relative(destination),
                "sha256": sha256(destination),
            }
    final_manifest = {
        **staging,
        "schema": "AERATHEA_TWIN_HAMMER_CENTERED_FACE_REVIEW_RENDER_A01_V1",
        "date_utc": utc_now(),
        "artifact_status": "proof only; pending Flamestrike visual review",
        "review_root": relative(FINAL_REVIEW_ROOT),
        "outputs": final_outputs,
        "visible_review_required": True,
        "flamestrike_decision": "pending",
        "result": "PASS",
    }
    write_json(FINAL_MANIFEST, final_manifest)
    print(
        json.dumps(
            {
                "result": "PASS",
                "manifest": relative(FINAL_MANIFEST),
                "boards": {
                    key: records["board"]["path"]
                    for key, records in final_outputs.items()
                },
                "next_gate": "open both boards visibly and stop",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--internal-render", action="store_true")
    parser.add_argument("--render-staging", action="store_true")
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--asset-key")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--staging-dir", type=Path)
    arguments = (
        sys.argv[sys.argv.index("--") + 1 :]
        if "--" in sys.argv
        else None
    )
    args = parser.parse_args(arguments)
    if args.internal_render:
        if not args.asset_key or args.output_dir is None:
            raise RuntimeError("Internal render needs asset key and output dir")
        return internal_render(args.asset_key, args.output_dir)
    if args.render_staging:
        if args.staging_dir is None:
            raise RuntimeError("Staging render needs --staging-dir")
        return render_staging(args.staging_dir)
    if args.publish:
        if args.staging_dir is None:
            raise RuntimeError("Publish needs --staging-dir")
        return publish(args.staging_dir)
    raise RuntimeError("Choose --render-staging, --publish, or --internal-render")


if __name__ == "__main__":
    raise SystemExit(main())
