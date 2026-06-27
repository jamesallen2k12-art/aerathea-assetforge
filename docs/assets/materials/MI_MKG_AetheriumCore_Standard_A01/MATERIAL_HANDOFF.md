# MI_MKG_AetheriumCore_Standard_A01 Material Handoff

## Purpose

Author the Aetherium core material variant for `Gnome Armory.png#Core_Standard` so Mekgineer devices can share a controlled blue power language without unique shader work per prop.

## Source References

- Production package: `docs/assets/materials/MI_MKG_AetheriumCore_Standard_A01/PRODUCTION_PACKAGE.md`
- Parent kit: `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md`
- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Armory.png`

## Production Target

- Material instance: `MI_MKG_AetheriumCore_Standard_A01`
- Unreal path: `/Game/Aerathea/Materials/Props/Mekgineer/Armory/MI_MKG_AetheriumCore_Standard_A01`
- Parent material: `M_AET_AetheriumGlow_Blue_A01` now, or future `M_MKG_AetheriumCore_Master`

## Material Constraints

- Preserve a restrained blue Aetherium identity.
- Do not over-bloom in the startup scene.
- Use parameter tuning before adding unique textures.
- Keep the variant readable on small cores, lenses, and backpack reactors.

## Authoring Sequence

1. Duplicate or instance the approved Aetherium glow master.
2. Set core color, opacity, pulse, and rim intensity for the variant role.
3. Test on `SM_MKG_AetherCoreUnit_A01`, `SM_MKG_MicroReactor_A01`, and backpack/reactor candidates.
4. Validate readability at small prop scale and third-person camera distance.

## Texture Deliverables

- Reuse shared Aetherium noise/mask textures unless a new master material requires new inputs.
- No unique BC/N/ORM texture set is required for this material-only child package.

## Export Targets

- Unreal material path: `/Game/Aerathea/Materials/Props/Mekgineer/Armory/MI_MKG_AetheriumCore_Standard_A01`

## Unreal Validation

- Material instance loads with no missing parent or texture references.
- Emissive intensity remains restrained under the startup lighting path.
- Low-settings material fallback can disable expensive panning/noise.

## Acceptance Checklist

- Variant role is visually distinct without style drift.
- Glow is justified and not full-surface noise.
- Material can be shared across multiple Gnome armory child assets.
