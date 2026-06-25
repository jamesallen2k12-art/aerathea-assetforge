import unreal


for name in dir(unreal):
    if "screenshot" in name.lower() or "automation" in name.lower():
        unreal.log("API {}".format(name))

for obj_name in ("AutomationLibrary", "AutomationEditorTask", "ScreenshotFunctionalTest"):
    obj = getattr(unreal, obj_name, None)
    if obj is None:
        continue
    unreal.log("METHODS {}".format(obj_name))
    for method in dir(obj):
        if obj_name == "AutomationEditorTask" or "screenshot" in method.lower() or "camera" in method.lower() or "take" in method.lower():
            unreal.log("  {}".format(method))
            member = getattr(obj, method, None)
            doc = getattr(member, "__doc__", None)
            if doc:
                unreal.log("    DOC {}".format(doc.replace("\n", " | ")))
