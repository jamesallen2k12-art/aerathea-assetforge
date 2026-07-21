"""Build the fresh pixel-authority Siege Breaker A03 DCC candidate.

The script uses A01 mechanical helpers for primitive creation, UV projection,
LOD joining, collision naming, and export only. It imports no A01/A02 geometry
and independently constructs every visible A03 form from the approved numeric
envelope and A03 source-pixel authority.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
REVISION = "PixelReconstruction_A03"
CONTRACT_ID = "SB-VF-A03-PIXEL"
CM = 0.01

SOURCE_ROOT = ROOT / "SourceAssets/Blender/Weapons/Dwarven" / ASSET_ID
EXPORT_ROOT = ROOT / "SourceAssets/Exports/Weapons/Dwarven" / ASSET_ID / REVISION
TEXTURE_ROOT = ROOT / "SourceAssets/Textures/Weapons/Dwarven" / ASSET_ID / REVISION
BLEND_PATH = SOURCE_ROOT / f"{ASSET_ID}_DCCGameReady_{REVISION}.blend"
MANIFEST_PATH = SOURCE_ROOT / f"{ASSET_ID}_{REVISION.upper()}_MANIFEST.json"
MEASUREMENT_PATH = ROOT / "docs/assets/blueprints" / ASSET_ID / "manifests/VISUAL_FIDELITY_A03_SOURCE_MEASUREMENTS.json"
CONFLICT_PATH = ROOT / "docs/assets/blueprints" / ASSET_ID / "manifests/VISUAL_FIDELITY_A03_CROSS_VIEW_CONFLICT_AUDIT.json"


def load_base_module():
    path = ROOT / "Tools/DCC/build_siegebreaker_final_package_a01.py"
    spec = importlib.util.spec_from_file_location("siegebreaker_mechanical_helpers", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load mechanical helpers: {path}")
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


def add_faceted_stone(name, side, material, collection):
    """Create one fresh convex/faceted hammer stone inside its 14 cm X allocation."""
    if side == "left":
        ring_specs = [
            (-25.68, 14.5, 17.4),
            (-24.2, 15.4, 18.1),
            (-21.0, 16.0, 19.0),
            (-17.5, 15.7, 18.6),
            (-14.0, 14.8, 17.2),
            (-12.0, 12.5, 14.8),
        ]
    else:
        ring_specs = [
            (12.0, 12.5, 14.8),
            (14.0, 14.8, 17.2),
            (17.5, 15.7, 18.6),
            (21.0, 16.0, 19.0),
            (24.2, 15.4, 18.1),
            (25.68, 14.5, 17.4),
        ]
    sides = 16
    irregular = (1.0, 0.96, 0.985, 0.945, 1.0, 0.955, 0.98, 0.94, 1.0, 0.965, 0.99, 0.95, 1.0, 0.95, 0.98, 0.955)
    vertices = []
    for x_cm, radius_y, radius_z in ring_specs:
        for index in range(sides):
            angle = math.tau * index / sides
            factor = irregular[(index + (0 if side == "left" else 3)) % sides]
            # Preserve exact extrema at cardinal samples.
            if index % 4 == 0:
                factor = 1.0
            y_cm = math.sin(angle) * radius_y * factor
            z_cm = 151.0 + math.cos(angle) * radius_z * factor
            vertices.append((x_cm * CM, y_cm * CM, z_cm * CM))
    faces = []
    for ring in range(len(ring_specs) - 1):
        for index in range(sides):
            nxt = (index + 1) % sides
            lower = ring * sides
            upper = (ring + 1) * sides
            # Alternate diagonals later through triangulation while retaining
            # the readable broad faceted quads in the source mesh.
            faces.append((lower + index, lower + nxt, upper + nxt, upper + index))
    faces.append(tuple(reversed(range(sides))))
    last = (len(ring_specs) - 1) * sides
    faces.append(tuple(last + index for index in range(sides)))
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.data.materials.append(material)
    base.tag(obj, name, 0)
    obj["Aerathea.A03Construction"] = "fresh faceted convex rings from numeric envelope"
    return base.finalize_mesh(obj, smooth=False)


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
        bevel = obj.modifiers.new("A03_Bevel", "BEVEL")
        bevel.width = bevel_cm * CM
        bevel.segments = 1
        base.apply_modifier(obj, bevel.name)
    return obj


def add_bar_yz(name, start_yz, end_yz, width_cm, depth_cm, x_cm, material, collection, tier=1):
    y0, z0 = start_yz
    y1, z1 = end_yz
    dy = y1 - y0
    dz = z1 - z0
    length = math.hypot(dy, dz)
    angle = math.atan2(dz, dy)
    return base.add_cube(
        name,
        (depth_cm, length, width_cm),
        (x_cm, (y0 + y1) * 0.5, (z0 + z1) * 0.5),
        material,
        collection,
        bevel_cm=0.16,
        tier=tier,
        rotation=(angle, 0.0, 0.0),
    )


def add_frame_xz(parts, name, center_x, center_z, width, height, y, depth, line_width, material, collection, tier=1):
    points = [
        (center_x, center_z + height * 0.5),
        (center_x + width * 0.5, center_z),
        (center_x, center_z - height * 0.5),
        (center_x - width * 0.5, center_z),
    ]
    for index in range(4):
        parts.append(base.add_bar_xz(f"{name}_{index:02d}", points[index], points[(index + 1) % 4], line_width, depth, y, material, collection, tier))


def add_frame_yz(parts, name, center_y, center_z, width_y, height, x, depth, line_width, material, collection, tier=1):
    points = [
        (center_y, center_z + height * 0.5),
        (center_y + width_y * 0.5, center_z),
        (center_y, center_z - height * 0.5),
        (center_y - width_y * 0.5, center_z),
    ]
    for index in range(4):
        parts.append(add_bar_yz(f"{name}_{index:02d}", points[index], points[(index + 1) % 4], line_width, depth, x, material, collection, tier))


def add_axis_x_cylinder(name, length_cm, diameter_cm, center_x_cm, center_z_cm, material, collection, vertices=20, tier=1):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=diameter_cm * CM * 0.5,
        depth=length_cm * CM,
        location=(center_x_cm * CM, 0.0, center_z_cm * CM),
        rotation=(0.0, math.pi * 0.5, 0.0),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    base.move_to_collection(obj, collection)
    base.tag(obj, name, tier)
    return base.finalize_mesh(obj, smooth=True)


def add_stone_surface_crack(name, start_xz, end_xz, face_sign, material, collection, tier=2):
    """Conform a narrow crack seam to the stone's curved front/back surface."""
    curve_data = bpy.data.curves.new(f"{name}_Curve", "CURVE")
    curve_data.dimensions = "3D"
    curve_data.resolution_u = 1
    curve_data.bevel_depth = 0.105 * CM
    curve_data.bevel_resolution = 0
    curve_data.resolution_u = 1
    curve_data.use_fill_caps = True
    spline = curve_data.splines.new("POLY")
    samples = 8
    spline.points.add(samples - 1)
    x0, z0 = start_xz
    x1, z1 = end_xz
    for index in range(samples):
        t = index / (samples - 1)
        x = x0 + (x1 - x0) * t
        z = z0 + (z1 - z0) * t
        # The approved stone mass is an irregularized ellipse around Z=151.
        # This sampled surface prevents the old constant-Y bars from floating
        # beyond the silhouette near the rounded crown and lower shoulder.
        radius_y = 15.35
        radius_z = 18.35
        normalized_z = max(-0.998, min(0.998, (z - 151.0) / radius_z))
        y = face_sign * (radius_y * math.sqrt(max(0.0, 1.0 - normalized_z * normalized_z)) + 0.06)
        spline.points[index].co = (x * CM, y * CM, z * CM, 1.0)
    obj = bpy.data.objects.new(name, curve_data)
    collection.objects.link(obj)
    obj.data.materials.append(material)
    base.tag(obj, name, tier)
    base.activate(obj)
    bpy.ops.object.convert(target="MESH")
    obj = bpy.context.object
    obj["Aerathea.A03Construction"] = "source-visible crack conformed to measured stone surface"
    return base.finalize_mesh(obj, smooth=True)


