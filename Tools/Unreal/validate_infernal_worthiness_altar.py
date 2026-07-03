import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
ALTAR_ACTOR_LABEL = "AET_PROD_INF_WorthinessAltar_A01"
FLOOR_ACTOR_LABEL = "AET_PROD_INF_CullingTrialFloor_A01"
ALTAR_MESH_PATH = "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01"
ACTOR_SCALE_TOLERANCE = 0.01
SNAP_DISTANCE_TOLERANCE_CM = 2.0


REQUIRED_MATERIALS = [
    "/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_CultStone_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_ScorchedStone_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_ObsidianIron_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_BoneHorn_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/WorthinessAltar/M_INF_WorthinessAltar_BrandGlow_Blockout_A01",
]


REQUIRED_MATERIAL_INSTANCES = [
    "/Game/Aerathea/Materials/Instances/MI_INF_WorthinessAltar_A01_CultStone",
    "/Game/Aerathea/Materials/Instances/MI_INF_WorthinessAltar_A01_ScorchedStone",
    "/Game/Aerathea/Materials/Instances/MI_INF_WorthinessAltar_A01_ObsidianIron",
    "/Game/Aerathea/Materials/Instances/MI_INF_WorthinessAltar_A01_BoneHorn",
    "/Game/Aerathea/Materials/Instances/MI_INF_WorthinessAltar_A01_BrandGlow",
]


REQUIRED_SOCKETS = [
    "snap_floor",
    "snap_arch_back",
    "interact_front",
    "stage_offering",
    "vfx_altar_core",
    "vfx_sacrifice_mark",
    "vfx_brand_transfer",
    "vfx_ring_link",
    "vfx_rejected_gap",
]


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    if actor_subsystem is not None:
        return list(actor_subsystem.get_all_level_actors())
    return list(unreal.EditorLevelLibrary.get_all_level_actors())


def actors_by_label():
    return {actor.get_actor_label(): actor for actor in all_level_actors()}


def vector_distance(a, b):
    return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + ((a.z - b.z) ** 2))


def vector_radius(vector):
    return math.sqrt((vector.x * vector.x) + (vector.y * vector.y) + (vector.z * vector.z))


def approx(value, target, tolerance):
    return abs(value - target) <= tolerance


def component_by_name(actor, component_class, expected_name):
    for component in actor.get_components_by_class(component_class):
        name = component.get_name()
        if name == expected_name or name.startswith("{}_".format(expected_name)):
            return component
    return None


def static_mesh_component_mesh(component):
    get_static_mesh = getattr(component, "get_static_mesh", None)
    if callable(get_static_mesh):
        mesh = get_static_mesh()
        if mesh is not None:
            return mesh
    try:
        return component.get_editor_property("static_mesh")
    except Exception:
        return None


def validate_assets(failures):
    for asset_path in REQUIRED_MATERIALS + REQUIRED_MATERIAL_INSTANCES:
        if unreal.load_asset(asset_path) is None:
            failures.append("{} failed to load".format(asset_path))

    mesh = unreal.load_asset(ALTAR_MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(ALTAR_MESH_PATH))
        return None

    material_count = len(mesh.get_editor_property("static_materials"))
    if material_count < 5:
        failures.append("{} has {} material slots, expected at least 5".format(ALTAR_MESH_PATH, material_count))

    if unreal.EditorStaticMeshLibrary.get_lod_count(mesh) < 4:
        failures.append("{} has fewer than 4 LODs".format(ALTAR_MESH_PATH))

    missing_sockets = [
        socket_name
        for socket_name in REQUIRED_SOCKETS
        if mesh.find_socket(unreal.Name(socket_name)) is None
    ]
    if missing_sockets:
        failures.append("{} missing sockets {}".format(ALTAR_MESH_PATH, ", ".join(missing_sockets)))
    return mesh


def floor_snap_location(label_to_actor):
    floor = label_to_actor.get(FLOOR_ACTOR_LABEL)
    if floor is None:
        return None
    component = floor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        return None
    socket_name = unreal.Name("snap_altar")
    try:
        if component.does_socket_exist(socket_name):
            return component.get_socket_location(socket_name)
    except Exception:
        return None
    return None


