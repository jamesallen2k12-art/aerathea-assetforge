# AssetForge External Evaluation Tools

Status: Research and evaluation only
Recorded: 2026-07-02

## Downloaded Tools

The following external repositories were downloaded under `Tools/External/` for ROCm architecture study, benchmark testing, and training-pipeline research:

| Tool | Local path | Upstream | Checked branch | Intended use |
|---|---|---|---|---|
| TRELLIS-AMD | `Tools/External/TRELLIS-AMD/` | `https://github.com/CalebisGross/TRELLIS-AMD` | `main` | Evaluate original TRELLIS ROCm structure and AMD inference behavior. |
| trellis2-amd | `Tools/External/trellis2-amd/` | `https://github.com/ATLAS-0321/trellis2-amd` | `rocm-port` | Evaluate TRELLIS.2 ROCm structure on RX 7900 XTX-class hardware. |
| FlashAttention | `Tools/External/flash-attention/` | `https://github.com/Dao-AILab/flash-attention` | `main` | TRELLIS.2 research dependency for the ROCm/Triton attention path. |

As of 2026-07-02, TRELLIS-AMD has an isolated research env, downloaded reference weights, and one recorded smoke-test report. `trellis2-amd` has an isolated ROCm 7.2 env with native modules importing successfully on the RX 7900 XTX, and one authenticated no-HDRI smoke completed successfully after DINOv3 access was accepted.

Runtime installs and model weights remain research-only and are tracked in `docs/projects/assetforge/ASSETFORGE_PROVENANCE_LOG.md`.

## Recorded Smoke Results

| Tool | Result | Output | Timing | Notes |
|---|---|---|---|---|
| TRELLIS-AMD | Built-in smoke completed once | `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/sample.glb` | First run completed; cached repeat failed before reliable timing footer | Cached repeat hit a ROCm illegal memory access inside `_nvdiffrast_c`. |
| trellis2-amd | No-HDRI RGBA-input smoke completed | `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat.glb` | `4:20.60` wall clock, `254.716` seconds script-reported | Output GLB has about `186,752` vertices and `198,552` faces. Peak resident memory was about `25.99 GiB`. |

## Production Boundary

These tools are not part of the Aerathea production asset pipeline. They may not be used to generate final in-game Aerathea assets, visual canon, DCC source candidates, DCC game-ready candidates, or Fully game-ready assets.

Outputs from these tools may be used only as temporary research artifacts for quality comparison, failure analysis, workflow timing, and benchmark documentation. Any final Aerathea asset must come from a clean, commercial-safe production path with approved source data, documented DCC work, Unreal validation, and Flamestrike approval.

## Allowed Use

- Study public architecture, model flow, data layout, ROCm setup, HIP build patterns, memory behavior, and failure modes.
- Benchmark candidate images against these engines to understand what they solve and where they fail.
- Use MIT-licensed source and model information only where the license allows, with attribution and retained license notices.
- Derive AssetForge requirements, test cases, dataset schemas, and quality gates from observed behavior.

## Prohibited Use

- Do not copy non-commercial source into Aerathea production code.
- Do not build the final commercial AssetForge engine around `nvdiffrast` or `nvdiffrast-rocm`.
- Do not use generated meshes, textures, GLBs, or render outputs from these engines as final in-game assets.
- Do not register any generated output from these tools as Aerathea visual canon.
- Do not train a commercial Aerathea model on tool-generated outputs until the full generation chain is confirmed commercial-safe.

## License Notes

- Microsoft TRELLIS and TRELLIS.2 code and Hugging Face model cards identify MIT licensing.
- The TRELLIS.2 AMD umbrella documents `nvdiffrast-rocm` as NVIDIA Source Code License and non-commercial only.
- `nvdiffrast`-derived pieces are acceptable for research/evaluation but must be replaced or avoided for any commercial production pipeline.

## AssetForge Direction

AssetForge should be built as a separate Aerathea-controlled program trained on clean, legal data. The target pipeline is:

1. Curate owned or properly licensed 3D assets.
2. Render multiview image, mask, depth, normal, albedo, and camera metadata through commercial-safe tools such as Blender.
3. Train or fine-tune a narrow Aerathea static-prop workflow first.
4. Export through our own validation path: mesh cleanup, UVs, texture maps, LODs, collision, Unreal import, review captures, and approval.

The external TRELLIS tools are reference engines and benchmarks only.
