"""Render six true fixed-object orthographic views at one identical scale.

Usage:
1. Put all authoritative asset meshes in a Blender collection named ASSET.
2. Open Blender's Scripting workspace and run this file.
3. Renders and render_manifest.json are written beside this script in generated/orthographic_true/.
"""
from pathlib import Path
import json
import bpy
from mathutils import Vector

TARGET_COLLECTION = "SB_ASSET"
RESOLUTION = 2048
MARGIN = 1.15


def objects_recursive(collection):
    result = list(collection.objects)
    for child in collection.children:
        result.extend(objects_recursive(child))
    return [o for o in result if o.type == "MESH"]


def world_bounds(objects):
    points = []
    for obj in objects:
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    if not points:
        raise RuntimeError(f"Collection {TARGET_COLLECTION!r} contains no mesh objects")
    minimum = Vector((min(p.x for p in points), min(p.y for p in points), min(p.z for p in points)))
    maximum = Vector((max(p.x for p in points), max(p.y for p in points), max(p.z for p in points)))
    return minimum, maximum


def ensure_camera(name, center, offset, ortho_scale):
    data = bpy.data.cameras.get(name) or bpy.data.cameras.new(name)
    camera = bpy.data.objects.get(name) or bpy.data.objects.new(name, data)
    if camera.name not in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.link(camera)
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = ortho_scale
    camera.location = center + Vector(offset)
    direction = center - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    return camera


def ensure_lighting(center, distance):
    for name, offset, energy, size in (
        ("Key", (distance, -distance, distance), 1200, 4.0),
        ("Fill", (-distance, -distance * 0.5, distance * 0.5), 700, 5.0),
        ("Rim", (0, distance, distance), 900, 4.0),
    ):
        data = bpy.data.lights.get(name) or bpy.data.lights.new(name, "AREA")
        data.energy = energy
        data.shape = "DISK"
        data.size = size
        obj = bpy.data.objects.get(name) or bpy.data.objects.new(name, data)
        if obj.name not in bpy.context.scene.collection.objects:
            bpy.context.scene.collection.objects.link(obj)
        obj.location = center + Vector(offset)
        obj.rotation_euler = (center - obj.location).to_track_quat("-Z", "Y").to_euler()


def main():
    collection = bpy.data.collections.get(TARGET_COLLECTION)
    if collection is None:
        raise RuntimeError(f"Create a collection named {TARGET_COLLECTION!r}")
    objects = objects_recursive(collection)
    minimum, maximum = world_bounds(objects)
    center = (minimum + maximum) * 0.5
    extent = maximum - minimum
    longest = max(extent)
    ortho_scale = longest * MARGIN
    distance = max(3.0, longest * 3.0)

    output = Path(__file__).resolve().parent.parent / "generated" / "orthographic_true"
    output.mkdir(parents=True, exist_ok=True)

    scene = bpy.context.scene
    scene.render.resolution_x = RESOLUTION
    scene.render.resolution_y = RESOLUTION
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.world.color = (1.0, 1.0, 1.0)
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except Exception:
        try:
            scene.render.engine = "BLENDER_EEVEE"
        except Exception:
            pass

    ensure_lighting(center, distance)
    views = {
        "front": (0, -distance, 0),
        "back": (0, distance, 0),
        "left": (-distance, 0, 0),
        "right": (distance, 0, 0),
        "top": (0, 0, distance),
        "bottom": (0, 0, -distance),
    }
    manifest = {
        "collection": TARGET_COLLECTION,
        "resolution_px": [RESOLUTION, RESOLUTION],
        "ortho_scale_m": ortho_scale,
        "pixels_per_meter": RESOLUTION / ortho_scale,
        "pixels_per_centimeter": RESOLUTION / ortho_scale / 100.0,
        "world_bounds_m": {"minimum": list(minimum), "maximum": list(maximum), "extent": list(extent)},
        "views": {},
    }
    for view, offset in views.items():
        camera = ensure_camera(f"CAM_{view.upper()}", center, offset, ortho_scale)
        scene.camera = camera
        path = output / f"{view}.png"
        scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)
        manifest["views"][view] = {
            "file": path.name,
            "camera_location": list(camera.location),
            "ortho_scale_m": camera.data.ortho_scale,
        }

    (output / "render_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Rendered six true orthographic views to {output}")


if __name__ == "__main__":
    main()
