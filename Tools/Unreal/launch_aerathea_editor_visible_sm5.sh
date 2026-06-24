#!/usr/bin/env bash
set -euo pipefail

ENGINE_ROOT="/home/Flamestrike/UnrealEngine/UE_5.8.0"
PROJECT_FILE="/home/Flamestrike/Projects/Aerathea/Aerathea.uproject"

# Known visible-editor route on this Fedora KDE workstation.
# SM6 remains enabled in project settings, but the Linux SM6/bindless editor
# presentation path can render as a black window.
export SDL_VIDEODRIVER=x11
export QT_QPA_PLATFORM=xcb
unset WAYLAND_DISPLAY
export SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0
export DISABLE_VK_LAYER_VALVE_steam_overlay_1=1
export DISABLE_VK_LAYER_VALVE_steam_fossilize_1=1
export VK_LOADER_LAYERS_DISABLE="VK_LAYER_FROG_gamescope_wsi_x86_64,VK_LAYER_VALVE_steam_overlay_32,VK_LAYER_VALVE_steam_overlay_64,VK_LAYER_VALVE_steam_fossilize_32,VK_LAYER_VALVE_steam_fossilize_64"

# Mesa lists the display-connected RX 7900 XTX first: 0000:0d:00.0.
export MESA_VK_DEVICE_SELECT=1002:744c

exec "${ENGINE_ROOT}/Engine/Binaries/Linux/UnrealEditor" \
  "${PROJECT_FILE}" \
  -vulkan \
  -sm5 \
  -BindlessOff \
  -windowed \
  -ResX=1280 \
  -ResY=720 \
  -NoSplash \
  -NoLiveCoding \
  -log \
  "$@"
