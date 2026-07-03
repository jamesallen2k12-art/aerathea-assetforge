#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ENGINE_ROOT="${UE_ENGINE_ROOT:-${HOME}/UnrealEngine/UE_5.8.0}"
PROJECT_FILE="${AET_UPROJECT:-${ROOT}/Aerathea.uproject}"
LOG_DIR="${ROOT}/Saved/Logs"

mkdir -p "${LOG_DIR}"

# Desktop-safe Linux editor route for the RX 7900 XTX workstation.
# Keep Unreal off Wayland and force the AMDGPU Mesa 26 ICD when present.
export SDL_VIDEODRIVER=x11
export QT_QPA_PLATFORM=xcb
unset WAYLAND_DISPLAY
export SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0

if [[ -f /etc/vulkan/icd.d/radeon_icd_amdgpu.x86_64.json ]]; then
  export VK_ICD_FILENAMES=/etc/vulkan/icd.d/radeon_icd_amdgpu.x86_64.json
fi

export MESA_VK_DEVICE_SELECT="${MESA_VK_DEVICE_SELECT:-1002:744c}"
export DISABLE_VK_LAYER_VALVE_steam_overlay_1=1
export DISABLE_VK_LAYER_VALVE_steam_fossilize_1=1
export VK_LOADER_LAYERS_DISABLE="${VK_LOADER_LAYERS_DISABLE:-VK_LAYER_FROG_gamescope_wsi_x86_64,VK_LAYER_VALVE_steam_overlay_32,VK_LAYER_VALVE_steam_overlay_64,VK_LAYER_VALVE_steam_fossilize_32,VK_LAYER_VALVE_steam_fossilize_64}"

exec "${ENGINE_ROOT}/Engine/Binaries/Linux/UnrealEditor" \
  "${PROJECT_FILE}" \
  -vulkan \
  -sm5 \
  -BindlessOff \
  -NoRHIThread \
  -windowed \
  -ResX=1600 \
  -ResY=900 \
  -ForceRes \
  -NoVSync \
  -NoSplash \
  "$@" >>"${LOG_DIR}/DesktopUnrealEditor.log" 2>&1
