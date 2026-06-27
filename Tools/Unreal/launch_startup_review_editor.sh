#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

exec "${ROOT}/Tools/Unreal/launch_aerathea_editor_exact_sm5.sh" \
  /Game/Aerathea/Maps/L_Aerathea_Startup \
  -ExecutePythonScript="${ROOT}/Tools/Unreal/prepare_startup_visual_review.py" \
  "$@"
