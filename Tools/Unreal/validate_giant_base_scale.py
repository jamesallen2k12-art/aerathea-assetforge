import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
GIANT_TEMPLATE_HEIGHT_CM = 457.0
GIANT_TEMPLATE_VISIBLE_HEIGHT_CM = 449.0
VISIBLE_HEIGHT_RATIO = GIANT_TEMPLATE_VISIBLE_HEIGHT_CM / GIANT_TEMPLATE_HEIGHT_CM
VISIBLE_HEIGHT_TOLERANCE_CM = 10.0
ACTOR_SCALE_TOLERANCE = 0.01

GIANT_ASSETS = [
    {
        "label": "AET_PROD_GiantMaleBase_A01",
        "mesh": "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01",
        "physics_asset": "/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Male_A01",
        "baseline_height_cm": 470.0,
    },
    {
        "label": "AET_PROD_GiantFemaleBase_A01",
        "mesh": "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01",
        "physics_asset": "/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Female_A01",
        "baseline_height_cm": 442.0,
    },
]

REQUIRED_SOCKETS = [
    "hand_r_weapon",
    "hand_l_offhand",
    "hand_r_twohand_grip",
    "hand_l_twohand_grip",
    "back_large_weapon",
    "back_shield",
    "belt_tool_l",
    "belt_tool_r",
    "head_hair_ornament",
    "chest_talisman",
    "vfx_rune_hand_l",
    "vfx_rune_hand_r",
    "vfx_stomp_ground",
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


def validate_asset(entry, failures):
    mesh = unreal.load_asset(entry["mesh"])
    if mesh is None:
        failures.append("{} failed to load".format(entry["mesh"]))
        return None

    if len(mesh.get_editor_property("materials")) == 0:
        failures.append("{} has no material slots".format(entry["mesh"]))

    physics_asset = mesh.get_editor_property("physics_asset")
    if physics_asset is None:
        failures.append("{} has no assigned physics asset".format(entry["mesh"]))
    elif asset_path_without_object(physics_asset) != entry["physics_asset"]:
        failures.append(
            "{} has unexpected physics asset {}".format(entry["mesh"], physics_asset.get_path_name())
        )

    missing_sockets = [
        socket_name
        for socket_name in REQUIRED_SOCKETS
        if mesh.find_socket(unreal.Name(socket_name)) is None
    ]
    if missing_sockets:
        failures.append("{} missing sockets {}".format(entry["mesh"], ", ".join(missing_sockets)))

    return mesh


def validate_actor(entry, mesh, level_actors, measurements, failures):
    actor = level_actors.get(entry["label"])
    if actor is None:
        failures.append("{} missing from {}".format(entry["label"], LEVEL_PATH))
        return

    scale = actor.get_actor_scale3d()
    if (
        abs(scale.x - 1.0) > ACTOR_SCALE_TOLERANCE
        or abs(scale.y - 1.0) > ACTOR_SCALE_TOLERANCE
        or abs(scale.z - 1.0) > ACTOR_SCALE_TOLERANCE
    ):
        failures.append("{} actor scale is {}, expected 1,1,1".format(entry["label"], scale))

    component = actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if component is None:
        failures.append("{} has no SkeletalMeshComponent".format(entry["label"]))
        return

    assigned_mesh = component.get_editor_property("skeletal_mesh")
    if assigned_mesh is None:
        failures.append("{} has no assigned skeletal mesh".format(entry["label"]))
    elif asset_path_without_object(assigned_mesh) != entry["mesh"]:
        failures.append(
            "{} uses {}, expected {}".format(entry["label"], assigned_mesh.get_path_name(), entry["mesh"])
        )
    elif mesh is not None and asset_path_without_object(assigned_mesh) != asset_path_without_object(mesh):
        failures.append("{} component mesh and loaded mesh disagree".format(entry["label"]))

    _origin, extent = actor.get_actor_bounds(False)
    visible_height = extent.z * 2.0
    expected_height = entry["baseline_height_cm"] * VISIBLE_HEIGHT_RATIO
    measurements.append((entry["label"], visible_height, expected_height, vector_radius(extent)))

    if abs(visible_height - expected_height) > VISIBLE_HEIGHT_TOLERANCE_CM:
        failures.append(
            "{} visible bounds height {:.2f} cm is outside {:.2f} +/- {:.2f} cm for approved {:.0f} cm baseline".format(
                entry["label"],
                visible_height,
                expected_height,
                VISIBLE_HEIGHT_TOLERANCE_CM,
                entry["baseline_height_cm"],
            )
        )


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    failures = []
    measurements = []
    level_actors = actors_by_label()
    for entry in GIANT_ASSETS:
        mesh = validate_asset(entry, failures)
        validate_actor(entry, mesh, level_actors, measurements, failures)

    if failures:
        raise RuntimeError("Giant base scale validation failed: {}".format("; ".join(failures)))

    print(
        "Giant base scale validation passed: {}.".format(
            "; ".join(
                "{} visible height {:.2f} cm, expected {:.2f} cm, bounds radius {:.2f} cm".format(
                    label,
                    visible_height,
                    expected_height,
                    radius,
                )
                for label, visible_height, expected_height, radius in measurements
            )
        )
    )


if __name__ == "__main__":
    main()
