# Ubuntu 22.04 Migration Status

Last updated: 2026-07-01

## Post-Rollback Status

Fedora 44 was restored after the first Ubuntu install attempt did not complete.
Read-only checks after the rollback showed:

- Current OS is Fedora Linux 44 KDE.
- The 4TB WD_BLACK SN850X, serial `25390T801898`, still has the emergency Fedora layout:
  - `nvme1n1p1` `EMERG_EFI`
  - `nvme1n1p2` `EMERG_BOOT`
  - `nvme1n1p3` `EmergencyFedora`
  - `nvme1n1p4` `FastStore`
- No Ubuntu EFI boot entry is present. EFI boot order remains main Fedora first, then emergency Fedora entries.
- The Ubuntu ISO at `/home/Flamestrike/Downloads/ubuntu-22.04.5-desktop-amd64.iso` still matches the backup ISO SHA256:
  `bfd1cee02bc4f35db939e69b934ba49a39a378797ce9aee20f6e3e3e728fefbf`.
- The ISO contains the expected `casper/vmlinuz` and `casper/initrd` paths.
- `/home/Flamestrike/FastStore_Staging` is still about 2.3T.
- `/backup/Ubuntu22_Migration_20260701-153501` is still present and about 362G.

Conclusion: Ubuntu did not land on the 4TB drive. The failed step was most likely before or during installer boot/install, not the backup or copy-protection stages.

## Retry Guidance

Do not retry the GRUB loopback ISO boot path as the primary migration route.
Use a real UEFI Ubuntu installer instead, preferably a USB installer created from the verified ISO.

## USB Installer Prepared

Created and verified on 2026-07-01:

- Device: Kingston DataTraveler 3.0, serial `2CFDA1BBB44D1680D9080542`
- Linux device during creation: `/dev/sdb`
- Source ISO: `/home/Flamestrike/Downloads/ubuntu-22.04.5-desktop-amd64.iso`
- Resulting USB label: `Ubuntu 22.04.5 LTS amd64`
- Byte-for-byte verification: `cmp -n 4762707968 ... /dev/sdb` completed with exit code 0.

The written ISO image is smaller than the 28.9G USB stick, so tools may warn that the backup GPT table is not at the end of the device. This is expected for a raw ISO-to-USB write and should not be repaired before booting the installer.

During the Ubuntu installer, use manual partitioning and confirm the target by model, size, and serial:

- Target only: 4TB WD_BLACK SN850X, serial `25390T801898`.
- Keep untouched: 8TB WD_BLACK SN850X, serial `253461800359`.
- Keep untouched: 12TB WDC WD122KFBX backup vault, serial `WD-B004R91D`.
- Prefer replacing only the emergency Fedora partitions on the 4TB disk:
  - use/format `EMERG_EFI` as EFI System Partition if needed,
  - use/format `EMERG_BOOT` as `/boot` if using a separate boot partition,
  - use/format `EmergencyFedora` as Ubuntu `/`,
  - do not format `FastStore` unless deliberately retiring it after re-checking the staged copy.

After the first successful Ubuntu boot, run `04_restore_codex_after_ubuntu.sh` and then verify Codex, Aerathea, Unreal, and the staged `/faststore` copy before changing the 8TB Fedora install.

## Completed Protection Gates

- Inventory captured under `/backup/Ubuntu22_Migration_20260701-153501/inventory`.
- Aerathea protected set backed up under `/backup/Ubuntu22_Migration_20260701-153501/aerathea_protected_set`.
- User continuity backed up under `/backup/Ubuntu22_Migration_20260701-153501/user_continuity`.
- Project-creation tools backed up under `/backup/Ubuntu22_Migration_20260701-153501/project_creation_tools`.
- `/faststore` staged to `/home/Flamestrike/FastStore_Staging`.
- Ubuntu 22.04.5 Desktop AMD64 ISO downloaded, SHA256 verified, and copied to `/backup/Ubuntu22_Migration_20260701-153501/ubuntu_install_media`.
- GRUB custom ISO boot entries installed at `/boot/grub2/custom.cfg` from `ubuntu22_grub_custom.cfg`.
- GRUB one-time next boot set to `ubuntu-22.04.5-iso`; Fedora saved default remains unchanged.

## Verified Copy State

- Aerathea protected backup size: about 278G.
- Project-creation tools backup size: about 78G.
- Project-creation tools manifest: 4,212 file entries.
- User continuity backup size: about 1.5G.
- `/faststore` staged size: about 2.3T.
- Root dry-run rsync comparison for `/faststore` reported:
  - created files: 0
  - deleted files: 0
  - regular files transferred: 0
  - compared total size: 2.43T

The first `/faststore` rsync pass hit permission denied on two `ollama`-owned files under `/faststore/AI/ollama-system/.ollama`. A root-authorized follow-up rsync copied exactly those 2 missing files and the final root dry-run comparison was clean.

## Project-Creation Programs Protected

- Unreal Engine installs and Epic/Unreal config.
- Epic Asset Manager Flatpak app data.
- ArmorPaint local install, launcher, desktop entry, and original purchased zip.
- Blender/Krita/GIMP package/config manifests where present.
- Android Studio local install.
- Local helper launchers under `/home/Flamestrike/bin` and `/home/Flamestrike/.local/bin`.
- Codex/OpenAI local executable path and package tree under `/home/Flamestrike/.local/lib/node_modules/@openai`.
- Large Unreal/Epic installer/source archives in Downloads.

## Hard Stop Before Installing Ubuntu

Do not erase, repartition, or format any disk from Fedora. The next destructive action must happen only inside the Ubuntu installer, at the keyboard, after confirming the target disk by model, size, and serial.

First Ubuntu install target:

- 4TB WD_BLACK SN850X, serial `25390T801898`

Avoid touching until the first Ubuntu install is proven:

- 8TB WD_BLACK SN850X, serial `253461800359`
- 12TB WDC WD122KFBX backup vault, serial `WD-B004R91D`
