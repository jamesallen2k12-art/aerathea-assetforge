#!/usr/bin/env python3
"""Build Blood Axe cairn target A1 DCC source candidate.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_target_a1.py

This build is targeted at the clearer BloodAxe A1 concept image:
docs/assets/visual_canon/BloodAxeCairnTargets_A01/VC_GIA_BloodAxe_CairnTarget_A1.png

The output is a DCC source candidate for concept-geometry review. It should not
be treated as fully game-ready or imported to Unreal until the side-by-side
comparison against the source target passes visual approval.
"""

from __future__ import annotations

import math
import sys
from array import array
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
TEXTURE_ROOT = SOURCE_ROOT / "Textures"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "SM_GIA_BloodAxeCairnTarget_A1_A01"

ASSET_NAME = "SM_GIA_BloodAxeCairnTarget_A1_A01"
REL_PATH = f"Props/Giants/BloodAxe/CairnTargets/A1/{ASSET_NAME}"
UNREAL_PATH = f"/Game/Aerathea/Props/Giants/BloodAxe/CairnTargets/A1/{ASSET_NAME}"
SOURCE_TARGET = "docs/assets/visual_canon/BloodAxeCairnTargets_A01/VC_GIA_BloodAxe_CairnTarget_A1.png"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def deterministic_noise(x: int, y: int, seed: int) -> float:
    value = (x * 374761393 + y * 668265263 + seed * 2654435761) & 0xFFFFFFFF
    value = (value ^ (value >> 13)) * 1274126177 & 0xFFFFFFFF
    return ((value ^ (value >> 16)) & 0xFFFF) / 65535.0


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def save_texture(path: Path, width: int, height: int, pixels: array) -> None:
    ensure_dir(path.parent)
    image = bpy.data.images.new(path.stem, width=width, height=height, alpha=True, float_buffer=False)
    image.pixels.foreach_set(pixels)
    image.filepath_raw = str(path)
    image.file_format = "PNG"
    image.save()
    bpy.data.images.remove(image)


