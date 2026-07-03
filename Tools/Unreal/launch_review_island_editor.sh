#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export AET_REVIEW_AUTO_PLAY="${AET_REVIEW_AUTO_PLAY:-0}"

exec "${SCRIPT_DIR}/launch_aerathea_editor_exact_sm5.sh" \
  /Game/Aerathea/Maps/L_Aerathea_ReviewIsland \
  -ExecutePythonScript="${SCRIPT_DIR}/apply_review_island_viewport.py" \
  -AETReviewViewMode=unlit \
  "$@"
