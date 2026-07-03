# AssetForge Controlled Benchmarks - 2026-07-03

Status: Active benchmark log
Scope: Research-only external-engine evaluation

## Guardrails

- External engine outputs stay quarantined under `Saved/AssetForgeResearch/`.
- These outputs are not Aerathea visual canon.
- These outputs are not DCC source candidates, DCC game-ready candidates, or Fully game-ready assets.
- Failed outputs are recorded here and should not be shown for visual approval.
- Visual approval should only be requested when a generated result plausibly matches the intended asset form.

## Benchmark: `cairn_a01_triposr_masked_rgba`

Result: `FAIL_FLAT_RELIEF`

The run completed technically, but the geometry failed the asset goal. The output reads as a nearly flat relief/plane instead of a usable cairn static-prop volume.

### Input

Source image:

- `SourceAssets/External/TripoSR/BloodAxeCairn_A1/BloodAxeCairn_A1_TripoSR_Input.png`

Prepared benchmark input:

- `Saved/AssetForgeResearch/benchmarks/inputs/cairn_a01/cairn_a01_triposr_input_masked_rgba.png`

Preparation:

- Script: `Saved/AssetForgeResearch/benchmarks/prepare_cairn_inputs.py`
- Method: corner-color flood-fill background removal, largest foreground component, expanded/feathered alpha.
- Output image: `RGBA`, `512 x 512`, alpha range `0-255`.
- Background removal model was bypassed because the prepared image already had alpha.

### Engine

- Tool: `trellis2-amd`
- Local source: `Tools/External/trellis2-amd/forks/TRELLIS2-rocm`
- Runner: `Saved/AssetForgeResearch/benchmarks/trellis2_benchmark_runner.py`
- GPU: `Radeon RX 7900 XTX`
- Torch: `2.12.1+rocm7.2`
- HIP: `7.2.53211`
- Decimation target: `200000`
- Texture size: `1024`

Command recorded by `/usr/bin/time`:

```bash
/home/james/Projects/Aerathea/Tools/External/trellis2-amd/.venv/bin/python \
  /home/james/Projects/Aerathea/Saved/AssetForgeResearch/benchmarks/trellis2_benchmark_runner.py \
  --benchmark-id cairn_a01_triposr_masked_rgba \
  --input /home/james/Projects/Aerathea/Saved/AssetForgeResearch/benchmarks/inputs/cairn_a01/cairn_a01_triposr_input_masked_rgba.png \
  --output-root /home/james/Projects/Aerathea/Saved/AssetForgeResearch/benchmarks/outputs/trellis2 \
  --decimation-target 200000 \
  --texture-size 1024 \
  --bypass-rembg
```

### Runtime

- Script-reported elapsed time: `186.396` seconds.
- Wall-clock time: `3:12.29`.
- Peak resident memory: `25300968 KB`, about `25.3 GB`.
- Exit status: `0`.

### Output Artifacts

- GLB: `Saved/AssetForgeResearch/benchmarks/outputs/trellis2/cairn_a01_triposr_masked_rgba/cairn_a01_triposr_masked_rgba.glb`
- JSON report: `Saved/AssetForgeResearch/benchmarks/outputs/trellis2/cairn_a01_triposr_masked_rgba/cairn_a01_triposr_masked_rgba.json`
- Geometry preview PLY: `Saved/AssetForgeResearch/benchmarks/outputs/trellis2/cairn_a01_triposr_masked_rgba/cairn_a01_triposr_masked_rgba.preview_geometry.ply`
- Log: `Saved/AssetForgeResearch/benchmarks/logs/trellis2_cairn_a01_triposr_masked_rgba.log`
- Failed preview renders exist for internal diagnosis only. Do not use them as approval candidates.

### Mesh Stats

- Geometries: `1`
- Vertices: `96,119`
- Faces: `188,380`
- Bounds min: `[-0.500731, -0.213808, -0.001007]`
- Bounds max: `[0.500728, 0.213885, 0.001004]`
- Extents: `[1.001459, 0.427693, 0.002010]`

The `Z` thickness is only about `0.002` against a width of about `1.001`, or roughly `0.2%` of the main width. That confirms the result is a flat/decal-like reconstruction, not a volumetric cairn.

### Interpretation

This is not a viable static-prop geometry candidate. The likely causes are:

