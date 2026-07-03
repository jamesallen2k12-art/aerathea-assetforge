import math
from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"

SOURCE = ROOT / "SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual.fbx"
MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual"
TEXTURE_PATHS = [
    "/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_BC",
    "/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_N",
    "/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_ORM",
]
PROJECTION_MATERIAL_PATH = "/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairn_Test2ManualProjection_A01"
SIDE_MATERIAL_PATH = "/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairn_Test2ManualSideStone_A01"
PROJECTION_MI_PATH = "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_Projection"
SIDE_MI_PATH = "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_SideStone"

ACTOR_LABEL = "AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual"
EXPECTED_LOCATION = unreal.Vector(12880.0, 10000.0, 0.0)
EXPECTED_YAW = -18.0
EXPECTED_TAGS = [
    "AET_FIRST_SLICE",
    "AET_BLOODAXE_CAIRN_TEST2_MANUAL_REVIEW",
    "AET_STATIC_REVIEW_TARGET",
]

COMMON_METADATA = {
    "Aerathea.StaticMesh.Package": "SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual",
    "Aerathea.StaticMesh.Status": "unreal_game_ready_test2_manual_paint01_pending_flamestrike_reapproval",
    "Aerathea.StaticMesh.SourceMethod": "front_faithful_deep_a01_image_relief_with_inferred_walkaround_depth",
    "Aerathea.StaticMesh.VisualCanonSource": "VC_GIA_BloodAxe_CairnStones_A01_A1_Crop",
    "Aerathea.StaticMesh.TextureProjection": "paint01_regraded_a01_projection_with_authored_albedo_ao_normal",
    "Aerathea.StaticMesh.CollisionPolicy": "broad_ucx_proxy_static_prop",
    "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
    "Aerathea.StaticMesh.FinalArtAuthored": "true",
    "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_reapproval_after_in_game_color_feedback",
    "Aerathea.StaticMesh.ApprovedPass": "A01-Test2-Paint-01",
    "Aerathea.StaticMesh.StartupPlaced": "startup_review_actor",
    "Aerathea.StaticMesh.StartupActor": ACTOR_LABEL,
    "Aerathea.StaticMesh.VisualReview": "test2_manual_paint01_corrective_pass_for_in_game_overbright_feedback",
}


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def normalized(value):
    return str(value).lower()


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
    for texture_path in TEXTURE_PATHS:
        texture = unreal.load_asset(texture_path)
        if texture is None:
            failures.append("{} failed to load".format(texture_path))
            continue
        get_x = getattr(texture, "blueprint_get_size_x", None)
        get_y = getattr(texture, "blueprint_get_size_y", None)
        if callable(get_x) and callable(get_y):
            width = get_x()
            height = get_y()
            if width <= 0 or height <= 0:
                failures.append("{} has invalid texture size {}x{}".format(texture_path, width, height))


def validate_materials(failures):
    projection_parent = unreal.load_asset(PROJECTION_MATERIAL_PATH)
    if projection_parent is None:
        failures.append("{} failed to load".format(PROJECTION_MATERIAL_PATH))
    else:
        try:
            blend_mode = projection_parent.get_editor_property("blend_mode")
            if "masked" not in normalized(blend_mode):
                failures.append("{} blend mode is {}, expected masked".format(PROJECTION_MATERIAL_PATH, blend_mode))
        except Exception as exc:
            failures.append("{} blend mode unreadable ({})".format(PROJECTION_MATERIAL_PATH, exc))

    side_parent = unreal.load_asset(SIDE_MATERIAL_PATH)
    if side_parent is None:
        failures.append("{} failed to load".format(SIDE_MATERIAL_PATH))

    instance_specs = [
        (PROJECTION_MI_PATH, PROJECTION_MATERIAL_PATH),
        (SIDE_MI_PATH, SIDE_MATERIAL_PATH),
    ]
    for instance_path, parent_path in instance_specs:
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
        elif asset_path_without_object(parent) != parent_path:
            failures.append("{} parent is {}, expected {}".format(instance_path, parent.get_path_name(), parent_path))


