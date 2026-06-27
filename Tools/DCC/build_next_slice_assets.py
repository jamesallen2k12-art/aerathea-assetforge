#!/usr/bin/env python3
"""Build next-slice Aerathea DCC review sources and FBX exports.

Run with:
    blender --background --python Tools/DCC/build_next_slice_assets.py

These assets are deterministic first-pass DCC review sources. They validate
scale, pivots, proportions, skeleton layout, sockets, and Unreal import paths;
they are not final sculpted/painted production art.
"""

from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"

sys.path.insert(0, str(ROOT))

from Tools.DCC.generate_first_slice_meshes import Mesh, create_common_materials  # noqa: E402


@dataclass(frozen=True)
class StaticAssetBuild:
    rel_path: str
    factory: object
    unreal_path: str

    @property
    def name(self) -> str:
        return self.rel_path.split("/")[-1]

    @property
    def blend_path(self) -> Path:
        return BLENDER_ROOT / self.rel_path / f"{self.name}.blend"

    @property
    def export_path(self) -> Path:
        return EXPORT_ROOT / self.rel_path / f"{self.name}.fbx"


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def setup_scene() -> None:
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.01
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_EEVEE"
    scene.frame_start = 1
    scene.frame_end = 32


def get_material(name: str, color: tuple[float, float, float]) -> bpy.types.Material:
    existing = bpy.data.materials.get(name)
    if existing is not None:
        return existing

    material = bpy.data.materials.new(name)
    material.diffuse_color = (color[0], color[1], color[2], 1.0)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = (color[0], color[1], color[2], 1.0)
        bsdf.inputs["Roughness"].default_value = 0.82
        if "Aetherium" in name or "Glow" in name:
            bsdf.inputs["Emission Color"].default_value = (0.0, 0.8, 2.8, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 1.4
    return material


def add_trapezoid_prism(
    mesh: Mesh,
    name: str,
    x_min: float,
    x_max: float,
    half_width_min: float,
    half_width_max: float,
    half_thickness: float,
    z: float,
    material: str,
) -> None:
    obj = mesh.add_object(name, material)
    obj.verts.extend(
        [
            (x_min, -half_width_min, z - half_thickness),
            (x_min, half_width_min, z - half_thickness),
            (x_max, half_width_max, z - half_thickness),
            (x_max, -half_width_max, z - half_thickness),
            (x_min, -half_width_min, z + half_thickness),
            (x_min, half_width_min, z + half_thickness),
            (x_max, half_width_max, z + half_thickness),
            (x_max, -half_width_max, z + half_thickness),
        ]
    )
    obj.faces.extend(
        [
            (1, 2, 3, 4),
            (5, 8, 7, 6),
            (1, 5, 6, 2),
            (2, 6, 7, 3),
            (3, 7, 8, 4),
            (4, 8, 5, 1),
        ]
    )


def ratchet_cleaver() -> Mesh:
    mesh = Mesh("SM_MKG_RatchetCleaver_A01")
    m = create_common_materials(mesh)
    add_trapezoid_prism(
        mesh,
        "Blade_DarkIron_WideCleaver",
        14,
        45,
        12,
        18,
        1.8,
        0,
        m["dark_iron"],
    )
    mesh.add_box("Blade_Brass_ReinforcedSpine", (27, 15, 2.1), (30, 5, 4.2), m["brass"])
    mesh.add_box("Blade_DarkIron_HeelPlate", (13, 0, 0), (6, 25, 5.2), m["dark_iron"])
    for index, x in enumerate((19, 25, 31, 37), 1):
        mesh.add_box(f"RatchetTooth_Brass_{index:02d}", (x, 20, 0), (5, 5, 5), m["brass"])
    mesh.add_box("Guard_Brass_Block", (10, 0, 0), (6, 30, 10), m["brass"])
    mesh.add_cylinder("Grip_Leather_OversizedGnome", (0, 0, 0), 4.6, 26, m["leather"], "x", 14)
    mesh.add_cylinder("Grip_Brass_FrontBand", (10, 0, 0), 5.2, 3, m["brass"], "x", 14)
    mesh.add_cylinder("Grip_Brass_BackBand", (-10, 0, 0), 5.2, 3, m["brass"], "x", 14)
    mesh.add_cylinder("Pommel_Brass_Counterweight", (-17, 0, 0), 6.0, 6, m["brass"], "x", 14)
    mesh.add_diamond("CalibrationInset_Aetherium_Blue", (12, -16, 0), (7, 4, 7), m["aetherium"])
    mesh.add_box("SocketMarker_HandRWeapon_Pivot", (0, 0, -7), (3, 3, 3), m["aetherium"])
    mesh.add_box("UCX_SM_MKG_RatchetCleaver_A01_00", (13, 0, 0), (66, 44, 11), m["stone"])
    return mesh


def gear_mace() -> Mesh:
    mesh = Mesh("SM_MKG_GearMace_A01")
    m = create_common_materials(mesh)
    mesh.add_cylinder("Grip_Leather_OversizedGnome", (-6, 0, 0), 4.2, 34, m["leather"], "x", 14)
    mesh.add_cylinder("Grip_Brass_FrontBand", (10, 0, 0), 5.1, 3, m["brass"], "x", 14)
    mesh.add_cylinder("Grip_Brass_BackBand", (-21, 0, 0), 5.1, 3, m["brass"], "x", 14)
    mesh.add_cylinder("Pommel_DarkIron_Cap", (-27, 0, 0), 5.8, 7, m["dark_iron"], "x", 14)
    mesh.add_box("Guard_Brass_Block", (14, 0, 0), (5, 22, 10), m["brass"])
    mesh.add_cylinder("Head_DarkIron_GearCore", (28, 0, 0), 11.0, 13, m["dark_iron"], "x", 18)
    mesh.add_cylinder("Head_Brass_OuterHub", (29, 0, 0), 8.2, 16, m["brass"], "x", 18)

    tooth_specs = [
        ("Top", 0, 14, (10, 7, 9)),
        ("Bottom", 0, -14, (10, 7, 9)),
        ("Left", 14, 0, (10, 9, 7)),
        ("Right", -14, 0, (10, 9, 7)),
        ("DiagA", 10, 10, (10, 7, 7)),
        ("DiagB", -10, 10, (10, 7, 7)),
        ("DiagC", 10, -10, (10, 7, 7)),
        ("DiagD", -10, -10, (10, 7, 7)),
    ]
    for name, y, z, size in tooth_specs:
        mesh.add_box(f"GearTooth_DarkIron_{name}", (29, y, z), size, m["dark_iron"])

    mesh.add_cylinder("Head_Aetherium_CenterCap_Front", (38, 0, 0), 4.6, 3, m["aetherium"], "x", 14)
    mesh.add_cylinder("Head_Aetherium_CenterCap_Back", (20, 0, 0), 3.2, 2, m["aetherium"], "x", 12)
    mesh.add_box("SocketMarker_HandRWeapon_Pivot", (0, 0, -6.5), (3, 3, 3), m["aetherium"])
    mesh.add_box("UCX_SM_MKG_GearMace_A01_00", (8, 0, 0), (72, 44, 44), m["stone"])
    return mesh


def monkey_wrench() -> Mesh:
    mesh = Mesh("SM_MKG_MonkeyWrench_A01")
    m = create_common_materials(mesh)

    # Pivot sits at the grip center for future equipped-item socket checks.
    mesh.add_cylinder("Grip_Leather_ThickGnomeScale", (-10, 0, 0), 4.4, 42, m["leather"], "x", 14)
    mesh.add_cylinder("Grip_Brass_BackBand", (-29, 0, 0), 5.1, 4, m["brass"], "x", 14)
    mesh.add_cylinder("Grip_Brass_FrontBand", (10, 0, 0), 5.1, 4, m["brass"], "x", 14)
    mesh.add_box("Pommel_DarkIron_LanyardCap", (-34, 0, 0), (7, 12, 10), m["dark_iron"])
    mesh.add_box("Handle_DarkIron_InternalSpine", (-6, 0, 0), (36, 5, 6), m["dark_iron"])

    mesh.add_box("Collar_Brass_AdjusterBlock", (16, 0, 0), (10, 22, 16), m["brass"])
    mesh.add_cylinder("AdjusterWheel_DarkIron_ReadableKnob", (18, 0, 12), 6.0, 5, m["dark_iron"], "y", 14)
    for index, x in enumerate((13, 18, 23), 1):
        mesh.add_box(f"AdjusterTooth_Brass_{index:02d}", (x, -13, 12), (4, 4, 5), m["brass"])

    mesh.add_box("JawStem_DarkIron_ThickNeck", (27, 0, 0), (18, 10, 12), m["dark_iron"])
    mesh.add_box("JawFixed_DarkIron_UpperHook", (41, 0, 8), (24, 10, 9), m["dark_iron"])
    mesh.add_box("JawFixed_DarkIron_UpperTip", (51, 0, 2), (9, 10, 20), m["dark_iron"])
    mesh.add_box("JawSliding_DarkIron_LowerHook", (38, 0, -10), (18, 10, 8), m["dark_iron"])
    mesh.add_box("JawSliding_Brass_SlidePlate", (28, 0, -9), (12, 14, 9), m["brass"])

    mesh.add_diamond("Aetherium_CalibrationInset_Blue", (8, -7, 0), (5, 3, 6), m["aetherium"])
    mesh.add_box("SocketMarker_HandRWeapon_Pivot", (0, 0, -7), (3, 3, 3), m["aetherium"])
    mesh.add_box("UCX_SM_MKG_MonkeyWrench_A01_00", (8, 0, 0), (90, 32, 42), m["stone"])
    return mesh


def spike_drill() -> Mesh:
    mesh = Mesh("SM_MKG_SpikeDrill_A01")
    m = create_common_materials(mesh)

    # Pivot sits at grip center; the drill axis points forward on +X.
    mesh.add_cylinder("Grip_Leather_ThickGnomeScale", (-12, 0, 0), 4.5, 38, m["leather"], "x", 14)
    mesh.add_cylinder("Grip_Brass_BackBand", (-29, 0, 0), 5.2, 4, m["brass"], "x", 14)
    mesh.add_cylinder("Grip_Brass_FrontBand", (6, 0, 0), 5.2, 4, m["brass"], "x", 14)
    mesh.add_box("Pommel_DarkIron_Counterweight", (-35, 0, 0), (8, 13, 11), m["dark_iron"])
    mesh.add_box("Handle_DarkIron_InternalSpine", (-11, 0, 0), (36, 5, 6), m["dark_iron"])

    mesh.add_box("Guard_Brass_Block", (10, 0, 0), (6, 24, 12), m["brass"])
    mesh.add_box("Brace_Brass_TopLeft", (21, 8, 10), (28, 4, 4), m["brass"])
    mesh.add_box("Brace_Brass_TopRight", (21, -8, 10), (28, 4, 4), m["brass"])
    mesh.add_box("Brace_Brass_BottomLeft", (21, 8, -10), (28, 4, 4), m["brass"])
    mesh.add_box("Brace_Brass_BottomRight", (21, -8, -10), (28, 4, 4), m["brass"])

    mesh.add_cylinder("Motor_DarkIron_CylindricalCore", (28, 0, 0), 12.0, 22, m["dark_iron"], "x", 18)
    mesh.add_cylinder("Motor_Brass_RearCollar", (17, 0, 0), 13.2, 4, m["brass"], "x", 18)
    mesh.add_cylinder("Motor_Brass_FrontCollar", (39, 0, 0), 13.2, 4, m["brass"], "x", 18)
    mesh.add_box("Motor_DarkIron_SideHousingLeft", (28, 13, 0), (18, 5, 12), m["dark_iron"])
    mesh.add_box("Motor_DarkIron_SideHousingRight", (28, -13, 0), (18, 5, 12), m["dark_iron"])
    mesh.add_diamond("Aetherium_PowerInset_Blue", (24, -15, 0), (6, 3, 7), m["aetherium"])

    mesh.add_cylinder("DrillSpike_DarkIron_Base", (45, 0, 0), 7.2, 12, m["dark_iron"], "x", 14)
    mesh.add_cylinder("DrillSpike_DarkIron_MidTaper", (55, 0, 0), 5.2, 12, m["dark_iron"], "x", 12)
    mesh.add_cylinder("DrillSpike_DarkIron_Tip", (63, 0, 0), 3.1, 8, m["dark_iron"], "x", 10)
    mesh.add_box("DrillFlute_DarkIron_Top", (55, 0, 5), (22, 4, 3), m["dark_iron"])
    mesh.add_box("DrillFlute_DarkIron_Bottom", (55, 0, -5), (22, 4, 3), m["dark_iron"])
    mesh.add_box("DrillFlute_DarkIron_Left", (55, 5, 0), (22, 3, 4), m["dark_iron"])
    mesh.add_box("DrillFlute_DarkIron_Right", (55, -5, 0), (22, 3, 4), m["dark_iron"])

    mesh.add_box("SocketMarker_HandRWeapon_Pivot", (0, 0, -7), (3, 3, 3), m["aetherium"])
    mesh.add_box("UCX_SM_MKG_SpikeDrill_A01_00", (14, 0, 0), (100, 42, 38), m["stone"])
    return mesh


def grapple_hook() -> Mesh:
    mesh = Mesh("SM_MKG_GrappleHook_A01")
    m = create_common_materials(mesh)

    # Pivot sits at the gnome grip center. The hook fires forward on +X and the cable exits -X.
    mesh.add_cylinder("Grip_Leather_CompactLauncher", (-18, 0, -4), 4.4, 30, m["leather"], "x", 14)
    mesh.add_cylinder("Grip_Brass_BackBand", (-31, 0, -4), 5.1, 4, m["brass"], "x", 14)
    mesh.add_cylinder("Grip_Brass_FrontBand", (-5, 0, -4), 5.1, 4, m["brass"], "x", 14)
    mesh.add_box("TriggerGuard_Brass_LoopBlock", (-4, 0, -12), (15, 16, 5), m["brass"])
    mesh.add_box("Trigger_DarkIron_Lever", (-2, 0, -16), (7, 5, 7), m["dark_iron"])

    mesh.add_cylinder("CableSocket_DarkIron_RearHousing", (-42, 0, 0), 7.0, 10, m["dark_iron"], "x", 16)
    mesh.add_cylinder("CableSocket_Brass_Rim", (-48, 0, 0), 5.6, 4, m["brass"], "x", 14)
    mesh.add_cylinder("CablePort_Aetherium_BlueGuide", (-51, 0, 0), 2.8, 2, m["aetherium"], "x", 12)
    mesh.add_box("CableDrum_DarkIron_LeftCap", (-26, 13, 5), (18, 5, 16), m["dark_iron"])
    mesh.add_box("CableDrum_DarkIron_RightCap", (-26, -13, 5), (18, 5, 16), m["dark_iron"])
    mesh.add_cylinder("CableDrum_Brass_Winder", (-26, 0, 5), 8.0, 22, m["brass"], "y", 16)

    mesh.add_cylinder("LauncherBody_DarkIron_PressureTube", (5, 0, 3), 8.5, 32, m["dark_iron"], "x", 18)
    mesh.add_cylinder("LauncherBody_Brass_RearCollar", (-10, 0, 3), 9.4, 4, m["brass"], "x", 18)
    mesh.add_cylinder("LauncherBody_Brass_FrontCollar", (21, 0, 3), 9.4, 5, m["brass"], "x", 18)
    mesh.add_box("LauncherBody_DarkIron_TopPlate", (6, 0, 14), (26, 11, 4), m["dark_iron"])
    mesh.add_diamond("Aetherium_TensionLens_Blue", (2, -10, 5), (6, 3, 8), m["aetherium"])

    mesh.add_cylinder("HookNeck_DarkIron_ForwardShaft", (34, 0, 3), 4.8, 22, m["dark_iron"], "x", 14)
    mesh.add_cylinder("HookHub_Brass_TripleClawMount", (46, 0, 3), 9.0, 8, m["brass"], "x", 18)
    mesh.add_cylinder("HookHub_DarkIron_CenterPin", (50, 0, 3), 4.0, 10, m["dark_iron"], "x", 12)

    add_trapezoid_prism(
        mesh,
        "HookClaw_DarkIron_CenterForward",
        49,
        74,
        4.0,
        2.0,
        2.8,
        3,
        m["dark_iron"],
    )
    mesh.add_box("HookClaw_DarkIron_LeftArm", (58, 11, 3), (24, 5, 6), m["dark_iron"])
    mesh.add_box("HookClaw_DarkIron_LeftTip", (69, 17, 3), (8, 11, 8), m["dark_iron"])
    mesh.add_box("HookClaw_DarkIron_RightArm", (58, -11, 3), (24, 5, 6), m["dark_iron"])
    mesh.add_box("HookClaw_DarkIron_RightTip", (69, -17, 3), (8, 11, 8), m["dark_iron"])
    mesh.add_box("HookClaw_DarkIron_TopArm", (57, 0, 13), (23, 6, 5), m["dark_iron"])
    mesh.add_box("HookClaw_DarkIron_TopTip", (68, 0, 20), (8, 8, 12), m["dark_iron"])

    mesh.add_box("SocketMarker_Muzzle", (76, 0, 3), (3, 3, 3), m["aetherium"])
    mesh.add_box("SocketMarker_Cable", (-54, 0, 0), (3, 3, 3), m["aetherium"])
    mesh.add_box("UCX_SM_MKG_GrappleHook_A01_00", (10, 0, 4), (132, 50, 48), m["stone"])
    return mesh


def multi_tool() -> Mesh:
    mesh = Mesh("SM_MKG_MultiTool_A01")
    m = create_common_materials(mesh)

    # Pivot sits at the folded handle center for belt, table, and pickup-display checks.
    mesh.add_box("Handle_DarkIron_FoldedSpine", (0, 0, 0), (38, 10, 7), m["dark_iron"])
    mesh.add_box("Handle_Leather_LeftGripPanel", (-2, 6, 1), (28, 3, 6), m["leather"])
    mesh.add_box("Handle_Leather_RightGripPanel", (-2, -6, 1), (28, 3, 6), m["leather"])
    mesh.add_cylinder("Hinge_Brass_MainPivot", (16, 0, 0), 6.3, 6, m["brass"], "y", 14)
    mesh.add_cylinder("Hinge_DarkIron_CenterPin", (16, 0, 0), 3.0, 8, m["dark_iron"], "y", 12)
    mesh.add_box("EndCap_Brass_Back", (-21, 0, 0), (5, 14, 9), m["brass"])

    mesh.add_box("Tool_WrenchStem_DarkIron", (30, 0, 3), (24, 6, 6), m["dark_iron"])
    mesh.add_box("Tool_WrenchJaw_UpperHook", (44, 0, 9), (18, 7, 6), m["dark_iron"])
    mesh.add_box("Tool_WrenchJaw_UpperTip", (51, 0, 4), (6, 7, 14), m["dark_iron"])
    mesh.add_box("Tool_WrenchJaw_LowerHook", (42, 0, -4), (14, 7, 5), m["dark_iron"])
    mesh.add_box("Tool_WrenchJaw_BrassSlider", (30, 0, -4), (9, 9, 6), m["brass"])

    mesh.add_box("Tool_ScrewdriverBlade_DarkIron", (18, 0, -11), (28, 5, 4), m["dark_iron"])
    mesh.add_box("Tool_ScrewdriverTip_DarkIron", (34, 0, -11), (8, 3, 5), m["dark_iron"])
    mesh.add_box("FoldedTool_Brass_FileSpine", (-2, 0, 8), (30, 4, 3), m["brass"])
    mesh.add_box("FoldedTool_DarkIron_SawBack", (-4, 0, -8), (27, 4, 3), m["dark_iron"])
    for index, x in enumerate((-13, -7, -1, 5), 1):
        mesh.add_box(f"SawTooth_DarkIron_{index:02d}", (x, 0, -12), (4, 4, 4), m["dark_iron"])

    mesh.add_diamond("Aetherium_CalibrationInset_Blue", (-10, -8, 1), (5, 3, 6), m["aetherium"])
    mesh.add_box("SocketMarker_HandRWeapon_Pivot", (0, 0, -8), (3, 3, 3), m["aetherium"])
    mesh.add_box("UCX_SM_MKG_MultiTool_A01_00", (10, 0, 0), (78, 24, 32), m["stone"])
    return mesh


def tool_pack() -> Mesh:
    mesh = Mesh("SM_MKG_ToolPack_A01")
    m = create_common_materials(mesh)

    # Origin is the gnome back_pack attachment pivot; the pack extends backward on -X.
    mesh.add_box("AttachPlate_DarkIron_BackPackPivot", (-2, 0, 4), (4, 26, 42), m["dark_iron"])
    mesh.add_box("PackBody_Leather_StackedMain", (-16, 0, 4), (22, 30, 48), m["leather"])
    mesh.add_box("PackBody_Leather_LowerRoll", (-18, 0, -24), (24, 26, 12), m["leather"])
    mesh.add_box("TopRoll_Leather_ToolBlanket", (-18, 0, 34), (24, 24, 12), m["leather"])

    mesh.add_box("SidePouch_Left_Leather", (-16, 23, -2), (15, 11, 24), m["leather"])
    mesh.add_box("SidePouch_Right_Leather", (-16, -23, -2), (15, 11, 24), m["leather"])
    mesh.add_box("PocketFlap_Left_BrassLatch", (-6, 23, 8), (4, 12, 5), m["brass"])
    mesh.add_box("PocketFlap_Right_BrassLatch", (-6, -23, 8), (4, 12, 5), m["brass"])

    mesh.add_box("Strap_Left_DarkIron", (-4, 9, 4), (5, 4, 50), m["dark_iron"])
    mesh.add_box("Strap_Right_DarkIron", (-4, -9, 4), (5, 4, 50), m["dark_iron"])
    mesh.add_box("Strap_Center_BrassBuckle", (-1, 0, 4), (4, 9, 8), m["brass"])
    mesh.add_cylinder("TopHandle_Brass_Crossbar", (-16, 0, 47), 2.2, 25, m["brass"], "y", 10)
    mesh.add_cylinder("TopHandle_Brass_LeftPost", (-16, 10, 40), 1.8, 10, m["brass"], "z", 10)
    mesh.add_cylinder("TopHandle_Brass_RightPost", (-16, -10, 40), 1.8, 10, m["brass"], "z", 10)

    mesh.add_cylinder("Tool_Wrench_Handle_DarkIron", (-25, 26, 6), 2.1, 48, m["dark_iron"], "z", 10)
    mesh.add_box("Tool_Wrench_JawTop_DarkIron", (-25, 26, 34), (12, 4, 6), m["dark_iron"])
    mesh.add_box("Tool_Wrench_JawBottom_DarkIron", (-25, 26, 26), (12, 4, 6), m["dark_iron"])
    mesh.add_cylinder("Tool_Saw_Handle_Timber", (-25, -26, -10), 2.8, 17, m["timber"], "z", 10)
    mesh.add_box("Tool_Saw_Blade_DarkIron", (-25, -26, 14), (16, 4, 36), m["dark_iron"])
    for index, z in enumerate((1, 8, 15, 22), 1):
        mesh.add_box(f"Tool_Saw_Tooth_{index:02d}", (-15, -26, z), (5, 4, 4), m["dark_iron"])
    mesh.add_box("Tool_Screwdriver_BrassShaft", (-30, -15, 12), (5, 3, 42), m["brass"])
    mesh.add_box("Tool_Screwdriver_DarkIronTip", (-30, -15, 35), (6, 4, 6), m["dark_iron"])

    mesh.add_diamond("Aetherium_Core_SmallCharge", (-31, 0, 8), (6, 5, 9), m["aetherium"])
    mesh.add_box("SocketMarker_BackPack_Pivot", (0, 0, 0), (3, 3, 3), m["aetherium"])
    mesh.add_box("UCX_SM_MKG_ToolPack_A01_00", (-16, 0, 6), (36, 58, 78), m["stone"])
    return mesh


def palisade_wall() -> Mesh:
    mesh = Mesh("SM_AET_Palisade_Wall_A01")
    m = create_common_materials(mesh)
    for i, x in enumerate(range(-175, 176, 50), 1):
        height = 286 + (i % 3) * 12
        mesh.add_cylinder(f"Stake_Timber_{i:02d}", (x, 0, height / 2), 18, height, m["timber"], "z", 10)
        mesh.add_box(f"Stake_Point_{i:02d}", (x, 0, height + 12), (34, 34, 24), m["timber"])
    mesh.add_box("Brace_Timber_FrontUpper", (0, -28, 218), (410, 18, 32), m["timber"])
    mesh.add_box("Brace_Timber_FrontLower", (0, -30, 110), (410, 20, 30), m["timber"])
    mesh.add_box("IronStrap_Left", (-150, -42, 164), (16, 8, 170), m["dark_iron"])
    mesh.add_box("IronStrap_Right", (150, -42, 164), (16, 8, 170), m["dark_iron"])
    mesh.add_box("StoneFooting_Main", (0, 0, 12), (400, 62, 24), m["stone"])
    mesh.add_box("UCX_SM_AET_Palisade_Wall_A01_00", (0, 0, 150), (410, 70, 300), m["stone"])
    return mesh


def palisade_post() -> Mesh:
    mesh = Mesh("SM_AET_Palisade_Post_A01")
    m = create_common_materials(mesh)
    mesh.add_cylinder("Post_Timber_Heavy", (0, 0, 158), 32, 316, m["timber"], "z", 12)
    mesh.add_box("Post_Cap_Point", (0, 0, 332), (58, 58, 32), m["timber"])
    mesh.add_box("IronBand_Lower", (0, -35, 90), (74, 8, 18), m["dark_iron"])
    mesh.add_box("IronBand_Upper", (0, -35, 220), (74, 8, 18), m["dark_iron"])
    mesh.add_box("StoneFooting_Post", (0, 0, 14), (82, 82, 28), m["stone"])
    mesh.add_box("UCX_SM_AET_Palisade_Post_A01_00", (0, 0, 160), (82, 82, 320), m["stone"])
    return mesh


def palisade_endcap() -> Mesh:
    mesh = Mesh("SM_AET_Palisade_EndCap_A01")
    m = create_common_materials(mesh)
    for i, x in enumerate((-35, 0, 35), 1):
        height = 284 + i * 10
        mesh.add_cylinder(f"EndStake_Timber_{i:02d}", (x, 0, height / 2), 18, height, m["timber"], "z", 10)
    mesh.add_box("EndBrace_Timber", (0, -28, 160), (120, 18, 30), m["timber"])
    mesh.add_box("EndIronStrap", (0, -39, 160), (16, 8, 160), m["dark_iron"])
    mesh.add_box("StoneFooting_End", (0, 0, 12), (120, 62, 24), m["stone"])
    mesh.add_box("UCX_SM_AET_Palisade_EndCap_A01_00", (0, 0, 150), (130, 70, 300), m["stone"])
    return mesh


def palisade_corner() -> Mesh:
    mesh = Mesh("SM_AET_Palisade_Corner_A01")
    m = create_common_materials(mesh)
    for i, x in enumerate(range(-170, 171, 68), 1):
        mesh.add_cylinder(f"CornerStake_X_{i:02d}", (x, 0, 146), 16, 292, m["timber"], "z", 10)
    for i, y in enumerate(range(70, 371, 68), 1):
        mesh.add_cylinder(f"CornerStake_Y_{i:02d}", (-200, y, 146), 16, 292, m["timber"], "z", 10)
    mesh.add_cylinder("CornerPost_Heavy", (-200, 0, 162), 34, 324, m["timber"], "z", 12)
    mesh.add_box("Brace_X_Front", (-10, -28, 160), (390, 18, 32), m["timber"])
    mesh.add_box("Brace_Y_Inside", (-228, 188, 160), (18, 390, 32), m["timber"])
    mesh.add_box("StoneFooting_X", (-10, 0, 12), (400, 62, 24), m["stone"])
    mesh.add_box("StoneFooting_Y", (-200, 190, 12), (62, 400, 24), m["stone"])
    mesh.add_box("UCX_SM_AET_Palisade_Corner_A01_00", (-10, 0, 150), (410, 70, 300), m["stone"])
    mesh.add_box("UCX_SM_AET_Palisade_Corner_A01_01", (-200, 190, 150), (70, 410, 300), m["stone"])
    return mesh


def palisade_gate() -> Mesh:
    mesh = Mesh("SM_AET_Palisade_Gate_A01")
    m = create_common_materials(mesh)
    for x in (-220, 220):
        mesh.add_cylinder(f"GatePost_Timber_{x}", (x, 0, 166), 34, 332, m["timber"], "z", 12)
        mesh.add_box(f"GatePost_IronBand_{x}_Low", (x, -36, 100), (76, 8, 18), m["dark_iron"])
        mesh.add_box(f"GatePost_IronBand_{x}_High", (x, -36, 236), (76, 8, 18), m["dark_iron"])
    for x in range(-140, 141, 70):
        mesh.add_box(f"GatePlank_Timber_{x}", (x, -6, 144), (45, 20, 250), m["timber"])
    mesh.add_box("GateBrace_Timber_Top", (0, -22, 230), (330, 20, 28), m["timber"])
    mesh.add_box("GateBrace_Timber_Bottom", (0, -24, 88), (330, 20, 28), m["timber"])
    mesh.add_box("GateIronStrap_Left", (-150, -38, 158), (18, 8, 185), m["dark_iron"])
    mesh.add_box("GateIronStrap_Right", (150, -38, 158), (18, 8, 185), m["dark_iron"])
    mesh.add_box("GateLatch_DarkIron", (0, -42, 150), (46, 8, 34), m["dark_iron"])
    mesh.add_box("StoneFooting_GateLeft", (-220, 0, 14), (88, 88, 28), m["stone"])
    mesh.add_box("StoneFooting_GateRight", (220, 0, 14), (88, 88, 28), m["stone"])
    mesh.add_box("UCX_SM_AET_Palisade_Gate_A01_00", (0, 0, 150), (470, 76, 300), m["stone"])
    return mesh


STATIC_ASSETS = [
    StaticAssetBuild(
        "Kits/Mekgineer/Armory/SM_MKG_MultiTool_A01",
        multi_tool,
        "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_MultiTool_A01",
    ),
    StaticAssetBuild(
        "Kits/Mekgineer/Armory/SM_MKG_GrappleHook_A01",
        grapple_hook,
        "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_GrappleHook_A01",
    ),
    StaticAssetBuild(
        "Kits/Mekgineer/Armory/SM_MKG_SpikeDrill_A01",
        spike_drill,
        "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SpikeDrill_A01",
    ),
    StaticAssetBuild(
        "Kits/Mekgineer/Armory/SM_MKG_MonkeyWrench_A01",
        monkey_wrench,
        "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_MonkeyWrench_A01",
    ),
    StaticAssetBuild(
        "Kits/Mekgineer/Armory/SM_MKG_RatchetCleaver_A01",
        ratchet_cleaver,
        "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_RatchetCleaver_A01",
    ),
    StaticAssetBuild(
        "Kits/Mekgineer/Armory/SM_MKG_GearMace_A01",
        gear_mace,
        "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_GearMace_A01",
    ),
    StaticAssetBuild(
        "Kits/Mekgineer/Armory/SM_MKG_ToolPack_A01",
        tool_pack,
        "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_ToolPack_A01",
    ),
    StaticAssetBuild(
        "Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Wall_A01",
        palisade_wall,
        "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Wall_A01",
    ),
    StaticAssetBuild(
        "Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Post_A01",
        palisade_post,
        "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Post_A01",
    ),
    StaticAssetBuild(
        "Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Corner_A01",
        palisade_corner,
        "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Corner_A01",
    ),
    StaticAssetBuild(
        "Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Gate_A01",
        palisade_gate,
        "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Gate_A01",
    ),
    StaticAssetBuild(
        "Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_EndCap_A01",
        palisade_endcap,
        "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_EndCap_A01",
    ),
]


def polish_mesh_object(obj: bpy.types.Object) -> None:
    """Add review-pass UVs and normals so Unreal imports avoid tangent noise."""
    if obj.type != "MESH":
        return

    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    if not obj.data.uv_layers:
        obj.data.uv_layers.new(name="UV0")
    try:
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.02)
        bpy.ops.object.mode_set(mode="OBJECT")
    except RuntimeError:
        bpy.ops.object.mode_set(mode="OBJECT")

    if not any(mod.type == "WEIGHTED_NORMAL" for mod in obj.modifiers):
        modifier = obj.modifiers.new("WN_ReviewImport", "WEIGHTED_NORMAL")
        modifier.keep_sharp = True
        modifier.weight = 50
    obj.data.update()


