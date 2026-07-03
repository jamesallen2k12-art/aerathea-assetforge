import unreal


MAGE_MESH_PATH = "/Game/Aerathea/Characters/Infernals/Mage/SK_INF_Mage_A01"
MATERIAL_PATH = "/Game/Aerathea/Materials/Infernals/VFX"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
VFX_PATH = "/Game/Aerathea/VFX/Infernals/AbyssalSpellcasting"


REQUIRED_PARENT_MATERIALS = [
    "M_INF_AbyssalArc_A01",
    "M_INF_AbyssalFlame_A01",
    "M_INF_BrandPulse_A01",
    "M_INF_EyeReveal_A01",
    "M_INF_AshMote_A01",
]


REQUIRED_MATERIAL_INSTANCES = [
    "MI_INF_AbyssalArc_A01",
    "MI_INF_AbyssalFlame_A01",
    "MI_INF_BrandPulse_A01",
    "MI_INF_EyeReveal_A01",
    "MI_INF_AshMote_A01",
]


REQUIRED_NIAGARA_SYSTEMS = [
    "NS_INF_AbyssalHandCharge_A01",
    "NS_INF_AbyssalBolt_A01",
    "NS_INF_ClawSlashCast_A01",
    "NS_INF_BrandChannel_A01",
    "NS_INF_RegenerationFlare_A01",
    "NS_INF_InvisibleSightReveal_A01",
    "NS_INF_WingMantleCast_A01",
    "NS_INF_RageSurge_A01",
]


REQUIRED_NIAGARA_EMITTERS = [
    "NE_INF_AbyssalArc_A01",
    "NE_INF_AbyssalFlame_A01",
    "NE_INF_BrandPulse_A01",
    "NE_INF_EyeReveal_A01",
    "NE_INF_AshMote_A01",
]


REQUIRED_MAGE_SOCKETS = [
    "hand_l_cast",
    "hand_r_cast",
    "vfx_hand_l",
    "vfx_hand_r",
    "vfx_eye_l",
    "vfx_eye_r",
    "vfx_brand_chest",
    "vfx_brand_forearm_l",
    "vfx_brand_forearm_r",
    "vfx_wing_root_l",
    "vfx_wing_root_r",
    "vfx_tail_tip",
    "vfx_regen_core",
    "vfx_sorcerer_focus",
    "vfx_mouth",
]


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def validate_asset_group(failures, base_path, asset_names):
    loaded = []
    for asset_name in asset_names:
        asset_path = "{}/{}".format(base_path, asset_name)
        asset = unreal.load_asset(asset_path)
        if asset is None:
            failures.append("{} failed to load".format(asset_path))
        else:
            loaded.append(asset)
    return loaded


def validate_material_instances(failures):
    parents_by_name = {
        asset.get_name(): asset
        for asset in validate_asset_group(failures, MATERIAL_PATH, REQUIRED_PARENT_MATERIALS)
    }
    instances = validate_asset_group(failures, MATERIAL_INSTANCE_PATH, REQUIRED_MATERIAL_INSTANCES)
    for instance in instances:
        parent = None
        try:
            parent = instance.get_editor_property("parent")
        except Exception:
            parent = None
        if parent is None:
            failures.append("{} has no parent material".format(instance.get_path_name()))
            continue
        if asset_path_without_object(parent) not in {
            "{}/{}".format(MATERIAL_PATH, parent_name)
            for parent_name in parents_by_name
        }:
            failures.append("{} has unexpected parent {}".format(instance.get_path_name(), parent.get_path_name()))


def validate_mage_socket_contract(failures):
    mesh = unreal.load_asset(MAGE_MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(MAGE_MESH_PATH))
        return

    missing_sockets = [
        socket_name
        for socket_name in REQUIRED_MAGE_SOCKETS
        if mesh.find_socket(unreal.Name(socket_name)) is None
    ]
    if missing_sockets:
        failures.append("{} missing VFX sockets {}".format(MAGE_MESH_PATH, ", ".join(missing_sockets)))


def main():
    failures = []
    validate_material_instances(failures)
    validate_asset_group(failures, VFX_PATH, REQUIRED_NIAGARA_SYSTEMS)
    validate_asset_group(failures, VFX_PATH, REQUIRED_NIAGARA_EMITTERS)
    validate_mage_socket_contract(failures)

    if failures:
        raise RuntimeError("Infernal abyssal spellcasting VFX validation failed: {}".format("; ".join(failures)))

    print(
        "Infernal abyssal spellcasting VFX validation passed: {} systems, {} emitters, {} material instances, {} Mage sockets.".format(
            len(REQUIRED_NIAGARA_SYSTEMS),
            len(REQUIRED_NIAGARA_EMITTERS),
            len(REQUIRED_MATERIAL_INSTANCES),
            len(REQUIRED_MAGE_SOCKETS),
        )
    )


if __name__ == "__main__":
    main()
