import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
ARCH_ACTOR_LABEL = "AET_PROD_INF_HornWingArch_A01"
ARCH_MESH_PATH = "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_HornWingArch_A01"
ACTOR_SCALE_TOLERANCE = 0.01


REQUIRED_MATERIALS = [
    "/Game/Aerathea/Materials/Infernals/HornWingArch/M_INF_HornWingArch_CultStone_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/HornWingArch/M_INF_HornWingArch_ScorchedStone_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/HornWingArch/M_INF_HornWingArch_ObsidianIron_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/HornWingArch/M_INF_HornWingArch_BoneHorn_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/HornWingArch/M_INF_HornWingArch_BrandGlow_Blockout_A01",
]


REQUIRED_SOCKETS = [
    "snap_floor",
    "snap_altar",
    "guard_l",
    "guard_r",
    "banner_l",
    "banner_r",
    "vfx_crown",
    "vfx_eye",
    "vfx_inner_throat",
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


def vector_radius(vector):
    return math.sqrt((vector.x * vector.x) + (vector.y * vector.y) + (vector.z * vector.z))


def approx(value, target, tolerance):
    return abs(value - target) <= tolerance


def validate_assets(failures):
    for asset_path in REQUIRED_MATERIALS:
        if unreal.load_asset(asset_path) is None:
            failures.append("{} failed to load".format(asset_path))

    mesh = unreal.load_asset(ARCH_MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(ARCH_MESH_PATH))
        return None

    material_count = len(mesh.get_editor_property("static_materials"))
    if material_count < 5:
        failures.append("{} has {} material slots, expected at least 5".format(ARCH_MESH_PATH, material_count))

    if unreal.EditorStaticMeshLibrary.get_lod_count(mesh) < 4:
        failures.append("{} has fewer than 4 LODs".format(ARCH_MESH_PATH))

    missing_sockets = [
        socket_name
        for socket_name in REQUIRED_SOCKETS
        if mesh.find_socket(unreal.Name(socket_name)) is None
    ]
    if missing_sockets:
        failures.append("{} missing sockets {}".format(ARCH_MESH_PATH, ", ".join(missing_sockets)))
    return mesh


def validate_actor(mesh, failures, measurements):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actor = actors_by_label().get(ARCH_ACTOR_LABEL)
    if actor is None:
        failures.append("{} missing from {}".format(ARCH_ACTOR_LABEL, LEVEL_PATH))
        return

    if actor.get_class().get_name() != "StaticMeshActor":
        failures.append("{} has unexpected class {}".format(ARCH_ACTOR_LABEL, actor.get_class().get_name()))

    scale = actor.get_actor_scale3d()
    if not (
        approx(scale.x, 1.0, ACTOR_SCALE_TOLERANCE)
        and approx(scale.y, 1.0, ACTOR_SCALE_TOLERANCE)
        and approx(scale.z, 1.0, ACTOR_SCALE_TOLERANCE)
    ):
        failures.append("{} actor scale is {}, expected 1,1,1".format(ARCH_ACTOR_LABEL, scale))

    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        failures.append("{} has no StaticMeshComponent".format(ARCH_ACTOR_LABEL))
        return

    assigned_mesh = component.get_editor_property("static_mesh")
    if assigned_mesh is None:
        failures.append("{} has no assigned static mesh".format(ARCH_ACTOR_LABEL))
    elif asset_path_without_object(assigned_mesh) != ARCH_MESH_PATH:
        failures.append("{} uses {}, expected {}".format(ARCH_ACTOR_LABEL, assigned_mesh.get_path_name(), ARCH_MESH_PATH))
    elif mesh is not None and asset_path_without_object(assigned_mesh) != asset_path_without_object(mesh):
        failures.append("{} component mesh and loaded mesh disagree".format(ARCH_ACTOR_LABEL))

    _origin, extent = actor.get_actor_bounds(False)
    visible_height = extent.z * 2.0
    visible_width = extent.x * 2.0
    visible_depth = extent.y * 2.0
    radius = vector_radius(extent)
    measurements.append((visible_height, visible_width, visible_depth, radius))
    if visible_height < 520.0 or visible_height > 690.0:
        failures.append("{} visible height {:.2f} cm is outside HornWingArch envelope".format(ARCH_ACTOR_LABEL, visible_height))
    if visible_width < 430.0 or visible_width > 720.0:
        failures.append("{} visible width {:.2f} cm is outside HornWingArch envelope".format(ARCH_ACTOR_LABEL, visible_width))
    if visible_depth < 120.0 or visible_depth > 260.0:
        failures.append("{} visible depth {:.2f} cm is outside HornWingArch envelope".format(ARCH_ACTOR_LABEL, visible_depth))
    if radius > 760.0:
        failures.append("{} bounds radius {:.2f} cm exceeds 760 cm".format(ARCH_ACTOR_LABEL, radius))


def main():
    failures = []
    measurements = []
    mesh = validate_assets(failures)
    validate_actor(mesh, failures, measurements)
    if failures:
        raise RuntimeError("Infernal HornWingArch validation failed: {}".format("; ".join(failures)))

    visible_height, visible_width, visible_depth, radius = measurements[0]
    print(
        "Infernal HornWingArch validation passed: {:.2f}h x {:.2f}w x {:.2f}d cm, bounds radius {:.2f} cm, {} sockets.".format(
            visible_height,
            visible_width,
            visible_depth,
            radius,
            len(REQUIRED_SOCKETS),
        )
    )


if __name__ == "__main__":
    main()
