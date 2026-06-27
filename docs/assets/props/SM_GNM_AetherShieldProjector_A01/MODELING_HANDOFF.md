# SM_GNM_AetherShieldProjector_A01 Modeling Handoff

## Purpose

Build the first DCC review source and Unreal import for the Gnome/Mekgineer Aether shield projector used by `BP_GNM_HeavyMekShieldwall_A01`.

## Source References

- Blueprint package: `docs/assets/blueprints/BP_GNM_HeavyMekShieldwall_A01/PRODUCTION_PACKAGE.md`
- Rivalry kit: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/PRODUCTION_PACKAGE.md`
- Gnome/Mekgineer visual anchor: `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md`

## DCC Requirements

- Author in centimeters.
- Origin at ground center.
- +X points toward the projected shield.
- Keep final footprint roughly 140 cm wide/deep and 120 cm tall.
- Include UCX collision proxy for first-pass review.
- Export as FBX to the package export path.

## Required Sockets

| Socket | Purpose |
| --- | --- |
| `vfx_core` | Aetherium core glow and boot pulse |
| `vfx_shield_emit_l` | Left shield arc emitter |
| `vfx_shield_emit_r` | Right shield arc emitter |
| `attach_mek_l` | Optional heavy Mek attachment left |
| `attach_mek_r` | Optional heavy Mek attachment right |
| `damage_spark` | Impact sparks and overload feedback |

## Unreal Targets

- Static mesh: `/Game/Aerathea/Props/Gnomes/Mekgineer/SM_GNM_AetherShieldProjector_A01`
- Review actor consumer: `/Game/Aerathea/Blueprints/GnomeOgre/BP_GNM_HeavyMekShieldwall_A01`
- Material instances: `/Game/Aerathea/Materials/Instances/MI_GNM_AetherShieldProjector_A01_*`

## Review Notes

The current DCC pass is a deterministic technical review mesh. Final art still requires sculpt/polish, authored UVs, texture sets, tuned collision, and final material instances.