def add_helical_ribbon(name, direction, phase, material, collection, tier=1):
    samples = 96
    turns = 8.25
    # Inset the helix centerline so the angled ribbon width terminates at the
    # exact approved grip interval Z=18..60 cm.
    z0 = 18.77
    z1 = 59.23
    # The grip cylinder is 4.58 cm in diameter.  Keep the wrap visibly proud
    # of that 2.29 cm radius so the source's broad brown crossed leather reads
    # in the registered full-asset view, not only in a macro inspection.
    radius = 2.385
    thickness = 0.20
    width = 1.62
    vertices = []
    for index in range(samples):
        t = index / (samples - 1)
        theta = phase + direction * turns * math.tau * t
        z = z0 + (z1 - z0) * t
        normal = Vector((math.cos(theta), math.sin(theta), 0.0))
        tangent = Vector((
            -radius * math.sin(theta) * direction * turns * math.tau,
            radius * math.cos(theta) * direction * turns * math.tau,
            z1 - z0,
        )).normalized()
        cross_width = normal.cross(tangent).normalized()
        center = Vector((normal.x * radius, normal.y * radius, z))
        outer = normal * (thickness * 0.5)
        inner = normal * (-thickness * 0.5)
        for offset in (-width * 0.5, width * 0.5):
            point = center + cross_width * offset + outer
            vertices.append(tuple(value * CM for value in point))
        for offset in (-width * 0.5, width * 0.5):
            point = center + cross_width * offset + inner
            vertices.append(tuple(value * CM for value in point))
    faces = []
    for index in range(samples - 1):
        current = index * 4
        nxt = (index + 1) * 4
        faces.extend([
            (current, nxt, nxt + 1, current + 1),
            (current + 3, nxt + 3, nxt + 2, current + 2),
            (current, current + 2, nxt + 2, nxt),
            (current + 1, nxt + 1, nxt + 3, current + 3),
        ])
    faces.extend([(0, 1, 3, 2), ((samples - 1) * 4, (samples - 1) * 4 + 2, (samples - 1) * 4 + 3, (samples - 1) * 4 + 1)])
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    obj.data.materials.append(material)
    base.tag(obj, name, tier)
    obj["Aerathea.WrapDirection"] = "ascending" if direction > 0 else "descending"
    return base.finalize_mesh(obj, smooth=True)


