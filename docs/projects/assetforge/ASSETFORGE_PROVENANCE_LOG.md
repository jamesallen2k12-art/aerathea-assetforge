# AssetForge Provenance Log

Status: Active
Started: 2026-07-02

This log records external tools, install actions, model downloads, benchmark inputs, and research outputs for AssetForge. It exists to keep the commercial Aerathea production path separate from evaluation-only tooling.

## Rules

- External engines are research/reference only unless explicitly promoted through a commercial-safe review.
- Generated outputs from external engines stay in `Saved/AssetForgeResearch/`.
- No generated output from external engines becomes Aerathea visual canon or final in-game content.
- `nvdiffrast` and `nvdiffrast-rocm` are evaluation-only/non-commercial risk components.
- Hugging Face tokens, API keys, and credentials must not be stored in the repo.

## Local Quarantine Paths

| Purpose | Path | Git state |
|---|---|---|
| TRELLIS-AMD inputs | `Saved/AssetForgeResearch/TRELLIS-AMD/inputs/` | Ignored through `Saved/` |
| TRELLIS-AMD outputs | `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/` | Ignored through `Saved/` |
| TRELLIS-AMD logs | `Saved/AssetForgeResearch/TRELLIS-AMD/logs/` | Ignored through `Saved/` |
| TRELLIS-AMD weights/cache | `Saved/AssetForgeResearch/TRELLIS-AMD/weights/` | Ignored through `Saved/` |
| trellis2-amd inputs | `Saved/AssetForgeResearch/trellis2-amd/inputs/` | Ignored through `Saved/` |
| trellis2-amd outputs | `Saved/AssetForgeResearch/trellis2-amd/outputs/` | Ignored through `Saved/` |
| trellis2-amd logs | `Saved/AssetForgeResearch/trellis2-amd/logs/` | Ignored through `Saved/` |
| trellis2-amd weights/cache | `Saved/AssetForgeResearch/trellis2-amd/weights/` | Ignored through `Saved/` |
| Shared benchmark inputs | `Saved/AssetForgeResearch/benchmarks/inputs/` | Ignored through `Saved/` |
| Shared benchmark outputs | `Saved/AssetForgeResearch/benchmarks/outputs/` | Ignored through `Saved/` |
| Shared benchmark logs | `Saved/AssetForgeResearch/benchmarks/logs/` | Ignored through `Saved/` |

## External Source Repos

| Date | Tool | Source | Local path | Branch | Commit | Action | Notes |
|---|---|---|---|---|---|---|---|
| 2026-07-02 | TRELLIS-AMD | `https://github.com/CalebisGross/TRELLIS-AMD` | `Tools/External/TRELLIS-AMD/` | `main` | `23a1b81` | Cloned source | No dependencies or model weights installed at clone time. |
| 2026-07-02 | trellis2-amd | `https://github.com/ATLAS-0321/trellis2-amd` | `Tools/External/trellis2-amd/` | `rocm-port` | `4034cd8` | Cloned source recursively | Submodules checked out. No dependencies or model weights installed at clone time. |
| 2026-07-02 | FlashAttention | `https://github.com/Dao-AILab/flash-attention` | `Tools/External/flash-attention/` | `main` | `73c992c8` | Cloned source recursively | Used as a TRELLIS.2 research dependency after the AMD port's `@tridao` branch reference failed. |

## Machine Baseline

| Date | Check | Result |
|---|---|---|
| 2026-07-02 | Python | `Python 3.10.12` at `/usr/bin/python3` |
| 2026-07-02 | HIP compiler | `hipcc` at `/usr/bin/hipcc`, HIP `7.2.53211-97f5574fe2`, ROCm `7.2.4` toolchain |
| 2026-07-02 | GPU architecture | Two Radeon RX 7900 XTX GPUs, both `gfx1100` |
| 2026-07-02 | RAM | About 125 GiB total, about 122 GiB available during check |
| 2026-07-02 | Disk | About 951 GiB free on `/`, `/home/james/Projects/Aerathea`, and `/tmp` |

## Install Script Review

| Date | Tool | Script | Result |
|---|---|---|---|
| 2026-07-02 | TRELLIS-AMD | `install_amd.sh` | Creates local `.venv`, installs PyTorch ROCm, installs requirements, builds `nvdiffrast-hip`, builds `diff-gaussian-rasterization`, installs `torchsparse`, patches `gradio_client` inside venv. No `sudo` inside this script. It hardcodes PyTorch index `rocm6.4`, so install should be adapted for local ROCm 7.2.4. |
| 2026-07-02 | TRELLIS-AMD | `setup.sh` | Original upstream setup has CUDA paths, conda support, `/tmp/extensions`, and some `sudo` behavior for older HIP setup. Do not run blindly. |
| 2026-07-02 | trellis2-amd | `install.sh` | Expects an active venv and builds FlexGEMM, `nvdiffrast-rocm`, CuMesh, O-Voxel, TRELLIS.2, and FlashAttention. The referenced FlashAttention branch `@tridao` was not available from upstream during this run. |
| 2026-07-02 | trellis2-amd | `forks/TRELLIS2-rocm/setup.sh` | Upstream-style setup can clone/build extensions and references older CUDA/ROCm assumptions. Do not run blindly; manual isolated build was used instead. |

