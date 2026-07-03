#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
UE_EDITOR="${UE_EDITOR:-${HOME}/UnrealEngine/UE_5.8.0/Engine/Binaries/Linux/UnrealEditor}"
UPROJECT="${ROOT}/Aerathea.uproject"
MAP_PATH="/Game/Aerathea/Maps/L_Aerathea_ReviewIsland"
OUTPUT_PATH="${1:-${ROOT}/Saved/Automation/ReviewIsland/AeratheaReviewIsland_Offscreen.png}"
VIEW_MODE="${2:-${AET_REVIEW_VIEWMODE:-unlit}}"
CAPTURE_DELAY="${AET_REVIEW_CAPTURE_DELAY:-}"

if [[ "${OUTPUT_PATH}" != /* ]]; then
  OUTPUT_PATH="${ROOT}/${OUTPUT_PATH}"
fi

DELAY_ARGS=()
if [[ -n "${CAPTURE_DELAY}" ]]; then
  DELAY_ARGS+=("-AETReviewCaptureDelay=${CAPTURE_DELAY}")
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
  "${DELAY_ARGS[@]}" \
  "-AETReviewViewMode=${VIEW_MODE}" \
  "-AETReviewCaptureFile=${OUTPUT_PATH}"
