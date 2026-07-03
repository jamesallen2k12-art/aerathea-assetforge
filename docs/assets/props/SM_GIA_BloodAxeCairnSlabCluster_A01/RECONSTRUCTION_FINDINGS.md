# SM_GIA_BloodAxeCairnSlabCluster_A01 Reconstruction Findings

## Status

The A1 Blood Axe cairn concept remains the desired visual target, but the current local reconstruction attempts have not produced an approvable full game-ready asset.

## What Failed

1. `SM_GIA_BloodAxeCairnSlabCluster_A01_Complete`
   - Technically valid static prop package.
   - Visually rejected by Flamestrike.
   - Failure mode: procedural/blockout forms, weak concept match, red paint reads as added bars instead of painted stone.

2. `SM_GIA_BloodAxeCairnSlabCluster_A01_HybridProjection`
   - Used A1 projected front shells plus side/back volume attempts.
   - Failure mode: still exposed vertical card/relief geometry from side and back angles.

3. `SM_GIA_BloodAxeCairnSlabCluster_A01_VolumeProjection`
   - Used real DCC stone volume with A1 source projection.
   - Failure mode: no longer a card, but still too blockout-heavy and not close enough to the source silhouette or hand-painted concept finish.

4. TripoSR single-image reconstruction
   - Tool installed under `Tools/External/TripoSR`.
   - ROCm PyTorch works outside sandbox on both AMD GPUs.
   - `torchmcubes` could not be built against this Fedora ROCm layout, so extraction was patched to use `scikit-image` marching cubes.
   - Gray-background pass reconstructed the input rectangle as a wall.
   - Background-removed pass produced a rounded noisy lump and lost the cairn slab identity.
   - Failure mode: TripoSR is not suitable for this irregular multi-stone environmental prop from a single painted concept image.

## Key Conclusion

The problem is not Unreal import, not LODs, and not simple material setup. The problem is that a single painted concept of an irregular prop cannot be converted into a concept-faithful 360-degree game asset by procedural scripting or lightweight single-image reconstruction.

The correct process is:

1. Build/approve a true multi-angle concept sheet or use a stronger image-to-3D generator to infer the full form.
2. Use that as a sculpt/modeling base in Blender.
3. Retopologize to mid-poly game geometry.
4. UV unwrap intentionally.
5. Project or hand-paint A1-style texture detail.
6. Generate LODs, collision, and Unreal import only after the visual match passes.

## Recommended Next Path

Use a higher-end image-to-3D or sculpt workflow rather than continuing procedural blockout:

- Primary next test: Hunyuan3D-2.1 shape generation, because it targets high-fidelity image-to-3D and PBR materials.
- Constraint: official setup is CUDA/PyTorch oriented; AMD/ROCm support may require compatibility work.
- Fallback: manual Blender sculpt/model pass from A1 with projection painting, using the source concept as the front art target and manually authored side/back forms.

## Current Review Outputs

- Hybrid projection board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_HybridProjection/SM_GIA_BloodAxeCairnSlabCluster_A01_HybridProjection_ProjectionVolumeReviewBoard.png`
- Volume projection board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_VolumeProjection/SM_GIA_BloodAxeCairnSlabCluster_A01_VolumeProjection_ConceptToVolumeReviewBoard.png`
- TripoSR gray-background board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR/SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR_ReviewBoard.png`
- TripoSR background-removed board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR_Rembg/SM_GIA_BloodAxeCairnSlabCluster_A01_TripoSR_ReviewBoard.png`
