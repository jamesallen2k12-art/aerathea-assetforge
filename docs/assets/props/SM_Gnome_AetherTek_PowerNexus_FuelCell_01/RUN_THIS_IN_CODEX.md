# Run This In Codex

Do not run the generator as a production step.

Current correct gate:

1. Locate or download the approved source package for `SM_Gnome_AetherTek_PowerNexus_FuelCell_01`.
2. Confirm the approved concept/reference image and record it as visual canon when Flamestrike approves it.
3. Open or create the Blender source with the verified Blender binary:

```bash
Tools/External/Blender/blender-4.5.11-linux-x64/blender
```

Use the existing generated proof only as non-canon reference material:

- `SourceAssets/Generated/Props/Mekgineer/SM_Gnome_AetherTek_PowerNexus_FuelCell_01/Preview/SM_Gnome_AetherTek_PowerNexus_FuelCell_01_PreviewSheet.png`
- `SourceAssets/Generated/Props/Mekgineer/SM_Gnome_AetherTek_PowerNexus_FuelCell_01/ASSET_MANIFEST.json`
- `docs/assets/props/SM_Gnome_AetherTek_PowerNexus_FuelCell_01/BUILD_IMPORT_STATUS.md`

Only run `python3 Tools/DCC/generate_gnome_power_nexus_fuel_cell.py` if Flamestrike explicitly asks for a new non-canon proof pass.

Do not mark the asset as a `DCC source candidate`, `DCC game-ready candidate`, or fully game-ready until the formal pipeline gates in `docs/assets/CONCEPT_ART_TO_GAME_READY_ASSET_PIPELINE.md` are satisfied.
