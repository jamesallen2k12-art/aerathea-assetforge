# SM_DRW_SiegeBreaker_Hammer_A01 - Measurement Manifest

- Artifact status: `quarantined`
- Superseded on: 2026-07-21
- Reason: the verified final package locks the origin to the bottom center of
  the pommel at `Z=0` and resolves the shaft/pommel relationship with a `4 cm`
  overlap. The centered assembly layout below must not drive production.
- Replacement authority:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/manifests/MEASUREMENT_AND_OWNERSHIP_CONTRACTS.json`

- Date: 2026-07-07
- Source: `VC-DRW-SiegeBreaker-Hammer-A01` (approved concept art)
- Historical status: measurement approved, DCC blockout claimed; superseded

## Source Evidence

- Concept image: `SourceAssets/Concepts/SiegeBreaker/siege_breaker_concept_view.png` (1122x1402 px)
- Orthographic views: front, back, left, right, top, bottom (same resolution)
- Source dimensions from concept specification document

## Calibration Data

- Source image dimensions: 1122 x 1402 px
- Object fills canvas (hero presentation render)
- Calibration: dimensions taken from authoritative spec document, not pixel measurement (no background separation in hero render)

## Component Dimensions (cm)

| Component | Dimension | Measurement |
|---|---|---|
| Overall length | 170 cm | Authoritative spec |
| Head max width | 52 cm | Authoritative spec |
| Head height | 38 cm | Authoritative spec |
| Head depth | 32 cm | Authoritative spec |
| Shaft length | 118 cm | Authoritative spec |
| Grip wrap length | 42 cm | Authoritative spec |
| Handle diameter | 5 cm | Authoritative spec |
| Pommel length | 18 cm | Authoritative spec |
| Pommel max width | 11 cm | Authoritative spec |

## Assembly Layout (Z-axis)

- Head top: +85 cm
- Head bottom: +47 cm (38 cm head height)
- Shaft visible: -21 cm to +47 cm (68 cm)
- Grip zone: -85 cm to -43 cm (42 cm)
- Pommel top: -103 cm
- Pommel bottom: -118 cm
- Origin (grip center): 0 cm

## DCC Blockout

- Script: `Tools/DCC/build_siegebreaker_hammer.py`
- Blender file: `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/SM_DRW_SiegeBreaker_Hammer_A01.blend` (to be created)
- Scale: 1 Blender unit = 1 cm
- Origin: center of grip area

## Next Steps

1. Run blockout script in Blender
2. Verify all dimensions match spec
3. Review proportions visually
4. Proceed to modeling pass with authoring
