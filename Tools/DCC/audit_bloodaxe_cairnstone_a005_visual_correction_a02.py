#!/usr/bin/env python3
"""Independently audit the bounded A005 A02 visual-correction package."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence, Set, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A02"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A02_PLAN.json"
VALIDATION_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A02_VALIDATION.json"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A02.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A02_MANIFEST.json"
FINAL_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A02" / f"{ASSET}_FINAL_CORRECTED_3D_A02.png"
RENDER_AUDIT_REL = FINAL_REL.parent / "FINAL_RENDER_AUDIT_A02.json"
LOCAL_AUDIT_REL = FINAL_REL.parent / "VISUAL_CORRECTION_A02_INDEPENDENT_AUDIT.json"
A01_AUDITOR_PATH = ROOT / "Tools/DCC/audit_bloodaxe_cairnstone_a005_visual_fidelity_recovery.py"
A01_EXPECTED = {
    "blend": {
        "path": DCC_ROOT / f"{ASSET}_DCCGameReady_A02.blend",
        "sha256": "4007ce3732a4109712767341abd4b295c4819ede8970c99a2fa089c48d921d36",
    },
    "final_image": {
        "path": Path("Saved/Automation/DCC") / ASSET / "Production/VisualFidelityRecovery_A01" / f"{ASSET}_FINAL_GAME_READY_ASSET.png",
        "sha256": "56666489f3b5420ad7a4d5206f96e0631147df936eece147780a2263d4d3c05b",
    },
}


def blender_args() -> List[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--schema-only", action="store_true")
    modes.add_argument("--audit", action="store_true")
    return parser.parse_args(list(argv))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(rel: Path) -> Dict[str, Any]:
    with (ROOT / rel).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(rel: Path, payload: Dict[str, Any]) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def gate(identifier: str, passed: bool, detail: Any) -> Dict[str, Any]:
    return {"id": identifier, "status": "pass" if passed else "fail", "detail": detail}


def load_a01_auditor() -> Any:
    spec = importlib.util.spec_from_file_location("a005_visual_fidelity_a01_auditor", A01_AUDITOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the preserved A01 auditor")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.CONTRACT = CONTRACT
    module.PLAN_REL = PLAN_REL
    module.VALIDATION_REL = VALIDATION_REL
    module.BLEND_REL = BLEND_REL
    module.MANIFEST_REL = MANIFEST_REL
    module.FINAL_REL = FINAL_REL
    module.RENDER_AUDIT_REL = RENDER_AUDIT_REL
    module.LOCAL_AUDIT_REL = LOCAL_AUDIT_REL
    return module


def connected_vertex_components(mesh: Any) -> List[Set[int]]:
    adjacency: Dict[int, Set[int]] = {index: set() for index in range(len(mesh.vertices))}
    for edge in mesh.edges:
        a, b = (int(value) for value in edge.vertices)
        adjacency[a].add(b)
        adjacency[b].add(a)
    remaining = set(adjacency)
    result: List[Set[int]] = []
    while remaining:
        seed = remaining.pop()
        component = {seed}
        pending = [seed]
        while pending:
            current = pending.pop()
            for neighbor in adjacency[current]:
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    pending.append(neighbor)
        result.append(component)
    return result


def component_bounds(obj: Any) -> Dict[str, Dict[str, List[float]]]:
    records: List[Dict[str, List[float]]] = []
    for component in connected_vertex_components(obj.data):
        points = [obj.matrix_world @ obj.data.vertices[index].co for index in component]
        minimum = [min(float(point[axis]) for point in points) for axis in range(3)]
        maximum = [max(float(point[axis]) for point in points) for axis in range(3)]
        records.append(
            {
                "min": minimum,
                "max": maximum,
                "dimensions": [maximum[index] - minimum[index] for index in range(3)],
            }
        )
    records.sort(key=lambda record: record["max"][2])
    names = ("C004_APRON", "C003_LOWER_TIER", "C002_UPPER_TIER", "C001_BODY")
    if len(records) != len(names):
        return {f"UNKNOWN_{index}": record for index, record in enumerate(records)}
    return {name: record for name, record in zip(names, records)}


def material_chain_record(bpy: Any) -> Dict[str, Any]:
    lod0 = bpy.data.objects.get(f"{ASSET}_LOD0")
    materials = [
        slot.material
        for slot in lod0.material_slots
        if slot.material is not None and slot.material.name.startswith("M_GIA_BloodAxeCairnstone_A005")
    ] if lod0 is not None else []
    if len(materials) != 1:
        return {"material_count": len(materials), "pass": False}
    material = materials[0]
    nodes = list(material.node_tree.nodes) if material.use_nodes else []
    links = list(material.node_tree.links) if material.use_nodes else []
    node_types = [node.bl_idname for node in nodes]
    shader = next((node for node in nodes if node.bl_idname == "ShaderNodeBsdfPrincipled"), None)
    emission_linked = bool(shader and shader.inputs.get("Emission") and shader.inputs["Emission"].is_linked)
    base_link = next((link for link in links if shader and link.to_node == shader and link.to_socket == shader.inputs.get("Base Color")), None)
    metallic_link = next((link for link in links if shader and link.to_node == shader and link.to_socket == shader.inputs.get("Metallic")), None)
    return {
        "material_count": len(materials),
        "name": material.name,
        "node_types": node_types,
        "gamma_nodes": node_types.count("ShaderNodeGamma"),
        "emission_linked": emission_linked,
        "base_color_source_node": base_link.from_node.name if base_link else None,
        "metallic_source_node": metallic_link.from_node.name if metallic_link else None,
        "display_color_chain": material.get("aerathea_display_color_chain"),
        "emissive_property": material.get("aerathea_emissive"),
        "metallic_required": material.get("aerathea_metallic_required"),
    }


def schema_report(base: Any) -> Dict[str, Any]:
    required = [PLAN_REL, BLEND_REL, MANIFEST_REL, FINAL_REL, RENDER_AUDIT_REL]
    existing = {str(path): (ROOT / path).is_file() for path in required}
    return {
        "schema": "aerathea.a005_visual_correction_a02_auditor_preflight.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "pass_schema_only_no_bpy_no_writes" if all(existing.values()) else "blocked_preflight",
        "bpy_imported": "bpy" in sys.modules,
        "files": existing,
        "validation": str(VALIDATION_REL),
        "local_audit": str(LOCAL_AUDIT_REL),
    }


def audit(base: Any) -> Dict[str, Any]:
    import bpy  # type: ignore

    payload = base.audit()
    manifest = load_json(MANIFEST_REL)
    render_audit = load_json(RENDER_AUDIT_REL)
    additional: List[Dict[str, Any]] = []

    preservation: Dict[str, Any] = {}
    for key, expected in A01_EXPECTED.items():
        path = ROOT / expected["path"]
        actual = sha256_file(path) if path.is_file() else None
        preservation[key] = {
            "path": str(expected["path"]),
            "exists": path.is_file(),
            "actual_sha256": actual,
            "expected_sha256": expected["sha256"],
            "pass": actual == expected["sha256"],
        }
    a02_paths = [manifest["blend"]["path"], *[record["path"] for record in manifest["exports"].values()], *[record["path"] for record in manifest["textures"].values()], str(FINAL_REL)]
    suffix_pass = all("A02" in Path(path).name or "A02" in str(Path(path).parent) for path in a02_paths)
    additional.append(gate("G21_a02_suffix_and_a01_preservation", suffix_pass and all(record["pass"] for record in preservation.values()), {"a02_paths": a02_paths, "a01": preservation}))

    lod0 = bpy.data.objects[f"{ASSET}_LOD0"]
    bounds = component_bounds(lod0)
    expected = {
        "C004_APRON": {"z": [0.0, 10.5], "max_xy": [140.0, 110.0]},
        "C003_LOWER_TIER": {"z": [9.5, 23.5], "max_xy": [112.0, 88.0]},
        "C002_UPPER_TIER": {"z": [22.5, 35.5], "max_xy": [106.0, 82.0]},
        "C001_BODY": {"z": [34.0, 220.0], "max_xy": [120.0, 90.0]},
    }
    bounds_pass = set(bounds) == set(expected)
    if bounds_pass:
        for name, target in expected.items():
            record = bounds[name]
            bounds_pass = bounds_pass and abs(record["min"][2] - target["z"][0]) <= 0.08
            bounds_pass = bounds_pass and abs(record["max"][2] - target["z"][1]) <= 0.08
            bounds_pass = bounds_pass and record["dimensions"][0] <= target["max_xy"][0] + 0.25
            bounds_pass = bounds_pass and record["dimensions"][1] <= target["max_xy"][1] + 0.25
    width_steps = {}
    if set(bounds) == set(expected):
        width_steps = {
            "apron_minus_lower": bounds["C004_APRON"]["dimensions"][0] - bounds["C003_LOWER_TIER"]["dimensions"][0],
            "lower_minus_upper": bounds["C003_LOWER_TIER"]["dimensions"][0] - bounds["C002_UPPER_TIER"]["dimensions"][0],
        }
        bounds_pass = bounds_pass and width_steps["apron_minus_lower"] >= 24.0 and width_steps["lower_minus_upper"] >= 4.0
    additional.append(gate("G22_three_base_component_bounds_and_steps", bounds_pass, {"components": bounds, "width_steps_cm": width_steps}))

    projection = render_audit["base_projection"]["band_heights_px"]
    margins = render_audit["alpha_bounds"]["margins_px"]
    projection_pass = (
        projection["C004_APRON_0_10"] >= 38.0
        and projection["C003_LOWER_10_23"] >= 48.0
        and projection["C002_UPPER_23_35"] >= 44.0
        and min(margins.values()) >= 55
        and render_audit["background"] == "clean neutral gradient; no ground intersection"
    )
    additional.append(gate("G23_projected_base_band_visibility_and_frame", projection_pass, {"band_heights_px": projection, "margins_px": margins, "alpha_bounds": render_audit["alpha_bounds"]}))

    color = render_audit["displayed_color"]
    deltas = color["stone_luminance_delta"]
    rendered = color["rendered_object"]
    source = color["source_front_owned"]
    color_pass = (
        color["stone_median_rgb_distance"] <= 32.0
        and abs(deltas["p10"]) <= 20
        and abs(deltas["p50"]) <= 20
        and abs(deltas["p90"]) <= 36
        and 24 <= rendered["stone"]["luminance"]["p50"] <= 90
        and rendered["red"]["pixels"] >= 1000
        and 0.35 * source["red_fraction"] <= rendered["red_fraction"] <= 2.50 * source["red_fraction"]
    )
    additional.append(gate("G24_displayed_source_color_comparison", color_pass, color))

    chain = material_chain_record(bpy)
    orm_record = next(record for name, record in manifest["textures"].items() if name.endswith("_ORM.png"))
    from PIL import Image

    metallic_extrema = Image.open(ROOT / orm_record["path"]).convert("RGB").getchannel("B").getextrema()
    chain_pass = (
        chain.get("material_count") == 1
        and chain.get("gamma_nodes") == 0
        and not chain.get("emission_linked")
        and chain.get("base_color_source_node") == "A02_DIRECT_SOURCE_BASECOLOR"
        and chain.get("display_color_chain") == "direct sRGB BaseColor; no gamma or grading"
        and not bool(chain.get("emissive_property"))
        and float(chain.get("metallic_required")) == 0.0
        and metallic_extrema == (0, 0)
    )
    additional.append(gate("G25_default_lit_nonmetallic_ungraded_material", chain_pass, {"material": chain, "orm_metallic_extrema": list(metallic_extrema)}))

    management = render_audit["color_management"]
    presentation_pass = (
        management == {"view_transform": "Standard", "look": "None", "exposure": 0.0, "gamma": 1.0}
        and render_audit["lights"] == "four neutral-white area lights; no colored lights"
        and render_audit["collision_visible"] == 0
        and render_audit["lod_visible"] == "LOD0 only"
        and render_audit["review_markers"] == 0
    )
    additional.append(gate("G26_neutral_final_presentation_chain", presentation_pass, {"color_management": management, "lights": render_audit["lights"], "background": render_audit["background"]}))

    payload["schema"] = "aerathea.a005_visual_correction_a02_validation.v1"
    payload["contract_id"] = CONTRACT
    payload["a02_additional_gates"] = additional
    payload["gates"].extend(additional)
    passed = all(item["status"] == "pass" for item in payload["gates"])
    payload["status"] = "pass_a02_dcc_game_ready_candidate_pending_flamestrike_visual_approval" if passed else "blocked_a02_independent_audit_failure"
    payload["artifact_classification"] = "proof only"
    payload["pipeline_status"] = "DCC game-ready candidate" if passed else "candidate blocked"
    payload["candidate"]["blend"] = str(BLEND_REL)
    payload["candidate"]["manifest"] = str(MANIFEST_REL)
    payload["final_review_image"]["path"] = str(FINAL_REL)
    payload["final_review_image"]["visual_gate"] = "pass_internal_a02_base_and_color_pending_Flamestrike" if passed else "blocked_internal_a02_gate"
    payload["gate_summary"] = {"passed": sum(item["status"] == "pass" for item in payload["gates"]), "total": len(payload["gates"])}
    payload["fully_game_ready"] = False
    payload["unreal_outputs"] = 0
    payload["review_requirement"] = "Open only the accepted final A02 image visibly for Flamestrike; intermediate attempts are not review artifacts."
    write_json(LOCAL_AUDIT_REL, payload)
    write_json(VALIDATION_REL, payload)
    return payload


def main() -> int:
    args = parse_args(blender_args())
    base = load_a01_auditor()
    result = schema_report(base) if args.schema_only else audit(base)
    print(json.dumps(result, indent=2))
    return 0 if not result["status"].startswith("blocked") else 1


if __name__ == "__main__":
    raise SystemExit(main())