def validate_actor(mesh, failures, measurements):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    label_to_actor = actors_by_label()
    actor = label_to_actor.get(ALTAR_ACTOR_LABEL)
    if actor is None:
        failures.append("{} missing from {}".format(ALTAR_ACTOR_LABEL, LEVEL_PATH))
        return

    class_name = actor.get_class().get_name()
    if class_name != "StaticMeshActor" and "BP_INF_RitualAltar_A01" not in class_name and "AETInfernalRitualAltarActor" not in class_name:
        failures.append("{} has unexpected class {}".format(ALTAR_ACTOR_LABEL, class_name))

    scale = actor.get_actor_scale3d()
    if not (
        approx(scale.x, 1.0, ACTOR_SCALE_TOLERANCE)
        and approx(scale.y, 1.0, ACTOR_SCALE_TOLERANCE)
        and approx(scale.z, 1.0, ACTOR_SCALE_TOLERANCE)
    ):
        failures.append("{} actor scale is {}, expected 1,1,1".format(ALTAR_ACTOR_LABEL, scale))

    snap_location = floor_snap_location(label_to_actor)
    if snap_location is not None:
        actor_location = actor.get_actor_location()
        snap_distance = vector_distance(actor_location, snap_location)
        if snap_distance > SNAP_DISTANCE_TOLERANCE_CM:
            failures.append(
                "{} is {:.2f} cm from {} snap_altar".format(
                    ALTAR_ACTOR_LABEL,
                    snap_distance,
                    FLOOR_ACTOR_LABEL,
                )
            )

    component = component_by_name(actor, unreal.StaticMeshComponent, "AltarMesh")
    if component is None:
        component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        failures.append("{} has no StaticMeshComponent".format(ALTAR_ACTOR_LABEL))
        return

    assigned_mesh = static_mesh_component_mesh(component)
    if assigned_mesh is None:
        failures.append("{} has no assigned static mesh".format(ALTAR_ACTOR_LABEL))
    elif asset_path_without_object(assigned_mesh) != ALTAR_MESH_PATH:
        failures.append("{} uses {}, expected {}".format(ALTAR_ACTOR_LABEL, assigned_mesh.get_path_name(), ALTAR_MESH_PATH))
    elif mesh is not None and asset_path_without_object(assigned_mesh) != asset_path_without_object(mesh):
        failures.append("{} component mesh and loaded mesh disagree".format(ALTAR_ACTOR_LABEL))

    _origin, extent = actor.get_actor_bounds(False)
    visible_height = extent.z * 2.0
    visible_width = extent.x * 2.0
    visible_depth = extent.y * 2.0
    radius = vector_radius(extent)
    measurements.append((visible_height, visible_width, visible_depth, radius))
    if visible_height < 250.0 or visible_height > 385.0:
        failures.append("{} visible height {:.2f} cm is outside WorthinessAltar envelope".format(ALTAR_ACTOR_LABEL, visible_height))
    if visible_width < 300.0 or visible_width > 430.0:
        failures.append("{} visible width {:.2f} cm is outside WorthinessAltar envelope".format(ALTAR_ACTOR_LABEL, visible_width))
    if visible_depth < 170.0 or visible_depth > 390.0:
        failures.append("{} visible depth {:.2f} cm is outside WorthinessAltar envelope".format(ALTAR_ACTOR_LABEL, visible_depth))
    if radius > 550.0:
        failures.append("{} bounds radius {:.2f} cm exceeds 550 cm".format(ALTAR_ACTOR_LABEL, radius))


def main():
    failures = []
    measurements = []
    mesh = validate_assets(failures)
    validate_actor(mesh, failures, measurements)
    if failures:
        raise RuntimeError("Infernal WorthinessAltar validation failed: {}".format("; ".join(failures)))

    visible_height, visible_width, visible_depth, radius = measurements[0]
    print(
        "Infernal WorthinessAltar validation passed: {:.2f}h x {:.2f}w x {:.2f}d cm, bounds radius {:.2f} cm, {} sockets.".format(
            visible_height,
            visible_width,
            visible_depth,
            radius,
            len(REQUIRED_SOCKETS),
        )
    )


if __name__ == "__main__":
    main()
