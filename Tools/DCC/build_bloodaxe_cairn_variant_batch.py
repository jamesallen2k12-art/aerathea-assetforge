#!/usr/bin/env python3
"""Build first-pass Blood Axe cairn-stone variant DCC assets.

Run with:
    blender --background --python Tools/DCC/build_bloodaxe_cairn_variant_batch.py

This creates deterministic first-pass DCC review sources, LOD source meshes,
FBX exports, and proof renders for the package-ready Blood Axe cairn variants.
They are DCC source candidates for review, not final sculpted or painted art.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "BloodAxeCairnVariants_A01"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_next_slice_assets import add_asset_metadata, clear_scene, setup_scene  # noqa: E402


VERTEX_COLOR_ATTRIBUTE = "Color"
GIANT_FEMALE_BASELINE_CM = 442.0
GIANT_MALE_BASELINE_CM = 470.0

STONE_DARK = (0.09, 0.10, 0.10, 1.0)
STONE_MID = (0.18, 0.18, 0.17, 1.0)
STONE_WORN = (0.29, 0.27, 0.23, 1.0)
STONE_CAVE = (0.12, 0.13, 0.135, 1.0)
ASH = (0.105, 0.105, 0.10, 1.0)
MUD = (0.08, 0.055, 0.04, 1.0)
RED = (0.62, 0.055, 0.035, 1.0)
RAWHIDE = (0.23, 0.14, 0.075, 1.0)
IRON = (0.06, 0.065, 0.065, 1.0)
BONE = (0.50, 0.42, 0.27, 1.0)


@dataclass(frozen=True)
class Stone:
    name: str
    loc: tuple[float, float, float]
    scale: tuple[float, float, float]
    rot: tuple[float, float, float]
    color: tuple[float, float, float, float] = STONE_MID
    subdivisions: int = 1


@dataclass(frozen=True)
class Ribbon:
    name: str
    loc: tuple[float, float, float]
    scale: tuple[float, float, float]
    rot: tuple[float, float, float]
    color: tuple[float, float, float, float] = RED


@dataclass(frozen=True)
class Accent:
    name: str
    loc: tuple[float, float, float]
    scale: tuple[float, float, float]
    rot: tuple[float, float, float]
    color: tuple[float, float, float, float]


@dataclass(frozen=True)
class CairnStack:
    prefix: str
    origin: tuple[float, float, float]
    yaw: float
    base_radius: tuple[float, float, float]
    stones: tuple[Stone, ...]
    ribbons: tuple[Ribbon, ...] = ()
    accents: tuple[Accent, ...] = ()
    base_color: tuple[float, float, float, float] = ASH
    mud_patch: bool = True


@dataclass(frozen=True)
class VariantSpec:
    asset_name: str
    rel_path: str
    unreal_path: str
    status_doc: str
    summary: str
    stacks: tuple[CairnStack, ...]
    camera: tuple[float, float, float] = (640.0, -660.0, 360.0)
    target: tuple[float, float, float] = (30.0, 0.0, 155.0)
    ortho_scale: float = 760.0


def rad(value: float) -> float:
    return math.radians(value)


def rotate_xy(x: float, y: float, yaw: float) -> tuple[float, float]:
    cos_yaw = math.cos(yaw)
    sin_yaw = math.sin(yaw)
    return (x * cos_yaw - y * sin_yaw, x * sin_yaw + y * cos_yaw)


def world_loc(origin: tuple[float, float, float], loc: tuple[float, float, float], yaw: float) -> tuple[float, float, float]:
    x, y = rotate_xy(loc[0], loc[1], yaw)
    return (origin[0] + x, origin[1] + y, origin[2] + loc[2])


def world_rot(rot: tuple[float, float, float], yaw: float) -> tuple[float, float, float]:
    return (rot[0], rot[1], rot[2] + yaw)


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
    material = bpy.data.materials.get("M_GIA_BloodAxeCairnVariants_VertexColor_A01")
    if material is None:
        material = bpy.data.materials.new("M_GIA_BloodAxeCairnVariants_VertexColor_A01")
    material.diffuse_color = (0.24, 0.23, 0.20, 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf is None:
        return material

    for link in list(material.node_tree.links):
        if link.to_node == bsdf and link.to_socket == bsdf.inputs["Base Color"]:
            material.node_tree.links.remove(link)
    attribute = nodes.new(type="ShaderNodeAttribute")
    attribute.attribute_name = VERTEX_COLOR_ATTRIBUTE
    material.node_tree.links.new(attribute.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = 0.9
    bsdf.inputs["Metallic"].default_value = 0.0
    return material


def set_active(obj: bpy.types.Object) -> None:
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)


def make_collection(name: str, hidden: bool = False) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    collection.hide_render = hidden
    collection.hide_viewport = hidden
    return collection


def apply_vertex_color(obj: bpy.types.Object) -> None:
    mesh = obj.data
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
        entry.color = tuple(obj.color)


def add_rough_stone(
    name: str,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    rotation: tuple[float, float, float],
    color: tuple[float, float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    subdivisions: int = 1,
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
    apply_vertex_color(obj)
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
    apply_vertex_color(obj)
    return obj


def add_disc(
    name: str,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    color: tuple[float, float, float, float],
    material: bpy.types.Material,
    collection: bpy.types.Collection,
    vertices: int = 24,
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
    apply_vertex_color(obj)
    return obj


def build_stack(stack: CairnStack, material: bpy.types.Material, collection: bpy.types.Collection, lod_level: int = 0) -> list[bpy.types.Object]:
    objects: list[bpy.types.Object] = []
    base_scale_factor = max(0.55, 1.0 - 0.14 * lod_level)
    stone_scale_factor = max(0.62, 1.0 - 0.11 * lod_level)
    ribbon_scale_factor = max(0.55, 1.0 - 0.16 * lod_level)

    base_location = (stack.origin[0], stack.origin[1], stack.origin[2] + 3.0)
    objects.append(
        add_disc(
            f"LOD{lod_level}_{stack.prefix}_AshMudBase",
            base_location,
            (
                stack.base_radius[0] * base_scale_factor,
                stack.base_radius[1] * base_scale_factor,
                stack.base_radius[2],
            ),
            stack.base_color,
            material,
            collection,
            max(12, 28 - lod_level * 6),
        )
    )
    if stack.mud_patch and lod_level <= 1:
        mud_x, mud_y = rotate_xy(-28.0, -16.0, stack.yaw)
        objects.append(
            add_disc(
                f"LOD{lod_level}_{stack.prefix}_MudScuff",
                (stack.origin[0] + mud_x, stack.origin[1] + mud_y, stack.origin[2] + 6.5),
                (stack.base_radius[0] * 0.54, stack.base_radius[1] * 0.42, 2.6),
                MUD,
                material,
                collection,
                14,
            )
        )

    max_stones = max(2, len(stack.stones) - lod_level)
    for stone in stack.stones[:max_stones]:
        objects.append(
            add_rough_stone(
                f"LOD{lod_level}_{stack.prefix}_{stone.name}",
                world_loc(stack.origin, stone.loc, stack.yaw),
                (
                    stone.scale[0] * stone_scale_factor,
                    stone.scale[1] * stone_scale_factor,
                    stone.scale[2] * stone_scale_factor,
                ),
                world_rot(stone.rot, stack.yaw),
                stone.color,
                material,
                collection,
                max(1, stone.subdivisions - lod_level),
            )
        )

    max_ribbons = 0 if lod_level >= 3 else max(1, len(stack.ribbons) - lod_level)
    for ribbon in stack.ribbons[:max_ribbons]:
        objects.append(
            add_box(
                f"LOD{lod_level}_{stack.prefix}_{ribbon.name}",
                world_loc(stack.origin, ribbon.loc, stack.yaw),
                (
                    ribbon.scale[0] * ribbon_scale_factor,
                    ribbon.scale[1],
                    ribbon.scale[2] * ribbon_scale_factor,
                ),
                world_rot(ribbon.rot, stack.yaw),
                ribbon.color,
                material,
                collection,
            )
        )

    if lod_level == 0:
        for accent in stack.accents:
            objects.append(
                add_box(
                    f"LOD0_{stack.prefix}_{accent.name}",
                    world_loc(stack.origin, accent.loc, stack.yaw),
                    accent.scale,
                    world_rot(accent.rot, stack.yaw),
                    accent.color,
                    material,
                    collection,
                )
            )
    return objects


def common_low_stack(prefix: str, origin: tuple[float, float, float], yaw: float = 0.0) -> CairnStack:
    return CairnStack(
        prefix=prefix,
        origin=origin,
        yaw=yaw,
        base_radius=(155, 110, 7),
        stones=(
            Stone("Stone_DominantHalfBuried", (-34, -4, 40), (82, 54, 34), (rad(8), rad(-5), rad(12)), STONE_MID, 2),
            Stone("Stone_RearBrace", (38, 24, 48), (58, 40, 38), (rad(-4), rad(10), rad(-22)), STONE_DARK, 1),
            Stone("Stone_LeftLowFoot", (-88, 28, 30), (43, 32, 24), (rad(6), rad(16), rad(34)), STONE_CAVE, 1),
            Stone("Stone_RightBrokenFoot", (88, -22, 34), (48, 30, 28), (rad(10), rad(-8), rad(-18)), STONE_MID, 1),
            Stone("Stone_BluntCap", (4, -2, 88), (46, 32, 24), (rad(14), rad(4), rad(-10)), STONE_WORN, 1),
        ),
        ribbons=(
            Ribbon("BloodAxeResidue_LowRedWrap", (-18, -66, 58), (74, 5, 16), (rad(4), 0, rad(-8))),
            Ribbon("RawhideResidue_FixedTie", (34, -50, 64), (56, 4, 7), (rad(2), 0, rad(17)), RAWHIDE),
        ),
    )


def leaning_stack(prefix: str, origin: tuple[float, float, float], yaw: float = 0.0) -> CairnStack:
    return CairnStack(
        prefix=prefix,
        origin=origin,
        yaw=yaw,
        base_radius=(145, 96, 6),
        stones=(
            Stone("Stone_LeaningPrimary", (-18, 0, 58), (68, 44, 70), (rad(2), rad(-18), rad(8)), STONE_MID, 2),
            Stone("Stone_SunkFootLeft", (-72, 24, 30), (48, 34, 28), (rad(8), rad(10), rad(26)), STONE_DARK, 1),
            Stone("Stone_SunkFootRight", (58, -22, 34), (52, 36, 30), (rad(5), rad(-8), rad(-18)), STONE_CAVE, 1),
            Stone("Stone_OffsetCap", (12, -8, 118), (42, 30, 28), (rad(18), rad(4), rad(-12)), STONE_WORN, 1),
        ),
        ribbons=(
            Ribbon("BloodAxeCloth_HangingRouteBeat", (4, -56, 92), (88, 5, 24), (rad(6), 0, rad(-2))),
            Ribbon("RawhideWrap_UnderCap", (2, -48, 116), (58, 4, 7), (rad(4), 0, rad(7)), RAWHIDE),
        ),
    )


def collapsed_stack(prefix: str, origin: tuple[float, float, float], yaw: float = 0.0) -> CairnStack:
    return CairnStack(
        prefix=prefix,
        origin=origin,
        yaw=yaw,
        base_radius=(178, 128, 7),
        stones=(
            Stone("Stone_FallenBaseSlab", (-50, -8, 30), (92, 52, 24), (rad(9), rad(6), rad(18)), STONE_MID, 2),
            Stone("Stone_RolledSideMass", (50, 28, 34), (68, 42, 30), (rad(15), rad(-2), rad(-26)), STONE_DARK, 1),
            Stone("Stone_BrokenCapOnGround", (0, -58, 32), (60, 32, 20), (rad(5), rad(24), rad(2)), STONE_WORN, 1),
            Stone("Stone_RemainingStub", (-12, 20, 74), (44, 34, 48), (rad(-8), rad(5), rad(10)), STONE_CAVE, 1),
        ),
        ribbons=(
            Ribbon("BloodAxeCloth_CollapsedStrip", (18, -76, 42), (98, 5, 16), (rad(2), 0, rad(11))),
        ),
    )


def cave_stack(prefix: str, origin: tuple[float, float, float], yaw: float = 0.0) -> CairnStack:
    return CairnStack(
        prefix=prefix,
        origin=origin,
        yaw=yaw,
        base_radius=(165, 118, 8),
        stones=(
            Stone("Stone_CaveGritBase", (-36, -2, 38), (86, 48, 34), (rad(7), rad(-6), rad(13)), STONE_CAVE, 2),
            Stone("Stone_ThresholdBack", (42, 18, 52), (64, 42, 42), (rad(-4), rad(9), rad(-18)), STONE_DARK, 1),
            Stone("Stone_LowSideChock", (-96, 22, 30), (42, 30, 24), (rad(8), rad(14), rad(31)), STONE_MID, 1),
            Stone("Stone_TopMemoryMarker", (2, -4, 112), (44, 30, 34), (rad(13), rad(2), rad(-8)), STONE_WORN, 1),
        ),
        ribbons=(
            Ribbon("BloodAxeRed_CaveMouthWrap", (-4, -62, 76), (92, 5, 15), (rad(5), 0, rad(-5))),
            Ribbon("Rawhide_LowOldTie", (38, -48, 56), (62, 4, 7), (rad(3), 0, rad(13)), RAWHIDE),
        ),
        base_color=(0.08, 0.08, 0.078, 1.0),
    )


def scrap_cap_stack(prefix: str, origin: tuple[float, float, float], yaw: float = 0.0) -> CairnStack:
    base = common_low_stack(prefix, origin, yaw)
    return CairnStack(
        prefix=base.prefix,
        origin=base.origin,
        yaw=base.yaw,
        base_radius=base.base_radius,
        stones=base.stones,
        ribbons=base.ribbons,
        accents=(
            Accent("BlackenedIron_ScrapCap", (7, -10, 118), (56, 20, 8), (rad(12), rad(-4), rad(8)), IRON),
            Accent("DullBone_TuckedWarningToken", (-64, -54, 42), (42, 8, 8), (rad(5), 0, rad(-24)), BONE),
        ),
        base_color=base.base_color,
        mud_patch=base.mud_patch,
    )


def approach_marker_stack(prefix: str, origin: tuple[float, float, float], yaw: float = 0.0) -> CairnStack:
    return CairnStack(
        prefix=prefix,
        origin=origin,
        yaw=yaw,
        base_radius=(182, 106, 6),
        stones=(
            Stone("Stone_BroadShoulder", (-38, -2, 42), (96, 54, 38), (rad(5), rad(-8), rad(10)), STONE_MID, 2),
            Stone("Stone_SunkOuterFoot", (-104, 22, 28), (48, 30, 22), (rad(6), rad(12), rad(28)), STONE_CAVE, 1),
            Stone("Stone_RouteEdgeBrace", (72, -18, 36), (62, 38, 30), (rad(8), rad(-5), rad(-18)), STONE_DARK, 1),
            Stone("Stone_LowOffsetCap", (8, 0, 88), (44, 30, 22), (rad(15), rad(3), rad(-10)), STONE_WORN, 1),
        ),
        ribbons=(
            Ribbon("BloodAxeCloth_SideWarningBeat", (-54, -62, 62), (78, 5, 18), (rad(5), 0, rad(-18))),
            Ribbon("RawhideWrap_ApproachEdgeTie", (28, -50, 68), (54, 4, 7), (rad(4), 0, rad(22)), RAWHIDE),
        ),
    )


def ritual_guidepost_stack(prefix: str, origin: tuple[float, float, float], yaw: float = 0.0) -> CairnStack:
    return CairnStack(
        prefix=prefix,
        origin=origin,
        yaw=yaw,
        base_radius=(126, 90, 6),
        stones=(
            Stone("Stone_TallLowerShard", (-6, 0, 66), (58, 40, 82), (rad(0), rad(-12), rad(5)), STONE_MID, 2),
            Stone("Stone_RearRitualBrace", (46, 20, 42), (48, 32, 34), (rad(-5), rad(8), rad(-24)), STONE_DARK, 1),
            Stone("Stone_FrontKneestone", (-52, -18, 32), (44, 28, 24), (rad(9), rad(9), rad(20)), STONE_CAVE, 1),
            Stone("Stone_CeremonialCrown", (4, -6, 142), (38, 28, 28), (rad(17), rad(2), rad(-7)), STONE_WORN, 1),
        ),
        ribbons=(
            Ribbon("BloodAxeCloth_HighRitualBand", (-2, -52, 112), (82, 5, 20), (rad(6), 0, rad(-4))),
            Ribbon("RawhideWrap_CrownTie", (8, -46, 138), (48, 4, 7), (rad(4), 0, rad(9)), RAWHIDE),
        ),
        accents=(
            Accent("DullBone_LowRitualToken", (-48, -48, 34), (32, 7, 7), (rad(5), 0, rad(-20)), BONE),
        ),
    )


def path_marker_stack(prefix: str, origin: tuple[float, float, float], yaw: float = 0.0) -> CairnStack:
    return CairnStack(
        prefix=prefix,
        origin=origin,
        yaw=yaw,
        base_radius=(132, 92, 5),
        stones=(
            Stone("Stone_SimpleLean", (-16, 2, 48), (58, 38, 58), (rad(4), rad(-24), rad(9)), STONE_MID, 2),
            Stone("Stone_TrailFootLeft", (-62, 22, 26), (38, 28, 20), (rad(6), rad(10), rad(28)), STONE_DARK, 1),
            Stone("Stone_TrailFootRight", (48, -20, 30), (42, 28, 23), (rad(5), rad(-7), rad(-22)), STONE_CAVE, 1),
            Stone("Stone_SmallDirectionCap", (0, -4, 98), (32, 24, 20), (rad(16), rad(3), rad(-12)), STONE_WORN, 1),
        ),
        ribbons=(
            Ribbon("BloodAxeCloth_SmallTrailBeat", (-6, -50, 76), (62, 5, 16), (rad(4), 0, rad(-6))),
        ),
    )


def collapsed_cave_remnant_stack(prefix: str, origin: tuple[float, float, float], yaw: float = 0.0) -> CairnStack:
    return CairnStack(
        prefix=prefix,
        origin=origin,
        yaw=yaw,
        base_radius=(186, 132, 7),
        stones=(
            Stone("Stone_CaveBuriedSlab", (-62, -8, 28), (92, 50, 22), (rad(8), rad(8), rad(16)), STONE_CAVE, 2),
            Stone("Stone_DarkSideMass", (44, 26, 30), (68, 40, 26), (rad(13), rad(-3), rad(-27)), STONE_DARK, 1),
            Stone("Stone_AshChokedCap", (-2, -56, 28), (56, 30, 18), (rad(4), rad(20), rad(2)), STONE_WORN, 1),
            Stone("Stone_LowMemoryStub", (-16, 18, 58), (38, 28, 30), (rad(-8), rad(4), rad(10)), STONE_CAVE, 1),
        ),
        ribbons=(
            Ribbon("BloodAxeCloth_OldBuriedStrip", (12, -76, 36), (82, 5, 12), (rad(2), 0, rad(13)), (0.42, 0.035, 0.028, 1.0)),
            Ribbon("Rawhide_CaveResidueTie", (-36, -58, 34), (48, 4, 6), (rad(3), 0, rad(-14)), RAWHIDE),
        ),
        base_color=(0.07, 0.072, 0.07, 1.0),
    )


VARIANTS: tuple[VariantSpec, ...] = (
    VariantSpec(
        asset_name="SM_GIA_BloodAxeApproachCairnMarker_A01",
        rel_path="Props/Giants/BloodAxe/StrongholdApproach/CairnMarkers/SM_GIA_BloodAxeApproachCairnMarker_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/StrongholdApproach/CairnMarkers/SM_GIA_BloodAxeApproachCairnMarker_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxeApproachCairnMarker_A01/DCC_BUILD_STATUS.md",
        summary="First-pass route-edge cairn marker with squat wedge mass, oxide red cloth, ash base, and no gameplay marker behavior.",
        stacks=(approach_marker_stack("ApproachMarker", (0, 0, 0), rad(-6)),),
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxeRitualCairnGuidepost_A01",
        rel_path="Props/Giants/BloodAxe/RitualStones/Guideposts/SM_GIA_BloodAxeRitualCairnGuidepost_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/RitualStones/Guideposts/SM_GIA_BloodAxeRitualCairnGuidepost_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxeRitualCairnGuidepost_A01/DCC_BUILD_STATUS.md",
        summary="First-pass single ritual cairn guidepost with stacked Giant-scale stones, one static red cloth beat, and ash/mud grounding.",
        stacks=(ritual_guidepost_stack("RitualGuidepost", (0, 0, 0), rad(3)),),
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxeLowThresholdCairn_A01",
        rel_path="Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeLowThresholdCairn_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeLowThresholdCairn_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxeLowThresholdCairn_A01/DCC_BUILD_STATUS.md",
        summary="First-pass squat low-threshold cairn for cave-edge Blood Axe dressing; broad footprint, low crown, and restrained cloth.",
        stacks=(common_low_stack("LowThreshold", (0, 0, 0), rad(0)),),
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxeCollapsedThresholdCairn_A01",
        rel_path="Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedThresholdCairn_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedThresholdCairn_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxeCollapsedThresholdCairn_A01/DCC_BUILD_STATUS.md",
        summary="First-pass collapsed threshold cairn with fallen stone massing, one remaining stub, and old red cloth residue.",
        stacks=(collapsed_stack("CollapsedThreshold", (0, 0, 0), rad(-8)),),
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxeCaveRemnantCairn_A01",
        rel_path="Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveRemnantCairn_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveRemnantCairn_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxeCaveRemnantCairn_A01/DCC_BUILD_STATUS.md",
        summary="First-pass cave remnant cairn with darker cave grit, compact vertical memory read, ash base, and old rawhide.",
        stacks=(cave_stack("CaveRemnant", (0, 0, 0), rad(6)),),
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01",
        rel_path="Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01/DCC_BUILD_STATUS.md",
        summary="First-pass collapsed cave remnant cairn with low shifted stones and darker cave-mouth ash/mud grounding.",
        stacks=(collapsed_cave_remnant_stack("CollapsedCaveRemnant", (0, 0, 0), rad(12)),),
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxeCaveThresholdCairnPair_A01",
        rel_path="Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveThresholdCairnPair_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveThresholdCairnPair_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxeCaveThresholdCairnPair_A01/DCC_BUILD_STATUS.md",
        summary="First-pass cave-threshold pair with two low non-symmetrical cairns for visual rhythm only.",
        stacks=(common_low_stack("LeftThresholdCairn", (-155, 0, 0), rad(-12)), common_low_stack("RightThresholdCairn", (155, 32, 0), rad(18))),
        camera=(760, -760, 390),
        target=(0, 10, 150),
        ortho_scale=980,
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxeMovedCampCairnPair_A01",
        rel_path="Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampCairnPair_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampCairnPair_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxeMovedCampCairnPair_A01/DCC_BUILD_STATUS.md",
        summary="First-pass moved-camp cairn pair with old ash breaks, uneven footprints, and non-interactive memory read.",
        stacks=(collapsed_stack("MovedCampCollapsed", (-135, -18, 0), rad(-18)), common_low_stack("MovedCampLow", (120, 36, 0), rad(21))),
        camera=(760, -760, 370),
        target=(0, 0, 140),
        ortho_scale=940,
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxePairedCairnClosePair_A01",
        rel_path="Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnClosePair_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnClosePair_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxePairedCairnClosePair_A01/DCC_BUILD_STATUS.md",
        summary="First-pass close paired cairns for guidepost rhythm; visual memory marker only, not a route gate.",
        stacks=(leaning_stack("ClosePairTall", (-92, 0, 0), rad(-7)), common_low_stack("ClosePairLow", (88, 18, 0), rad(14))),
        camera=(720, -740, 365),
        target=(0, 5, 155),
        ortho_scale=860,
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxePairedCairnStaggeredPair_A01",
        rel_path="Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnStaggeredPair_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnStaggeredPair_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxePairedCairnStaggeredPair_A01/DCC_BUILD_STATUS.md",
        summary="First-pass staggered paired cairns with offset height and spacing for repeated route-edge dressing only.",
        stacks=(leaning_stack("StaggeredForward", (-140, -46, 0), rad(-18)), collapsed_stack("StaggeredRear", (132, 64, 0), rad(24))),
        camera=(780, -790, 380),
        target=(0, 0, 150),
        ortho_scale=980,
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxeCairnPathMarker_A01",
        rel_path="Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnPathMarker_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnPathMarker_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxeCairnPathMarker_A01/DCC_BUILD_STATUS.md",
        summary="First-pass cairn path marker with leaning mass, fixed cloth beat, and ash base; no waypoint or objective behavior.",
        stacks=(path_marker_stack("PathMarker", (0, 0, 0), rad(-14)),),
    ),
    VariantSpec(
        asset_name="SM_GIA_BloodAxeCairnScrapCap_A01",
        rel_path="Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnScrapCap_A01",
        unreal_path="/Game/Aerathea/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnScrapCap_A01",
        status_doc="docs/assets/props/SM_GIA_BloodAxeCairnScrapCap_A01/DCC_BUILD_STATUS.md",
        summary="First-pass cairn scrap-cap variant with blackened iron and dull bone accents kept subordinate to stone mass.",
        stacks=(scrap_cap_stack("ScrapCap", (0, 0, 0), rad(8)),),
    ),
)


def purge_unused_materials() -> None:
    for material in list(bpy.data.materials):
        if material.users == 0:
            bpy.data.materials.remove(material)


def add_scale_marker(name: str, height_cm: float, x: float, material: bpy.types.Material, y: float = -60.0) -> None:
    marker_collection = bpy.data.collections.get("Review_Markers")
    if marker_collection is None:
        marker_collection = make_collection("Review_Markers")
    add_box(f"Review_{name}_Post", (x, y, height_cm * 0.5), (8, 8, height_cm), (0, 0, 0), (0.78, 0.72, 0.58, 1.0), material, marker_collection)
    add_box(f"Review_{name}_Cap", (x, y, height_cm), (42, 8, 6), (0, 0, 0), (0.78, 0.72, 0.58, 1.0), material, marker_collection)


def add_label(text: str, location: tuple[float, float, float], size: float = 13.0) -> None:
    bpy.ops.object.text_add(location=location, rotation=(rad(72), 0, 0))
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


def render_review(spec: VariantSpec, material: bpy.types.Material) -> None:
    review_dir = REVIEW_ROOT / spec.asset_name
    review_dir.mkdir(parents=True, exist_ok=True)
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
    marker_y = -60.0
    female_marker_x = 245.0
    male_marker_x = 305.0
    add_scale_marker("GiantFemale_442cm", GIANT_FEMALE_BASELINE_CM, female_marker_x, marker_material, marker_y)
    add_scale_marker("GiantMale_470cm", GIANT_MALE_BASELINE_CM, male_marker_x, marker_material, marker_y)
    add_label("442 cm female Giant", (female_marker_x, marker_y - 15, 382), 11)
    add_label("470 cm male Giant", (male_marker_x, marker_y - 15, 410), 11)
    add_label("ground-center pivot", (0, marker_y - 12, 22), 12)

    bpy.ops.object.light_add(type="SUN", location=(0, -520, 820), rotation=(rad(48), 0, rad(24)))
    sun = bpy.context.object
    sun.name = "AET_BloodAxeCairnVariantReview_Sun"
    sun.data.energy = 1.0

    bpy.ops.object.light_add(type="AREA", location=(-260, -430, 380))
    key = bpy.context.object
    key.name = "AET_BloodAxeCairnVariantReview_KeyLight"
    key.data.energy = 590
    key.data.size = 470

    bpy.ops.object.light_add(type="AREA", location=(380, 300, 270))
    fill = bpy.context.object
    fill.name = "AET_BloodAxeCairnVariantReview_FillLight"
    fill.data.energy = 170
    fill.data.size = 540

    bpy.ops.object.camera_add(location=spec.camera)
    camera = bpy.context.object
    direction = Vector(spec.target) - Vector(camera.location)
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = spec.ortho_scale
    camera.data.clip_start = 1
    camera.data.clip_end = 5000
    scene.camera = camera

    scene.render.filepath = str(review_dir / f"{spec.asset_name}_DCCReview.png")
    bpy.ops.render.render(write_still=True)


def export_collection(collection: bpy.types.Collection, export_path: Path) -> None:
    export_path.parent.mkdir(parents=True, exist_ok=True)
    previous_collection_hidden = collection.hide_viewport
    collection.hide_viewport = False
    previous_object_hidden: list[tuple[bpy.types.Object, bool, bool]] = []
    bpy.ops.object.select_all(action="DESELECT")
    export_objects = [obj for obj in collection.objects if obj.type == "MESH"]
    for obj in export_objects:
        previous_object_hidden.append((obj, obj.hide_viewport, obj.hide_get()))
        obj.hide_viewport = False
        obj.hide_set(False)
        obj.select_set(True)
    if export_objects:
        bpy.context.view_layer.objects.active = export_objects[0]
    bpy.context.view_layer.update()
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
    for obj, hide_viewport, hide_get in previous_object_hidden:
        obj.hide_viewport = hide_viewport
        obj.hide_set(hide_get)
    collection.hide_viewport = previous_collection_hidden


def build_variant(spec: VariantSpec) -> None:
    clear_scene()
    setup_scene()
    material = review_material()

    lod_collections: list[bpy.types.Collection] = []
    for lod_level in range(4):
        hidden = lod_level > 0
        collection = make_collection(f"{spec.asset_name}_LOD{lod_level}_Source", hidden=hidden)
        lod_collections.append(collection)
        for stack in spec.stacks:
            build_stack(stack, material, collection, lod_level=lod_level)

    add_asset_metadata(
        spec.asset_name,
        f"{spec.summary} First-pass DCC source candidate only; not final sculpt, authored UV/texture pass, Unreal validation, or Fully game-ready content.",
        spec.unreal_path,
    )

    blend_path = BLENDER_ROOT / spec.rel_path / f"{spec.asset_name}.blend"
    export_path = EXPORT_ROOT / spec.rel_path / f"{spec.asset_name}.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    render_review(spec, material)
    purge_unused_materials()
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    export_collection(lod_collections[0], export_path)
    for lod_level, collection in enumerate(lod_collections):
        lod_path = export_path.parent / f"{spec.asset_name}_LOD{lod_level}.fbx"
        export_collection(collection, lod_path)

    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)} and LOD0-LOD3")
    print(f"Rendered {REVIEW_ROOT.relative_to(ROOT)}/{spec.asset_name}/{spec.asset_name}_DCCReview.png")


def build() -> None:
    for spec in VARIANTS:
        build_variant(spec)


if __name__ == "__main__":
    build()