def generate_texture_set(
    label: str,
    base: tuple[float, float, float],
    accent: tuple[float, float, float],
    seed: int,
    profile: str,
) -> dict[str, Path]:
    texture_dir = TEXTURE_ROOT / REL_PATH
    ensure_dir(texture_dir)
    width = 1024
    height = 1024
    bc = array("f")
    normal = array("f")
    orm = array("f")
    for y in range(height):
        for x in range(width):
            n1 = deterministic_noise(x, y, seed)
            n2 = deterministic_noise(x // 5, y // 5, seed + 17)
            n3 = deterministic_noise(x // 19, y // 13, seed + 29)
            vein_threshold = 0.982 if profile == "stone" else 0.935
            chip_threshold = 0.993 if profile == "stone" else 0.982
            crack_threshold = 0.988 if profile == "stone" else 0.965
            vein = 1.0 if deterministic_noise(x // 31, y // 17, seed + 41) > vein_threshold else 0.0
            chip = 1.0 if deterministic_noise(x // 11, y // 17, seed + 71) > chip_threshold else 0.0
            streak = abs(math.sin(((x * 0.018) + (y * 0.006) + seed) % math.tau))
            crack = 1.0 if deterministic_noise((x + y) // 23, (y - x) // 29, seed + 87) > crack_threshold else 0.0
            dust = deterministic_noise(x // 47, y // 43, seed + 119)
            mix = ((n1 * 0.30) + (n2 * 0.22) + (n3 * 0.12) + (vein * 0.08) + (chip * 0.06)) * 0.66
            if profile == "stone":
                mix *= 0.52
            color = (
                base[0] * (1.0 - mix) + accent[0] * mix,
                base[1] * (1.0 - mix) + accent[1] * mix,
                base[2] * (1.0 - mix) + accent[2] * mix,
            )

            alpha = 1.0
            if profile == "stone":
                shadow = 1.0 - (crack * 0.28) - (vein * 0.07)
                warm_edge = chip * (0.09 + streak * 0.05)
                color = (
                    clamp(color[0] * shadow + warm_edge),
                    clamp(color[1] * shadow + warm_edge * 0.90),
                    clamp(color[2] * shadow + warm_edge * 0.70),
                )
            elif profile == "earth":
                ash = 0.10 + dust * 0.16
                wet = 1.0 - (n3 * 0.18)
                color = (
                    clamp(color[0] * wet + ash * 0.48),
                    clamp(color[1] * wet + ash * 0.44),
                    clamp(color[2] * wet + ash * 0.36),
                )
            elif profile == "rawhide":
                fiber = 0.82 + streak * 0.20
                grime = 1.0 - (crack * 0.18) - (n3 * 0.08)
                color = (clamp(color[0] * fiber * grime), clamp(color[1] * fiber * grime), clamp(color[2] * fiber * grime))
            elif profile == "red":
                wear = 0.56 + (n2 * 0.24) - (chip * 0.20) - (crack * 0.22)
                oxidized = (0.28 + n1 * 0.18, 0.030 + n2 * 0.035, 0.020 + n3 * 0.028)
                color = (
                    clamp((color[0] * wear) + oxidized[0] * (1.0 - wear)),
                    clamp((color[1] * wear) + oxidized[1] * (1.0 - wear)),
                    clamp((color[2] * wear) + oxidized[2] * (1.0 - wear)),
                )
                alpha = clamp(0.48 + (wear * 0.26) - (chip * 0.18) - (crack * 0.14) + (streak * 0.04))
            bc.extend((clamp(color[0]), clamp(color[1]), clamp(color[2]), alpha))

            bump_strength = 0.24 if profile == "stone" else 0.18 if profile == "earth" else 0.12
            bump = ((n1 - 0.5) * bump_strength) + ((n2 - 0.5) * 0.08) - (crack * 0.08) + (chip * 0.05)
            normal.extend((clamp(0.5 + bump), clamp(0.5 + (deterministic_noise(x, y, seed + 101) - 0.5) * 0.12), 1.0, 1.0))
            occlusion = 0.50 + (1.0 - n2) * 0.28 - crack * 0.10
            roughness_base = 0.92 if profile in {"stone", "earth", "red"} else 0.82
            roughness = roughness_base + n1 * 0.07 + crack * 0.04
            orm.extend((clamp(occlusion), clamp(roughness), 0.0, 1.0))

    file_label = label.replace(" ", "")
    paths = {
        "bc": texture_dir / f"T_GIA_BloodAxeCairnTarget_A1_A01_{file_label}_BC.png",
        "n": texture_dir / f"T_GIA_BloodAxeCairnTarget_A1_A01_{file_label}_N.png",
        "orm": texture_dir / f"T_GIA_BloodAxeCairnTarget_A1_A01_{file_label}_ORM.png",
    }
    save_texture(paths["bc"], width, height, bc)
    save_texture(paths["n"], width, height, normal)
    save_texture(paths["orm"], width, height, orm)
    return paths


def generate_textures() -> dict[str, dict[str, Path]]:
    return {
        "stone": generate_texture_set("Stone", (0.12, 0.118, 0.105), (0.40, 0.36, 0.28), 5103, "stone"),
        "earth": generate_texture_set("Earth", (0.15, 0.095, 0.060), (0.36, 0.235, 0.135), 6207, "earth"),
        "rawhide": generate_texture_set("Rawhide", (0.24, 0.135, 0.055), (0.46, 0.275, 0.115), 7301, "rawhide"),
        "red": generate_texture_set("RedPaint", (0.20, 0.022, 0.016), (0.50, 0.060, 0.034), 8409, "red"),
    }


def make_texture_material(name: str, textures: dict[str, Path], roughness: float, review_color: tuple[float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    is_red_paint = name.endswith("_RedPaint")
    material.diffuse_color = (review_color[0], review_color[1], review_color[2], 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        return material

    material["Aerathea.TextureBC"] = str(textures["bc"].relative_to(ROOT))
    material["Aerathea.TextureN"] = str(textures["n"].relative_to(ROOT))
    material["Aerathea.TextureORM"] = str(textures["orm"].relative_to(ROOT))
    material["Aerathea.MaterialPass"] = "dcc_texture_integration_proof"
    if is_red_paint:
        material["Aerathea.SurfaceTreatment"] = "worn_oxide_pigment_surface_decal"
        material.blend_method = "OPAQUE"
        material.show_transparent_back = False

    def load_image_node(path: Path, label: str, color_space: str) -> bpy.types.Node:
        image = bpy.data.images.load(str(path), check_existing=True)
        try:
            image.colorspace_settings.name = color_space
        except TypeError:
            pass
        node = nodes.new(type="ShaderNodeTexImage")
        node.name = label
        node.label = label
        node.image = image
        return node

    bc_node = load_image_node(textures["bc"], f"{name}_BC", "sRGB")
    bc_node.location = (-680, 180)
    n_node = load_image_node(textures["n"], f"{name}_N", "Non-Color")
    n_node.location = (-680, -80)
    orm_node = load_image_node(textures["orm"], f"{name}_ORM", "Non-Color")
    orm_node.location = (-680, -340)
    normal_map = nodes.new(type="ShaderNodeNormalMap")
    normal_map.name = f"{name}_NormalMap"
    normal_map.inputs["Strength"].default_value = 0.45
    normal_map.location = (-360, -80)
    separate = nodes.new(type="ShaderNodeSeparateRGB")
    separate.name = f"{name}_ORMSplit"
    separate.location = (-360, -340)

    links = material.node_tree.links
    links.new(bc_node.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(n_node.outputs["Color"], normal_map.inputs["Color"])
    links.new(normal_map.outputs["Normal"], bsdf.inputs["Normal"])
    links.new(orm_node.outputs["Color"], separate.inputs["Image"])
    links.new(separate.outputs["G"], bsdf.inputs["Roughness"])
    bsdf.inputs["Base Color"].default_value = (review_color[0], review_color[1], review_color[2], 1.0)
    if is_red_paint and "Alpha" in bsdf.inputs:
        bsdf.inputs["Alpha"].default_value = 1.0
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = 0.0
    return material


def make_flat_material(name: str, roughness: float, color: tuple[float, float, float], purpose: str) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = (color[0], color[1], color[2], 1.0)
    material.use_nodes = True
    material["Aerathea.MaterialPass"] = purpose
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = (color[0], color[1], color[2], 1.0)
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = 0.0
    return material


def make_materials(texture_paths: dict[str, dict[str, Path]]) -> dict[str, bpy.types.Material]:
    return {
        "stone": make_texture_material("M_GIA_BloodAxeCairnTarget_A1_A01_Stone", texture_paths["stone"], 0.94, (0.18, 0.175, 0.155)),
        "stone_light": make_flat_material(
            "M_GIA_BloodAxeCairnTarget_A1_A01_StoneFacetLight",
            0.9,
            (0.32, 0.29, 0.22),
            "dcc_hand_painted_edge_highlight_proof",
        ),
        "stone_dark": make_flat_material(
            "M_GIA_BloodAxeCairnTarget_A1_A01_StoneFacetDark",
            0.94,
            (0.075, 0.070, 0.060),
            "dcc_hand_painted_crack_shadow_proof",
        ),
        "earth": make_texture_material("M_GIA_BloodAxeCairnTarget_A1_A01_Earth", texture_paths["earth"], 0.96, (0.19, 0.12, 0.075)),
        "rawhide": make_texture_material("M_GIA_BloodAxeCairnTarget_A1_A01_Rawhide", texture_paths["rawhide"], 0.92, (0.30, 0.17, 0.07)),
        "red": make_texture_material("M_GIA_BloodAxeCairnTarget_A1_A01_RedPaint", texture_paths["red"], 0.97, (0.26, 0.024, 0.017)),
    }


def make_collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    collection.hide_viewport = hidden
    collection.hide_render = hidden
    return collection


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def set_active(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def roughen_mesh(obj: bpy.types.Object, amount: float, seed: int) -> None:
    for index, vertex in enumerate(obj.data.vertices):
        n1 = deterministic_noise(index, seed, seed + 13) - 0.5
        n2 = deterministic_noise(seed, index, seed + 29) - 0.5
        n3 = deterministic_noise(index + 5, seed + 7, seed + 43) - 0.5
        vertex.co.x += n1 * amount
        vertex.co.y += n2 * amount
        vertex.co.z += n3 * amount * 0.75


def add_rough_box(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
    bevel_scale: float = 0.055,
    rough_scale: float = 0.12,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bevel_width = max(0.45, min(dimensions) * bevel_scale)
    bevel = obj.modifiers.new(f"{name}_BrokenEdgeBevel", "BEVEL")
    bevel.width = bevel_width
    bevel.segments = 1
    bevel.affect = "EDGES"
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    roughen_mesh(obj, min(dimensions) * rough_scale, seed)
    bpy.ops.object.shade_flat()
    move_to_collection(obj, collection)
    return obj


def add_tapered_slab(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
    top_scale_x: float = 0.72,
    top_scale_y: float = 0.86,
    top_offset: tuple[float, float] = (0.0, 0.0),
    bevel_scale: float = 0.045,
    rough_scale: float = 0.115,
) -> bpy.types.Object:
    width, depth, height = dimensions
    bx = width * 0.5
    by = depth * 0.5
    tx = width * top_scale_x * 0.5
    ty = depth * top_scale_y * 0.5
    ox, oy = top_offset
    verts = [
        (-bx, -by, -height * 0.5),
        (bx, -by, -height * 0.5),
        (bx * 0.94, by, -height * 0.5),
        (-bx * 0.88, by, -height * 0.5),
        (-tx + ox, -ty + oy, height * 0.5),
        (tx + ox, -ty + oy, height * 0.5),
        (tx * 0.86 + ox, ty + oy, height * 0.5),
        (-tx * 0.94 + ox, ty + oy, height * 0.5),
    ]
    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (3, 7, 4, 0),
    ]
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    collection.objects.link(obj)
    set_active(obj)
    bevel_width = max(0.35, min(dimensions) * bevel_scale)
    bevel = obj.modifiers.new(f"{name}_BrokenEdgeBevel", "BEVEL")
    bevel.width = bevel_width
    bevel.segments = 1
    bevel.affect = "EDGES"
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    roughen_mesh(obj, min(dimensions) * rough_scale, seed)
    bpy.ops.object.shade_flat()
    return obj


def add_fractured_slab(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    outline: list[tuple[float, float]],
    seed: int,
    rough_scale: float = 0.10,
) -> bpy.types.Object:
    """Create a low-poly extruded stone slab with an irregular X/Z outline."""
    width, depth, height = dimensions
    front_y = -depth * 0.5
    back_y = depth * 0.5
    verts: list[tuple[float, float, float]] = []
    front: list[int] = []
    back: list[int] = []
    for index, (nx, nz) in enumerate(outline):
        x_noise = (deterministic_noise(index, seed, seed + 11) - 0.5) * width * 0.045
        z_noise = (deterministic_noise(seed, index, seed + 17) - 0.5) * height * 0.045
        front_y_noise = (deterministic_noise(index, seed + 19, seed + 23) - 0.5) * depth * 0.05
        back_y_noise = (deterministic_noise(index, seed + 29, seed + 31) - 0.5) * depth * 0.04
        x = nx * width + x_noise
        z = nz * height + z_noise
        front.append(len(verts))
        verts.append((x, front_y + front_y_noise, z))
        back.append(len(verts))
        back_x = x * (0.92 + deterministic_noise(index, seed + 3, seed + 31) * 0.08)
        back_z = z * (0.94 + deterministic_noise(index, seed + 5, seed + 37) * 0.06)
        verts.append((back_x, back_y + back_y_noise, back_z))

    front_center = len(verts)
    verts.append((0.0, front_y - max(0.8, depth * 0.05), 0.0))
    back_center = len(verts)
    verts.append((0.0, back_y + max(0.8, depth * 0.05), 0.0))

    faces: list[tuple[int, ...]] = []
    for index in range(len(outline)):
        next_index = (index + 1) % len(outline)
        faces.append((front_center, front[index], front[next_index]))
        faces.append((back_center, back[next_index], back[index]))
        faces.append((front[index], back[index], back[next_index], front[next_index]))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    collection.objects.link(obj)
    set_active(obj)
    bevel = obj.modifiers.new(f"{name}_BrokenEdgeBevel", "BEVEL")
    bevel.width = max(0.35, min(dimensions) * 0.035)
    bevel.segments = 1
    bevel.affect = "EDGES"
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    roughen_mesh(obj, min(dimensions) * rough_scale, seed)
    bpy.ops.object.shade_flat()
    return obj


def add_paint_strip(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
) -> bpy.types.Object:
    return add_rough_box(name, collection, material, location, dimensions, rotation, seed, bevel_scale=0.16, rough_scale=0.035)


def add_surface_stroke(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
    treatment: str,
    segments: int = 13,
    min_width: float = 0.10,
    edge_noise: float = 0.72,
    center_noise_scale: float = 0.36,
    gap_threshold: float = 0.92,
) -> bpy.types.Object:
    length, surface_offset, stroke_width = dimensions
    verts: list[tuple[float, float, float]] = []
    faces: list[tuple[int, int, int, int]] = []
    for index in range(segments + 1):
        t = index / segments
        x = (-length * 0.5) + (length * t)
        taper = 0.30 + math.sin(t * math.pi) * 0.66
        upper_noise = (deterministic_noise(index, seed, seed + 3) - 0.5) * stroke_width * edge_noise
        lower_noise = (deterministic_noise(seed, index, seed + 7) - 0.5) * stroke_width * edge_noise
        center_noise = (deterministic_noise(index, seed + 11, seed + 13) - 0.5) * stroke_width * center_noise_scale
        half_width = max(stroke_width * taper * 0.5, stroke_width * min_width)
        verts.append((x, surface_offset, center_noise - half_width + lower_noise))
        verts.append((x, surface_offset, center_noise + half_width + upper_noise))

    for index in range(segments):
        if deterministic_noise(index, seed + 23, seed + 29) > gap_threshold:
            continue
        faces.append((index * 2, index * 2 + 1, index * 2 + 3, index * 2 + 2))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    obj["Aerathea.SurfaceTreatment"] = treatment
    try:
        obj.visible_shadow = False
    except AttributeError:
        pass
    collection.objects.link(obj)
    return obj


def add_worn_paint_patch(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
) -> bpy.types.Object:
    return add_surface_stroke(
        name,
        collection,
        material,
        location,
        dimensions,
        rotation,
        seed,
        "worn_oxide_pigment_stain_no_thickness",
        segments=17,
        min_width=0.08,
        edge_noise=0.62,
        center_noise_scale=0.30,
        gap_threshold=0.94,
    )


def add_surface_patch(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    outline: list[tuple[float, float]],
    seed: int,
    treatment: str,
) -> bpy.types.Object:
    width, surface_offset, height = dimensions
    verts: list[tuple[float, float, float]] = []
    sx = 0.032 if width > 24 else 0.018
    sz = 0.032 if height > 24 else 0.018
    for index, (nx, nz) in enumerate(outline):
        x = nx * width + (deterministic_noise(index, seed, seed + 13) - 0.5) * width * sx
        z = nz * height + (deterministic_noise(seed, index, seed + 29) - 0.5) * height * sz
        verts.append((x, surface_offset, z))
    faces: list[tuple[int, ...]] = [tuple(range(len(outline)))]
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    obj["Aerathea.SurfaceTreatment"] = treatment
    try:
        obj.visible_shadow = False
    except AttributeError:
        pass
    collection.objects.link(obj)
    return obj


def add_cylinder_between(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    start: tuple[float, float, float],
    end: tuple[float, float, float],
    radius: float,
    seed: int,
    vertices: int = 8,
) -> bpy.types.Object:
    start_v = Vector(start)
    end_v = Vector(end)
    delta = end_v - start_v
    length = delta.length
    if length <= 0.01:
        raise ValueError(f"{name} has no length")
    midpoint = start_v + (delta * 0.5)
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=length, location=midpoint)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = delta.to_track_quat("Z", "Y").to_euler()
    obj.data.materials.append(material)
    set_active(obj)
    roughen_mesh(obj, radius * 0.22, seed)
    bpy.ops.object.shade_flat()
    move_to_collection(obj, collection)
    return obj


def add_curved_rope(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    points: list[tuple[float, float, float]],
    radius: float,
    seed: int,
) -> bpy.types.Object:
    curve = bpy.data.curves.new(f"{name}_Curve", "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 2
    curve.bevel_depth = radius
    curve.bevel_resolution = 1
    curve.fill_mode = "FULL"
    spline = curve.splines.new("POLY")
    spline.points.add(len(points) - 1)
    for point, co in zip(spline.points, points):
        point.co = (co[0], co[1], co[2], 1.0)

    obj = bpy.data.objects.new(name, curve)
    obj.data.materials.append(material)
    collection.objects.link(obj)
    set_active(obj)
    bpy.ops.object.convert(target="MESH")
    obj = bpy.context.object
    obj.name = name
    roughen_mesh(obj, radius * 0.18, seed)
    bpy.ops.object.shade_flat()
    return obj


def add_surface_facet(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    dimensions: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
) -> bpy.types.Object:
    facet_outline = [
        (-0.50, -0.34),
        (-0.27, -0.50),
        (-0.04, -0.41),
        (0.24, -0.49),
        (0.50, -0.18),
        (0.38, 0.08),
        (0.47, 0.30),
        (0.12, 0.51),
        (-0.18, 0.40),
        (-0.44, 0.20),
    ]
    return add_fractured_slab(
        name,
        collection,
        material,
        location,
        dimensions,
        rotation,
        facet_outline,
        seed,
        rough_scale=0.035,
    )


def add_small_stone(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    rotation: tuple[float, float, float],
    seed: int,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    roughen_mesh(obj, min(scale) * 0.18, seed)
    bpy.ops.object.shade_flat()
    move_to_collection(obj, collection)
    return obj


def add_irregular_ground(
    name: str,
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    radius_x: float,
    radius_y: float,
    depth: float,
    segments: int,
    seed: int,
    location: tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> bpy.types.Object:
    verts: list[tuple[float, float, float]] = []
    bottom: list[int] = []
    top: list[int] = []
    for index in range(segments):
        angle = (math.tau * index) / segments
        front_bias = 0.82 if math.sin(angle) < -0.45 else 1.0
        rear_bias = 1.12 if math.sin(angle) > 0.50 else 1.0
        n = 0.78 + deterministic_noise(index, seed, seed + 5) * 0.32
        x = math.cos(angle) * radius_x * n
        y = math.sin(angle) * radius_y * (0.78 + deterministic_noise(seed, index, seed + 9) * 0.27) * front_bias * rear_bias
        bottom.append(len(verts))
        verts.append((x, y, 0.0))
        top.append(len(verts))
        verts.append((x * 0.93, y * 0.91, depth + deterministic_noise(index, seed + 3, seed + 11) * 3.0))
    bottom_center = len(verts)
    verts.append((0.0, 0.0, 0.0))
    top_center = len(verts)
    verts.append((0.0, 0.0, depth + 1.5))
    faces: list[tuple[int, ...]] = []
    for index in range(segments):
        next_index = (index + 1) % segments
        faces.append((bottom[index], bottom[next_index], top[next_index], top[index]))
        faces.append((bottom_center, bottom[index], bottom[next_index]))
        faces.append((top_center, top[next_index], top[index]))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.data.materials.append(material)
    collection.objects.link(obj)
    return obj


def add_lod_ground(collection: bpy.types.Collection, materials: dict[str, bpy.types.Material], lod: int) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    segments = 42 if lod == 0 else 28 if lod == 1 else 18 if lod == 2 else 12
    objects.append(add_irregular_ground(f"LOD{lod}_IrregularMudAshTerrainContact", collection, materials["earth"], 168.0, 124.0, 8.0, segments, 101 + lod))
    if lod <= 1:
        objects.append(add_irregular_ground(f"LOD{lod}_FrontBrokenMudLip", collection, materials["earth"], 118.0, 52.0, 4.5, 20, 121 + lod, (-20.0, -70.0, 5.0)))
        objects.append(add_irregular_ground(f"LOD{lod}_RearAshAndStoneScatter", collection, materials["earth"], 98.0, 66.0, 4.0, 18, 141 + lod, (12.0, 78.0, 5.0)))
    return objects


def build_asset_lod(collection: bpy.types.Collection, materials: dict[str, bpy.types.Material], lod: int) -> list[bpy.types.Object]:
    objects = add_lod_ground(collection, materials, lod)
    prefix = f"LOD{lod}"
    detail = lod == 0
    mid = lod <= 1
    low = lod <= 2

    # Front proportions are locked to the traced A1 guide in
    # docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/*_A1_FrontTraceGuide.png.
    dominant_painted_outline = [
        (-0.40, 0.37),
        (-0.02, 0.50),
        (0.34, 0.32),
        (0.50, -0.08),
        (0.26, -0.50),
        (-0.20, -0.45),
        (-0.50, -0.06),
    ]
    tall_crag_outline = [
        (-0.33, 0.50),
        (0.13, 0.41),
        (0.50, -0.41),
        (-0.04, -0.50),
        (-0.50, 0.01),
    ]
    support_crag_outline = [
        (-0.29, 0.50),
        (0.35, 0.40),
        (0.50, -0.27),
        (0.02, -0.50),
        (-0.50, -0.28),
    ]
    low_slab_outline = [
        (-0.52, -0.42),
        (-0.37, -0.53),
        (-0.12, -0.46),
        (0.09, -0.54),
        (0.38, -0.42),
        (0.55, -0.14),
        (0.43, 0.11),
        (0.51, 0.31),
        (0.18, 0.52),
        (-0.07, 0.43),
        (-0.30, 0.53),
        (-0.50, 0.20),
        (-0.40, -0.03),
    ]
    front_slab_rotation = (math.radians(-42), math.radians(-5), math.radians(0))
    front_paint_y = -91

    fractured_specs = [
        (
            "DominantPaintedFrontSlab",
            (-26, -60, 68),
            (145, 22, 132),
            front_slab_rotation,
            dominant_painted_outline,
            201,
        ),
        (
            "TallRearOathSlab",
            (4, 50, 102),
            (96, 24, 174),
            (math.radians(-10), math.radians(5), math.radians(0)),
            tall_crag_outline,
            202,
        ),
        (
            "RightUprightSupportStone",
            (86, -8, 58),
            (52, 22, 96),
            (math.radians(-1), math.radians(-8), math.radians(0)),
            support_crag_outline,
            206,
        ),
        (
            "RightRearSupportStone",
            (106, 30, 35),
            (24, 16, 44),
            (math.radians(-7), math.radians(5), math.radians(11)),
            support_crag_outline,
            207,
        ),
    ]
    secondary_fractured_specs = [
        ("LeftBundledStackLowSlab", (-102, -34, 34), (78, 32, 24), (math.radians(2), math.radians(-7), math.radians(5)), low_slab_outline, 203),
        ("LeftBundledStackMidSlab", (-110, -34, 56), (72, 30, 26), (math.radians(-1), math.radians(5), math.radians(-7)), low_slab_outline, 204),
        ("LeftBundledStackTopSlab", (-98, -34, 80), (60, 26, 24), (math.radians(4), math.radians(-5), math.radians(12)), low_slab_outline, 205),
        ("RearLowCounterweight", (-42, 54, 42), (86, 28, 30), (math.radians(-4), math.radians(4), math.radians(8)), low_slab_outline, 208),
    ]
    primary_specs: list[tuple[str, tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], int]] = []
    if low:
        secondary_fractured_specs.extend(
            [
                ("FrontBrokenFootStone", (24, -96, 18), (68, 22, 15), (math.radians(3), math.radians(4), math.radians(-5)), low_slab_outline, 209),
                ("RearGroundLockStone", (12, 92, 24), (76, 22, 20), (math.radians(2), math.radians(-4), math.radians(2)), low_slab_outline, 210),
            ]
        )
    if mid:
        secondary_fractured_specs.extend(
            [
                ("LeftBackBrokenShard", (-130, 16, 42), (22, 18, 54), (math.radians(-7), math.radians(8), math.radians(-18)), support_crag_outline, 211),
                ("RearNeedleShardLeft", (-24, 60, 84), (18, 14, 74), (math.radians(-11), math.radians(-7), math.radians(7)), tall_crag_outline, 212),
                ("RearNeedleShardRight", (66, 74, 44), (10, 9, 26), (math.radians(8), math.radians(5), math.radians(14)), support_crag_outline, 213),
                ("MainSlabLeftEmbeddedSupport", (-70, -74, 34), (32, 18, 24), (math.radians(-22), math.radians(-7), math.radians(-20)), low_slab_outline, 221),
                ("MainSlabRightEmbeddedSupport", (48, -88, 28), (38, 18, 20), (math.radians(-15), math.radians(7), math.radians(-4)), low_slab_outline, 222),
            ]
        )
    if detail:
        secondary_fractured_specs.extend(
            [
                ("FrontLeftGroundShard", (-62, -96, 20), (42, 19, 22), (math.radians(5), math.radians(7), math.radians(-23)), low_slab_outline, 214),
                ("FarRightSmallSupportShard", (132, -34, 25), (12, 11, 24), (math.radians(5), math.radians(-8), math.radians(18)), support_crag_outline, 215),
                ("BackLeftButtressShard", (-98, 78, 34), (48, 24, 38), (math.radians(-8), math.radians(-4), math.radians(-14)), low_slab_outline, 216),
                ("BackRightButtressShard", (96, 78, 30), (32, 19, 30), (math.radians(5), math.radians(7), math.radians(13)), support_crag_outline, 217),
            ]
        )

    for label, location, dimensions, rotation, outline, seed in fractured_specs:
        rough_scale = 0.16 if label.startswith("Dominant") else 0.10
        objects.append(add_fractured_slab(f"{prefix}_Stone_{label}", collection, materials["stone"], location, dimensions, rotation, outline, seed + lod * 31, rough_scale=rough_scale))

    for label, location, dimensions, rotation, outline, seed in secondary_fractured_specs:
        objects.append(add_fractured_slab(f"{prefix}_Stone_{label}", collection, materials["stone"], location, dimensions, rotation, outline, seed + lod * 31, rough_scale=0.12))

    for label, location, dimensions, rotation, seed in primary_specs:
        objects.append(add_rough_box(f"{prefix}_Stone_{label}", collection, materials["stone"], location, dimensions, rotation, seed + lod * 31))

    if mid:
        facet_specs: list[tuple[str, tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], str, int]] = []
        for label, location, dimensions, rotation, material_key, seed in facet_specs:
            objects.append(add_surface_facet(f"{prefix}_StoneFacet_{label}", collection, materials[material_key], location, dimensions, rotation, seed + lod * 29))

    if mid:
        paint_band_outline = [
            (-0.54, 0.06),
            (-0.24, 0.36),
            (0.52, 0.20),
            (0.50, -0.08),
            (0.05, -0.26),
            (-0.46, -0.18),
        ]
        paint_stem_outline = [
            (-0.18, 0.50),
            (0.16, 0.42),
            (0.18, -0.44),
            (-0.12, -0.50),
            (-0.26, -0.05),
        ]
        paint_lower_outline = [
            (-0.52, 0.06),
            (-0.16, 0.24),
            (0.54, 0.14),
            (0.48, -0.10),
            (0.02, -0.26),
            (-0.45, -0.20),
        ]
        paint_patch_specs = [
            ("MainSlabUpperLeftPaintMask", (-34, front_paint_y, 98), (50, -0.62, 13), front_slab_rotation, paint_band_outline, 301),
            ("MainSlabCentralPaintMask", (-8, front_paint_y, 82), (16, -0.62, 66), front_slab_rotation, paint_stem_outline, 302),
            ("MainSlabLowerPaintMask", (8, front_paint_y, 51), (54, -0.62, 13), front_slab_rotation, paint_lower_outline, 303),
            ("LeftStackSubtleRedMask", (-105, -53, 66), (30, -0.62, 9), (math.radians(2), math.radians(-6), math.radians(5)), paint_lower_outline, 304),
            ("RearSlabTallWarPaintMask", (12, 14, 130), (13, -0.62, 50), (math.radians(-7), math.radians(5), math.radians(62)), paint_stem_outline, 305),
        ]
        if lod == 0:
            paint_patch_specs.extend(
                [
                    ("MainSlabAxeHeadBrokenMask", (-10, front_paint_y, 86), (26, -0.62, 16), front_slab_rotation, paint_band_outline, 307),
                    ("MainSlabBottomDripMask", (18, front_paint_y, 35), (10, -0.62, 22), front_slab_rotation, paint_stem_outline, 306),
                ]
            )
        for label, location, dimensions, rotation, outline, seed in paint_patch_specs:
            objects.append(
                add_surface_patch(
                    f"{prefix}_BloodAxePaint_{label}",
                    collection,
                    materials["red"],
                    location,
                    dimensions,
                    rotation,
                    outline,
                    seed + lod * 37,
                    "worn_oxide_pigment_mask_no_thickness",
                )
            )

        surface_overlay_specs: list[tuple[str, tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], str, int]] = []
        for label, location, dimensions, rotation, material_key, seed in surface_overlay_specs:
            objects.append(
                add_surface_stroke(
                    f"{prefix}_StoneSurface_{label}",
                    collection,
                    materials[material_key],
                    location,
                    dimensions,
                    rotation,
                    seed + lod * 41,
                    "stone_crack_or_edge_overlay_no_thickness",
                    segments=12,
                    min_width=0.10,
                    edge_noise=0.35,
                    center_noise_scale=0.18,
                    gap_threshold=0.97,
                )
            )

    if detail:
        rope_specs = [
            ("LeftStackWrapUpper", [(-132, -55, 78), (-112, -59, 81), (-88, -58, 79), (-70, -54, 75)], 1.10, 401),
            ("LeftStackWrapMid", [(-134, -55, 60), (-112, -59, 62), (-88, -58, 61), (-69, -54, 58)], 1.08, 402),
            ("LeftStackWrapLower", [(-130, -55, 43), (-108, -59, 45), (-88, -58, 44), (-72, -54, 41)], 0.95, 403),
            ("LeftStackShortVerticalTieA", [(-123, -56, 38), (-126, -59, 58), (-123, -57, 85)], 0.85, 407),
            ("LeftStackShortVerticalTieB", [(-83, -56, 39), (-80, -59, 60), (-84, -55, 82)], 0.85, 408),
            ("RightSupportWrapUpper", [(70, -36, 82), (89, -40, 86), (111, -35, 82)], 0.86, 405),
            ("RightSupportWrapLower", [(72, -36, 61), (90, -40, 64), (111, -35, 60)], 0.82, 409),
            ("RearCounterweightBinding", [(-66, 91, 50), (-36, 95, 52), (6, 92, 51)], 1.00, 406),
            ("RearSlabWaistWrap", [(-18, 24, 114), (8, 20, 120), (46, 24, 119)], 0.92, 410),
        ]
        for label, points, radius, seed in rope_specs:
            objects.append(add_curved_rope(f"{prefix}_RawhideRope_{label}", collection, materials["rawhide"], points, radius, seed))

        knot_specs = [
            ("LeftUpperKnotA", (-124, -56, 79), (3.5, 2.6, 3.2), 421),
            ("LeftUpperKnotB", (-84, -55, 77), (3.4, 2.5, 3.1), 422),
            ("LeftMiddleBindKnot", (-104, -56, 61), (3.6, 2.6, 3.2), 423),
            ("RightSupportKnot", (114, -35, 79), (3.2, 2.5, 3.1), 424),
            ("RearWrapKnot", (-26, 94, 51), (3.3, 2.6, 3.1), 425),
        ]
        for label, location, scale, seed in knot_specs:
            objects.append(
                add_small_stone(
                    f"{prefix}_RawhideKnot_{label}",
                    collection,
                    materials["rawhide"],
                    location,
                    scale,
                    (math.radians(seed % 17), math.radians(seed % 11), math.radians(seed % 29)),
                    seed,
                )
            )

        pebble_specs = [
            (-152, -82, 16, (18, 12, 8), 501),
            (-96, -106, 15, (20, 13, 8), 502),
            (-30, -118, 14, (14, 11, 7), 503),
            (70, -112, 16, (21, 12, 8), 504),
            (142, -82, 17, (16, 12, 9), 505),
            (182, 34, 18, (18, 13, 10), 506),
            (-182, 36, 17, (22, 14, 10), 507),
            (3, 97, 18, (18, 13, 9), 508),
            (-124, 125, 17, (21, 14, 10), 509),
            (-48, 148, 16, (17, 12, 8), 510),
            (52, 151, 16, (19, 13, 9), 511),
            (136, 118, 18, (22, 14, 10), 512),
        ]
        for index in range(42):
            angle = math.radians(205 + index * 7.5)
            radius_x = 86 + deterministic_noise(index, 18, 650) * 105
            radius_y = 66 + deterministic_noise(19, index, 651) * 62
            x = math.cos(angle) * radius_x
            y = math.sin(angle) * radius_y - 10
            z = 13 + deterministic_noise(index, 21, 652) * 8
            sx = 8 + deterministic_noise(index, 22, 653) * 16
            sy = 6 + deterministic_noise(index, 23, 654) * 10
            sz = 5 + deterministic_noise(index, 24, 655) * 9
            pebble_specs.append((x, y, z, (sx, sy, sz), 620 + index))
        for x, y, z, scale, seed in pebble_specs:
            objects.append(
                add_small_stone(
                    f"{prefix}_LooseGroundStone_{seed}",
                    collection,
                    materials["stone"],
                    (x, y, z),
                    scale,
                    (math.radians(seed % 17), math.radians(seed % 11), math.radians(seed % 29)),
                    seed,
                )
            )

    return objects


def add_collision_proxy(collection: bpy.types.Collection, material: bpy.types.Material) -> bpy.types.Object:
    obj = add_rough_box(
        f"UCX_{ASSET_NAME}_00",
        collection,
        material,
        (-8.0, 6.0, 72.0),
        (350.0, 286.0, 170.0),
        (0.0, 0.0, 0.0),
        9001,
        bevel_scale=0.01,
        rough_scale=0.0,
    )
    obj.hide_viewport = True
    obj.hide_render = True
    return obj


def object_triangles(objects: list[bpy.types.Object]) -> int:
    total = 0
    for obj in objects:
        if obj.type != "MESH":
            continue
        total += sum(max(1, len(poly.vertices) - 2) for poly in obj.data.polygons)
    return total


def add_smart_uv0(objects: list[bpy.types.Object]) -> None:
    for obj in objects:
        if obj.type != "MESH" or obj.name.startswith("UCX_"):
            continue
        if bpy.context.object is not None and bpy.context.object.mode != "OBJECT":
            bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.select_all(action="DESELECT")
        set_active(obj)
        if not obj.data.uv_layers:
            obj.data.uv_layers.new(name="UV0")
        try:
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_all(action="SELECT")
            bpy.ops.uv.smart_project(angle_limit=1.1519, island_margin=0.02)
        finally:
            bpy.ops.object.mode_set(mode="OBJECT")
            obj.select_set(False)


def export_objects(objects: list[bpy.types.Object], path: Path) -> None:
    ensure_dir(path.parent)
    collection_states: list[tuple[bpy.types.Collection, bool, bool]] = []
    object_states: list[tuple[bpy.types.Object, bool, bool, bool]] = []
    seen_collections: set[str] = set()
    for obj in objects:
        object_states.append((obj, obj.hide_viewport, obj.hide_render, obj.hide_get()))
        obj.hide_viewport = False
        obj.hide_render = False
        obj.hide_set(False)
        for collection in obj.users_collection:
            if collection.name in seen_collections:
                continue
            seen_collections.add(collection.name)
            collection_states.append((collection, collection.hide_viewport, collection.hide_render))
            collection.hide_viewport = False
            collection.hide_render = False
    bpy.context.view_layer.update()

    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    try:
        bpy.ops.export_scene.fbx(
            filepath=str(path),
            use_selection=True,
            object_types={"MESH"},
            apply_unit_scale=True,
            apply_scale_options="FBX_SCALE_UNITS",
            add_leaf_bones=False,
            bake_space_transform=False,
            mesh_smooth_type="FACE",
        )
    finally:
        for obj, hide_viewport, hide_render, hide_get in object_states:
            obj.hide_viewport = hide_viewport
            obj.hide_render = hide_render
            obj.hide_set(hide_get)
        for collection, hide_viewport, hide_render in collection_states:
            collection.hide_viewport = hide_viewport
            collection.hide_render = hide_render
        bpy.ops.object.select_all(action="DESELECT")
        bpy.context.view_layer.update()


def look_at(camera: bpy.types.Object, target: Vector) -> None:
    direction = target - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def configure_review_scene() -> tuple[bpy.types.Object, Vector]:
    world = bpy.context.scene.world or bpy.data.worlds.new("AeratheaDCCWorld")
    bpy.context.scene.world = world
    world.color = (0.68, 0.67, 0.64)

    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE"
        scene.eevee.use_gtao = True
        scene.eevee.gtao_distance = 2.4
        scene.eevee.gtao_factor = 0.24
        scene.eevee.shadow_cube_size = "2048"
        scene.eevee.shadow_cascade_size = "2048"
        scene.eevee.taa_render_samples = 48
    except (AttributeError, TypeError):
        pass
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0.82
    scene.view_settings.gamma = 1.0
    scene.render.film_transparent = False

    bpy.ops.object.light_add(type="AREA", location=(-260, -320, 430))
    key = bpy.context.object
    key.name = "AET_DCC_Key_Area"
    key.data.energy = 52000.0
    key.data.size = 430.0

    bpy.ops.object.light_add(type="POINT", location=(280, -240, 190))
    fill = bpy.context.object
    fill.name = "AET_DCC_Fill_Point"
    fill.data.energy = 28000.0
    fill.data.shadow_soft_size = 380.0

    bpy.ops.object.light_add(type="AREA", location=(250, 340, 270))
    rim = bpy.context.object
    rim.name = "AET_DCC_Back_Rim_Area"
    rim.data.energy = 19000.0
    rim.data.size = 360.0

    bpy.ops.object.light_add(type="SUN", location=(-220, -340, 520))
    sun = bpy.context.object
    sun.name = "AET_DCC_Broad_SunFill"
    sun.data.energy = 2.4
    look_at(sun, Vector((0.0, -2.0, 75.0)))

    bpy.ops.object.camera_add(location=(315, -430, 220))
    camera = bpy.context.object
    camera.name = "AET_DCC_ReviewCamera"
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 455.0
    camera.data.lens = 45
    camera.data.sensor_width = 32
    bpy.context.scene.camera = camera
    target = Vector((0.0, -2.0, 75.0))
    look_at(camera, target)
    return camera, target


def render_view(
    camera: bpy.types.Object,
    target: Vector,
    location: tuple[float, float, float],
    path: Path,
    resolution: tuple[int, int],
    ortho_scale: float | None = None,
) -> None:
    camera.location = location
    look_at(camera, target)
    if ortho_scale is not None:
        camera.data.ortho_scale = ortho_scale
    ensure_dir(path.parent)
    scene = bpy.context.scene
    scene.render.resolution_x = resolution[0]
    scene.render.resolution_y = resolution[1]
    if hasattr(scene, "eevee"):
        scene.eevee.taa_render_samples = 16
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def compose_review_board(image_paths: list[Path], output_path: Path, tile_width: int, tile_height: int) -> None:
    cols = 3
    rows = 2
    board_width = tile_width * cols
    board_height = tile_height * rows
    board = array("f", [0.055] * (board_width * board_height * 4))
    for pixel in range(3, len(board), 4):
        board[pixel] = 1.0

    for tile_index, path in enumerate(image_paths):
        image = bpy.data.images.load(str(path))
        pixels = array("f", [0.0] * (tile_width * tile_height * 4))
        image.pixels.foreach_get(pixels)
        col = tile_index % cols
        row = tile_index // cols
        x_offset = col * tile_width
        y_offset = (rows - 1 - row) * tile_height
        for y in range(tile_height):
            for x in range(tile_width):
                src_index = ((y * tile_width) + x) * 4
                dst_index = (((y + y_offset) * board_width) + (x + x_offset)) * 4
                board[dst_index : dst_index + 4] = pixels[src_index : src_index + 4]
        bpy.data.images.remove(image)

    ensure_dir(output_path.parent)
    board_image = bpy.data.images.new(output_path.stem, width=board_width, height=board_height, alpha=True, float_buffer=False)
    board_image.pixels.foreach_set(board)
    board_image.filepath_raw = str(output_path)
    board_image.file_format = "PNG"
    board_image.save()
    bpy.data.images.remove(board_image)


def add_metadata_to_objects(objects: list[bpy.types.Object]) -> None:
    add_asset_metadata(
        ASSET_NAME,
        f"DCC source candidate pending concept-geometry review against {SOURCE_TARGET}",
        UNREAL_PATH,
    )
    for obj in objects:
        obj["Aerathea.Asset"] = ASSET_NAME
        obj["Aerathea.UnrealPath"] = UNREAL_PATH
        obj["Aerathea.AssetType"] = "Static Mesh"
        obj["Aerathea.Faction"] = "Blood Axe Giants"
        obj["Aerathea.Status"] = "dcc_source_candidate_pending_concept_geometry_review"
        obj["Aerathea.SourceTarget"] = SOURCE_TARGET
        obj["Aerathea.SourceMethod"] = "hand_authored_dcc_candidate_against_clear_bloodaxe_a1_multiview_target"
        obj["Aerathea.Collision"] = "broad_ucx_hull_for_primary_slab_cluster_only"


def main() -> None:
    clear_scene()
    setup_scene()
    texture_paths = generate_textures()
    materials = make_materials(texture_paths)

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3", hidden=True)
    collision_collection = make_collection(f"{ASSET_NAME}_Collision", hidden=True)

    lod0_objects = build_asset_lod(lod0_collection, materials, 0)
    lod1_objects = build_asset_lod(lod1_collection, materials, 1)
    lod2_objects = build_asset_lod(lod2_collection, materials, 2)
    lod3_objects = build_asset_lod(lod3_collection, materials, 3)
    add_smart_uv0(lod0_objects)
    add_smart_uv0(lod1_objects)
    add_smart_uv0(lod2_objects)
    add_smart_uv0(lod3_objects)
    collision = add_collision_proxy(collision_collection, materials["stone"])
    add_metadata_to_objects(lod0_objects + lod1_objects + lod2_objects + lod3_objects + [collision])

    export_dir = EXPORT_ROOT / REL_PATH
    export_objects(lod0_objects, export_dir / f"{ASSET_NAME}.fbx")
    export_objects(lod0_objects, export_dir / f"{ASSET_NAME}_LOD0.fbx")
    export_objects(lod1_objects, export_dir / f"{ASSET_NAME}_LOD1.fbx")
    export_objects(lod2_objects, export_dir / f"{ASSET_NAME}_LOD2.fbx")
    export_objects(lod3_objects, export_dir / f"{ASSET_NAME}_LOD3.fbx")
    export_objects([collision], export_dir / f"{ASSET_NAME}_UCX.fbx")

    camera, target = configure_review_scene()
    render_paths = [
        REVIEW_ROOT / f"{ASSET_NAME}_FrontReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_RightReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_BackReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_LeftReview.png",
        REVIEW_ROOT / f"{ASSET_NAME}_HeroReview.png",
    ]
    view_locations = [
        (0, -545, 178),
        (545, -8, 205),
        (60, 545, 212),
        (-545, -8, 205),
        (340, -455, 238),
    ]
    for path, location in zip(render_paths, view_locations):
        render_view(camera, target, location, path, (960, 540))
    render_view(
        camera,
        Vector((-10.0, -24.0, 76.0)),
        (-125, -525, 188),
        REVIEW_ROOT / f"{ASSET_NAME}_TargetFrontMatchReview.png",
        (960, 540),
        430.0,
    )
    compose_review_board(render_paths, REVIEW_ROOT / f"{ASSET_NAME}_DCCProofTurntable.png", 960, 540)

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    ensure_dir(blend_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    print(
        "Built {}: LOD0 {} tris, LOD1 {} tris, LOD2 {} tris, LOD3 {} tris. Exports: {}".format(
            ASSET_NAME,
            object_triangles(lod0_objects),
            object_triangles(lod1_objects),
            object_triangles(lod2_objects),
            object_triangles(lod3_objects),
            export_dir,
        )
    )


if __name__ == "__main__":
    main()
