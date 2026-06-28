# Infernal Visual Rules

## Approved Identity

- Race code: `INF`.
- Core read: mortal-descended demonic race blessed by Balgoroth.
- Required traits: horns, large leathery wings, long thick tail, reddish skin, black claws.
- Required abilities with visual hooks: regeneration and invisible sight.
- Combat doctrine: natural weapons and magic; mortal weapons read as weakness and should not define the base race.

## Body And Silhouette Rules

- Use upright predatory posture, not default hunched monster posture.
- Adult production body bands are Compact 5'0"-5'8", Standard 5'8"-6'8", Greater 6'8"-8'0", and Exalted 8'0"-9'0".
- Horns must be real geometry and visible in front, side, and gameplay camera views.
- Wings must read when folded; spread wings are for concept/silhouette and selected animation states.
- Tail must be thick and readable in side/back view, not a thin decorative cord.
- Claws must be visible on hands in neutral and combat poses.
- Regeneration should show through healed scars, skin seam marks, or subtle ember-vein texture, not gore.
- Invisible sight should show through eyes, brow marks, or controlled VFX, not oversized particles.

## Stage Rules For Lesser Infernals

| Stage | Visual rule |
| --- | --- |
| Spawn | Compact, autonomous, aggressive, horn buds, small claws, short tail, folded wing ridges. |
| 1st Kill | Sharper posture, stronger claws, longer tail, wing membrane emerging, first hunt scars. |
| Blooded | Young trained Infernal, obvious horns, partial wings, active culling temper body language. |
| Elder | Mature adult Infernal, full wings/tail/horns/claws, controlled predatory stance. |
| Ancient | Elder silhouette plus visible late age, scarred wings, heavier horn mass, ritual authority. |

## Material Rules

- Skin family: ember red, crimson, ash red, dark umber.
- Keratin family: black claws, black horn tips, worn horn edges.
- Wing family: dark leathery membrane with red-brown undertones.
- Ritual family: charcoal leather, ash cloth, obsidian, bone, scorched metal.
- Glow family: readable red-orange, ember, or violet abyssal accents for eyes, brands, mage marks, flame, lightning-like energy, and ritual power.

## Visual Cleanse Rules

- Use `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md` when evaluating Infernal source images or writing new Infernal prompts.
- Prefer `InfernalMaleLit.png` and `InfernalFemaleLit2.png` as the adult base anchors.
- Prefer `InfernalMaleSorcererLit.png` for mage posture and brand-channeling after reducing spell-circle density.
- Prefer `LesserInfernal24.png` as the bright Lesser/action anchor, with cinematic clutter reduced.
- Brighten midtones enough that red skin, black armor, dark wings, tail, and claws remain readable. If the source is too dark, start from a roughly 30 percent brighter pass before cleanup.
- Reduce tiny repeated rivets, random speckle artifacts, malformed micro-spikes, broken micro-chains, hanging noise, torn-strip noise, dense floor sigils, and glow fuzz that hides anatomy.
- Preserve skull/bone villain iconography, flame, lightning-like abyssal energy, glowing eyes, anger, and threat when those elements support Infernal identity.
- Prefer A03-style cleanup that keeps glow, menace, skulls, and useful detail. Use stronger A04-style cleanup only when A03 remains too noisy.
- Keep broad forms as geometry and push fine membrane veins, scars, scratches, small brands, and tiny surface details into texture/normal/emissive maps.

## Do Not Use

- No mortal swords, axes, bows, or polearms as defining race read.
- No true-Abyss creature silhouettes as the base identity.
- No excessive fire covering the body.
- No gore as regeneration language.
- No tiny over-modeled brands, stitches, or membrane veins that should be texture detail.

## Production Checks

- Can the character be recognized by horns/wings/tail/claws at MMO camera distance?
- Does the base body still look like a race with society, not a one-off demon?
- Do the visual rules support Warrior, Rogue, Hunter, and Mage without weapon dependency?
- Are wing and tail collision risks planned before Unreal import?
