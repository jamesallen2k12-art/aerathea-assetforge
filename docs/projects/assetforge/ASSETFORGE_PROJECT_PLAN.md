# AssetForge Project Plan

Status: Active research project
Recorded: 2026-07-02
Owner: Aerathea / Flamestrike

## Objective

Build AssetForge as an Aerathea-controlled tool that converts approved 2D art inputs into clean 3D static-prop asset candidates, then validates them through Blender and Unreal before any asset can enter the Aerathea production pipeline.

The long-term user experience target is:

1. Drop an image into the tool.
2. Press convert.
3. Receive a candidate 3D asset package with mesh, textures, scale notes, LOD suggestions, collision suggestion, review renders, and validation report.
4. Promote only after Blender and Unreal review.

## Production Boundary

The external TRELLIS AMD tools are research/reference engines only.

They may be used for:

- ROCm/HIP architecture study.
- Benchmarking.
- Failure analysis.
- Understanding data formats and model flow.
- Comparing quality against our own future tool.

They may not be used for:

- Final Aerathea in-game assets.
- Aerathea visual canon.
- DCC source candidates.
- DCC game-ready candidates.
- Fully game-ready assets.
- Commercial AssetForge production code where restricted dependencies are involved.

Any output from external engines must stay quarantined as research output.

## Recovery And Checkpoint Policy

AssetForge work must be recoverable after a reboot, hard reset, power outage, or Codex context loss.

Tracked recovery files:

- `docs/projects/assetforge/RECOVERY_JOURNAL.md`
- `docs/projects/assetforge/ASSETFORGE_PROVENANCE_LOG.md`
- `docs/projects/assetforge/ASSETFORGE_PROJECT_PLAN.md`
- `docs/projects/assetforge/reports/`
- `docs/systems/ASSETFORGE_EXTERNAL_EVALUATION_TOOLS.md`

Ignored recovery files:

- `Saved/ProjectRecovery/`
- `Saved/AssetForgeResearch/`

Checkpoint command:

```bash
Tools/System/aerathea_checkpoint.sh "short note"
```

Automatic local checkpoint timer:

```bash
Tools/System/install_aerathea_checkpoint_timer.sh
systemctl --user status aerathea-checkpoint.timer
```

The timer runs this local-only snapshot every 30 minutes:

```bash
Tools/System/aerathea_checkpoint.sh --local-only "automatic systemd checkpoint"
```

Local-only snapshots update `Saved/ProjectRecovery/LATEST.md` and `Saved/ProjectRecovery/LOCAL_CHECKPOINTS.md` without modifying tracked files. Manual checkpoints still append to the tracked recovery journal and are required at intentional milestones.

Use it:

- Before starting a long TRELLIS, Blender, Unreal, import, validation, or benchmark job.
- Immediately after a long job completes or fails.
- Before stopping for the night.
- Before any risky system operation, reboot, reset, package install, or storage move.
- Before ending a session with meaningful tracked changes, run a manual checkpoint, commit the scoped tracked work, and push `main` to `assetforge`.

The tracked journal records the short resume trail. The ignored snapshot folder records bulky local details such as full `git status`, recent files, running processes, disk state, and recent research outputs.

## Current Local State

External repos downloaded:

| Tool | Local path | Branch | Commit | Size | State |
|---|---|---|---|---|---|
| TRELLIS-AMD | `Tools/External/TRELLIS-AMD/` | `main` | `23a1b81` | Source about 477M; venv about 18G; weights about 4.0G | Isolated ROCm 7.2 env installed. First built-in smoke test completed and outputs were quarantined. Cached repeat failed in `_nvdiffrast_c` with ROCm illegal memory access. |
| trellis2-amd | `Tools/External/trellis2-amd/` | `rocm-port` | `4034cd8` | Source plus env about 18G; model cache about 16G after successful smoke | Isolated ROCm 7.2 env installed. FlexGEMM, `nvdiffrast-rocm`, CuMesh, O-Voxel, and FlashAttention import on GPU. FlashAttention forward pass works. Authenticated no-HDRI RGBA-input smoke completed and exported a research GLB. |
| FlashAttention | `Tools/External/flash-attention/` | `main` | `73c992c8` | about 1.6G source/submodules | Cloned as external TRELLIS.2 research dependency after `@tridao` branch reference failed. Ignored from git. |

Project guardrail note:

- `docs/systems/ASSETFORGE_EXTERNAL_EVALUATION_TOOLS.md`

