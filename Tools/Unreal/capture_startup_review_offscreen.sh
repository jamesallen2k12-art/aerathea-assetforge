#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
UE_EDITOR="${AET_UE_EDITOR:-}"
if [[ -z "${UE_EDITOR}" ]]; then
  for candidate in \
    "/home/james/UnrealEngine/UE_5.8.0/Engine/Binaries/Linux/UnrealEditor" \
    "/home/Flamestrike/UnrealEngine/UE_5.8.0/Engine/Binaries/Linux/UnrealEditor"; do
    if [[ -x "${candidate}" ]]; then
      UE_EDITOR="${candidate}"
      break
    fi
  done
fi
if [[ ! -x "${UE_EDITOR}" ]]; then
  echo "UnrealEditor not found. Set AET_UE_EDITOR to the UnrealEditor binary path." >&2
  exit 1
fi
UPROJECT="${ROOT}/Aerathea.uproject"
MAP_PATH="/Game/Aerathea/Maps/L_Aerathea_Startup"
OUTPUT_PATH="${1:-${ROOT}/Saved/Automation/StartupReview/AeratheaStartupReview_Game4_Offscreen.png}"
if [[ "${OUTPUT_PATH}" != /* ]]; then
  OUTPUT_PATH="${ROOT}/${OUTPUT_PATH}"
fi
VIEW_MODE="${AET_REVIEW_VIEWMODE:-lit}"
SHOW_MARKERS="${AET_REVIEW_MARKERS:-0}"
ENCOUNTER_PHASE="${AET_REVIEW_ENCOUNTER_PHASE:-}"
CAPTURE_DELAY="${AET_REVIEW_CAPTURE_DELAY:-}"
PHASE_FOCUS="${AET_REVIEW_PHASE_FOCUS:-0}"

if [[ "$#" -eq 0 && "${SHOW_MARKERS}" =~ ^(1|true|TRUE|yes|YES|on|ON)$ ]]; then
  OUTPUT_PATH="${ROOT}/Saved/Automation/StartupReview/AeratheaStartupReview_Game4_Markers.png"
fi

MARKER_ARGS=()
if [[ "${SHOW_MARKERS}" =~ ^(1|true|TRUE|yes|YES|on|ON)$ ]]; then
  MARKER_ARGS+=("-AETReviewMarkers")
fi

PHASE_ARGS=()
if [[ -n "${ENCOUNTER_PHASE}" ]]; then
  PHASE_ARGS+=("-AETEncounterPhase=${ENCOUNTER_PHASE}")
fi

DELAY_ARGS=()
if [[ -n "${CAPTURE_DELAY}" ]]; then
  DELAY_ARGS+=("-AETReviewCaptureDelay=${CAPTURE_DELAY}")
fi

FOCUS_ARGS=()
if [[ "${PHASE_FOCUS}" =~ ^(1|true|TRUE|yes|YES|on|ON)$ ]]; then
  FOCUS_ARGS+=("-AETReviewPhaseFocus")
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
  "${PHASE_ARGS[@]}" \
  "${DELAY_ARGS[@]}" \
  "${FOCUS_ARGS[@]}" \
  "-AETReviewViewMode=${VIEW_MODE}" \
  "-AETReviewCaptureFile=${OUTPUT_PATH}"
