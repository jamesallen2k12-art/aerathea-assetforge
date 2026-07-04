# Perspective and Rendering Math Research Notes

Purpose: record the formulas and principles being applied to the Aerathea perspective redraw training boards.

## Sources Checked

- Wolfram MathWorld, Homogeneous Coordinates: https://mathworld.wolfram.com/HomogeneousCoordinates.html
- Wolfram MathWorld, Projective Geometry: https://mathworld.wolfram.com/ProjectiveGeometry.html
- Wolfram Language documentation, ImageLines: https://reference.wolfram.com/language/ref/ImageLines.html
- Canny, J. "A Computational Approach to Edge Detection", IEEE TPAMI, 1986: https://doi.org/10.1109/TPAMI.1986.4767851
- Duda, R. O. and Hart, P. E. "Use of the Hough Transformation to Detect Lines and Curves in Pictures", Communications of the ACM, 1972: https://doi.org/10.1145/361237.361242
- Grompone von Gioi et al., "LSD: a Line Segment Detector", IPOL, 2012: https://www.ipol.im/pub/art/2012/gjmr-lsd/
- Wing, J. M. "Computational Thinking", Communications of the ACM, 2006: https://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf
- Mildenhall et al., "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis", ECCV 2020: https://arxiv.org/abs/2003.08934
- Kerbl et al., "3D Gaussian Splatting for Real-Time Radiance Field Rendering", ACM TOG 2023: https://arxiv.org/abs/2308.04079
- Zeng, Cai, Zhao, "A Survey on Physics-based Differentiable Rendering", 2025: https://arxiv.org/abs/2504.01402

## Applied Formulas

### Homogeneous line representation

For image coordinates `(x, y)`, a 2D line is stored as:

```text
l = (a, b, c)
ax + by + c = 0
```

The line through two points `p1 = (x1, y1, 1)` and `p2 = (x2, y2, 1)` is:

```text
l = p1 x p2
```

The intersection of two lines is:

```text
v = l1 x l2
```

The Cartesian point is recovered by:

```text
(x, y) = (v_x / v_z, v_y / v_z)
```

### Hough normal form

Straight lines are detected using Duda-Hart normal form:

```text
rho = x cos(theta) + y sin(theta)
```

Pixels vote in `(rho, theta)` accumulator space. The new P08 pass restricts each edge pixel to theta values close to its gradient-normal direction instead of letting every edge vote for every possible line.

### Canny-style edge principles

The edge pass uses:

```text
Gx = Sobel_x(I)
Gy = Sobel_y(I)
|G| = sqrt(Gx^2 + Gy^2)
theta = atan2(Gy, Gx)
```

Then it applies non-maximum suppression along the gradient direction and keeps only high-confidence edge points.

### Weighted vanishing-point solve

For selected line candidates `li = (ai, bi, ci)`, solve:

```text
min_v sum_i wi * (ai vx + bi vy + ci)^2
```

The normal equations are:

```text
[sum wi ai^2   sum wi ai bi] [vx] = [-sum wi ai ci]
[sum wi ai bi  sum wi bi^2] [vy]   [-sum wi bi ci]
```

Line weight is based on Hough votes, support-pixel count, and detected span length. Residuals are retained so weak or false perspective lines can be rejected instead of silently accepted.

### Computational thinking rule applied

The task is decomposed into reproducible stages:

1. Normalize/crop the source.
2. Detect edge evidence.
3. Convert pixels to line hypotheses.
4. Validate spans with support pixels.
5. Solve perspective geometry.
6. Redraw from measured primitives.
7. Report equations, angles, residuals, and confidence.

## Rendering AI Lesson Applied

NeRF, Gaussian Splatting, and differentiable rendering all reinforce the same production principle: use a forward model, compare against observed evidence, and optimize parameters with a measurable loss. For these 2D training boards the equivalent is:

```text
source evidence -> measured primitives -> rendered redraw -> residual/error report
```

Do not "invent" clean geometry without tying it back to measured source evidence.
