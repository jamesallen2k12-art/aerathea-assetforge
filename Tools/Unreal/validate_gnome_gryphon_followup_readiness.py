import unreal


ASSET_CHECKS = [
    {
        "name": "SK_GNM_Base_A01",
        "mesh": "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01",
        "skeleton": "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01_Skeleton",
        "physics_asset": "/Game/Aerathea/Characters/Gnomes/Base/PHYS_GNM_Base_A01",
        "anim_blueprint": "/Game/Aerathea/Characters/Gnomes/Base/ABP_GNM_Base_A01",
        "optional_animation": None,
        "required_sockets": [
            "hand_r_weapon",
            "hand_l_offhand",
            "back_pack",
            "head_goggles",
            "belt_tool_l",
            "belt_tool_r",
            "muzzle_preview",
            "vfx_aether_core",
        ],
    },
    {
        "name": "SK_CRE_Gryphon_A01",
        "mesh": "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01",
        "skeleton": "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01_Skeleton",
        "physics_asset": "/Game/Aerathea/Creatures/Gryphon/Base/PHYS_CRE_Gryphon_A01",
        "anim_blueprint": "/Game/Aerathea/Creatures/Gryphon/Base/ABP_CRE_Gryphon_A01",
        "optional_animation": "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01_Anim",
        "required_sockets": [
            "socket_head_vfx",
            "socket_beak",
            "socket_talon_l",
            "socket_talon_r",
            "socket_back_mount",
            "socket_saddle",
            "socket_wing_l_vfx",
            "socket_wing_r_vfx",
            "socket_tail",
        ],
    },
]


def try_call(obj, method_name):
    method = getattr(obj, method_name, None)
    if not callable(method):
        return None
    try:
        return method()
    except Exception:
        return None


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def skeletal_mesh_skeleton(mesh):
    skeleton = try_call(mesh, "get_skeleton")
    if skeleton is not None:
        return skeleton
    try:
        return mesh.get_editor_property("skeleton")
    except Exception:
        return None


def validate_asset(entry):
    failures = []
    mesh = unreal.load_asset(entry["mesh"])
    if mesh is None:
        return ["{} failed to load".format(entry["mesh"])]

    skeleton = skeletal_mesh_skeleton(mesh)
    if skeleton is None:
        failures.append("{} has no assigned skeleton".format(entry["mesh"]))
    elif asset_path_without_object(skeleton) != entry["skeleton"]:
        failures.append("{} has unexpected skeleton {}".format(entry["mesh"], skeleton.get_path_name()))

    physics_asset = mesh.get_editor_property("physics_asset")
    if physics_asset is None:
        failures.append("{} has no assigned physics asset".format(entry["mesh"]))
    elif asset_path_without_object(physics_asset) != entry["physics_asset"]:
        failures.append("{} has unexpected physics asset {}".format(entry["mesh"], physics_asset.get_path_name()))

    if len(mesh.get_editor_property("materials")) == 0:
        failures.append("{} has no material slots".format(entry["mesh"]))

    for socket_name in entry["required_sockets"]:
        if mesh.find_socket(unreal.Name(socket_name)) is None:
            failures.append("{} missing socket {}".format(entry["mesh"], socket_name))

    for asset_key in ("skeleton", "physics_asset", "anim_blueprint", "optional_animation"):
        asset_path = entry.get(asset_key)
        if asset_path is not None and not unreal.EditorAssetLibrary.does_asset_exist(asset_path):
            failures.append("{} missing {}".format(entry["name"], asset_path))

    return failures


def main():
    failures = []
    for entry in ASSET_CHECKS:
        failures.extend(validate_asset(entry))

    if failures:
        raise RuntimeError("Gnome/Gryphon follow-up readiness validation failed: {}".format("; ".join(failures)))

    print(
        "Gnome/Gryphon follow-up readiness validation passed: {} assets have expected skeletons, physics, sockets, and animation placeholders.".format(
            len(ASSET_CHECKS)
        )
    )


if __name__ == "__main__":
    main()
