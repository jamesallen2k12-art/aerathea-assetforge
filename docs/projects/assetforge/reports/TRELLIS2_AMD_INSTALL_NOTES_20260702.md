# TRELLIS.2 AMD Install Notes

Date: 2026-07-02
Status: Native stack installed; authenticated no-HDRI inference smoke completed on RX 7900 XTX.

## Scope

This report records the local `trellis2-amd` reference-engine setup for AssetForge research. It is not an Aerathea production dependency and must not be used to generate final in-game assets.

## Source

- Umbrella repo: `Tools/External/trellis2-amd/`
- Upstream: `https://github.com/ATLAS-0321/trellis2-amd`
- Branch: `rocm-port`
- Commit: `4034cd8`
- FlashAttention repo: `Tools/External/flash-attention/`
- FlashAttention upstream: `https://github.com/Dao-AILab/flash-attention`
- FlashAttention commit: `73c992c8ca746935548df620ef3c1b6238fe6e68`

## Machine

- GPU: Radeon RX 7900 XTX, `gfx1100`
- ROCm/HIP: `7.2.53211`
- PyTorch: `2.12.1+rocm7.2`
- Python: `3.10`
- Free project disk before model downloads: about 897 GiB
- No-HDRI smoke peak RAM: about 25.99 GiB resident

## Installed Runtime Pieces

The `trellis2-amd` environment was built under:

- `Tools/External/trellis2-amd/.venv/`

Installed and verified:

- PyTorch ROCm `2.12.1+rocm7.2`
- torchvision `0.27.1+rocm7.2`
- base TRELLIS.2 Python dependencies
- `flex_gemm`
- `nvdiffrast-rocm`
- `cumesh`
- `o_voxel`
- official FlashAttention `2.8.4` using the ROCm/Triton AMD path
- `amd-aiter`
- `triton_kernels` tagged for AMD ROCm 7.2

GPU-visible import check passed for:

- `torch`
- `flex_gemm`
- `nvdiffrast`
- `cumesh`
- `o_voxel`
- `flash_attn`

FlashAttention forward pass passed on the RX 7900 XTX:

- input tensor: `(1, 64, 4, 64)`, `float16`, CUDA/HIP device
- output: finite tensor with expected shape

## Build Notes

- `Tools/External/trellis2-amd/install.sh` references `git+https://github.com/Dao-AILab/flash-attention.git@tridao`, but that branch/tag was not available from the upstream remote during this run.
- The working FlashAttention path was the official main branch with:

```text
BUILD_TARGET=rocm
FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE
pip install --no-build-isolation -v .
```

- `cumesh` failed when the inherited `CPATH` override was active. Clearing `CPATH` allowed ROCm's HIP/C++ wrapper path to compile it successfully.
- `pip check` is not clean after FlashAttention because PyTorch declares `triton-rocm`, while FlashAttention installs package name `triton`. Runtime checks passed, and the installed stack includes AMD ROCm `triton_kernels`, but the metadata warning remains recorded.

## Smoke Tests

### Built-In Example

Command log:

- `Saved/AssetForgeResearch/trellis2-amd/logs/example_smoke.log`

Result:

- Failed before inference because OpenCV could not decode the bundled DWAB-compressed `assets/hdri/forest.exr`.
- No TRELLIS.2 output asset was produced.

### No-HDRI Inference Smoke

Script:

- `Saved/AssetForgeResearch/trellis2-amd/trellis2_smoke_no_hdri.py`

Command log:

- Failed pre-auth/access attempt: `Saved/AssetForgeResearch/trellis2-amd/logs/trellis2_smoke_no_hdri.log`
- Successful authenticated run: `Saved/AssetForgeResearch/trellis2-amd/logs/trellis2_smoke_no_hdri_no_rembg.log`

Result:

- Initial model download cached TRELLIS.2 weights under `Saved/AssetForgeResearch/trellis2-amd/weights/`.
- Full run initially blocked while initializing the image conditioner because `facebook/dinov3-vitl16-pretrain-lvd1689m` is a gated Hugging Face repo.
- Hugging Face authentication was completed outside the repository; account verified as `Novakor`.
- DINOv3 access was accepted, and `model.safetensors` was downloaded with `HF_HUB_DISABLE_XET=1` after the Xet path stalled.
- The test input `assets/example_image/steampunk_apparat.png` already has alpha, so the smoke script monkey-patched the RMBG stage as a no-op and did not download `briaai/RMBG-2.0`.
- Inference, remesh, UV unwrap, attribute sampling, and GLB export completed.
- Wall time from `/usr/bin/time`: `4:20.60`.
- Script-reported elapsed time: `254.716` seconds.
- Peak resident memory: `25,986,424` KB.
- Raw mesh before postprocess: `6,367,232` vertices, `13,423,136` faces.
- After remeshing: `10,713,810` vertices, `21,475,072` faces.
- Exported mesh: `186,752` vertices, `198,552` faces.
- Exported GLB: `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat.glb`, about `8.5M`.
- Output JSON: `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat.json`.
- Geometry preview: `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat_preview.png`.

## Resolved Blockers And Remaining Cautions

Resolved during this run:

- Authenticated access to `facebook/dinov3-vitl16-pretrain-lvd1689m`.
- Xet transfer stall for the DINOv3 safetensors file by using direct HTTP with `HF_HUB_DISABLE_XET=1`.
- Built-in EXR decode failure by using a no-HDRI smoke script.
- Gated background-removal dependency for this one RGBA input by using a no-op RMBG patch.

Remaining cautions:

- Do not store Hugging Face tokens in the repository.
- The GLB is exported with `EXT_texture_webp`; Blender 3.0 cannot import that texture extension. A geometry-only PLY was exported for preview rendering.
- First-run Triton autotuning adds noise to runtime. Repeat benchmarks should be run separately after cache warm-up.
- `nvdiffrast-rocm` remains a restricted/non-commercial-risk component and must stay research-only.
- This successful output is proof of external reference-engine viability only. It is not Aerathea visual canon or a production asset.

## DINOv3 Access Scope Audit

After approval, authenticated metadata checks for account `Novakor` confirmed access to the official Hugging Face `DINOv3` collection:

- Collection slug: `facebook/dinov3-68924841bd6b561778e31009`
- Collection title: `DINOv3`
- Collection contents: 13 model repositories and 2 paper entries
- TRELLIS.2 required repo: `facebook/dinov3-vitl16-pretrain-lvd1689m`

The 13 official DINOv3 model repositories reported as accessible were:

- `facebook/dinov3-vit7b16-pretrain-lvd1689m`
- `facebook/dinov3-vits16-pretrain-lvd1689m`
- `facebook/dinov3-convnext-small-pretrain-lvd1689m`
- `facebook/dinov3-vitb16-pretrain-lvd1689m`
- `facebook/dinov3-convnext-base-pretrain-lvd1689m`
- `facebook/dinov3-vits16plus-pretrain-lvd1689m`
- `facebook/dinov3-convnext-tiny-pretrain-lvd1689m`
- `facebook/dinov3-vitl16-pretrain-sat493m`
- `facebook/dinov3-vitl16-pretrain-lvd1689m`
- `facebook/dinov3-vith16plus-pretrain-lvd1689m`
- `facebook/dinov3-convnext-large-pretrain-lvd1689m`
- `facebook/dinov3-vit7b16-pretrain-sat493m`
- `facebook/dinov3-vitl16-chmv2-dpt-head`

Search also returned one extra related gated repo, `facebook/sam-3d-body-dinov3`, and authenticated metadata access succeeded for it as well. It is not part of the official 13-model DINOv3 collection list checked above.

## Research Boundary

All TRELLIS.2 outputs, if later produced, remain research-only. They must not become Aerathea visual canon, DCC source candidates, DCC game-ready candidates, Fully game-ready assets, or production training data unless a later license and provenance review explicitly permits it.