Git ignore state:

- `Tools/External/` is ignored.
- External source, model caches, virtual environments, and research dependencies should not be committed into Aerathea.

## Known Machine Baseline

From prior local checks:

- CPU: AMD Ryzen 7 5800X3D, 8 cores / 16 threads.
- RAM: about 125 GiB.
- GPUs: 2x AMD Radeon RX 7900 XTX, about 24 GB VRAM each, ROCm visible.
- Current project disk had about 953 GB free on `/`.
- Extra large storage exists but should be mounted/planned before dataset scale-up.
- Blender 4.5.11 exists under `Tools/External/Blender/`.

## Legal And License Rules

1. Record every external repo, model, dataset, script, and dependency.
2. Keep source, license, model revision, and download date in the provenance log.
3. Treat `nvdiffrast` and `nvdiffrast-rocm` as research/evaluation only because of NVIDIA non-commercial restrictions.
4. Do not copy non-commercial code into AssetForge production code.
5. Do not train a commercial Aerathea model on tool-generated outputs until the full generation chain is confirmed commercial-safe.
6. Use owned or clearly commercially usable assets for AssetForge training.

## Full Ordered Process

### 1. Lock The Legal And Production Boundary

- Keep TRELLIS-AMD and trellis2-amd research/reference only.
- No generated output becomes final Aerathea game content.
- No generated output becomes visual canon.
- No restricted code enters AssetForge.

### 2. Maintain The Provenance Log

- Record external repos, licenses, commits, model weights, datasets, scripts, and install actions.
- Track what is only studied versus what is actually used.
- Flag restricted dependencies clearly.

### 3. Create Research Quarantine Folders

Create separate folders for:

- External source repos.
- Model weights.
- Test inputs.
- Generated research outputs.
- Runtime logs.
- Benchmark reports.

Research outputs must stay out of `SourceAssets/` and Unreal `Content/`.

### 4. Review Install Scripts Before Running Anything

Read before executing:

- `Tools/External/TRELLIS-AMD/install_amd.sh`
- `Tools/External/TRELLIS-AMD/setup.sh`
- `Tools/External/trellis2-amd/install.sh`
- `Tools/External/trellis2-amd/forks/TRELLIS2-rocm/setup.sh`

Block:

- Blind `sudo`.
- Global Python installs.
- Uncontrolled system changes.
- Repo-polluting model or cache downloads.

### 5. Verify Machine Readiness

- Confirm ROCm sees both RX 7900 XTX GPUs.
- Confirm ROCm version.
- Confirm Python versions.
- Confirm disk space.
- Confirm RAM.
- Confirm compiler/build tools.
- Confirm PyTorch ROCm compatibility.

### 6. Set Storage Policy

- Keep external source repos in `Tools/External/`.
- Put model weights and future datasets in a planned cache/storage location.
- Do not store large datasets casually inside the repo.
- Keep caches outside git.

### 7. Install TRELLIS-AMD First

- Create isolated env.
- Install PyTorch ROCm matching this system.
- Install required packages.
- Build required HIP/native extensions.
- Download required TRELLIS model weights.
- Run built-in example.

### 8. Smoke-Test TRELLIS-AMD

Record:

- Command used.
- Input image.
- Output files.
- Runtime.
- VRAM usage.
- Errors.
- Mesh/GLB export success.
- Output quality.
- License-risk components used.

### 9. Install trellis2-amd Second

- Create separate isolated env.
- Build ROCm/HIP submodules.
- Download TRELLIS.2 weights.
- Handle Hugging Face token outside the repo if needed.
- Run built-in example.

### 10. Smoke-Test trellis2-amd

Record:

- Command used.
- Input image.
- Output files.
- Runtime.
- VRAM usage.
- Errors.
- PBR mesh/GLB export success.
- Output quality.
- License-risk components used.

Current result:

- Built-in `example.py` failed before inference because OpenCV could not decode bundled DWAB EXR `assets/hdri/forest.exr`.
- A no-HDRI smoke script bypassed the HDRI path and completed after Hugging Face access to `facebook/dinov3-vitl16-pretrain-lvd1689m` was accepted.
- The successful smoke used `assets/example_image/steampunk_apparat.png`, which already has alpha, so the gated `briaai/RMBG-2.0` background-removal model was not downloaded.
- Successful output: `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat.glb`.
- Runtime: `4:20.60` wall clock; script-reported elapsed time `254.716` seconds.
- Peak resident memory: about `25.99 GiB`.
- Exported GLB mesh stats: `186,752` vertices and `198,552` faces.
- Geometry preview: `Saved/AssetForgeResearch/trellis2-amd/outputs/trellis2_smoke_steampunk_apparat_preview.png`.