## Model Weights

The first TRELLIS-AMD smoke test downloaded reference weights into the research quarantine cache.

| Date | Tool | Model | Source | Local/cache path | License | Action |
|---|---|---|---|---|---|---|
| 2026-07-02 | TRELLIS-AMD | `microsoft/TRELLIS-image-large` | Hugging Face | `Saved/AssetForgeResearch/TRELLIS-AMD/weights/hub/` | MIT per model card; research only in this project | Downloaded by `example.py` smoke test |
| 2026-07-02 | TRELLIS-AMD | DINOv2 image-conditioning checkpoint | `torch.hub` / `facebookresearch/dinov2` | `Saved/AssetForgeResearch/TRELLIS-AMD/weights/torch/` | License audit pending; research only | Downloaded by TRELLIS image-conditioning path |
| 2026-07-02 | trellis2-amd | `microsoft/TRELLIS.2-4B` | Hugging Face | `Saved/AssetForgeResearch/trellis2-amd/weights/hub/` | MIT per model card; research only in this project | Downloaded during smoke setup and used in successful no-HDRI inference smoke. |
| 2026-07-02 | trellis2-amd | `facebook/dinov3-vitl16-pretrain-lvd1689m` | Hugging Face | `Saved/AssetForgeResearch/trellis2-amd/weights/hub/` | Gated; research only; token not stored in repo | Access accepted for account `Novakor`; `model.safetensors` downloaded with `HF_HUB_DISABLE_XET=1` after Xet transfer stalled. |
| 2026-07-02 | trellis2-amd | `briaai/RMBG-2.0` | Hugging Face | Not downloaded for successful smoke | Gated; not validated here | Earlier run hit `403` while initializing background removal. Successful smoke used an RGBA input and monkey-patched RMBG as a no-op, so this model was not required. |

## System Package Actions

| Date | Tool | Action | Result |
|---|---|---|---|
| 2026-07-02 | TRELLIS-AMD | Installed `libsparsehash-dev`, `python3.10-venv`, `cmake`, and `ninja-build` through `apt` after GUI sudo approval | Completed; required for venv creation and native extension builds |

## Runtime Actions

TRELLIS-AMD has completed one successful built-in smoke test and one failed repeatability/timing attempt.

