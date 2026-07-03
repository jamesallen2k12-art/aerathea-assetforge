#!/usr/bin/env python3
"""Generate SM_Gnome_AetherTek_PowerNexus_FuelCell_01 non-canon proof package.

This is a deterministic proof utility for a small Mekgineer static mesh. It is
not part of the formal production path unless Flamestrike explicitly asks for a
new non-canon proof pass. It does not replace approved concept intake, Blender
source authoring, FBX export, Unreal validation, or final aesthetic approval.
"""

from __future__ import annotations

import hashlib
import json
import math
import struct
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET = "SM_Gnome_AetherTek_PowerNexus_FuelCell_01"
DOC_ROOT = ROOT / "docs" / "assets" / "props" / ASSET
PKG_ROOT = ROOT / "SourceAssets" / "Generated" / "Props" / "Mekgineer" / ASSET
MESH_ROOT = PKG_ROOT / "Meshes"
TEXTURE_ROOT = PKG_ROOT / "Textures"
PREVIEW_ROOT = PKG_ROOT / "Preview"


@dataclass(frozen=True)
class MaterialDef:
    name: str
    color: tuple[float, float, float, float]
    metallic: float = 0.0
    roughness: float = 0.75
    emissive: tuple[float, float, float] = (0.0, 0.0, 0.0)


@dataclass
class ObjPart:
    name: str
    material: str
    verts: list[tuple[float, float, float]] = field(default_factory=list)
    faces: list[tuple[int, ...]] = field(default_factory=list)


