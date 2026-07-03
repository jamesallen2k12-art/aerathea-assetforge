#!/usr/bin/env python3
"""Generate first-slice Aerathea source meshes without Blender.

Blender is the preferred DCC, but the local Blender binary currently fails to
launch because of a USD/MaterialX library mismatch. This script creates
deterministic OBJ source meshes from the approved production handoffs so the
first Unreal import loop can proceed while the Blender install is repaired.
"""

from __future__ import annotations

import math
import subprocess
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "SourceAssets"
BLENDER_ROOT = SOURCE_ROOT / "Blender"
EXPORT_ROOT = SOURCE_ROOT / "Exports"


@dataclass
class ObjObject:
    name: str
    material: str
    verts: list[tuple[float, float, float]] = field(default_factory=list)
    faces: list[tuple[int, ...]] = field(default_factory=list)


class Mesh:
    def __init__(self, name: str):
        self.name = name
        self.objects: list[ObjObject] = []
        self.materials: dict[str, tuple[float, float, float]] = {}

    def material(self, name: str, color: tuple[float, float, float]) -> str:
        self.materials[name] = color
        return name

    def add_object(self, name: str, material: str) -> ObjObject:
        obj = ObjObject(name=name, material=material)
        self.objects.append(obj)
        return obj

    def add_box(
        self,
        name: str,
        center: tuple[float, float, float],
        size: tuple[float, float, float],
        material: str,
    ) -> None:
        cx, cy, cz = center
        sx, sy, sz = (size[0] / 2.0, size[1] / 2.0, size[2] / 2.0)
        verts = [
            (cx - sx, cy - sy, cz - sz),
            (cx + sx, cy - sy, cz - sz),
            (cx + sx, cy + sy, cz - sz),
            (cx - sx, cy + sy, cz - sz),
            (cx - sx, cy - sy, cz + sz),
            (cx + sx, cy - sy, cz + sz),
            (cx + sx, cy + sy, cz + sz),
            (cx - sx, cy + sy, cz + sz),
        ]
        faces = [
            (1, 2, 3, 4),
            (5, 8, 7, 6),
            (1, 5, 6, 2),
            (2, 6, 7, 3),
            (3, 7, 8, 4),
            (4, 8, 5, 1),
        ]
        obj = self.add_object(name, material)
        obj.verts.extend(verts)
        obj.faces.extend(faces)

    def add_cylinder(
        self,
        name: str,
        center: tuple[float, float, float],
        radius: float,
        depth: float,
        material: str,
        axis: str = "z",
        segments: int = 16,
    ) -> None:
        obj = self.add_object(name, material)
        half = depth / 2.0
        ring_a = []
        ring_b = []
        for i in range(segments):
            ang = math.tau * i / segments
            ca, sa = math.cos(ang), math.sin(ang)
            if axis == "z":
                a = (center[0] + ca * radius, center[1] + sa * radius, center[2] - half)
                b = (center[0] + ca * radius, center[1] + sa * radius, center[2] + half)
            elif axis == "x":
                a = (center[0] - half, center[1] + ca * radius, center[2] + sa * radius)
                b = (center[0] + half, center[1] + ca * radius, center[2] + sa * radius)
            else:
                a = (center[0] + ca * radius, center[1] - half, center[2] + sa * radius)
                b = (center[0] + ca * radius, center[1] + half, center[2] + sa * radius)
            ring_a.append(len(obj.verts) + 1)
            obj.verts.append(a)
            ring_b.append(len(obj.verts) + 1)
            obj.verts.append(b)
        for i in range(segments):
            j = (i + 1) % segments
            obj.faces.append((ring_a[i], ring_a[j], ring_b[j], ring_b[i]))
        obj.faces.append(tuple(reversed(ring_a)))
        obj.faces.append(tuple(ring_b))

    def add_ellipsoid(
        self,
        name: str,
        center: tuple[float, float, float],
        radii: tuple[float, float, float],
        material: str,
        rings: int = 8,
        segments: int = 16,
    ) -> None:
        obj = self.add_object(name, material)
        bottom_index = 1
        obj.verts.append((center[0], center[1], center[2] - radii[2]))
        for r in range(1, rings):
            phi = -math.pi / 2.0 + math.pi * r / rings
            cp = math.cos(phi)
            sp = math.sin(phi)
            for s in range(segments):
                theta = math.tau * s / segments
                obj.verts.append(
                    (
                        center[0] + math.cos(theta) * cp * radii[0],
                        center[1] + math.sin(theta) * cp * radii[1],
                        center[2] + sp * radii[2],
                    )
                )
        top_index = len(obj.verts) + 1
        obj.verts.append((center[0], center[1], center[2] + radii[2]))

        first_ring = 2
        last_ring = 2 + (rings - 2) * segments
        for s in range(segments):
            a = first_ring + s
            b = first_ring + ((s + 1) % segments)
            obj.faces.append((bottom_index, b, a))

        for r in range(rings - 2):
            current = 2 + r * segments
            nxt = current + segments
            for s in range(segments):
                a = current + s
                b = current + ((s + 1) % segments)
                c = nxt + ((s + 1) % segments)
                d = nxt + s
                obj.faces.append((a, b, c, d))

        for s in range(segments):
            a = last_ring + s
            b = last_ring + ((s + 1) % segments)
            obj.faces.append((a, b, top_index))

    def add_diamond(
        self,
        name: str,
        center: tuple[float, float, float],
        size: tuple[float, float, float],
        material: str,
    ) -> None:
        cx, cy, cz = center
        sx, sy, sz = (size[0] / 2.0, size[1] / 2.0, size[2] / 2.0)
        obj = self.add_object(name, material)
        obj.verts.extend(
            [
                (cx, cy, cz + sz),
                (cx + sx, cy, cz),
                (cx, cy + sy, cz),
                (cx - sx, cy, cz),
                (cx, cy - sy, cz),
                (cx, cy, cz - sz),
            ]
        )
        obj.faces.extend(
            [
                (1, 2, 3),
                (1, 3, 4),
                (1, 4, 5),
                (1, 5, 2),
                (6, 3, 2),
                (6, 4, 3),
                (6, 5, 4),
                (6, 2, 5),
            ]
        )

    def write(self, obj_path: Path) -> None:
        obj_path.parent.mkdir(parents=True, exist_ok=True)
        mtl_path = obj_path.with_suffix(".mtl")
        with mtl_path.open("w", encoding="utf-8") as mtl:
            mtl.write(f"# Materials for {self.name}\n")
            for name, color in self.materials.items():
                mtl.write(f"newmtl {name}\n")
                mtl.write(f"Kd {color[0]:.4f} {color[1]:.4f} {color[2]:.4f}\n")
                mtl.write("Ks 0.0500 0.0500 0.0500\n")
                mtl.write("Ns 12.0000\n\n")
        with obj_path.open("w", encoding="utf-8") as obj_file:
            obj_file.write(f"# {self.name}\n")
            obj_file.write(f"mtllib {mtl_path.name}\n")
            offset = 0
            for obj in self.objects:
                obj_file.write(f"o {obj.name}\n")
                obj_file.write(f"usemtl {obj.material}\n")
                for v in obj.verts:
                    obj_file.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
                for face in obj.faces:
                    indices = " ".join(str(offset + idx) for idx in face)
                    obj_file.write(f"f {indices}\n")
                offset += len(obj.verts)


