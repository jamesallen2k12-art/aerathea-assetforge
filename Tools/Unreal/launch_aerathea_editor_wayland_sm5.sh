#!/usr/bin/env bash
set -euo pipefail

ENGINE_ROOT="/home/Flamestrike/UnrealEngine/UE_5.8.0"
PROJECT_FILE="/home/Flamestrike/Projects/Aerathea/Aerathea.uproject"

# Native Wayland diagnostic route: keep the visible SM5/bindless-off renderer
# while avoiding the X11/XWayland input path.
export SDL_VIDEODRIVER=wayland
export QT_QPA_PLATFORM=wayland
export XDG_SESSION_TYPE=wayland
export WAYLAND_DISPLAY="${WAYLAND_DISPLAY:-wayland-0}"
export SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0
export DISABLE_VK_LAYER_VALVE_steam_overlay_1=1
export DISABLE_VK_LAYER_VALVE_steam_fossilize_1=1
export VK_LOADER_LAYERS_DISABLE="VK_LAYER_FROG_gamescope_wsi_x86_64,VK_LAYER_VALVE_steam_overlay_32,VK_LAYER_VALVE_steam_overlay_64,VK_LAYER_VALVE_steam_fossilize_32,VK_LAYER_VALVE_steam_fossilize_64"
export MESA_VK_DEVICE_SELECT=1002:744c

exec "${ENGINE_ROOT}/Engine/Binaries/Linux/UnrealEditor" \
  "${PROJECT_FILE}" \
  /Engine/Maps/Templates/Template_Default \
  -NoSplash \
  -sm5 \
  -BindlessOff \
  -windowed \
  -ResX=1600 \
  -ResY=900 \
  -ForceRes \
  -NoVSync \
  -log \
  "$@"
