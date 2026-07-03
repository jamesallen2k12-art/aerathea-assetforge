import json
import time
import traceback
from datetime import datetime
from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
RUN_STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
DESTINATION = "/Game/Aerathea/Developer/AssetForgeResearch/ImportValidation/Run_{}".format(RUN_STAMP)
OUTPUT_DIR = ROOT / "Saved/AssetForgeResearch/benchmarks/outputs/unreal/import_validation"
OUTPUT_JSON = OUTPUT_DIR / "assetforge_cairn_repaired_unreal_import_validation_{}.json".format(RUN_STAMP)
OUTPUT_MD = OUTPUT_DIR / "assetforge_cairn_repaired_unreal_import_validation_{}.md".format(RUN_STAMP)

INPUTS = [
    {
        "id": "cairn_a01_sculpted_v4_dcc_multiview_mesh_decimated_20000_repaired",
        "budget": "20k repaired GLB",
        "source": ROOT
        / "Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/repaired/cairn_a01_sculpted_v4_dcc_multiview_mesh_decimated_20000_repaired.glb",
        "expected_faces": 20000,
    },
    {
        "id": "cairn_a01_sculpted_v4_dcc_multiview_mesh_decimated_50000_repaired",
        "budget": "50k repaired GLB",
        "source": ROOT
        / "Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/repaired/cairn_a01_sculpted_v4_dcc_multiview_mesh_decimated_50000_repaired.glb",
        "expected_faces": 50000,
    },
]


def safe_call(label, fallback, fn):
    try:
        return fn()
    except Exception as exc:
        unreal.log_warning("{} unavailable: {}".format(label, exc))
        return fallback


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def delete_temp_destination():
    if unreal.EditorAssetLibrary.does_directory_exist(DESTINATION):
        unreal.EditorAssetLibrary.delete_directory(DESTINATION)


def import_source(entry):
    if not entry["source"].exists():
        raise RuntimeError("Missing source GLB: {}".format(entry["source"]))

    asset_name = "SM_AFG_{}".format(entry["expected_faces"])
    task = unreal.AssetImportTask()
    task.set_editor_property("filename", str(entry["source"]))
    task.set_editor_property("destination_path", DESTINATION)
    task.set_editor_property("destination_name", asset_name)
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)

    start = time.time()
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    elapsed = time.time() - start

    imported_paths = safe_call(
        "AssetImportTask.imported_object_paths",
        [],
        lambda: list(task.get_editor_property("imported_object_paths")),
    )
    return elapsed, imported_paths


def list_static_meshes():
    paths = unreal.EditorAssetLibrary.list_assets(DESTINATION, recursive=True, include_folder=False)
    meshes = []
    for path in paths:
        asset = unreal.load_asset(path)
        if asset is not None and asset.get_class().get_name() == "StaticMesh":
            meshes.append(asset)
    return meshes


def lod_count(mesh):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        return safe_call("StaticMeshEditorSubsystem.get_lod_count", None, lambda: int(subsystem.get_lod_count(mesh)))
    return safe_call("EditorStaticMeshLibrary.get_lod_count", None, lambda: int(unreal.EditorStaticMeshLibrary.get_lod_count(mesh)))


def collision_counts(mesh):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        return {
            "simple": safe_call("StaticMeshEditorSubsystem.get_simple_collision_count", None, lambda: int(subsystem.get_simple_collision_count(mesh))),
            "convex": safe_call("StaticMeshEditorSubsystem.get_convex_collision_count", None, lambda: int(subsystem.get_convex_collision_count(mesh))),
        }
    counter = getattr(unreal.EditorStaticMeshLibrary, "get_simple_collision_count", None)
    if callable(counter):
        return {
            "simple": safe_call("EditorStaticMeshLibrary.get_simple_collision_count", None, lambda: int(counter(mesh))),
            "convex": None,
        }
    return {"simple": None, "convex": None}


def mesh_bounds(mesh):
    bounds = safe_call("StaticMesh.get_bounds", None, mesh.get_bounds)
    if bounds is None:
        return None
    extent = bounds.get_editor_property("box_extent")
    origin = bounds.get_editor_property("origin")
    return {
        "origin_cm": [float(origin.x), float(origin.y), float(origin.z)],
        "extent_cm": [float(extent.x), float(extent.y), float(extent.z)],
        "size_cm": [float(extent.x * 2.0), float(extent.y * 2.0), float(extent.z * 2.0)],
    }


def material_slots(mesh):
    slots = safe_call("StaticMesh.static_materials", [], lambda: list(mesh.get_editor_property("static_materials")))
    names = []
    assigned = []
    for slot in slots:
        names.append(str(safe_call("StaticMaterial.material_slot_name", "", lambda: slot.get_editor_property("material_slot_name"))))
        material = safe_call("StaticMaterial.material_interface", None, lambda: slot.get_editor_property("material_interface"))
        assigned.append(asset_path_without_object(material) if material is not None else None)
    return {"count": len(slots), "slot_names": names, "assigned_materials": assigned}


