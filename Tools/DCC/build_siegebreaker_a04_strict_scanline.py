#!/usr/bin/env python3
"""Build the fresh A04 strict-scanline Siege Breaker DCC package.

The visible primary facade is a closed mesh whose exterior row contours and UV
coordinates come directly from the fresh A04 source mask.  Its RGB atlas region
is an unscaled integer-coordinate copy of the approved source sheet.  Closed
three-dimensional backing, hidden surfaces, PBR response, LOD simplification,
and collision are explicitly tagged interpretation inside the locked numeric
envelope.  No A01/A02/A03 Hammer output is read by this program.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from statistics import median
from typing import Any

import bmesh
import bpy
from mathutils import Vector
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = "StrictScanline_A04"
CONTRACT_ID = "SB-VF-A04-STRICT-SCANLINE"
CM = 0.01
ATLAS_SIZE = 2048

EVIDENCE_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A04" / "FreshEvidence"
EVIDENCE_MANIFEST = EVIDENCE_ROOT / f"{ASSET_ID}_A04_FreshEvidenceManifest.json"
PRE_GEOMETRY_AUDIT = EVIDENCE_ROOT / f"{ASSET_ID}_A04_PreGeometryAudit.json"
SOURCE = ROOT / (
    "SourceAssets/Reference/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/"
    "02_SiegeBreaker_Codex_Final_Package/reference/concept_sheet_style_reference.png"
)
TEXTURE_ROOT = ROOT / "SourceAssets/Textures/Weapons/Dwarven" / ASSET_ID / REVISION
BLENDER_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID
EXPORT_ROOT = ROOT / "SourceAssets/Exports/Weapons/Dwarven" / ASSET_ID / REVISION
REVIEW_ROOT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A04"
BLEND_PATH = BLENDER_ROOT / f"{ASSET_ID}_DCCGameReady_{REVISION}.blend"
BUILD_MANIFEST = BLENDER_ROOT / f"{ASSET_ID}_{REVISION}_BUILD_MANIFEST.json"
TEXTURE_MANIFEST = TEXTURE_ROOT / f"{ASSET_ID}_{REVISION}_TEXTURE_MANIFEST.json"

MATERIAL_ORDER = ["M_Stone", "M_Bronze", "M_Steel", "M_Leather", "M_Rune_Emissive"]
FAMILIES = {
    "M_Stone": "Stone",
    "M_Bronze": "Bronze",
    "M_Steel": "Steel",
    "M_Leather": "Leather",
    "M_Rune_Emissive": "Rune",
}
FAMILY_FILL = {
    "Stone": (31, 38, 48, 255),
    "Bronze": (104, 58, 28, 255),
    "Steel": (49, 60, 74, 255),
    "Leather": (69, 28, 17, 255),
    "Rune": (24, 144, 238, 255),
}
FAMILY_ORM = {
    "Stone": (255, 204, 0, 255),
    "Bronze": (255, 118, 255, 255),
    "Steel": (255, 98, 255, 255),
    "Leather": (255, 176, 0, 255),
    "Rune": (255, 62, 0, 255),
}
COMPONENT_MATERIAL = {"head": "M_Stone", "shaft": "M_Steel", "grip": "M_Leather", "pommel": "M_Bronze"}
COMPONENT_FRONT_Y_CM = {"head": -16.0, "shaft": -2.5, "grip": -2.5, "pommel": -5.5}
COMPONENT_BACK_Y_CM = {"head": 16.0, "shaft": 2.5, "grip": 2.5, "pommel": 4.5}
COMPONENT_SIDE_X_CM = {"head": 26.0, "shaft": 2.5, "grip": 2.5, "pommel": 5.5}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def pixel_sha256(image: Image.Image) -> str:
    return hashlib.sha256(image.convert("RGB").tobytes("raw", "RGB")).hexdigest()


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for collection in list(bpy.data.collections):
        if collection.name != "Collection":
            bpy.data.collections.remove(collection)
    for datablocks in (bpy.data.meshes, bpy.data.curves, bpy.data.materials, bpy.data.images, bpy.data.cameras, bpy.data.lights):
        for datablock in list(datablocks):
            if datablock.users == 0:
                datablocks.remove(datablock)


def get_collection(name: str, hide_render: bool = False) -> bpy.types.Collection:
    collection = bpy.data.collections.get(name)
    if collection is None:
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
    collection.hide_render = hide_render
    return collection


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def configure_scene() -> None:
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.length_unit = "CENTIMETERS"
    scene.unit_settings.scale_length = 1.0
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.image_settings.color_depth = "8"
    scene.render.film_transparent = False
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.gtao_distance = 3.0
    scene.eevee.gtao_factor = 1.15
    scene.eevee.taa_render_samples = 64
    scene.view_settings.view_transform = "Standard"
    available_looks = {item.identifier for item in scene.view_settings.bl_rna.properties["look"].enum_items}
    scene.view_settings.look = "Medium High Contrast" if "Medium High Contrast" in available_looks else "None"
    scene.view_settings.exposure = 0.0
    scene.view_settings.gamma = 1.0
    scene.world.use_nodes = True
    background = next(node for node in scene.world.node_tree.nodes if node.type == "BACKGROUND")
    background.inputs["Color"].default_value = (0.78, 0.755, 0.69, 1.0)
    background.inputs["Strength"].default_value = 0.62
    scene["Aerathea.AssetID"] = ASSET_ID
    scene["Aerathea.ContractID"] = CONTRACT_ID
    scene["Aerathea.Revision"] = REVISION
    scene["Aerathea.SourceOnlyA04"] = True
    scene["Aerathea.PriorHammerCandidateInputs"] = "none"
    scene["Aerathea.BoundsCM"] = "52x32x170"
    scene["Aerathea.ArtifactStatus"] = "candidate"


def load_authority() -> dict[str, Any]:
    evidence = json.loads(EVIDENCE_MANIFEST.read_text(encoding="utf-8"))
    preaudit = json.loads(PRE_GEOMETRY_AUDIT.read_text(encoding="utf-8"))
    if not preaudit.get("passed"):
        raise RuntimeError("A04 pre-geometry audit did not pass")
    if evidence["source_file_sha256"] != sha256(SOURCE):
        raise RuntimeError("A04 source file changed after evidence extraction")
    if evidence["authority"]["prior_hammer_candidate_inputs"]:
        raise RuntimeError("A04 evidence contains a prior Hammer candidate input")
    return evidence


def create_texture_package(evidence: dict[str, Any]) -> dict[str, Any]:
    TEXTURE_ROOT.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGB")
    primary = evidence["views"]["primary"]
    primary_mask = Image.open(ROOT / primary["mask"]).convert("L")
    primary_bbox = tuple(primary["source_bbox_xyxy"])

    alpha = Image.new("L", (ATLAS_SIZE, ATLAS_SIZE), 255)
    # The exact source-sheet rectangle is transparent by default; only primary
    # source-owned object pixels are visible there.  The unused atlas region is
    # opaque and stores the inferred hidden-surface material fill.
    alpha.paste(0, (0, 0, source.width, source.height))
    alpha.paste(primary_mask, (primary_bbox[0], primary_bbox[1]))
    for view_name, view in evidence["views"].items():
        if view_name == "primary":
            continue
        mask = Image.open(ROOT / view["mask"]).convert("L")
        bbox = tuple(view["source_bbox_xyxy"])
        alpha.paste(mask, (bbox[0], bbox[1]))

    files: dict[str, Any] = {}
    for family, fill in FAMILY_FILL.items():
        bc = Image.new("RGBA", (ATLAS_SIZE, ATLAS_SIZE), fill)
        bc.paste(source, (0, 0))
        bc.putalpha(alpha)
        normal = Image.new("RGBA", (ATLAS_SIZE, ATLAS_SIZE), (128, 128, 255, 255))
        orm = Image.new("RGBA", (ATLAS_SIZE, ATLAS_SIZE), FAMILY_ORM[family])
        emissive = Image.new("RGBA", (ATLAS_SIZE, ATLAS_SIZE), (0, 0, 0, 255))
        source_pixels = source.load()
        emissive_pixels = emissive.load()
        for y in range(source.height):
            for x in range(source.width):
                red, green, blue = source_pixels[x, y]
                if blue > 112 and blue > red * 1.16 and blue > green * 1.05:
                    emissive_pixels[x, y] = (red, green, blue, 255)
        if family == "Rune":
            for y in range(source.height, ATLAS_SIZE):
                for x in range(source.width, ATLAS_SIZE):
                    emissive_pixels[x, y] = (28, 126, 255, 255)

        paths = {
            "BC": TEXTURE_ROOT / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_BC.png",
            "N": TEXTURE_ROOT / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_N.png",
            "ORM": TEXTURE_ROOT / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_ORM.png",
            "E": TEXTURE_ROOT / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_E.png",
        }
        for suffix, image in (("BC", bc), ("N", normal), ("ORM", orm), ("E", emissive)):
            image.save(paths[suffix], optimize=True)

        reloaded = Image.open(paths["BC"]).convert("RGB")
        copied_source = reloaded.crop((0, 0, source.width, source.height))
        exact = pixel_sha256(copied_source) == pixel_sha256(source)
        if not exact:
            raise RuntimeError(f"{family} atlas source RGB is not an exact integer copy")
        files[family] = {
            suffix: {"path": rel(path), "sha256": sha256(path), "size": list(Image.open(path).size)}
            for suffix, path in paths.items()
        }
        files[family]["visible_source_rgb_exact"] = exact
        files[family]["source_region_xyxy"] = [0, 0, source.width, source.height]
        files[family]["copy_method"] = "exact integer paste; no resize; no filter"

    manifest = {
        "schema": "aerathea.siegebreaker_a04_texture_manifest.v1",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "status": "candidate",
        "source": rel(SOURCE),
        "source_file_sha256": sha256(SOURCE),
        "atlas_size": [ATLAS_SIZE, ATLAS_SIZE],
        "visible_source_rgb_exact_all_families": all(item["visible_source_rgb_exact"] for item in files.values()),
        "filtered_resampling": False,
        "files": files,
    }
    TEXTURE_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def texture_path(family: str, suffix: str) -> Path:
    return TEXTURE_ROOT / f"T_DRW_SiegeBreaker_Hammer_A01_{family}_{suffix}.png"


def set_noncolor(image: bpy.types.Image) -> None:
    try:
        image.colorspace_settings.name = "Non-Color"
    except TypeError:
        image.colorspace_settings.name = "Linear"


def create_material(name: str, family: str) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    material.blend_method = "CLIP"
    material.shadow_method = "CLIP"
    material.alpha_threshold = 0.5
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

    bc = nodes.new("ShaderNodeTexImage")
    bc.name = f"{family}_BC_ExactSourceAtlas"
    bc.interpolation = "Closest"
    bc.extension = "CLIP"
    bc.image = bpy.data.images.load(str(texture_path(family, "BC")), check_existing=True)
    bc.image.colorspace_settings.name = "sRGB"
    links.new(bc.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(bc.outputs["Alpha"], bsdf.inputs["Alpha"])

    normal_tex = nodes.new("ShaderNodeTexImage")
    normal_tex.name = f"{family}_N"
    normal_tex.interpolation = "Closest"
    normal_tex.image = bpy.data.images.load(str(texture_path(family, "N")), check_existing=True)
    set_noncolor(normal_tex.image)
    normal_map = nodes.new("ShaderNodeNormalMap")
    normal_map.inputs["Strength"].default_value = 0.45
    links.new(normal_tex.outputs["Color"], normal_map.inputs["Color"])
    links.new(normal_map.outputs["Normal"], bsdf.inputs["Normal"])

    orm = nodes.new("ShaderNodeTexImage")
    orm.name = f"{family}_ORM"
    orm.interpolation = "Closest"
    orm.image = bpy.data.images.load(str(texture_path(family, "ORM")), check_existing=True)
    set_noncolor(orm.image)
    separate = nodes.new("ShaderNodeSeparateRGB")
    links.new(orm.outputs["Color"], separate.inputs["Image"])
    links.new(separate.outputs["G"], bsdf.inputs["Roughness"])
    links.new(separate.outputs["B"], bsdf.inputs["Metallic"])

    emissive = nodes.new("ShaderNodeTexImage")
    emissive.name = f"{family}_E"
    emissive.interpolation = "Closest"
    emissive.image = bpy.data.images.load(str(texture_path(family, "E")), check_existing=True)
    set_noncolor(emissive.image)
    emission_name = "Emission" if "Emission" in bsdf.inputs else "Emission Color"
    links.new(emissive.outputs["Color"], bsdf.inputs[emission_name])
    if "Emission Strength" in bsdf.inputs:
        bsdf.inputs["Emission Strength"].default_value = 1.3 if family != "Rune" else 3.5
    material["Aerathea.SourceRGBExact"] = True
    material["Aerathea.HiddenFillInterpretation"] = True
    return material


def create_materials() -> dict[str, bpy.types.Material]:
    return {name: create_material(name, family) for name, family in FAMILIES.items()}


def activate(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def apply_modifier(obj: bpy.types.Object, modifier_name: str) -> None:
    activate(obj)
    bpy.ops.object.modifier_apply(modifier=modifier_name)


def tag(obj: bpy.types.Object, component: str, lod: int, authority: str, status: str = "candidate") -> None:
    obj["Aerathea.AssetID"] = ASSET_ID
    obj["Aerathea.ContractID"] = CONTRACT_ID
    obj["Aerathea.Revision"] = REVISION
    obj["Aerathea.Component"] = component
    obj["Aerathea.LOD"] = lod
    obj["Aerathea.GeometryAuthority"] = authority
    obj["Aerathea.ArtifactStatus"] = status
    obj["Aerathea.PriorCandidateInput"] = False


def assign_fill_uv(obj: bpy.types.Object) -> None:
    uv = obj.data.uv_layers.get("UVMap") or obj.data.uv_layers.new(name="UVMap")
    safe = (1800.5 / ATLAS_SIZE, 1.0 - 1800.5 / ATLAS_SIZE)
    for loop_uv in uv.data:
        loop_uv.uv = safe


def finalize_mesh(obj: bpy.types.Object, smooth: bool = False) -> bpy.types.Object:
    activate(obj)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    if smooth:
        for polygon in obj.data.polygons:
            polygon.use_smooth = True
    assign_fill_uv(obj)
    return obj


def add_cube(
    name: str,
    dims_cm: tuple[float, float, float],
    location_cm: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    lod: int,
    component: str,
    bevel_cm: float = 0.0,
    rotation: tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=tuple(value * CM for value in location_cm), rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = tuple(value * CM for value in dims_cm)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    if bevel_cm > 0.0:
        bevel = obj.modifiers.new("A04_SourceCharacterBevel", "BEVEL")
        bevel.width = bevel_cm * CM
        bevel.segments = 1 if lod >= 1 else 2
        bevel.affect = "EDGES"
        apply_modifier(obj, bevel.name)
    obj.data.materials.append(material)
    move_to_collection(obj, collection)
    tag(obj, component, lod, "numeric envelope + hidden-surface interpretation")
    return finalize_mesh(obj, smooth=False)


def add_cylinder(
    name: str,
    diameter_cm: float,
    depth_cm: float,
    center_cm: tuple[float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    lod: int,
    component: str,
    vertices: int = 16,
    rotation: tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=max(8, vertices),
        radius=diameter_cm * CM * 0.5,
        depth=depth_cm * CM,
        location=tuple(value * CM for value in center_cm),
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    move_to_collection(obj, collection)
    tag(obj, component, lod, "direct_constraint for visible interval; interpreted radial tessellation")
    return finalize_mesh(obj, smooth=lod <= 1)


def add_xz_prism(
    name: str,
    points_xz_cm: list[tuple[float, float]],
    y_min_cm: float,
    y_max_cm: float,
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    lod: int,
    component: str,
) -> bpy.types.Object:
    count = len(points_xz_cm)
    vertices = [(x * CM, y_min_cm * CM, z * CM) for x, z in points_xz_cm]
    vertices += [(x * CM, y_max_cm * CM, z * CM) for x, z in points_xz_cm]
    faces = [tuple(reversed(range(count))), tuple(range(count, count * 2))]
    for index in range(count):
        nxt = (index + 1) % count
        faces.append((index, nxt, count + nxt, count + index))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.data.materials.append(material)
    tag(obj, component, lod, "hidden-surface interpretation inside numeric envelope")
    return finalize_mesh(obj, smooth=False)


def add_lathe(
    name: str,
    rings: list[tuple[float, float, float]],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    lod: int,
    component: str,
    sides: int,
) -> bpy.types.Object:
    vertices: list[tuple[float, float, float]] = []
    for z_cm, radius_x_cm, radius_y_cm in rings:
        for side in range(sides):
            angle = 2.0 * math.pi * side / sides
            vertices.append((math.cos(angle) * radius_x_cm * CM, math.sin(angle) * radius_y_cm * CM, z_cm * CM))
    faces: list[tuple[int, ...]] = []
    for ring_index in range(len(rings) - 1):
        for side in range(sides):
            nxt = (side + 1) % sides
            lower = ring_index * sides
            upper = (ring_index + 1) * sides
            faces.append((lower + side, lower + nxt, upper + nxt, upper + side))
    faces.append(tuple(reversed(range(sides))))
    last = (len(rings) - 1) * sides
    faces.append(tuple(last + side for side in range(sides)))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.data.materials.append(material)
    tag(obj, component, lod, "direct numeric interval + interpreted hidden radial profile")
    return finalize_mesh(obj, smooth=False)


def add_diamond(
    name: str,
    center_x: float,
    center_z: float,
    width: float,
    height: float,
    y_min: float,
    y_max: float,
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    lod: int,
    component: str,
) -> bpy.types.Object:
    points = [
        (center_x, center_z + height * 0.5),
        (center_x + width * 0.5, center_z),
        (center_x, center_z - height * 0.5),
        (center_x - width * 0.5, center_z),
    ]
    return add_xz_prism(name, points, y_min, y_max, material, collection, lod, component)


def add_helix(
    name: str,
    phase: float,
    direction: float,
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    lod: int,
) -> bpy.types.Object:
    curve = bpy.data.curves.new(f"{name}_Curve", "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 1
    curve.bevel_depth = (0.22 if lod == 0 else 0.18) * CM
    curve.bevel_resolution = 0
    samples = {0: 150, 1: 92, 2: 52}.get(lod, 28)
    spline = curve.splines.new("POLY")
    spline.points.add(samples - 1)
    for index, point in enumerate(spline.points):
        t = index / (samples - 1)
        angle = phase + direction * 6.2 * 2.0 * math.pi * t
        radius = 2.27
        point.co = (math.cos(angle) * radius * CM, math.sin(angle) * radius * CM, (18.3 + 41.4 * t) * CM, 1.0)
    obj = bpy.data.objects.new(name, curve)
    collection.objects.link(obj)
    curve.materials.append(material)
    activate(obj)
    bpy.ops.object.convert(target="MESH")
    obj = bpy.context.object
    tag(obj, "Grip_Leather_Wrap", lod, "source-visible cross-wrap language; interpreted hidden continuation")
    return finalize_mesh(obj, smooth=lod <= 1)


def uv_for_source_pixel(source_x: float, source_y: float) -> tuple[float, float]:
    return ((source_x + 0.5) / ATLAS_SIZE, 1.0 - (source_y + 0.5) / ATLAS_SIZE)


def representative_center_and_scale(component: str, spans: list[dict[str, int]], target_width_cm: float) -> tuple[float, float]:
    centers = [(item["source_x_min"] + item["source_x_max_inclusive"]) * 0.5 for item in spans]
    widths = [item["pixel_width"] for item in spans]
    if component in {"head", "pommel", "grip"}:
        source_min = min(item["source_x_min"] for item in spans)
        source_max = max(item["source_x_max_inclusive"] for item in spans)
        center = (source_min + source_max) * 0.5
        # Vertex coordinates represent pixel centers, so the exact geometric
        # span is max-center minus min-center rather than the inclusive sample
        # count.  This keeps the direct contour inside the numeric envelope.
        reference_width = source_max - source_min
    else:
        # The shaft's source rows contain authored collars much broader than the
        # exact 5 cm structural shaft.  The median owns the 5 cm shaft; broader
        # source rows remain direct traced collar ornament.
        center = median(centers)
        reference_width = median(widths)
    return float(center), float(target_width_cm) / float(reference_width)


def create_source_facade(
    component: str,
    component_record: dict[str, Any],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    lod: int,
) -> bpy.types.Object:
    raw_spans = component_record["row_spans"]
    step = {0: 1, 1: 2, 2: 4, 3: 8}[lod]
    spans = raw_spans[::step]
    if spans[-1] != raw_spans[-1]:
        spans.append(raw_spans[-1])
    z_min, z_max = component_record["world_z_interval_cm"]
    source_y_min = raw_spans[0]["source_y"]
    source_y_max = raw_spans[-1]["source_y"]
    center_px, cm_per_px = representative_center_and_scale(component, raw_spans, component_record["world_visible_width_cm"])
    front_y = COMPONENT_FRONT_Y_CM[component]
    back_y = front_y + (0.22 if lod == 0 else 0.16)

    vertices: list[tuple[float, float, float]] = []
    source_uvs: list[tuple[float, float]] = []
    source_rows: list[dict[str, Any]] = []
    for item in spans:
        fraction = (item["source_y"] - source_y_min) / max(1, source_y_max - source_y_min)
        z_cm = z_max - fraction * (z_max - z_min)
        left_x = (item["source_x_min"] - center_px) * cm_per_px
        right_x = (item["source_x_max_inclusive"] - center_px) * cm_per_px
        vertices.extend(
            [
                (left_x * CM, front_y * CM, z_cm * CM),
                (right_x * CM, front_y * CM, z_cm * CM),
                (left_x * CM, back_y * CM, z_cm * CM),
                (right_x * CM, back_y * CM, z_cm * CM),
            ]
        )
        source_uvs.extend(
            [
                uv_for_source_pixel(item["source_x_min"], item["source_y"]),
                uv_for_source_pixel(item["source_x_max_inclusive"], item["source_y"]),
                (1800.5 / ATLAS_SIZE, 1.0 - 1800.5 / ATLAS_SIZE),
                (1800.5 / ATLAS_SIZE, 1.0 - 1800.5 / ATLAS_SIZE),
            ]
        )
        source_rows.append(
            {
                "source_y": item["source_y"],
                "world_z_cm": z_cm,
                "source_x_min": item["source_x_min"],
                "source_x_max_inclusive": item["source_x_max_inclusive"],
                "world_x_min_cm": left_x,
                "world_x_max_cm": right_x,
            }
        )

    faces: list[tuple[int, ...]] = []
    face_uv_vertex_indices: list[tuple[int, ...]] = []
    for row in range(len(spans) - 1):
        base = row * 4
        nxt = (row + 1) * 4
        # Front traced surface, back closed surface, and two closed perimeter walls.
        faces.append((base, base + 1, nxt + 1, nxt))
        face_uv_vertex_indices.append((base, base + 1, nxt + 1, nxt))
        faces.append((base + 2, nxt + 2, nxt + 3, base + 3))
        face_uv_vertex_indices.append((base + 2, nxt + 2, nxt + 3, base + 3))
        faces.append((base, nxt, nxt + 2, base + 2))
        face_uv_vertex_indices.append((base + 2, base + 2, base + 2, base + 2))
        faces.append((base + 1, base + 3, nxt + 3, nxt + 1))
        face_uv_vertex_indices.append((base + 2, base + 2, base + 2, base + 2))
    first = 0
    last = (len(spans) - 1) * 4
    faces.extend([(first, first + 2, first + 3, first + 1), (last, last + 1, last + 3, last + 2)])
    face_uv_vertex_indices.extend([(first + 2, first + 2, first + 2, first + 2), (last + 2, last + 2, last + 2, last + 2)])

    name = f"A04_SourceFacade_{component.title()}_LOD{lod}"
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.data.materials.append(material)
    uv_layer = obj.data.uv_layers.new(name="UVMap")
    for polygon, uv_indices in zip(mesh.polygons, face_uv_vertex_indices):
        for loop_index, vertex_index in zip(polygon.loop_indices, uv_indices):
            uv_layer.data[loop_index].uv = source_uvs[vertex_index]

    tag(obj, f"Primary_{component}_SourceFacade", lod, "fresh A04 exact source mask row contours")
    obj["Aerathea.VisibleSelectionMethod"] = "source_priority"
    obj["Aerathea.SourceScope"] = "component_isolated"
    obj["Aerathea.SourceViewOwner"] = "primary"
    obj["Aerathea.SourceRowsJSON"] = json.dumps(source_rows, separators=(",", ":"))
    obj["Aerathea.SourceCenterPixel"] = center_px
    obj["Aerathea.CMPerSourcePixel"] = cm_per_px
    obj["Aerathea.ExteriorContourDirectTraced"] = True
    obj["Aerathea.MeshClosed"] = True
    return obj


def create_secondary_card(
    view_name: str,
    component: str,
    record: dict[str, Any],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    lod: int,
) -> bpy.types.Object:
    x0, y0, x1, y1 = record["source_bbox_xyxy"]
    z_min, z_max = record["world_z_interval_cm"]
    half_span = float(record["world_visible_span_cm"]) * 0.5
    thickness = 0.12
    safe_uv = (1800.5 / ATLAS_SIZE, 1.0 - 1800.5 / ATLAS_SIZE)
    source_uv = [
        uv_for_source_pixel(x0, y0),
        uv_for_source_pixel(x1 - 1, y0),
        uv_for_source_pixel(x1 - 1, y1 - 1),
        uv_for_source_pixel(x0, y1 - 1),
    ]

    if view_name == "back":
        outward = COMPONENT_BACK_Y_CM[component]
        inward = outward - thickness
        vertices = [
            (-half_span * CM, outward * CM, z_max * CM),
            (half_span * CM, outward * CM, z_max * CM),
            (half_span * CM, outward * CM, z_min * CM),
            (-half_span * CM, outward * CM, z_min * CM),
            (-half_span * CM, inward * CM, z_max * CM),
            (half_span * CM, inward * CM, z_max * CM),
            (half_span * CM, inward * CM, z_min * CM),
            (-half_span * CM, inward * CM, z_min * CM),
        ]
    else:
        sign = -1.0 if view_name == "left" else 1.0
        outward = sign * COMPONENT_SIDE_X_CM[component]
        inward = outward - sign * thickness
        vertices = [
            (outward * CM, -half_span * CM, z_max * CM),
            (outward * CM, half_span * CM, z_max * CM),
            (outward * CM, half_span * CM, z_min * CM),
            (outward * CM, -half_span * CM, z_min * CM),
            (inward * CM, -half_span * CM, z_max * CM),
            (inward * CM, half_span * CM, z_max * CM),
            (inward * CM, half_span * CM, z_min * CM),
            (inward * CM, -half_span * CM, z_min * CM),
        ]
    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (3, 7, 4, 0),
    ]
    name = f"A04_SecondaryFacade_{view_name.title()}_{component.title()}_LOD{lod}"
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.data.materials.append(material)
    uv_layer = obj.data.uv_layers.new(name="UVMap")
    face_uvs = [source_uv, [safe_uv] * 4, [safe_uv] * 4, [safe_uv] * 4, [safe_uv] * 4, [safe_uv] * 4]
    for polygon, uvs in zip(mesh.polygons, face_uvs):
        for loop_index, uv in zip(polygon.loop_indices, uvs):
            uv_layer.data[loop_index].uv = uv
    tag(obj, f"Secondary_{view_name}_{component}_SourceFacade", lod, f"fresh A04 exact {view_name} component mask and RGB")
    obj["Aerathea.VisibleSelectionMethod"] = "exact"
    obj["Aerathea.SourceScope"] = "component_isolated"
    obj["Aerathea.SourceViewOwner"] = view_name
    obj["Aerathea.ExactAlphaSilhouette"] = True
    obj["Aerathea.MeshClosed"] = True
    return obj


def add_head_backing(materials: dict[str, bpy.types.Material], collection: bpy.types.Collection, lod: int) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    bevel = {0: 2.1, 1: 1.6, 2: 1.0, 3: 0.5}[lod]
    # The exact source facade owns Y=-16.0.  Hidden stone volume starts behind
    # it while retaining the authoritative rear depth at Y=+16.0.
    objects.append(add_cube(f"Head_Stone_Left_LOD{lod}", (13.8, 31.5, 38.0), (-18.9, 0.05, 151.0), materials["M_Stone"], collection, lod, "Head_Stone_Left", bevel))
    objects.append(add_cube(f"Head_Stone_Right_LOD{lod}", (13.8, 31.5, 38.0), (18.9, 0.05, 151.0), materials["M_Stone"], collection, lod, "Head_Stone_Right", bevel))
    objects.append(add_cube(f"Head_Core_LOD{lod}", (24.0, 22.0, 32.0), (0.0, 0.0, 150.0), materials["M_Steel"], collection, lod, "Head_Core", 1.3))
    objects.append(add_cube(f"Head_CoreBronzeInset_LOD{lod}", (18.0, 23.0, 25.0), (0.0, -0.2, 151.0), materials["M_Bronze"], collection, lod, "Head_Core_Bronze", 0.9))
    # Dwarven architectural braces resolve the source's nested metal frame.
    if lod <= 2:
        brace_depth = 1.0
        for suffix, x0, z0, x1, z1 in (
            ("UL", -10.0, 139.0, 0.0, 151.0), ("UR", 10.0, 139.0, 0.0, 151.0),
            ("LL", -10.0, 163.0, 0.0, 151.0), ("LR", 10.0, 163.0, 0.0, 151.0),
        ):
            dx, dz = x1 - x0, z1 - z0
            length = math.hypot(dx, dz)
            angle = -math.atan2(dz, dx)
            objects.append(add_cube(f"Head_NestedBrace_{suffix}_LOD{lod}", (length, brace_depth, 2.3), ((x0 + x1) * 0.5, -11.55, (z0 + z1) * 0.5), materials["M_Steel"], collection, lod, "Head_Nested_Brace", 0.22, (0.0, angle, 0.0)))
    objects.append(add_diamond(f"Head_CoreRunePlate_LOD{lod}", 0.0, 151.0, 9.0, 15.0, -12.25, -11.45, materials["M_Rune_Emissive"], collection, lod, "Rune_Inlays"))
    if lod <= 1:
        objects.append(add_diamond(f"Head_LeftRunePlate_LOD{lod}", -19.0, 151.0, 6.0, 10.0, -15.68, -15.42, materials["M_Rune_Emissive"], collection, lod, "Rune_Inlays"))
        objects.append(add_diamond(f"Head_RightRunePlate_LOD{lod}", 19.0, 151.0, 6.0, 10.0, -15.68, -15.42, materials["M_Rune_Emissive"], collection, lod, "Rune_Inlays"))
    # Cross-head tie bars, collar, and source-visible crown/finial.
    for z_cm in (143.5, 158.5):
        objects.append(add_cylinder(f"Head_TieBar_{z_cm:g}_LOD{lod}", 3.0, 42.0, (0.0, 0.0, z_cm), materials["M_Bronze"], collection, lod, "Head_TieBar", 12 if lod >= 2 else 18, (0.0, math.pi * 0.5, 0.0)))
    objects.append(add_cylinder(f"Head_LowerCollar_LOD{lod}", 8.0, 4.0, (0.0, 0.0, 134.0), materials["M_Bronze"], collection, lod, "Head_LowerCollar", 12 if lod >= 2 else 20))
    rings = [(160.0, 4.6, 4.6), (163.0, 5.2, 5.2), (166.0, 4.0, 4.0), (168.5, 3.2, 3.2), (170.0, 1.3, 1.3)]
    objects.append(add_lathe(f"Head_CrownFinial_LOD{lod}", rings, materials["M_Bronze"], collection, lod, "Head_CrownFinial", 8 if lod >= 2 else 16))
    return objects


def add_shaft_grip_pommel(materials: dict[str, bpy.types.Material], collection: bpy.types.Collection, lod: int) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    sides = {0: 24, 1: 18, 2: 12, 3: 8}[lod]
    # Source facade owns the front radial extreme; the closed shaft backing owns
    # the rear extreme so their union remains exactly 5 cm deep.
    objects.append(add_cylinder(f"Shaft_Metal_LOD{lod}", 4.8, 118.0, (0.0, 0.0, 73.0), materials["M_Steel"], collection, lod, "Shaft_Metal", sides))
    objects.append(add_cylinder(f"Grip_Leather_Core_LOD{lod}", 4.55, 42.0, (0.0, 0.0, 39.0), materials["M_Leather"], collection, lod, "Grip_Leather", sides))
    if lod <= 2:
        objects.append(add_helix(f"Grip_CrossWrap_A_LOD{lod}", 0.0, 1.0, materials["M_Leather"], collection, lod))
        objects.append(add_helix(f"Grip_CrossWrap_B_LOD{lod}", math.pi, -1.0, materials["M_Leather"], collection, lod))
    for index, (z_cm, diameter, height) in enumerate(((18.0, 6.8, 1.4), (60.0, 7.4, 1.6), (64.0, 7.0, 2.0), (128.5, 7.5, 2.0), (132.0, 8.2, 2.0))):
        if lod >= 3 and index not in (0, 1, 4):
            continue
        objects.append(add_cylinder(f"Shaft_Collar_{index:02d}_LOD{lod}", diameter, height, (0.0, 0.0, z_cm), materials["M_Bronze"], collection, lod, "Shaft_Collar", max(8, sides - 2)))
    if lod <= 1:
        for z_cm in (72.0, 84.0, 96.0, 108.0, 120.0):
            objects.append(add_diamond(f"Shaft_Rune_{int(z_cm)}_LOD{lod}", 0.0, z_cm, 1.5, 3.3, -2.62, -2.38, materials["M_Rune_Emissive"], collection, lod, "Rune_Inlays"))
    pommel_rings = [(0.0, 1.3, 1.2), (2.0, 2.2, 2.0), (5.0, 4.7, 3.8), (9.0, 5.3, 4.3), (13.0, 5.1, 4.2), (16.5, 3.4, 3.0), (18.0, 2.5, 2.5)]
    objects.append(add_lathe(f"Pommel_Main_LOD{lod}", pommel_rings, materials["M_Bronze"], collection, lod, "Pommel", 8 if lod >= 2 else 16))
    if lod <= 2:
        objects.append(add_diamond(f"Pommel_Rune_Front_LOD{lod}", 0.0, 10.0, 4.8, 6.8, -4.75, -4.48, materials["M_Rune_Emissive"], collection, lod, "Rune_Inlays"))
        objects.append(add_diamond(f"Pommel_Rune_Back_LOD{lod}", 0.0, 10.0, 4.8, 6.8, 4.48, 4.75, materials["M_Rune_Emissive"], collection, lod, "Rune_Inlays"))
    return objects


def build_lod(evidence: dict[str, Any], materials: dict[str, bpy.types.Material], lod: int) -> tuple[bpy.types.Collection, list[bpy.types.Object]]:
    collection = get_collection(f"SB_A04_LOD{lod}", hide_render=lod != 0)
    objects: list[bpy.types.Object] = []
    objects.extend(add_head_backing(materials, collection, lod))
    objects.extend(add_shaft_grip_pommel(materials, collection, lod))
    for component, record in evidence["primary_components"].items():
        objects.append(create_source_facade(component, record, materials[COMPONENT_MATERIAL[component]], collection, lod))
    for view_name in ("back", "left", "right"):
        for component, record in evidence["secondary_components"][view_name].items():
            objects.append(create_secondary_card(view_name, component, record, materials[COMPONENT_MATERIAL[component]], collection, lod))
    return collection, objects


def add_collision(collection: bpy.types.Collection) -> list[bpy.types.Object]:
    collision_material = bpy.data.materials.new("M_A04_CollisionProxy")
    collision_material.diffuse_color = (0.05, 0.8, 0.2, 0.35)
    head = add_cube(f"UCX_{ASSET_ID}_00", (52.0, 32.0, 38.0), (0.0, 0.0, 151.0), collision_material, collection, 0, "Collision_Head")
    shaft = add_cylinder(f"UCX_{ASSET_ID}_01", 5.0, 118.0, (0.0, 0.0, 73.0), collision_material, collection, 0, "Collision_Shaft", 12)
    pommel = add_cube(f"UCX_{ASSET_ID}_02", (11.0, 9.0, 18.0), (0.0, 0.0, 9.0), collision_material, collection, 0, "Collision_Pommel")
    for obj in (head, shaft, pommel):
        obj.hide_render = True
        obj.display_type = "WIRE"
        obj["Aerathea.CollisionRole"] = "custom_convex_proxy"
        obj["Aerathea.ArtifactStatus"] = "candidate"
    return [head, shaft, pommel]


def triangle_count(obj: bpy.types.Object) -> int:
    if obj.type != "MESH":
        return 0
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def bounds_cm(objects: list[bpy.types.Object]) -> tuple[list[float], list[float], list[float]]:
    points = [obj.matrix_world @ Vector(corner) for obj in objects if obj.type == "MESH" for corner in obj.bound_box]
    minimum = [min(point[index] for point in points) / CM for index in range(3)]
    maximum = [max(point[index] for point in points) / CM for index in range(3)]
    extent = [maximum[index] - minimum[index] for index in range(3)]
    return minimum, maximum, extent


def export_selected(objects: list[bpy.types.Object], path: Path, kind: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        if obj.type == "MESH":
            obj.hide_set(False)
            obj.select_set(True)
    bpy.context.view_layer.objects.active = next(obj for obj in objects if obj.type == "MESH")
    if kind == "fbx":
        bpy.ops.export_scene.fbx(
            filepath=str(path),
            use_selection=True,
            object_types={"MESH"},
            apply_unit_scale=True,
            apply_scale_options="FBX_SCALE_UNITS",
            axis_forward="-Y",
            axis_up="Z",
            use_mesh_modifiers=True,
            mesh_smooth_type="FACE",
            add_leaf_bones=False,
            bake_anim=False,
            path_mode="AUTO",
        )
    elif kind == "glb":
        bpy.ops.export_scene.gltf(filepath=str(path), export_format="GLB", use_selection=True, export_apply=True, export_materials="EXPORT")
    else:
        raise ValueError(kind)
    bpy.ops.object.select_all(action="DESELECT")


def look_at(obj: bpy.types.Object, target: tuple[float, float, float]) -> None:
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()


def add_area(name: str, location: tuple[float, float, float], energy: float, size: float, color: tuple[float, float, float], target=(0.0, 0.0, 0.9)) -> bpy.types.Object:
    data = bpy.data.lights.new(name, "AREA")
    data.energy = energy
    data.shape = "DISK"
    data.size = size
    data.color = color
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    look_at(obj, target)
    return obj


def add_review_scene() -> None:
    review_collection = get_collection("SB_A04_REVIEW")
    bpy.ops.mesh.primitive_plane_add(size=12.0, location=(0.0, 0.0, -0.0003))
    ground = bpy.context.object
    ground.name = "SB_A04_ReviewGround"
    ground_material = bpy.data.materials.new("M_SB_A04_ReviewGround")
    ground_material.use_nodes = True
    ground_bsdf = ground_material.node_tree.nodes.get("Principled BSDF")
    ground_bsdf.inputs["Base Color"].default_value = (0.72, 0.68, 0.58, 1.0)
    ground_bsdf.inputs["Roughness"].default_value = 0.95
    ground.data.materials.append(ground_material)
    move_to_collection(ground, review_collection)
    add_area("SB_A04_Key", (-2.5, -3.7, 4.0), 620.0, 3.2, (1.0, 0.78, 0.56), target=(0.0, 0.0, 1.05))
    add_area("SB_A04_Fill", (3.0, -2.0, 2.8), 330.0, 4.0, (0.46, 0.66, 1.0), target=(0.0, 0.0, 1.0))
    add_area("SB_A04_Rim", (-1.2, 3.0, 3.6), 470.0, 2.8, (0.30, 0.54, 1.0), target=(0.0, 0.0, 1.25))


def save_and_export(lods: dict[int, list[bpy.types.Object]], collision: list[bpy.types.Object]) -> dict[str, Any]:
    BLENDER_ROOT.mkdir(parents=True, exist_ok=True)
    EXPORT_ROOT.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH), compress=True)
    exports: dict[str, Any] = {}
    for lod, objects in lods.items():
        path = EXPORT_ROOT / (f"{ASSET_ID}.fbx" if lod == 0 else f"{ASSET_ID}_LOD{lod}.fbx")
        payload = objects + (collision if lod == 0 else [])
        export_selected(payload, path, "fbx")
        exports[f"LOD{lod}_FBX"] = {"path": rel(path), "sha256": sha256(path), "bytes": path.stat().st_size}
    glb_path = EXPORT_ROOT / f"{ASSET_ID}.glb"
    try:
        export_selected(lods[0], glb_path, "glb")
        exports["LOD0_GLB"] = {"path": rel(glb_path), "sha256": sha256(glb_path), "bytes": glb_path.stat().st_size, "status": "complete"}
    except RuntimeError as error:
        # The distribution Blender in this environment omits numpy from its
        # glTF add-on.  Preserve the completed source/FBXs and let the approved
        # official Blender runtime perform the isolated GLB closeout.
        exports["LOD0_GLB"] = {
            "path": rel(glb_path),
            "status": "pending_official_blender_runtime",
            "environment_error": str(error).splitlines()[-1] if str(error).splitlines() else str(error),
        }
    return exports


def main() -> int:
    evidence = load_authority()
    texture_manifest = create_texture_package(evidence)
    clear_scene()
    configure_scene()
    materials = create_materials()

    lod_objects: dict[int, list[bpy.types.Object]] = {}
    lod_collections: dict[int, bpy.types.Collection] = {}
    for lod in range(4):
        collection, objects = build_lod(evidence, materials, lod)
        lod_collections[lod] = collection
        lod_objects[lod] = objects
    collision_collection = get_collection("SB_A04_COLLISION", hide_render=True)
    collision = add_collision(collision_collection)
    add_review_scene()

    exports = save_and_export(lod_objects, collision)
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH), compress=True)

    lod_metrics: dict[str, Any] = {}
    for lod, objects in lod_objects.items():
        minimum, maximum, extent = bounds_cm(objects)
        lod_metrics[f"LOD{lod}"] = {
            "objects": len(objects),
            "triangles": sum(triangle_count(obj) for obj in objects),
            "bounds_min_cm": minimum,
            "bounds_max_cm": maximum,
            "bounds_extent_cm": extent,
        }
    manifest = {
        "schema": "aerathea.siegebreaker_a04_build_manifest.v1",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "status": "candidate",
        "source": rel(SOURCE),
        "source_sha256": sha256(SOURCE),
        "fresh_evidence_manifest": rel(EVIDENCE_MANIFEST),
        "pre_geometry_audit": rel(PRE_GEOMETRY_AUDIT),
        "source_only_inputs": True,
        "prior_hammer_candidate_inputs": [],
        "blend": {"path": rel(BLEND_PATH), "sha256": sha256(BLEND_PATH), "bytes": BLEND_PATH.stat().st_size},
        "numeric_authority": {
            "overall_bounds_cm": [52.0, 32.0, 170.0],
            "head_interval_cm": [132.0, 170.0],
            "shaft_interval_cm": [14.0, 132.0],
            "grip_interval_cm": [18.0, 60.0],
            "pommel_interval_cm": [0.0, 18.0],
            "shaft_diameter_cm": 5.0,
            "pommel_max_width_cm": 11.0,
        },
        "visible_construction": {
            "method": "closed per-row source-contour facade meshes with exact source-pixel UV lineage",
            "selection_method": "source_priority",
            "source_scope": "component_isolated",
            "averaging": False,
            "analytic_replacement": False,
            "filtered_resampling": False,
            "components": list(evidence["primary_components"].keys()),
            "secondary_view_components": {
                view: list(components.keys()) for view, components in evidence["secondary_components"].items()
            },
        },
        "hidden_interpretation": [
            "backing volume and hidden surface continuation",
            "internal head core/socket closure",
            "PBR normal, ORM, and restrained emission response",
            "LOD simplification and collision proxies",
        ],
        "materials": MATERIAL_ORDER,
        "texture_manifest": rel(TEXTURE_MANIFEST),
        "texture_maps": 20,
        "visible_source_rgb_exact_all_families": texture_manifest["visible_source_rgb_exact_all_families"],
        "lod_metrics": lod_metrics,
        "collision": [obj.name for obj in collision],
        "exports": exports,
        "unreal_authority": False,
        "fully_game_ready": False,
    }
    BUILD_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(BLEND_PATH)
    print(BUILD_MANIFEST)
    for lod, metrics in lod_metrics.items():
        print(lod, "triangles", metrics["triangles"], "bounds", [round(value, 4) for value in metrics["bounds_extent_cm"]])
    print("A04 BUILD COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
