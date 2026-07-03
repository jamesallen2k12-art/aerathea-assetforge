import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
REVIEW_LIGHT_LABELS = [
    "AET_BOOT_KeyLight_Directional",
    "AET_BOOT_SkyLight",
    "AET_PROD_ReviewFillLight_A01",
]


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def light_component(actor):
    light_component_base = getattr(unreal, "LightComponentBase", None)
    if light_component_base is not None:
        component = actor.get_component_by_class(light_component_base)
        if component is not None:
            return component
    for class_name in (
        "DirectionalLightComponent",
        "SkyLightComponent",
        "PointLightComponent",
        "SpotLightComponent",
        "RectLightComponent",
    ):
        component_class = getattr(unreal, class_name, None)
        if component_class is None:
            continue
        component = actor.get_component_by_class(component_class)
        if component is not None:
            return component
    return None


def mobility_name(component):
    try:
        return str(component.get_editor_property("mobility")).rsplit(".", 1)[-1]
    except Exception:
        return "unknown"


def set_movable(component):
    before = mobility_name(component)
    try:
        component.set_mobility(unreal.ComponentMobility.MOVABLE)
    except Exception:
        component.set_editor_property("mobility", unreal.ComponentMobility.MOVABLE)
    after = mobility_name(component)
    return before, after


def dump_unbuilt_light_interactions(label):
    world = unreal.EditorLevelLibrary.get_editor_world()
    unreal.log("DumpUnbuiltLightInteractions {}".format(label))
    unreal.SystemLibrary.execute_console_command(world, "DumpUnbuiltLightInteractions")


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    dump_unbuilt_light_interactions("before dynamic review-light fix")

    failures = []
    for label in REVIEW_LIGHT_LABELS:
        actor = find_actor_by_label(label)
        if actor is None:
            failures.append("missing {}".format(label))
            continue
        component = light_component(actor)
        if component is None:
            failures.append("{} has no light component".format(label))
            continue
        before, after = set_movable(component)
        unreal.log("{} mobility {} -> {}".format(label, before, after))

    if failures:
        raise RuntimeError("Could not update review lighting: {}".format("; ".join(failures)))

    dump_unbuilt_light_interactions("after dynamic review-light fix")

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save startup map after review-light mobility fix")

    unreal.log("Startup review lighting is movable; saved {}.".format(LEVEL_PATH))


main()
