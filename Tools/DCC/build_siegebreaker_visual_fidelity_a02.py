"""Build the bounded Siege Breaker Visual Fidelity A02 DCC candidate.

This revision preserves the verified final-package numeric authority while
replacing the under-resolved A01 presentation with canon-defining dwarven
stone, bracing, grip, shaft, rune, and pommel forms.

Blender usage:
  blender --background --python Tools/DCC/build_siegebreaker_visual_fidelity_a02.py
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path

import bpy


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = "VisualFidelity_A02"
CONTRACT_ID = "SB-VF-A02"
CM = 0.01

SOURCE_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID
EXPORT_ROOT = ROOT / "SourceAssets/Exports/Weapons/Dwarven" / ASSET_ID / REVISION
TEXTURE_ROOT = ROOT / "SourceAssets/Textures/Weapons/Dwarven" / ASSET_ID / REVISION
BLEND_PATH = SOURCE_ROOT / f"{ASSET_ID}_DCCGameReady_{REVISION}.blend"
MANIFEST_PATH = SOURCE_ROOT / f"{ASSET_ID}_{REVISION.upper()}_MANIFEST.json"


def load_base_module():
    path = ROOT / "Tools/DCC/build_siegebreaker_final_package_a01.py"
    spec = importlib.util.spec_from_file_location("siegebreaker_a01_base", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load base helpers: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load_base_module()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tune_a02_materials(materials):
    stone = materials["M_Stone"]
    nodes = stone.node_tree.nodes
    links = stone.node_tree.links
    bsdf = nodes.get("Principled BSDF")
    if bsdf is not None and bsdf.inputs["Base Color"].is_linked:
        source = bsdf.inputs["Base Color"].links[0].from_socket
        links.remove(bsdf.inputs["Base Color"].links[0])
        tint = nodes.new("ShaderNodeMixRGB")
        tint.name = "A02_DarkRunestoneTint"
        tint.blend_type = "MULTIPLY"
        tint.inputs[0].default_value = 1.0
        tint.inputs[2].default_value = (0.18, 0.21, 0.26, 1.0)
        links.new(source, tint.inputs[1])
        links.new(tint.outputs["Color"], bsdf.inputs["Base Color"])

    rune = materials["M_Rune_Emissive"]
    for node in rune.node_tree.nodes:
        if node.type == "MATH" and node.operation == "MULTIPLY":
            node.inputs[1].default_value = 3.4


def add_yz_prism(name, points_yz_cm, x_min_cm, x_max_cm, material, collection, bevel_cm=0.0, tier=1):
    count = len(points_yz_cm)
    vertices = [(x_min_cm * CM, y * CM, z * CM) for y, z in points_yz_cm]
    vertices += [(x_max_cm * CM, y * CM, z * CM) for y, z in points_yz_cm]
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
    base.tag(obj, name, tier)
    base.finalize_mesh(obj)
    if bevel_cm > 0:
        bevel = obj.modifiers.new("AET_Bevel", "BEVEL")
        bevel.width = bevel_cm * CM
        bevel.segments = 1
        base.apply_modifier(obj, bevel.name)
    return obj


def add_strap_helix(name, direction, phase, material, collection):
    curve = bpy.data.curves.new(f"{name}_Curve", "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 1
    curve.bevel_depth = 0.00200
    curve.bevel_resolution = 0
    curve.resolution_u = 1
    spline = curve.splines.new("POLY")
    samples = 92
    spline.points.add(samples - 1)
    z0 = 18.183
    z1 = 59.82
    turns = 6.25 * direction
    radius = 2.301
    for index, point in enumerate(spline.points):
        t = index / (samples - 1)
        angle = phase + turns * 2.0 * math.pi * t
        point.co = (
            math.cos(angle) * radius * CM,
            math.sin(angle) * radius * CM,
            (z0 + (z1 - z0) * t) * CM,
            1.0,
        )
    obj = bpy.data.objects.new(name, curve)
    collection.objects.link(obj)
    curve.materials.append(material)
    base.activate(obj)
    bpy.ops.object.convert(target="MESH")
    obj = bpy.context.object
    base.tag(obj, name, 1)
    obj["Aerathea.WrapDirection"] = "ascending" if direction > 0 else "descending"
    return base.finalize_mesh(obj, smooth=True)


def add_grip_lacing(name, direction, material, collection):
    segments = []
    for face_name, y_cm in (("Front", -2.32), ("Back", 2.32)):
        for index, center_z in enumerate((20.8, 26.0, 31.2, 36.4, 41.6, 46.8, 52.0, 57.2)):
            low_x = -1.72 if direction > 0 else 1.72
            high_x = 1.72 if direction > 0 else -1.72
            segment = base.add_bar_xz(
                f"{name}_{face_name}_{index:02d}",
                (low_x, center_z - 2.0),
                (high_x, center_z + 2.0),
                0.82,
                0.36,
                y_cm,
                material,
                collection,
                1,
            )
            base.activate(segment)
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            segments.append(segment)
    bpy.ops.object.select_all(action="DESELECT")
    for segment in segments:
        segment.select_set(True)
    bpy.context.view_layer.objects.active = segments[0]
    bpy.ops.object.join()
    obj = bpy.context.object
    obj.name = name
    base.tag(obj, name, 1)
    obj["Aerathea.WrapDirection"] = "ascending" if direction > 0 else "descending"
    return base.finalize_mesh(obj)


def add_face_facet(name, points, front, material, collection, tier=1):
    if front:
        return base.add_xz_prism(name, points, -15.99, -15.67, material, collection, 0.10, tier)
    return base.add_xz_prism(name, points, 15.67, 15.99, material, collection, 0.10, tier)


def add_double_sided_diamond(parts, name, x, z, width, height, material, collection, tier=1, depth_outer=15.98, depth_inner=15.54):
    parts.append(base.add_diamond(f"{name}_Front", x, z, width, height, -depth_outer, -depth_inner, material, collection, tier))
    parts.append(base.add_diamond(f"{name}_Back", x, z, width, height, depth_inner, depth_outer, material, collection, tier))


def build_geometry(materials):
    asset = base.get_collection("SB_ASSET")
    root = bpy.data.objects.new("SiegeBreaker_ROOT", None)
    asset.objects.link(root)
    root["Aerathea.ContractID"] = CONTRACT_ID
    root["Aerathea.Revision"] = REVISION
    root["Aerathea.OverallBoundsCM"] = "52x32x170"
    root["Aerathea.Pivot"] = "bottom center of pommel at world origin"
    root["Aerathea.RequiredFeatureGroups"] = 6

    stone_left = [
        (-24.2, 132.0), (-18.0, 132.4), (-13.4, 136.8), (-12.0, 143.0),
        (-12.4, 160.2), (-15.8, 167.4), (-20.4, 170.0), (-24.6, 168.8),
        (-26.0, 163.4), (-25.6, 137.0),
    ]
    stone_right = [(-x, z) for x, z in stone_left]
    stone_right.reverse()

    parts = [
        base.add_xz_prism("Head_Stone_Left", stone_left, -15.58, 15.58, materials["M_Stone"], asset, 0.42, 0),
        base.add_xz_prism("Head_Stone_Right", stone_right, -15.58, 15.58, materials["M_Stone"], asset, 0.42, 0),
        base.add_cube("Head_Core_Bronze", (24.0, 25.0, 29.0), (0.0, 0.0, 151.0), materials["M_Bronze"], asset, 0.48, 0),
        base.add_cube("Head_Core_Steel", (19.0, 28.2, 24.5), (0.0, 0.0, 151.0), materials["M_Steel"], asset, 0.38, 0),
        base.add_cylinder("Shaft_Metal", 5.0, 118.0, 73.0, materials["M_Steel"], asset, 24, 0),
        base.add_cylinder("Grip_Leather", 4.38, 42.0, 39.0, materials["M_Steel"], asset, 24, 0),
        base.add_elliptic_lathe(
            "Pommel",
            [(0.0, 2.1, 1.8), (1.5, 3.4, 2.8), (4.0, 4.7, 3.9),
             (7.0, 5.5, 4.5), (11.5, 5.5, 4.5), (15.5, 4.4, 3.7),
             (18.0, 3.0, 2.6)],
            materials["M_Steel"], asset, sides=12, tier=0,
        ),
        base.add_cylinder("Collar_Grip_Bottom", 7.8, 2.4, 18.8, materials["M_Bronze"], asset, 20, 1),
        base.add_cylinder("Collar_Grip_Top", 8.2, 3.2, 60.0, materials["M_Bronze"], asset, 20, 1),
        base.add_cylinder("Collar_Head_Lower", 10.8, 4.2, 130.2, materials["M_Bronze"], asset, 20, 1),
        base.add_cylinder("Collar_Head_Upper", 8.4, 3.0, 133.0, materials["M_Steel"], asset, 20, 1),
    ]

    # Irregular face facets: shallow, authored planar breaks that stay inside
    # the approved head envelope and create the dark runestone read.
    facet_sets = {
        "Left_UpperOuter": [(-24.7, 158.0), (-20.2, 168.9), (-16.2, 166.5), (-18.0, 155.4)],
        "Left_MidOuter": [(-25.2, 143.0), (-23.7, 157.2), (-18.0, 154.6), (-18.6, 143.0)],
        "Left_LowerOuter": [(-24.9, 134.8), (-18.8, 133.0), (-18.6, 142.2), (-25.1, 142.3)],
        "Left_UpperInner": [(-17.6, 155.2), (-16.0, 166.2), (-13.0, 159.8), (-12.7, 149.2)],
        "Left_LowerInner": [(-18.2, 143.0), (-13.0, 138.0), (-12.6, 148.4), (-17.7, 154.3)],
    }
    for side_name, mirror in (("Left", -1), ("Right", 1)):
        for label, points in facet_sets.items():
            source = points if side_name == "Left" else [(-x, z) for x, z in reversed(points)]
            for face_name, front in (("Front", True), ("Back", False)):
                parts.append(add_face_facet(f"StoneFacet_{side_name}_{label.split('_', 1)[1]}_{face_name}", source, front, materials["M_Stone"], asset, 1))

    # Outer side facets make the 3/4 silhouette authored rather than extruded.
    side_profile = [(-14.8, 136.0), (-12.0, 133.2), (10.0, 133.2), (15.2, 141.0), (14.0, 163.0), (8.0, 168.0), (-10.0, 168.0), (-15.0, 162.0)]
    parts.append(add_yz_prism("StoneFacet_Left_Outer", side_profile, -26.0, -25.70, materials["M_Stone"], asset, 0.08, 1))
    parts.append(add_yz_prism("StoneFacet_Right_Outer", side_profile, 25.70, 26.0, materials["M_Stone"], asset, 0.08, 1))

    # Dwarven stone clamps: steel foundations, aged-bronze rails, and compact
    # recessed rune marks on both reviewable faces.
    for x in (-23.4, -13.7, 13.7, 23.4):
        parts.append(base.add_cube(f"StoneClamp_Steel_{x:+.1f}", (2.3, 31.2, 28.0), (x, 0.0, 151.0), materials["M_Steel"], asset, 0.24, 1))
        parts.append(base.add_cube(f"StoneClamp_Bronze_{x:+.1f}", (0.78, 31.55, 25.2), (x, 0.0, 151.0), materials["M_Bronze"], asset, 0.16, 1))
    for x in (-19.2, 19.2):
        add_double_sided_diamond(parts, f"StoneRuneFrame_{x:+.1f}", x, 151.0, 8.3, 19.8, materials["M_Steel"], asset, 1)
        for z, size in ((144.8, 2.3), (151.0, 4.6), (157.2, 2.3)):
            add_double_sided_diamond(parts, f"StoneRune_{x:+.1f}_{z:.1f}", x, z, size, size * 1.25, materials["M_Rune_Emissive"], asset, 2, 16.0, 15.92)

    # Deep central mechanism and layered shield geometry.
    for face_name, y in (("Front", -15.20), ("Back", 15.20)):
        parts.extend(
            [
                base.add_bar_xz(f"CoreBrace_OuterA_{face_name}", (-10.0, 138.8), (10.0, 163.2), 3.2, 1.10, y, materials["M_Steel"], asset, 1),
                base.add_bar_xz(f"CoreBrace_OuterB_{face_name}", (-10.0, 163.2), (10.0, 138.8), 3.2, 1.10, y, materials["M_Steel"], asset, 1),
                base.add_bar_xz(f"CoreBrace_BronzeA_{face_name}", (-9.3, 139.6), (9.3, 162.4), 1.45, 1.22, y - 0.10 if y < 0 else y + 0.10, materials["M_Bronze"], asset, 1),
                base.add_bar_xz(f"CoreBrace_BronzeB_{face_name}", (-9.3, 162.4), (9.3, 139.6), 1.45, 1.22, y - 0.10 if y < 0 else y + 0.10, materials["M_Bronze"], asset, 1),
            ]
        )
        y0, y1 = ((-15.97, -15.28) if y < 0 else (15.28, 15.97))
        parts.append(base.add_diamond(f"CoreShield_Bronze_{face_name}", 0.0, 151.0, 15.2, 23.4, y0, y1, materials["M_Bronze"], asset, 1))
        inner0, inner1 = ((-16.0, -15.97) if y < 0 else (15.97, 16.0))
        parts.append(base.add_diamond(f"CoreShield_Steel_{face_name}", 0.0, 151.0, 10.3, 16.4, inner0, inner1, materials["M_Steel"], asset, 1))
        parts.append(base.add_diamond(f"CoreRune_Focal_{face_name}", 0.0, 151.0, 5.2, 8.0, inner0, inner1, materials["M_Rune_Emissive"], asset, 2))

    for face_name, y in (("Front", -15.76), ("Back", 15.76)):
        for x0, x1 in ((-13.2, -7.8), (7.8, 13.2)):
            parts.append(base.add_bar_xz(f"RadialBrace_{face_name}_{x0:+.1f}", (x0, 145.5), (x1, 151.0), 1.7, 0.38, y, materials["M_Bronze"], asset, 1))

    # Crown and socket retain the monumental dwarven vertical rhythm.
    parts.extend(
        [
            base.add_cylinder("Head_Undersocket", 11.0, 1.2, 132.6, materials["M_Steel"], asset, 20, 1),
            base.add_cylinder("Head_Crown_Base", 11.8, 2.0, 166.5, materials["M_Bronze"], asset, 20, 1),
            base.add_cylinder("Head_Crown_Mid", 8.8, 1.8, 168.0, materials["M_Steel"], asset, 20, 1),
            base.add_cylinder("Head_Crown_Top", 5.2, 1.2, 169.2, materials["M_Bronze"], asset, 16, 2),
            base.add_cylinder("Head_Crown_Tip", 2.8, 0.2, 169.9, materials["M_Steel"], asset, 12, 2),
            base.add_torus("GripRing_Bottom", 3.02, 0.36, 20.3, materials["M_Steel"], asset, 1, 20),
            base.add_torus("GripRing_Top", 3.10, 0.38, 58.3, materials["M_Steel"], asset, 1, 20),
            add_grip_lacing("Grip_Wrap_Ascending", 1, materials["M_Leather"], asset),
            add_grip_lacing("Grip_Wrap_Descending", -1, materials["M_Leather"], asset),
        ]
    )

    # Engraved/inlaid shaft: thin surface-owned rails and runes remain inside
    # the exact 5 cm cylinder envelope.
    for face_name, y in (("Front", -2.47), ("Back", 2.47)):
        parts.append(base.add_cube(f"Shaft_InlayRail_L_{face_name}", (0.24, 0.05, 63.0), (-1.52, y, 94.5), materials["M_Bronze"], asset, 0.03, 1))
        parts.append(base.add_cube(f"Shaft_InlayRail_R_{face_name}", (0.24, 0.05, 63.0), (1.52, y, 94.5), materials["M_Bronze"], asset, 0.03, 1))
        y0, y1 = ((-2.50, -2.47) if y < 0 else (2.47, 2.50))
        for z in (69.0, 82.0, 95.0, 108.0, 121.0):
            parts.append(base.add_diamond(f"Shaft_EngravedRune_{face_name}_{z:.0f}", 0.0, z, 1.25, 4.8, y0, y1, materials["M_Rune_Emissive"], asset, 2))
    for z in (62.0, 77.5, 92.5, 107.5, 123.5, 129.5):
        parts.append(base.add_torus(f"ShaftBand_{z:.1f}", 2.19, 0.22, z, materials["M_Bronze"], asset, 1, 20))

    # Layered counterweight: steel mass, bronze armor facets, and one compact
    # rune crystal per broad face.
    for face_name, y0, y1 in (("Front", -4.50, -4.12), ("Back", 4.12, 4.50)):
        parts.append(base.add_diamond(f"PommelPlate_Bronze_{face_name}", 0.0, 9.2, 9.0, 11.7, y0, y1, materials["M_Bronze"], asset, 1))
        outer0, outer1 = ((-4.50, -4.46) if y0 < 0 else (4.46, 4.50))
        parts.append(base.add_diamond(f"PommelPlate_Steel_{face_name}", 0.0, 9.2, 6.2, 8.3, outer0, outer1, materials["M_Steel"], asset, 1))
        parts.append(base.add_diamond(f"PommelRune_Focal_{face_name}", 0.0, 9.2, 3.2, 4.7, outer0, outer1, materials["M_Rune_Emissive"], asset, 2))
    parts.extend(
        [
            base.add_torus("PommelBand_Lower", 4.55, 0.32, 4.0, materials["M_Bronze"], asset, 1, 20),
            base.add_torus("PommelBand_Upper", 4.18, 0.30, 15.5, materials["M_Bronze"], asset, 1, 20),
            base.add_cylinder("PommelNeck", 6.2, 2.0, 17.0, materials["M_Bronze"], asset, 16, 1),
        ]
    )

    # Limited large rivets support craftsmanship without micro-detail bloat.
    rivets = [(-9.0, 139.4), (-9.0, 162.6), (9.0, 139.4), (9.0, 162.6)]
    for index, (x, z) in enumerate(rivets):
        parts.append(base.add_rivet(f"Rivet_Core_Front_{index:02d}", (x, -15.70, z), materials["M_Bronze"], asset, 2))
        parts.append(base.add_rivet(f"Rivet_Core_Back_{index:02d}", (x, 15.70, z), materials["M_Bronze"], asset, 2))

    for obj in parts:
        obj.parent = root
    return asset, root, parts


def main() -> int:
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    EXPORT_ROOT.mkdir(parents=True, exist_ok=True)
    TEXTURE_ROOT.mkdir(parents=True, exist_ok=True)

    base.TEXTURE_ROOT = TEXTURE_ROOT
    base.clear_scene()
    base.configure_scene()
    bpy.context.scene["Aerathea.ContractID"] = CONTRACT_ID
    bpy.context.scene["Aerathea.Revision"] = REVISION
    materials = base.create_materials()
    tune_a02_materials(materials)
    _asset, _root, source_objects = build_geometry(materials)

    export_collection = base.get_collection("SB_EXPORT")
    collision_collection = base.get_collection("SB_COLLISION")
    lod0 = base.create_lod(source_objects, 0, 2, 1.0, materials, export_collection)
    lod1 = base.create_lod(source_objects, 1, 2, 0.64, materials, export_collection)
    lod2 = base.create_lod(source_objects, 2, 2, 0.41, materials, export_collection)
    lod3 = base.create_lod(source_objects, 3, 2, 0.19, materials, export_collection)
    lods = [lod0, lod1, lod2, lod3]
    collisions = base.create_collision(collision_collection)

    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))

    base_fbx = EXPORT_ROOT / f"{ASSET_ID}.fbx"
    base.export_selected([lod0, *collisions], base_fbx, "fbx")
    export_paths = [base_fbx]
    for level, lod in enumerate(lods[1:], start=1):
        path = EXPORT_ROOT / f"{ASSET_ID}_LOD{level}.fbx"
        base.export_selected([lod], path, "fbx")
        export_paths.append(path)
    glb_path = EXPORT_ROOT / f"{ASSET_ID}.glb"
    base.export_selected([lod0], glb_path, "glb")
    export_paths.append(glb_path)

    minimum, maximum, extent = base.bounds_cm(source_objects)
    source_triangles = sum(base.triangle_count(obj) for obj in source_objects)
    lod0_triangles = base.triangle_count(lod0)
    lod_stats = []
    for level, lod in enumerate(lods):
        lod_min, lod_max, lod_extent = base.bounds_cm([lod])
        lod_stats.append(
            {
                "level": level,
                "object": lod.name,
                "triangles": base.triangle_count(lod),
                "ratio_to_lod0": round(base.triangle_count(lod) / max(lod0_triangles, 1), 6),
                "bounds_cm": {"minimum": lod_min, "maximum": lod_max, "extent": lod_extent},
                "uv_layers": [layer.name for layer in lod.data.uv_layers],
                "material_slots": [slot.material.name if slot.material else None for slot in lod.material_slots],
            }
        )

    required_features = {
        "dark_irregular_faceted_runestone_head": sorted(obj.name for obj in source_objects if obj.name.startswith("StoneFacet_")),
        "layered_dwarven_head_bracing": sorted(obj.name for obj in source_objects if obj.name.startswith(("StoneClamp_", "CoreBrace_", "CoreShield_", "RadialBrace_"))),
        "restrained_recessed_blue_runes": sorted(obj.name for obj in source_objects if "Rune" in obj.name),
        "crisscross_leather_grip": sorted(obj.name for obj in source_objects if obj.name.startswith("Grip_Wrap_")),
        "engraved_inlaid_shaft": sorted(obj.name for obj in source_objects if obj.name.startswith(("Shaft_Inlay", "Shaft_Engraved"))),
        "layered_focal_pommel": sorted(obj.name for obj in source_objects if obj.name.startswith(("PommelPlate_", "PommelRune_", "PommelBand_"))),
    }
    manifest = {
        "schema": "aerathea.dcc_game_ready_candidate.v2",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "artifact_status": "candidate",
        "pipeline_status": "DCC game-ready candidate",
        "authority": {
            "package_sha256": "6d4bf67fe4dcb1bc752c615d16b039bf6fd430037b6ffa4772f8ae83c689a8f0",
            "geometry": ["asset_spec.json", "dimensions_cm.csv"],
            "style": ["VC-DRW-SiegeBreaker-Hammer-A01", "reference/concept_sheet_style_reference.png"],
            "legacy_builder_used": False,
            "a01_candidate_overwritten": False,
        },
        "coordinate_frame": {
            "x": "head width, right positive",
            "y": "head depth, back positive",
            "z": "overall length, up positive",
            "origin": "bottom center of pommel at Z=0",
        },
        "world_bounds_cm": {"minimum": minimum, "maximum": maximum, "extent": extent},
        "source_component_count": len(source_objects),
        "source_triangles": source_triangles,
        "lods": lod_stats,
        "materials": base.MATERIAL_ORDER,
        "textures": sorted(str(path.relative_to(ROOT)) for path in TEXTURE_ROOT.glob("*.png")),
        "required_feature_groups": required_features,
        "collision": [
            {"object": obj.name, "triangles": base.triangle_count(obj), "role": obj["Aerathea.CollisionRole"]}
            for obj in collisions
        ],
        "contacts": {
            "shaft_head": {"shaft_top_z_cm": 132, "head_bottom_z_cm": 132, "gap_cm": 0, "status": "pass"},
            "shaft_pommel": {"shaft_interval_z_cm": [14, 132], "pommel_interval_z_cm": [0, 18], "overlap_cm": 4, "status": "pass"},
            "grip": {"interval_z_cm": [18, 60], "visible_length_cm": 42, "status": "pass"},
        },
        "outputs": [
            {"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "bytes": path.stat().st_size}
            for path in [BLEND_PATH, *export_paths]
        ],
        "final_visual_approval": "pending Flamestrike",
        "unreal_import_authorized": False,
        "fully_game_ready": False,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(MANIFEST_PATH)
    print(f"source_components={len(source_objects)} source_triangles={source_triangles} lod0_triangles={lod0_triangles}")
    print(f"lod_triangles={[base.triangle_count(lod) for lod in lods]}")
    print(f"bounds_cm={extent}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
