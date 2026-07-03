# TRELLIS-AMD Smoke Test Report

Status: Research output only
Run date: 2026-07-02
Report path: `docs/projects/assetforge/reports/TRELLIS_AMD_SMOKE_TEST_20260702.md`

## Boundary

This test validates TRELLIS-AMD as a reference engine only. Outputs are not Aerathea visual canon, DCC source candidates, DCC game-ready candidates, or Fully game-ready assets. The run uses nvdiffrast-derived code and remains restricted to research/evaluation.

## Source And Runtime

| Item | Value |
|---|---|
| Source repo | `Tools/External/TRELLIS-AMD/` |
| Upstream | `https://github.com/CalebisGross/TRELLIS-AMD` |
| Branch / commit | `main` / `23a1b81` |
| Python env | `Tools/External/TRELLIS-AMD/.venv/` |
| PyTorch | `2.12.1+rocm7.2` |
| torchvision | `0.27.1+rocm7.2` |
| triton-rocm | `3.7.1` |
| GPU check outside sandbox | `torch.cuda.is_available() == True`, 2 GPUs, `Radeon RX 7900 XTX` |
| Sandbox note | Sandboxed Python cannot see ROCm GPUs; GPU tests require approved unsandboxed execution |

## Install Notes

- The repo `install_amd.sh` hardcodes PyTorch ROCm 6.4, so the local install was adapted for ROCm/HIP 7.2.
- Installed system packages needed for build/runtime: `libsparsehash-dev`, `python3.10-venv`, `cmake`, `ninja-build`.
- Installed repo requirements into the isolated venv.
- Built and imported `nvdiffrast` HIP path, `diff_gaussian_rasterization`, and `torchsparse`.
- `pip check` reported no broken requirements.

## Smoke Command Shape

The successful run used the built-in `example.py` with:

- `HF_HOME=Saved/AssetForgeResearch/TRELLIS-AMD/weights`
- `HUGGINGFACE_HUB_CACHE=Saved/AssetForgeResearch/TRELLIS-AMD/weights/hub`
- `TORCH_HOME=Saved/AssetForgeResearch/TRELLIS-AMD/weights/torch`
- `ATTN_BACKEND=sdpa`
- `XFORMERS_DISABLED=1`
- `SPARSE_BACKEND=torchsparse`
- `TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1`
- `OUTPUT_FORMATS=mesh,gaussian`

Input image: `Tools/External/TRELLIS-AMD/assets/example_image/T.png`

## Successful Output

First smoke log: `Saved/AssetForgeResearch/TRELLIS-AMD/logs/example_smoke.log`

Quarantined outputs:

| Output | Path | Size |
|---|---|---|
| Gaussian preview | `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/sample_gs.mp4` | about 557 KB |
| Mesh preview | `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/sample_mesh.mp4` | about 1.6 MB |
| Textured GLB | `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/sample.glb` | about 2.6 MB |
| Gaussian PLY | `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/sample.ply` | about 32 MB |

GLB export stats from the successful run:

- Initial mesh before postprocess: 327,001 vertices, 651,316 faces.
- After decimation: 16,104 vertices, 32,565 faces.
- Final exported GLB: 33,390 vertices and 32,376 faces.
- Texture bake: 1,024 texture size, 2,500 optimization steps.

## Memory Notes

The successful run logged these visible PyTorch memory checkpoints on one RX 7900 XTX:

| Stage | Free | Used |
|---|---:|---:|
| After pipeline moved to GPU | 18.38 GiB | 5.60 GiB |
| After image conditioning | 18.05 GiB | 5.93 GiB |
| After sparse structure sample | 17.86 GiB | 6.13 GiB |
| After slat sample | 19.88 GiB | 4.11 GiB |
| After decode | 12.51 GiB | 11.47 GiB |

These are PyTorch-reported checkpoints, not full system telemetry.

## Repeatability Finding

A cached timed rerun was attempted to capture exact wall-clock runtime:

Log: `Saved/AssetForgeResearch/TRELLIS-AMD/logs/example_smoke_cached_time.log`

Result: failed after saving `sample_gs.mp4`. It entered mesh rendering and then threw a ROCm illegal-memory-access error inside `_nvdiffrast_c`. Ubuntu crash reporting held the aborted process open, so it was terminated manually and no reliable `/usr/bin/time` footer was produced.

Observed stack location:

- Error type: `c10::AcceleratorError`
- Reported error: `CUDA error: an illegal memory access was encountered`
- Extension in stack: `_nvdiffrast_c.cpython-310-x86_64-linux-gnu.so`

This confirms that TRELLIS-AMD can run once on this PC, but the mesh/rasterizer path is not proven stable or repeatable on ROCm 7.2.

## Storage Impact

| Item | Size |
|---|---:|
| TRELLIS-AMD model/cache folder | about 4.0 GB |
| TRELLIS-AMD venv | about 18 GB |
| TRELLIS-AMD source tree excluding venv | about 477 MB |

## Conclusion

TRELLIS-AMD is viable as a research/reference engine on this AMD machine, but not reliable enough to treat as a push-button production path. The first smoke test produced GLB/PLY/video outputs, while the repeat run exposed instability in the restricted nvdiffrast-derived render path.

For AssetForge, this supports the existing direction: study the architecture and ROCm interactions, but replace the nvdiffrast-dependent path with a commercial-safe, controlled renderer/postprocess path before any production use.
