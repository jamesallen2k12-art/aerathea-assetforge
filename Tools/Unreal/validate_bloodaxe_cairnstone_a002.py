import json
import math
from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"

ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A002"
DCC_PACKAGE = "SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01"
SOURCE_DIR = ROOT / "SourceAssets/Exports/Props/Giants/BloodAxe/Cairns" / DCC_PACKAGE
SOURCE = SOURCE_DIR / "{}.fbx".format(DCC_PACKAGE)
LOD_SOURCES = [
    SOURCE_DIR / "{}_LOD0.fbx".format(DCC_PACKAGE),
    SOURCE_DIR / "{}_LOD1.fbx".format(DCC_PACKAGE),
    SOURCE_DIR / "{}_LOD2.fbx".format(DCC_PACKAGE),
    SOURCE_DIR / "{}_LOD3.fbx".format(DCC_PACKAGE),
]
UCX_SOURCE = SOURCE_DIR / "{}_UCX.fbx".format(DCC_PACKAGE)
DCC_AUDIT = ROOT / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Audit.json"
DCC_MANIFEST = ROOT / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Manifest.json"

MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002"
TEXTURE_PATH = "/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002/T_GIA_BloodAxeCairnstone_A002_SourceTemplate_BC"
MATERIAL_INSTANCE_PATHS = [
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnstone_A002_SourceTemplate",
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnstone_A002_InferredHidden",
]

ACTOR_LABEL = "AET_PROD_GIA_BloodAxeCairnstone_A002"
EXPECTED_LOCATION = unreal.Vector(12480.0, 10360.0, 0.0)
EXPECTED_YAW = -18.0
EXPECTED_TAGS = [
    "AET_FIRST_SLICE",
    "AET_BLOODAXE_CAIRNSTONE_A002_REVIEW",
    "AET_STATIC_REVIEW_TARGET",
]

EXPECTED_METADATA = {
    "Aerathea.StaticMesh.Package": ASSET_NAME,
    "Aerathea.StaticMesh.DCCPackage": DCC_PACKAGE,
    "Aerathea.StaticMesh.DCCManifest": "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Manifest.json",
    "Aerathea.StaticMesh.DCCAudit": "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Audit.json",
    "Aerathea.StaticMesh.DCCAuditStatus": "pass",
    "Aerathea.StaticMesh.CollisionPolicy": "broad_simple_static_prop_collision",
    "Aerathea.StaticMesh.CollisionImportSource": "generated_box_fallback_dcc_ucx_source_verified",
    "Aerathea.StaticMesh.CollisionSourceFBX": "SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_UCX.fbx",
    "Aerathea.StaticMesh.CollisionFallbackRecorded": "true",
    "Aerathea.StaticMesh.ExpectedCollisionProxyCount": "3",
    "Aerathea.StaticMesh.ComplexAsSimple": "false",
    "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_review",
    "Aerathea.StaticMesh.FullyGameReady": "false",
    "Aerathea.StaticMesh.A001A02SourceAuthority": "false",
}


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def read_json(failures, path):
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except Exception as exc:
        failures.append("{} is unreadable JSON ({})".format(path, exc))
        return None


