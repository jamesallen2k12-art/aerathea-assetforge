#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
SYSTEMD_USER_DIR="${XDG_CONFIG_HOME:-${HOME}/.config}/systemd/user"
SERVICE_PATH="${SYSTEMD_USER_DIR}/aerathea-checkpoint.service"
TIMER_PATH="${SYSTEMD_USER_DIR}/aerathea-checkpoint.timer"

mkdir -p "${SYSTEMD_USER_DIR}"

cat >"${SERVICE_PATH}" <<EOF
[Unit]
Description=Aerathea local recovery checkpoint

[Service]
Type=oneshot
WorkingDirectory=${REPO_ROOT}
ExecStart=${REPO_ROOT}/Tools/System/aerathea_checkpoint.sh --local-only "automatic systemd checkpoint"
EOF

cat >"${TIMER_PATH}" <<'EOF'
[Unit]
Description=Run Aerathea local recovery checkpoint every 30 minutes

[Timer]
OnBootSec=5min
OnUnitActiveSec=30min
Persistent=true
RandomizedDelaySec=2min
Unit=aerathea-checkpoint.service

[Install]
WantedBy=timers.target
EOF

systemctl --user daemon-reload
systemctl --user enable --now aerathea-checkpoint.timer
systemctl --user list-timers aerathea-checkpoint.timer --no-pager

echo
echo "Installed Aerathea checkpoint timer:"
echo "  Service: ${SERVICE_PATH}"
echo "  Timer: ${TIMER_PATH}"