### 11. Run Controlled Benchmarks

Benchmark images:

- Simple clean object.
- Stone/cairn-like prop.
- A01/cairn reference images.
- Low-res input.
- High-res input.

Save outputs only as research outputs.

Current benchmark report:

- `docs/projects/assetforge/reports/ASSETFORGE_CONTROLLED_BENCHMARKS_20260703.md`

Current controlled benchmark result:

- `cairn_a01_triposr_masked_rgba` through `trellis2-amd`: `FAIL_FLAT_RELIEF`. The run completed in `3:12.29`, but the generated mesh extents were about `1.001 x 0.428 x 0.002`, so it reconstructed as a flat relief/plane instead of a volumetric cairn static prop. Do not present this output for approval.
- `cairn_a01_sculpted_v4_dcc_multiview_mesh` through `TRELLIS-AMD`: `PASS_VOLUME_GATE_RAW_MESH`. The run completed in `0:51.90`; the generated mesh extents were about `1.001 x 0.928 x 0.617`, so it produced a real cairn-like volume. The raw output is still research-only, very high density at `831,554` faces, and needs cleanup, decimation, paint/texture work, UVs, collision, LODs, and Unreal validation before any production-facing candidate exists.

Current cleanup/budget result:

- Local Blender decimation test indicates this generated cairn wants about `18k-25k` faces for a practical LOD0-style MMO asset after cleanup and paint/normal support.
- `40k-60k` faces is a safer high/detail review range.
- `8k-12k` faces reads as a lower LOD/chunky stylized version.
- `4k` faces preserves broad massing but loses too much surface language for this cairn as a primary close-view asset.
- Initial GLB export reported mesh-validity warnings on decimated variants, but a follow-up Blender repair pass re-exported clean `50k`, `20k`, and `10k` GLBs without those warnings.
- Unreal import validation on the repaired `20k` and `50k` GLBs passed as quarantined research-only assets. Temporary Unreal content was deleted after measurement. Raw imports produced one static mesh each, one LOD, one fallback material slot, one convex collision entry, and about `1 m` bounds; scale normalization, tangent cleanup, material-slot authoring, generated LODs, UV/material metadata, and collision policy remain required AssetForge post-process work.

Queued non-cairn benchmark candidate:

- `docs/assets/reference/planet_maps/ProjectedEarth_PolarCluster/` should be used for planet/map texture and Unreal import validation, not irregular prop-volume reconstruction.

### 12. Analyze External Engine Limits

Evaluate:

- Geometry accuracy.
- Texture quality.
- UV quality.
- Topology cleanliness.
- Runtime cost.
- AMD stability.
- Dependency risks.
- Where `nvdiffrast` is required.
- Whether multiview conditioning reliably prevents flat-relief failures on static props.
- How much cleanup/decimation is needed to move raw outputs toward Aerathea MMO triangle budgets.

### 13. Choose Commercial-Safe Replacements

Candidate replacements:

- Blender for rendering, baking, masks, normals, depth, UV checks, and texture baking.
- PyTorch3D or our own renderer only if differentiable rendering is required.
- Vulkan/OpenGL path if useful for a custom renderer.

Avoid `nvdiffrast` in the final commercial path.

### 14. Define AssetForge Data Format

Each training or evaluation item should include:

- Input image.
- Multiview renders.
- Masks.
- Depth.
- Normals.
- Albedo/PBR.
- Camera metadata.
- Mesh.
- UVs.
- Texture maps.
- Scale.
- Source/license manifest.
- Quality score.

### 15. Build Dataset Acquisition Rules

Every asset needs:

- Source.
- License.
- Commercial-use status.
- Derivative rights.
- Training rights.
- Category.
- Quality rating.
- Geometry cleanliness rating.

Reject unclear licenses.

### 16. Build Dataset Factory

- Import legal 3D assets.
- Normalize scale and orientation.
- Render multiview training images in Blender.
- Generate masks, depth, normals, albedo, and camera metadata.
- Run geometry, UV, and material quality checks.

### 17. Start With A Narrow Dataset

Start with static props:

- Stones.
- Cairns.
- Crates.
- Barrels.
- Ruins.