def tune_materials(materials):
    # Keep texture-driven PBR values while matching the source's dark-value
    # hierarchy and restrained cyan emission.
    for material_name, roughness_bias in (("M_Stone", 0.10), ("M_Bronze", 0.02), ("M_Steel", 0.04), ("M_Leather", 0.08)):
        material = materials[material_name]
        bsdf = next((node for node in material.node_tree.nodes if node.type == "BSDF_PRINCIPLED"), None)
        if bsdf is not None and not bsdf.inputs["Roughness"].is_linked:
            bsdf.inputs["Roughness"].default_value = min(1.0, bsdf.inputs["Roughness"].default_value + roughness_bias)
    rune = materials["M_Rune_Emissive"]
    for node in rune.node_tree.nodes:
        if node.type == "MATH" and node.operation == "MULTIPLY":
            node.inputs[1].default_value = 2.2

    def color_adjust(material_name, saturation, value, hue=0.5):
        material = materials[material_name]
        nodes = material.node_tree.nodes
        links = material.node_tree.links
        bsdf = next((node for node in nodes if node.type == "BSDF_PRINCIPLED"), None)
        if bsdf is None or not bsdf.inputs["Base Color"].is_linked:
            return
        old_link = bsdf.inputs["Base Color"].links[0]
        source = old_link.from_socket
        links.remove(old_link)
        adjust = nodes.new("ShaderNodeHueSaturation")
        adjust.name = f"A03_{material_name}_SourcePaletteAdjust"
        adjust.inputs["Hue"].default_value = hue
        adjust.inputs["Saturation"].default_value = saturation
        adjust.inputs["Value"].default_value = value
        adjust.inputs["Fac"].default_value = 1.0
        links.new(source, adjust.inputs["Color"])
        links.new(adjust.outputs["Color"], bsdf.inputs["Base Color"])

    color_adjust("M_Stone", 0.82, 0.52)
    color_adjust("M_Bronze", 0.72, 0.82, 0.535)
    color_adjust("M_Steel", 0.72, 0.88)
    color_adjust("M_Leather", 1.02, 1.35)