class Mesh:
    def __init__(self, name: str):
        self.name = name
        self.materials: dict[str, MaterialDef] = {}
        self.parts: list[ObjPart] = []

    def material(
        self,
        name: str,
        color: tuple[float, float, float, float],
        metallic: float = 0.0,
        roughness: float = 0.75,
        emissive: tuple[float, float, float] = (0.0, 0.0, 0.0),
    ) -> str:
        self.materials[name] = MaterialDef(name, color, metallic, roughness, emissive)
        return name

    def add_part(self, name: str, material: str) -> ObjPart:
        part = ObjPart(name=name, material=material)
        self.parts.append(part)
        return part

    def add_box(
        self,
        name: str,
        center: tuple[float, float, float],
        size: tuple[float, float, float],
        material: str,
    ) -> None:
        cx, cy, cz = center
        sx, sy, sz = size[0] / 2.0, size[1] / 2.0, size[2] / 2.0
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
        part = self.add_part(name, material)
        part.verts.extend(verts)
        part.faces.extend(faces)

    def add_cylinder(
        self,
        name: str,
        center: tuple[float, float, float],
        radius: float,
        depth: float,
        material: str,
        axis: str = "z",
        segments: int = 16,
        scale_y: float = 1.0,
    ) -> None:
        part = self.add_part(name, material)
        half = depth / 2.0
        ring_a: list[int] = []
        ring_b: list[int] = []
        for i in range(segments):
            angle = math.tau * i / segments
            ca = math.cos(angle) * radius
            sa = math.sin(angle) * radius * scale_y
            if axis == "z":
                a = (center[0] + ca, center[1] + sa, center[2] - half)
                b = (center[0] + ca, center[1] + sa, center[2] + half)
            elif axis == "x":
                a = (center[0] - half, center[1] + ca, center[2] + sa)
                b = (center[0] + half, center[1] + ca, center[2] + sa)
            else:
                a = (center[0] + ca, center[1] - half, center[2] + sa)
                b = (center[0] + ca, center[1] + half, center[2] + sa)
            ring_a.append(len(part.verts) + 1)
            part.verts.append(a)
            ring_b.append(len(part.verts) + 1)
            part.verts.append(b)
        for i in range(segments):
            j = (i + 1) % segments
            part.faces.append((ring_a[i], ring_a[j], ring_b[j], ring_b[i]))
        part.faces.append(tuple(reversed(ring_a)))
        part.faces.append(tuple(ring_b))

    def add_diamond(
        self,
        name: str,
        center: tuple[float, float, float],
        size: tuple[float, float, float],
        material: str,
    ) -> None:
        cx, cy, cz = center
        sx, sy, sz = size[0] / 2.0, size[1] / 2.0, size[2] / 2.0
        part = self.add_part(name, material)
        part.verts.extend(
            [
                (cx, cy, cz + sz),
                (cx + sx, cy, cz),
                (cx, cy + sy, cz),
                (cx - sx, cy, cz),
                (cx, cy - sy, cz),
                (cx, cy, cz - sz),
            ]
        )
        part.faces.extend(
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

    def bounds(self) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        verts = [v for part in self.parts for v in part.verts]
        return (
            (min(v[0] for v in verts), min(v[1] for v in verts), min(v[2] for v in verts)),
            (max(v[0] for v in verts), max(v[1] for v in verts), max(v[2] for v in verts)),
        )

    def triangle_count(self) -> int:
        return sum(max(0, len(face) - 2) for part in self.parts for face in part.faces)

    def visual_part_count(self) -> int:
        return len([part for part in self.parts if not part.name.startswith("UCX_")])

    def write_obj(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        mtl_path = path.with_suffix(".mtl")
        with mtl_path.open("w", encoding="utf-8") as mtl:
            mtl.write(f"# Materials for {self.name}\n")
            for mat in self.materials.values():
                r, g, b, _a = mat.color
                mtl.write(f"newmtl {mat.name}\n")
                mtl.write(f"Kd {r:.4f} {g:.4f} {b:.4f}\n")
                mtl.write(f"Ke {mat.emissive[0]:.4f} {mat.emissive[1]:.4f} {mat.emissive[2]:.4f}\n")
                mtl.write("Ks 0.0500 0.0500 0.0500\n")
                mtl.write("Ns 24.0000\n\n")
        with path.open("w", encoding="utf-8") as obj:
            obj.write(f"# {self.name}\n")
            obj.write(f"mtllib {mtl_path.name}\n")
            offset = 0
            for part in self.parts:
                obj.write(f"o {part.name}\n")
                obj.write(f"usemtl {part.material}\n")
                for v in part.verts:
                    obj.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
                for face in part.faces:
                    obj.write("f " + " ".join(str(offset + idx) for idx in face) + "\n")
                offset += len(part.verts)


def add_mekgineer_materials(mesh: Mesh) -> dict[str, str]:
    return {
        "dark": mesh.material("M_GNM_DarkIron_A01", (0.055, 0.060, 0.065, 1.0), 0.75, 0.58),
        "brass": mesh.material("M_GNM_Brass_A01", (0.74, 0.49, 0.19, 1.0), 0.75, 0.42),
        "copper": mesh.material("M_GNM_Copper_A01", (0.68, 0.29, 0.13, 1.0), 0.80, 0.46),
        "leather": mesh.material("M_GNM_DarkLeather_A01", (0.16, 0.085, 0.045, 1.0), 0.0, 0.82),
        "glass": mesh.material(
            "M_GNM_RefractorGlass_A01",
            (0.18, 0.66, 0.95, 0.55),
            0.0,
            0.18,
            (0.03, 0.16, 0.32),
        ),
        "aether": mesh.material(
            "M_GNM_AetheriumCore_Emissive_A01",
            (0.04, 0.40, 1.0, 1.0),
            0.0,
            0.25,
            (0.0, 0.52, 1.45),
        ),
        "paint": mesh.material(
            "M_GNM_AetheriumRunePaint_A01",
            (0.02, 0.22, 0.58, 1.0),
            0.0,
            0.65,
            (0.0, 0.18, 0.55),
        ),
    }


def add_socket(mesh: Mesh, mats: dict[str, str], name: str, x: float, y: float, z: float, segments: int) -> None:
    mesh.add_cylinder(f"{name}_DarkIronSocketCup", (x, y, z), 5.8, 3.2, mats["dark"], "y", segments)
    mesh.add_cylinder(f"{name}_BrassContactRing", (x, y - 2.3, z), 4.2, 2.4, mats["brass"], "y", segments)
    mesh.add_cylinder(f"{name}_AetheriumPin", (x, y - 4.0, z), 2.0, 1.8, mats["aether"], "y", max(6, segments // 2))


def build_lod(lod: int) -> Mesh:
    mesh = Mesh(f"{ASSET}_LOD{lod}")
    m = add_mekgineer_materials(mesh)

    if lod == 0:
        seg = 16
        mesh.add_box("Housing_DarkIron_CartridgeBody", (0, 0, 38), (38, 22, 68), m["dark"])
        mesh.add_box("RearMount_DarkIron_SocketBackplate", (0, 13.5, 38), (46, 5, 74), m["dark"])
        mesh.add_box("FrontInset_DarkIron_RecessPlate", (0, -13.2, 38), (34, 3, 58), m["dark"])
        mesh.add_box("TopLock_Brass_Collar", (0, -1, 75), (45, 26, 7), m["brass"])
        mesh.add_box("BottomLock_Brass_Collar", (0, -1, 1), (45, 26, 7), m["brass"])
        mesh.add_box("TopCopper_RoutingBridge", (0, -13.8, 68), (34, 4, 5), m["copper"])
        mesh.add_box("BottomCopper_RoutingBridge", (0, -13.8, 8), (30, 4, 5), m["copper"])
        mesh.add_diamond("Core_Aetherium_TallFacetedCell", (0, -16.7, 38), (15, 6, 42), m["aether"])
        mesh.add_cylinder("Front_RefractorShield_Lens", (0, -18.2, 40), 14.8, 3.5, m["glass"], "y", seg, 1.22)
        mesh.add_box("LensGuard_Brass_LeftRail", (-18.5, -18.8, 40), (4, 4, 42), m["brass"])
        mesh.add_box("LensGuard_Brass_RightRail", (18.5, -18.8, 40), (4, 4, 42), m["brass"])
        mesh.add_box("LensGuard_Brass_TopRail", (0, -18.8, 61.8), (36, 4, 4), m["brass"])
        mesh.add_box("LensGuard_Brass_BottomRail", (0, -18.8, 18.2), (36, 4, 4), m["brass"])
        mesh.add_box("LensGuard_Brass_CenterSpine", (0, -19.2, 40), (3, 4, 39), m["brass"])
        mesh.add_box("LensGuard_Brass_CrossBrace_A", (0, -19.5, 50), (32, 3, 3), m["brass"])
        mesh.add_box("LensGuard_Brass_CrossBrace_B", (0, -19.5, 30), (32, 3, 3), m["brass"])
        for x in (-25, 25):
            mesh.add_cylinder(f"SideCapacitor_{x}_CopperTube", (x, 0, 38), 5.2, 53, m["copper"], "z", seg)
            mesh.add_box(f"SideCapacitor_{x}_DarkIronTopClamp", (x, 0, 66), (12, 22, 5), m["dark"])
            mesh.add_box(f"SideCapacitor_{x}_DarkIronBottomClamp", (x, 0, 10), (12, 22, 5), m["dark"])
            mesh.add_cylinder(f"SideRail_{x}_BrassRoundSpine", (x * 0.86, -12.5, 38), 2.4, 68, m["brass"], "z", 10)
        add_socket(mesh, m, "HardpointSocket_LeftPowerRoute", -15, -20.5, 65, seg)
        add_socket(mesh, m, "HardpointSocket_RightPowerRoute", 15, -20.5, 65, seg)
        add_socket(mesh, m, "HardpointSocket_LowerReturnRoute", 0, -20.5, 14, seg)
        for x in (-15, 15):
            mesh.add_box(f"AetheriumTrace_{x}_VerticalGlow", (x, -21.8, 41), (2.4, 1.2, 39), m["paint"])
            mesh.add_box(f"CopperTrace_{x}_InnerRail", (x * 0.55, -20.9, 53), (3, 2.2, 19), m["copper"])
        mesh.add_box("AetheriumTrace_LowerForkGlow", (0, -21.8, 24), (18, 1.2, 2.4), m["paint"])
        for x in (-18, 18):
            mesh.add_box(f"RearLeather_Strap_{x}", (x, 16.7, 39), (6, 4, 64), m["leather"])
            mesh.add_box(f"RearMount_Brass_Lug_{x}_Upper", (x, 19.5, 60), (10, 5, 8), m["brass"])
            mesh.add_box(f"RearMount_Brass_Lug_{x}_Lower", (x, 19.5, 17), (10, 5, 8), m["brass"])
        for x in (-18, 18):
            for z in (8, 24, 52, 68):
                mesh.add_cylinder(f"CornerRivet_{x}_{z}_BrassHead", (x, -20.8, z), 1.8, 1.2, m["brass"], "y", 8)
        for x in (-29, 29):
            for z in (16, 38, 60):
                mesh.add_box(f"PanelChip_{x}_{z}_CopperPatch", (x * 0.62, -14.9, z), (4, 1.5, 7), m["copper"])
        mesh.add_box("SocketMarker_PowerRoute_A", (-15, -24.4, 65), (1.6, 1.6, 1.6), m["aether"])
        mesh.add_box("SocketMarker_PowerRoute_B", (15, -24.4, 65), (1.6, 1.6, 1.6), m["aether"])
        mesh.add_box("SocketMarker_PowerRoute_C", (0, -24.4, 14), (1.6, 1.6, 1.6), m["aether"])
    elif lod == 1:
        seg = 12
        mesh.add_box("Housing_DarkIron_CartridgeBody", (0, 0, 38), (38, 22, 68), m["dark"])
        mesh.add_box("RearMount_DarkIron_SocketBackplate", (0, 13.5, 38), (46, 5, 74), m["dark"])
        mesh.add_box("TopBottom_Brass_Collars", (0, -1, 38), (44, 25, 79), m["brass"])
        mesh.add_diamond("Core_Aetherium_FacetedCell", (0, -16.5, 38), (14, 5, 40), m["aether"])
        mesh.add_cylinder("Front_RefractorShield_Lens", (0, -18.0, 40), 14, 3, m["glass"], "y", seg, 1.18)
        mesh.add_box("LensGuard_Brass_FrameVertical", (0, -19, 40), (38, 3, 42), m["brass"])
        for x in (-25, 25):
            mesh.add_cylinder(f"SideCapacitor_{x}_CopperTube", (x, 0, 38), 5, 53, m["copper"], "z", seg)
            mesh.add_box(f"SideClamp_{x}", (x, 0, 38), (12, 22, 63), m["dark"])
        add_socket(mesh, m, "HardpointSocket_LeftPowerRoute", -15, -20.2, 65, seg)
        add_socket(mesh, m, "HardpointSocket_RightPowerRoute", 15, -20.2, 65, seg)
        add_socket(mesh, m, "HardpointSocket_LowerReturnRoute", 0, -20.2, 14, seg)
        for x in (-18, 18):
            mesh.add_box(f"RearLeather_Strap_{x}", (x, 16.7, 39), (6, 4, 64), m["leather"])
        mesh.add_box("AetheriumTrace_FrontGlow", (0, -21.5, 42), (30, 1.2, 48), m["paint"])
    elif lod == 2:
        seg = 8
        mesh.add_box("Housing_DarkIron_SimplifiedBody", (0, 0, 38), (42, 25, 76), m["dark"])
        mesh.add_box("Brass_Collar_Block", (0, -1, 38), (45, 27, 79), m["brass"])
        mesh.add_diamond("Core_Aetherium_SimpleCell", (0, -16.5, 38), (13, 5, 38), m["aether"])
        mesh.add_cylinder("Front_RefractorShield_SimpleLens", (0, -18, 40), 14, 3, m["glass"], "y", seg, 1.15)
        for x in (-25, 25):
            mesh.add_cylinder(f"SideCapacitor_{x}_LowTube", (x, 0, 38), 5.5, 55, m["copper"], "z", seg)
        add_socket(mesh, m, "HardpointSocket_LeftPowerRoute", -15, -20, 65, seg)
        add_socket(mesh, m, "HardpointSocket_RightPowerRoute", 15, -20, 65, seg)
        add_socket(mesh, m, "HardpointSocket_LowerReturnRoute", 0, -20, 14, seg)
    else:
        seg = 6
        mesh.add_box("Silhouette_DarkIron_Block", (0, 0, 38), (46, 27, 78), m["dark"])
        mesh.add_box("Silhouette_Brass_FrontPlate", (0, -14, 38), (38, 3, 60), m["brass"])
        mesh.add_diamond("Silhouette_Aetherium_CoreInset", (0, -17, 38), (13, 4, 38), m["aether"])
        mesh.add_cylinder("Silhouette_Refractor_LowLens", (0, -19, 40), 13, 2, m["glass"], "y", seg, 1.1)
        for x, z in [(-15, 65), (15, 65), (0, 14)]:
            mesh.add_cylinder(f"Silhouette_Socket_{x}_{z}", (x, -20, z), 4.5, 2, m["brass"], "y", seg)
    return mesh


def build_collision() -> Mesh:
    mesh = Mesh(f"UCX_{ASSET}")
    m = add_mekgineer_materials(mesh)
    part = mesh.add_part(f"UCX_{ASSET}_00", m["dark"])
    center = (0.0, 0.0, 38.0)
    rx, ry, h = 30.0, 20.0, 80.0
    bottom: list[int] = []
    top: list[int] = []
    for i in range(9):
        angle = math.tau * i / 9.0 + math.radians(10)
        x = center[0] + math.cos(angle) * rx
        y = center[1] + math.sin(angle) * ry
        bottom.append(len(part.verts) + 1)
        part.verts.append((x, y, center[2] - h / 2.0))
        top.append(len(part.verts) + 1)
        part.verts.append((x, y, center[2] + h / 2.0))
    for i in range(9):
        j = (i + 1) % 9
        part.faces.append((bottom[i], bottom[j], top[j], top[i]))
    part.faces.append(tuple(reversed(bottom)))
    part.faces.append(tuple(top))
    return mesh


def triangulate(face: tuple[int, ...]) -> list[tuple[int, int, int]]:
    return [(face[0], face[i], face[i + 1]) for i in range(1, len(face) - 1)]


def vec_sub(a: tuple[float, float, float], b: tuple[float, float, float]) -> tuple[float, float, float]:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def cross(a: tuple[float, float, float], b: tuple[float, float, float]) -> tuple[float, float, float]:
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def normalize(v: tuple[float, float, float]) -> tuple[float, float, float]:
    length = math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
    if length <= 0.00001:
        return (0.0, 0.0, 1.0)
    return (v[0] / length, v[1] / length, v[2] / length)


def write_glb(mesh: Mesh, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    material_names = list(mesh.materials)
    material_index = {name: idx for idx, name in enumerate(material_names)}
    gltf: dict[str, object] = {
        "asset": {"version": "2.0", "generator": "Aerathea deterministic DCC candidate generator"},
        "scene": 0,
        "scenes": [{"nodes": []}],
        "nodes": [],
        "meshes": [],
        "materials": [],
        "buffers": [{"byteLength": 0}],
        "bufferViews": [],
        "accessors": [],
    }
    for mat in mesh.materials.values():
        material: dict[str, object] = {
            "name": mat.name,
            "pbrMetallicRoughness": {
                "baseColorFactor": list(mat.color),
                "metallicFactor": mat.metallic,
                "roughnessFactor": mat.roughness,
            },
            "emissiveFactor": list(mat.emissive),
        }
        if mat.color[3] < 0.99:
            material["alphaMode"] = "BLEND"
            material["doubleSided"] = True
        gltf["materials"].append(material)

    blob = bytearray()

    def align() -> None:
        while len(blob) % 4:
            blob.append(0)

    def add_view(data: bytes, target: int) -> int:
        align()
        offset = len(blob)
        blob.extend(data)
        view = {"buffer": 0, "byteOffset": offset, "byteLength": len(data), "target": target}
        gltf["bufferViews"].append(view)
        return len(gltf["bufferViews"]) - 1

    for part in mesh.parts:
        positions: list[tuple[float, float, float]] = []
        normals: list[tuple[float, float, float]] = []
        indices: list[int] = []
        for face in part.faces:
            for tri in triangulate(face):
                v0 = part.verts[tri[0] - 1]
                v1 = part.verts[tri[1] - 1]
                v2 = part.verts[tri[2] - 1]
                normal = normalize(cross(vec_sub(v1, v0), vec_sub(v2, v0)))
                base = len(positions)
                positions.extend([v0, v1, v2])
                normals.extend([normal, normal, normal])
                indices.extend([base, base + 1, base + 2])

        pos_bytes = b"".join(struct.pack("<3f", *v) for v in positions)
        nrm_bytes = b"".join(struct.pack("<3f", *v) for v in normals)
        idx_bytes = b"".join(struct.pack("<I", i) for i in indices)

        pos_view = add_view(pos_bytes, 34962)
        nrm_view = add_view(nrm_bytes, 34962)
        idx_view = add_view(idx_bytes, 34963)
        mins = [min(v[i] for v in positions) for i in range(3)]
        maxs = [max(v[i] for v in positions) for i in range(3)]
        pos_acc = {
            "bufferView": pos_view,
            "componentType": 5126,
            "count": len(positions),
            "type": "VEC3",
            "min": mins,
            "max": maxs,
        }
        nrm_acc = {"bufferView": nrm_view, "componentType": 5126, "count": len(normals), "type": "VEC3"}
        idx_acc = {"bufferView": idx_view, "componentType": 5125, "count": len(indices), "type": "SCALAR"}
        gltf["accessors"].extend([pos_acc, nrm_acc, idx_acc])
        pos_i = len(gltf["accessors"]) - 3
        nrm_i = len(gltf["accessors"]) - 2
        idx_i = len(gltf["accessors"]) - 1
        gltf["meshes"].append(
            {
                "name": part.name,
                "primitives": [
                    {
                        "attributes": {"POSITION": pos_i, "NORMAL": nrm_i},
                        "indices": idx_i,
                        "material": material_index[part.material],
                    }
                ],
            }
        )
        gltf["nodes"].append({"name": part.name, "mesh": len(gltf["meshes"]) - 1})
        gltf["scenes"][0]["nodes"].append(len(gltf["nodes"]) - 1)

    gltf["buffers"][0]["byteLength"] = len(blob)
    json_bytes = json.dumps(gltf, separators=(",", ":")).encode("utf-8")
    while len(json_bytes) % 4:
        json_bytes += b" "
    while len(blob) % 4:
        blob.append(0)

    total_len = 12 + 8 + len(json_bytes) + 8 + len(blob)
    with path.open("wb") as fh:
        fh.write(struct.pack("<4sII", b"glTF", 2, total_len))
        fh.write(struct.pack("<I4s", len(json_bytes), b"JSON"))
        fh.write(json_bytes)
        fh.write(struct.pack("<I4s", len(blob), b"BIN\0"))
        fh.write(blob)


def material_color(mesh: Mesh, material: str) -> tuple[int, int, int]:
    c = mesh.materials[material].color
    return (int(c[0] * 255), int(c[1] * 255), int(c[2] * 255))


def project(v: tuple[float, float, float], view: str) -> tuple[float, float, float]:
    x, y, z = v
    if view == "front":
        return (x, z, -y)
    if view == "side":
        return (y, z, x)
    if view == "top":
        return (x, -y, z)
    # three-quarter isometric front.
    u = (x - y) * 0.82
    vv = z + (x + y) * 0.24
    depth = (0.45 * x) - (0.95 * y) - (0.08 * z)
    return (u, vv, depth)


def draw_mesh_view(
    draw: ImageDraw.ImageDraw,
    mesh: Mesh,
    box: tuple[int, int, int, int],
    view: str,
    label: str,
    font: ImageFont.ImageFont,
) -> None:
    x0, y0, x1, y1 = box
    projected: list[tuple[float, list[tuple[float, float]], str]] = []
    all_points: list[tuple[float, float]] = []
    for part in mesh.parts:
        if part.name.startswith("SocketMarker"):
            continue
        for face in part.faces:
            pts3 = [part.verts[i - 1] for i in face]
            pts = [project(v, view) for v in pts3]
            avg_depth = sum(p[2] for p in pts) / len(pts)
            pts2 = [(p[0], p[1]) for p in pts]
            all_points.extend(pts2)
            projected.append((avg_depth, pts2, part.material))
    if not all_points:
        return
    minx, maxx = min(p[0] for p in all_points), max(p[0] for p in all_points)
    miny, maxy = min(p[1] for p in all_points), max(p[1] for p in all_points)
    scale = min((x1 - x0 - 42) / max(1, maxx - minx), (y1 - y0 - 52) / max(1, maxy - miny))
    ox = x0 + (x1 - x0) / 2.0 - (minx + maxx) * scale / 2.0
    oy = y0 + (y1 - y0) / 2.0 + (miny + maxy) * scale / 2.0 + 10
    draw.rectangle(box, outline=(82, 76, 65), width=2)
    for _depth, pts2, mat in sorted(projected, key=lambda row: row[0]):
        screen = [(ox + px * scale, oy - py * scale) for px, py in pts2]
        base = material_color(mesh, mat)
        fill = tuple(min(255, int(ch * 0.92 + 16)) for ch in base)
        draw.polygon(screen, fill=fill, outline=(22, 24, 26))
    draw.text((x0 + 12, y0 + 10), label, fill=(235, 229, 214), font=font)


def create_preview(meshes: dict[str, Mesh], collision: Mesh, stats: dict[str, object]) -> Path:
    PREVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", (1800, 1250), (31, 32, 34))
    draw = ImageDraw.Draw(image)
    try:
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 34)
        font = ImageFont.truetype("DejaVuSans.ttf", 23)
        small = ImageFont.truetype("DejaVuSans.ttf", 18)
    except OSError:
        title_font = font = small = ImageFont.load_default()

    draw.text((44, 32), ASSET, fill=(242, 228, 184), font=title_font)
    draw.text((46, 78), "DCC game-ready candidate: gnome/Mekgineer Light Mek Power Nexus fuel cell", fill=(171, 209, 230), font=font)
    lod0 = meshes["LOD0"]
    draw_mesh_view(draw, lod0, (42, 130, 510, 590), "front", "LOD0 Front", font)
    draw_mesh_view(draw, lod0, (534, 130, 1002, 590), "side", "LOD0 Side", font)
    draw_mesh_view(draw, lod0, (1026, 130, 1494, 590), "top", "LOD0 Top", font)
    draw_mesh_view(draw, lod0, (42, 620, 760, 1168), "iso", "LOD0 Three-Quarter", font)
    draw_mesh_view(draw, meshes["LOD1"], (784, 620, 1112, 906), "iso", "LOD1", font)
    draw_mesh_view(draw, meshes["LOD2"], (1130, 620, 1458, 906), "iso", "LOD2", font)
    draw_mesh_view(draw, meshes["LOD3"], (1476, 620, 1760, 906), "iso", "LOD3", font)
    draw_mesh_view(draw, collision, (784, 930, 1112, 1168), "iso", "UCX Collision", font)

    y = 930
    x = 1146
    draw.text((x, y), "Technical Proof Stats", fill=(242, 228, 184), font=font)
    y += 38
    for key in ["LOD0", "LOD1", "LOD2", "LOD3", "Collision"]:
        row = stats[key]
        draw.text(
            (x, y),
            f"{key}: {row['triangles']} tris, {row['parts']} named parts",
            fill=(223, 220, 208),
            font=small,
        )
        y += 30
    y += 16
    for text in [
        "Scale: 81 cm tall x 62 cm wide x 47 cm deep",
        "Pivot target: rear-bottom center for Mek chest socketing",
        "Sockets: PowerRoute_A, PowerRoute_B, PowerRoute_C",
        "Materials: dark iron, brass, copper, leather, refractor glass, Aetherium",
        "Status: ready for Unreal import testing, not approved library asset",
    ]:
        draw.text((x, y), text, fill=(171, 209, 230), font=small)
        y += 28

    path = PREVIEW_ROOT / f"{ASSET}_PreviewSheet.png"
    image.save(path)
    return path


def create_texture_guides() -> list[Path]:
    TEXTURE_ROOT.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    colors = [
        ((18, 19, 20), "dark iron"),
        ((189, 125, 48), "brass"),
        ((173, 74, 33), "copper"),
        ((40, 22, 12), "leather"),
        ((48, 168, 242), "refractor"),
        ((10, 102, 255), "aetherium"),
    ]
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
    bc = Image.new("RGB", (1024, 1024), (28, 28, 30))
    draw = ImageDraw.Draw(bc)
    for i, (color, name) in enumerate(colors):
        y0 = i * 160 + 30
        draw.rectangle((40, y0, 984, y0 + 120), fill=color)
        draw.text((64, y0 + 42), name, fill=(235, 231, 219), font=font)
    p = TEXTURE_ROOT / f"T_{ASSET}_BC_Guide.png"
    bc.save(p)
    paths.append(p)

    normal = Image.new("RGB", (1024, 1024), (128, 128, 255))
    p = TEXTURE_ROOT / f"T_{ASSET}_N_Guide.png"
    normal.save(p)
    paths.append(p)

    orm = Image.new("RGB", (1024, 1024), (180, 185, 32))
    draw = ImageDraw.Draw(orm)
    draw.text((48, 48), "Guide ORM: R=AO, G=Roughness, B=Metallic", fill=(0, 0, 0), font=font)
    p = TEXTURE_ROOT / f"T_{ASSET}_ORM_Guide.png"
    orm.save(p)
    paths.append(p)

    emissive = Image.new("RGB", (1024, 1024), (0, 0, 0))
    draw = ImageDraw.Draw(emissive)
    draw.rectangle((380, 80, 644, 820), fill=(0, 120, 255))
    draw.ellipse((315, 168, 709, 562), outline=(0, 85, 220), width=35)
    draw.ellipse((230, 725, 794, 970), fill=(0, 35, 100))
    p = TEXTURE_ROOT / f"T_{ASSET}_E_Guide.png"
    emissive.save(p)
    paths.append(p)
    return paths


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def write_manifest(paths: list[Path], stats: dict[str, object], preview: Path) -> Path:
    manifest = {
        "asset": ASSET,
        "status": "DCC game-ready candidate; Unreal import and Flamestrike final approval pending",
        "unit_scale": "centimeters",
        "pivot_target": "rear-bottom center",
        "dimensions_cm": {"width": 62, "depth": 47, "height": 81},
        "sockets": {
            "Socket_PowerRoute_A": {"location_cm": [-15, -24.4, 65], "purpose": "upper-left chest routing"},
            "Socket_PowerRoute_B": {"location_cm": [15, -24.4, 65], "purpose": "upper-right chest routing"},
            "Socket_PowerRoute_C": {"location_cm": [0, -24.4, 14], "purpose": "lower return route"},
        },
        "stats": stats,
        "preview": str(preview.relative_to(ROOT)),
        "files": [
            {
                "path": str(p.relative_to(ROOT)),
                "sha256_16": file_hash(p),
                "bytes": p.stat().st_size,
            }
            for p in sorted(paths)
        ],
    }
    path = PKG_ROOT / "ASSET_MANIFEST.json"
    path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return path


def write_codex_files(stats: dict[str, object]) -> list[Path]:
    DOC_ROOT.mkdir(parents=True, exist_ok=True)
    process = DOC_ROOT / "CODEX_2D_IMAGE_TO_ACCURATE_3D_GAME_READY_ASSET.md"
    process.write_text(
        f"""# Codex 2D Concept To 3D Game Asset Checklist

Asset: `{ASSET}`

Use the Aerathea concept-to-game-ready pipeline:

1. Confirm visual canon or keep the asset as a candidate.
2. Record reference intake, lore, gameplay role, scale, and target engine.
3. Break down silhouette, primary forms, material zones, glow zones, sockets, and missing views.
4. Document front, side, back, and top interpretation.
5. Define technical targets: triangles, textures, materials, pivot, sockets, collision, and LODs.
6. Build blockout first, then production mesh.
7. Keep large silhouette forms in geometry; move micro detail to textures or normal maps.
8. Create UVs, BaseColor, Normal, ORM, and Emissive maps.
9. Create LOD0, LOD1, LOD2, and LOD3.
10. Create simple UCX collision.
11. Import into Unreal, assign materials, validate scale/collision/LOD/materials.
12. Stop for Flamestrike approval before marking it an approved library asset.

Current generated proof stats:

| LOD | Triangles | Named Parts |
| --- | ---: | ---: |
| LOD0 | {stats['LOD0']['triangles']} | {stats['LOD0']['parts']} |
| LOD1 | {stats['LOD1']['triangles']} | {stats['LOD1']['parts']} |
| LOD2 | {stats['LOD2']['triangles']} | {stats['LOD2']['parts']} |
| LOD3 | {stats['LOD3']['triangles']} | {stats['LOD3']['parts']} |
| Collision | {stats['Collision']['triangles']} | {stats['Collision']['parts']} |
""",
        encoding="utf-8",
    )
    runner = DOC_ROOT / "RUN_THIS_IN_CODEX.md"
    runner.write_text(
        f"""# Run This In Codex

Generate the DCC candidate package:

```bash
python3 Tools/DCC/generate_gnome_power_nexus_fuel_cell.py
```

Then review:

- `SourceAssets/Generated/Props/Mekgineer/{ASSET}/Preview/{ASSET}_PreviewSheet.png`
- `SourceAssets/Generated/Props/Mekgineer/{ASSET}/ASSET_MANIFEST.json`
- `docs/assets/props/{ASSET}/BUILD_IMPORT_STATUS.md`

Do not mark the asset fully game-ready until Unreal import testing and Flamestrike approval are complete.
""",
        encoding="utf-8",
    )
    return [process, runner]


def write_status_docs(stats: dict[str, object], manifest_path: Path, preview: Path) -> list[Path]:
    DOC_ROOT.mkdir(parents=True, exist_ok=True)
    production = DOC_ROOT / "PRODUCTION_PACKAGE.md"
    production.write_text(
        f"""# {ASSET} Production Package

## Art Direction Summary

- Asset name: `{ASSET}`
- Asset type: Static Mesh / Mek chest power fuel cell
- Faction: Gnome / Mekgineer
- Status: DCC game-ready candidate; Unreal import and visual approval pending

A compact AetherTek Generator fuel cell that slots into a gnome Light Mek chest Power Nexus. It uses dark iron cartridge massing, brass and copper routing hardware, protected blue Aetherium core glow, a front refractor shield lens, and three power-routing hardpoint sockets.

## Gameplay Purpose

Chest-mounted Light Mek power module, workshop display prop, loot/quest object, socket test mesh, and future VFX attachment source for Aetherium power-routing effects.

## Silhouette Notes

Use a compact vertical cartridge silhouette with side capacitors, front protected lens, triangular socket arrangement, and readable brass cage framing. The object should read as engineered Mekgineer hardware, not a loose magic crystal.

## Scale Notes

- Approximate generated dimensions: 62 cm wide, 47 cm deep, 81 cm tall.
- Pivot target: rear-bottom center for Mek chest socketing.
- Scale fit must be validated against the approved Light Mek chest Power Nexus.

## Materials And Color Palette

Dark iron structural body, worn brass collars and lens cage, copper routing traces and capacitors, dark leather rear straps, blue Aetherium core, and restrained cyan refractor glass.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `{ASSET}` for the world of Aerathea. The design should emphasize a compact gnome Mekgineer AetherTek fuel-cell cartridge silhouette, brass and copper power routing, dark iron protective housing, a front refractor shield lens, three hardpoint power-routing sockets, blue Aetherium core glow, practical Light Mek chest integration, and production-friendly MMO readability. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and mid-poly Unreal asset design. Present it as a front, side, back, top, and three-quarter production sheet on a clean background. Avoid copied franchise designs, excessive micro-detail, uncontrolled glow, and unreadable all-dark forms.

## Modeling Notes

Model the cartridge body, brass collars, front lens cage, side capacitors, socket cups, rear lugs, and main Aetherium core as real geometry. Texture tiny screws, scratches, grime, gauge marks, micro runes, and leather stitching.

## Texture And Material Notes

Generated guide textures:

- `T_{ASSET}_BC_Guide.png`
- `T_{ASSET}_N_Guide.png`
- `T_{ASSET}_ORM_Guide.png`
- `T_{ASSET}_E_Guide.png`

Final production should replace guide textures with authored hand-painted BaseColor, Normal, packed ORM, and restrained Emissive maps.

## Triangle Budget

Generated proof:

| LOD | Triangles | Named Parts |
| --- | ---: | ---: |
| LOD0 | {stats['LOD0']['triangles']} | {stats['LOD0']['parts']} |
| LOD1 | {stats['LOD1']['triangles']} | {stats['LOD1']['parts']} |
| LOD2 | {stats['LOD2']['triangles']} | {stats['LOD2']['parts']} |
| LOD3 | {stats['LOD3']['triangles']} | {stats['LOD3']['parts']} |

Target remains small-prop safe.

## LOD Plan

- LOD0: full cartridge, lens cage, side capacitors, sockets, core, rear mount lugs.
- LOD1: simplified clamps, merged rails, reduced cylinders.
- LOD2: simplified body, core, lens, capacitors, and socket silhouettes.
- LOD3: boxed silhouette with core/lens inset and socket reads.

## Collision Notes

Generated simple convex UCX proxy: `{stats['Collision']['triangles']}` tris, one named UCX part. Use simple collision for world placement and disable collision when attached inside a Light Mek chest socket unless gameplay requires interaction.

## Animation Notes

Static mesh baseline. Future material instance may pulse the core. Future Blueprint may expose active, depleted, overloaded, and damaged emissive states.

## Unreal Import Notes

- Suggested folder: `/Game/Aerathea/Props/Mekgineer/Power/`
- Mesh: `{ASSET}`
- Material instance: `MI_Gnome_AetherTek_PowerNexus_FuelCell_01`
- Pivot: rear-bottom center
- Collision: import UCX proxy
- Sockets: `Socket_PowerRoute_A`, `Socket_PowerRoute_B`, `Socket_PowerRoute_C`
- Validate scale against the Light Mek chest Power Nexus before approval.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/{ASSET}/`
- Generated source: `SourceAssets/Generated/Props/Mekgineer/{ASSET}/`
- Unreal target: `/Game/Aerathea/Props/Mekgineer/Power/`

## Quality Gate Checklist

- Gnome/Mekgineer identity is clear.
- Fuel-cell cartridge role is readable.
- Front refractor shield lens is visible.
- Three routing sockets are present.
- Glow is restrained and purposeful.
- LOD0-LOD3 exist.
- Collision proxy exists.
- Guide textures and manifest exist.
- Unreal import validation remains pending.
- Flamestrike final visual approval remains pending.
""",
        encoding="utf-8",
    )
    status = DOC_ROOT / "BUILD_IMPORT_STATUS.md"
    status.write_text(
        f"""# {ASSET} Build Import Status

## Status

`DCC game-ready candidate`

This package has generated mesh exports, LODs, collision, guide textures, preview sheet, source script, and manifest. It is ready for Unreal import testing. It is not yet a fully game-ready or approved library asset.

## Generated Review Files

- Preview sheet: `{preview.relative_to(ROOT)}`
- Manifest: `{manifest_path.relative_to(ROOT)}`
- Mesh root: `{MESH_ROOT.relative_to(ROOT)}`
- Texture root: `{TEXTURE_ROOT.relative_to(ROOT)}`

## Technical Stats

| LOD | Triangles | Named Parts | Purpose |
| --- | ---: | ---: | --- |
| LOD0 | {stats['LOD0']['triangles']} | {stats['LOD0']['parts']} | close / inspected mesh |
| LOD1 | {stats['LOD1']['triangles']} | {stats['LOD1']['parts']} | medium distance |
| LOD2 | {stats['LOD2']['triangles']} | {stats['LOD2']['parts']} | far distance |
| LOD3 | {stats['LOD3']['triangles']} | {stats['LOD3']['parts']} | very far silhouette |
| Collision | {stats['Collision']['triangles']} | {stats['Collision']['parts']} | simple convex UCX proxy |

## Blocking Items Before Full Game-Ready

- Import into Unreal.
- Assign material instances and guide textures.
- Configure LODs and collision.
- Add sockets or Blueprint socket metadata.
- Place in approved review or gameplay map.
- Validate scale against the Light Mek chest Power Nexus.
- Capture Unreal review image.
- Record Flamestrike aesthetic approval.
""",
        encoding="utf-8",
    )
    return [production, status]


def main() -> int:
    paths: list[Path] = []
    meshes = {f"LOD{i}": build_lod(i) for i in range(4)}
    collision = build_collision()
    stats: dict[str, object] = {}
    for key, mesh in meshes.items():
        glb = MESH_ROOT / f"{ASSET}_{key}.glb"
        obj = MESH_ROOT / f"{ASSET}_{key}.obj"
        write_glb(mesh, glb)
        mesh.write_obj(obj)
        paths.extend([glb, obj, obj.with_suffix(".mtl")])
        stats[key] = {"triangles": mesh.triangle_count(), "parts": mesh.visual_part_count()}
    col_glb = MESH_ROOT / f"UCX_{ASSET}_00.glb"
    col_obj = MESH_ROOT / f"UCX_{ASSET}_00.obj"
    write_glb(collision, col_glb)
    collision.write_obj(col_obj)
    paths.extend([col_glb, col_obj, col_obj.with_suffix(".mtl")])
    stats["Collision"] = {"triangles": collision.triangle_count(), "parts": len(collision.parts)}
    paths.extend(create_texture_guides())
    preview = create_preview(meshes, collision, stats)
    paths.append(preview)
    paths.extend(write_codex_files(stats))
    manifest = write_manifest(paths, stats, preview)
    paths.append(manifest)
    paths.extend(write_status_docs(stats, manifest, preview))
    print(json.dumps({"asset": ASSET, "status": "generated", "stats": stats, "preview": str(preview)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
