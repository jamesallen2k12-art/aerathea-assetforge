#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date +%Y%m%d-%H%M%S)"
DEST_ROOT="${1:-/backup/Ubuntu22_Migration_${STAMP}/project_creation_tools}"
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

# Local creative app trees and launch helpers.
copy_path /home/Flamestrike/Tools "${DEST_ROOT}/home/Flamestrike/" "home_tools"
copy_path /home/Flamestrike/bin "${DEST_ROOT}/home/Flamestrike/" "home_bin"
copy_path /home/Flamestrike/.local/bin "${DEST_ROOT}/home/Flamestrike/.local/" "local_bin"
copy_path /home/Flamestrike/.local/lib/node_modules/@openai "${DEST_ROOT}/home/Flamestrike/.local/lib/node_modules/" "local_openai_node_modules"
copy_path /home/Flamestrike/android-studio "${DEST_ROOT}/home/Flamestrike/" "android_studio"
copy_path /home/Flamestrike/.local/share/applications "${DEST_ROOT}/home/Flamestrike/.local/share/" "local_applications"
copy_path /home/Flamestrike/Desktop/Epic\ Asset\ Manager.desktop "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_epic_asset_manager"
copy_path /home/Flamestrike/Desktop/Unreal\ Engine\ Setup.desktop "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_unreal_engine_setup"
copy_path /home/Flamestrike/Desktop/Unreal\ Engine\ Linux\ Download.desktop "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_unreal_linux_download"
copy_path /home/Flamestrike/Desktop/Unreal\ Engine\ 5.8\ Preview.desktop "${DEST_ROOT}/home/Flamestrike/Desktop/" "desktop_unreal_preview"

# App data and settings for creation tools.
copy_path /home/Flamestrike/.config/Unreal\ Engine "${DEST_ROOT}/home/Flamestrike/.config/" "unreal_engine_config"
copy_path /home/Flamestrike/.cache/Epic "${DEST_ROOT}/home/Flamestrike/.cache/" "epic_cache"
copy_path /home/Flamestrike/.var/app/io.github.achetagames.epic_asset_manager "${DEST_ROOT}/home/Flamestrike/.var/app/" "epic_asset_manager_var"
copy_path /home/Flamestrike/.config/blender "${DEST_ROOT}/home/Flamestrike/.config/" "blender_config"
copy_path /home/Flamestrike/.cache/blender "${DEST_ROOT}/home/Flamestrike/.cache/" "blender_cache"
copy_path /home/Flamestrike/.config/krita "${DEST_ROOT}/home/Flamestrike/.config/" "krita_config"
copy_path /home/Flamestrike/.local/share/krita "${DEST_ROOT}/home/Flamestrike/.local/share/" "krita_share"
copy_path /home/Flamestrike/.config/GIMP "${DEST_ROOT}/home/Flamestrike/.config/" "gimp_config"

# Installer/source archives that may be slow or impossible to reacquire during migration.
copy_path /home/Flamestrike/Downloads/ArmorPaint_10alpha_linux64.zip "${DEST_ROOT}/home/Flamestrike/Downloads/" "download_armorpaint"
copy_path /home/Flamestrike/Downloads/Linux_Unreal_Engine_5.8.0.zip "${DEST_ROOT}/home/Flamestrike/Downloads/" "download_unreal_580"
copy_path /home/Flamestrike/Downloads/Linux_Unreal_Engine_5.8.0_preview-1.zip "${DEST_ROOT}/home/Flamestrike/Downloads/" "download_unreal_580_preview"
copy_path /home/Flamestrike/Downloads/EpicInstaller-20.1.0-unrealEngine-0e14de4e99434f4f87e705d0d6ff74d1.exe "${DEST_ROOT}/home/Flamestrike/Downloads/" "download_epic_installer_1"
copy_path /home/Flamestrike/Downloads/EpicInstaller-20.1.0-unrealEngine-0e14de4e99434f4f87e705d0d6ff74d1\ \(1\).exe "${DEST_ROOT}/home/Flamestrike/Downloads/" "download_epic_installer_2"
copy_path /home/Flamestrike/Downloads/EpicInstaller-20.1.0-unrealEngine-6a454fa0e02340abb56d1dfade8306a6.exe "${DEST_ROOT}/home/Flamestrike/Downloads/" "download_epic_installer_3"
copy_path /home/Flamestrike/Downloads/Unreal_Map_Port_Package "${DEST_ROOT}/home/Flamestrike/Downloads/" "download_unreal_map_port_package"
copy_path /home/Flamestrike/Downloads/Unreal_Map_Port_Package.zip "${DEST_ROOT}/home/Flamestrike/Downloads/" "download_unreal_map_port_zip"

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

bash -lc 'command -v blender armorpaint krita gimp godot unreal-engine-installer unreal-linux-download-page legendary gh code || true' >"${LOG_DIR}/creative-tool-commands.txt" 2>&1 || true

find "${DEST_ROOT}" -xdev -type f -printf '%P\t%s\n' | sort >"${LOG_DIR}/file_manifest.tsv"
du -sh "${DEST_ROOT}" >"${LOG_DIR}/backup_size.txt"

cat >"${DEST_ROOT}/RESTORE_PROJECT_CREATION_TOOLS.txt" <<'EOF'
Project creation tools backup.

Local/self-contained tools can be restored with rsync:

rsync -aHAX --numeric-ids /backup/.../project_creation_tools/home/Flamestrike/Tools /home/Flamestrike/
rsync -aHAX --numeric-ids /backup/.../project_creation_tools/home/Flamestrike/bin /home/Flamestrike/
rsync -aHAX --numeric-ids /backup/.../project_creation_tools/home/Flamestrike/.local/bin /home/Flamestrike/.local/
rsync -aHAX --numeric-ids /backup/.../project_creation_tools/home/Flamestrike/.local/lib/node_modules/@openai /home/Flamestrike/.local/lib/node_modules/
rsync -aHAX --numeric-ids /backup/.../project_creation_tools/home/Flamestrike/.local/share/applications /home/Flamestrike/.local/share/

Package-managed apps such as Blender, Krita, VS Code, Chrome, and system libraries should be reinstalled on Ubuntu from apt, Flatpak, or vendor packages, using the manifests in _logs as the reference.

ArmorPaint is preserved from the local tree and original downloaded zip.
Unreal Engine is preserved by the Aerathea protected backup.
EOF

echo "Project creation tools backup written to ${DEST_ROOT}"
echo "Manifest: ${LOG_DIR}/file_manifest.tsv"
