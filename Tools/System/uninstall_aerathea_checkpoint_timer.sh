#!/usr/bin/env bash
set -euo pipefail

SYSTEMD_USER_DIR="${XDG_CONFIG_HOME:-${HOME}/.config}/systemd/user"
SERVICE_PATH="${SYSTEMD_USER_DIR}/aerathea-checkpoint.service"
TIMER_PATH="${SYSTEMD_USER_DIR}/aerathea-checkpoint.timer"

systemctl --user disable --now aerathea-checkpoint.timer 2>/dev/null || true
rm -f "${SERVICE_PATH}" "${TIMER_PATH}"
systemctl --user daemon-reload

echo "Removed Aerathea checkpoint timer."
