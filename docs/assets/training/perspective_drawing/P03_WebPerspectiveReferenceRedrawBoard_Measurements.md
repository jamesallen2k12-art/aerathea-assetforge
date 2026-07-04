# P03 Measured Perspective Redraw Data

Coordinates are normalized to each downloaded source image: `(0, 0)` is top-left and `(1, 1)` is bottom-right.
Each vanishing point is solved by least-squares intersection of the recorded visible line spans.

## 1. Arcade Capriccio
- Computed VP: `(0.5050, 0.5650)`
- Source image size: `3654 x 2536` pixels
- VP residual mean/max: `0.000000` / `0.000000` normalized image units
- Measurement note: VP solved from aisle edges, column-base receding lines, and floor grid convergence.
- VP source lines, equations, and angles:
  - L1: endpoints `(0.3720, 0.9250) -> (0.4172, 0.8026)`; angle `+61.973 deg`; line `0.938031x + 0.346550y + -0.669507 = 0`; VP residual `0.000000`
  - L2: endpoints `(0.6200, 0.9250) -> (0.5752, 0.7846)`; angle `+114.715 deg`; line `0.952578x + -0.304296y + -0.309125 = 0`; VP residual `0.000000`
  - L3: endpoints `(0.2920, 0.8250) -> (0.3857, 0.7106)`; angle `+40.271 deg`; line `0.773559x + 0.633724y + -0.748701 = 0`; VP residual `0.000000`
  - L4: endpoints `(0.7150, 0.8250) -> (0.6436, 0.7366)`; angle `+139.328 deg`; line `0.777941x + -0.628337y + -0.037850 = 0`; VP residual `0.000000`
  - L5: endpoints `(0.3860, 0.7350) -> (0.4324, 0.6687)`; angle `+44.755 deg`; line `0.819232x + 0.573462y + -0.737718 = 0`; VP residual `0.000000`
  - L6: endpoints `(0.6030, 0.7350) -> (0.5599, 0.6602)`; angle `+129.713 deg`; line `0.866355x + -0.499428y + -0.155332 = 0`; VP residual `0.000000`

## 2. Palace Fantasy
- Computed VP: `(0.5020, 0.5740)`
- Source image size: `1000 x 771` pixels
- VP residual mean/max: `0.000000` / `0.000000` normalized image units
- Measurement note: VP solved from floor-tile diagonals and opposing portico roof edges.
- VP source lines, equations, and angles:
  - L1: endpoints `(0.2200, 0.8750) -> (0.3159, 0.7727)`; angle `+39.453 deg`; line `0.729764x + 0.683699y + -0.758785 = 0`; VP residual `0.000000`
  - L2: endpoints `(0.7850, 0.8750) -> (0.6746, 0.7576)`; angle `+140.647 deg`; line `0.728555x + -0.684987y + 0.027448 = 0`; VP residual `0.000000`
  - L3: endpoints `(0.3450, 0.8900) -> (0.4141, 0.7510)`; angle `+57.202 deg`; line `0.895558x + 0.444945y + -0.704968 = 0`; VP residual `0.000000`
  - L4: endpoints `(0.6500, 0.8900) -> (0.5997, 0.7826)`; angle `+121.277 deg`; line `0.905597x + -0.424140y + -0.211153 = 0`; VP residual `0.000000`
  - L5: endpoints `(0.2800, 0.3000) -> (0.3666, 0.4069)`; angle `-43.579 deg`; line `-0.776981x + 0.629524y + 0.028697 = 0`; VP residual `0.000000`
  - L6: endpoints `(0.7300, 0.3000) -> (0.6297, 0.4206)`; angle `-137.183 deg`; line `-0.768681x + -0.639632y + 0.753027 = 0`; VP residual `0.000000`

