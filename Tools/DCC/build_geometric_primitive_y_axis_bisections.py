#!/usr/bin/env python3
"""Build the P01C geometric primitive Y-axis bisection board.

This training proof cuts every approved P01 primitive with the same plane:
the X/Z plane through the origin, perpendicular to the Y axis.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "P01C_YAxis90BisectionBoard"
DOC_ROOT = ROOT / "docs" / "assets" / "training" / "geometric_primitives"
REVIEW_ROOT = ROOT / "Saved" / "Automation" / "DCC" / "GeometricPrimitives"
TILE_ROOT = REVIEW_ROOT / "y_axis_bisected_tiles"
BLEND_ROOT = ROOT / "SourceAssets" / "Blender" / "Props" / "Training" / "GeometricPrimitives" / ASSET_NAME
DOC_IMAGE = DOC_ROOT / f"{ASSET_NAME}.png"
REVIEW_IMAGE = REVIEW_ROOT / f"{ASSET_NAME}.png"

sys.path.insert(0, str(ROOT))

from Tools.DCC.build_geometric_primitive_bisections import (  # noqa: E402
    build_materials,
    compose_contact_sheet,
    make_bisected_pair,
    mesh_world_bounds,
)
from Tools.DCC.build_geometric_primitive_fundamentals import (  # noqa: E402
    add_cone,
    add_cube,
    add_cylinder,
    add_dodecahedron,
    add_ground_plane,
    add_hexagonal_prism,
    add_icosahedron,
    add_octa_cut,
    add_oval_egg,
    add_parallelepiped,
    add_pentagonal_trapezohedron,
    add_rectangular_slab,
    add_sphere,
    add_tetrahedron,
    add_zocchihedron,
    configure_scene,
    ensure_dir,
    look_at,
    render,
)
from Tools.DCC.build_next_slice_assets import clear_scene, setup_scene  # noqa: E402


def y_axis_90_bisect_plane(_source: bpy.types.Object) -> tuple[Vector, Vector, str]:
    return Vector((0.0, 0.0, 0.0)), Vector((0.0, 1.0, 0.0)), "90 degree cut to Y axis; X/Z plane through center"


def render_y_axis_tile(
    camera: bpy.types.Object,
    objects: tuple[bpy.types.Object, bpy.types.Object],
    base: bpy.types.Object,
    path: Path,
    ortho_scale: float,
) -> None:
    visible = {objects[0], objects[1], base}
    state = [(item, item.hide_render, item.hide_viewport) for item in bpy.context.scene.objects]
    try:
        for item in bpy.context.scene.objects:
            if item.type == "MESH" and item not in visible:
                item.hide_render = True
                item.hide_viewport = True
        minimum, maximum = mesh_world_bounds(objects)
        center = (minimum + maximum) * 0.5
        span = maximum - minimum
        camera.data.ortho_scale = max(ortho_scale, max(span.x, span.y, span.z) * 1.34)
        target = Vector((center.x, center.y, center.z + 0.05))
        camera.location = (center.x + 2.65, center.y - 7.25, center.z + 3.7)
        look_at(camera, target)
        render(camera, path, (620, 460))
    finally:
        for item, hide_render, hide_viewport in state:
            item.hide_render = hide_render
            item.hide_viewport = hide_viewport


def main() -> None:
    clear_scene()
    setup_scene()
    materials = build_materials("P01C")
    base = add_ground_plane(materials["base"])
    base.name = "P01C_NeutralReviewBase"

    build_specs = [
        ("Cube", lambda: add_cube("P01C_Cube_Source", (0.0, 0.0, 1.0), materials["cube"]), 3.8),
        ("Slab", lambda: add_rectangular_slab("P01C_RectangularSlab_Source", (0.0, 0.0, 0.7), materials["slab"]), 4.4),
        ("Parallelepiped", lambda: add_parallelepiped("P01C_Parallelepiped_Source", (0.0, 0.0, 1.2), materials["para"]), 4.4),
        ("Hex Prism", lambda: add_hexagonal_prism("P01C_HexagonalPrism_Source", (0.0, 0.0, 1.08), materials["hex"]), 4.0),
        ("Cylinder", lambda: add_cylinder("P01C_Cylinder_Source", (0.0, 0.0, 1.1), materials["cylinder"]), 4.0),
        ("Zocchihedron", lambda: add_zocchihedron("P01C_Zocchihedron_Source", (0.0, 0.0, 1.1), materials["zocchi"]), 4.0),
        ("Tetrahedron", lambda: add_tetrahedron("P01C_Tetrahedron_Source", (0.0, 0.0, 1.0), materials["tetra"]), 4.1),
        ("Octa Cut", lambda: add_octa_cut("P01C_OctaCut_Source", (0.0, 0.0, 1.25), materials["octa"]), 4.1),
        ("Icosahedron", lambda: add_icosahedron("P01C_Icosahedron_Source", (0.0, 0.0, 1.25), materials["ico"]), 4.2),
        ("Dodecahedron", lambda: add_dodecahedron("P01C_Dodecahedron_Source", (0.0, 0.0, 1.25), materials["dodeca"]), 4.2),
        ("D10 Trapezohedron", lambda: add_pentagonal_trapezohedron("P01C_PentagonalTrapezohedron_Source", (0.0, 0.0, 1.25), materials["d10"]), 4.1),
        ("Cone", lambda: add_cone("P01C_Cone_Source", (0.0, 0.0, 1.12), materials["cone"]), 4.0),
        ("Smooth Sphere", lambda: add_sphere("P01C_SmoothSphere_Source", (0.0, 0.0, 1.08), materials["sphere"]), 4.0),
        ("Oval Egg", lambda: add_oval_egg("P01C_OvalEgg_Source", (0.0, 0.0, 1.24), materials["egg"]), 4.0),
    ]

    camera = configure_scene()
    tile_specs: list[tuple[str, Path]] = []
    for index, (label, builder, ortho_scale) in enumerate(build_specs, 1):
        source = builder()
        halves = make_bisected_pair(
            source,
            label,
            materials["cut"],
            y_axis_90_bisect_plane,
            object_prefix="P01C",
            primitive_stage="P01C Y-axis 90 degree bisection",
            presentation_note="All halves cut perpendicular to the Y axis and opened 30 degrees for cut-face review.",
        )
        for obj in halves:
            obj["Aerathea.TrainingLane"] = "geometric_primitive_to_cairnstone"
            obj["Aerathea.Stage"] = "P01C Y-Axis 90 Degree Bisection Board"
        tile_path = TILE_ROOT / f"P01C_{index:02d}_{label.replace(' ', '_')}_YAxis90_Bisected.png"
        render_y_axis_tile(camera, halves, base, tile_path, ortho_scale)
        tile_specs.append((label, tile_path))

    compose_contact_sheet(
        tile_specs,
        REVIEW_IMAGE,
        title="P01C Y-Axis 90 Degree Bisection Board",
        subtitle="all primitives bisected by the X/Z plane: 90 degrees to the Y axis",
    )
    ensure_dir(DOC_IMAGE.parent)
    shutil.copyfile(REVIEW_IMAGE, DOC_IMAGE)

    blend_path = BLEND_ROOT / f"{ASSET_NAME}.blend"
    ensure_dir(blend_path.parent)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"P01C Y-axis bisection board written: {DOC_IMAGE}")


if __name__ == "__main__":
    main()
