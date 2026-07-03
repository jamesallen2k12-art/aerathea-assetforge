#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date +%Y%m%d-%H%M%S)"
DEST_ROOT="${1:-/backup/Ubuntu22_Migration_${STAMP}/aerathea_protected_set}"
LOG_DIR="${DEST_ROOT}/_logs"

mkdir -p "${LOG_DIR}"

RSYNC_COMMON=(
  -aHAX
  --numeric-ids
  --human-readable
  --info=stats2
  --protect-args
)

copy_path() {
  local src="$1"
  local dest="$2"
  local log_name="$3"

  if [[ ! -e "${src}" ]]; then
    echo "SKIP missing ${src}" | tee -a "${LOG_DIR}/missing.txt"
    return 0
  fi

  mkdir -p "$(dirname "${dest}")"
  echo "Backing up ${src} -> ${dest}"
  rsync "${RSYNC_COMMON[@]}" "${src}" "${dest}" | tee "${LOG_DIR}/${log_name}.log"
}

copy_path /home/Flamestrike/Projects/Aerathea "${DEST_ROOT}/home/Flamestrike/Projects/" "projects_aerathea"
copy_path /home/Flamestrike/Desktop/Aerathea "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_aerathea"
copy_path "/home/Flamestrike/Desktop/Aerathea Abyssal Search Results" "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_aerathea_abyssal_search_results"
copy_path "/home/Flamestrike/Desktop/Aerathea Pending Approval Images" "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_aerathea_pending_approval_images"
copy_path "/home/Flamestrike/Desktop/Aerathea Pending.md" "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_aerathea_pending_md"
copy_path "/home/Flamestrike/Desktop/Aetherium ARPG Derivative Creative Questions.md" "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_aetherium_arpg_questions"
copy_path "/home/Flamestrike/Desktop/Aetherium MMORPG Timeline.md" "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_aetherium_timeline"
copy_path "/home/Flamestrike/Desktop/Aetherium MMORPG.md" "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_aetherium_mmorpg_md"
copy_path /home/Flamestrike/UnrealEngine "${DEST_ROOT}/home/Flamestrike/" "unreal_engine"
copy_path /home/Flamestrike/.config/Epic "${DEST_ROOT}/home/Flamestrike/.config/" "epic_config"
copy_path /home/Flamestrike/.epic "${DEST_ROOT}/home/Flamestrike/" "epic_home"
copy_path /home/Flamestrike/.codex "${DEST_ROOT}/home/Flamestrike/" "codex_home"
copy_path /home/Flamestrike/.hermes "${DEST_ROOT}/home/Flamestrike/" "hermes_home"
copy_path /faststore/AI/hermes "${DEST_ROOT}/faststore/AI/" "faststore_hermes"

find "${DEST_ROOT}" -xdev -type f -printf '%P\t%s\n' | sort >"${LOG_DIR}/file_manifest.tsv"
du -sh "${DEST_ROOT}" >"${LOG_DIR}/backup_size.txt"

cat >"${DEST_ROOT}/RESTORE_NOTES.txt" <<EOF
Protected Aerathea backup created at ${STAMP}.

Restore examples after Ubuntu install:

rsync -aHAX --numeric-ids '${DEST_ROOT}/home/Flamestrike/Projects/Aerathea' /home/Flamestrike/Projects/
rsync -aHAX --numeric-ids '${DEST_ROOT}/home/Flamestrike/Desktop/Aerathea' /home/Flamestrike/Desktop/
rsync -aHAX --numeric-ids '${DEST_ROOT}/home/Flamestrike/UnrealEngine' /home/Flamestrike/
rsync -aHAX --numeric-ids '${DEST_ROOT}/home/Flamestrike/.codex' /home/Flamestrike/
rsync -aHAX --numeric-ids '${DEST_ROOT}/home/Flamestrike/.config/Epic' /home/Flamestrike/.config/
EOF

echo "Aerathea protected backup written to ${DEST_ROOT}"
echo "Manifest: ${LOG_DIR}/file_manifest.tsv"
