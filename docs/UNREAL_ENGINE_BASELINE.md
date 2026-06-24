# Unreal Engine Baseline

Aerathea is pinned to the official Linux Unreal Engine 5.8.0 release install:

- Engine path: `/home/Flamestrike/UnrealEngine/UE_5.8.0`
- Version: `5.8.0`
- Changelist: `55116800`
- Branch: `++UE5+Release-5.8`
- Installed from: `/home/Flamestrike/Downloads/Linux_Unreal_Engine_5.8.0.zip`
- Previous preview install kept for rollback: `/home/Flamestrike/UnrealEngine/UE_5.8.0_preview-1`

Use the official engine path explicitly for command-line builds and editor launches until the local desktop association is registered.

## Project Setup Status

- Project file: `/home/Flamestrike/Projects/Aerathea/Aerathea.uproject`
- C++ editor target builds successfully against the official 5.8.0 engine.
- Startup map: `/Game/Aerathea/Maps/L_Aerathea_Startup`
- Startup map file: `Content/Aerathea/Maps/L_Aerathea_Startup.umap`
- Default editor, game, and server maps are set to the Aerathea startup map in `Config/DefaultEngine.ini`.
- Headless validation through `UnrealEditor-Cmd -NullRHI -NoRHIThread` loads the startup map successfully.
- `Tools/Unreal/bootstrap_startup_scene.py` creates the current startup scene and base material assets.
- `Tools/Unreal/validate_startup_scene.py` verifies the startup map, 5 base materials, and 14 expected bootstrap actors.
- Latest map check result: `0 Error(s), 0 Warning(s)`.
- Linux target RHIs include `SF_VULKAN_SM5` and `SF_VULKAN_SM6`.
- SM6 remains the feature/validation target for UE 5.8 rendering features.
- Safe SM6 editor launcher passes `-vulkan -sm6`.
- Visible Linux editor workaround launcher passes `-sm5 -BindlessOff -NoRHIThread` with X11 and fixed 1600x900 startup.
- Current X11 manual-edit launcher loads the project startup map from `Config/DefaultEngine.ini`; it does not force an engine template map.
- Native Wayland SM5 diagnostic launcher exists, but is not the current recommended manual-edit path.
- SM6 validation result: `rhifeaturelevel="SM6"` and `shaderplatform="VULKAN_SM6"` in `Saved/Logs/Aerathea.log`.

## Current GUI Status

The Aerathea project loads correctly through command-line Unreal. A real Plasma X11 session now launches a visible Unreal Editor window through the SM5/bindless-off helper, loads the Aerathea startup map, survives close with `-NoRHIThread`, and relaunches cleanly. Use that as the manual-edit path during bootstrap.

The remaining risk is the Linux SM6/Wayland editor presentation path, which has previously frozen, rendered black, or hit Vulkan device-loss during desktop testing. Treat those failures as GUI/window-system or Vulkan interaction issues until proven otherwise, not as project data failures.

Keep command-line/editor scripting available for setup work and validation. Do not delete the previous preview engine install until the official 5.8.0 GUI path has been exercised across normal edit/save/reopen workflows.

The first SM6 GUI launch initialized as `VULKAN_SM6`, compiled the initial SM6 shaders, then hit a Vulkan device-loss in `LumenReflections`. To keep the editor stable during project bootstrap, Lumen GI/reflections and virtual shadow maps are disabled in `Config/DefaultEngine.ini` while SM6 remains enabled.

Prior Aetherium notes record the known visible-editor workaround for this workstation: use X11, Vulkan SM5, and bindless disabled. The current exact Aerathea helper is:

`Tools/Unreal/launch_aerathea_editor_exact_sm5.sh`

Use that helper when the SM6 editor path opens a black window. Use SM6 command-line validation for feature checks and Nanite-related work until the Linux SM6 editor presentation path is stable.

## 2026-06-24 GUI Findings

- Official UE 5.8.0 release remains the correct project baseline: `/home/Flamestrike/UnrealEngine/UE_5.8.0`, CL `55116800`.
- Official X11/SM5/bindless-off launch renders the editor and viewport under the current KDE Wayland session, but the XWayland window did not accept mouse or keyboard input during testing.
- Native Wayland/SM5/bindless-off launch initializes as `VULKAN_SM5` with `Using SDL video driver 'wayland'`, but the viewport remained visually stuck at `Preparing Shaders (1)` during testing.
- Preview engine `/home/Flamestrike/UnrealEngine/UE_5.8.0_preview-1` is not a valid manual-edit workaround for the updated Aerathea project unless the project is rebuilt against preview; the log reports `Incompatible or missing module: Aerathea`.
- Plasma X11 support has been installed through `plasma-workspace-x11`; `/usr/share/xsessions/plasmax11.desktop` is present.
- Real Plasma X11 session validated on 2026-06-24: `XDG_SESSION_TYPE=x11`, `DISPLAY=:0`.
- `Tools/Unreal/launch_aerathea_editor_exact_sm5.sh` launched a visible editor window titled `Aerathea - Unreal Editor`.
- X11 editor window manager geometry was reported as `3220x1820` at position `103,296`.
- The first X11 launch rebuilt the stale `AeratheaEditor` module successfully against UE 5.8.0 and produced `Binaries/Linux/libUnrealEditor-Aerathea.so`.
- Log confirmation: `Using SDL video driver 'x11'`; Vulkan initialized as `VULKAN_SM5`; Vulkan swapchain created with `VK_PRESENT_MODE_IMMEDIATE_KHR`.
- The Aerathea startup map loaded from `Content/Aerathea/Maps/L_Aerathea_Startup.umap`.
- GUI map check on the loaded startup map completed with `0 Error(s), 0 Warning(s)`.
- `bootstrap_startup_scene.py` completed successfully through `UnrealEditor-Cmd -NullRHI -NoRHIThread` after avoiding the UE 5.8 commandlet `MAP CHECK` crash path.
- `validate_startup_scene.py` completed successfully through `UnrealEditor-Cmd -NullRHI -NoRHIThread`, verifying 6 expected assets and 14 expected actors.
- The first close attempt with RHI threading enabled aborted in `EndDrawingViewport` on the RHI thread. The X11 SM5 helper now includes `-NoRHIThread` for bootstrap stability.
- Clean shutdown was validated with `-NoRHIThread`: no Unreal or CrashReport process remained, and no new `Saved/Crashes` directory was created.
- The editor was relaunched after the shutdown test and left running for manual work.
- Use the X11 SM5 helper as the current manual-edit route:

`/home/Flamestrike/Projects/Aerathea/Tools/Unreal/launch_aerathea_editor_exact_sm5.sh`
