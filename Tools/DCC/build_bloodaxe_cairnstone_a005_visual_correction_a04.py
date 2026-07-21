#!/usr/bin/env python3
"""Build the fresh A005 A04 concept-proportion correction candidate.

The script uses the preserved A005 packaging utilities only. Geometry is
constructed from the A04 contract and approved source-owner measurements; no
A01-A03 mesh is opened or consumed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import random
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_GIA_BloodAxeCairnstone_A005"
CONTRACT = "A005-CR-VISUAL-CORRECTION-A04"
BLUEPRINT_ROOT = Path("docs/assets/blueprints") / ASSET
PLAN_REL = BLUEPRINT_ROOT / "manifests/VISUAL_CORRECTION_A04_PLAN.json"
SOURCE_REL = Path("docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png")
MASK_MANIFEST_REL = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET / "Technical/SM_GIA_BloodAxeCairnstone_A005_SOURCE_MASK_MANIFEST_A01.json"
TEXTURE_PARENT = Path("SourceAssets/Textures/Props/Giants/BloodAxe/Cairns") / ASSET
TEXTURE_ROOT = TEXTURE_PARENT / "VisualCorrection_A04"
BC_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A04_BC.png"
N_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A04_N.png"
ORM_REL = TEXTURE_ROOT / "T_GIA_BloodAxeCairnstone_A005_VF_A04_ORM.png"
DCC_ROOT = Path("SourceAssets/Blender/Props/Giants/BloodAxe/Cairns") / ASSET
BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A04.blend"
MANIFEST_REL = DCC_ROOT / f"{ASSET}_VISUAL_CORRECTION_A04_MANIFEST.json"
EXPORT_ROOT = Path("SourceAssets/Exports/Props/Giants/BloodAxe/Cairns") / ASSET / "VisualCorrection_A04"
FBX_RELS = {
    "LOD0": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A04.fbx",
    "LOD1": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A04_LOD1.fbx",
    "LOD2": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A04_LOD2.fbx",
    "LOD3": EXPORT_ROOT / f"{ASSET}_VisualCorrection_A04_LOD3.fbx",
}
BASE_MODULE_PATH = ROOT / "Tools/DCC/build_bloodaxe_cairnstone_a005_visual_fidelity_recovery.py"
A01_BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_A02.blend"
A02_FINAL_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A02" / f"{ASSET}_FINAL_CORRECTED_3D_A02.png"
A03_BLEND_REL = DCC_ROOT / f"{ASSET}_DCCGameReady_VisualCorrection_A03.blend"
A03_FINAL_REL = Path("Saved/Automation/DCC") / ASSET / "Production/VisualCorrection_A03" / f"{ASSET}_FINAL_CORRECTED_3D_A03.png"

Vec3 = Tuple[float, float, float]


def blender_args() -> List[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--schema-only", action="store_true")
    mode.add_argument("--build", action="store_true")
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


def load_base_module() -> Any:
    spec = importlib.util.spec_from_file_location("a005_a04_packaging", BASE_MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load preserved A005 packaging utilities")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def superellipse_xy(angle: float, half_width: float, half_depth: float, exponent: float) -> Tuple[float, float]:
    cosine = math.cos(angle)
    sine = math.sin(angle)
    return (
        half_width * math.copysign(abs(cosine) ** (2.0 / exponent), cosine),
        half_depth * math.copysign(abs(sine) ** (2.0 / exponent), sine),
    )


def ring_shell(base: Any, bpy: Any, name: str, rings: Sequence[Sequence[Vec3]], collection: Any) -> Any:
    if not rings or len({len(ring) for ring in rings}) != 1:
        raise RuntimeError(f"{name}: inconsistent ring sizes")
    columns = len(rings[0])
    vertices = [point for ring in rings for point in ring]
    faces: List[List[int]] = []
    for ring_index in range(len(rings) - 1):
        lower = ring_index * columns
        upper = (ring_index + 1) * columns
        for column in range(columns):
            nxt = (column + 1) % columns
            faces.append([lower + column, lower + nxt, upper + nxt, upper + column])
    bottom_center = len(vertices)
    vertices.append((0.0, 0.0, min(point[2] for point in rings[0])))
    top_center = len(vertices)
    vertices.append((0.0, 0.0, max(point[2] for point in rings[-1])))
    top_start = (len(rings) - 1) * columns
    for column in range(columns):
        nxt = (column + 1) % columns
        faces.append([bottom_center, nxt, column])
        faces.append([top_center, top_start + column, top_start + nxt])
    return base.create_mesh_object(bpy, name, vertices, faces, collection)


def slab_shell(
    base: Any,
    bpy: Any,
    name: str,
    blocks: int,
    profiles: Sequence[Tuple[float, float, float]],
    exponent: float,
    seed: int,
    collection: Any,
) -> Any:
    """Create one closed, visibly hand-set slab shell with deep joint breaks."""
    rng = random.Random(seed)
    columns_per_block = 10
    columns = blocks * columns_per_block
    radial_offsets = [rng.uniform(-0.60, 0.25) for _ in range(blocks)]
    height_offsets = [rng.uniform(-1.00, 1.00) for _ in range(blocks)]
    widths = [rng.uniform(0.80, 1.20) for _ in range(blocks)]
    width_scale = math.tau / sum(widths)
    block_widths = [value * width_scale for value in widths]
    block_starts: List[float] = []
    cursor = -math.pi * 0.5
    for value in block_widths:
        block_starts.append(cursor)
        cursor += value

    rings: List[List[Vec3]] = []
    ring_weights = (0.0, 0.35, 0.75, 1.0, 0.65, 0.0)
    for ring_index, (z_value, width, depth) in enumerate(profiles):
        ring: List[Vec3] = []
        for column in range(columns):
            block = column // columns_per_block
            phase = column % columns_per_block
            angle = block_starts[block] + block_widths[block] * phase / columns_per_block
            # A deep V-shaped radial recess at every block boundary makes the
            # slab read as masonry while retaining one watertight shell.
            if phase == 0:
                radial = -2.80
            elif phase in (1, columns_per_block - 1):
                radial = -1.10
            elif phase in (2, columns_per_block - 2):
                radial = -0.25
            else:
                radial = radial_offsets[block]
            radial *= ring_weights[ring_index]
            x_value, y_value = superellipse_xy(angle, width * 0.5, depth * 0.5, exponent)
            scale = max(0.78, 1.0 + radial / max(width * 0.5, depth * 0.5))
            crown = height_offsets[block] * ring_weights[ring_index]
            if phase in (0, 1, columns_per_block - 1):
                crown *= 0.25
            ring.append((x_value * scale, y_value * scale, z_value + crown))
        rings.append(ring)
    result = ring_shell(base, bpy, name, rings, collection)
    result[f"aerathea_{name}_blocks"] = blocks
    result[f"aerathea_{name}_joint_recesses"] = blocks
    result["aerathea_structural_role"] = "supporting slab" if "UPPER" in name else "larger lower slab"
    return result


def rubble_apron_shell(base: Any, bpy: Any, name: str, collection: Any) -> Any:
    columns = 48
    levels = (
        (0.0, 70.0, 55.0),
        (2.8, 69.0, 54.0),
        (6.3, 66.0, 51.0),
        (8.5, 64.0, 49.0),
    )
    rings: List[List[Vec3]] = []
    for level_index, (z_value, half_width, half_depth) in enumerate(levels):
        ring: List[Vec3] = []
        for index in range(columns):
            angle = math.tau * index / columns
            x_value, y_value = superellipse_xy(angle, half_width, half_depth, 3.0)
            if level_index == 0:
                scale = 1.0
                local_z = 0.0
            else:
                joint = 1.0 if index % 3 == 1 else 0.0
                irregular = 0.012 + 0.018 * abs(math.sin(index * 1.731 + level_index))
                scale = 1.0 - irregular - joint * (0.028 + 0.010 * level_index)
                local_z = z_value + (0.45 * math.sin(index * 2.17 + level_index) if index % 3 != 1 else -0.55)
            ring.append((x_value * scale, y_value * scale, local_z))
        rings.append(ring)
    result = ring_shell(base, bpy, name, rings, collection)
    result["aerathea_structural_role"] = "shallow peripheral rubble apron; not a structural slab"
    result["aerathea_A04_irregular_changes"] = 16
    return result


def plinth_profiles() -> List[Tuple[float, float, float, float]]:
    sparse = [
        (34.0, 90.0, 64.0, 0.0),
        (35.0, 96.0, 68.0, 0.0),
        (50.0, 104.0, 73.0, 0.0),
        (68.0, 108.0, 78.0, 0.0),
        (92.0, 101.0, 74.0, 0.0),
        (124.0, 91.0, 68.0, 0.0),
        (156.0, 79.0, 60.0, 0.0),
        (184.0, 67.0, 52.0, 0.0),
        (206.0, 56.0, 45.0, 0.0),
        (220.0, 48.0, 40.0, 0.0),
    ]
    result: List[Tuple[float, float, float, float]] = []
    for first, second in zip(sparse, sparse[1:]):
        result.append(first)
        result.append(tuple((first[index] + second[index]) * 0.5 for index in range(4)))
        result.append(tuple(first[index] * 0.25 + second[index] * 0.75 for index in range(4)))
    result.append(sparse[-1])
    return result


def source_panel_y(view: str, z_value: float) -> float:
    mapping = {
        "front": ((35.0, 340.0, 220.0, 40.0), (22.0, 365.0, 35.0, 340.0), (8.0, 400.0, 22.0, 365.0), (0.0, 410.0, 8.0, 400.0)),
        "back": ((35.0, 233.0, 220.0, 40.0), (22.0, 267.0, 35.0, 233.0), (8.0, 300.0, 22.0, 267.0), (0.0, 305.0, 8.0, 300.0)),
        "left": ((35.0, 238.0, 220.0, 10.0), (22.0, 262.0, 35.0, 238.0), (8.0, 293.0, 22.0, 262.0), (0.0, 305.0, 8.0, 293.0)),
        "right": ((35.0, 225.0, 220.0, 37.0), (22.0, 248.0, 35.0, 225.0), (8.0, 277.0, 22.0, 248.0), (0.0, 283.0, 8.0, 277.0)),
    }
    for z0, y0, z1, y1 in mapping[view]:
        if z0 <= z_value <= z1:
            return y0 + (z_value - z0) * (y1 - y0) / max(z1 - z0, 1.0e-9)
    return mapping[view][0][1] if z_value > 220.0 else mapping[view][-1][1]


def interpolate_profile(z_value: float, axis: str) -> float:
    profiles = plinth_profiles()
    value_index = 1 if axis == "x" else 2
    if z_value <= profiles[0][0]:
        return profiles[0][value_index] * 0.5
    for first, second in zip(profiles, profiles[1:]):
        if first[0] <= z_value <= second[0]:
            alpha = (z_value - first[0]) / max(second[0] - first[0], 1.0e-9)
            return (first[value_index] + alpha * (second[value_index] - first[value_index])) * 0.5
    return profiles[-1][value_index] * 0.5


def base_half_extent(z_value: float, axis: str) -> float:
    if z_value <= 8.5:
        outer, inner = ((70.0, 64.0) if axis == "x" else (55.0, 49.0))
        return outer + (inner - outer) * max(0.0, z_value) / 8.5
    if z_value <= 22.5:
        lower, upper = ((68.0, 64.0) if axis == "x" else (52.0, 48.0))
        return lower + (upper - lower) * (z_value - 8.5) / 14.0
    lower, upper = ((60.0, 57.0) if axis == "x" else (45.0, 42.0))
    return lower + (upper - lower) * min(1.0, max(0.0, (z_value - 22.5) / 13.0))


def configure_base(base: Any) -> None:
    base.CONTRACT = CONTRACT
    base.PLAN_REL = PLAN_REL
    base.SOURCE_REL = SOURCE_REL
    base.MASK_MANIFEST_REL = MASK_MANIFEST_REL
    base.OLD_TEXTURE_ROOT = TEXTURE_PARENT
    base.TEXTURE_ROOT = TEXTURE_ROOT
    base.BC_REL = BC_REL
    base.N_REL = N_REL
    base.ORM_REL = ORM_REL
    base.BLEND_REL = BLEND_REL
    base.MANIFEST_REL = MANIFEST_REL
    base.EXPORT_ROOT = EXPORT_ROOT
    base.FBX_RELS = FBX_RELS

    original_copy_textures = base.copy_textures
    original_loft = base.loft
    original_project_point = base.project_point
    original_assign_uv = base.assign_source_uv

    def copy_textures_a04() -> Dict[str, Dict[str, Any]]:
        records = original_copy_textures()
        # Lift only Step 14's non-source-owned authored zone into the approved
        # source-stone midtone range. Source windows are outside this rectangle
        # and remain byte-exact. This keeps exposed slab ledges readable under
        # neutral light without grading the source art.
        from PIL import Image

        base_color_path = ROOT / BC_REL
        base_color_image = Image.open(base_color_path).convert("RGB")
        authored_rect = (16, 976, 2032, 2032)
        authored = base_color_image.crop(authored_rect)
        lifted = []
        for red, green, blue in authored.getdata():
            luminance = int(round(0.2126 * red + 0.7152 * green + 0.0722 * blue))
            value = max(46, min(112, int(round(luminance * 1.28 + 12))))
            lifted.append((value, max(0, int(round(value * 0.94))), max(0, int(round(value * 0.88)))))
        authored.putdata(lifted)
        base_color_image.paste(authored, authored_rect[:2])
        base_color_image.save(base_color_path, format="PNG")
        for record in records.values():
            record["a04_correction"] = record.pop("recovery_correction", "none")
            record["recovery_role"] = "A04 source-regenerated atlas; source-owned RGB remains exact"
            record_path = ROOT / record["path"]
            record["sha256"] = sha256_file(record_path)
            if record_path == base_color_path:
                record["a04_correction"] += "; non-owned authored zone lifted to dark-stone midtones"
        return records

    def loft_a04(
        bpy: Any,
        name: str,
        profiles: Sequence[Tuple[float, float, float, float]],
        segments: int,
        exponent: float,
        collection: Any,
    ) -> Any:
        if name == "MONOLITH_BODY":
            result = original_loft(bpy, name, plinth_profiles(), 92, 4.5, collection)
            result["aerathea_structural_role"] = "central tapered plinth"
            return result
        if name == "APRON_CORE":
            return rubble_apron_shell(base, bpy, name, collection)
        if name == "LOWER_COURSE_CORE":
            return slab_shell(
                base,
                bpy,
                name,
                19,
                ((7.5, 128.0, 98.0), (8.0, 136.0, 104.0), (10.0, 136.0, 104.0), (20.5, 132.0, 100.0), (22.2, 132.0, 100.0), (23.0, 128.0, 96.0)),
                12.0,
                60403,
                collection,
            )
        if name == "UPPER_COURSE_CORE":
            return slab_shell(
                base,
                bpy,
                name,
                17,
                ((21.5, 112.0, 82.0), (22.0, 120.0, 90.0), (24.0, 120.0, 90.0), (33.5, 116.0, 86.0), (35.0, 116.0, 86.0), (35.5, 112.0, 82.0)),
                12.0,
                60402,
                collection,
            )
        return original_loft(bpy, name, profiles, segments, exponent, collection)

    def project_point_a04(point: Vec3, view: str, bbox: Sequence[int], row_spans: Sequence[Tuple[int, int]]) -> Tuple[float, float]:
        x_value, y_value, z_value = point
        if view in ("front", "back", "left", "right"):
            panel_y = source_panel_y(view, max(0.0, min(220.0, z_value)))
            horizontal = {"front": x_value, "back": -x_value, "left": -y_value, "right": y_value}[view]
            axis = "x" if view in ("front", "back") else "y"
            half_extent = interpolate_profile(z_value, axis) if z_value >= 34.0 else base_half_extent(z_value, axis)
            row = max(0, min(len(row_spans) - 1, int(round(panel_y))))
            span_min, span_max = row_spans[row]
            inset = 3.0
            normalized = max(0.0, min(1.0, (horizontal + half_extent) / max(2.0 * half_extent, 1.0e-9)))
            return (span_min + inset + normalized * max(1.0, span_max - span_min - 2.0 * inset), panel_y)
        return original_project_point(point, view, bbox, row_spans)

    def create_materials_a04(bpy: Any) -> Tuple[Any, Any]:
        stone = bpy.data.materials.new("M_GIA_BloodAxeCairnstone_A005_VisualCorrection_A04")
        stone.use_nodes = True
        stone.use_backface_culling = True
        nodes = stone.node_tree.nodes
        links = stone.node_tree.links
        nodes.clear()
        output = nodes.new("ShaderNodeOutputMaterial")
        shader = nodes.new("ShaderNodeBsdfPrincipled")
        base_color = nodes.new("ShaderNodeTexImage")
        base_color.name = "A04_DIRECT_SOURCE_BASECOLOR"
        base_color.image = bpy.data.images.load(str(ROOT / BC_REL), check_existing=False)
        base_color.image.colorspace_settings.name = "sRGB"
        base_color.interpolation = "Linear"
        base_color.extension = "EXTEND"
        normal_image = nodes.new("ShaderNodeTexImage")
        normal_image.name = "A04_DIRECTX_NORMAL"
        normal_image.image = bpy.data.images.load(str(ROOT / N_REL), check_existing=False)
        try:
            normal_image.image.colorspace_settings.name = "Non-Color"
        except TypeError:
            normal_image.image.colorspace_settings.name = "Linear"
        split_normal = nodes.new("ShaderNodeSeparateRGB")
        invert_green = nodes.new("ShaderNodeMath")
        invert_green.operation = "SUBTRACT"
        invert_green.inputs[0].default_value = 1.0
        combine_normal = nodes.new("ShaderNodeCombineRGB")
        normal_map = nodes.new("ShaderNodeNormalMap")
        normal_map.inputs["Strength"].default_value = 0.18
        orm = nodes.new("ShaderNodeTexImage")
        orm.name = "A04_ORM_NONMETALLIC"
        orm.image = bpy.data.images.load(str(ROOT / ORM_REL), check_existing=False)
        try:
            orm.image.colorspace_settings.name = "Non-Color"
        except TypeError:
            orm.image.colorspace_settings.name = "Linear"
        separate_orm = nodes.new("ShaderNodeSeparateRGB")
        links.new(base_color.outputs["Color"], shader.inputs["Base Color"])
        links.new(normal_image.outputs["Color"], split_normal.inputs["Image"])
        links.new(split_normal.outputs["R"], combine_normal.inputs["R"])
        links.new(split_normal.outputs["G"], invert_green.inputs[1])
        links.new(invert_green.outputs[0], combine_normal.inputs["G"])
        links.new(split_normal.outputs["B"], combine_normal.inputs["B"])
        links.new(combine_normal.outputs["Image"], normal_map.inputs["Color"])
        links.new(normal_map.outputs["Normal"], shader.inputs["Normal"])
        links.new(orm.outputs["Color"], separate_orm.inputs["Image"])
        links.new(separate_orm.outputs["G"], shader.inputs["Roughness"])
        links.new(separate_orm.outputs["B"], shader.inputs["Metallic"])
        shader.inputs["Specular"].default_value = 0.0
        links.new(shader.outputs["BSDF"], output.inputs["Surface"])
        stone["aerathea_display_color_chain"] = "direct sRGB BaseColor; no gamma or grading"
        stone["aerathea_emissive"] = False
        stone["aerathea_metallic_required"] = 0.0
        removable = bpy.data.materials.new("M_GIA_BloodAxeCairnstone_A005_A04_REMOVED_HELPER")
        return stone, removable

    def assign_uv_a04(obj: Any) -> Dict[str, int]:
        counts = original_assign_uv(obj)
        texel_center = 0.5 / 2048.0
        layer = obj.data.uv_layers.get("UVMap")
        if layer is None:
            raise RuntimeError("A04 UVMap missing")
        for loop in layer.data:
            loop.uv.x += texel_center
            loop.uv.y -= texel_center
        # The source sheets do not own the exposed horizontal slab ledges or
        # the shallow rubble skirt. Route those interpreted transition faces
        # to unique cells in Step 14's authored dark-stone zone. This prevents
        # bright source-background bands without altering any source-owned
        # atlas texel or the source-facing vertical masonry.
        authored_faces = 0
        for polygon in obj.data.polygons:
            coordinates = [obj.data.vertices[index].co for index in polygon.vertices]
            center_z = sum(float(point.z) for point in coordinates) / len(coordinates)
            authored_transition = center_z < 9.0 or (center_z < 40.0 and float(polygon.normal.z) > 0.22)
            if not authored_transition:
                continue
            authored_faces += 1
            normal_z = float(polygon.normal.z)
            if center_z < 9.0 and normal_z <= 0.22:
                # Unique unwrap of the shallow apron perimeter into a narrow
                # authored strip. U follows angle and V follows height.
                for loop_index in polygon.loop_indices:
                    point = obj.data.vertices[obj.data.loops[loop_index].vertex_index].co
                    angle = (math.atan2(float(point.y), float(point.x)) + math.pi) / math.tau
                    pixel_x = 24.0 + angle * 2000.0
                    pixel_y = 984.0 + max(0.0, min(1.0, float(point.z) / 9.0)) * 128.0
                    layer.data[loop_index].uv = (pixel_x / 2048.0, 1.0 - pixel_y / 2048.0)
                continue
            if center_z < 9.0:
                rect = (24.0, 1136.0, 676.0, 1648.0)
                half_width, half_depth = 70.0, 55.0
            elif center_z < 24.0:
                rect = (698.0, 1136.0, 1360.0, 1648.0)
                half_width, half_depth = 68.0, 52.0
            else:
                rect = (1382.0, 1136.0, 2024.0, 1648.0)
                half_width, half_depth = 60.0, 45.0
            for loop_index in polygon.loop_indices:
                point = obj.data.vertices[obj.data.loops[loop_index].vertex_index].co
                normalized_x = max(0.0, min(1.0, (float(point.x) + half_width) / (2.0 * half_width)))
                normalized_y = max(0.0, min(1.0, (float(point.y) + half_depth) / (2.0 * half_depth)))
                pixel_x = rect[0] + normalized_x * (rect[2] - rect[0])
                pixel_y = rect[1] + (1.0 - normalized_y) * (rect[3] - rect[1])
                layer.data[loop_index].uv = (pixel_x / 2048.0, 1.0 - pixel_y / 2048.0)
        obj["aerathea_A04_structure"] = "plinth_on_upper_slab_on_larger_lower_slab"
        obj["aerathea_A04_component_widths_cm"] = json.dumps({"plinth_contact": 96, "upper_slab": 120, "lower_slab": 136, "apron": 140})
        obj["aerathea_A04_geometry_authority"] = "concept-relative source-owner proportions"
        obj["aerathea_A04_authored_transition_faces"] = authored_faces
        return counts

    base.copy_textures = copy_textures_a04
    base.loft = loft_a04
    base.project_point = project_point_a04
    base.create_materials = create_materials_a04
    base.assign_source_uv = assign_uv_a04


def schema_report() -> Dict[str, Any]:
    plan = load_json(PLAN_REL)
    checks: Dict[str, Any] = {}
    for name, record in plan["authority_inputs"].items():
        path = ROOT / record["path"]
        actual = sha256_file(path) if path.is_file() else None
        checks[name] = {"path": record["path"], "actual_sha256": actual, "expected_sha256": record["sha256"], "pass": actual == record["sha256"]}
    passed = all(record["pass"] for record in checks.values())
    return {
        "schema": "aerathea.a005_visual_correction_a04_builder_preflight.v1",
        "asset_id": ASSET,
        "contract_id": CONTRACT,
        "status": "pass_schema_only_no_output" if passed else "blocked_authority_hash",
        "bpy_imported": "bpy" in sys.modules,
        "authority_inputs": checks,
        "historical_geometry_inputs": 0,
        "outputs": [str(BLEND_REL), str(MANIFEST_REL), str(BC_REL), str(N_REL), str(ORM_REL), *[str(path) for path in FBX_RELS.values()]],
    }


def build(base: Any) -> Dict[str, Any]:
    plan = load_json(PLAN_REL)
    configure_base(base)
    preservation_paths = {
        "A01_blend": A01_BLEND_REL,
        "A02_final": A02_FINAL_REL,
        "A03_blend": A03_BLEND_REL,
        "A03_final": A03_FINAL_REL,
    }
    preservation_before = {name: sha256_file(ROOT / path) for name, path in preservation_paths.items()}
    manifest = base.build()
    manifest.update(
        {
            "schema": "aerathea.a005_visual_correction_a04_candidate.v1",
            "contract_id": CONTRACT,
            "date": "2026-07-21",
            "status": "candidate_pending_a04_independent_audit",
            "artifact_classification": "candidate",
            "pipeline_status": "DCC game-ready candidate pending A04 audit and Flamestrike review",
            "recovery_from": "A03 source-target proportion conflict",
            "geometry_authority": "A04 concept-relative source-owner proportions; no A01-A03 geometry inputs",
            "a04_structure": {
                "C001": {"role": "central tapered plinth", "max_cm": [108.0, 78.0], "contact_max_cm": [96.0, 68.0]},
                "C002": {"role": "upper supporting slab", "footprint_cm": [120.0, 90.0], "blocks": 17},
                "C003": {"role": "larger lower slab", "footprint_cm": [136.0, 104.0], "blocks": 19},
                "C004": {"role": "shallow peripheral rubble; not a slab", "footprint_cm": [140.0, 110.0], "height_cm": 8.5},
            },
            "structural_ratios": {
                "plinth_contact_over_upper_width": 96.0 / 120.0,
                "upper_over_lower_width": 120.0 / 136.0,
                "lower_over_apron_width": 136.0 / 140.0,
            },
            "preservation": {
                name: {
                    "path": str(path),
                    "sha256_before": digest,
                    "sha256_after": sha256_file(ROOT / path),
                    "pass": digest == sha256_file(ROOT / path),
                }
                for name, (path, digest) in ((key, (preservation_paths[key], value)) for key, value in preservation_before.items())
            },
            "unreal_outputs": 0,
            "fully_game_ready": False,
            "visual_canon": False,
        }
    )
    manifest_path = ROOT / MANIFEST_REL
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    args = parse_args(blender_args())
    base = load_base_module()
    report = schema_report() if args.schema_only else build(base)
    if args.schema_only and report["bpy_imported"]:
        raise RuntimeError("schema-only path imported bpy")
    print(json.dumps(report, indent=2))
    return 0 if not report["status"].startswith("blocked") else 1


if __name__ == "__main__":
    raise SystemExit(main())
