#!/usr/bin/env python3
"""Audit downloaded static-asset reference packages with Blender.

Run with:
    blender --background --python Tools/DCC/audit_reference_static_assets.py

The script reads reference assets from the ignored Saved/AssetForgeResearch
area and writes a JSON report there. It is for benchmarking packaging and
technical production patterns only; do not copy reference art into Aerathea.
"""

from __future__ import annotations

import json
from pathlib import Path

import bpy


ROOT = Path(__file__).resolve().parents[2]
REFERENCE_ROOT = ROOT / "Saved" / "AssetForgeResearch" / "benchmarks" / "reference_assets" / "unpacked"
REPORT_ROOT = ROOT / "Saved" / "AssetForgeResearch" / "benchmarks" / "reference_assets" / "reports"
REPORT_PATH = REPORT_ROOT / "static_asset_reference_audit.json"

SAMPLES = [
    {
        "id": "kenney_graveyard_rocks",
        "source": "Kenney Graveyard Kit 5.0",
        "license": "CC0",
        "path": REFERENCE_ROOT / "kenney_graveyard-kit_5.0" / "Models" / "OBJ format" / "rocks.obj",
    },
    {
        "id": "kenney_graveyard_gravestone_broken",
        "source": "Kenney Graveyard Kit 5.0",
        "license": "CC0",
        "path": REFERENCE_ROOT / "kenney_graveyard-kit_5.0" / "Models" / "OBJ format" / "gravestone-broken.obj",
    },
    {
        "id": "kenney_graveyard_stone_wall_damaged",
        "source": "Kenney Graveyard Kit 5.0",
        "license": "CC0",
        "path": REFERENCE_ROOT / "kenney_graveyard-kit_5.0" / "Models" / "OBJ format" / "stone-wall-damaged.obj",
    },
    {
        "id": "kenney_modular_dungeon_template_wall",
        "source": "Kenney Modular Dungeon Kit 2.1",
        "license": "CC0",
        "path": REFERENCE_ROOT / "kenney_modular-dungeon-kit_1.0" / "Models" / "OBJ format" / "template-wall.obj",
    },
    {
        "id": "kenney_modular_dungeon_gate",
        "source": "Kenney Modular Dungeon Kit 2.1",
        "license": "CC0",
        "path": REFERENCE_ROOT / "kenney_modular-dungeon-kit_1.0" / "Models" / "OBJ format" / "gate.obj",
    },
    {
        "id": "khronos_lantern_gltf",
        "source": "Khronos glTF Sample Models Lantern",
        "license": "CC0",
        "path": REFERENCE_ROOT / "khronos_lantern_gltf" / "Lantern.gltf",
    },
]


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    for mesh in list(bpy.data.meshes):
        bpy.data.meshes.remove(mesh)
    for material in list(bpy.data.materials):
        bpy.data.materials.remove(material)
    for image in list(bpy.data.images):
        bpy.data.images.remove(image)


def import_asset(path: Path) -> None:
    suffix = path.suffix.lower()
    if suffix == ".fbx":
        bpy.ops.import_scene.fbx(filepath=str(path))
    elif suffix == ".obj":
        bpy.ops.import_scene.obj(filepath=str(path))
    elif suffix in {".gltf", ".glb"}:
        bpy.ops.import_scene.gltf(filepath=str(path))
    else:
        raise ValueError(f"Unsupported reference format: {path}")


def texture_uri(gltf: dict[str, object], texture_info: dict[str, object] | None) -> str:
    if not texture_info:
        return ""
    textures = gltf.get("textures", [])
    images = gltf.get("images", [])
    if not isinstance(textures, list) or not isinstance(images, list):
        return ""
    texture_index = int(texture_info.get("index", -1))
    if texture_index < 0 or texture_index >= len(textures):
        return ""
    texture = textures[texture_index]
    if not isinstance(texture, dict):
        return ""
    image_index = int(texture.get("source", -1))
    if image_index < 0 or image_index >= len(images):
        return ""
    image = images[image_index]
    if not isinstance(image, dict):
        return ""
    return str(image.get("uri", ""))