def create_common_materials(mesh: Mesh) -> dict[str, str]:
    return {
        "stone": mesh.material("M_AET_Stone_Handpainted_A01", (0.34, 0.35, 0.34)),
        "timber": mesh.material("M_AET_Timber_Handpainted_A01", (0.38, 0.22, 0.11)),
        "straw": mesh.material("M_AET_Straw_A01", (0.72, 0.52, 0.20)),
        "leather": mesh.material("M_AET_Leather_Dark_A01", (0.19, 0.11, 0.07)),
        "dark_iron": mesh.material("M_AET_DarkIron_A01", (0.08, 0.09, 0.10)),
        "brass": mesh.material("M_AET_Brass_A01", (0.74, 0.50, 0.20)),
        "aetherium": mesh.material("M_AET_AetheriumGlow_Blue_A01", (0.05, 0.34, 0.90)),
        "earth": mesh.material("M_AET_PackedEarth_A01", (0.25, 0.19, 0.13)),
        "moss": mesh.material("M_AET_Moss_A01", (0.18, 0.30, 0.16)),
    }


def target_dummy() -> Mesh:
    mesh = Mesh("SM_AET_TargetDummy_A01")
    m = create_common_materials(mesh)
    mesh.add_cylinder("Post_Main", (0, 0, 92), 13, 184, m["timber"], "z", 18)
    mesh.add_cylinder("Crossbar_Main", (0, 0, 162), 10, 130, m["timber"], "x", 14)
    mesh.add_ellipsoid("Torso_StrawWrap", (0, 0, 112), (34, 24, 48), m["straw"], 8, 18)
    mesh.add_box("TargetPlate_Front", (0, -24, 125), (52, 5, 64), m["leather"])
    for z in (95, 125, 151):
        mesh.add_box(f"Strap_Leather_{z}", (0, -27, z), (62, 5, 6), m["leather"])
    mesh.add_box("Base_XFeet_A", (0, 0, 7), (115, 16, 14), m["timber"])
    mesh.add_box("Base_XFeet_B", (0, 0, 7), (16, 115, 14), m["timber"])
    mesh.add_box("Band_Iron_PostLower", (0, 0, 45), (34, 34, 7), m["dark_iron"])
    mesh.add_box("Band_Iron_PostUpper", (0, 0, 167), (32, 32, 7), m["dark_iron"])
    mesh.add_box("Paint_AetheriumMark", (0, -30, 129), (28, 3, 8), m["aetherium"])
    mesh.add_box("UCX_SM_AET_TargetDummy_A01_00", (0, 0, 104), (70, 55, 145), m["stone"])
    mesh.add_box("UCX_SM_AET_TargetDummy_A01_01", (0, 0, 162), (130, 22, 22), m["stone"])
    mesh.add_box("UCX_SM_AET_TargetDummy_A01_02", (0, 0, 8), (115, 115, 16), m["stone"])
    return mesh


