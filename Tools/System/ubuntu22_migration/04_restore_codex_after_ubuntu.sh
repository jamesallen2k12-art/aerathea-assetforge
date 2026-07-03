#!/usr/bin/env bash
set -euo pipefail

BACKUP_ROOT="${1:-}"

if [[ -z "${BACKUP_ROOT}" ]]; then
  echo "Usage: $0 /backup/Ubuntu22_Migration_YYYYMMDD-HHMMSS" >&2
  exit 1
fi

if [[ ! -d "${BACKUP_ROOT}" ]]; then
  echo "Backup root does not exist: ${BACKUP_ROOT}" >&2
  exit 1
fi

mkdir -p /home/Flamestrike/.local/lib/node_modules /home/Flamestrike/.config /home/Flamestrike/Projects

if [[ -d "${BACKUP_ROOT}/aerathea_protected_set/home/Flamestrike/.codex" ]]; then
  rsync -aHAX --numeric-ids "${BACKUP_ROOT}/aerathea_protected_set/home/Flamestrike/.codex" /home/Flamestrike/
fi

if [[ -d "${BACKUP_ROOT}/user_continuity/home/Flamestrike/.local/bin" ]]; then
  rsync -aHAX --numeric-ids "${BACKUP_ROOT}/user_continuity/home/Flamestrike/.local/bin" /home/Flamestrike/.local/
fi

if [[ -d "${BACKUP_ROOT}/user_continuity/home/Flamestrike/.local/lib/node_modules/@openai" ]]; then
  rsync -aHAX --numeric-ids "${BACKUP_ROOT}/user_continuity/home/Flamestrike/.local/lib/node_modules/@openai" /home/Flamestrike/.local/lib/node_modules/
fi

for item in .ssh .gitconfig .gitignore .bashrc .bash_profile .npmrc; do
  if [[ -e "${BACKUP_ROOT}/user_continuity/home/Flamestrike/${item}" ]]; then
    rsync -aHAX --numeric-ids "${BACKUP_ROOT}/user_continuity/home/Flamestrike/${item}" /home/Flamestrike/
  fi
done

if [[ -d "${BACKUP_ROOT}/aerathea_protected_set/home/Flamestrike/Projects/Aerathea" ]]; then
  rsync -aHAX --numeric-ids "${BACKUP_ROOT}/aerathea_protected_set/home/Flamestrike/Projects/Aerathea" /home/Flamestrike/Projects/
fi

if [[ -d "${BACKUP_ROOT}/project_creation_tools/home/Flamestrike/Tools" ]]; then
  rsync -aHAX --numeric-ids "${BACKUP_ROOT}/project_creation_tools/home/Flamestrike/Tools" /home/Flamestrike/
fi

if [[ -d "${BACKUP_ROOT}/project_creation_tools/home/Flamestrike/bin" ]]; then
  rsync -aHAX --numeric-ids "${BACKUP_ROOT}/project_creation_tools/home/Flamestrike/bin" /home/Flamestrike/
fi

if [[ -d "${BACKUP_ROOT}/project_creation_tools/home/Flamestrike/.local/share/applications" ]]; then
  mkdir -p /home/Flamestrike/.local/share
  rsync -aHAX --numeric-ids "${BACKUP_ROOT}/project_creation_tools/home/Flamestrike/.local/share/applications" /home/Flamestrike/.local/share/
fi

chown -R Flamestrike:Flamestrike /home/Flamestrike/.codex /home/Flamestrike/.local /home/Flamestrike/Projects/Aerathea /home/Flamestrike/Tools /home/Flamestrike/bin 2>/dev/null || true

echo "Codex/Aerathea continuity restore attempted from ${BACKUP_ROOT}"
echo "If codex does not run, install Node/npm and run: npm install -g @openai/codex@0.142.4"
