import math
from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_ReviewIsland"

SOURCE = ROOT / "SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady.fbx"
MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady"
TEXTURE_BASE = "/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady"
TEXTURE_PATHS = {
    "{}/T_GIA_BloodAxeCairnSlabCluster_A01_A1Projection_BC".format(TEXTURE_BASE): (300, 300),
    "{}/T_GIA_BloodAxeCairnSlabCluster_A01_GameReadySide_BC".format(TEXTURE_BASE): (1024, 1024),
    "{}/T_GIA_BloodAxeCairnSlabCluster_A01_GameReadySide_N".format(TEXTURE_BASE): (1024, 1024),
    "{}/T_GIA_BloodAxeCairnSlabCluster_A01_GameReadySide_ORM".format(TEXTURE_BASE): (1024, 1024),
}
MATERIAL_PATHS = [
    "/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairn_GameReady_A1Projection_A01",
    "/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairn_GameReady_StoneSide_A01",
    "/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairn_GameReady_AshMudSide_A01",
    "/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairn_GameReady_RawhideSide_A01",
]
MATERIAL_INSTANCE_PATHS = [
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_GameReady_A1Projection",
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_GameReady_StoneSide",
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_GameReady_AshMud",
    "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_GameReady_Rawhide",
]

ACTOR_LABEL = "AET_REVIEW_CurrentAsset_BloodAxeCairn_A01"
EXPECTED_LOCATION = unreal.Vector(0.0, 0.0, 8.0)
EXPECTED_YAW = -18.0
EXPECTED_TAGS = [
    "AET_REVIEW_ISLAND",
    "AET_REVIEW_TARGET",
]

COMMON_METADATA = {
    "Aerathea.StaticMesh.Package": "SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady",
    "Aerathea.StaticMesh.Status": "unreal_game_ready_candidate_pending_flamestrike_review",
    "Aerathea.StaticMesh.SourceMethod": "hand_traced_a01_shells_with_concept_projected_front_uvs_and_inferred_side_back_forms",
    "Aerathea.StaticMesh.VisualCanonSource": "VC_GIA_BloodAxe_CairnStones_A01_A1_Crop",
    "Aerathea.StaticMesh.TextureProjection": "a01_concept_projected_front_uvs_on_true_3d_mesh_faces",
    "Aerathea.StaticMesh.CollisionPolicy": "ucx_and_broad_simple_static_prop_collision",
    "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
    "Aerathea.StaticMesh.DCCGameReadyCandidate": "true",
    "Aerathea.StaticMesh.UnrealImportTested": "true",
    "Aerathea.StaticMesh.ReviewIslandPlaced": "true",
    "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_review",
}


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


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


