#!/usr/bin/env bash
set -euo pipefail

ENGINE_ROOT="/home/Flamestrike/UnrealEngine/UE_5.8.0_preview-1"
PROJECT_FILE="/home/Flamestrike/Projects/Aerathea/Aerathea.uproject"

# Diagnostic only. Previous Aetherium visible-editor logs used this preview
# binary with X11, Vulkan SM5, and bindless disabled.
export SDL_VIDEODRIVER=x11
export QT_QPA_PLATFORM=xcb
unset WAYLAND_DISPLAY
export SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0

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