- Single-view input does not provide enough 360-degree geometric evidence for this cairn form.
- The input is a concept/render image rather than a true multiview capture with camera metadata.
- The model favored image-plane relief over inferred stone volume.

Next tests should prioritize:

- Multi-view cairn inputs with front, side, back, and top views.
- Engines or harnesses that explicitly support multi-image conditioning.
- Automatic gating before visual approval so flat or rectangular failures are logged but not presented.

## Benchmark: `cairn_a01_sculpted_v4_dcc_multiview_mesh`

Result: `PASS_VOLUME_GATE_RAW_MESH`

The run completed successfully and produced a real volumetric cairn-like mesh rather than a flat image-plane relief. This is still raw research output only. It is not a DCC source candidate, DCC game-ready candidate, Fully game-ready asset, or Aerathea visual canon.

### Input

Source DCC file:

- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_SculptedMidpolyV4/SM_GIA_BloodAxeCairnSlabCluster_A01_SculptedMidpolyV4.blend`

Prepared benchmark inputs:

- `Saved/AssetForgeResearch/benchmarks/inputs/cairn_a01_sculpted_v4_dcc_multiview/cairn_a01_sculpted_v4_dcc_multiview_front.png`
- `Saved/AssetForgeResearch/benchmarks/inputs/cairn_a01_sculpted_v4_dcc_multiview/cairn_a01_sculpted_v4_dcc_multiview_right.png`
- `Saved/AssetForgeResearch/benchmarks/inputs/cairn_a01_sculpted_v4_dcc_multiview/cairn_a01_sculpted_v4_dcc_multiview_back.png`
- `Saved/AssetForgeResearch/benchmarks/inputs/cairn_a01_sculpted_v4_dcc_multiview/cairn_a01_sculpted_v4_dcc_multiview_left.png`
- `Saved/AssetForgeResearch/benchmarks/inputs/cairn_a01_sculpted_v4_dcc_multiview/cairn_a01_sculpted_v4_dcc_multiview_top.png`

Preparation:

- Script: `Saved/AssetForgeResearch/benchmarks/render_dcc_multiview_inputs.py`
- Method: Blender 4.5.11 orthographic front/right/back/left/top renders from the DCC source.
- Output images: `RGBA`, `768 x 768`, alpha range `0-255`.
- Contact sheet: `Saved/AssetForgeResearch/benchmarks/inputs/cairn_a01_sculpted_v4_dcc_multiview/cairn_a01_sculpted_v4_dcc_multiview_input_contact_sheet.png`

### Engine

- Tool: `TRELLIS-AMD`
- Local source: `Tools/External/TRELLIS-AMD`
- Runner: `Saved/AssetForgeResearch/benchmarks/trellis_amd_multiview_benchmark_runner.py`
- Job launcher: `Saved/AssetForgeResearch/benchmarks/run_trellis_amd_cairn_multiview_mesh_job.sh`
- GPU: `Radeon RX 7900 XTX`
- Torch: `2.12.1+rocm7.2`
- HIP: `7.2.53211`
- Mode: `multidiffusion`
- Formats: `mesh`
- Sparse backend: `torchsparse`
- Attention backend: `sdpa`
- Sparse structure steps: `12`, CFG `7.5`
- SLAT steps: `12`, CFG `3.0`

Command path:

```bash
systemd-run --user --unit=assetforge-trellis-amd-cairn-mv --collect \
  --working-directory=/home/james/Projects/Aerathea \
  /home/james/Projects/Aerathea/Saved/AssetForgeResearch/benchmarks/run_trellis_amd_cairn_multiview_mesh_job.sh
