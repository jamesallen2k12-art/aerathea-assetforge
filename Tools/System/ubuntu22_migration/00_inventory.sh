#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date +%Y%m%d-%H%M%S)"
OUT="${1:-/backup/Ubuntu22_Migration_${STAMP}/inventory}"

mkdir -p "${OUT}"

run() {
  local name="$1"
  shift
  {
    printf '$'
    printf ' %q' "$@"
    printf '\n\n'
    "$@"
  } >"${OUT}/${name}.txt" 2>&1 || true
}

run lsblk lsblk -f -o NAME,SIZE,TYPE,FSTYPE,FSVER,LABEL,UUID,MOUNTPOINTS,MODEL,SERIAL
run df df -hT
run findmnt findmnt -R /
run os_release cat /etc/os-release
run kernel uname -a
run codex_paths find /home/Flamestrike -maxdepth 4 -iname '*codex*'
run aerathea_paths find /home/Flamestrike /faststore -maxdepth 5 '(' -iname '*Aerathea*' -o -iname '*Aetherium*' ')'
run project_creation_paths find /home/Flamestrike/Tools /home/Flamestrike/bin /home/Flamestrike/Downloads /home/Flamestrike/.config /home/Flamestrike/.local/share /home/Flamestrike/.var/app -maxdepth 3 '(' -iname '*armor*' -o -iname '*blender*' -o -iname '*unreal*' -o -iname '*epic*' -o -iname '*krita*' -o -iname '*gimp*' -o -iname '*godot*' -o -iname '*substance*' -o -iname '*fab*' -o -iname '*quixel*' ')'
run creative_tool_commands bash -lc 'command -v blender armorpaint krita gimp godot unreal-engine-installer unreal-linux-download-page legendary gh code || true'
run sizes du -sh /home/Flamestrike/Projects/Aerathea /home/Flamestrike/Desktop/Aerathea /home/Flamestrike/UnrealEngine /home/Flamestrike/.codex /home/Flamestrike/.config/Epic /home/Flamestrike/.local /home/Flamestrike/Tools /home/Flamestrike/bin /home/Flamestrike/android-studio /home/Flamestrike/.var/app/io.github.achetagames.epic_asset_manager /faststore
run git_status git -C /home/Flamestrike/Projects/Aerathea status --short

if command -v rpm >/dev/null 2>&1; then
  rpm -qa | sort >"${OUT}/rpm-installed.txt" 2>&1 || true
fi

if command -v dnf >/dev/null 2>&1; then
  dnf repoquery --userinstalled --qf '%{name}\n' 2>/dev/null | sort >"${OUT}/dnf-userinstalled.txt" || true
fi

if command -v flatpak >/dev/null 2>&1; then
  flatpak list --app --columns=application,name,branch,origin >"${OUT}/flatpak-apps.txt" 2>&1 || true
  flatpak --system list --app --columns=application,name,branch,origin >"${OUT}/flatpak-system-apps.txt" 2>&1 || true
  flatpak --user list --app --columns=application,name,branch,origin >"${OUT}/flatpak-user-apps.txt" 2>&1 || true
fi

if command -v npm >/dev/null 2>&1; then
  npm list -g --depth=0 >"${OUT}/npm-global.txt" 2>&1 || true
fi

cat >"${OUT}/README.txt" <<EOF
Inventory captured at ${STAMP}.

Review these files before installing Ubuntu:
- lsblk.txt
- df.txt
- aerathea_paths.txt
- project_creation_paths.txt
- creative_tool_commands.txt
- sizes.txt
- git_status.txt
- rpm-installed.txt
- dnf-userinstalled.txt
- flatpak-apps.txt
- npm-global.txt
EOF

echo "Inventory written to ${OUT}"