def mesh_to_blender(mesh: Mesh) -> list[bpy.types.Object]:
    materials = {name: get_material(name, color) for name, color in mesh.materials.items()}
    created: list[bpy.types.Object] = []
    for source_obj in mesh.objects:
        blender_mesh = bpy.data.meshes.new(source_obj.name)
        faces = [tuple(index - 1 for index in face) for face in source_obj.faces]
        blender_mesh.from_pydata(source_obj.verts, [], faces)
        blender_mesh.update()

        obj = bpy.data.objects.new(source_obj.name, blender_mesh)
        bpy.context.collection.objects.link(obj)
        obj.data.materials.append(materials[source_obj.material])
        for polygon in obj.data.polygons:
            polygon.material_index = 0
        if source_obj.name.startswith("UCX_"):
            obj.display_type = "WIRE"
            obj.show_wire = True
        else:
            polish_mesh_object(obj)
        created.append(obj)
    return created


def add_asset_metadata(asset_name: str, status: str, unreal_path: str) -> None:
    empty = bpy.data.objects.new(f"{asset_name}_ProductionNotes", None)
    empty.empty_display_type = "PLAIN_AXES"
    empty.empty_display_size = 8
    empty["AeratheaStatus"] = status
    empty["Units"] = "Centimeters"
    empty["UnrealPath"] = unreal_path
    empty["Pipeline"] = "Source .blend -> FBX -> Unreal import"
    empty["ReviewUVs"] = "UV0 smart-projected for technical review; final UVs still require art-model pass"
    empty["LODPlan"] = "LOD0 source plus Unreal-generated LOD1-LOD3 for review validation"
    bpy.context.collection.objects.link(empty)


