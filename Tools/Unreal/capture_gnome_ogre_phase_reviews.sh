#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUTPUT_DIR="${1:-${ROOT}/Saved/Automation/GnomeOgrePhaseReview}"
if [[ "${OUTPUT_DIR}" != /* ]]; then
  OUTPUT_DIR="${ROOT}/${OUTPUT_DIR}"
fi

CAPTURE_DELAY="${AET_REVIEW_CAPTURE_DELAY:-0.45}"
PHASE_FOCUS="${AET_REVIEW_PHASE_FOCUS:-1}"
VIEW_MODE="${AET_REVIEW_VIEWMODE:-unlit}"
PHASES=(
  "ShieldImpact"
  "PylonOverload"
  "CasterReinforcement"
  "ManticoreInterrupt"
)

mkdir -p "${OUTPUT_DIR}"

for PHASE in "${PHASES[@]}"; do
  AET_REVIEW_ENCOUNTER_PHASE="${PHASE}" \
  AET_REVIEW_CAPTURE_DELAY="${CAPTURE_DELAY}" \
  AET_REVIEW_PHASE_FOCUS="${PHASE_FOCUS}" \
  AET_REVIEW_VIEWMODE="${VIEW_MODE}" \
  "${ROOT}/Tools/Unreal/capture_startup_review_offscreen.sh" \
    "${OUTPUT_DIR}/AeratheaStartupReview_${PHASE}.png"
done