def vector_distance(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def rotation_yaw(rotation):
    for name in ("yaw", "Yaw"):
        if hasattr(rotation, name):
            return float(getattr(rotation, name))
    try:
        return float(rotation.get_editor_property("yaw"))
    except Exception:
        return 0.0


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def metadata_value(failures, asset, tag):
    getter = getattr(unreal.EditorAssetLibrary, "get_metadata_tag", None)
    if not callable(getter):
        failures.append("EditorAssetLibrary.get_metadata_tag is unavailable")
        return None
    try:
        value = getter(asset, tag)
    except Exception as exc:
        failures.append("{} metadata {} unreadable ({})".format(asset.get_path_name(), tag, exc))
        return None
    return "" if value is None else str(value)


def material_slots(mesh):
    try:
        return list(mesh.get_editor_property("static_materials"))
    except Exception:
        return []


def validate_source_files(failures):
    for source in [SOURCE, UCX_SOURCE, DCC_AUDIT, DCC_MANIFEST] + LOD_SOURCES:
        if not source.exists():
            failures.append("Missing source file {}".format(source))
        elif source.stat().st_size <= 0:
            failures.append("Source file is empty {}".format(source))
    audit = read_json(failures, DCC_AUDIT) if DCC_AUDIT.exists() else None
    if audit is not None and audit.get("status") != "pass":
        failures.append("{} status is {!r}, expected 'pass'".format(DCC_AUDIT, audit.get("status")))
    manifest = read_json(failures, DCC_MANIFEST) if DCC_MANIFEST.exists() else None
    if manifest is not None:
        proxies = manifest.get("collision_proxies") or []
        if len(proxies) != 3:
            failures.append("{} collision proxy count is {}, expected 3".format(DCC_MANIFEST, len(proxies)))


def validate_texture_and_materials(failures):
    texture = unreal.load_asset(TEXTURE_PATH)
    if texture is None:
        failures.append("{} failed to load".format(TEXTURE_PATH))
    for material_path in MATERIAL_INSTANCE_PATHS:
        material = unreal.load_asset(material_path)
        if material is None:
            failures.append("{} failed to load".format(material_path))


def validate_collision(failures, mesh):
    simple_count = 0
    convex_count = 0
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        try:
            simple_count = int(subsystem.get_simple_collision_count(mesh))
            convex_count = int(subsystem.get_convex_collision_count(mesh))
        except Exception as exc:
            failures.append("{} collision count unreadable ({})".format(MESH_PATH, exc))
            return
    else:
        counter = getattr(unreal.EditorStaticMeshLibrary, "get_simple_collision_count", None)
        if callable(counter):
            try:
                simple_count = int(counter(mesh))
            except Exception as exc:
                failures.append("{} collision count unreadable ({})".format(MESH_PATH, exc))
                return
        else:
            failures.append("No static mesh collision count API is available for {}".format(MESH_PATH))
            return
    if max(simple_count, convex_count) < 1:
        failures.append("{} has no simple/convex collision".format(MESH_PATH))


def validate_metadata(failures, mesh):
    for tag, expected in EXPECTED_METADATA.items():
        value = metadata_value(failures, mesh, tag)
        if value is None:
            continue
        if value != expected:
            failures.append("{} metadata {} is {!r}, expected {!r}".format(MESH_PATH, tag, value, expected))
    status = metadata_value(failures, mesh, "Aerathea.StaticMesh.Status")
    if status and "fully" in status.lower():
        failures.append("{} metadata status claims fully game-ready".format(MESH_PATH))
    simple_count = metadata_value(failures, mesh, "Aerathea.StaticMesh.ImportedSimpleCollisionCount")
    if simple_count is not None:
        try:
            if int(simple_count) < 1:
                failures.append("{} metadata ImportedSimpleCollisionCount is {}, expected >= 1".format(MESH_PATH, simple_count))
        except ValueError:
            failures.append("{} metadata ImportedSimpleCollisionCount is not an integer: {!r}".format(MESH_PATH, simple_count))
    convex_count = metadata_value(failures, mesh, "Aerathea.StaticMesh.ImportedConvexCollisionCount")
    if convex_count is not None:
        try:
            if int(convex_count) < 0:
                failures.append("{} metadata ImportedConvexCollisionCount is {}, expected >= 0".format(MESH_PATH, convex_count))
        except ValueError:
            failures.append("{} metadata ImportedConvexCollisionCount is not an integer: {!r}".format(MESH_PATH, convex_count))


def validate_mesh_material_slots(failures, mesh):
    slots = material_slots(mesh)
    if len(slots) < 1:
        failures.append("{} has no material slots".format(MESH_PATH))
    assigned_paths = set()
    for slot in slots:
        material = slot.get_editor_property("material_interface")
        if material is not None:
            assigned_paths.add(asset_path_without_object(material))
    for material_path in MATERIAL_INSTANCE_PATHS:
        if material_path not in assigned_paths:
            failures.append("{} is not assigned to {}".format(material_path, MESH_PATH))


def validate_mesh(failures):
    mesh = unreal.load_asset(MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(MESH_PATH))
        return None
    if unreal.EditorStaticMeshLibrary.get_lod_count(mesh) < 4:
        failures.append("{} has fewer than 4 LODs".format(MESH_PATH))
    validate_mesh_material_slots(failures, mesh)
    validate_collision(failures, mesh)
    validate_metadata(failures, mesh)
    return mesh


def validate_actor(failures, mesh):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        failures.append("Failed to load level {}".format(LEVEL_PATH))
        return
    actor = find_actor_by_label(ACTOR_LABEL)
    if actor is None:
        failures.append("Missing startup review actor {}".format(ACTOR_LABEL))
        return
    if actor.get_class().get_name() != "StaticMeshActor":
        failures.append("{} class is {}, expected StaticMeshActor".format(ACTOR_LABEL, actor.get_class().get_name()))

    location = actor.get_actor_location()
    if vector_distance(location, EXPECTED_LOCATION) > 1.0:
        failures.append("{} location {} differs from expected {}".format(ACTOR_LABEL, location, EXPECTED_LOCATION))
    yaw = rotation_yaw(actor.get_actor_rotation())
    if abs(yaw - EXPECTED_YAW) > 0.5:
        failures.append("{} yaw {:.2f} differs from expected {:.2f}".format(ACTOR_LABEL, yaw, EXPECTED_YAW))
    tags = {str(tag) for tag in actor.get_editor_property("tags")}
    for tag in EXPECTED_TAGS:
        if tag not in tags:
            failures.append("{} missing tag {}".format(ACTOR_LABEL, tag))

    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        failures.append("{} has no StaticMeshComponent".format(ACTOR_LABEL))
        return
    assigned_mesh = component.get_editor_property("static_mesh")
    if assigned_mesh is None:
        failures.append("{} StaticMeshComponent has no mesh".format(ACTOR_LABEL))
    elif asset_path_without_object(assigned_mesh) != MESH_PATH:
        failures.append("{} mesh is {}, expected {}".format(ACTOR_LABEL, assigned_mesh.get_path_name(), MESH_PATH))
    try:
        if component.get_collision_enabled() != unreal.CollisionEnabled.QUERY_AND_PHYSICS:
            failures.append("{} collision is {}, expected QUERY_AND_PHYSICS".format(ACTOR_LABEL, component.get_collision_enabled()))
    except Exception as exc:
        failures.append("{} collision state unreadable ({})".format(ACTOR_LABEL, exc))
    if mesh is not None and assigned_mesh is not None and assigned_mesh != mesh:
        failures.append("{} actor mesh object differs from loaded mesh object".format(ACTOR_LABEL))


def main():
    failures = []
    validate_source_files(failures)
    validate_texture_and_materials(failures)
    mesh = validate_mesh(failures)
    validate_actor(failures, mesh)

    if failures:
        for failure in failures:
            unreal.log_error(failure)
        raise RuntimeError("A002 Unreal import validation failed with {} issue(s)".format(len(failures)))

    unreal.log("A002 Unreal import validation passed: 4 LODs, simple collision, materials, startup actor, and metadata present.")


if __name__ == "__main__":
    main()