## 3. Double Arch Portico
- Computed VP: `(0.5550, 0.6640)`
- Source image size: `6172 x 4720` pixels
- VP residual mean/max: `0.000000` / `0.000000` normalized image units
- Measurement note: VP solved from tiled floor edges and receding arcade roof/base lines visible through the arches.
- VP source lines, equations, and angles:
  - L1: endpoints `(0.2050, 0.8750) -> (0.3240, 0.8033)`; angle `+24.751 deg`; line `0.516294x + 0.856412y + -0.855200 = 0`; VP residual `0.000000`
  - L2: endpoints `(0.8350, 0.8750) -> (0.7258, 0.7927)`; angle `+150.046 deg`; line `0.601824x + -0.798629y + 0.196277 = 0`; VP residual `0.000000`
  - L3: endpoints `(0.3500, 0.8750) -> (0.4402, 0.7822)`; angle `+38.207 deg`; line `0.717231x + 0.696836y + -0.860762 = 0`; VP residual `0.000000`
  - L4: endpoints `(0.7100, 0.8750) -> (0.6573, 0.8033)`; angle `+133.848 deg`; line `0.805919x + -0.592026y + -0.054180 = 0`; VP residual `0.000000`
  - L5: endpoints `(0.2850, 0.4500) -> (0.3903, 0.5335)`; angle `-31.221 deg`; line `-0.621149x + 0.783693y + -0.175634 = 0`; VP residual `0.000000`
  - L6: endpoints `(0.7750, 0.4500) -> (0.6782, 0.5442)`; angle `-143.355 deg`; line `-0.697264x + -0.716814y + 0.862946 = 0`; VP residual `0.000000`

## 4. Perspective Street
- Computed VP: `(0.2440, 0.8150)`
- Source image size: `4000 x 3282` pixels
- VP residual mean/max: `0.000000` / `0.000000` normalized image units
- Measurement note: VP solved from right-facade roof courses, window bands, street edge, and left foreground building edge.
- VP source lines, equations, and angles:
  - L1: endpoints `(0.9650, 0.1850) -> (0.7199, 0.3992)`; angle `-144.362 deg`; line `-0.657987x + -0.753029y + 0.774268 = 0`; VP residual `0.000000`
  - L2: endpoints `(0.9850, 0.8750) -> (0.6960, 0.8516)`; angle `+176.199 deg`; line `0.080708x + -0.996738y + 0.792649 = 0`; VP residual `0.000000`
  - L3: endpoints `(0.8100, 0.3300) -> (0.5610, 0.5434)`; angle `-144.890 deg`; line `-0.650681x + -0.759351y + 0.777637 = 0`; VP residual `0.000000`
  - L4: endpoints `(0.7600, 0.5350) -> (0.5846, 0.6302)`; angle `-156.000 deg`; line `-0.476941x + -0.878935y + 0.832706 = 0`; VP residual `0.000000`
  - L5: endpoints `(0.5600, 0.6250) -> (0.4368, 0.6991)`; angle `-153.741 deg`; line `-0.515293x + -0.857014y + 0.824198 = 0`; VP residual `0.000000`
  - L6: endpoints `(0.0700, 0.9400) -> (0.1466, 0.8850)`; angle `+30.517 deg`; line `0.583444x + 0.812154y + -0.804265 = 0`; VP residual `0.000000`

## 5. Interior Hall
- Computed VP: `(0.3900, 0.7930)`
- Source image size: `3572 x 2877` pixels
- VP residual mean/max: `0.000000` / `0.000000` normalized image units
- Measurement note: VP solved from floor tiles and tunnel wall/ceiling convergence through the central barrel vault.
- VP source lines, equations, and angles:
  - L1: endpoints `(0.1500, 0.9300) -> (0.2316, 0.8834)`; angle `+24.691 deg`; line `0.495749x + 0.868466y + -0.882036 = 0`; VP residual `0.000000`
  - L2: endpoints `(0.9200, 0.9300) -> (0.7133, 0.8766)`; angle `+168.239 deg`; line `0.250265x + -0.968177y + 0.670161 = 0`; VP residual `0.000000`
  - L3: endpoints `(0.3020, 0.9000) -> (0.3407, 0.8529)`; angle `+44.402 deg`; line `0.772347x + 0.635201y + -0.804930 = 0`; VP residual `0.000000`
  - L4: endpoints `(0.5480, 0.9000) -> (0.4943, 0.8636)`; angle `+151.390 deg`; line `0.560732x + -0.827997y + 0.437916 = 0`; VP residual `0.000000`
  - L5: endpoints `(0.3250, 0.6900) -> (0.3503, 0.7302)`; angle `-51.921 deg`; line `-0.845684x + 0.533684y + -0.093395 = 0`; VP residual `0.000000`
  - L6: endpoints `(0.4740, 0.6900) -> (0.4370, 0.7353)`; angle `-135.357 deg`; line `-0.774962x + -0.632008y + 0.803417 = 0`; VP residual `0.000000`
