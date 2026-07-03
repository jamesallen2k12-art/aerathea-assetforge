---
name: aerathea-unreal-implementation
description: Implement Aerathea assets in Unreal. Use for FBX import scripts, materials, material instances, Blueprints, sockets, startup scene placement, review actors, native class hooks, map integration, and focused Unreal validators.
---

# Aerathea Unreal Implementation

## Quick Start

1. Read the production package, modeling handoff, and current validators.
2. Use existing `Tools/Unreal/import_*.py`, `create_*.py`, and `validate_*.py` patterns.
3. Preserve stable Unreal asset names once docs reference them.
4. Add focused validators for new runtime contracts.
5. Run focused validators before startup validation.

## Ownership

Allowed by task packet:

- `Tools/Unreal/import_*.py`
- `Tools/Unreal/create_*.py`
- `Tools/Unreal/validate_*.py`
- `Source/Aerathea/` for native classes when assigned
- `Content/Aerathea/` through Unreal Editor command scripts

Do not change visual art direction or gameplay rules without approval.

## Validation Order

1. Python syntax check for scripts.
2. C++ build when native code changes.
3. Focused Unreal validator.
4. Related gameplay or VFX contract validator.
5. `Tools/Unreal/validate_startup_scene.py`.