def vector_distance(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z
    return math.sqrt((dx * dx) + (dy * dy) + (dz * dz))


def rotation_yaw(rotation):
    for name in ("yaw", "Yaw"):
        if hasattr(rotation, name):
            return float(getattr(rotation, name))
    try:
        return float(rotation.get_editor_property("yaw"))
    except Exception:
        return 0.0


def validate_source_fbx(failures):
    if not SOURCE.exists():
        failures.append("Missing source FBX {}".format(SOURCE))
    elif SOURCE.stat().st_size <= 0:
        failures.append("Source FBX is empty {}".format(SOURCE))


def validate_textures(failures):
    for texture_path, min_size in TEXTURE_PATHS.items():
        texture = unreal.load_asset(texture_path)
        if texture is None:
            failures.append("{} failed to load".format(texture_path))
            continue
        get_x = getattr(texture, "blueprint_get_size_x", None)
        get_y = getattr(texture, "blueprint_get_size_y", None)
        if callable(get_x) and callable(get_y):
            width = get_x()
            height = get_y()
            if width < min_size[0] or height < min_size[1]:
                failures.append("{} has texture size {}x{}, expected at least {}x{}".format(texture_path, width, height, min_size[0], min_size[1]))


def validate_materials(failures):
    for material_path in MATERIAL_PATHS:
        material = unreal.load_asset(material_path)
        if material is None:
            failures.append("{} failed to load".format(material_path))

    for index, instance_path in enumerate(MATERIAL_INSTANCE_PATHS):
        instance = unreal.load_asset(instance_path)
        if instance is None:
            failures.append("{} failed to load".format(instance_path))
            continue
        try:
            parent = instance.get_editor_property("parent")
        except Exception:
            parent = None
        if parent is None:
            failures.append("{} has no parent material".format(instance_path))
        elif asset_path_without_object(parent) != MATERIAL_PATHS[index]:
            failures.append("{} parent is {}, expected {}".format(instance_path, parent.get_path_name(), MATERIAL_PATHS[index]))


def material_slots(mesh):
    try:
        return list(mesh.get_editor_property("static_materials"))
    except Exception:
        return []


def validate_mesh_material_slots(failures, mesh):
    slots = material_slots(mesh)
    if len(slots) < 4:
        failures.append("{} has {} material slots, expected at least 4".format(MESH_PATH, len(slots)))
    assigned_paths = set()
    for slot in slots:
        material = slot.get_editor_property("material_interface")
        if material is not None:
            assigned_paths.add(asset_path_without_object(material))
    for instance_path in MATERIAL_INSTANCE_PATHS:
        if instance_path not in assigned_paths:
            failures.append("{} is not assigned to any material slot on {}".format(instance_path, MESH_PATH))


def validate_mesh_bounds(failures, mesh, measurements):
    getter = getattr(mesh, "get_bounds", None)
    if not callable(getter):
        measurements.append(("unavailable", "unavailable", "unavailable"))
        return
    try:
        bounds = getter()
        extent = bounds.get_editor_property("box_extent")
    except Exception:
        measurements.append(("unavailable", "unavailable", "unavailable"))
        return
    width = extent.x * 2.0
    depth = extent.y * 2.0
    height = extent.z * 2.0
    measurements.append((height, width, depth))
    if height < 130.0 or height > 190.0:
        failures.append("{} height {:.2f} cm outside expected game-ready cairn envelope".format(MESH_PATH, height))
    if width < 300.0 or width > 390.0:
        failures.append("{} width {:.2f} cm outside expected game-ready cairn envelope".format(MESH_PATH, width))
    if depth < 45.0 or depth > 95.0:
        failures.append("{} depth {:.2f} cm outside expected game-ready cairn envelope".format(MESH_PATH, depth))


def validate_collision_source(failures, mesh):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        try:
            simple_count = subsystem.get_simple_collision_count(mesh)
            convex_count = subsystem.get_convex_collision_count(mesh)
        except Exception as exc:
            failures.append("{} collision count unreadable ({})".format(MESH_PATH, exc))
            return
        if max(int(simple_count), int(convex_count)) < 1:
            failures.append("{} has no simple/convex collision".format(MESH_PATH))
        return

    counter = getattr(unreal.EditorStaticMeshLibrary, "get_simple_collision_count", None)
    if not callable(counter):
        failures.append("No static mesh collision count API is available for {}".format(MESH_PATH))
        return
    try:
        collision_count = counter(mesh)
    except Exception as exc:
        failures.append("{} collision count unreadable ({})".format(MESH_PATH, exc))
        return
    if collision_count is not None and collision_count < 1:
        failures.append("{} has no simple collision".format(MESH_PATH))


def validate_metadata(failures, mesh):
    for tag, expected in COMMON_METADATA.items():
        value = metadata_value(failures, mesh, tag)
        if value is None:
            continue
        if value != expected:
            failures.append("{} metadata {} is {!r}, expected {!r}".format(MESH_PATH, tag, value, expected))


def validate_mesh(failures, measurements):
    mesh = unreal.load_asset(MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(MESH_PATH))
        return None
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        lod_count = subsystem.get_lod_count(mesh)
    else:
        lod_count = unreal.EditorStaticMeshLibrary.get_lod_count(mesh)
    if lod_count < 4:
        failures.append("{} has fewer than 4 LODs".format(MESH_PATH))
    validate_mesh_material_slots(failures, mesh)
    validate_mesh_bounds(failures, mesh, measurements)
    validate_collision_source(failures, mesh)
    validate_metadata(failures, mesh)
    return mesh


def validate_actor(failures, mesh):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        failures.append("Failed to load level {}".format(LEVEL_PATH))
        return
    actor = find_actor_by_label(ACTOR_LABEL)
    if actor is None:
        failures.append("Missing review island actor {}".format(ACTOR_LABEL))
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

    expected_material_paths = set(MATERIAL_INSTANCE_PATHS)
    override_paths = set()
    for index in range(len(material_slots(mesh)) if mesh is not None else 0):
        material = component.get_material(index)
        if material is not None:
            override_paths.add(asset_path_without_object(material))
    for instance_path in expected_material_paths:
        if instance_path not in override_paths:
            failures.append("{} actor component does not use material override {}".format(ACTOR_LABEL, instance_path))


def main():
    failures = []
    measurements = []
    validate_source_fbx(failures)
    validate_textures(failures)
    validate_materials(failures)
    mesh = validate_mesh(failures, measurements)
    validate_actor(failures, mesh)

    if failures:
        for failure in failures:
            unreal.log_error(failure)
        raise RuntimeError("Blood Axe game-ready cairn validation failed with {} issue(s)".format(len(failures)))

    height, width, depth = measurements[0] if measurements else ("unavailable", "unavailable", "unavailable")
    unreal.log(
        "Blood Axe game-ready cairn validation passed: {:.2f}h x {:.2f}w x {:.2f}d cm, 4 LODs, 4 materials, 4 textures, review island actor {}, broad collision enabled.".format(
            height,
            width,
            depth,
            ACTOR_LABEL,
        )
    )


if __name__ == "__main__":
    main()