def validate_entry(entry):
    entry_dest = "{}/{}".format(DESTINATION, entry["id"])
    unreal.EditorAssetLibrary.make_directory(entry_dest)

    original_destination = DESTINATION
    globals()["DESTINATION"] = entry_dest
    try:
        elapsed, imported_paths = import_source(entry)
        meshes = list_static_meshes()
    finally:
        globals()["DESTINATION"] = original_destination

    failures = []
    if not meshes:
        failures.append("No StaticMesh asset was created by the GLB import.")

    mesh_reports = []
    for mesh in meshes:
        mesh_reports.append(
            {
                "path": asset_path_without_object(mesh),
                "class": mesh.get_class().get_name(),
                "lod_count": lod_count(mesh),
                "bounds": mesh_bounds(mesh),
                "materials": material_slots(mesh),
                "collision": collision_counts(mesh),
            }
        )

    if len(meshes) > 1:
        failures.append("Import created {} StaticMesh assets; expected one primary mesh.".format(len(meshes)))

    primary = mesh_reports[0] if mesh_reports else {}
    material_count = primary.get("materials", {}).get("count")
    if material_count is not None and material_count < 1:
        failures.append("Imported mesh has no material slots.")

    return {
        "id": entry["id"],
        "budget": entry["budget"],
        "source": str(entry["source"]),
        "source_size_bytes": entry["source"].stat().st_size if entry["source"].exists() else None,
        "expected_faces": entry["expected_faces"],
        "destination": entry_dest,
        "import_elapsed_seconds": round(elapsed, 3),
        "imported_object_paths": imported_paths,
        "static_mesh_count": len(meshes),
        "static_meshes": mesh_reports,
        "failures": failures,
        "result": "PASS_IMPORT_VALIDATION" if not failures else "FAIL_IMPORT_VALIDATION",
    }


def write_markdown(report):
    lines = [
        "# AssetForge Unreal Import Validation",
        "",
        "Status: {}".format(report["overall_result"]),
        "Scope: Research-only import validation; no production content promoted.",
        "Run: `{}`".format(report["run_stamp"]),
        "Temporary Unreal destination: `{}`".format(report["temporary_unreal_destination"]),
        "Cleanup: {}".format("complete" if report["temporary_cleanup_complete"] else "incomplete"),
        "",
        "## Results",
        "",
        "| Input | Result | Static Meshes | LODs | Material Slots | Collision | Bounds cm | Import Seconds |",
        "|---|---|---:|---:|---:|---|---|---:|",
    ]

    for item in report["items"]:
        primary = item["static_meshes"][0] if item["static_meshes"] else {}
        bounds = primary.get("bounds") or {}
        size = bounds.get("size_cm")
        size_text = "{:.2f} x {:.2f} x {:.2f}".format(*size) if size else "unavailable"
        materials = primary.get("materials", {})
        collision = primary.get("collision", {})
        collision_text = "simple={}, convex={}".format(collision.get("simple"), collision.get("convex"))
        lines.append(
            "| `{}` | `{}` | {} | {} | {} | {} | {} | {:.3f} |".format(
                item["budget"],
                item["result"],
                item["static_mesh_count"],
                primary.get("lod_count"),
                materials.get("count"),
                collision_text,
                size_text,
                item["import_elapsed_seconds"],
            )
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- The repaired GLBs were imported only into a timestamped research folder under `/Game/Aerathea/Developer/AssetForgeResearch/ImportValidation/`.",
            "- The temporary Unreal folder was deleted after measurement so no research asset is promoted into production `Content/`.",
            "- These remain external-engine research outputs, not DCC source candidates, DCC game-ready candidates, Fully game-ready assets, or Aerathea visual canon.",
            "- Missing generated LODs or collision is expected for raw GLB import and must be handled by a future AssetForge post-process if the pipeline advances.",
            "",
            "JSON report: `{}`".format(OUTPUT_JSON.relative_to(ROOT)),
        ]
    )

    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    delete_temp_destination()
    ensure_directory(DESTINATION)

    report = {
        "run_stamp": RUN_STAMP,
        "temporary_unreal_destination": DESTINATION,
        "scope": "research-only Unreal import validation for repaired AssetForge benchmark GLBs",
        "items": [],
        "temporary_cleanup_complete": False,
        "overall_result": "FAIL_IMPORT_VALIDATION",
    }

    try:
        for entry in INPUTS:
            report["items"].append(validate_entry(entry))
        report["overall_result"] = (
            "PASS_IMPORT_VALIDATION"
            if all(item["result"] == "PASS_IMPORT_VALIDATION" for item in report["items"])
            else "FAIL_IMPORT_VALIDATION"
        )
    except Exception as exc:
        report["exception"] = str(exc)
        report["traceback"] = traceback.format_exc()
        unreal.log_error(report["traceback"])
    finally:
        delete_temp_destination()
        report["temporary_cleanup_complete"] = not unreal.EditorAssetLibrary.does_directory_exist(DESTINATION)
        OUTPUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        write_markdown(report)

    unreal.log("AssetForge Unreal import validation wrote {}".format(OUTPUT_JSON))
    if report["overall_result"] != "PASS_IMPORT_VALIDATION":
        raise RuntimeError("AssetForge Unreal import validation failed; see {}".format(OUTPUT_JSON))


if __name__ == "__main__":
    main()
