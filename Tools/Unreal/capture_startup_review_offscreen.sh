#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
UE_EDITOR="/home/Flamestrike/UnrealEngine/UE_5.8.0/Engine/Binaries/Linux/UnrealEditor"
UPROJECT="${ROOT}/Aerathea.uproject"
MAP_PATH="/Game/Aerathea/Maps/L_Aerathea_Startup"
OUTPUT_PATH="${1:-${ROOT}/Saved/Automation/StartupReview/AeratheaStartupReview_Game4_Offscreen.png}"
if [[ "${OUTPUT_PATH}" != /* ]]; then
  OUTPUT_PATH="${ROOT}/${OUTPUT_PATH}"
fi
VIEW_MODE="${AET_REVIEW_VIEWMODE:-lit}"
SHOW_MARKERS="${AET_REVIEW_MARKERS:-0}"

if [[ "$#" -eq 0 && "${SHOW_MARKERS}" =~ ^(1|true|TRUE|yes|YES|on|ON)$ ]]; then
  OUTPUT_PATH="${ROOT}/Saved/Automation/StartupReview/AeratheaStartupReview_Game4_Markers.png"
fi

MARKER_ARGS=()
if [[ "${SHOW_MARKERS}" =~ ^(1|true|TRUE|yes|YES|on|ON)$ ]]; then
  MARKER_ARGS+=("-AETReviewMarkers")
fi

mkdir -p "$(dirname "${OUTPUT_PATH}")"

timeout 90s "${UE_EDITOR}" "${UPROJECT}" "${MAP_PATH}" \
  -game \
  -RenderOffscreen \
  -Unattended \
  -NoSplash \
  -sm5 \
  -BindlessOff \
  -NoRHIThread \
  -ResX=1280 \
  -ResY=720 \
  -ForceRes \
  -NoVSync \
  -log \
  -AETReviewCapture \
  -AETReviewCaptureExit \
  "${MARKER_ARGS[@]}" \
  "-AETReviewViewMode=${VIEW_MODE}" \
  "-AETReviewCaptureFile=${OUTPUT_PATH}"
