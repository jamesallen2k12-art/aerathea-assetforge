# SK_INF_Base_A01 Animation Handoff

## Purpose

Define the first production animation rules for adult Infernals, Lesser Infernals, and class overlays such as `SK_INF_Mage_A01`. This handoff protects the race identity in motion: natural weapons, wings, tail, predatory intelligence, controlled rage, regeneration, and invisible sight must all read through animation, not only still images.

## Source References

- Base package: `docs/assets/characters/SK_INF_Base_A01/PRODUCTION_PACKAGE.md`
- Final art direction: `docs/assets/characters/SK_INF_Base_A01/FINAL_ART_DIRECTION.md`
- Lesser lifecycle sheet: `docs/assets/characters/SK_INF_Lesser_A01/LIFECYCLE_STAGE_SHEET.md`
- Mage package: `docs/assets/characters/SK_INF_Mage_A01/PRODUCTION_PACKAGE.md`
- Visual cleanse standard: `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`
- Brand material states: `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md`
- Combat VFX: `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/PRODUCTION_PACKAGE.md`

## Production Target

- Base animation target: `ABP_INF_Base_A01`
- Lesser animation target: `ABP_INF_Lesser_Base_A01` with stage overrides
- Mage overlay target: `ABP_INF_Mage_A01`
- Primary skeleton: final `SK_INF_Base_A01` skeleton when locked
- First implementation state: placeholder ABPs exist for base and Lesser review meshes; real authored animation sets pending

## Core Motion Identity

- Infernals are not hunched monsters. They move with upright predatory control and visible intelligence.
- Natural weapons lead the motion language: clawed hands, wing pressure, thick tail counterbalance, horns/head threat, and body-powered magic.
- Rage is controlled until triggered. Even violent actions should feel intentional rather than mindless.
- Wings and tail are part of balance and threat display, not decorative appendages.
- Regeneration and invisible sight should create readable body-state changes without constant glow spam.

## Claw Animation Rules

- Hands default to semi-open claw readiness, not relaxed human hands.
- Important poses:
  - neutral claw idle
  - open palm cast
  - hooked grip
  - rake windup
  - two-hit claw combo
  - pounce claw spread
  - finishing slash
  - see-invisible focus hand lift
- Claw attacks should travel in broad arcs readable from MMO camera distance.
- Do not create many tiny finger flicks as the main read. Use finger detail as secondary polish after wrist, elbow, shoulder, and torso lines read.
- Required sockets:
  - `hand_l_claw`
  - `hand_r_claw`
  - `hand_l_cast`
  - `hand_r_cast`
  - `vfx_hand_l`
  - `vfx_hand_r`

## Wing Animation Rules

- Default movement uses folded wings that do not block navigation.
- Spread wings are reserved for readable states:
  - intimidation flare
  - wing-assisted hop
  - leap takeoff
  - glide test if gameplay approves it
  - wing buffet
  - wing mantle cast
  - hit-react spread
  - damaged fold
- Wing fold transitions need clear shoulder/root motion before membrane motion.
- Wing membranes should avoid noisy flutter in idle. Use low-frequency weight shifts and occasional tension changes.
- Wings are non-blocking by default; gameplay collision should be enabled only for specific abilities or boss variants.
- Required sockets:
  - `wing_l_tip`
  - `wing_r_tip`
  - `vfx_wing_root_l`
  - `vfx_wing_root_r`

## Tail Animation Rules

- Tail is thick, muscular, and expressive. It should never read as a thin decorative cord.
- Tail supports:
  - walk/run counterbalance
  - crouch/pounce preparation
  - turn anticipation
  - tail sweep attack
  - hit reaction
  - rage lash
  - focused stillness for high-status characters
  - spellcasting counterweight for mage poses
- Keep idle motion restrained and purposeful. Excess constant swaying will make the race feel less controlled.
- Tail collision should use 2-4 simplified bodies only when needed for combat/hit reaction.
- Required sockets:
  - `tail_tip`
  - `vfx_tail_tip`