def export_static_asset(asset: StaticAssetBuild) -> None:
    clear_scene()
    setup_scene()
    mesh = asset.factory()
    mesh_to_blender(mesh)
    add_asset_metadata(
        asset.name,
        "DCC review source generated from approved Aerathea production handoff",
        asset.unreal_path,
    )
    asset.blend_path.parent.mkdir(parents=True, exist_ok=True)
    asset.export_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(asset.blend_path))
    bpy.ops.export_scene.fbx(
        filepath=str(asset.export_path),
        use_selection=False,
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
    print(f"Built {asset.blend_path.relative_to(ROOT)}")
    print(f"Exported {asset.export_path.relative_to(ROOT)}")


SKIN_MATERIALS = {
    "M_GNM_Skin_Blockout_A01": (0.78, 0.55, 0.38),
    "M_GNM_Workwear_Blockout_A01": (0.18, 0.24, 0.29),
    "M_GNM_BootLeather_Blockout_A01": (0.17, 0.10, 0.06),
    "M_GNM_Eye_Blockout_A01": (0.04, 0.16, 0.28),
    "M_CRE_Gryphon_Feather_Blockout_A01": (0.75, 0.58, 0.24),
    "M_CRE_Gryphon_Fur_Blockout_A01": (0.58, 0.38, 0.16),
    "M_CRE_Gryphon_Keratin_Blockout_A01": (0.78, 0.68, 0.46),
}


def create_materials(materials: dict[str, tuple[float, float, float]]) -> dict[str, bpy.types.Material]:
    return {name: get_material(name, color) for name, color in materials.items()}


def apply_transform(obj: bpy.types.Object) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)


