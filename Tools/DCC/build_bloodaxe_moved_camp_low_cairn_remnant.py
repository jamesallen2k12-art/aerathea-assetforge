#!/usr/bin/env python3
"""Build first-pass Blood Axe moved-camp low cairn remnant DCC assets.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py

This creates a deterministic first-pass DCC review source, proof render, and
LOD0 FBX export for SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01. It is a
review target, not final sculpted or painted production art.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


ASSET_NAME = "SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01"
REL_PATH = "Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01"
UNREAL_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01"

LOD0_HEIGHT_CM = 132.0
GIANT_FEMALE_BASELINE_CM = 442.0
GIANT_MALE_BASELINE_CM = 470.0
VERTEX_COLOR_ATTRIBUTE = "Color"


def flat_material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.get(name)
    if material is None:
        material = bpy.data.materials.new(name)
    material.diffuse_color = color
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = 0.88
        bsdf.inputs["Metallic"].default_value = 0.0
    return material


def review_material() -> bpy.types.Material:
    material = bpy.data.materials.get("M_GIA_BloodAxeMovedCampLowCairnRemnant_Blockout_A01")
    if material is None:
        material = bpy.data.materials.new("M_GIA_BloodAxeMovedCampLowCairnRemnant_Blockout_A01")
    material.diffuse_color = (0.38, 0.36, 0.32, 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        return material

    for link in list(material.node_tree.links):
        if link.to_node == bsdf and link.to_socket == bsdf.inputs["Base Color"]:
            material.node_tree.links.remove(link)
    vertex_color = nodes.new(type="ShaderNodeAttribute")
    vertex_color.attribute_name = VERTEX_COLOR_ATTRIBUTE
    material.node_tree.links.new(vertex_color.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = 0.88
    bsdf.inputs["Metallic"].default_value = 0.0
    return material


def set_active(obj: bpy.types.Object) -> None:
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def add_rough_stone(
    name: str,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    rotation: tuple[float, float, float],
    color: tuple[float, float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    subdivisions: int = 2,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=subdivisions, radius=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.color = color
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    bpy.ops.object.shade_flat()
    move_to_collection(obj, collection)
    return obj


def add_box(
    name: str,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    rotation: tuple[float, float, float],
    color: tuple[float, float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    obj.color = color
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    move_to_collection(obj, collection)
    return obj


def add_disc(
    name: str,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    color: tuple[float, float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    vertices: int = 28,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=1.0, depth=1.0, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.color = color
    obj.data.materials.append(material)
    set_active(obj)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.shade_flat()
    move_to_collection(obj, collection)
    return obj


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def apply_vertex_color(obj: bpy.types.Object) -> None:
    """Bake the object's review color into vertex color for one-material Unreal import."""
    mesh = obj.data
    color = tuple(obj.color)
    color_layer = None
    color_attributes = getattr(mesh, "color_attributes", None)
    if color_attributes is not None:
        color_layer = color_attributes.get(VERTEX_COLOR_ATTRIBUTE)
        if color_layer is None:
            color_layer = color_attributes.new(name=VERTEX_COLOR_ATTRIBUTE, type="BYTE_COLOR", domain="CORNER")
        try:
            color_attributes.active_color = color_layer
        except Exception:
            pass
    else:
        vertex_colors = getattr(mesh, "vertex_colors", None)
        if vertex_colors is not None:
            color_layer = vertex_colors.get(VERTEX_COLOR_ATTRIBUTE) or vertex_colors.new(name=VERTEX_COLOR_ATTRIBUTE)
            try:
                vertex_colors.active = color_layer
            except Exception:
                pass

    if color_layer is None:
        return
    for entry in color_layer.data:
        entry.color = color


def make_collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    collection.hide_render = hidden
    collection.hide_viewport = hidden
    return collection


