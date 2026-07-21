#!/usr/bin/env python3
"""Independently audit the A005 A04 Steps 01-16 DCC candidate."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A04"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A04_PLAN.json"
VALIDATION_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A04_VALIDATION.json"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A04_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A04"
FBX_RELS = {
    "LOD0": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A04.fbx",
    "LOD1": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A04_LOD1.fbx",
    "LOD2": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A04_LOD2.fbx",
    "LOD3": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A04_LOD3.fbx",
}
OUTPUT_ROOT_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A04"
FINAL_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A04.png"
FINAL_RGBA_REL = OUTPUT_ROOT_REL / f"{ASSET}_FINAL_CORRECTED_3D_A04_OBJECT_RGBA.png"
FINAL_AUDIT_REL = OUTPUT_ROOT_REL / "FINAL_RENDER_AUDIT_A04.json"
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical" / f"{ASSET}_SOURCE_MASK_MANIFEST_A01.json"
UV_PLAN_REL = BLUEPRINT_ROOT / "manifests/STEP_14_UV_OWNERSHIP_PLAN.json"
SOURCE_BC_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "T_GIA_BloodAxeCairnstone_A005_BC.png"
A04_BC_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A04/T_GIA_BloodAxeCairnstone_A005_VF_A04_BC.png"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(rel: Path) -> Dict[str, Any]:
    with (ROOT / rel).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def mesh_triangles(mesh: Any) -> int:
    mesh.calc_loop_triangles()
    return len(mesh.loop_triangles)


def object_bounds(obj: Any) -> Dict[str, List[float]]:
    from mathutils import Vector  # type: ignore

    points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    minimum = [min(float(point[index]) for point in points) for index in range(3)]
    maximum = [max(float(point[index]) for point in points) for index in range(3)]
    return {
        "min": minimum,
        "max": maximum,
        "dimensions": [maximum[index] - minimum[index] for index in range(3)],
    }


def close(first: Sequence[float], second: Sequence[float], tolerance: float = 1.0e-4) -> bool:
    return len(first) == len(second) and all(abs(float(a) - float(b)) <= tolerance for a, b in zip(first, second))


def connected_component_bounds(obj: Any) -> Tuple[List[Dict[str, Any]], Dict[str, int]]:
    import bmesh  # type: ignore

    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.verts.ensure_lookup_table()
    remaining = set(vertex.index for vertex in bm.verts)
    components: List[Dict[str, Any]] = []
    while remaining:
        start = remaining.pop()
        pending = [start]
        indices = [start]
        while pending:
            index = pending.pop()
            for edge in bm.verts[index].link_edges:
                other = edge.other_vert(bm.verts[index]).index
                if other in remaining:
                    remaining.remove(other)
                    pending.append(other)
                    indices.append(other)
        coords = [bm.verts[index].co for index in indices]
        minimum = [min(float(point[axis]) for point in coords) for axis in range(3)]
        maximum = [max(float(point[axis]) for point in coords) for axis in range(3)]
        components.append(
            {
                "vertices": len(indices),
                "min": minimum,
                "max": maximum,
                "dimensions": [maximum[axis] - minimum[axis] for axis in range(3)],
            }
        )
    topology = {
        "components": len(components),
        "boundary_edges": sum(1 for edge in bm.edges if len(edge.link_faces) == 1),
        "nonmanifold_edges": sum(1 for edge in bm.edges if len(edge.link_faces) not in (1, 2)),
        "degenerate_faces": sum(1 for face in bm.faces if face.calc_area() <= 1.0e-8),
    }
    bm.free()
    components.sort(key=lambda record: record["max"][2])
    return components, topology


def alpha_span_at_world_z(image: Any, z_value: float) -> Dict[str, int]:
    row = int(round(512.0 + (110.0 - z_value) * (1024.0 / 250.0)))
    row = max(0, min(image.height - 1, row))
    alpha = image.getchannel("A")
    owned = [column for column in range(image.width) if alpha.getpixel((column, row)) >= 16]
    return {"z_cm": int(round(z_value)), "row": row, "width_px": max(owned) - min(owned) + 1 if owned else 0}


def source_owned_rgb_audit() -> Dict[str, Any]:
    from PIL import Image

    mask_manifest = load_json(MASK_MANIFEST_REL)
    uv_plan = load_json(UV_PLAN_REL)
    windows = {entry["view"]: entry["rect"] for entry in uv_plan["uv0"]["source_windows_half_open_px"]}
    source = Image.open(ROOT / SOURCE_BC_REL).convert("RGB")
    candidate = Image.open(ROOT / A04_BC_REL).convert("RGB")
    compared = 0
    mismatches = 0
    by_view: Dict[str, Any] = {}
    for record in mask_manifest["records"]:
        mask = Image.open(ROOT / record["mask_path"]).convert("L")
        rect = windows[record["view"]]
        source_panel = source.crop(tuple(rect))
        candidate_panel = candidate.crop(tuple(rect))
        view_compared = 0
        view_mismatches = 0
        for source_pixel, candidate_pixel, owned in zip(source_panel.getdata(), candidate_panel.getdata(), mask.getdata()):
            if owned <= 0:
                continue
            view_compared += 1
            if source_pixel != candidate_pixel:
                view_mismatches += 1
        compared += view_compared
        mismatches += view_mismatches
        by_view[record["view"]] = {"pixels_compared": view_compared, "mismatches": view_mismatches}
    return {"pixels_compared": compared, "mismatches": mismatches, "by_view": by_view}


def clean_fbx_reimport(bpy: Any, manifest: Dict[str, Any]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for lod_name, rel in FBX_RELS.items():
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.fbx(filepath=str(ROOT / rel), use_custom_normals=True)
        meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
        primary = [obj for obj in meshes if not obj.name.startswith("UCX_")]
        primary_triangles = sum(mesh_triangles(obj.data) for obj in primary)
        expected = int(manifest["lods"][lod_name]["triangles"])
        result[lod_name] = {
            "mesh_objects": len(meshes),
            "primary_objects": len(primary),
            "primary_triangles": primary_triangles,
            "expected_triangles": expected,
            "pass": len(primary) == 1 and primary_triangles == expected,
        }
    return result


def main() -> int:
    import bpy  # type: ignore
    from PIL import Image

    plan = load_json(PLAN_REL)
    manifest = load_json(MANIFEST_REL)
    final_audit = load_json(FINAL_AUDIT_REL)
    lod0 = bpy.data.objects.get(f"{ASSET}_LOD0")
    if lod0 is None:
        raise RuntimeError("A04 LOD0 missing")

    authority = {}
    for name, record in plan["authority_inputs"].items():
        actual = sha256_file(ROOT / record["path"])
        authority[name] = {"expected": record["sha256"], "actual": actual, "pass": actual == record["sha256"]}

    lods = {}
    for lod_name in ("LOD0", "LOD1", "LOD2", "LOD3"):
        obj = bpy.data.objects.get(f"{ASSET}_{lod_name}")
        lods[lod_name] = {
            "present": obj is not None,
            "triangles": mesh_triangles(obj.data) if obj else 0,
            "bounds": object_bounds(obj) if obj else None,
            "uv_layers": [layer.name for layer in obj.data.uv_layers] if obj else [],
            "materials": len(obj.data.materials) if obj else 0,
        }

    components, topology = connected_component_bounds(lod0)
    if len(components) != 4:
        raise RuntimeError(f"expected four components, found {len(components)}")
    apron, lower, upper, plinth = components
    hierarchy = {
        "plinth": plinth,
        "upper_slab": upper,
        "lower_slab": lower,
        "apron": apron,
        "ratios": {
            "plinth_contact_over_upper_contract": 96.0 / upper["dimensions"][0],
            "upper_over_lower": upper["dimensions"][0] / lower["dimensions"][0],
            "lower_over_apron": lower["dimensions"][0] / apron["dimensions"][0],
        },
    }

    front_lit_rel = Path(final_audit["proofs"]["front_lit"]["path"])
    front_lit = Image.open(ROOT / front_lit_rel).convert("RGBA")
    projection_widths = {
        "plinth_above_contact": alpha_span_at_world_z(front_lit, 37.0),
        "upper_slab": alpha_span_at_world_z(front_lit, 28.0),
        "lower_slab": alpha_span_at_world_z(front_lit, 15.0),
        "apron": alpha_span_at_world_z(front_lit, 4.0),
    }
    widths = [projection_widths[key]["width_px"] for key in ("plinth_above_contact", "upper_slab", "lower_slab", "apron")]

    render_rgba = Image.open(ROOT / FINAL_RGBA_REL).convert("RGBA")
    object_pixels = [(r, g, b) for r, g, b, alpha in render_rgba.getdata() if alpha >= 16]
    bright_fraction = sum(1 for pixel in object_pixels if min(pixel) >= 180 and max(pixel) - min(pixel) <= 20) / max(1, len(object_pixels))
    source_rgb = source_owned_rgb_audit()
    collisions = sorted(obj.name for obj in bpy.data.objects if obj.name.startswith("UCX_"))
    clean_import = clean_fbx_reimport(bpy, manifest)

    gates: List[Dict[str, Any]] = []
    def gate(gate_id: str, passed: bool, detail: Any) -> None:
        gates.append({"id": gate_id, "status": "pass" if passed else "fail", "detail": detail})

    gate("G01_authority_hashes", all(record["pass"] for record in authority.values()), authority)
    gate("G02_contract_and_classification", manifest.get("contract_id") == CONTRACT and manifest.get("artifact_classification") == "candidate", {"contract": manifest.get("contract_id"), "classification": manifest.get("artifact_classification")})
    gate("G03_lods_and_budget", [lods[name]["triangles"] for name in lods] == [9856, 4532, 2068, 788], lods)
    gate("G04_bounds_and_pivot", all(close(lods[name]["bounds"]["dimensions"], [140.0, 110.0, 220.0]) and close(lods[name]["bounds"]["min"], [-70.0, -55.0, 0.0]) for name in lods), {name: lods[name]["bounds"] for name in lods})
    gate("G05_four_closed_primary_shells", topology == {"components": 4, "boundary_edges": 0, "nonmanifold_edges": 0, "degenerate_faces": 0}, topology)
    gate("G06_structural_component_dimensions", close(plinth["dimensions"][:2], [108.0, 78.0], 0.25) and close(upper["dimensions"][:2], [120.0, 90.0], 0.25) and close(lower["dimensions"][:2], [136.0, 104.0], 0.25) and close(apron["dimensions"][:2], [140.0, 110.0], 0.25) and apron["dimensions"][2] <= 9.0, hierarchy)
    gate(
        "G07_projection_three_mass_hierarchy",
        widths[0] < widths[1] < widths[2]
        and widths[1] - widths[0] >= 40
        and widths[2] - widths[1] >= 40
        and widths[3] >= int(math.floor(widths[2] * 0.95)),
        {
            **projection_widths,
            "rule": "three structural masses must descend strictly; non-structural irregular apron may recess locally but remains within five percent of lower slab at the sampled row",
        },
    )
    gate("G08_material_and_uv", all(lods[name]["materials"] == 1 and lods[name]["uv_layers"] == ["UVMap", "LightmapUV"] for name in lods), {name: {"materials": lods[name]["materials"], "uv_layers": lods[name]["uv_layers"]} for name in lods})
    gate("G09_collision_set", len(collisions) == 4, collisions)
    export_hashes = {name: {"actual": sha256_file(ROOT / rel), "expected": manifest["exports"][name]["sha256"]} for name, rel in FBX_RELS.items()}
    gate("G10_fbx_hashes", all(record["actual"] == record["expected"] for record in export_hashes.values()), export_hashes)
    gate("G11_clean_fbx_reimport", all(record["pass"] for record in clean_import.values()), clean_import)
    gate("G12_source_owned_rgb_exact", source_rgb["pixels_compared"] > 0 and source_rgb["mismatches"] == 0, source_rgb)
    gate("G13_a01_a03_preservation", all(record["pass"] for record in manifest["preservation"].values()), manifest["preservation"])
    alpha = final_audit["alpha_bounds"]["margins_px"]
    gate("G14_final_review_framing", min(alpha.values()) >= 80 and final_audit["size"] == [1400, 1600], {"size": final_audit["size"], "margins": alpha, "orientation": final_audit["orientation"]})
    gate("G15_final_bright_fringe", bright_fraction <= 0.001, {"bright_fringe_fraction": bright_fraction})
    source_stone = final_audit["displayed_color"]["source_front_owned"]["stone_median_rgb"]
    final_stone = final_audit["displayed_color"]["final"]["stone_median_rgb"]
    stone_distance = math.sqrt(sum((int(a) - int(b)) ** 2 for a, b in zip(source_stone, final_stone)))
    gate("G16_displayed_stone_color", stone_distance <= 12.0, {"source": source_stone, "final": final_stone, "rgb_distance": stone_distance})
    gate("G17_unreal_firewall", manifest.get("unreal_outputs") == 0 and manifest.get("fully_game_ready") is False, {"unreal_outputs": manifest.get("unreal_outputs"), "fully_game_ready": manifest.get("fully_game_ready")})

    passed = sum(1 for record in gates if record["status"] == "pass")
    validation = {
        "schema": "aerathea.a005_visual_correction_a04_validation.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "date": "2026-07-21",
        "status": "pass_candidate_pending_flamestrike_visual_review" if passed == len(gates) else "blocked_a04_independent_audit",
        "artifact_classification": "proof only",
        "pipeline_status": "DCC game-ready candidate" if passed == len(gates) else "candidate blocked",
        "fully_game_ready": False,
        "unreal_outputs": 0,
        "candidate": {"manifest": str(MANIFEST_REL), "manifest_sha256": sha256_file(ROOT / MANIFEST_REL)},
        "final_review_image": {"path": str(FINAL_REL), "sha256": sha256_file(ROOT / FINAL_REL), "visual_gate": "pending Flamestrike" if passed == len(gates) else "blocked"},
        "gates": gates,
        "gate_summary": {"passed": passed, "total": len(gates)},
    }
    (ROOT / VALIDATION_REL).write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))
    return 0 if passed == len(gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
