import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
GRYPHON_LABEL = "AET_PROD_CRE_Gryphon_A01"
CAMERA_LABEL = "AET_PROD_Camera_Review_A01"


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def vsub(a, b):
    return unreal.Vector(a.x - b.x, a.y - b.y, a.z - b.z)


def vdot(a, b):
    return (a.x * b.x) + (a.y * b.y) + (a.z * b.z)


def vlen(a):
    return math.sqrt(vdot(a, a))


def vnorm(a):
    length = vlen(a)
    if length <= 0.0001:
        return unreal.Vector(0.0, 0.0, 0.0)
    return unreal.Vector(a.x / length, a.y / length, a.z / length)


def log_socket(component, actor_location, name):
    try:
        location = component.get_socket_location(name)
    except Exception:
        unreal.log_warning("Missing gryphon socket/bone {}".format(name))
        return None
    offset = vsub(location, actor_location)
    unreal.log("Gryphon orientation {} world={} offset={}.".format(name, location, offset))
    return location


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actor = find_actor_by_label(GRYPHON_LABEL)
    if actor is None:
        raise RuntimeError("Missing {}".format(GRYPHON_LABEL))
    camera = find_actor_by_label(CAMERA_LABEL)
    if camera is None:
        raise RuntimeError("Missing {}".format(CAMERA_LABEL))

    component = actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if component is None:
        raise RuntimeError("{} has no SkeletalMeshComponent".format(GRYPHON_LABEL))

    actor_location = actor.get_actor_location()
    camera_location = camera.get_actor_location()
    camera_to_actor = vnorm(vsub(actor_location, camera_location))
    unreal.log(
        "Gryphon orientation actor location={} rotation={} scale={} camera={} camera_to_actor={}.".format(
            actor_location,
            actor.get_actor_rotation(),
            actor.get_actor_scale3d(),
            camera_location,
            camera_to_actor,
        )
    )

    for socket_name in component.get_all_socket_names():
        unreal.log("Gryphon available socket/bone: {}".format(socket_name))

    head = log_socket(component, actor_location, "SOCKET_head_vfx")
    tail = log_socket(component, actor_location, "SOCKET_tail")
    saddle = log_socket(component, actor_location, "SOCKET_saddle_root")
    if head is not None and tail is not None:
        head_direction = vnorm(vsub(head, tail))
        camera_to_head = vnorm(vsub(head, camera_location))
        unreal.log(
            "Gryphon head direction tail_to_head={} camera_to_head={} dot={:.3f} saddle={}.".format(
                head_direction,
                camera_to_head,
                vdot(head_direction, camera_to_head),
                saddle,
            )
        )


main()