def material_slots(mesh):
    try:
        return list(mesh.get_editor_property("static_materials"))
    except Exception:
        return []


def validate_mesh_material_slots(failures, mesh):
    slots = material_slots(mesh)
    if len(slots) != 2:
        failures.append("{} has {} material slots, expected 2".format(MESH_PATH, len(slots)))
        return
    expected = [PROJECTION_MI_PATH, SIDE_MI_PATH]
    for index, expected_path in enumerate(expected):
        material = slots[index].get_editor_property("material_interface")
        if material is None:
            failures.append("{} material slot {} is unassigned".format(MESH_PATH, index))
        elif asset_path_without_object(material) != expected_path:
            failures.append("{} material slot {} is {}, expected {}".format(MESH_PATH, index, material.get_path_name(), expected_path))


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
    if height < 190.0 or height > 230.0:
        failures.append("{} height {:.2f} cm outside expected test2-manual cairn envelope".format(MESH_PATH, height))
    if max(width, depth) < 300.0 or max(width, depth) > 340.0:
        failures.append("{} max horizontal bounds {:.2f} cm outside expected test2-manual cairn envelope".format(MESH_PATH, max(width, depth)))
    if min(width, depth) < 145.0 or min(width, depth) > 170.0:
        failures.append("{} min horizontal bounds {:.2f} cm outside expected test2-manual cairn envelope".format(MESH_PATH, min(width, depth)))


def validate_collision_source(failures, mesh):
    counter = getattr(unreal.EditorStaticMeshLibrary, "get_simple_collision_count", None)
    if callable(counter):
        try:
            collision_count = counter(mesh)
        except Exception:
            collision_count = None
        if collision_count is not None and collision_count < 1:
            failures.append("{} has no simple collision, expected imported UCX proxy".format(MESH_PATH))


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
    if unreal.EditorStaticMeshLibrary.get_lod_count(mesh) < 4:
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

    expected_materials = [PROJECTION_MI_PATH, SIDE_MI_PATH]
    for index, expected_path in enumerate(expected_materials):
        material = component.get_material(index)
        if material is None:
            failures.append("{} material slot {} is unassigned".format(ACTOR_LABEL, index))
        elif asset_path_without_object(material) != expected_path:
            failures.append("{} material slot {} is {}, expected {}".format(ACTOR_LABEL, index, material.get_path_name(), expected_path))

    try:
        if component.get_collision_enabled() != unreal.CollisionEnabled.QUERY_AND_PHYSICS:
            failures.append("{} collision is {}, expected QUERY_AND_PHYSICS".format(ACTOR_LABEL, component.get_collision_enabled()))
    except Exception as exc:
        failures.append("{} collision state unreadable ({})".format(ACTOR_LABEL, exc))

    if mesh is not None:
        _origin, extent = actor.get_actor_bounds(False)
        if extent.z * 2.0 < 190.0 or extent.z * 2.0 > 230.0:
            failures.append("{} actor height {:.2f} cm outside expected envelope".format(ACTOR_LABEL, extent.z * 2.0))


def main():
    failures = []
    measurements = []
    validate_source_fbx(failures)
    validate_textures(failures)
    validate_materials(failures)
    mesh = validate_mesh(failures, measurements)
    validate_actor(failures, mesh)
    if failures:
        raise RuntimeError("Blood Axe test2-manual cairn validation failed: {}".format("; ".join(failures)))

    if measurements and measurements[0][0] != "unavailable":
        height, width, depth = measurements[0]
        print(
            "Blood Axe test2-manual cairn validation passed: {:.2f}h x {:.2f}w x {:.2f}d cm, 4 LODs, 2 materials, 3 textures, startup actor {}, broad collision enabled.".format(
                height,
                width,
                depth,
                ACTOR_LABEL,
            )
        )
    else:
        print(
            "Blood Axe test2-manual cairn validation passed: 4 LODs, 2 materials, 3 textures, startup actor {}, broad collision enabled.".format(
                ACTOR_LABEL,
            )
        )


if __name__ == "__main__":
    main()