def build_lod0(collection: bpy.types.Collection, material: bpy.types.Material) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    stone_dark = (0.09, 0.105, 0.11, 1.0)
    stone_mid = (0.18, 0.18, 0.17, 1.0)
    stone_worn = (0.27, 0.25, 0.21, 1.0)
    ash = (0.11, 0.11, 0.105, 1.0)
    mud = (0.075, 0.055, 0.045, 1.0)
    red = (0.74, 0.045, 0.025, 1.0)
    rawhide = (0.22, 0.13, 0.075, 1.0)

    objects.append(add_disc("LOD0_AshMudBase_BroadGrounding", (0, 0, 4), (165, 118, 7), ash, material, collection))
    objects.append(add_disc("LOD0_MudScuff_OffsetPatch", (-38, -18, 8), (112, 76, 4), mud, material, collection, 18))

    objects.append(
        add_rough_stone(
            "LOD0_Stone_DominantBase_HalfBuried",
            (-34, -6, 45),
            (86, 55, 38),
            (math.radians(8), math.radians(-6), math.radians(14)),
            stone_mid,
            material,
            collection,
        )
    )
    objects.append(
        add_rough_stone(
            "LOD0_Stone_RearSupport_Shifted",
            (42, 28, 52),
            (62, 44, 42),
            (math.radians(-6), math.radians(12), math.radians(-22)),
            stone_dark,
            material,
            collection,
        )
    )
    objects.append(
        add_rough_stone(
            "LOD0_Stone_LeftLowBuried",
            (-95, 34, 34),
            (48, 36, 27),
            (math.radians(5), math.radians(18), math.radians(37)),
            stone_dark,
            material,
            collection,
            1,
        )
    )
    objects.append(
        add_rough_stone(
            "LOD0_Stone_RightBrokenContact",
            (92, -24, 38),
            (52, 32, 30),
            (math.radians(12), math.radians(-8), math.radians(-18)),
            stone_mid,
            material,
            collection,
            1,
        )
    )
    objects.append(
        add_rough_stone(
            "LOD0_Stone_UpperCollapsedCrown",
            (4, 2, 104),
            (48, 34, 28),
            (math.radians(16), math.radians(4), math.radians(-10)),
            stone_worn,
            material,
            collection,
            1,
        )
    )

    objects.append(
        add_box(
            "LOD0_BloodAxeResidue_FadedRedPaintBeat",
            (-18, -76, 62),
            (80, 5, 18),
            (math.radians(4), math.radians(0), math.radians(-10)),
            red,
            material,
            collection,
        )
    )
    objects.append(
        add_box(
            "LOD0_BloodAxeResidue_DriedRedStoneSlash",
            (-42, -58, 78),
            (14, 5, 56),
            (math.radians(2), math.radians(0), math.radians(24)),
            red,
            material,
            collection,
        )
    )
    objects.append(
        add_box(
            "LOD0_RawhideResidue_LowFixedTie",
            (35, -54, 64),
            (62, 4, 7),
            (math.radians(2), math.radians(0), math.radians(18)),
            rawhide,
            material,
            collection,
        )
    )
    objects.append(
        add_box(
            "LOD0_RawhideResidue_CrownWrap",
            (3, -40, 104),
            (56, 4, 7),
            (math.radians(3), math.radians(0), math.radians(-8)),
            rawhide,
            material,
            collection,
        )
    )
    return objects


def build_simplified_lod(
    collection: bpy.types.Collection,
    material: bpy.types.Material,
    prefix: str,
    stone_count: int,
    height: float,
    base_scale: tuple[float, float, float],
) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    objects.append(add_disc(f"{prefix}_AshMudBase_Simplified", (0, 0, 3), base_scale, (0.11, 0.11, 0.105, 1.0), material, collection, 16))
    objects.append(add_rough_stone(f"{prefix}_Stone_PrimaryMass", (-24, -4, height * 0.34), (72, 46, height * 0.22), (0, 0, math.radians(10)), (0.18, 0.18, 0.17, 1.0), material, collection, 1))
    if stone_count >= 2:
        objects.append(add_rough_stone(f"{prefix}_Stone_SecondaryMass", (42, 24, height * 0.38), (48, 34, height * 0.19), (0, 0, math.radians(-18)), (0.09, 0.105, 0.11, 1.0), material, collection, 1))
    if stone_count >= 3:
        objects.append(add_rough_stone(f"{prefix}_Stone_CrownMass", (4, 0, height * 0.78), (38, 27, height * 0.16), (0, 0, math.radians(-8)), (0.27, 0.25, 0.21, 1.0), material, collection, 1))
    objects.append(add_box(f"{prefix}_BloodAxeResidue_FadedLowBeat", (-10, -60, height * 0.44), (58, 4, 12), (0, 0, math.radians(-8)), (0.74, 0.045, 0.025, 1.0), material, collection))
    return objects


def add_scale_marker(name: str, height_cm: float, x: float, material: bpy.types.Material) -> None:
    marker_collection = bpy.data.collections.get("Review_Markers")
    if marker_collection is None:
        marker_collection = make_collection("Review_Markers")
    color = (0.78, 0.72, 0.58, 1.0)
    add_box(f"Review_{name}_Post", (x, 160, height_cm * 0.5), (8, 8, height_cm), (0, 0, 0), color, material, marker_collection)
    add_box(f"Review_{name}_Cap", (x, 160, height_cm), (42, 8, 6), (0, 0, 0), color, material, marker_collection)


def add_label(text: str, location: tuple[float, float, float], size: float = 13.0) -> None:
    bpy.ops.object.text_add(location=location, rotation=(math.radians(72), 0, 0))
    obj = bpy.context.object
    obj.name = "Review_Label_" + text.replace(" ", "_").replace("/", "_")
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    material = flat_material("M_AET_ReviewLabel_Tan_A01", (0.86, 0.82, 0.70, 1.0))
    obj.data.materials.clear()
    obj.data.materials.append(material)
    obj.color = (0.86, 0.82, 0.70, 1.0)


