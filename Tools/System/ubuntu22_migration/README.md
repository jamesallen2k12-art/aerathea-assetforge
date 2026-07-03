# Ubuntu 22.04 Migration Runbook

This bundle is for moving the workstation from Fedora 44 KDE to Ubuntu 22.04 LTS without losing Aerathea, Codex, Unreal, or user data.

## Current Disk Map

- `nvme0n1` 8TB WD_BLACK SN850X: current Fedora system.
  - `nvme0n1p1` EFI, mounted `/boot/efi`
  - `nvme0n1p2` boot, mounted `/boot`
  - `nvme0n1p3` Btrfs, mounted `/` and `/home`
- `nvme1n1` 4TB WD_BLACK SN850X: emergency Fedora plus `/faststore`.
  - `nvme1n1p1` emergency EFI
  - `nvme1n1p2` emergency boot
  - `nvme1n1p3` emergency Fedora
  - `nvme1n1p4` Btrfs `FastStore`, mounted `/faststore`
- `sda1` 12TB WD Red: Btrfs `BackupVault`, mounted `/backup`

Do not rely on `nvme0n1` / `nvme1n1` names during the installer. Confirm by model, serial, and size.

## Protected Aerathea Set

Nothing destructive may happen until these have at least two verified copies:

- `/home/Flamestrike/Projects/Aerathea`
- `/home/Flamestrike/Desktop/Aerathea`
- `/home/Flamestrike/Desktop/Aerathea Abyssal Search Results`
- `/home/Flamestrike/Desktop/Aerathea Pending Approval Images`
- `/home/Flamestrike/Desktop/Aerathea Pending.md`
- `/home/Flamestrike/Desktop/Aetherium ARPG Derivative Creative Questions.md`
- `/home/Flamestrike/Desktop/Aetherium MMORPG Timeline.md`
- `/home/Flamestrike/Desktop/Aetherium MMORPG.md`
- `/home/Flamestrike/UnrealEngine`
- `/home/Flamestrike/.config/Epic`
- `/home/Flamestrike/.epic`
- `/home/Flamestrike/.codex`
- `/home/Flamestrike/.hermes`
- `/faststore/AI/hermes`

The active Aerathea repo is only around 19GB, but the Unreal install is around 145GB and `/faststore` is around 2.3TB.

## Protected Project-Creation Programs

Programs and tooling used to create Aerathea are protected migration assets too. Preserve local installs, configs, launchers, and installers before any OS install:

- Unreal Engine installs: `/home/Flamestrike/UnrealEngine`
- Unreal/Epic config: `/home/Flamestrike/.config/Epic`, `/home/Flamestrike/.config/Unreal Engine`, `/home/Flamestrike/.epic`, `/home/Flamestrike/.cache/Epic`
- Epic Asset Manager app data: `/home/Flamestrike/.var/app/io.github.achetagames.epic_asset_manager`
- ArmorPaint purchased/local install: `/home/Flamestrike/Tools/ArmorPaint`, `/home/Flamestrike/.local/bin/armorpaint`, `/home/Flamestrike/.local/share/applications/armorpaint.desktop`, `/home/Flamestrike/Downloads/ArmorPaint_10alpha_linux64.zip`
- Blender and Krita package/config records. These are package-managed on Fedora and must be reinstalled on Ubuntu, but settings and manifests are backed up.
- Android Studio local install: `/home/Flamestrike/android-studio`
- Project helper scripts and launchers: `/home/Flamestrike/bin`, `/home/Flamestrike/.local/bin`, `/home/Flamestrike/.local/share/applications`, relevant Desktop launchers
- Large installer/source archives: `/home/Flamestrike/Downloads/Linux_Unreal_Engine_5.8.0.zip`, `/home/Flamestrike/Downloads/Linux_Unreal_Engine_5.8.0_preview-1.zip`, Epic installer files, and Unreal map-port package files

## Phase Gates

1. Run `00_inventory.sh`.
2. Run `01_backup_aerathea_protected_set.sh` to `/backup`.
3. Run `05_backup_project_creation_tools.sh` to `/backup`.
4. Run `02_backup_user_continuity.sh` to `/backup`.
5. Run `03_stage_faststore_to_main_ssd.sh` to copy `/faststore` onto the 8TB SSD.
6. Verify manifests and spot-check files from `/backup` and the staged `/faststore` copy.
7. Only then install Ubuntu 22.04.5 LTS onto the 4TB SSD.
8. Boot Ubuntu, restore Codex/user continuity, reinstall package-managed creative apps, and verify Aerathea opens.
9. Only after Ubuntu on the 4TB SSD is proven good, consider installing Ubuntu on the 8TB SSD and keeping the 4TB SSD as backup OS.

## Post-Rollback Retry Note

The first attempt returned to Fedora with no Ubuntu EFI entry and the 4TB disk still showing the emergency Fedora plus `FastStore` layout. Do not treat the GRUB loopback ISO boot entry as the primary retry path. Use a real UEFI Ubuntu installer USB made from the verified ISO, then choose manual partitioning.

For the retry, target only the 4TB WD_BLACK SN850X, serial `25390T801898`. Prefer replacing the emergency Fedora partitions (`EMERG_EFI`, `EMERG_BOOT`, and `EmergencyFedora`) while leaving `FastStore` unformatted unless intentionally retiring it after re-checking the staged copy on the 8TB SSD.

## Hard Stops

- Do not erase, repartition, or format either NVMe until `/backup` contains verified copies.
- Do not clear `nvme1n1p4` `/faststore` until `/faststore` has been copied to the 8TB SSD and verified.
- Do not overwrite `nvme0n1` until Ubuntu on the 4TB SSD can boot and Aerathea/Codex are restored.
- Do not assume `/home` has been preserved by an OS install. Back it up explicitly.
- Do not assume a paid/local app can be redownloaded quickly. Preserve the current local app tree and installer archive first.

## Ubuntu Installer Target

First install target:

- 4TB WD_BLACK SN850X `nvme1n1`, serial `25390T801898`

Avoid touching:

- 8TB WD_BLACK SN850X `nvme0n1`, serial `253461800359`, until the new Ubuntu install is proven.
- 12TB WDC WD122KFBX `sda`, serial `WD-B004R91D`, because it is the migration backup vault.

Use Ubuntu 22.04.5 LTS Desktop AMD64:

- https://releases.ubuntu.com/22.04/

Epic currently lists Ubuntu 22.04 as the recommended Linux development OS for Unreal Engine:

- https://dev.epicgames.com/documentation/en-us/unreal-engine/linux-development-requirements-for-unreal-engine
