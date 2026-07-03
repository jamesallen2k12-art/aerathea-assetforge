---
name: aerathea-vfx-materials
description: Author Aerathea VFX and material state contracts. Use for Niagara systems, material instances, emissive state language, VFX readability limits, bloom/particle-density control, VFX validators, state material handoffs, and final graph approval gates.
---

# Aerathea VFX Materials

## Quick Start

1. Read the asset package and runtime contract before authoring effects.
2. Keep emissive accents sparse and state-driven.
3. Use existing VFX import and validation scripts as patterns.
4. Validate material scalar ranges and asset references before visual signoff.
5. Treat template-derived Niagara systems as placeholders until a bespoke graph pass is approved.

## Readability Rules

- Preserve silhouettes from MMO/ARPG camera distance.
- Avoid constant full-screen fire, smoke walls, and bloom-heavy idle states.
- Use event pulses for accepted, rejected, hit, shutdown, or judgment states.
- Reduce particle density before removing primary ring/sigil/projectile readability.

## Required Outputs

- VFX purpose and state list
- material and color palette
- Niagara system/emitter names
- `User.*` parameter contract
- fixed bounds and LOD notes
- focused validator path
- startup validation impact