## Rage And Culling Temper Rules

- Adult rage is controlled brutality: stillness, eye lock, brand brightening, hand flex, wing tension, then sudden violence.
- Lesser culling temper is less disciplined:
  - Spawn: skitter, recoil, sudden pounce
  - 1st Kill: aggressive lunge, feeding crouch without gore emphasis, rage idle
  - Blooded: stalk, leap, short wing burst, two-hit claw combo
  - Elder: controlled idle, wing flare, claw strike, tail sweep
  - Ancient: slow authority turn, wing mantle, ritual judgment pose
- Avoid cartoon tantrum motion. Rage should be frightening because it is powerful, fast, and purposeful.
- VFX sync: eyes and brands brighten during escalation, then collapse back to focused glow after release.

## Regeneration Animation Rules

- Regeneration reads as body control and healed scar response, not gore.
- First-pass animation beats:
  - injury/hit reaction
  - brief torso or limb tension
  - chest/core brand pulse
  - scar-line glow and skin-settle motion
  - controlled exhale or predatory reset
- Avoid open wound animation as the primary read.
- Suggested sockets/VFX:
  - `vfx_regen_core`
  - `vfx_brand_chest`
  - `vfx_brand_forearm_l`
  - `vfx_brand_forearm_r`
- Material state dependency: `MI_INF_BrandGlowStates_A01_Smolder` or `MI_INF_BrandGlowStates_A01_TrialActive` depending gameplay context.

## Invisible-Sight Animation Rules

- Invisible sight should feel predatory and supernatural, not like ordinary looking.
- First-pass animation beats:
  - head stills
  - eyes brighten
  - brow/forehead brand activates
  - one hand or claw rises slightly as if triangulating a target
  - wings and tail go still for a short focus beat
  - target-lock release into movement or cast
- Keep VFX tight to eyes, brow, hand, and optional target-line shimmer.
- Required sockets:
  - `vfx_eye_l`
  - `vfx_eye_r`
  - `vfx_sorcerer_focus`
- VFX dependency: `NS_INF_InvisibleSightReveal_A01` from `VFX_INF_AbyssalSpellcasting_A01`.

## Base Animation Set

Required first authored adult set:

- idle calm
- idle controlled rage
- walk
- run
- turn left/right
- jump
- land
- wing-assisted hop
- claw combo
- pounce
- tail sweep
- wing buffet
- see-invisible focus
- regeneration flare
- brand activation
- hit react light/heavy
- death
- interact

## Mage Overlay Set

Required first mage overlay:

- idle predatory caster
- brand-channel loop
- one-hand claw cast
- two-hand abyssal bolt
- wing-mantle cast
- invisible-sight reveal
- regeneration flare
- rage surge
- worthiness judgment gesture
- hover/leap cast anticipation if traversal permits it later

## Unreal Notes

- Base ABP target: `/Game/Aerathea/Characters/Infernals/Base/ABP_INF_Base_A01`
- Lesser ABP target: `/Game/Aerathea/Characters/Infernals/Lesser/ABP_INF_Lesser_Base_A01`
- Mage ABP target: `/Game/Aerathea/Characters/Infernals/Mage/ABP_INF_Mage_A01`
- Use montage sections for claw combo, tail sweep, wing buffet, regeneration flare, invisible-sight reveal, and mage casts.
- Animation notifies should trigger brand material state changes and Niagara events through named sockets.
- Default movement collision ignores folded wings and tail secondary bodies unless an ability explicitly enables them.

## Acceptance Checklist

- Adult Infernals move as intelligent mortal-descended predators, not mindless monsters.
- Claws, wings, tail, rage, regeneration, and invisible sight each have readable motion rules.
- Lesser stages show culling temper by age/stage without gore.
- Mage overlay uses body/brand/hand/wing casting instead of mortal weapons.
- Sockets, VFX dependencies, material dependencies, ABP targets, and notify expectations are documented.
