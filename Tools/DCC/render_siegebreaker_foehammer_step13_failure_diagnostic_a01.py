#!/usr/bin/env python3
"""Read-only topology-problem renders for the failed Step 13 hammer sources.

The Blender portion opens each locked source, renders a normal three-quarter
view, adds temporary issue-line curves in memory, and renders the same view
again.  It never calls a Blender save operator.  The host-side portion packages
one plain-English diagnostic board per hammer and records source hashes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import struct
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
DIAGNOSTIC_ID = "STEP_13_TECHNICAL_FAIL_DIAGNOSTIC_RENDER_A01"
PROOF_ROOT = ROOT / (
    "docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/"
    "SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02"
)
APPROVAL = (
    PROOF_ROOT
    / "steps/STEP_13_TECHNICAL_FAIL_DIAGNOSTIC_RENDER_A01_APPROVAL_RECORD.md"
)
STEP_STATE = PROOF_ROOT / "manifests/STEP_STATE.json"
TECHNICAL_AUDIT = (
    PROOF_ROOT
    / "manifests/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_TECHNICAL_AUDIT.json"
)
OUTPUT_ROOT = (
    PROOF_ROOT / "review/STEP_13_TECHNICAL_FAIL_DIAGNOSTIC_A01"
)
RAW_ROOT = OUTPUT_ROOT / "raw"
MANIFEST = (
    PROOF_ROOT
    / "manifests/STEP_13_TECHNICAL_FAIL_DIAGNOSTIC_RENDER_A01.json"
)
BLENDER = ROOT / "Tools/External/Blender/blender-4.5.11-linux-x64/blender"

EXPECTED_APPROVAL_HASH = (
    "8e7e63b621c91f855c3006ef2cb40447a397463729f5725f299703ec382d32a1"
)
EXPECTED_TECHNICAL_AUDIT_HASH = (
    "e1c2e6bcbc4f2cf7b7ff991c8ea8fa25f72ecf2ae4913683b1d9ba1ab1a945ad"
)
EXPECTED_BLENDER_HASH = (
    "dc72290ee8651c93c4a946c012c5f2a034946fd320e6c3ab214fa23181427428"
)

ASSETS = {
    "siege_breaker": {
        "asset_id": "SM_DRW_SiegeBreaker_Hammer_A01",
        "display_name": "SIEGE BREAKER",
        "treatment": "DOUBLE-RUNE-SIDED",
        "blend": ROOT / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_SiegeBreaker_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "SM_DRW_SiegeBreaker_Hammer_A01_DCCSource_SharedDepth_A01.blend"
        ),
        "sha256": "c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537",
        "expected": {
            "unpaired_boundary_edges": 19200,
            "overloaded_boundary_edges": 890,
            "local_c04_winding_edges": 276,
            "local_c04_winding_per_occurrence": 138,
        },
    },
    "foe_hammer": {
        "asset_id": "SM_DRW_FoeHammer_Hammer_A01",
        "display_name": "FOE HAMMER",
        "treatment": "DOUBLE-METAL-CENTER-PIECE-SIDED",
        "blend": ROOT / (
            "SourceAssets/Blender/Weapons/Dwarven/"
            "SM_DRW_FoeHammer_Hammer_A01/"
            "A12_R10_R8_SharedDepth_DCCSource_A01/"
            "SM_DRW_FoeHammer_Hammer_A01_DCCSource_SharedDepth_A01.blend"
        ),
        "sha256": "67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4",
        "expected": {
            "unpaired_boundary_edges": 18900,
            "overloaded_boundary_edges": 890,
            "local_c04_winding_edges": 236,
            "local_c04_winding_per_occurrence": 118,
        },
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


def coordinate_bytes(point: tuple[float, float, float]) -> bytes:
    return struct.pack(">ddd", *point)


def decode_coordinate(value: bytes) -> tuple[float, float, float]:
    return struct.unpack(">ddd", value)


def verify_authority() -> dict[str, Any]:
    checks = {
        "approval_record_hash_matches": sha256(APPROVAL)
        == EXPECTED_APPROVAL_HASH,
        "technical_audit_hash_matches": sha256(TECHNICAL_AUDIT)
        == EXPECTED_TECHNICAL_AUDIT_HASH,
        "blender_hash_matches": sha256(BLENDER) == EXPECTED_BLENDER_HASH,
    }
    audit = load_json(TECHNICAL_AUDIT)
    state = load_json(STEP_STATE)
    boundary = state.get("step_13_technical_fail_diagnostic_render_a01", {})
    checks.update(
        {
            "technical_audit_is_fail": audit.get("result") == "FAIL",
            "diagnostic_approval_record_matches_state": boundary.get(
                "approval_record_sha256"
            )
            == EXPECTED_APPROVAL_HASH,
            "diagnostic_decision_approved": boundary.get(
                "flamestrike_decision"
            )
            == "approved",
            "read_only_blender_authority_true": bool(
                boundary.get("read_only_blender_diagnostic_authority")
            ),
            "source_save_authority_false": not bool(
                boundary.get("source_save_authority")
            ),
            "geometry_modification_authority_false": not bool(
                boundary.get("geometry_modification_authority")
            ),
            "repair_or_rebuild_authority_false": not bool(
                boundary.get("repair_or_rebuild_authority")
            ),
            "mirror_and_weld_authority_false": not bool(
                boundary.get("mirror_and_weld_authority")
            ),
            "step_14_authority_false": not bool(
                boundary.get("step_14_authority")
            ),
            "unreal_authority_false": not bool(
                boundary.get("export_or_unreal_authority")
            ),
        }
    )
    for asset_key, asset in ASSETS.items():
        checks[f"{asset_key}_source_hash_matches"] = (
            sha256(asset["blend"]) == asset["sha256"]
        )
    if not all(checks.values()):
        failed = [key for key, value in checks.items() if not value]
        raise RuntimeError(f"Diagnostic authority failed: {failed}")
    return {
        "approval_record": {
            "path": relative(APPROVAL),
            "sha256": sha256(APPROVAL),
        },
        "technical_audit": {
            "path": relative(TECHNICAL_AUDIT),
            "sha256": sha256(TECHNICAL_AUDIT),
            "result": audit["result"],
        },
        "step_state": {
            "path": relative(STEP_STATE),
            "sha256_at_preflight": sha256(STEP_STATE),
        },
        "blender": {
            "path": relative(BLENDER),
            "sha256": sha256(BLENDER),
        },
        "checks": checks,
    }


def world_points(obj: Any) -> list[tuple[float, float, float]]:
    return [
        tuple(float(value) for value in (obj.matrix_world @ vertex.co))
        for vertex in obj.data.vertices
    ]


def collect_issue_segments(
    objects: list[Any],
) -> dict[str, list[tuple[tuple[float, float, float], tuple[float, float, float]]]]:
    import bmesh

    assembly_boundary: dict[
        tuple[bytes, bytes], list[tuple[str, str]]
    ] = defaultdict(list)
    c04_winding: list[
        tuple[tuple[float, float, float], tuple[float, float, float]]
    ] = []

    for obj in objects:
        points = world_points(obj)
        point_keys = [coordinate_bytes(point) for point in points]
        bm = bmesh.new()
        bm.from_mesh(obj.data)
        bm.verts.ensure_lookup_table()
        bm.edges.ensure_lookup_table()
        bm.verts.index_update()
        bm.normal_update()
        is_c04_closure = (
            obj.get("Aerathea.Component") == "C04_LOCAL_TREATMENT"
            and obj.get("Aerathea.EquationId")
            == "EQ_RULED_C04_TO_SHARED_BODY_BOUNDARIES"
        )
        for edge in bm.edges:
            linked = len(edge.link_faces)
            if linked == 1:
                start = point_keys[edge.verts[0].index]
                end = point_keys[edge.verts[1].index]
                key = (start, end) if start <= end else (end, start)
                assembly_boundary[key].append((obj.name, str(linked)))
            elif (
                linked == 2
                and is_c04_closure
                and not edge.is_contiguous
            ):
                c04_winding.append(
                    (
                        points[edge.verts[0].index],
                        points[edge.verts[1].index],
                    )
                )
        bm.free()

    unpaired = [
        (decode_coordinate(key[0]), decode_coordinate(key[1]))
        for key, participants in assembly_boundary.items()
        if len(participants) == 1
    ]
    overloaded = [
        (decode_coordinate(key[0]), decode_coordinate(key[1]))
        for key, participants in assembly_boundary.items()
        if len(participants) > 2
    ]
    return {
        "unpaired": unpaired,
        "overloaded": overloaded,
        "c04_winding": c04_winding,
    }


def create_issue_curve(
    bpy: Any,
    name: str,
    segments: list[
        tuple[tuple[float, float, float], tuple[float, float, float]]
    ],
    color: tuple[float, float, float, float],
    bevel_depth: float,
) -> Any:
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 1
    curve.bevel_depth = bevel_depth
    curve.bevel_resolution = 0
    curve.resolution_v = 0
    for start, end in segments:
        spline = curve.splines.new("POLY")
        spline.points.add(1)
        spline.points[0].co = (*start, 1.0)
        spline.points[1].co = (*end, 1.0)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.scene.collection.objects.link(obj)
    obj.color = color
    obj.show_in_front = True
    obj["Aerathea.DiagnosticOnly"] = True
    obj["Aerathea.NotProductionGeometry"] = True
    return obj


def configure_scene(bpy: Any) -> None:
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_WORKBENCH_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_WORKBENCH"
    scene.render.resolution_x = 720
    scene.render.resolution_y = 900
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.render.film_transparent = False
    scene.display.shading.light = "STUDIO"
    scene.display.shading.studio_light = "paint.sl"
    scene.display.shading.color_type = "MATERIAL"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "WORLD"
    scene.display.shading.curvature_ridge_factor = 1.5
    scene.display.shading.curvature_valley_factor = 1.2
    scene.display.shading.show_specular_highlight = True
    scene.world.color = (0.012, 0.017, 0.024)


def look_at(camera: Any, target: tuple[float, float, float]) -> None:
    from mathutils import Vector

    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def create_camera(bpy: Any) -> Any:
    target = (0.0, 0.0, 85.0)
    direction = (1.0, -1.35, 0.58)
    length = math.sqrt(sum(value * value for value in direction))
    unit = tuple(value / length for value in direction)
    camera_data = bpy.data.cameras.new("CAM_DIAGNOSTIC_MATCHED_3Q")
    camera_data.type = "ORTHO"
    camera_data.ortho_scale = 225.0
    camera = bpy.data.objects.new("CAM_DIAGNOSTIC_MATCHED_3Q", camera_data)
    bpy.context.scene.collection.objects.link(camera)
    camera.location = tuple(
        target[index] + unit[index] * 420.0 for index in range(3)
    )
    look_at(camera, target)
    bpy.context.scene.camera = camera
    return camera


def render_still(bpy: Any, output: Path) -> None:
    bpy.context.scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)


def internal_render(asset_key: str) -> int:
    import bpy

    asset = ASSETS[asset_key]
    source_hash_before = sha256(asset["blend"])
    if source_hash_before != asset["sha256"]:
        raise RuntimeError(f"Source hash mismatch before render: {asset_key}")
    if Path(bpy.data.filepath).resolve() != asset["blend"].resolve():
        raise RuntimeError(f"Wrong Blender source loaded: {bpy.data.filepath}")

    objects = sorted(
        (obj for obj in bpy.data.objects if obj.type == "MESH"),
        key=lambda item: item.name,
    )
    segments = collect_issue_segments(objects)
    observed = {
        "unpaired_boundary_edges": len(segments["unpaired"]),
        "overloaded_boundary_edges": len(segments["overloaded"]),
        "local_c04_winding_edges": len(segments["c04_winding"]),
    }
    expected = asset["expected"]
    for key in observed:
        if observed[key] != expected[key]:
            raise RuntimeError(
                f"{asset_key} {key}: observed {observed[key]}, "
                f"expected {expected[key]}"
            )

    asset_raw_root = RAW_ROOT / asset_key
    asset_raw_root.mkdir(parents=True, exist_ok=True)
    normal_path = asset_raw_root / f"{asset['asset_id']}_NORMAL_3Q.png"
    issue_path = asset_raw_root / f"{asset['asset_id']}_ISSUES_3Q.png"

    configure_scene(bpy)
    create_camera(bpy)
    bpy.context.scene.display.shading.color_type = "MATERIAL"
    render_still(bpy, normal_path)

    for obj in objects:
        obj.color = (0.26, 0.30, 0.36, 1.0)
    bpy.context.scene.display.shading.color_type = "OBJECT"
    create_issue_curve(
        bpy,
        "DIAG_UNPAIRED_EXACT_BOUNDARIES_RED",
        segments["unpaired"],
        (1.0, 0.025, 0.035, 1.0),
        0.115,
    )
    create_issue_curve(
        bpy,
        "DIAG_OVERLOADED_BOUNDARIES_YELLOW",
        segments["overloaded"],
        (1.0, 0.63, 0.01, 1.0),
        0.18,
    )
    create_issue_curve(
        bpy,
        "DIAG_C04_WINDING_ERRORS_MAGENTA",
        segments["c04_winding"],
        (1.0, 0.0, 0.72, 1.0),
        0.25,
    )
    render_still(bpy, issue_path)

    source_hash_after = sha256(asset["blend"])
    if source_hash_after != source_hash_before:
        raise RuntimeError(f"Source changed during render: {asset_key}")
    report = {
        "asset_key": asset_key,
        "asset_id": asset["asset_id"],
        "artifact_status": "proof only; technical-failure diagnostic",
        "source": {
            "path": relative(asset["blend"]),
            "sha256_before": source_hash_before,
            "sha256_after": source_hash_after,
            "byte_identical": source_hash_before == source_hash_after,
        },
        "observed_issue_counts": observed,
        "expected_issue_counts": expected,
        "raw_renders": {
            "normal": {
                "path": relative(normal_path),
                "sha256": sha256(normal_path),
            },
            "issues": {
                "path": relative(issue_path),
                "sha256": sha256(issue_path),
            },
        },
        "camera": {
            "type": "ORTHO",
            "direction": [1.0, -1.35, 0.58],
            "target_cm": [0.0, 0.0, 85.0],
            "ortho_scale_cm": 225.0,
            "resolution_px": [720, 900],
        },
        "overlay_legend": {
            "red": "exact saved panel boundary edge with no matching partner",
            "yellow": "exact saved boundary edge used by more than two panels",
            "magenta": "directly observed local-C04 face-winding error",
        },
        "temporary_overlay_geometry_saved_to_source": False,
        "source_save_operator_invoked": False,
        "geometry_repaired_or_rebuilt": False,
        "result": "PASS",
    }
    write_json(asset_raw_root / "render_report.json", report)
    print(
        json.dumps(
            {
                "asset": asset["asset_id"],
                "result": report["result"],
                "observed_issue_counts": observed,
                "source_byte_identical": report["source"][
                    "byte_identical"
                ],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def resample_filter() -> int:
    from PIL import Image

    if hasattr(Image, "Resampling"):
        return Image.Resampling.LANCZOS
    if hasattr(Image, "LANCZOS"):
        return Image.LANCZOS
    return Image.ANTIALIAS


def compose_board(asset_key: str, report: dict[str, Any]) -> Path:
    from PIL import Image, ImageDraw, ImageFont

    asset = ASSETS[asset_key]
    normal = Image.open(
        ROOT / report["raw_renders"]["normal"]["path"]
    ).convert("RGB")
    issues = Image.open(
        ROOT / report["raw_renders"]["issues"]["path"]
    ).convert("RGB")
    if normal.size != (720, 900) or issues.size != (720, 900):
        raise RuntimeError(f"Unexpected raw render size for {asset_key}")

    width = 1580
    height = 1280
    board = Image.new("RGB", (width, height), (13, 18, 25))
    draw = ImageDraw.Draw(board)
    font_root = Path("/usr/share/fonts/truetype/dejavu")
    title = ImageFont.truetype(
        str(font_root / "DejaVuSans-Bold.ttf"), 38
    )
    subtitle = ImageFont.truetype(
        str(font_root / "DejaVuSans-Bold.ttf"), 21
    )
    body = ImageFont.truetype(
        str(font_root / "DejaVuSans.ttf"), 18
    )
    body_bold = ImageFont.truetype(
        str(font_root / "DejaVuSans-Bold.ttf"), 18
    )
    small = ImageFont.truetype(
        str(font_root / "DejaVuSans.ttf"), 15
    )

    draw.rectangle((0, 0, width, 112), fill=(91, 27, 34))
    draw.text(
        (45, 20),
        f"{asset['display_name']} — SAVED-MESH PROBLEM VIEW",
        font=title,
        fill=(255, 255, 255),
    )
    draw.text(
        (47, 72),
        f"{asset['treatment']}  •  PROOF ONLY  •  NO REPAIR PERFORMED",
        font=body_bold,
        fill=(255, 205, 208),
    )

    draw.text(
        (45, 126),
        "NORMAL SHADED VIEW",
        font=subtitle,
        fill=(226, 233, 240),
    )
    draw.text(
        (815, 126),
        "SAME CAMERA — FAULTY JOINS HIGHLIGHTED",
        font=subtitle,
        fill=(255, 184, 190),
    )
    board.paste(normal, (45, 160))
    board.paste(issues, (815, 160))
    draw.rectangle((45, 160, 764, 1059), outline=(72, 88, 106), width=2)
    draw.rectangle((815, 160, 1534, 1059), outline=(113, 62, 68), width=2)

    # Keep the explanation below both renders so it cannot hide hammer geometry.
    legend_y = 1080
    draw.rectangle((832, legend_y, 1517, 1235), fill=(10, 14, 20))
    legend = [
        ((255, 25, 32), "RED", "panel edge with no exact partner"),
        ((255, 170, 20), "YELLOW", "edge used by more than two panels"),
        ((255, 15, 188), "MAGENTA", "reversed C04 face-to-face winding"),
    ]
    y = legend_y + 13
    for color, label, meaning in legend:
        draw.rectangle((848, y + 3, 866, y + 21), fill=color)
        draw.text((876, y), label, font=body_bold, fill=color)
        draw.text((1015, y), meaning, font=body, fill=(222, 229, 236))
        y += 39

    counts = report["observed_issue_counts"]
    draw.rectangle((62, 1080, 746, 1235), fill=(10, 14, 20))
    draw.text(
        (78, 1094),
        "WHAT THE SAVED FILE CONTAINS",
        font=body_bold,
        fill=(255, 195, 199),
    )
    draw.text(
        (78, 1125),
        f"{counts['unpaired_boundary_edges']:,} exact panel edges have no partner",
        font=body,
        fill=(242, 104, 111),
    )
    draw.text(
        (78, 1154),
        f"{counts['overloaded_boundary_edges']:,} exact edges are used by 3+ panels",
        font=body,
        fill=(255, 185, 72),
    )
    draw.text(
        (78, 1183),
        (
            f"{asset['expected']['local_c04_winding_per_occurrence']} "
            "reversed-winding joins on each C04 side"
        ),
        font=body,
        fill=(255, 96, 210),
    )

    draw.text(
        (45, 1250),
        (
            "The normal render can look solid because panels overlap or touch. "
            "The colored lines show the saved connectivity problem directly."
        ),
        font=small,
        fill=(151, 164, 177),
    )
    output = OUTPUT_ROOT / (
        f"{asset['asset_id']}_TECHNICAL_FAIL_DIAGNOSTIC_A01.png"
    )
    board.save(output, format="PNG", optimize=True)
    return output


def external_render_all() -> int:
    authority = verify_authority()
    if OUTPUT_ROOT.exists() or MANIFEST.exists():
        raise RuntimeError("Fresh diagnostic output path already exists")
    RAW_ROOT.mkdir(parents=True, exist_ok=False)
    source_hashes_before = {
        key: sha256(asset["blend"]) for key, asset in ASSETS.items()
    }
    environment = dict(os.environ)
    environment["PYTHONHASHSEED"] = "0"
    for asset_key, asset in ASSETS.items():
        command = [
            str(BLENDER),
            "--background",
            "--factory-startup",
            str(asset["blend"]),
            "--python",
            str(Path(__file__).resolve()),
            "--",
            "--internal-render",
            asset_key,
        ]
        subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            check=True,
        )

    asset_outputs: dict[str, Any] = {}
    for asset_key, asset in ASSETS.items():
        report_path = RAW_ROOT / asset_key / "render_report.json"
        report = load_json(report_path)
        if report["result"] != "PASS":
            raise RuntimeError(f"Raw render report failed: {asset_key}")
        if report["source"]["sha256_before"] != source_hashes_before[
            asset_key
        ]:
            raise RuntimeError(f"Pre-render source hash drift: {asset_key}")
        final_board = compose_board(asset_key, report)
        source_hash_after = sha256(asset["blend"])
        if source_hash_after != asset["sha256"]:
            raise RuntimeError(f"Post-package source hash drift: {asset_key}")
        asset_outputs[asset_key] = {
            "asset_id": asset["asset_id"],
            "source": {
                "path": relative(asset["blend"]),
                "sha256_before": source_hashes_before[asset_key],
                "sha256_after": source_hash_after,
                "byte_identical": source_hashes_before[asset_key]
                == source_hash_after,
            },
            "observed_issue_counts": report["observed_issue_counts"],
            "raw_render_report": {
                "path": relative(report_path),
                "sha256": sha256(report_path),
            },
            "raw_renders": report["raw_renders"],
            "final_diagnostic_image": {
                "path": relative(final_board),
                "sha256": sha256(final_board),
                "size_px": [1580, 1280],
            },
        }

    result = (
        "PASS"
        if all(
            output["source"]["byte_identical"]
            for output in asset_outputs.values()
        )
        else "FAIL"
    )
    manifest = {
        "schema": "AERATHEA_STEP_13_TECHNICAL_FAIL_DIAGNOSTIC_RENDER_A01_V1",
        "date_utc": utc_now(),
        "run_id": RUN_ID,
        "diagnostic_id": DIAGNOSTIC_ID,
        "artifact_status": f"proof only; {result}",
        "result": result,
        "plain_english_purpose": (
            "Show why a normal render can look acceptable while the saved "
            "surface panels contain bad joins and reversed C04 winding."
        ),
        "authority": authority,
        "renderer": {
            "path": relative(Path(__file__)),
            "sha256": sha256(Path(__file__)),
        },
        "assets": asset_outputs,
        "legend": {
            "red": "exact saved panel boundary edge with no matching partner",
            "yellow": "exact saved boundary edge used by more than two panels",
            "magenta": "directly observed local-C04 face-winding error",
        },
        "source_save_operator_invoked": False,
        "source_geometry_modified": False,
        "repair_or_rebuild_performed": False,
        "mirror_and_weld_performed": False,
        "assumptions": [],
        "artifact_classification": {
            "final_images": "proof only; technical-failure diagnostic",
            "raw_renders": "proof only",
            "temporary_overlay_curves": (
                "in-memory diagnostic only; never saved to either source"
            ),
            "sources": (
                "DCC source candidate pipeline status; quarantined as "
                "Step 13-pass or downstream authority"
            ),
        },
        "next_approval_need": (
            "Flamestrike visual feedback and any additional data; "
            "mirror-and-weld recovery remains separately locked"
        ),
        "step_13_complete": False,
        "step_14_authority": False,
        "geometry_repair_authority": False,
        "export_or_unreal_authority": False,
    }
    write_json(MANIFEST, manifest)
    print(
        json.dumps(
            {
                "result": result,
                "manifest": relative(MANIFEST),
                "final_images": {
                    key: value["final_diagnostic_image"]["path"]
                    for key, value in asset_outputs.items()
                },
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result == "PASS" else 2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-all", action="store_true")
    parser.add_argument("--internal-render")
    return parser.parse_args(
        sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else None
    )


def main() -> int:
    args = parse_args()
    if args.internal_render:
        if args.internal_render not in ASSETS:
            raise RuntimeError(f"Unknown asset: {args.internal_render}")
        return internal_render(args.internal_render)
    if args.render_all:
        return external_render_all()
    raise RuntimeError("Choose --render-all or --internal-render ASSET_KEY")


if __name__ == "__main__":
    raise SystemExit(main())