Do not start with:

- Characters.
- Creatures.
- Buildings.
- Animated assets.

### 18. Build AssetForge v0

Required components:

- Drop-frame input.
- Convert button.
- Job queue.
- Model runner.
- Blender post-process.
- Mesh/texture export.
- Review renders.
- Validation report.

### 19. Train Or Fine-Tune Narrow Model

- Use clean static-prop dataset.
- Track failures.
- Retrain on corrected examples.
- Compare against TRELLIS outputs as benchmarks only.

### 20. Add Game-Ready Post-Process

Generate:

- Mesh cleanup.
- UV validation.
- Texture maps.
- Triangle budget.
- LOD candidates.
- Collision proxy.
- Scale notes.
- FBX/GLB export.

### 21. Validate In Unreal

Check:

- Import success.
- Scale.
- Materials.
- Collision.
- LODs.
- Lighting.
- Silhouette.
- Performance.
- Review captures.

### 22. Approval Gate

Only after Unreal validation and Flamestrike approval can an asset move toward Aerathea production.

Until then, output is research output or a candidate only, not Fully game-ready.

## Immediate Next Step

TRELLIS-AMD and trellis2-amd are now runnable as research/reference engines and have recorded smoke-test reports:

- `docs/projects/assetforge/reports/TRELLIS_AMD_SMOKE_TEST_20260702.md`
- `docs/projects/assetforge/reports/TRELLIS2_AMD_INSTALL_NOTES_20260702.md`

Next step: run controlled benchmark images through the reference engines, starting with simple static props and cairn-like forms. Record runtime, VRAM/RAM behavior, mesh quality, texture quality, topology problems, UV quality, and where postprocess cleanup is mandatory.

Stop before free asset or dataset acquisition. Flamestrike has ideas for that stage and should be brought back in before any free assets are downloaded.

Current next benchmark direction:

- Use multi-view cairn inputs and a multi-image-capable path before trying more single-image cairn generation. Single-view TRELLIS.2 produced a flat-relief failure and should not be repeated without a materially different input or configuration.
- Gate previews internally. Only open a visual approval image for Flamestrike if the output plausibly reads as the intended asset.

## Reload Checklist

When resuming this project, read these first:

1. `docs/projects/assetforge/ASSETFORGE_PROJECT_PLAN.md`
2. `docs/projects/assetforge/RECOVERY_JOURNAL.md`
3. `docs/systems/ASSETFORGE_EXTERNAL_EVALUATION_TOOLS.md`
4. `docs/projects/assetforge/reports/ASSETFORGE_CONTROLLED_BENCHMARKS_20260703.md`
5. `.gitignore`

Then verify local state:

```bash
git -C Tools/External/TRELLIS-AMD status --short --branch
git -C Tools/External/TRELLIS-AMD rev-parse --short HEAD
git -C Tools/External/trellis2-amd status --short --branch
git -C Tools/External/trellis2-amd rev-parse --short HEAD
git -C Tools/External/trellis2-amd submodule status --recursive
du -sh Tools/External/TRELLIS-AMD Tools/External/trellis2-amd
```

Expected state after the first TRELLIS/TRELLIS.2 evaluation pass:

- `TRELLIS-AMD`: branch `main`, commit `23a1b81`; isolated venv exists; model/cache folder exists; first smoke outputs are quarantined in `Saved/AssetForgeResearch/TRELLIS-AMD/outputs/`.
- `trellis2-amd`: branch `rocm-port`, commit `4034cd8`; isolated venv exists; ROCm native modules import; DINOv3 gated dependency is cached after authenticated access; first successful GLB smoke output is quarantined in `Saved/AssetForgeResearch/trellis2-amd/outputs/`.
- Free asset and dataset acquisition has not started.

## Status Vocabulary

For AssetForge-generated assets, keep Aerathea terminology strict:

- `Research output`: temporary evaluation output. Not production.
- `AssetForge candidate`: generated candidate package for review. Not production.
- `DCC source candidate`: Blender or other DCC source exists for review.
- `DCC game-ready candidate`: source, FBX, UV/texture/material plan, LODs, collision proxy, scale, and proof renders exist and the asset is ready for Unreal import testing.
- `Fully game-ready`: imported into Unreal, configured, placed in gameplay or approved review map, validated for scale/materials/LODs/collision/performance, and approved for the asset library.

Do not call AssetForge output Fully game-ready without Unreal validation and approval.
