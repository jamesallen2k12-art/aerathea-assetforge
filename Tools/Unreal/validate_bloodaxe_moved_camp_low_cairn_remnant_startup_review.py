import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01"

ACTOR_LABEL = "AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01"
EXPECTED_LOCATION = unreal.Vector(1280.0, 430.0, 0.0)
EXPECTED_YAW = -18.0
EXPECTED_TAGS = [
    "AET_FIRST_SLICE",
    "AET_BLOODAXE_MOVED_CAMP_REVIEW",
    "AET_STATIC_REVIEW_TARGET",
]


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


def rotation_yaw(rotation):
    for name in ("yaw", "Yaw"):
        if hasattr(rotation, name):
            return float(getattr(rotation, name))
    try:
        return float(rotation.get_editor_property("yaw"))
    except Exception:
        return 0.0


def vector_distance(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z
    return math.sqrt((dx * dx) + (dy * dy) + (dz * dz))


def validate_component_visibility(failures, actor, component):
    is_hidden_ed = getattr(actor, "is_hidden_ed", None)
    if callable(is_hidden_ed):
        try:
            if is_hidden_ed():
                failures.append("{} is hidden in editor".format(ACTOR_LABEL))
        except Exception:
            pass
    try:
        if actor.get_actor_hidden_in_game():
            failures.append("{} is hidden in game".format(ACTOR_LABEL))
    except Exception:
        pass
    try:
        if not component.is_visible():
            failures.append("{} static mesh component is not visible".format(ACTOR_LABEL))
    except Exception:
        pass
    try:
        if component.get_collision_enabled() != unreal.CollisionEnabled.NO_COLLISION:
            failures.append("{} collision is enabled; expected no collision correctness claim".format(ACTOR_LABEL))
    except Exception as exc:
        failures.append("{} collision state unreadable ({})".format(ACTOR_LABEL, exc))


def validate_actor(failures, mesh):
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

    scale = actor.get_actor_scale3d()
    if vector_distance(scale, unreal.Vector(1.0, 1.0, 1.0)) > 0.01:
        failures.append("{} scale {} differs from expected 1.0".format(ACTOR_LABEL, scale))

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

    material = component.get_material(0)
    if material is None:
        failures.append("{} material slot 0 is unassigned".format(ACTOR_LABEL))
    elif asset_path_without_object(material) != MATERIAL_INSTANCE_PATH:
        failures.append("{} material slot 0 is {}, expected {}".format(ACTOR_LABEL, material.get_path_name(), MATERIAL_INSTANCE_PATH))

    if mesh is not None:
        validate_component_visibility(failures, actor, component)


def validate_mesh_metadata(failures, mesh):
    expected = {
        "Aerathea.StaticMesh.StartupPlaced": "startup_review_actor",
        "Aerathea.StaticMesh.StartupActor": ACTOR_LABEL,
        "Aerathea.StaticMesh.VisualReview": "requested_changes_material_value_pass_pending_approval_not_final_art",
        "Aerathea.StaticMesh.FinalArtAuthored": "false",
        "Aerathea.StaticMesh.CollisionPolicy": "disabled_no_correctness_claim",
        "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
        "Aerathea.StaticMesh.MaterialValueRevision": "AET-MA-20260629-583_requested_changes",
        "Aerathea.StaticMesh.MaterialValueControl": "vertex_color_parent_material_multiplier_v02",
    }
    for tag, expected_value in expected.items():
        value = metadata_value(failures, mesh, tag)
        if value is None:
            continue
        if value != expected_value:
            failures.append("{} metadata {} is {!r}, expected {!r}".format(MESH_PATH, tag, value, expected_value))


def main():
    failures = []
    mesh = unreal.load_asset(MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(MESH_PATH))
    else:
        validate_mesh_metadata(failures, mesh)

    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        failures.append("Failed to load level {}".format(LEVEL_PATH))
    else:
        validate_actor(failures, mesh)

    if failures:
        raise RuntimeError("Blood Axe low cairn startup review validation failed: {}".format("; ".join(failures)))

    print(
        "Blood Axe low cairn startup review validation passed: {} placed at {:.1f}, {:.1f}, {:.1f}, yaw {:.1f}, no collision, material/value pass pending approval, final art not authored.".format(
            ACTOR_LABEL,
            EXPECTED_LOCATION.x,
            EXPECTED_LOCATION.y,
            EXPECTED_LOCATION.z,
            EXPECTED_YAW,
        )
    )


if __name__ == "__main__":
    main()