| Date | Tool | Action | Command/log | Result |
|---|---|---|---|---|
| 2026-07-02 | TRELLIS-AMD | Install isolated env | `Tools/External/TRELLIS-AMD/.venv/` | Complete. Installed PyTorch `2.12.1+rocm7.2`, torchvision `0.27.1+rocm7.2`, triton-rocm `3.7.1`, and repo requirements. `pip check` reported no broken requirements. |
| 2026-07-02 | TRELLIS-AMD | Build native extensions | `Saved/AssetForgeResearch/TRELLIS-AMD/logs/diff_gaussian_build.log`, `Saved/AssetForgeResearch/TRELLIS-AMD/logs/torchsparse_build.log` | Complete. `nvdiffrast` HIP import, `diff_gaussian_rasterization` import, and `torchsparse` import were verified. Restricted/risk dependencies remain research only. |
| 2026-07-02 | TRELLIS-AMD | Built-in smoke test | `Saved/AssetForgeResearch/TRELLIS-AMD/logs/example_smoke.log` | Complete. Generated `sample_gs.mp4`, `sample_mesh.mp4`, `sample.glb`, and `sample.ply`; copies are quarantined under `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/`. |
| 2026-07-02 | TRELLIS-AMD | Cached timed repeat attempt | `Saved/AssetForgeResearch/TRELLIS-AMD/logs/example_smoke_cached_time.log` | Failed after saving `sample_gs.mp4`. The mesh render path hit a ROCm illegal memory access inside `_nvdiffrast_c`; the process was terminated after the crash reporter held it open. No reliable timing footer was produced. |
| 2026-07-02 | trellis2-amd | Install isolated env | `Tools/External/trellis2-amd/.venv/` | Complete. Installed PyTorch `2.12.1+rocm7.2`, torchvision `0.27.1+rocm7.2`, base TRELLIS.2 deps, and utility deps. |
| 2026-07-02 | trellis2-amd | Build `flex_gemm` | `Saved/AssetForgeResearch/trellis2-amd/logs/flexgemm_build.log` | Complete. Built with `--no-deps --no-build-isolation`; GPU-visible import passed. |
| 2026-07-02 | trellis2-amd | Build `nvdiffrast-rocm` | `Saved/AssetForgeResearch/trellis2-amd/logs/nvdiffrast_rocm_build.log` | Complete. Import requires Torch/ROCm libraries on `LD_LIBRARY_PATH`; GPU-visible import passed. Restricted/non-commercial-risk dependency remains research only. |
| 2026-07-02 | trellis2-amd | Build `cumesh` | `Saved/AssetForgeResearch/trellis2-amd/logs/cumesh_build_no_cpath.log` | Complete after clearing inherited `CPATH`; earlier attempts with `CPATH` failed in ROCm/HIP placement-new diagnostics. |
| 2026-07-02 | trellis2-amd | Build `o_voxel` | `Saved/AssetForgeResearch/trellis2-amd/logs/o_voxel_build.log` | Complete. GPU-visible import passed. |
| 2026-07-02 | trellis2-amd | Build FlashAttention ROCm/Triton path | `Saved/AssetForgeResearch/trellis2-amd/logs/flash_attn_build_local.log` | Complete from official `Dao-AILab/flash-attention` main branch. Tiny FlashAttention GPU forward test passed on RX 7900 XTX. `pip check` still reports PyTorch wants `triton-rocm` package metadata while runtime uses `triton` plus AMD `triton_kernels`. |
| 2026-07-02 | trellis2-amd | Built-in smoke test | `Saved/AssetForgeResearch/trellis2-amd/logs/example_smoke.log` | Failed before inference because OpenCV could not read bundled DWAB EXR `assets/hdri/forest.exr`. |
| 2026-07-02 | trellis2-amd | DINOv3 direct HTTP download | `Saved/AssetForgeResearch/trellis2-amd/logs/dinov3_model_safetensors_http_download.log` | Complete. Downloaded DINOv3 `model.safetensors` after disabling Hugging Face Xet. Previous partial Xet download stalled and was removed. |
| 2026-07-02 | trellis2-amd | No-HDRI smoke test, pre-access | `Saved/AssetForgeResearch/trellis2-amd/logs/trellis2_smoke_no_hdri.log`, `Saved/AssetForgeResearch/trellis2-amd/logs/trellis2_smoke_no_hdri_authenticated.log`, `Saved/AssetForgeResearch/trellis2-amd/logs/trellis2_smoke_no_hdri_http.log` | Earlier attempts blocked first on gated DINOv3 access, then on gated `briaai/RMBG-2.0`. No output generated from these attempts. |
| 2026-07-02 | trellis2-amd | No-HDRI smoke test, RGBA input with no-op RMBG | `Saved/AssetForgeResearch/trellis2-amd/logs/trellis2_smoke_no_hdri_no_rembg.log` | Complete. Inference, remesh, UV unwrap, attribute sampling, and GLB export succeeded on RX 7900 XTX. Wall time `4:20.60`; peak resident memory about `25.99 GiB`; exported GLB has `186,752` vertices and `198,552` faces. |
| 2026-07-03 | trellis2-amd | Controlled cairn benchmark, single RGBA input | `Saved/AssetForgeResearch/benchmarks/logs/trellis2_cairn_a01_triposr_masked_rgba.log` | Complete but failed quality gate. Wall time `3:12.29`; peak resident memory about `25.3 GB`; output mesh extents about `1.001 x 0.428 x 0.002`, so the result is a flat-relief failure, not an approval candidate. |
| 2026-07-03 | TRELLIS-AMD | Controlled cairn benchmark, DCC multiview inputs | `Saved/AssetForgeResearch/benchmarks/logs/cairn_a01_sculpted_v4_dcc_multiview_mesh.log` | Complete and passed first volumetric gate. Wall time `0:51.90`; peak resident memory about `7.3 GB`; output mesh extents about `1.001 x 0.928 x 0.617`. Raw mesh has `417,228` vertices and `831,554` faces, so it remains research-only and requires cleanup/decimation/paint/UV/collision/LOD validation. |
| 2026-07-03 | Blender 4.5.11 | Controlled cairn cleanup/decimation benchmark | `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/cairn_a01_sculpted_v4_dcc_multiview_mesh_decimation_report.json` | Complete. Removed `785` tiny disconnected components. Exported `100k`, `50k`, `20k`, `10k`, and `4k` face variants. Visual review suggests `18k-25k` faces as practical LOD0-style budget, `40k-60k` for high/detail review, `8k-12k` for lower LOD, and `4k` only for far LOD/massing. Blender warned several decimated GLBs may export wrongly, so repair is required before Unreal testing. |
| 2026-07-03 | Blender 4.5.11 | Controlled cairn repair/export benchmark | `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/repaired/repair_report.json` | Complete. Basic repair pass on `50k`, `20k`, and `10k` variants removed no loose geometry and required no validation topology changes. Re-exported GLBs did not emit the earlier mesh-validity warnings. |

