#!/usr/bin/env python3
"""Build A005 A11 from A10 pixel-exact footprint authority."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A11"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A11_PLAN.json"
A10_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A10_PIXEL_EXACT_BASE_RECONCILIATION.json"
A08_MEASUREMENT_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A08_TOP_STONE_MEASUREMENT.json"
A09_SUPPORT = ROOT / "Tools/DCC/build_bloodaxe_cairnstone_a005_visual_correction_a09.py"
TEXTURE_ROOT = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A11"
BC_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A11_BC.png"
N_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A11_N.png"
ORM_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A11_ORM.png"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A11.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A11_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A11"
FBX_RELS = {
    "LOD0": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A11.fbx",
    "LOD1": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A11_LOD1.fbx",
    "LOD2": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A11_LOD2.fbx",
    "LOD3": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A11_LOD3.fbx",
}
MODULE_FBX_RELS = {
    "C001": EXPORT_ROOT / "Modules" / f"{ASSET}_C001_Monolith_A11.fbx",
    "C002": EXPORT_ROOT / "Modules" / f"{ASSET}_C002_UpperCourse_A11.fbx",
    "C003": EXPORT_ROOT / "Modules" / f"{ASSET}_C003_LowerCourse_A11.fbx",
    "C004": EXPORT_ROOT / "Modules" / f"{ASSET}_C004_RubbleApron_A11.fbx",
}


def blender_args() -> List[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--schema-only", action="store_true")
    mode.add_argument("--build", action="store_true")
    return parser.parse_args(list(argv))


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def configure_paths(a09: Any) -> None:
    a09.CONTRACT = CONTRACT
    a09.PLAN_REL = PLAN_REL
    a09.MEASUREMENT_REL = A08_MEASUREMENT_REL
    a09.TEXTURE_ROOT = TEXTURE_ROOT
    a09.BC_REL = BC_REL
    a09.N_REL = N_REL
    a09.ORM_REL = ORM_REL
    a09.BLEND_REL = BLEND_REL
    a09.MANIFEST_REL = MANIFEST_REL
    a09.EXPORT_ROOT = EXPORT_ROOT
    a09.FBX_RELS = FBX_RELS
    a09.MODULE_FBX_RELS = MODULE_FBX_RELS


def patch_a11(a09: Any) -> None:
    original_patch = a09.patch_builder
    original_extract = a09.extract_modules_from_lod0
    rubble_stone_a09 = a09.rubble_stone

    def rubble_stone_a11(
        base: Any,
        bpy: Any,
        name: str,
        angle_deg: float,
        outer_row: bool,
        z_range: Any,
        seed: int,
        collection: Any,
    ) -> Any:
        result = rubble_stone_a09(base, bpy, name, angle_deg, outer_row, z_range, seed, collection)
        vertices = result.data.vertices
        center_x = sum(float(vertex.co.x) for vertex in vertices) / len(vertices)
        center_y = sum(float(vertex.co.y) for vertex in vertices) / len(vertices)
        radial_length = max(1.0e-6, math.hypot(center_x, center_y))
        radial = (center_x / radial_length, center_y / radial_length)
        tangent = (-radial[1], radial[0])
        tangential_factor = 1.30 if outer_row else 1.36
        radial_factor = 1.08 if outer_row else 1.12
        for vertex in vertices:
            delta_x = float(vertex.co.x) - center_x
            delta_y = float(vertex.co.y) - center_y
            tangent_offset = delta_x * tangent[0] + delta_y * tangent[1]
            radial_offset = delta_x * radial[0] + delta_y * radial[1]
            vertex.co.x = center_x + tangent[0] * tangent_offset * tangential_factor + radial[0] * radial_offset * radial_factor
            vertex.co.y = center_y + tangent[1] * tangent_offset * tangential_factor + radial[1] * radial_offset * radial_factor
        bottom_z = min(float(vertex.co.z) for vertex in vertices)
        top_z = max(float(vertex.co.z) for vertex in vertices)
        if top_z - bottom_z < 7.5:
            height_factor = 7.5 / max(1.0e-6, top_z - bottom_z)
            for vertex in vertices:
                vertex.co.z = bottom_z + (float(vertex.co.z) - bottom_z) * height_factor
        result["aerathea_A11_dense_rubble_coverage"] = True
        result["aerathea_A11_tangential_coverage_factor"] = tangential_factor
        return result

    a09.rubble_stone = rubble_stone_a11

    def receiver_bed_a11(
        base: Any,
        bpy: Any,
        name: str,
        outer_xy: Any,
        inner_xy: Any,
        z_range: Any,
        segments: int,
        phase: float,
        collection: Any,
    ) -> Any:
        """Build a closed hidden receiver so the owner-view pitch cannot see sky."""
        vertices = []
        for z_value, dimensions in (
            (z_range[0], outer_xy),
            (z_range[0], inner_xy),
            (z_range[1], outer_xy),
            (z_range[1], inner_xy),
        ):
            for index in range(segments):
                angle = math.tau * index / segments
                x_value, y_value = a09.irregular_xy(angle, dimensions[0] * 0.5, dimensions[1] * 0.5, phase)
                vertices.append((x_value, y_value, z_value))
        outer_bottom = 0
        inner_bottom = segments
        outer_top = segments * 2
        inner_top = segments * 3
        faces = []
        for index in range(segments):
            following = (index + 1) % segments
            faces.extend(
                [
                    [outer_bottom + index, outer_bottom + following, outer_top + following, outer_top + index],
                    [inner_bottom + following, inner_bottom + index, inner_top + index, inner_top + following],
                    [outer_bottom + following, outer_bottom + index, inner_bottom + index, inner_bottom + following],
                    [outer_top + index, outer_top + following, inner_top + following, inner_top + index],
                ]
            )
        result = base.create_mesh_object(bpy, name, vertices, faces, collection)
        result["aerathea_A09_hidden_receiver"] = True
        result["aerathea_A09_receiver_z_cm"] = json.dumps(list(z_range))
        result["aerathea_A11_closed_top_cap"] = True
        return result

    a09.receiver_bed = receiver_bed_a11

    def patch_builder_a11(a08: Any) -> Dict[str, Any]:
        state = original_patch(a08)
        configure_a09 = a08.configure_base

        def configure_base_a11(base: Any, a04: Any) -> None:
            configure_a09(base, a04)
            loft_a09 = base.loft
            materials_a09 = base.create_materials
            assign_uv_a09 = base.assign_source_uv
            measurement = a09.load_json(A08_MEASUREMENT_REL)

            def create_materials_a11(bpy: Any):
                stone, removable = materials_a09(bpy)
                stone.name = "M_GIA_BloodAxeCairnstone_A005_VisualCorrection_A11"
                removable.name = "M_GIA_BloodAxeCairnstone_A005_A11_REMOVED_HELPER"
                stone["aerathea_A11_display_color_chain"] = "unchanged source-owned color; no A11 grade"
                return stone, removable

            def loft_a11(bpy: Any, name: str, profiles: Any, segments: int, exponent: float, collection: Any) -> Any:
                if name == "UPPER_COURSE_CORE":
                    result = a09.joined_course(
                        a08, base, bpy, name, measurement["courses"]["C002"]["records"],
                        (118.611111, 77.149321), (92.305556, 55.239819), (23.0, 34.25),
                        (115.611111, 74.149321), (89.305556, 52.239819), (21.70, 35.10),
                        110502, collection, 0.52,
                        "C002 A11 pixel-exact upper masonry module; 19 source-count stones",
                    )
                elif name == "LOWER_COURSE_CORE":
                    result = a09.joined_course(
                        a08, base, bpy, name, measurement["courses"]["C003"]["records"],
                        (134.166667, 96.063348), (116.611111, 75.149321), (9.75, 22.25),
                        (131.166667, 93.063348), (113.611111, 72.149321), (7.90, 22.40),
                        110503, collection, 0.48,
                        "C003 A11 pixel-exact lower masonry module; 24 source-count stones",
                    )
                elif name == "APRON_CORE":
                    receiver_bed_a09 = a09.receiver_bed

                    def receiver_bed_a11(base_arg: Any, bpy_arg: Any, receiver_name: str, outer_xy: Any, inner_xy: Any, z_range: Any, receiver_segments: int, phase: float, receiver_collection: Any) -> Any:
                        if receiver_name == "APRON_CORE_HIDDEN_RECEIVER":
                            outer_xy = (132.166667, 94.063348)
                            inner_xy = (114.611111, 73.149321)
                            z_range = (7.75, 10.00)
                        return receiver_bed_a09(base_arg, bpy_arg, receiver_name, outer_xy, inner_xy, z_range, receiver_segments, phase, receiver_collection)

                    a09.receiver_bed = receiver_bed_a11
                    try:
                        result = loft_a09(bpy, name, profiles, segments, exponent, collection)
                    finally:
                        a09.receiver_bed = receiver_bed_a09
                else:
                    result = loft_a09(bpy, name, profiles, segments, exponent, collection)
                result["aerathea_A11_contract"] = CONTRACT
                result["aerathea_A11_fresh_geometry"] = name != "MONOLITH_BODY"
                return result

            def assign_uv_a11(obj: Any) -> Dict[str, int]:
                counts = assign_uv_a09(obj)
                layer = obj.data.uv_layers.get("UVMap")
                if layer is None:
                    raise RuntimeError("A11 UVMap missing")
                components = a08.component_indices(obj.data)
                plinth = max(components, key=lambda indices: max(float(obj.data.vertices[index].co.z) for index in indices))
                receivers = []
                for indices in components:
                    if indices is plinth:
                        continue
                    center_x = sum(float(obj.data.vertices[index].co.x) for index in indices) / len(indices)
                    center_y = sum(float(obj.data.vertices[index].co.y) for index in indices) / len(indices)
                    if math.hypot(center_x, center_y) < 20.0:
                        receivers.append(indices)
                receiver_vertices = {index for indices in receivers for index in indices}
                dark_transition_faces = 0
                hidden_receiver_faces = 0
                for polygon in obj.data.polygons:
                    coordinates = [obj.data.vertices[index].co for index in polygon.vertices]
                    center_z = sum(float(point.z) for point in coordinates) / len(coordinates)
                    is_receiver = all(int(index) in receiver_vertices for index in polygon.vertices)
                    if not is_receiver and (center_z >= 35.2 or float(polygon.normal.z) <= 0.22):
                        continue
                    dark_transition_faces += 1
                    if is_receiver:
                        hidden_receiver_faces += 1
                    if center_z < 10.1:
                        rect = (122.0, 411.0, 410.0, 434.0)
                        half_width, half_depth = 70.0, 55.0
                    elif center_z < 22.5:
                        rect = (127.0, 390.0, 404.0, 420.0)
                        half_width, half_depth = 67.083334, 48.031674
                    else:
                        rect = (143.0, 359.0, 388.0, 389.0)
                        half_width, half_depth = 59.305556, 38.574661
                    for loop_index in polygon.loop_indices:
                        point = obj.data.vertices[obj.data.loops[loop_index].vertex_index].co
                        normalized_x = max(0.0, min(1.0, (float(point.x) + half_width) / (2.0 * half_width)))
                        normalized_y = max(0.0, min(1.0, (float(point.y) + half_depth) / (2.0 * half_depth)))
                        pixel_x = rect[0] + normalized_x * (rect[2] - rect[0])
                        pixel_y = rect[1] + (1.0 - normalized_y) * (rect[3] - rect[1])
                        layer.data[loop_index].uv = (pixel_x / 2048.0, 1.0 - pixel_y / 2048.0)
                obj["aerathea_A11_structure"] = "exact_A04_C001_plus_A10_dimensioned_C002_C003_C004"
                obj["aerathea_A11_A09_assembled_geometry_inputs"] = 0
                obj["aerathea_A11_no_color_grade"] = True
                obj["aerathea_A11_source_base_transition_faces"] = dark_transition_faces
                obj["aerathea_A11_source_band_hidden_receiver_faces"] = hidden_receiver_faces
                counts["a11_source_base_transition_faces"] = dark_transition_faces
                counts["a11_source_band_hidden_receiver_faces"] = hidden_receiver_faces
                return counts

            base.create_materials = create_materials_a11
            base.loft = loft_a11
            base.assign_source_uv = assign_uv_a11

        a08.configure_base = configure_base_a11
        return state

    def extract_modules_a11(bpy: Any, a08: Any, lod0: Any):
        names, records = original_extract(bpy, a08, lod0)
        collection = bpy.data.collections.get("A09_MODULAR_COMPONENTS")
        if collection is not None:
            collection.name = "A11_MODULAR_COMPONENTS"
        for component, old_name in list(names.items()):
            obj = bpy.data.objects[old_name]
            new_name = old_name.replace("_A09", "_A11")
            obj.name = new_name
            obj["aerathea_A11_module_id"] = component
            obj["aerathea_A11_exact_LOD0_UV_subset"] = True
            names[component] = new_name
        return names, records

    a09.patch_builder = patch_builder_a11
    a09.extract_modules_from_lod0 = extract_modules_a11


def finalize_manifest(a09: Any, manifest: Dict[str, Any]) -> Dict[str, Any]:
    plan = json.loads((ROOT / PLAN_REL).read_text(encoding="utf-8"))
    modules = {
        component: {
            "object": manifest["a09_modules"][component]["object"],
            **{key: value for key, value in record.items() if key not in {"role", "preserve_exact_A04_geometry_and_uv"}},
        }
        for component, record in plan["modules"].items()
    }
    modules["C001"]["preserved_exact_A04"] = True
    manifest.update(
        {
            "schema": "aerathea.a005_visual_correction_a11_candidate.v1",
            "contract_id": CONTRACT,
            "status": "candidate_pending_a11_proof_and_independent_audit",
            "artifact_classification": "candidate",
            "pipeline_status": "DCC game-ready candidate pending A11 audit and Flamestrike review",
            "recovery_from": "A09 circular base read caused by depth values superseded by approved A10 owner-view ratios",
            "geometry_authority": "fresh A11 C002/C003/C004 construction from A10 exact extents plus exact A04 C001; A09 assembled geometry inputs zero",
            "a10_measurement_authority": plan["authority_inputs"]["a10_pixel_exact_measurement"],
            "a11_modules": modules,
            "a09_modules": modules,
            "A09_assembled_geometry_inputs": 0,
            "A11_fresh_course_geometry": True,
            "A11_construction_decisions_are_interpretation": True,
            "A11_top_contact_closure_claimed_as_evidence": False,
            "A11_closed_receiver_top_caps": True,
            "receiver_overlap_policy": "three source-hidden inset receivers use closed owner-view top caps to close only assembly interfaces and remain inside A10 visible exterior maxima; the C004 receiver is vertically limited to 7.75-10.00 cm behind the rubble/contact zone",
            "unreal_outputs": 0,
            "fully_game_ready": False,
            "visual_canon": False,
        }
    )
    for record in manifest.get("textures", {}).values():
        record["a11_role"] = "unchanged A04 source-color atlas retained without grading for A11 geometry"
    (ROOT / MANIFEST_REL).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    args = parse_args(blender_args())
    a09 = load_module("a005_a09_support", A09_SUPPORT)
    configure_paths(a09)
    patch_a11(a09)
    if args.schema_only:
        report = a09.schema_report(load_module("a005_a08_schema_support", a09.A08_MODULE_PATH))
        report.update({"schema": "aerathea.a005_visual_correction_a11_builder_preflight.v1", "contract_id": CONTRACT, "a10_authority": str(A10_REL)})
    else:
        a08 = load_module("a005_a08_build_support", a09.A08_MODULE_PATH)
        report = finalize_manifest(a09, a09.build(a08))
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