def add_box_obj(
    name: str,
    center: tuple[float, float, float],
    size: tuple[float, float, float],
    material: bpy.types.Material,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1, location=center)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_Mesh"
    obj.dimensions = size
    apply_transform(obj)
    obj.data.materials.append(material)
    polish_mesh_object(obj)
    return obj


def add_ellipsoid_obj(
    name: str,
    center: tuple[float, float, float],
    radii: tuple[float, float, float],
    material: bpy.types.Material,
    segments: int = 16,
    rings: int = 8,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1, location=center)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_Mesh"
    obj.scale = radii
    apply_transform(obj)
    obj.data.materials.append(material)
    polish_mesh_object(obj)
    return obj


def add_cylinder_between(
    name: str,
    start: tuple[float, float, float],
    end: tuple[float, float, float],
    radius: float,
    material: bpy.types.Material,
    vertices: int = 12,
) -> bpy.types.Object:
    a = Vector(start)
    b = Vector(end)
    midpoint = (a + b) * 0.5
    direction = b - a
    length = direction.length
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=length, location=midpoint)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_Mesh"
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    apply_transform(obj)
    obj.data.materials.append(material)
    polish_mesh_object(obj)
    return obj


def create_armature(name: str, bone_defs: list[tuple[str, tuple[float, float, float], tuple[float, float, float], str | None]]) -> bpy.types.Object:
    bpy.ops.object.armature_add(enter_editmode=True, location=(0, 0, 0))
    armature = bpy.context.object
    armature.name = name
    armature.data.name = name
    armature.show_in_front = True

    edit_bones = armature.data.edit_bones
    for bone in list(edit_bones):
        edit_bones.remove(bone)
    created = {}
    for bone_name, head, tail, parent_name in bone_defs:
        bone = edit_bones.new(bone_name)
        bone.head = head
        bone.tail = tail
        bone.roll = 0.0
        if parent_name:
            bone.parent = created[parent_name]
            bone.use_connect = False
        created[bone_name] = bone
    bpy.ops.object.mode_set(mode="OBJECT")
    return armature