def portal_arch() -> Mesh:
    mesh = Mesh("SM_AET_PortalArch_A01")
    m = create_common_materials(mesh)
    for x, side in ((-520, "Left"), (520, "Right")):
        mesh.add_box(f"Base_{side}_MegalithFoot", (x, 0, 36), (300, 340, 72), m["stone"])
        mesh.add_box(f"Column_{side}_LowerMegalith", (x, 0, 270), (190, 260, 500), m["stone"])
        mesh.add_box(f"Column_{side}_UpperMegalith", (x, 0, 760), (210, 250, 500), m["stone"])
        mesh.add_box(f"Column_{side}_OuterShoulder", (x + (-125 if x < 0 else 125), 12, 570), (70, 215, 850), m["stone"])
        mesh.add_box(f"IronBand_{side}_Lower", (x, -134, 265), (240, 18, 34), m["dark_iron"])
        mesh.add_box(f"IronBand_{side}_Upper", (x, -134, 775), (260, 18, 34), m["dark_iron"])
        mesh.add_diamond(f"AetheriumSocket_{side}_Lower", (x, -152, 410), (54, 18, 82), m["aetherium"])
        mesh.add_diamond(f"AetheriumSocket_{side}_Upper", (x, -152, 830), (58, 18, 92), m["aetherium"])

    mesh.add_box("Capstone_Main_ImpossibleSlab", (0, 0, 1100), (1240, 280, 160), m["stone"])
    mesh.add_box("Capstone_Top_WeatheredCrown", (0, 0, 1230), (1010, 238, 80), m["stone"])
    mesh.add_box("Capstone_BackCounterweight", (0, 105, 1038), (1060, 76, 72), m["stone"])
    mesh.add_diamond("Keystone_Aetherium_AncientCore", (0, -156, 1095), (95, 24, 132), m["aetherium"])

    mesh.add_box("InnerFrame_Left_DarkIron", (-410, -142, 510), (32, 28, 900), m["dark_iron"])
    mesh.add_box("InnerFrame_Right_DarkIron", (410, -142, 510), (32, 28, 900), m["dark_iron"])
    mesh.add_box("InnerFrame_Top_DarkIron", (0, -142, 1022), (820, 28, 36), m["dark_iron"])
    mesh.add_box("Aetherium_Channel_Top", (0, -164, 972), (640, 12, 22), m["aetherium"])
    mesh.add_box("Aetherium_Channel_Left", (-368, -164, 500), (16, 12, 760), m["aetherium"])
    mesh.add_box("Aetherium_Channel_Right", (368, -164, 500), (16, 12, 760), m["aetherium"])
    mesh.add_box("Threshold_SideSlab_Left", (-500, -18, 18), (270, 220, 36), m["stone"])
    mesh.add_box("Threshold_SideSlab_Right", (500, -18, 18), (270, 220, 36), m["stone"])

    mesh.add_box("UCX_SM_AET_PortalArch_A01_00", (-520, 0, 515), (250, 280, 1030), m["stone"])
    mesh.add_box("UCX_SM_AET_PortalArch_A01_01", (520, 0, 515), (250, 280, 1030), m["stone"])
    mesh.add_box("UCX_SM_AET_PortalArch_A01_02", (0, 0, 1110), (1240, 280, 180), m["stone"])
    mesh.add_box("UCX_SM_AET_PortalArch_A01_03", (-520, 0, 36), (300, 340, 72), m["stone"])
    mesh.add_box("UCX_SM_AET_PortalArch_A01_04", (520, 0, 36), (300, 340, 72), m["stone"])
    return mesh


