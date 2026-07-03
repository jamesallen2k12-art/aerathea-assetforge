#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date +%Y%m%d-%H%M%S)"
DEST_ROOT="${1:-/backup/Ubuntu22_Migration_${STAMP}/user_continuity}"
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

copy_path /home/Flamestrike/.ssh "${DEST_ROOT}/home/Flamestrike/" "ssh"
copy_path /home/Flamestrike/.gitconfig "${DEST_ROOT}/home/Flamestrike/" "gitconfig"
copy_path /home/Flamestrike/.gitignore "${DEST_ROOT}/home/Flamestrike/" "gitignore"
copy_path /home/Flamestrike/.bashrc "${DEST_ROOT}/home/Flamestrike/" "bashrc"
copy_path /home/Flamestrike/.bash_profile "${DEST_ROOT}/home/Flamestrike/" "bash_profile"
copy_path /home/Flamestrike/.local/bin "${DEST_ROOT}/home/Flamestrike/.local/" "local_bin"
copy_path /home/Flamestrike/.local/lib/node_modules/@openai "${DEST_ROOT}/home/Flamestrike/.local/lib/node_modules/" "openai_node_modules"
copy_path /home/Flamestrike/.npmrc "${DEST_ROOT}/home/Flamestrike/" "npmrc"
copy_path /home/Flamestrike/.mozilla "${DEST_ROOT}/home/Flamestrike/" "mozilla"
copy_path /home/Flamestrike/.config/google-chrome "${DEST_ROOT}/home/Flamestrike/.config/" "google_chrome"
copy_path /home/Flamestrike/.config/Code "${DEST_ROOT}/home/Flamestrike/.config/" "vscode_config"
copy_path /home/Flamestrike/.config/gh "${DEST_ROOT}/home/Flamestrike/.config/" "gh_config"
copy_path /home/Flamestrike/.ollama "${DEST_ROOT}/home/Flamestrike/" "ollama_config"

if command -v dnf >/dev/null 2>&1; then
  dnf repoquery --userinstalled --qf '%{name}\n' 2>/dev/null | sort >"${LOG_DIR}/dnf-userinstalled.txt" || true
fi

if command -v rpm >/dev/null 2>&1; then
  rpm -qa | sort >"${LOG_DIR}/rpm-installed.txt" 2>&1 || true
fi

if command -v flatpak >/dev/null 2>&1; then
  flatpak list --app --columns=application,name,branch,origin >"${LOG_DIR}/flatpak-apps.txt" 2>&1 || true
  flatpak --system list --app --columns=application,name,branch,origin >"${LOG_DIR}/flatpak-system-apps.txt" 2>&1 || true
  flatpak --user list --app --columns=application,name,branch,origin >"${LOG_DIR}/flatpak-user-apps.txt" 2>&1 || true
fi

if command -v npm >/dev/null 2>&1; then
  npm list -g --depth=0 >"${LOG_DIR}/npm-global.txt" 2>&1 || true
fi

find "${DEST_ROOT}" -xdev -type f -printf '%P\t%s\n' | sort >"${LOG_DIR}/file_manifest.tsv"
du -sh "${DEST_ROOT}" >"${LOG_DIR}/backup_size.txt"

cat >"${DEST_ROOT}/RESTORE_CODEX_NOTES.txt" <<'EOF'
After Ubuntu install:

1. Install prerequisites:
   sudo apt update
   sudo apt install -y git curl nodejs npm ripgrep rsync gh

2. Restore Codex config and install:
   rsync -aHAX --numeric-ids /backup/.../user_continuity/home/Flamestrike/.local/bin /home/Flamestrike/.local/
   rsync -aHAX --numeric-ids /backup/.../user_continuity/home/Flamestrike/.local/lib/node_modules/@openai /home/Flamestrike/.local/lib/node_modules/
   rsync -aHAX --numeric-ids /backup/.../aerathea_protected_set/home/Flamestrike/.codex /home/Flamestrike/

3. If the copied Codex binary does not run because Node changed:
   npm install -g @openai/codex@0.142.4

4. Keep /home/Flamestrike/.local/bin on PATH.
EOF

echo "User continuity backup written to ${DEST_ROOT}"
echo "Manifest: ${LOG_DIR}/file_manifest.tsv"
