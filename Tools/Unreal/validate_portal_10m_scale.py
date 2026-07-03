import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
PORTAL_ACTOR_LABEL = "AET_PROD_Portal_A01"
PORTAL_MESH_PATH = "/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01"
PORTAL_BLUEPRINT_PATH = "/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01"

REQUIRED_SOCKETS = [
    "Socket_PortalCore",
    "Socket_VFX_Center",
    "Socket_Audio_Hum",
]


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    if actor_subsystem is not None:
        return list(actor_subsystem.get_all_level_actors())
    return list(unreal.EditorLevelLibrary.get_all_level_actors())


def find_actor(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def vector_radius(vector):
    return math.sqrt((vector.x * vector.x) + (vector.y * vector.y) + (vector.z * vector.z))


def component_local_dimensions(component):
    get_local_bounds = getattr(component, "get_local_bounds", None)
    if not callable(get_local_bounds):
        return None
    min_bound, max_bound = get_local_bounds()
    return unreal.Vector(
        max_bound.x - min_bound.x,
        max_bound.y - min_bound.y,
        max_bound.z - min_bound.z,
    )


def component_relative_location(component):
    getter = getattr(component, "get_relative_location", None)
    if callable(getter):
        return getter()
    return component.get_editor_property("relative_location")


def component_relative_scale(component):
    getter = getattr(component, "get_relative_scale3d", None)
    if callable(getter):
        return getter()
    return component.get_editor_property("relative_scale3d")


def box_extent(component):
    getter = getattr(component, "get_unscaled_box_extent", None)
    if callable(getter):
        return getter()
    return component.get_editor_property("box_extent")


def approx(value, target, tolerance):
    return abs(value - target) <= tolerance


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    failures = []
    mesh = unreal.load_asset(PORTAL_MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(PORTAL_MESH_PATH))
    else:
        for socket_name in REQUIRED_SOCKETS:
            if mesh.find_socket(unreal.Name(socket_name)) is None:
                failures.append("{} missing socket {}".format(PORTAL_MESH_PATH, socket_name))
        if unreal.EditorStaticMeshLibrary.get_lod_count(mesh) < 4:
            failures.append("{} has fewer than 4 LODs".format(PORTAL_MESH_PATH))

    if unreal.load_asset(PORTAL_BLUEPRINT_PATH) is None:
        failures.append("{} failed to load".format(PORTAL_BLUEPRINT_PATH))

    actor = find_actor(PORTAL_ACTOR_LABEL)
    if actor is None:
        failures.append("{} missing from {}".format(PORTAL_ACTOR_LABEL, LEVEL_PATH))
    else:
        scale = actor.get_actor_scale3d()
        if not (approx(scale.x, 1.0, 0.01) and approx(scale.y, 1.0, 0.01) and approx(scale.z, 1.0, 0.01)):
            failures.append("{} actor scale is {}, expected 1,1,1".format(PORTAL_ACTOR_LABEL, scale))

        actor_class_name = actor.get_class().get_name()
        if "BP_AET_Portal_A01" not in actor_class_name and "AETPortalActor" not in actor_class_name:
            failures.append("{} has unexpected class {}".format(PORTAL_ACTOR_LABEL, actor_class_name))

        arch_component = actor.get_editor_property("portal_arch_mesh")
        if arch_component is None:
            failures.append("{} missing PortalArchMesh component".format(PORTAL_ACTOR_LABEL))
        else:
            assigned_mesh = arch_component.get_editor_property("static_mesh")
            if assigned_mesh is None:
                failures.append("{} PortalArchMesh has no mesh".format(PORTAL_ACTOR_LABEL))
            elif asset_path_without_object(assigned_mesh) != PORTAL_MESH_PATH:
                failures.append(
                    "{} PortalArchMesh uses {}, expected {}".format(
                        PORTAL_ACTOR_LABEL,
                        assigned_mesh.get_path_name(),
                        PORTAL_MESH_PATH,
                    )
                )
            dimensions = component_local_dimensions(arch_component)
            if dimensions is not None:
                if dimensions.x < 1180.0 or dimensions.z < 1240.0:
                    failures.append("{} arch dimensions too small: {}".format(PORTAL_ACTOR_LABEL, dimensions))

        core_component = actor.get_editor_property("portal_core_mesh")
        if core_component is None:
            failures.append("{} missing PortalCoreMesh component".format(PORTAL_ACTOR_LABEL))
        else:
            core_location = component_relative_location(core_component)
            core_scale = component_relative_scale(core_component)
            if not approx(core_location.z, 500.0, 5.0):
                failures.append("{} core Z {:.2f} cm should center on 10 m aperture".format(PORTAL_ACTOR_LABEL, core_location.z))
            if core_scale.x < 7.0 or core_scale.z < 9.5:
                failures.append("{} core scale {} is too small for 10 m aperture".format(PORTAL_ACTOR_LABEL, core_scale))

        interaction = actor.get_editor_property("interaction_volume")
        if interaction is None:
            failures.append("{} missing InteractionVolume component".format(PORTAL_ACTOR_LABEL))
        else:
            extent = box_extent(interaction)
            location = component_relative_location(interaction)
            if extent.x < 540.0 or extent.z < 540.0:
                failures.append("{} interaction extent {} is too small for 10 m portal".format(PORTAL_ACTOR_LABEL, extent))
            if not approx(location.z, 520.0, 10.0):
                failures.append("{} interaction Z {:.2f} cm should span the portal height".format(PORTAL_ACTOR_LABEL, location.z))

        _origin, actor_extent = actor.get_actor_bounds(False)
        if actor_extent.x < 590.0 or actor_extent.z < 620.0:
            failures.append("{} actor bounds extent {} is too small".format(PORTAL_ACTOR_LABEL, actor_extent))
        if vector_radius(actor_extent) > 1250.0:
            failures.append("{} actor bounds radius {:.2f} cm exceeds 1250 cm".format(PORTAL_ACTOR_LABEL, vector_radius(actor_extent)))

    if failures:
        raise RuntimeError("10 m portal validation failed: {}".format("; ".join(failures)))

    print("10 m portal validation passed for {} using {}.".format(PORTAL_ACTOR_LABEL, PORTAL_MESH_PATH))


if __name__ == "__main__":
    main()