def ground_tile() -> Mesh:
    mesh = Mesh("SM_AET_ModularGroundTile_A01")
    m = create_common_materials(mesh)
    mesh.add_box("Tile_Base", (0, 0, -4), (400, 400, 8), m["earth"])
    slabs = [
        (-95, -95, 140, 120),
        (85, -120, 155, 95),
        (-120, 78, 105, 145),
        (60, 70, 170, 130),
        (150, 145, 80, 90),
    ]
    for i, (x, y, sx, sy) in enumerate(slabs, 1):
        mesh.add_box(f"StoneSlab_{i:02d}", (x, y, 1), (sx, sy, 3), m["stone"])
    mesh.add_box("MossPatch_NorthWest", (-174, 150, 2), (42, 90, 2), m["moss"])
    mesh.add_box("MossPatch_SouthEast", (165, -150, 2), (50, 65, 2), m["moss"])
    mesh.add_box("UCX_SM_AET_ModularGroundTile_A01_00", (0, 0, -3), (400, 400, 6), m["stone"])
    return mesh


def workshop_crate() -> Mesh:
    mesh = Mesh("SM_MKG_WorkshopPropCrate_A01")
    m = create_common_materials(mesh)
    mesh.add_box("Body_Box", (0, 0, 28), (90, 65, 52), m["timber"])
    mesh.add_box("Lid_Lip", (0, 0, 57), (96, 71, 8), m["timber"])
    for x in (-42, 42):
        for y in (-30, 30):
            mesh.add_box(f"Corner_Brass_{x}_{y}", (x, y, 31), (12, 10, 60), m["brass"])
    mesh.add_box("Latch_DarkIron", (0, -35, 37), (28, 8, 20), m["dark_iron"])
    mesh.add_box("Hinge_Back_Left", (-25, 35, 50), (22, 8, 10), m["dark_iron"])
    mesh.add_box("Hinge_Back_Right", (25, 35, 50), (22, 8, 10), m["dark_iron"])
    mesh.add_cylinder("Handle_Left", (-52, 0, 36), 6, 32, m["leather"], "y", 12)
    mesh.add_cylinder("Handle_Right", (52, 0, 36), 6, 32, m["leather"], "y", 12)
    mesh.add_box("AetheriumMark_Top", (0, -8, 63), (18, 18, 3), m["aetherium"])
    mesh.add_box("UCX_SM_MKG_WorkshopPropCrate_A01_00", (0, 0, 30), (96, 72, 60), m["stone"])
    return mesh


ASSETS = {
    "Props/Training/SM_AET_TargetDummy_A01": target_dummy,
    "Props/Portal/SM_AET_PortalArch_A01": portal_arch,
    "Props/Environment/SM_AET_ModularGroundTile_A01": ground_tile,
    "Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01": workshop_crate,
}


def export_with_assimp(obj_path: Path, fbx_path: Path) -> bool:
    fbx_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["assimp", "export", str(obj_path), str(fbx_path)]
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        return False
    return True


def main() -> int:
    failures = []
    for rel, factory in ASSETS.items():
        mesh = factory()
        asset_name = rel.split("/")[-1]
        obj_path = BLENDER_ROOT / rel / f"{asset_name}.obj"
        fbx_path = EXPORT_ROOT / rel / f"{asset_name}.fbx"
        mesh.write(obj_path)
        if export_with_assimp(obj_path, fbx_path):
            print(f"Generated {obj_path.relative_to(ROOT)} and {fbx_path.relative_to(ROOT)}")
        else:
            failures.append(str(obj_path))
            print(f"Generated OBJ but failed FBX export for {obj_path.relative_to(ROOT)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
