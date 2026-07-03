#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
STAMP="$(date '+%Y%m%d-%H%M%S')"
HUMAN_TIME="$(date '+%Y-%m-%d %H:%M:%S %Z %z')"
LOCAL_ONLY="${AET_CHECKPOINT_LOCAL_ONLY:-0}"

if [[ "${1:-}" == "--local-only" ]]; then
  LOCAL_ONLY=1
  shift
fi

NOTE="${*:-manual checkpoint}"

JOURNAL="${REPO_ROOT}/docs/projects/assetforge/RECOVERY_JOURNAL.md"
SNAPSHOT_DIR="${REPO_ROOT}/Saved/ProjectRecovery/${STAMP}"
mkdir -p "${SNAPSHOT_DIR}" "$(dirname "${JOURNAL}")"

run_capture() {
  local label="$1"
  shift
  {
    echo "# ${label}"
    echo
    "$@"
  } >"${SNAPSHOT_DIR}/${label}.txt" 2>&1 || true
}

run_capture "git_status_short" git -C "${REPO_ROOT}" status --short
run_capture "git_status_branch" git -C "${REPO_ROOT}" status --short --branch
run_capture "git_log_recent" git -C "${REPO_ROOT}" log --oneline --decorate -12
run_capture "git_diff_stat" git -C "${REPO_ROOT}" diff --stat
run_capture "disk_free" df -h "${REPO_ROOT}" /tmp
run_capture "project_disk_usage" du -sh "${REPO_ROOT}/docs" "${REPO_ROOT}/Saved" "${REPO_ROOT}/Tools/External"
run_capture "long_job_processes" pgrep -af 'Unreal|ShaderCompileWorker|blender|trellis|AssetForge|python'

write_recent_files() {
  local output="$1"
  local limit="$2"
  shift 2
  local raw="${output}.all"
  local sorted="${output}.sorted"

  find "$@" -type f -printf '%T@ %TY-%Tm-%Td %TH:%TM:%TS %p\n' >"${raw}" 2>/dev/null || true
  sort -nr "${raw}" >"${sorted}" 2>/dev/null || true
  head -"${limit}" "${sorted}" >"${output}" 2>/dev/null || true
}

write_recent_files "${SNAPSHOT_DIR}/assetforge_tracked_docs.txt" 80 \
  "${REPO_ROOT}/docs/projects/assetforge"
write_recent_files "${SNAPSHOT_DIR}/assetforge_recent_saved_outputs.txt" 200 \
  "${REPO_ROOT}/Saved/AssetForgeResearch"
write_recent_files "${SNAPSHOT_DIR}/recent_project_files.txt" 80 \
  "${REPO_ROOT}/docs" "${REPO_ROOT}/Tools" "${REPO_ROOT}/SourceAssets"

if [[ ! -f "${JOURNAL}" ]]; then
  cat >"${JOURNAL}" <<'EOF'
# AssetForge Recovery Journal

Status: Active

## Entries

EOF
fi

HEAD="$(git -C "${REPO_ROOT}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
BRANCH="$(git -C "${REPO_ROOT}" branch --show-current 2>/dev/null || echo unknown)"
STATUS_COUNT="$(git -C "${REPO_ROOT}" status --short 2>/dev/null | wc -l | tr -d ' ')"

if [[ "${LOCAL_ONLY}" == "1" ]]; then
  LOCAL_LOG="${REPO_ROOT}/Saved/ProjectRecovery/LOCAL_CHECKPOINTS.md"
  LATEST="${REPO_ROOT}/Saved/ProjectRecovery/LATEST.md"

  cat >"${LATEST}" <<EOF
# Latest Aerathea Local Checkpoint

- Time: ${HUMAN_TIME}
- Note: ${NOTE}
- Snapshot: \`Saved/ProjectRecovery/${STAMP}/\`
- Git: branch \`${BRANCH}\`, HEAD \`${HEAD}\`, status lines \`${STATUS_COUNT}\`
- Resume: inspect \`Saved/ProjectRecovery/${STAMP}/git_status_short.txt\` and \`Saved/ProjectRecovery/${STAMP}/recent_project_files.txt\`.
EOF

  cat >>"${LOCAL_LOG}" <<EOF

### ${HUMAN_TIME} - ${NOTE}

- Snapshot: \`Saved/ProjectRecovery/${STAMP}/\`
- Git: branch \`${BRANCH}\`, HEAD \`${HEAD}\`, status lines \`${STATUS_COUNT}\`
EOF

  echo "Local checkpoint written:"
  echo "  Latest: ${LATEST}"
  echo "  Snapshot: ${SNAPSHOT_DIR}"
  exit 0
fi

cat >>"${JOURNAL}" <<EOF

### ${HUMAN_TIME} - ${NOTE}

- Snapshot: \`Saved/ProjectRecovery/${STAMP}/\`
- Git: branch \`${BRANCH}\`, HEAD \`${HEAD}\`, status lines \`${STATUS_COUNT}\`
- Recovery files:
  - \`Saved/ProjectRecovery/${STAMP}/git_status_short.txt\`
  - \`Saved/ProjectRecovery/${STAMP}/recent_project_files.txt\`
  - \`Saved/ProjectRecovery/${STAMP}/assetforge_recent_saved_outputs.txt\`
- Next resume step: read this entry, then inspect the snapshot folder before continuing any interrupted long job.
EOF

echo "Checkpoint written:"
echo "  Journal: ${JOURNAL}"
echo "  Snapshot: ${SNAPSHOT_DIR}"
