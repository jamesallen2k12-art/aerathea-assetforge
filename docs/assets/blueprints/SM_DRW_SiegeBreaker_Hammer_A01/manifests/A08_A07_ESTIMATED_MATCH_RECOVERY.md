# A08 A07 Estimated-Match Recovery Record

- Date: `2026-07-22`
- Detected by: Flamestrike
- Status: `authoritative recovery boundary`

## Drift

The unexecuted `build_siegebreaker_a08_pommel_a07.py` used an estimated source
window (`x=512..628`, `y=1074..1253`) and a hand-selected `13 degree` yaw while
being described as a perfect-match revision.

## Classification

- A07 script: `invalid; preserved in place; never executed`.
- A07 `.blend`, manifest, and review: do not exist.
- A06 pommel: `reference only; revision requested by Flamestrike`.
- A01-A05 pommels: remain `quarantined`.

## Recovery

Do not repair A07 forward. A09 restarts from the immutable front, left, back,
and concept sources, recomputes scan membership, uses uniform source-pixel
proportions, constructs one physical half, and mirrors it in Blender.