def purge_unused_materials() -> None:
    for material in list(bpy.data.materials):
        if material.users == 0:
            bpy.data.materials.remove(material)


def render_review(material: bpy.types.Material) -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 1800
    scene.render.resolution_y = 1200
    try:
        scene.eevee.taa_render_samples = 64
    except Exception:
        pass
    if scene.world is not None:
        scene.world.color = (0.58, 0.57, 0.52)

    marker_material = flat_material("M_AET_ReviewMarker_Tan_A01", (0.78, 0.72, 0.58, 1.0))
    add_scale_marker("LowCairn_132cm", LOD0_HEIGHT_CM, 250, marker_material)
    add_scale_marker("GiantFemale_442cm", GIANT_FEMALE_BASELINE_CM, 320, marker_material)
    add_scale_marker("GiantMale_470cm", GIANT_MALE_BASELINE_CM, 380, marker_material)
    add_label("132 cm remnant", (250, 145, 150), 11)
    add_label("442 cm female Giant", (320, 145, 462), 11)
    add_label("470 cm male Giant", (380, 145, 490), 11)
    add_label("ground-center pivot", (0, 148, 22), 12)

    bpy.ops.object.light_add(type="SUN", location=(0, -520, 820), rotation=(math.radians(48), 0, math.radians(24)))
    sun = bpy.context.object
    sun.name = "AET_LowCairnRemnantReview_Sun"
    sun.data.energy = 1.0

    bpy.ops.object.light_add(type="AREA", location=(-240, -420, 360))
    key = bpy.context.object
    key.name = "AET_LowCairnRemnantReview_KeyLight"
    key.data.energy = 560
    key.data.size = 460

    bpy.ops.object.light_add(type="AREA", location=(360, 300, 260))
    fill = bpy.context.object
    fill.name = "AET_LowCairnRemnantReview_FillLight"
    fill.data.energy = 160
    fill.data.size = 520

    bpy.ops.object.camera_add(location=(650, -620, 330))
    camera = bpy.context.object
    target = Vector((120.0, 0.0, 230.0))
    direction = target - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 900
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    scene.camera = camera

    scene.render.filepath = str(REVIEW_ROOT / f"{ASSET_NAME}_DCCReview.png")
    bpy.ops.render.render(write_still=True)


def build() -> None:
    clear_scene()
    setup_scene()
    material = review_material()

    lod0_collection = make_collection(f"{ASSET_NAME}_LOD0_Export")
    lod1_collection = make_collection(f"{ASSET_NAME}_LOD1_Source", hidden=True)
    lod2_collection = make_collection(f"{ASSET_NAME}_LOD2_Source", hidden=True)
    lod3_collection = make_collection(f"{ASSET_NAME}_LOD3_Source", hidden=True)

    export_objects = build_lod0(lod0_collection, material)
    lod_source_objects = []
    lod_source_objects.extend(build_simplified_lod(lod1_collection, material, "LOD1", 4, 120.0, (150, 104, 6)))
    lod_source_objects.extend(build_simplified_lod(lod2_collection, material, "LOD2", 3, 110.0, (128, 88, 5)))
    lod_source_objects.extend(build_simplified_lod(lod3_collection, material, "LOD3", 2, 96.0, (108, 72, 4)))
    for obj in export_objects + lod_source_objects:
        apply_vertex_color(obj)

    add_asset_metadata(
        ASSET_NAME,
        "First-pass DCC review source for a static Blood Axe moved-camp low cairn remnant. LOD1-LOD3 source meshes are saved in hidden collections; FBX export contains LOD0 only with vertex colors for one-material Unreal review. Collision remains disabled/future-gated.",
        UNREAL_PATH,
    )

    blend_path = BLENDER_ROOT / REL_PATH / f"{ASSET_NAME}.blend"
    export_path = EXPORT_ROOT / REL_PATH / f"{ASSET_NAME}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    render_review(material)
    purge_unused_materials()
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    bpy.ops.object.select_all(action="DESELECT")
    for obj in export_objects:
        obj.select_set(True)
    if export_objects:
        bpy.context.view_layer.objects.active = export_objects[0]

    bpy.ops.export_scene.fbx(
        filepath=str(export_path),
        use_selection=True,
        object_types={"MESH"},
        mesh_smooth_type="FACE",
        global_scale=1.0,
        apply_unit_scale=False,
        apply_scale_options="FBX_SCALE_NONE",
        axis_forward="X",
        axis_up="Z",
        bake_space_transform=False,
        add_leaf_bones=False,
    )
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")
    print(f"Rendered {REVIEW_ROOT.relative_to(ROOT)}/{ASSET_NAME}_DCCReview.png")


if __name__ == "__main__":
    build()