def build_geometry(materials):
    asset = base.get_collection("SB_ASSET")
    root = bpy.data.objects.new("SiegeBreaker_A03_ROOT", None)
    asset.objects.link(root)
    root["Aerathea.ContractID"] = CONTRACT_ID
    root["Aerathea.Revision"] = REVISION
    root["Aerathea.GeometryInputs"] = "fresh A03 construction; zero A01/A02 geometry inputs"
    root["Aerathea.NumericEnvelopeCM"] = "52x32x170"
    root["Aerathea.PrimaryVisualAuthority"] = "large 3/4 concept render source pixels"
    parts = []

    # Primary source-owned masses.
    parts.append(add_faceted_stone("Head_Stone_Left_A03", "left", materials["M_Stone"], asset))
    parts.append(add_faceted_stone("Head_Stone_Right_A03", "right", materials["M_Stone"], asset))
    core_outline = [
        (-7.0, 135.0), (7.0, 135.0), (12.0, 141.0), (12.0, 161.0),
        (7.0, 167.0), (-7.0, 167.0), (-12.0, 161.0), (-12.0, 141.0),
    ]
    parts.append(base.add_xz_prism("Head_Core_A03", core_outline, -13.8, 13.8, materials["M_Steel"], asset, 0.55, 0))
    parts.append(base.add_cylinder("Shaft_Metal", 5.0, 118.0, 73.0, materials["M_Steel"], asset, 24, 0))
    parts.append(base.add_cylinder("Grip_Leather", 4.34, 42.0, 39.0, materials["M_Leather"], asset, 24, 0))
    parts.append(base.add_elliptic_lathe(
        "Pommel",
        [(0.0, 2.2, 1.9), (1.8, 3.2, 2.7), (3.4, 4.2, 3.5),
         (5.0, 5.5, 4.5), (14.0, 5.5, 4.5), (16.0, 4.8, 3.9),
         (18.0, 2.9, 2.5)],
        materials["M_Steel"], asset, sides=12, tier=0,
    ))

    # Stone-face facets, crack seams, structural rails, and restrained runes.
    stone_cracks = [
        ((-23.2, 166.8), (-20.4, 158.8)), ((-20.4, 158.8), (-24.2, 151.8)),
        ((-20.4, 158.8), (-15.3, 162.7)), ((-24.2, 151.8), (-21.2, 143.8)),
        ((-21.2, 143.8), (-24.0, 136.8)), ((-21.2, 143.8), (-15.2, 147.0)),
    ]
    for side_name, mirror in (("Left", 1.0), ("Right", -1.0)):
        for face_name, face_sign in (("Front", -1.0), ("Back", 1.0)):
            for index, (start, end) in enumerate(stone_cracks):
                p0 = (start[0] * mirror, start[1])
                p1 = (end[0] * mirror, end[1])
                parts.append(add_stone_surface_crack(f"StoneCrack_{side_name}_{face_name}_{index:02d}", p0, p1, face_sign, materials["M_Steel"], asset, 2))
        rail_x = -14.3 if side_name == "Left" else 14.3
        parts.append(base.add_cube(f"StoneRail_Steel_{side_name}", (2.7, 31.55, 31.0), (rail_x, 0.0, 151.0), materials["M_Steel"], asset, 0.22, 1))
        parts.append(base.add_cube(f"StoneRail_Bronze_{side_name}", (0.88, 31.82, 27.5), (rail_x, 0.0, 151.0), materials["M_Bronze"], asset, 0.14, 1))
        for face_name, y0, y1 in (("Front", -16.0, -15.94), ("Back", 15.94, 16.0)):
            for index, z in enumerate((141.5, 146.2, 151.0, 155.8, 160.5)):
                parts.append(base.add_diamond(f"StoneRail_Rune_{side_name}_{face_name}_{index:02d}", rail_x, z, 1.45, 2.75, y0, y1, materials["M_Rune_Emissive"], asset, 2))

    # Large strike-face rune frames on the actual X-facing stone caps.
    for side_name, x_surface, direction in (("Left", -25.90, -1.0), ("Right", 25.90, 1.0)):
        x_plate_min, x_plate_max = ((-25.88, -25.72) if direction < 0 else (25.72, 25.88))
        diamond_yz = [(0.0, 161.0), (8.0, 151.0), (0.0, 141.0), (-8.0, 151.0)]
        parts.append(add_yz_prism(f"StoneStrikePlate_{side_name}", diamond_yz, x_plate_min, x_plate_max, materials["M_Steel"], asset, 0.12, 1))
        add_frame_yz(parts, f"StoneStrikeFrame_Bronze_{side_name}", 0.0, 151.0, 12.0, 16.0, x_surface, 0.16, 1.3, materials["M_Bronze"], asset, 1)
        rune_points = [(0.0, 155.5), (3.4, 151.0), (0.0, 146.5), (-3.4, 151.0)]
        rune_x_min, rune_x_max = ((-26.0, -25.94) if direction < 0 else (25.94, 26.0))
        parts.append(add_yz_prism(f"StoneStrikeRune_{side_name}", rune_points, rune_x_min, rune_x_max, materials["M_Rune_Emissive"], asset, 0.0, 2))
        strike_cracks = [
            ((0.0, 161.0), (-7.0, 167.0)), ((0.0, 161.0), (8.5, 166.0)),
            ((8.0, 151.0), (13.0, 156.0)), ((8.0, 151.0), (12.5, 144.0)),
            ((0.0, 141.0), (7.0, 135.5)), ((0.0, 141.0), (-8.0, 136.5)),
            ((-8.0, 151.0), (-13.0, 157.0)), ((-8.0, 151.0), (-12.0, 144.5)),
        ]
        for index, (start, end) in enumerate(strike_cracks):
            parts.append(add_bar_yz(f"StoneStrikeCrack_{side_name}_{index:02d}", start, end, 0.22, 0.10, x_surface, materials["M_Steel"], asset, 2))

    # Axles and layered mechanical connectors anchor each stone to the core.
    for z in (143.0, 159.0):
        parts.append(add_axis_x_cylinder(f"Head_Axle_Steel_{z:.0f}", 34.0, 5.2, 0.0, z, materials["M_Steel"], asset, 20, 1))
        parts.append(add_axis_x_cylinder(f"Head_Axle_Bronze_{z:.0f}", 30.0, 3.3, 0.0, z, materials["M_Bronze"], asset, 18, 1))
    for x in (-10.6, 10.6):
        parts.append(add_axis_x_cylinder(f"Head_AxleHub_{x:+.1f}", 4.0, 8.2, x, 151.0, materials["M_Bronze"], asset, 20, 1))

    # Nested architectural face construction. Braces terminate at structural
    # nodes instead of reading as one flat X-frame.
    for face_name, y, sign in (("Front", -15.56, -1.0), ("Back", 15.56, 1.0)):
        y_outer = -15.84 if sign < 0 else 15.84
        y_inner = -15.66 if sign < 0 else 15.66
        plate_outline = [
            (-6.5, 136.8), (6.5, 136.8), (11.2, 142.5), (11.2, 159.5),
            (6.5, 165.2), (-6.5, 165.2), (-11.2, 159.5), (-11.2, 142.5),
        ]
        parts.append(base.add_xz_prism(f"CoreShield_Backplate_{face_name}", plate_outline, min(y, y_inner), max(y, y_inner), materials["M_Steel"], asset, 0.24, 1))
        add_frame_xz(parts, f"CoreShield_OuterBronze_{face_name}", 0.0, 151.0, 19.0, 27.0, y_outer, 0.22, 2.15, materials["M_Bronze"], asset, 1)
        add_frame_xz(parts, f"CoreShield_InnerSteel_{face_name}", 0.0, 151.0, 13.6, 20.0, y_outer + 0.02 * sign, 0.20, 1.35, materials["M_Steel"], asset, 1)
        parts.append(base.add_diamond(f"CoreShield_InnerPlate_{face_name}", 0.0, 151.0, 9.4, 14.2, min(y_outer, y_outer + 0.16 * sign), max(y_outer, y_outer + 0.16 * sign), materials["M_Steel"], asset, 1))
        parts.append(base.add_diamond(f"CoreRune_Focal_{face_name}", 0.0, 151.0, 4.8, 7.8, -16.0 if sign < 0 else 15.96, -15.96 if sign < 0 else 16.0, materials["M_Rune_Emissive"], asset, 2))
        # Layered roof/knee braces around the shield.
        brace_segments = [
            ((-10.6, 159.0), (-17.0, 166.0)), ((-10.6, 143.0), (-17.0, 136.0)),
            ((10.6, 159.0), (17.0, 166.0)), ((10.6, 143.0), (17.0, 136.0)),
            ((-11.0, 161.0), (-16.0, 151.0)), ((11.0, 161.0), (16.0, 151.0)),
            ((-11.0, 141.0), (-16.0, 151.0)), ((11.0, 141.0), (16.0, 151.0)),
        ]
        for index, (start, end) in enumerate(brace_segments):
            parts.append(base.add_bar_xz(f"CoreArchitecturalBrace_{face_name}_{index:02d}", start, end, 1.55, 0.55, y, materials["M_Bronze"], asset, 1))
        for x in (-8.6, 8.6):
            for z in (140.5, 161.5):
                parts.append(base.add_rivet(f"Rivet_Core_{face_name}_{x:+.1f}_{z:.1f}", (x, -15.70 if sign < 0 else 15.70, z), materials["M_Bronze"], asset, 2))

    # Crown, socket, and collars reproduce the source's stacked dwarven rhythm.
    parts.extend([
        base.add_cylinder("Head_Crown_Base_A03", 13.4, 2.0, 165.6, materials["M_Bronze"], asset, 20, 1),
        base.add_cylinder("Head_Crown_Steel_A03", 10.2, 2.0, 167.2, materials["M_Steel"], asset, 20, 1),
        base.add_cylinder("Head_Crown_Bronze_A03", 7.4, 1.7, 168.6, materials["M_Bronze"], asset, 18, 1),
        base.add_cylinder("Head_Crown_Tip_A03", 4.0, 1.0, 169.5, materials["M_Steel"], asset, 16, 2),
        base.add_cylinder("Shaft_HeadSocket_Steel_A03", 11.0, 4.0, 133.8, materials["M_Steel"], asset, 20, 1),
        base.add_cylinder("Shaft_HeadSocket_Bronze_A03", 8.2, 4.2, 131.8, materials["M_Bronze"], asset, 20, 1),
        base.add_torus("Shaft_HeadSocket_Ring_A03", 4.35, 0.48, 129.8, materials["M_Steel"], asset, 1, 20),
    ])

    # The source uses a long, ornate transition below the hammer head rather
    # than a small isolated socket.
    parts.extend([
        base.add_elliptic_lathe(
            "Shaft_HeadCollarBody_A03",
            [(116.0, 2.9, 2.9), (118.0, 4.1, 3.8), (121.0, 5.0, 4.5),
             (126.0, 5.2, 4.7), (130.0, 4.3, 3.9), (132.0, 3.3, 3.1)],
            materials["M_Steel"], asset, sides=12, tier=1,
        ),
        base.add_torus("Shaft_HeadCollarBand_Lower_A03", 3.85, 0.32, 118.5, materials["M_Bronze"], asset, 1, 20),
        base.add_torus("Shaft_HeadCollarBand_Mid_A03", 4.75, 0.30, 124.2, materials["M_Bronze"], asset, 1, 20),
        base.add_torus("Shaft_HeadCollarBand_Upper_A03", 3.95, 0.30, 130.2, materials["M_Bronze"], asset, 1, 20),
    ])
    for face_name, y, sign in (("Front", -4.74, -1.0), ("Back", 4.74, 1.0)):
        parts.append(base.add_diamond(f"Shaft_HeadCollarPlate_{face_name}", 0.0, 124.8, 6.8, 8.5, y - 0.05, y + 0.05, materials["M_Bronze"], asset, 1))
        rune_y = sorted((y + 0.08 * sign, y + 0.14 * sign))
        parts.append(base.add_diamond(f"Shaft_HeadCollarRune_{face_name}", 0.0, 124.8, 2.7, 4.0, rune_y[0], rune_y[1], materials["M_Rune_Emissive"], asset, 2))
    for side_name, x0, x1, x_surface in (("Left", -5.21, -5.14, -5.23), ("Right", 5.14, 5.21, 5.23)):
        collar_points = [(0.0, 129.0), (3.5, 124.8), (0.0, 120.6), (-3.5, 124.8)]
        parts.append(add_yz_prism(f"Shaft_HeadCollarSidePlate_{side_name}", collar_points, x0, x1, materials["M_Bronze"], asset, 0.05, 1))
        collar_rune = [(0.0, 127.0), (1.5, 124.8), (0.0, 122.6), (-1.5, 124.8)]
        rune_x = sorted((x_surface, x_surface + (-0.05 if x_surface < 0 else 0.05)))
        parts.append(add_yz_prism(f"Shaft_HeadCollarSideRune_{side_name}", collar_rune, rune_x[0], rune_x[1], materials["M_Rune_Emissive"], asset, 0.0, 2))

    # Engraved shaft: continuous rails plus a repeating chevron/vine path.
    for face_name, y in (("Front", -2.48), ("Back", 2.48)):
        parts.append(base.add_cube(f"Shaft_EngravedRail_L_{face_name}", (0.20, 0.04, 63.0), (-1.63, y, 95.0), materials["M_Steel"], asset, 0.02, 1))
        parts.append(base.add_cube(f"Shaft_EngravedRail_R_{face_name}", (0.20, 0.04, 63.0), (1.63, y, 95.0), materials["M_Steel"], asset, 0.02, 1))
        for index, z in enumerate((65.0, 72.5, 80.0, 87.5, 95.0, 102.5, 110.0, 117.5)):
            if index % 2 == 0:
                start, end = (-1.25, z - 3.0), (1.25, z + 3.0)
            else:
                start, end = (1.25, z - 3.0), (-1.25, z + 3.0)
            parts.append(base.add_bar_xz(f"Shaft_EngravedVine_{face_name}_{index:02d}", start, end, 0.42, 0.05, y, materials["M_Steel"], asset, 2))
        for index, z in enumerate((68.8, 83.8, 98.8, 113.8)):
            y0, y1 = ((-2.50, -2.48) if y < 0 else (2.48, 2.50))
            parts.append(base.add_diamond(f"Shaft_Rune_{face_name}_{index:02d}", 0.0, z, 1.1, 3.2, y0, y1, materials["M_Rune_Emissive"], asset, 2))
    for z in (62.0, 78.0, 96.0, 114.0, 128.0):
        parts.append(base.add_torus(f"Shaft_EngravedBand_{z:.0f}", 2.18, 0.22, z, materials["M_Steel"], asset, 2, 18))

    # Dense, actual 360-degree crossed leather ribbons.
    parts.append(add_helical_ribbon("Grip_Wrap_Ascending_A03", 1, 0.0, materials["M_Leather"], asset, 1))
    parts.append(add_helical_ribbon("Grip_Wrap_Descending_A03", -1, math.pi * 0.5, materials["M_Leather"], asset, 1))
    parts.extend([
        base.add_torus("Grip_Band_Lower_A03", 2.16, 0.30, 18.5, materials["M_Bronze"], asset, 1, 20),
        base.add_torus("Grip_Band_Upper_A03", 2.16, 0.30, 59.5, materials["M_Bronze"], asset, 1, 20),
        base.add_cylinder("Grip_Collar_Lower_Steel_A03", 7.6, 2.0, 17.3, materials["M_Steel"], asset, 18, 1),
        base.add_cylinder("Grip_Collar_Lower_Bronze_A03", 6.6, 1.1, 18.8, materials["M_Bronze"], asset, 18, 1),
        base.add_cylinder("Grip_Collar_Upper_Steel_A03", 8.0, 2.2, 60.6, materials["M_Steel"], asset, 18, 1),
        base.add_cylinder("Grip_Collar_Upper_Bronze_A03", 6.8, 1.2, 59.5, materials["M_Bronze"], asset, 18, 1),
    ])
    for face_name, y in (("Front", -3.98), ("Back", 3.98)):
        parts.append(base.add_diamond(f"Grip_Collar_Rune_{face_name}", 0.0, 60.6, 3.4, 4.2, y - 0.03, y + 0.03, materials["M_Rune_Emissive"], asset, 2))

    # Compact faceted pommel with a broad focal rune and layered bands.
    parts.extend([
        base.add_torus("PommelBand_Lower_A03", 3.1, 0.34, 2.2, materials["M_Bronze"], asset, 1, 20),
        base.add_torus("PommelBand_Mid_A03", 4.72, 0.30, 7.0, materials["M_Bronze"], asset, 1, 20),
        base.add_torus("PommelBand_Upper_A03", 4.45, 0.30, 14.6, materials["M_Bronze"], asset, 1, 20),
        base.add_cylinder("PommelNeck_A03", 6.0, 1.8, 17.1, materials["M_Bronze"], asset, 16, 1),
    ])
    for face_name, y, sign in (("Front", -4.58, -1.0), ("Back", 4.58, 1.0)):
        parts.append(base.add_diamond(f"PommelPlate_Steel_{face_name}", 0.0, 10.0, 10.0, 12.8, y - 0.10, y + 0.10, materials["M_Steel"], asset, 1))
        add_frame_xz(parts, f"PommelFrame_Bronze_{face_name}", 0.0, 10.0, 9.2, 11.6, y + 0.12 * sign, 0.18, 1.15, materials["M_Bronze"], asset, 1)
        rune_y = sorted((y + 0.22 * sign, y + 0.28 * sign))
        parts.append(base.add_diamond(f"PommelRune_Focal_{face_name}", 0.0, 10.0, 4.2, 6.2, rune_y[0], rune_y[1], materials["M_Rune_Emissive"], asset, 2))
    for side_name, x0, x1 in (("Left", -5.49, -5.42), ("Right", 5.42, 5.49)):
        points = [(0.0, 14.0), (3.2, 10.0), (0.0, 6.0), (-3.2, 10.0)]
        parts.append(add_yz_prism(f"PommelSidePlate_{side_name}", points, x0, x1, materials["M_Steel"], asset, 0.06, 1))
        x_surface = -5.44 if side_name == "Left" else 5.44
        add_frame_yz(parts, f"PommelSideFrame_Bronze_{side_name}", 0.0, 10.0, 5.0, 7.2, x_surface, 0.10, 0.75, materials["M_Bronze"], asset, 1)
        rune_points = [(0.0, 12.4), (1.7, 10.0), (0.0, 7.6), (-1.7, 10.0)]
        rune_x = (-5.50, -5.48) if side_name == "Left" else (5.48, 5.50)
        parts.append(add_yz_prism(f"PommelSideRune_{side_name}", rune_points, rune_x[0], rune_x[1], materials["M_Rune_Emissive"], asset, 0.0, 2))

    for obj in parts:
        obj.parent = root
        obj["Aerathea.SourceAuthority"] = "SB-VF-A03-PIXEL numeric envelope + approved primary source pixels"
        obj["Aerathea.A01A02GeometryUsed"] = False
    return asset, root, parts


