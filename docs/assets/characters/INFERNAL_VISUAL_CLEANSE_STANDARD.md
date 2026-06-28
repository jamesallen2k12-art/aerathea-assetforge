# Infernal Visual Cleanse Standard

## Purpose

This standard applies the approved visual cleanse pass to the provided Infernal and Lesser Infernal concept references. The source images remain useful, but their noisy elements must not become production requirements.

The goal is a cleaner Aerathea production target: readable full-body silhouettes, brighter midtones, preserved villain power, reduced artifact noise, and buildable Unreal-friendly forms.

## Primary Production Anchors

| Role | Source image | Production use |
| --- | --- | --- |
| Adult male base | `InfernalMaleLit.png` | Cleanest adult male body read; use for horns, wing fold, tail thickness, black claws, skin value, and base pose language. |
| Adult female base | `InfernalFemaleLit2.png` | Cleanest adult female body read; use for wing span, armor/body separation, tail mass, clawed feet, and readable red/black material language. |
| Adult sorcerer | `InfernalMaleSorcererLit.png` | Mage posture, ritual hand shapes, brand-channeling, and sorcerer hierarchy; reduce spell-circle density and floor sigils. |
| Lesser combat/action | `LesserInfernal24.png` | Bright action reference for Lesser Infernal aggression, wing display, and readable opposition scenes; do not copy the crowded background. |

## Secondary References

| Source image | Keep | Cleanse before use |
| --- | --- | --- |
| `InfernalMaleSorcerer2.png` | Dynamic flight/casting, airborne aggression, large wing silhouette. | Reduce background noise, spell-burst density, and cropped/cinematic staging for production sheets. |
| `InfernalFemaleLit3.png` | Female lit-brand read, ritual hand magic, wing membrane glow. | Reduce chains, hanging jewelry, micro-spikes, and wing-edge clutter. |
| `InfernalMaleSorcerer3.png` | Greater/Exalted male power pose, brute mage mass, strong claws, skull iconography, fire, lightning, anger, and villain threat. | Brighten first if needed, then reduce rivets, artifact speckle, malformed micro-spikes, and noisy texture fragments without flattening glow or skull language. |
| `Lesser Infernal15.png` | Lesser aerial attack posture and predatory motion. | Avoid cropped wings, excessive weapon emphasis, and overly cinematic camera angle in production sheets. |
| `LesserInfernal13.png` | Lesser male attack energy, dwarf-scale combat contrast, lava battlefield mood. | Downplay mortal weapon use and reduce background/VFX noise. |
| `LesserInfernal14.png` | Lesser female ambush posture, claw reach, winged dive. | Avoid crop-heavy framing and reduce environmental complexity. |
| `LesserInfernal15.png` | Bright duel, readable female Infernal body, shield interaction, focused beam direction. | Reduce beam dominance and keep full silhouette visible. |
| `LesserInfernal20.png` | Bright daylight contrast and holy/Infernal opposition read. | Use as lighting reference only; avoid making the Infernal too weightless or angelic. |

## Cleanse Rules For All Provided Images

Preserve:

- Reddish skin, black claws, required horns, large leathery wings, long thick tails, glowing eyes, and predatory upright posture.
- Natural-weapon combat identity: claws, teeth, tail, wings, body power, and magic before mortal weapons.
- Balgoroth cult identity through brands, healed scar-emissive lines, ritual trim, major skull/bone iconography, flame, lightning-like abyssal energy, anger, and strong orange-red glow.
- Broad armor plates, wing bones, tail segments, horn mass, claw silhouettes, and large readable garment layers.

Reduce:

- Tiny repeated rivets, random orange/black speckle artifacts, malformed micro-spikes, broken micro-chains, tiny gold filigree, torn-strip clutter, and over-modeled armor shards.
- Tiny repeated skull/bone charms only when they become noisy texture clutter. Preserve large intentional skull belts, skull pauldrons, trophies, and villain motifs.
- Oversized spell circles, dense ground sigils, uncontrolled fire, and glow fuzz only when they hide anatomy, eyes, hands, claws, or wing membranes.
- Background complexity when creating production sheets.
- Cropped feet, hidden claws, clipped wings, or poses that obscure tail thickness.
- Mortal weapons as the defining combat read.

Brighten:

- Midtones on skin, wings, armor, and tail so forms read at MMO camera distance.
- Separation between red skin, black armor, dark wings, and smoky/lava backgrounds.
- Eye, brand, hand-magic, fire, and lightning accents enough to read invisible sight, regeneration, ritual power, and villain threat.

## Cleanup Strength

- If the source is too dark, create or request a roughly 30 percent brighter pass before cleanup.
- Use A03-style cleanup by default: remove artifact speckles, tiny repeated rivets, malformed micro-spikes, and noisy texture fragments while preserving glow, skulls, flame, lightning, anger, and useful detail.
- Use A04-style cleanup only when the image remains too noisy after A03. A04 can simplify surfaces further, but must not reduce eye glow, magic glow, villain threat, or major skull/bone iconography.

## Production Translation

- Model real geometry for body forms, horns, claws, wing bones, tail mass, major armor plates, major brands, and large ritual ornaments.
- Use texture, normal, AO, ORM, and emissive maps for fine membrane veins, scale texture, scar seams, tiny scratches, small rivets, cloth wear, and minor brand lines.
- Use full-body neutral or three-quarter poses for base sheets.
- Use action scenes only for animation, VFX, mood, and encounter staging.
- Keep emissive focused and readable: eyes, brands, mage hands, regeneration cores, and selected ritual marks.

## Prompt Addendum

Append this to Infernal image prompts when a cleanse pass is needed:

Clean the design for production readability: full body visible, feet and wings uncropped, readable midtone lighting, clear separation between red skin, black armor, dark wings, and background. If the source is too dark, start from a roughly 30 percent brighter pass. Preserve horns, leathery wings, thick tail, black claws, glowing eyes, skull/bone villain iconography, flame, lightning-like abyssal energy, anger, and Balgoroth brand identity. Use A03-style cleanup by default: reduce excessive tiny rivets, random speckle artifacts, malformed micro-spikes, broken micro-chains, torn-strip noise, dense spell clutter that hides anatomy, and photoreal surface garbage. Keep large forms buildable as mid-poly Unreal geometry and push micro-detail into texture, normal, AO, ORM, and emissive maps.
