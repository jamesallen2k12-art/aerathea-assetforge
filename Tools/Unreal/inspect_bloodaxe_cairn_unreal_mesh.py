import unreal


MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady"


def asset_path(asset):
    if asset is None:
        return "<none>"
    return asset.get_path_name().split(".", 1)[0]


def main():
    mesh = unreal.load_asset(MESH_PATH)
    if mesh is None:
        raise RuntimeError("Missing mesh {}".format(MESH_PATH))

    bounds = mesh.get_bounds()
    extent = bounds.get_editor_property("box_extent")
    origin = bounds.get_editor_property("origin")
    unreal.log("INSPECT mesh={}".format(mesh.get_path_name()))
    unreal.log(
        "INSPECT bounds origin=({:.2f},{:.2f},{:.2f}) size=({:.2f},{:.2f},{:.2f})".format(
            origin.x,
            origin.y,
            origin.z,
            extent.x * 2.0,
            extent.y * 2.0,
            extent.z * 2.0,
        )
    )

    slots = list(mesh.get_editor_property("static_materials"))
    unreal.log("INSPECT material_slot_count={}".format(len(slots)))
    for index, slot in enumerate(slots):
        name = slot.get_editor_property("material_slot_name")
        interface = slot.get_editor_property("material_interface")
        unreal.log(
            "INSPECT slot[{}] name={} material={}".format(
                index,
                name,
                asset_path(interface),
            )
        )

    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is None:
        unreal.log_warning("INSPECT StaticMeshEditorSubsystem unavailable")
        return

    try:
        unreal.log("INSPECT lod_count={}".format(subsystem.get_lod_count(mesh)))
    except Exception as exc:
        unreal.log_warning("INSPECT get_lod_count failed: {}".format(exc))

    method_names = [name for name in dir(subsystem) if "section" in name.lower() or "lod" in name.lower() or "material" in name.lower()]
    unreal.log("INSPECT subsystem_methods={}".format(", ".join(sorted(method_names))))

    for method_name in (
        "get_lod_section_count",
        "get_num_sections",
        "get_number_sections",
        "get_lod_sections",
        "get_section_info",
        "get_material_index",
    ):
        if not hasattr(subsystem, method_name):
            continue
        method = getattr(subsystem, method_name)
        for args in ((mesh, 0), (mesh, 0, 0), (mesh, 0, 0, 0)):
            try:
                result = method(*args)
            except Exception:
                continue
            unreal.log("INSPECT {}{} -> {}".format(method_name, args[1:], result))
            break


main()
