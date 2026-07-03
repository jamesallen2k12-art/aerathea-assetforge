#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ENGINE_ROOT="${UE_ENGINE_ROOT:-${HOME}/UnrealEngine/UE_5.8.0}"
PROJECT_FILE="${AET_UPROJECT:-${ROOT}/Aerathea.uproject}"

# Mirrors the last known visible Linux editor route recorded in the Aetherium
# notes: X11, Vulkan SM5, bindless disabled, fixed window size, no VSync.
# RHI threading is disabled during bootstrap because the X11 SM5 editor route
# can abort in EndDrawingViewport on shutdown with the RHI thread enabled.
export SDL_VIDEODRIVER=x11
export QT_QPA_PLATFORM=xcb
unset WAYLAND_DISPLAY
export SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0

exec "${ENGINE_ROOT}/Engine/Binaries/Linux/UnrealEditor" \
  "${PROJECT_FILE}" \
  -NoSplash \
  -sm5 \
  -BindlessOff \
  -NoRHIThread \
  -windowed \
  -ResX=1600 \
  -ResY=900 \
  -ForceRes \
  -NoVSync \
  -log \
  "$@"