def audit_gltf(path: Path) -> dict[str, object]:
    gltf = json.loads(path.read_text(encoding="utf-8"))
    accessors = gltf.get("accessors", [])
    meshes = gltf.get("meshes", [])
    materials = gltf.get("materials", [])
    if not isinstance(accessors, list):
        accessors = []
    if not isinstance(meshes, list):
        meshes = []
    if not isinstance(materials, list):
        materials = []

    total_triangles = 0
    total_vertices = 0
    primitive_reports: list[dict[str, object]] = []
    for mesh_index, mesh in enumerate(meshes):
        if not isinstance(mesh, dict):
            continue
        primitives = mesh.get("primitives", [])
        if not isinstance(primitives, list):
            continue
        for primitive_index, primitive in enumerate(primitives):
            if not isinstance(primitive, dict):
                continue
            mode = int(primitive.get("mode", 4))
            attributes = primitive.get("attributes", {})
            position_index = attributes.get("POSITION", -1) if isinstance(attributes, dict) else -1
            vertices = 0
            if isinstance(position_index, int) and 0 <= position_index < len(accessors):
                accessor = accessors[position_index]
                if isinstance(accessor, dict):
                    vertices = int(accessor.get("count", 0))
            indices_index = primitive.get("indices", -1)
            index_count = 0
            if isinstance(indices_index, int) and 0 <= indices_index < len(accessors):
                accessor = accessors[indices_index]
                if isinstance(accessor, dict):
                    index_count = int(accessor.get("count", 0))
            triangles = index_count // 3 if mode == 4 and index_count else vertices // 3 if mode == 4 else 0
            total_vertices += vertices
            total_triangles += triangles
            primitive_reports.append(
                {
                    "mesh_index": mesh_index,
                    "primitive_index": primitive_index,
                    "vertices": vertices,
                    "triangles": triangles,
                    "mode": mode,
                    "material_index": primitive.get("material", -1),
                    "attributes": sorted(attributes.keys()) if isinstance(attributes, dict) else [],
                }
            )

    material_reports: list[dict[str, object]] = []
    for material_index, material in enumerate(materials):
        if not isinstance(material, dict):
            continue
        pbr = material.get("pbrMetallicRoughness", {})
        if not isinstance(pbr, dict):
            pbr = {}
        material_reports.append(
            {
                "index": material_index,
                "name": material.get("name", f"Material_{material_index}"),
                "base_color_texture": texture_uri(gltf, pbr.get("baseColorTexture") if isinstance(pbr.get("baseColorTexture"), dict) else None),
                "metallic_roughness_texture": texture_uri(
                    gltf,
                    pbr.get("metallicRoughnessTexture") if isinstance(pbr.get("metallicRoughnessTexture"), dict) else None,
                ),
                "normal_texture": texture_uri(gltf, material.get("normalTexture") if isinstance(material.get("normalTexture"), dict) else None),
                "emissive_texture": texture_uri(gltf, material.get("emissiveTexture") if isinstance(material.get("emissiveTexture"), dict) else None),
                "alpha_mode": material.get("alphaMode", "OPAQUE"),
            }
        )
    return {
        "mesh_object_count": len(meshes),
        "total_triangles": total_triangles,
        "total_vertices": total_vertices,
        "material_count": len(materials),
        "materials": material_reports,
        "objects": primitive_reports,
        "buffer_count": len(gltf.get("buffers", [])) if isinstance(gltf.get("buffers", []), list) else 0,
        "image_count": len(gltf.get("images", [])) if isinstance(gltf.get("images", []), list) else 0,
        "texture_count": len(gltf.get("textures", [])) if isinstance(gltf.get("textures", []), list) else 0,
    }


def mesh_triangles(obj: bpy.types.Object) -> int:
    if obj.type != "MESH":
        return 0
    return sum(max(1, len(poly.vertices) - 2) for poly in obj.data.polygons)


def texture_paths(material: bpy.types.Material) -> list[str]:
    paths: list[str] = []
    if not material.use_nodes:
        return paths
    for node in material.node_tree.nodes:
        if node.type != "TEX_IMAGE" or node.image is None:
            continue
        source = node.image.filepath or node.image.filepath_raw or node.image.name
        if source and source not in paths:
            paths.append(source)
    return sorted(paths)


def material_report() -> list[dict[str, object]]:
    reports: list[dict[str, object]] = []
    for material in sorted(bpy.data.materials, key=lambda mat: mat.name):
        reports.append(
            {
                "name": material.name,
                "uses_nodes": bool(material.use_nodes),
                "texture_paths": texture_paths(material),
            }
        )
    return reports


def object_report() -> list[dict[str, object]]:
    reports: list[dict[str, object]] = []
    for obj in sorted(bpy.context.scene.objects, key=lambda item: item.name):
        if obj.type != "MESH":
            continue
        reports.append(
            {
                "name": obj.name,
                "triangles": mesh_triangles(obj),
                "vertices": len(obj.data.vertices),
                "polygons": len(obj.data.polygons),
                "uv_layers": [uv.name for uv in obj.data.uv_layers],
                "material_slots": [slot.material.name if slot.material else "" for slot in obj.material_slots],
                "dimensions": [round(value, 4) for value in obj.dimensions],
            }
        )
    return reports


def audit_sample(sample: dict[str, object]) -> dict[str, object]:
    clear_scene()
    path = Path(sample["path"])
    result: dict[str, object] = {
        "id": sample["id"],
        "source": sample["source"],
        "license": sample["license"],
        "path": str(path.relative_to(ROOT)),
        "exists": path.exists(),
    }
    if not path.exists():
        result["error"] = "missing reference file"
        return result
    if path.suffix.lower() == ".gltf":
        result.update(audit_gltf(path))
        result["audit_method"] = "gltf_json_parse"
        return result

    import_asset(path)
    objects = object_report()
    result.update(
        {
            "mesh_object_count": len(objects),
            "total_triangles": sum(int(obj["triangles"]) for obj in objects),
            "total_vertices": sum(int(obj["vertices"]) for obj in objects),
            "material_count": len(bpy.data.materials),
            "materials": material_report(),
            "objects": objects,
        }
    )
    return result


def main() -> None:
    REPORT_ROOT.mkdir(parents=True, exist_ok=True)
    report = {
        "purpose": "Static asset benchmark audit for Aerathea production process; reference art remains external and is not visual canon.",
        "samples": [audit_sample(sample) for sample in SAMPLES],
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