def assign_to_bone(obj: bpy.types.Object, armature: bpy.types.Object, bone_name: str) -> None:
    group = obj.vertex_groups.new(name=bone_name)
    group.add(range(len(obj.data.vertices)), 1.0, "ADD")
    modifier = obj.modifiers.new(name="Armature", type="ARMATURE")
    modifier.object = armature
    obj.parent = armature


def add_socket_empty(name: str, location: tuple[float, float, float], armature: bpy.types.Object, bone_name: str) -> bpy.types.Object:
    empty = bpy.data.objects.new(name, None)
    empty.empty_display_type = "SPHERE"
    empty.empty_display_size = 5
    empty.location = location
    empty.parent = armature
    empty.parent_type = "BONE"
    empty.parent_bone = bone_name
    bpy.context.collection.objects.link(empty)
    return empty


def export_skeletal_fbx(path: Path, objects: list[bpy.types.Object], armature: bpy.types.Object, bake_anim: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    bpy.ops.export_scene.fbx(
        filepath=str(path),
        use_selection=True,
        object_types={"ARMATURE", "MESH", "EMPTY"},
        mesh_smooth_type="FACE",
        global_scale=1.0,
        apply_unit_scale=False,
        apply_scale_options="FBX_SCALE_NONE",
        axis_forward="X",
        axis_up="Z",
        bake_space_transform=False,
        add_leaf_bones=False,
        bake_anim=bake_anim,
        bake_anim_use_all_actions=False,
        bake_anim_use_nla_strips=False,
    )


def build_gnome_base() -> None:
    clear_scene()
    setup_scene()
    mats = create_materials(SKIN_MATERIALS)
    bones = [
        ("root", (0, 0, 0), (0, 0, 12), None),
        ("pelvis", (0, 0, 46), (0, 0, 58), "root"),
        ("spine_01", (0, 0, 58), (0, 0, 76), "pelvis"),
        ("chest", (0, 0, 76), (0, 0, 90), "spine_01"),
        ("neck", (0, 0, 90), (0, 0, 96), "chest"),
        ("head", (0, 0, 96), (0, 0, 116), "neck"),
        ("ear_l", (0, 11, 104), (0, 27, 108), "head"),
        ("ear_r", (0, -11, 104), (0, -27, 108), "head"),
        ("clavicle_l", (0, 8, 86), (0, 18, 84), "chest"),
        ("upperarm_l", (0, 18, 84), (0, 31, 64), "clavicle_l"),
        ("lowerarm_l", (0, 31, 64), (0, 33, 43), "upperarm_l"),
        ("hand_l", (0, 33, 43), (0, 35, 34), "lowerarm_l"),
        ("clavicle_r", (0, -8, 86), (0, -18, 84), "chest"),
        ("upperarm_r", (0, -18, 84), (0, -31, 64), "clavicle_r"),
        ("lowerarm_r", (0, -31, 64), (0, -33, 43), "upperarm_r"),
        ("hand_r", (0, -33, 43), (0, -35, 34), "lowerarm_r"),
        ("thigh_l", (0, 8, 48), (0, 12, 26), "pelvis"),
        ("calf_l", (0, 12, 26), (0, 12, 8), "thigh_l"),
        ("foot_l", (0, 12, 8), (12, 12, 2), "calf_l"),
        ("thigh_r", (0, -8, 48), (0, -12, 26), "pelvis"),
        ("calf_r", (0, -12, 26), (0, -12, 8), "thigh_r"),
        ("foot_r", (0, -12, 8), (12, -12, 2), "calf_r"),
    ]
    armature = create_armature("SKEL_GNM_Base_A01", bones)
    objects: list[bpy.types.Object] = []
    skin = mats["M_GNM_Skin_Blockout_A01"]
    cloth = mats["M_GNM_Workwear_Blockout_A01"]
    boot = mats["M_GNM_BootLeather_Blockout_A01"]
    eye = mats["M_GNM_Eye_Blockout_A01"]

    for obj, bone in [
        (add_ellipsoid_obj("Body_Head", (0, 0, 100), (12, 13, 16), skin), "head"),
        (add_ellipsoid_obj("Body_LeftEar", (0, 19, 103), (5, 12, 8), skin, 12, 6), "ear_l"),
        (add_ellipsoid_obj("Body_RightEar", (0, -19, 103), (5, 12, 8), skin, 12, 6), "ear_r"),
        (add_ellipsoid_obj("Body_Torso_Workwear", (0, 0, 70), (15, 12, 22), cloth), "spine_01"),
        (add_ellipsoid_obj("Body_Pelvis_Workwear", (0, 0, 48), (14, 13, 9), cloth), "pelvis"),
        (add_ellipsoid_obj("Eye_Left", (10, 5, 102), (2.2, 1.0, 2.0), eye, 8, 4), "head"),
        (add_ellipsoid_obj("Eye_Right", (10, -5, 102), (2.2, 1.0, 2.0), eye, 8, 4), "head"),
        (add_cylinder_between("Arm_Left_Upper", (0, 18, 82), (1, 30, 63), 4.2, skin), "upperarm_l"),
        (add_cylinder_between("Arm_Left_Lower", (1, 30, 63), (1, 33, 44), 3.8, skin), "lowerarm_l"),
        (add_ellipsoid_obj("Hand_Left_FourFingerBlock", (2, 35, 36), (5, 4, 5), skin, 10, 5), "hand_l"),
        (add_cylinder_between("Arm_Right_Upper", (0, -18, 82), (1, -30, 63), 4.2, skin), "upperarm_r"),
        (add_cylinder_between("Arm_Right_Lower", (1, -30, 63), (1, -33, 44), 3.8, skin), "lowerarm_r"),
        (add_ellipsoid_obj("Hand_Right_FourFingerBlock", (2, -35, 36), (5, 4, 5), skin, 10, 5), "hand_r"),
        (add_cylinder_between("Leg_Left_Upper", (0, 8, 46), (2, 12, 27), 5.2, cloth), "thigh_l"),
        (add_cylinder_between("Leg_Left_Lower", (2, 12, 27), (3, 12, 9), 4.8, cloth), "calf_l"),
        (add_box_obj("Boot_Left_Oversized", (9, 12, 4), (18, 10, 8), boot), "foot_l"),
        (add_cylinder_between("Leg_Right_Upper", (0, -8, 46), (2, -12, 27), 5.2, cloth), "thigh_r"),
        (add_cylinder_between("Leg_Right_Lower", (2, -12, 27), (3, -12, 9), 4.8, cloth), "calf_r"),
        (add_box_obj("Boot_Right_Oversized", (9, -12, 4), (18, 10, 8), boot), "foot_r"),
    ]:
        assign_to_bone(obj, armature, bone)
        objects.append(obj)

    for side, y, bone in (("Left", 38, "hand_l"), ("Right", -38, "hand_r")):
        for idx, offset in enumerate((-3.0, -1.0, 1.0, 3.0), 1):
            obj = add_cylinder_between(f"Hand_{side}_Finger_{idx}", (3, y, 36 + offset), (8, y, 36 + offset), 0.8, skin, 8)
            assign_to_bone(obj, armature, bone)
            objects.append(obj)
        thumb = add_cylinder_between(f"Hand_{side}_Thumb", (1, y, 39), (6, y + (4 if y > 0 else -4), 42), 0.9, skin, 8)
        assign_to_bone(thumb, armature, bone)
        objects.append(thumb)

    for socket_name, location, bone_name in [
        ("SOCKET_hand_r_weapon", (4, -38, 37), "hand_r"),
        ("SOCKET_hand_l_offhand", (4, 38, 37), "hand_l"),
        ("SOCKET_back_pack", (-10, 0, 74), "chest"),
        ("SOCKET_head_goggles", (11, 0, 103), "head"),
        ("SOCKET_belt_tool_l", (0, 15, 50), "pelvis"),
        ("SOCKET_belt_tool_r", (0, -15, 50), "pelvis"),
        ("SOCKET_muzzle_preview", (12, -39, 37), "hand_r"),
        ("SOCKET_vfx_aether_core", (9, 0, 78), "chest"),
    ]:
        add_socket_empty(socket_name, location, armature, bone_name)

    add_asset_metadata(
        "SK_GNM_Base_A01",
        "First-pass DCC review body and skeleton; final sculpt, retopo, LODs, physics, and textures pending",
        "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01",
    )
    blend_path = BLENDER_ROOT / "Characters/Gnomes/SK_GNM_Base_A01/SK_GNM_Base_A01.blend"
    export_path = EXPORT_ROOT / "Characters/Gnomes/SK_GNM_Base_A01/SK_GNM_Base_A01.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    export_skeletal_fbx(export_path, objects, armature, bake_anim=False)
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")


def build_gryphon_base() -> None:
    clear_scene()
    setup_scene()
    mats = create_materials(SKIN_MATERIALS)
    bones = [
        ("root", (0, 0, 0), (0, 0, 18), None),
        ("pelvis", (-35, 0, 70), (-12, 0, 82), "root"),
        ("spine", (-12, 0, 82), (34, 0, 96), "pelvis"),
        ("chest", (34, 0, 96), (64, 0, 104), "spine"),
        ("neck", (64, 0, 104), (94, 0, 122), "chest"),
        ("head", (94, 0, 122), (126, 0, 128), "neck"),
        ("jaw", (112, 0, 118), (132, 0, 114), "head"),
        ("tail_01", (-58, 0, 72), (-86, 0, 72), "pelvis"),
        ("tail_02", (-86, 0, 72), (-116, 0, 76), "tail_01"),
        ("wing_l_upper", (28, 18, 102), (8, 86, 126), "chest"),
        ("wing_l_lower", (8, 86, 126), (-22, 148, 116), "wing_l_upper"),
        ("wing_r_upper", (28, -18, 102), (8, -86, 126), "chest"),
        ("wing_r_lower", (8, -86, 126), (-22, -148, 116), "wing_r_upper"),
        ("foreleg_l_upper", (48, 16, 88), (54, 22, 50), "chest"),
        ("foreleg_l_lower", (54, 22, 50), (62, 24, 16), "foreleg_l_upper"),
        ("forefoot_l", (62, 24, 16), (76, 24, 3), "foreleg_l_lower"),
        ("foreleg_r_upper", (48, -16, 88), (54, -22, 50), "chest"),
        ("foreleg_r_lower", (54, -22, 50), (62, -24, 16), "foreleg_r_upper"),
        ("forefoot_r", (62, -24, 16), (76, -24, 3), "foreleg_r_lower"),
        ("hindleg_l_upper", (-28, 18, 70), (-26, 24, 40), "pelvis"),
        ("hindleg_l_lower", (-26, 24, 40), (-10, 24, 15), "hindleg_l_upper"),
        ("hindfoot_l", (-10, 24, 15), (10, 24, 4), "hindleg_l_lower"),
        ("hindleg_r_upper", (-28, -18, 70), (-26, -24, 40), "pelvis"),
        ("hindleg_r_lower", (-26, -24, 40), (-10, -24, 15), "hindleg_r_upper"),
        ("hindfoot_r", (-10, -24, 15), (10, -24, 4), "hindleg_r_lower"),
    ]
    armature = create_armature("SKEL_CRE_Gryphon_A01", bones)
    objects: list[bpy.types.Object] = []
    feather = mats["M_CRE_Gryphon_Feather_Blockout_A01"]
    fur = mats["M_CRE_Gryphon_Fur_Blockout_A01"]
    keratin = mats["M_CRE_Gryphon_Keratin_Blockout_A01"]

    for obj, bone in [
        (add_ellipsoid_obj("Body_LionRear", (-32, 0, 74), (36, 22, 23), fur), "pelvis"),
        (add_ellipsoid_obj("Body_EagleChest", (34, 0, 92), (36, 20, 28), feather), "chest"),
        (add_cylinder_between("Neck_FeatherRuff", (62, 0, 104), (92, 0, 122), 12, feather, 14), "neck"),
        (add_ellipsoid_obj("Head_Eagle", (112, 0, 125), (18, 12, 13), feather), "head"),
        (add_box_obj("Beak_Keratin", (132, 0, 122), (30, 12, 9), keratin), "head"),
        (add_box_obj("Crest_Feather", (105, 0, 141), (22, 8, 12), feather), "head"),
        (add_cylinder_between("Tail_Lion", (-58, 0, 72), (-118, 0, 76), 5, fur, 10), "tail_01"),
        (add_ellipsoid_obj("Tail_Tuft", (-126, 0, 77), (13, 9, 9), fur), "tail_02"),
    ]:
        assign_to_bone(obj, armature, bone)
        objects.append(obj)

    for side, sign in (("Left", 1), ("Right", -1)):
        wing_upper = add_box_obj(f"Wing_{side}_UpperFeatherMass", (16, sign * 54, 112), (45, 78, 10), feather)
        wing_upper.rotation_euler[0] = math.radians(0)
        assign_to_bone(wing_upper, armature, f"wing_{'l' if sign > 0 else 'r'}_upper")
        objects.append(wing_upper)
        wing_lower = add_box_obj(f"Wing_{side}_PrimaryFeatherSlabs", (-12, sign * 120, 108), (55, 90, 8), feather)
        assign_to_bone(wing_lower, armature, f"wing_{'l' if sign > 0 else 'r'}_lower")
        objects.append(wing_lower)
        for i, x in enumerate((-30, -14, 2, 18), 1):
            feather_slab = add_box_obj(f"Wing_{side}_SilhouetteFeather_{i:02d}", (x, sign * (144 + i * 5), 96 - i * 5), (10, 48, 5), feather)
            assign_to_bone(feather_slab, armature, f"wing_{'l' if sign > 0 else 'r'}_lower")
            objects.append(feather_slab)

        for prefix, upper_bone, lower_bone, foot_bone, x0 in (
            ("Fore", f"foreleg_{'l' if sign > 0 else 'r'}_upper", f"foreleg_{'l' if sign > 0 else 'r'}_lower", f"forefoot_{'l' if sign > 0 else 'r'}", 52),
            ("Hind", f"hindleg_{'l' if sign > 0 else 'r'}_upper", f"hindleg_{'l' if sign > 0 else 'r'}_lower", f"hindfoot_{'l' if sign > 0 else 'r'}", -26),
        ):
            upper = add_cylinder_between(f"{prefix}Leg_{side}_Upper", (x0, sign * 18, 78), (x0 + 5, sign * 24, 44), 6, fur if prefix == "Hind" else feather, 10)
            assign_to_bone(upper, armature, upper_bone)
            objects.append(upper)
            lower = add_cylinder_between(f"{prefix}Leg_{side}_Lower", (x0 + 5, sign * 24, 44), (x0 + 16, sign * 24, 12), 5, fur if prefix == "Hind" else feather, 10)
            assign_to_bone(lower, armature, lower_bone)
            objects.append(lower)
            foot = add_box_obj(f"{prefix}Foot_{side}", (x0 + 26, sign * 24, 5), (24, 10, 8), keratin if prefix == "Fore" else fur)
            assign_to_bone(foot, armature, foot_bone)
            objects.append(foot)
            for claw_idx, claw_y in enumerate((-4, 0, 4), 1):
                claw = add_box_obj(f"{prefix}Claw_{side}_{claw_idx}", (x0 + 40, sign * (24 + claw_y), 3), (12, 2.5, 3), keratin)
                assign_to_bone(claw, armature, foot_bone)
                objects.append(claw)

    add_socket_empty("SOCKET_saddle_root", (-4, 0, 106), armature, "spine")
    add_socket_empty("SOCKET_head_vfx", (124, 0, 130), armature, "head")
    add_socket_empty("SOCKET_wing_l_vfx", (-22, 148, 116), armature, "wing_l_lower")
    add_socket_empty("SOCKET_wing_r_vfx", (-22, -148, 116), armature, "wing_r_lower")

    action = bpy.data.actions.new("ANIM_CRE_Gryphon_WingSpread_Blockout")
    armature.animation_data_create()
    armature.animation_data.action = action
    for frame, angle in ((1, 0), (16, 24), (32, 0)):
        bpy.context.scene.frame_set(frame)
        for bone_name, sign in (("wing_l_upper", 1), ("wing_l_lower", 1), ("wing_r_upper", -1), ("wing_r_lower", -1)):
            pose_bone = armature.pose.bones[bone_name]
            pose_bone.rotation_mode = "XYZ"
            pose_bone.rotation_euler = (math.radians(angle * 0.25), math.radians(0), math.radians(sign * angle))
            pose_bone.keyframe_insert(data_path="rotation_euler", frame=frame)

    add_asset_metadata(
        "SK_CRE_Gryphon_A01",
        "First-pass DCC review creature source with skeleton and wing-spread blockout; final sculpt, skinning, physics, LODs, and textures pending",
        "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01",
    )
    blend_path = BLENDER_ROOT / "Creatures/Gryphon/SK_CRE_Gryphon_A01/SK_CRE_Gryphon_A01.blend"
    export_path = EXPORT_ROOT / "Creatures/Gryphon/SK_CRE_Gryphon_A01/SK_CRE_Gryphon_A01.fbx"
    blend_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    export_skeletal_fbx(export_path, objects, armature, bake_anim=True)
    print(f"Built {blend_path.relative_to(ROOT)}")
    print(f"Exported {export_path.relative_to(ROOT)}")


def selected_asset_names() -> set[str]:
    raw = os.environ.get("AET_BUILD_ASSETS", "")
    return {part.strip() for part in raw.split(",") if part.strip()}


def main() -> None:
    selected = selected_asset_names()
    known = {asset.name for asset in STATIC_ASSETS} | {"SK_GNM_Base_A01", "SK_CRE_Gryphon_A01"}
    unknown = selected - known
    if unknown:
        raise RuntimeError(f"Unknown AET_BUILD_ASSETS entries: {', '.join(sorted(unknown))}")

    for asset in STATIC_ASSETS:
        if not selected or asset.name in selected:
            export_static_asset(asset)
    if not selected or "SK_GNM_Base_A01" in selected:
        build_gnome_base()
    if not selected or "SK_CRE_Gryphon_A01" in selected:
        build_gryphon_base()


if __name__ == "__main__":
    main()