## Generated Research Outputs

These outputs are quarantined research artifacts only. They are not Aerathea visual canon, DCC source candidates, DCC game-ready candidates, or Fully game-ready assets.

| Date | Tool | Output | Path | Notes |
|---|---|---|---|---|
| 2026-07-02 | TRELLIS-AMD | Gaussian preview video | `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/sample_gs.mp4` | From first successful smoke test |
| 2026-07-02 | TRELLIS-AMD | Mesh normal preview video | `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/sample_mesh.mp4` | From first successful smoke test |
| 2026-07-02 | TRELLIS-AMD | Textured GLB | `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/sample.glb` | From first successful smoke test; about 33,390 vertices and 32,376 faces after export |
| 2026-07-02 | TRELLIS-AMD | Gaussian PLY | `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/sample.ply` | From first successful smoke test |
| 2026-07-02 | trellis2-amd | Textured GLB | `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat.glb` | From successful no-HDRI RGBA-input smoke; about `8.5M`; one mesh with `186,752` vertices and `198,552` faces. Uses `EXT_texture_webp`; research-only. |
| 2026-07-02 | trellis2-amd | Output JSON report | `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat.json` | Records input path, output path, elapsed seconds, Torch/HIP versions, GPU, decimation target, and texture size. |
| 2026-07-02 | trellis2-amd | Geometry-only preview PLY | `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat.preview_geometry.ply` | Exported from the GLB with `trimesh` because Blender 3.0 cannot import the WebP-textured GLB. Preview aid only. |
| 2026-07-02 | trellis2-amd | Geometry preview PNG | `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat_preview.png` | Blender-rendered proof image from the geometry-only PLY; nonblank and correctly framed. |
| 2026-07-02 | trellis2-amd | Geometry preview Blender file | `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat_preview.blend` | Preview scene generated for inspection only. |
| 2026-07-03 | trellis2-amd | Controlled cairn GLB | `Saved/AssetForgeResearch/benchmarks/outputs/trellis2/cairn_a01_triposr_masked_rgba/cairn_a01_triposr_masked_rgba.glb` | Research-only failed output. Not a visual approval candidate. Flat/decal-like mesh, not cairn volume. |
| 2026-07-03 | trellis2-amd | Controlled cairn JSON report | `Saved/AssetForgeResearch/benchmarks/outputs/trellis2/cairn_a01_triposr_masked_rgba/cairn_a01_triposr_masked_rgba.json` | Records input, runtime, engine configuration, image metadata, and mesh stats for the flat-relief failure. |
| 2026-07-03 | trellis2-amd | Controlled cairn internal preview assets | `Saved/AssetForgeResearch/benchmarks/outputs/trellis2/cairn_a01_triposr_masked_rgba/` | Diagnostic previews confirmed the flat-rectangle failure. Keep for internal diagnosis only; do not present for approval. |
| 2026-07-03 | TRELLIS-AMD | Controlled cairn raw mesh PLY | `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/cairn_a01_sculpted_v4_dcc_multiview_mesh.preview_geometry.ply` | Research-only raw mesh from DCC multiview inputs. Passed volumetric gate but is far above MMO prop budget and needs cleanup before any production-facing candidate exists. |
| 2026-07-03 | TRELLIS-AMD | Controlled cairn JSON report | `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/cairn_a01_sculpted_v4_dcc_multiview_mesh.json` | Records input set, runtime, engine configuration, image metadata, and raw mesh stats for the multiview benchmark. |
| 2026-07-03 | TRELLIS-AMD | Controlled cairn internal preview renders | `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/` | Three-quarter and side neutral-geometry previews confirmed a real cairn-like volume. The three-quarter preview was opened visually because it passed the internal close-enough gate. |
| 2026-07-03 | Blender 4.5.11 | Controlled cairn decimated mesh variants | `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/` | Research-only PLY/GLB variants and contact sheets for cleaned raw, `100k`, `50k`, `20k`, `10k`, and `4k` face budgets. Not production assets; repair, retopo, UVs, paint/normal maps, collision, and Unreal validation are still required. |
| 2026-07-03 | Blender 4.5.11 | Controlled cairn repaired GLBs | `Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd/cairn_a01_sculpted_v4_dcc_multiview_mesh/decimation/repaired/` | Research-only clean GLB exports for `50k`, `20k`, and `10k` face budgets. Suitable for next Unreal import benchmark only; not production content. |
