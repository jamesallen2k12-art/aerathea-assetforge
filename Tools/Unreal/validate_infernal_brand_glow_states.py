import unreal


MATERIAL_PATH = "/Game/Aerathea/Materials/Infernals"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
MASTER_MATERIAL_PATH = "{}/M_INF_BrandGlow_Master_A01".format(MATERIAL_PATH)
FUNCTION_PATH = "{}/MF_INF_BrandGlowStates_A01".format(MATERIAL_PATH)


REQUIRED_STATES = [
    "Inactive",
    "Smolder",
    "TrialActive",
    "Accepted",
    "Rejected",
    "SorcererFocus",
]


REQUIRED_CLASS_SOCKET_CONTRACTS = {
    "/Game/Aerathea/Characters/Infernals/Mage/SK_INF_Mage_A01": [
        "vfx_eye_l",
        "vfx_eye_r",
        "vfx_brand_chest",
        "vfx_brand_forearm_l",
        "vfx_brand_forearm_r",
        "vfx_sorcerer_focus",
    ],
    "/Game/Aerathea/Characters/Infernals/Warrior/SK_INF_Warrior_A01": [
        "vfx_eye_l",
        "vfx_eye_r",
        "vfx_brand_chest",
        "vfx_brand_forearm_l",
        "vfx_brand_forearm_r",
        "vfx_rage_core",
    ],
    "/Game/Aerathea/Characters/Infernals/Rogue/SK_INF_Rogue_A01": [
        "vfx_eye_l",
        "vfx_eye_r",
        "vfx_brand_chest",
        "vfx_brand_forearm_l",
        "vfx_brand_forearm_r",
        "vfx_ambush_mark",
        "vfx_invisible_sight_focus",
    ],
    "/Game/Aerathea/Characters/Infernals/Hunter/SK_INF_Hunter_A01": [
        "vfx_eye_l",
        "vfx_eye_r",
        "vfx_brand_chest",
        "vfx_brand_forearm_l",
        "vfx_brand_forearm_r",
        "vfx_target_mark",
        "vfx_brow_sight",
        "vfx_pursuit_burst",
    ],
}


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def validate_state_instances(failures):
    parent = unreal.load_asset(MASTER_MATERIAL_PATH)
    if parent is None:
        failures.append("{} failed to load".format(MASTER_MATERIAL_PATH))
        return

    if unreal.load_asset(FUNCTION_PATH) is None:
        failures.append("{} failed to load".format(FUNCTION_PATH))

    instances = []
    for state_name in REQUIRED_STATES:
        instance_path = "{}/MI_INF_BrandGlowStates_A01_{}".format(MATERIAL_INSTANCE_PATH, state_name)
        instance = unreal.load_asset(instance_path)
        if instance is None:
            failures.append("{} failed to load".format(instance_path))
            continue
        instances.append(instance)

        instance_parent = None
        try:
            instance_parent = instance.get_editor_property("parent")
        except Exception:
            instance_parent = None
        if instance_parent is None:
            failures.append("{} has no parent material".format(instance_path))
        elif asset_path_without_object(instance_parent) != MASTER_MATERIAL_PATH:
            failures.append("{} has unexpected parent {}".format(instance_path, instance_parent.get_path_name()))

    return instances


def validate_class_socket_contracts(failures):
    for mesh_path, required_sockets in REQUIRED_CLASS_SOCKET_CONTRACTS.items():
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            failures.append("{} failed to load".format(mesh_path))
            continue
        missing_sockets = [
            socket_name
            for socket_name in required_sockets
            if mesh.find_socket(unreal.Name(socket_name)) is None
        ]
        if missing_sockets:
            failures.append("{} missing brand-state sockets {}".format(mesh_path, ", ".join(missing_sockets)))


def main():
    failures = []
    validate_state_instances(failures)
    validate_class_socket_contracts(failures)

    if failures:
        raise RuntimeError("Infernal brand glow state validation failed: {}".format("; ".join(failures)))

    print(
        "Infernal brand glow state validation passed: 1 master material, 1 material function, {} material instances, {} class meshes.".format(
            len(REQUIRED_STATES),
            len(REQUIRED_CLASS_SOCKET_CONTRACTS),
        )
    )


if __name__ == "__main__":
    main()
