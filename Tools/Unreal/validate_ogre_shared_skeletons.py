import unreal


OGRE_MALE_SKELETON = "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton"

OGRE_SHARED_SKELETON_MESHES = [
    {
        "name": "SK_OGR_Base_Male_A01",
        "mesh": "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01",
        "physics_asset": "/Game/Aerathea/Characters/Ogres/Base/PHYS_OGR_Base_Male_A01",
        "required_sockets": [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "spine_teknomancy_pack",
            "shoulder_l_large",
            "shoulder_r_large",
            "belt_front",
            "belt_back",
            "vfx_mouth",
            "vfx_eye_l",
            "vfx_eye_r",
            "vfx_chest_core",
            "vfx_stomp_ground",
        ],
    },
    {
        "name": "SK_OGR_Teknomancer_A01",
        "mesh": "/Game/Aerathea/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01",
        "physics_asset": "/Game/Aerathea/Characters/Ogres/Teknomancer/PHYS_OGR_Teknomancer_A01",
        "required_sockets": [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "spine_teknomancy_pack",
            "vfx_chest_core",
            "vfx_mouth",
            "vfx_stomp_ground",
            "vfx_hammer_core",
            "vfx_bracer_l",
            "vfx_bracer_r",
            "vfx_tek_core",
            "weapon_socket_r",
            "head_fx",
        ],
    },
    {
        "name": "SK_OGR_Warrior_Rival_A01",
        "mesh": "/Game/Aerathea/Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01",
        "physics_asset": "/Game/Aerathea/Characters/Ogres/Warrior/PHYS_OGR_Warrior_Rival_A01",
        "required_sockets": [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "belt_front",
            "vfx_belt_forge",
            "vfx_shield_core",
            "vfx_hammer_core",
            "vfx_stomp_ground",
            "head_fx",
        ],
    },
    {
        "name": "SK_OGR_Shaman_A01",
        "mesh": "/Game/Aerathea/Characters/Ogres/Shaman/SK_OGR_Shaman_A01",
        "physics_asset": "/Game/Aerathea/Characters/Ogres/Shaman/PHYS_OGR_Shaman_A01",
        "required_sockets": [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "vfx_mouth",
            "vfx_stomp_ground",
            "vfx_staff_head",
            "vfx_rune_wheel",
            "vfx_totem_chest",
            "weapon_staff_r",
            "head_fx",
        ],
    },
    {
        "name": "SK_OGR_Necromancer_A01",
        "mesh": "/Game/Aerathea/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01",
        "physics_asset": "/Game/Aerathea/Characters/Ogres/Necromancer/PHYS_OGR_Necromancer_A01",
        "required_sockets": [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "vfx_mouth",
            "vfx_stomp_ground",
            "vfx_lantern_core",
            "vfx_chest_necro",
            "vfx_bracer_l",
            "vfx_bracer_r",
            "weapon_staff_r",
            "head_fx",
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


def validate_mesh(entry):
    failures = []
    mesh = unreal.load_asset(entry["mesh"])
    if mesh is None:
        return ["{} failed to load".format(entry["mesh"])]

    skeleton = skeletal_mesh_skeleton(mesh)
    if skeleton is None:
        failures.append("{} has no assigned skeleton".format(entry["mesh"]))
    elif asset_path_without_object(skeleton) != OGRE_MALE_SKELETON:
        failures.append(
            "{} is bound to {}, expected {}".format(entry["mesh"], skeleton.get_path_name(), OGRE_MALE_SKELETON)
        )

    physics_asset = mesh.get_editor_property("physics_asset")
    if physics_asset is None:
        failures.append("{} has no assigned physics asset".format(entry["mesh"]))
    elif asset_path_without_object(physics_asset) != entry["physics_asset"]:
        failures.append(
            "{} has unexpected physics asset {}".format(entry["mesh"], physics_asset.get_path_name())
        )

    if len(mesh.get_editor_property("materials")) == 0:
        failures.append("{} has no material slots".format(entry["mesh"]))

    for socket_name in entry["required_sockets"]:
        if mesh.find_socket(unreal.Name(socket_name)) is None:
            failures.append("{} missing socket {}".format(entry["mesh"], socket_name))

    return failures


def main():
    if not unreal.EditorAssetLibrary.does_asset_exist(OGRE_MALE_SKELETON):
        raise RuntimeError("Missing Ogre male shared skeleton: {}".format(OGRE_MALE_SKELETON))

    failures = []
    for entry in OGRE_SHARED_SKELETON_MESHES:
        failures.extend(validate_mesh(entry))

    if failures:
        raise RuntimeError("Ogre shared skeleton validation failed: {}".format("; ".join(failures)))

    print(
        "Ogre shared skeleton validation passed: {} male Ogre meshes bound to {}.".format(
            len(OGRE_SHARED_SKELETON_MESHES),
            OGRE_MALE_SKELETON,
        )
    )


if __name__ == "__main__":
    main()
