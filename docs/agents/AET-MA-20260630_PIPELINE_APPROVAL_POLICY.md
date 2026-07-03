# Aerathea Standing Pipeline Approval Policy

Date: 2026-06-30

Source: Flamestrike approved the production pipeline and asked to stay involved in subjective gates: image approvals, aesthetic approvals, combat systems, playstyles, combat feel, and visual-marker consistency.

Reference pipeline: `docs/assets/CONCEPT_ART_TO_GAME_READY_ASSET_PIPELINE.md`

## Standing Approval

Technical production work may proceed without repeated user approval when all of the following are true:

- A task packet names the goal, dependencies, allowed files, blocked files, validators, and integration owner.
- The work stays inside the approved Aerathea visual style, visual-canon entries, race/faction anchors, scale anchors, material language, and performance budgets.
- The work is technical implementation, validation, import configuration, DCC/export/proof generation, documentation/index alignment, or review-capture preparation.
- Any first-pass DCC, Unreal, material, VFX, or startup review output is treated as a review target, not final art approval.
- QA evidence and remaining approval blockers are recorded before Docs/Index marks a lane complete.

This standing approval applies to scoped task-packet work such as DCC source creation, source/export folder creation, FBX export, Unreal import/configuration, material instance setup, focused validators, build/import status docs, review captures, and task-board/index updates.

Status wording must follow the project pipeline. A `DCC game-ready candidate` is not the same as a fully game-ready asset. Full game-ready status requires Unreal import, gameplay or approved review-map testing, validation, and any required Flamestrike aesthetic approval.

## Required User Approval Gates

Stop and ask Flamestrike before locking or changing:

- generated image selections, source-concept approval, or final image approval
- registering an image or selected variant as visual canon
- final aesthetic approval, final silhouette, color language, faction identity, race identity, hero art direction, or major VFX behavior
- combat-system identity, class playstyle, combat feel, ability pacing, encounter feel, or final gameplay behavior
- final economy, vendor, reward, backend, multiplayer authority, or live-service direction
- source-concept storage policy outside the repo
- final startup-scene showcase approval when the change is meant to represent shipped visual composition

## Visual Marker Discipline

Every visual, DCC, Unreal, or VFX task packet must preserve the approved Aerathea markers:

- strong readable silhouettes
- stylized fantasy MMORPG shape language
- hand-painted texture intent with baked-AO-style depth
- mid-poly MMO-safe geometry and aggressive LODs
- restrained emissive accents
- no excessive micro-detail, overglow, photoreal clutter, or style drift
- race, creature, faction, and scale anchors from `AGENTS.md`

If a technical pass reveals that the asset no longer matches these markers, return it to `Needs Approval` or a corrective art-direction task before treating it as build-ready.

## Visual Canon Discipline

Use provided concept art and approved generated variants as binding visual targets. Once Flamestrike chooses an image or variant, record it in `docs/assets/VISUAL_CANON_REGISTRY.md` before production treats the look as locked.

DCC, material, and Unreal review work should copy the approved canon target's production-relevant silhouette, material language, color language, culture, and mood. Procedural blockouts, failed captures, and unapproved first-pass review meshes are not canon.

## Operating Rule

When a decision is objective and scoped, proceed and validate. When a decision changes the player's feel, fantasy, combat identity, or final visual read, stop for Flamestrike.
