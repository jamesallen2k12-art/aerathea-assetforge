# SM_GIA_BloodAxeCairnstone_A002 Phase 1 Source Evidence Lock

Status: `A002 source evidence approved`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`

## Phase Goal

Verify the approved source template, verify scanline evidence, confirm source hierarchy, and confirm no A001 generated output is being used as A002 source data.

## Approved Source Template

- Path: `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`
- File type: PNG image data, `1055 x 1491`, 8-bit RGB, non-interlaced
- File SHA256: `4b953abb87f5f254a5f51c6214e76d3f72c4fc55bc2fa4e4d605b2440d6e53c2`

## Scanline Evidence

- Manifest: `docs/assets/reference/bloodaxe_cairnstone_asset/ScanlineCapture/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate_ScanlineManifest.json`
- Scan record: `docs/assets/reference/bloodaxe_cairnstone_asset/ScanlineCapture/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.rgbscan.gz`
- Rebuilt image: `docs/assets/reference/bloodaxe_cairnstone_asset/ScanlineCapture/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate_RebuiltFromScanlines.png`
- Difference image: `docs/assets/reference/bloodaxe_cairnstone_asset/ScanlineCapture/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate_Difference.png`

Manifest results:

- Width: `1055`
- Height: `1491`
- Scanlines: `1491`
- Pixel SHA256: `65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72`
- Target pixel SHA256: `65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72`
- Rebuild pixel SHA256: `65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72`
- `max_rgb_delta`: `0`
- `changed_pixels`: `0`
- `mean_grayscale_delta`: `0.0`
- `pixel_exact`: `true`

## Source Hierarchy Confirmed

Primary A002 source authority:

1. Approved visual source template.
2. Source scanline evidence.
3. Project reconstruction authority: `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
4. Asset-specific modular authority: `docs/projects/assetforge/BLOODAXE_CAIRNSTONE_A001_MODULAR_COMPONENT_ASSEMBLY_PLAN.md`
5. Asset-specific geometry authority: `docs/projects/assetforge/BLOODAXE_CAIRNSTONE_A001_GEOMETRY_CONSTRUCTION_PLAN.md`
6. Successful process recovery authority: `docs/projects/assetforge/BLOODAXE_CAIRNSTONE_TODAYS_SUCCESS_PROCESS_VS_BLUEPRINT.md`

## A001 Generated Output Boundary

A001 generated meshes, renders, materials, textures, exports, Unreal imports, packages, and late-pass manifests are not A002 source authority.

A001 written plans may constrain A002 only as written constraints. A001 pre-geometry manifests may be reviewed as candidate evidence during Phase 2, but they must be revalidated from the approved source template before driving A002 production.

## Phase 1 Decision

Decision: `approved`

A002 Phase 1 Source Evidence Lock passes.

No A001 generated output was used as source data.

## Next Core-Valid Step

Begin A002 Phase 2: Measurement Formula Lock.

The next task is to declare or verify the pixel convention, crop formulas, component split formulas, component centers, contact formulas, snap-anchor formulas, visible/inferred/diagnostic masks, and blocked methods before any geometry work.