```

### Runtime

- Script-reported elapsed time: `45.009` seconds.
- Wall-clock time: `0:51.90`.
- Peak resident memory: `7306484 KB`, about `7.3 GB`.
- Exit status: `0`.

### Output Artifacts

- JSON report: `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/cairn_a01_sculpted_v4_dcc_multiview_mesh.json`
- Raw mesh preview PLY: `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/cairn_a01_sculpted_v4_dcc_multiview_mesh.preview_geometry.ply`
- Three-quarter internal preview PNG: `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/cairn_a01_sculpted_v4_dcc_multiview_mesh_internal_threequarter.png`
- Side internal preview PNG: `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/cairn_a01_sculpted_v4_dcc_multiview_mesh_internal_side.png`
- Log: `Saved/AssetForgeResearch/benchmarks/logs/cairn_a01_sculpted_v4_dcc_multiview_mesh.log`

### Mesh Stats

- Raw vertices: `417,228`
- Raw faces: `831,554`
- Bounds min: `[-0.501731, -0.469333, -0.314447]`
- Bounds max: `[0.498960, 0.458975, 0.302588]`
- Extents: `[1.000690, 0.928308, 0.617034]`

The smallest dimension is about `61.7%` of the largest dimension, so this result passes the first volumetric geometry gate. It is not a flat/decal reconstruction.

### Interpretation

This confirms that multi-view conditioning is meaningfully better than the single-image test for cairn/static-prop volume recovery. The preview reads as a cairn-like rocky cluster and was close enough to open visually for user review.

Production concerns remain:

- Raw mesh density is far above a small/medium static-prop budget.
- The output contains noisy edge fragments and ragged floating shards.
- The preview is neutral geometry only, not a textured or painted asset.
- UVs, material slots, collision, scale, LODs, and Unreal import validation still need a separate conversion/cleanup pass.
- The external-engine result remains quarantined research output and cannot be promoted into Aerathea production as-is.

Next tests should prioritize:

- Raw mesh cleanup and decimation benchmark.
- GLB/export path validation for this multi-view result.
- UV unwrap and texture-paint pipeline test.
- Comparison against the DCC source and approved visual-canon target before any production-facing candidate is created.

### Cleanup / Decimation Follow-Up

Result: `PASS_DECIMATION_RANGE_TEST_WITH_WARNINGS`

A local Blender cleanup benchmark removed tiny disconnected components and exported several decimated research variants.

Script:

- `Saved/AssetForgeResearch/benchmarks/decimate_raw_mesh_benchmark.py`

Report:

- `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/cairn_a01_sculpted_v4_dcc_multiview_mesh_decimation_report.json`

Contact sheets:

- Three-quarter: `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/cairn_a01_sculpted_v4_dcc_multiview_mesh_decimation_contact_sheet.png`
- Side: `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/cairn_a01_sculpted_v4_dcc_multiview_mesh_decimation_side_contact_sheet.png`

Component cleanup:

- Raw mesh: `417,228` vertices, `831,554` faces.
- Connected components found: `942`.
- Components kept with `>=64` faces: `157`.
- Components removed: `785`.
- Cleaned mesh: `407,488` vertices, `815,252` faces.

Decimation outputs:

| Target faces | Actual vertices | Actual faces | Visual read |
|---:|---:|---:|---|
| `100,000` | `49,862` | `100,000` | Very close to cleaned raw silhouette; still heavy for a normal MMO prop. |
| `50,000` | `24,862` | `50,000` | Strong silhouette retention; viable high/detail research target for this complex cairn cluster. |
| `20,000` | `9,862` | `20,000` | Still reads as the same cairn; visible faceting begins. Likely lowest practical LOD0-style budget before paint/normal recovery. |
| `10,000` | `4,862` | `10,000` | Reads as a chunky/stylized low-poly cairn; usable as LOD1/LOD2 direction, not ideal as the primary asset if close-up detail matters. |
| `4,000` | `1,862` | `4,000` | Keeps broad massing but loses too much rock-surface language for this asset without heavy texture/normal recovery. |

Working budget conclusion for this generated cairn:

- Hero/close review candidate: `40k-60k` faces before final retopo/normal-map bake.
- Practical MMO LOD0 target after cleanup and texture support: `18k-25k` faces.
- Lower LOD direction: `8k-12k` faces.
- `4k` is too low for this particular cluster as a primary view asset, though it may work for far LOD.

Warnings:

- Blender GLB export warned that several decimated meshes were not fully valid and may export wrongly.
- This means a mesh-repair pass is required before any Unreal import benchmark.
- These outputs are still neutral-material research artifacts, not production candidates.

### Mesh Repair Follow-Up

Result: `PASS_REPAIRED_GLB_EXPORT_FOR_USEFUL_BUDGETS`

A basic Blender repair/export pass was run on the most useful budgets: `50k`, `20k`, and `10k` faces.

Script:

- `Saved/AssetForgeResearch/benchmarks/repair_decimated_mesh_benchmark.py`

Report:

- `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/repaired/repair_report.json`

Repaired outputs:

- `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/repaired/cairn_a01_sculpted_v4_dcc_multiview_mesh_decimated_50000_repaired.glb`
- `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/repaired/cairn_a01_sculpted_v4_dcc_multiview_mesh_decimated_20000_repaired.glb`
- `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/repaired/cairn_a01_sculpted_v4_dcc_multiview_mesh_decimated_10000_repaired.glb`

Repair result:

- Blender removed no loose vertices/edges/faces.
- Merge-by-distance removed no vertices at `0.00001`.
- `mesh.validate(clean_customdata=True)` reported no required topology changes.
- Re-exported `50k`, `20k`, and `10k` GLBs did not emit the earlier mesh-validity warnings.

Interpretation:

- The useful-budget meshes are suitable for the next research benchmark: Unreal import validation.
- They are still not production assets. Texture paint, UV validation, collision, LOD setup, scale, material slots, and final visual approval remain open.

### Unreal Import Validation Follow-Up

Result: `PASS_UNREAL_IMPORT_VALIDATION_WITH_POSTPROCESS_GAPS`

The repaired `20k` and `50k` GLBs were imported through headless Unreal Editor as research-only assets, measured, and then deleted from the temporary Unreal content folder.

Script:

- `Tools/Unreal/validate_assetforge_repaired_glb_imports.py`

Reports:

- `Saved/AssetForgeResearch/benchmarks/outputs/unreal/import_validation/assetforge_cairn_repaired_unreal_import_validation_20260703-080443.json`
- `Saved/AssetForgeResearch/benchmarks/outputs/unreal/import_validation/assetforge_cairn_repaired_unreal_import_validation_20260703-080443.md`

Temporary Unreal destination:

- `/Game/Aerathea/Developer/AssetForgeResearch/ImportValidation/Run_20260703-080443`

Cleanup:

- Complete. No research `uasset` files remained under `Content/Aerathea/Developer/AssetForgeResearch/` after the benchmark.

Import results:

| Input | Result | Static meshes | LODs | Materials | Collision | Bounds cm | Import seconds |
|---|---|---:|---:|---:|---|---|---:|
| `20k repaired GLB` | `PASS_IMPORT_VALIDATION` | `1` | `1` | `1` WorldGrid slot | `simple=0`, `convex=1` | `97.63 x 92.02 x 61.49` | `1.590` |
| `50k repaired GLB` | `PASS_IMPORT_VALIDATION` | `1` | `1` | `1` WorldGrid slot | `simple=0`, `convex=1` | `97.93 x 92.50 x 61.65` | `4.115` |

Unreal import warnings observed:

- glTF mesh primitives had no materials assigned.
- Imported static meshes reported degenerate tangent bases and nearly zero binormals.
- Asset path length warnings appeared because the source benchmark names are long.

Interpretation:

- The repaired GLBs are importable in Unreal and survive the static-mesh build path.
- The imports are normalized to roughly `1 m` wide, so scale normalization is still required before any Aerathea candidate package.
- Raw GLB import gives only one LOD and one fallback material slot; AssetForge must generate or assign LODs, authored material slots, UV/material metadata, and collision policy before a candidate can advance.
- The result remains research-only and does not create visual canon, a DCC source candidate, a DCC game-ready candidate, or Fully game-ready content.

## Queued Alternate Benchmark: `ProjectedEarth_PolarCluster`

This package is queued as a different benchmark class: planet/map texture and Unreal import validation, not single-prop image-to-3D generation.

Path:

- `docs/assets/reference/planet_maps/ProjectedEarth_PolarCluster/`

Useful files:

- `ProjectedEarth_PolarCluster_Texture_4096.png` - RGB `4096 x 2048`
- `ProjectedEarth_PolarCluster_LandMask.png` - RGB `4096 x 2048`
- `ProjectedEarth_PolarCluster_Model.obj`
- `ProjectedEarth_PolarCluster_Model.glb`
- `planet_specs.json`
- `README.md`

Appropriate tests:

- Verify texture/map dimensions and color space.
- Validate OBJ/GLB import through Blender.
- Check material assignment and UV behavior.
- Generate Unreal import notes for planet-scale reference use.
- Confirm scale constants from `planet_specs.json`.

This should not be used to judge cairn/static-prop reconstruction quality because its parameters are map/model validation, not irregular prop-volume recovery.