def main() -> int:
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    EXPORT_ROOT.mkdir(parents=True, exist_ok=True)
    TEXTURE_ROOT.mkdir(parents=True, exist_ok=True)
    if not MEASUREMENT_PATH.exists() or not CONFLICT_PATH.exists():
        raise RuntimeError("A03 pixel measurement and conflict audit are required before geometry")
    base.TEXTURE_ROOT = TEXTURE_ROOT
    base.clear_scene()
    base.configure_scene()
    scene = bpy.context.scene
    scene["Aerathea.ContractID"] = CONTRACT_ID
    scene["Aerathea.Revision"] = REVISION
    scene["Aerathea.Authority"] = "A03 pixel override + exact numeric envelope"
    scene["Aerathea.A01A02GeometryUsed"] = False
    materials = base.create_materials()
    tune_materials(materials)
    _asset, _root, source_objects = build_geometry(materials)

    export_collection = base.get_collection("SB_EXPORT")
    collision_collection = base.get_collection("SB_COLLISION")
    lod0 = base.create_lod(source_objects, 0, 2, 0.80, materials, export_collection)
    lod1 = base.create_lod(source_objects, 1, 2, 0.55, materials, export_collection)
    lod2 = base.create_lod(source_objects, 2, 1, 0.58, materials, export_collection)
    lod3 = base.create_lod(source_objects, 3, 1, 0.30, materials, export_collection)
    lods = [lod0, lod1, lod2, lod3]
    collisions = base.create_collision(collision_collection)
    for obj in collisions:
        obj["Aerathea.ContractID"] = CONTRACT_ID

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
        lod_stats.append({
            "level": level,
            "object": lod.name,
            "triangles": base.triangle_count(lod),
            "ratio_to_lod0": round(base.triangle_count(lod) / max(1, lod0_triangles), 6),
            "bounds_cm": {"minimum": lod_min, "maximum": lod_max, "extent": lod_extent},
            "uv_layers": [layer.name for layer in lod.data.uv_layers],
            "material_slots": [slot.material.name if slot.material else None for slot in lod.material_slots],
        })

    required_features = {
        "faceted_runestone_masses": sorted(obj.name for obj in source_objects if obj.name.startswith("Head_Stone_")),
        "stone_crack_and_rail_system": sorted(obj.name for obj in source_objects if obj.name.startswith(("StoneCrack_", "StoneRail_", "StoneStrike"))),
        "layered_architectural_core": sorted(obj.name for obj in source_objects if obj.name.startswith(("CoreShield_", "CoreArchitecturalBrace_", "Head_Axle"))),
        "engraved_shaft": sorted(obj.name for obj in source_objects if obj.name.startswith(("Shaft_Engraved", "Shaft_Rune"))),
        "dense_crossed_grip": sorted(obj.name for obj in source_objects if obj.name.startswith("Grip_Wrap_")),
        "compact_faceted_pommel": sorted(obj.name for obj in source_objects if obj.name.startswith(("PommelBand_", "PommelPlate_", "PommelFrame_", "PommelRune_"))),
    }
    manifest = {
        "schema": "aerathea.dcc_game_ready_candidate.v3",
        "asset_id": ASSET_ID,
        "revision": REVISION,
        "contract_id": CONTRACT_ID,
        "artifact_status": "candidate",
        "pipeline_status": "DCC source candidate pending matched-view visual audit",
        "authority": {
            "numeric": ["asset_spec.json", "dimensions_cm.csv"],
            "primary_projected_visual": "large 3/4 concept render under SOURCE_AUTHORITY_A03_PIXEL_OVERRIDE.json",
            "secondary": "normalized structure only under VISUAL_FIDELITY_A03_CROSS_VIEW_CONFLICT_AUDIT.json",
            "measurement_sha256": sha256(MEASUREMENT_PATH),
            "conflict_audit_sha256": sha256(CONFLICT_PATH),
            "a01_a02_geometry_used": False,
        },
        "coordinate_frame": {
            "x": "head width, right positive", "y": "head depth, back positive", "z": "overall length, up positive",
            "origin": "bottom center of pommel at Z=0",
        },
        "world_bounds_cm": {"minimum": minimum, "maximum": maximum, "extent": extent},
        "source_component_count": len(source_objects),
        "source_triangles": source_triangles,
        "lods": lod_stats,
        "materials": base.MATERIAL_ORDER,
        "textures": sorted(str(path.relative_to(ROOT)) for path in TEXTURE_ROOT.glob("*.png")),
        "required_feature_groups": required_features,
        "collision": [{"object": obj.name, "triangles": base.triangle_count(obj), "role": obj["Aerathea.CollisionRole"]} for obj in collisions],
        "contacts": {
            "shaft_head": {"shaft_top_z_cm": 132, "head_bottom_z_cm": 132, "status": "pass"},
            "shaft_pommel": {"overlap_cm": 4, "status": "pass"},
            "grip": {"interval_z_cm": [18, 60], "length_cm": 42, "status": "pass"},
        },
        "outputs": [{"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "bytes": path.stat().st_size} for path in [BLEND_PATH, *export_paths]],
        "final_visual_approval": "pending Flamestrike",
        "unreal_import_authorized": False,
        "fully_game_ready": False,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(MANIFEST_PATH)
    print(f"source_components={len(source_objects)} source_triangles={source_triangles}")
    print(f"lod_triangles={[base.triangle_count(lod) for lod in lods]}")
    print(f"bounds_cm={extent}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
