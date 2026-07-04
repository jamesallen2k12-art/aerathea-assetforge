# Geometric Shape Formula Registry

This registry locks the geometric training lane to formula-defined construction.
Retired ambiguous labels such as `Zocchihedron`, `Oval Egg`, `Octa Cut`, and
`Stellated Icosa Form` must not be used as exact shape names.

## Exactness Rule

- No board shape may be hand drawn, sculpted by eye, or renamed from a vague temporary form.
- For polyhedra, the listed vertices, faces, edge rules, and dimensions are authoritative.
- For continuous surfaces and curves, the analytic equation is authoritative, and the board mesh must use the locked segment/ring/control-point counts listed below.
- Any later Cairn Stone construction pass must cite the exact source formula before changing proportions.

## Exact Primitive Board Shapes

### Cube

- Status: exact polyhedron.
- Dimension rule: side length `s = 1.9`.
- Vertices: `(±s/2, ±s/2, ±s/2)`.
- Faces: 6 squares.

### Rectangular Slab

- Status: exact cuboid.
- Dimensions: `width = 3.0`, `depth = 1.15`, `height = 1.15`.
- Vertices: `(±width/2, ±depth/2, ±height/2)`.
- Faces: 6 rectangles.

### Parallelepiped

- Status: exact sheared hexahedron.
- Dimensions: `width = 2.35`, `depth = 1.35`, `height = 2.25`.
- Shear: `shear_x = 0.55`, `shear_y = 0.15`.
- Bottom vertices: `(±width/2, ±depth/2, -height/2)`.
- Top vertices: `(x + shear_x, y + shear_y, height/2)` for each bottom corner `(x, y)`.

### Hexagonal Prism

- Status: exact regular hexagonal prism mesh.
- Parameters: `radius = 1.02`, `depth = 2.15`, `sides = 6`, rotation `30 degrees`.
- Ring vertices: `(r cos(2πk/6 + π/6), r sin(2πk/6 + π/6), ±depth/2)`.

### Cylinder

- Status: exact analytic cylinder; board mesh uses 96 locked radial segments.
- Parameters: `radius = 0.92`, `height = 2.2`, `segments = 96`.
- Equation: `x^2 + y^2 = radius^2`, `-height/2 <= z <= height/2`.

### D100 50-Gonal Trapezohedron

- Status: exact 100-face trapezohedron.
- Parameters: `n = 50`, `radius = 1.04`, `ring_z = 0.20`, `pole_z = 1.18`.
- Vertices:
  - Top pole: `(0, 0, pole_z)`.
  - Bottom pole: `(0, 0, -pole_z)`.
  - Upper ring: `(r cos(2πk/n + θ), r sin(2πk/n + θ), ring_z)`.
  - Lower ring: `(r cos(2π(k+0.5)/n + θ), r sin(2π(k+0.5)/n + θ), -ring_z)`.
- Faces per `k`: `(top, upper_k, lower_k, upper_{k+1})` and `(bottom, lower_{k+1}, upper_{k+1}, lower_k)`.

### Tetrahedron

- Status: exact regular tetrahedron.
- Parameter: `edge_length = 2.25`.
- Base radius: `edge_length / sqrt(3)`.
- Height: `sqrt(2/3) * edge_length`.
- Vertices: three base vertices at angles `90`, `210`, `330` degrees and one apex.

### Regular Octahedron

- Status: exact regular octahedron.
- Parameter: circumradius `r = 1.18`.
- Vertices: `(±r, 0, 0)`, `(0, ±r, 0)`, `(0, 0, ±r)`.
- Faces: 8 equilateral triangles.

### Icosahedron

- Status: exact regular icosahedron.
- Uses golden ratio `φ = (1 + sqrt(5)) / 2`.
- Raw vertices: permutations of `(0, ±1, ±φ)`, `(±1, ±φ, 0)`, `(±φ, 0, ±1)`, normalized to radius `1.22`.
- Faces: 20 equilateral triangles.

### Dodecahedron

- Status: exact regular dodecahedron.
- Construction: dual of the exact icosahedron.
- Vertices: normalized centers of each icosahedron face, scaled to radius `1.16`.
- Faces: 12 pentagons from ordered adjacent icosahedron face centers.

### D10 Pentagonal Trapezohedron

- Status: exact 10-face pentagonal trapezohedron.
- Parameters: `n = 5`, `radius = 1.06`, `ring_z = 0.30`, `pole_z = 1.36`, `θ = 18 degrees`.
- Uses the same trapezohedron formula as the D100 with `n = 5`.

### Cone

- Status: exact analytic cone; board mesh uses 64 locked radial segments.
- Parameters: `base_radius = 1.05`, `top_radius = 0`, `height = 2.25`, `segments = 64`.
- Equation: `sqrt(x^2 + y^2) = base_radius * (height/2 - z) / height`.

### Smooth Sphere

- Status: exact analytic sphere; board mesh uses 64 locked longitude segments and 32 locked rings.
- Parameter: `radius = 1.08`.
- Equation: `x^2 + y^2 + z^2 = radius^2`.

### Prolate Spheroid

- Status: exact analytic spheroid; board mesh uses 64 locked longitude segments and 32 locked rings.
- Parameters: `a = 0.78`, `b = 0.78`, `c = 1.34`.
- Equation: `x^2/a^2 + y^2/b^2 + z^2/c^2 = 1`.

## Exact Complex Board Shapes

### Truncated Icosahedron

- Status: exact truncation of a regular icosahedron.
- Rule: each directed edge is cut at `1/3` from its source vertex.
- Face result: 12 pentagons and 20 hexagons.

### Truncated Dodecahedron

- Status: exact truncation of a regular dodecahedron.
- Rule: each directed edge is cut at `0.30` from its source vertex.
- Face result: original dodecahedral faces plus vertex-truncation faces.

### Rhombicuboctahedron

- Status: exact coordinate convex hull.
- Coordinates: all signed permutations of `(1, 1, 1 + sqrt(2))`.

### Truncated Cuboctahedron

- Status: exact coordinate convex hull.
- Coordinates: all signed permutations of `(1, 1 + sqrt(2), 1 + 2sqrt(2))`.

### Exact Icosahedral Stellation

- Status: exact face stellation of a regular icosahedron.
- Rule: each icosahedron face receives one apex on the normalized face-center direction.
- Apex radius: `1.5` times the icosahedron circumradius used in construction.
- Faces: three triangles per original icosahedron face, 60 total triangles.

### Geodesic Icosphere

- Status: exact subdivided icosahedral mesh.
- Rule: start with a regular icosahedron, subdivide triangular faces three times, normalize vertices to the sphere radius.

### Torus

- Status: exact analytic torus; board mesh uses 96 locked major segments and 24 locked minor segments.
- Parameters: major radius `R = 0.82`, minor radius `r = 0.22`.
- Equation: `(R + r cos v) cos u, (R + r cos v) sin u, r sin v`.

### Mobius Strip

- Status: exact parametric surface; board mesh uses 128 locked U segments and 14 locked V segments.
- Parameters: center radius `R = 1.05`, half width `w = 0.34`.
- Equation: `((R + v cos(u/2)) cos u, (R + v cos(u/2)) sin u, v sin(u/2))`.

### Klein Bottle

- Status: exact parametric immersion; board mesh uses 96 locked U segments and 36 locked V segments.
- Rule: piecewise standard Klein bottle immersion over `u, v in [0, 2π)`.

### Trefoil Knot

- Status: exact parametric knot curve; board curve uses 220 locked points and bevel depth `0.055`.
- Equation: `x = sin t + 2 sin 2t`, `y = cos t - 2 cos 2t`, `z = -sin 3t`.

### Helix Tube

- Status: exact parametric helix; board curve uses 220 locked points and bevel depth `0.06`.
- Parameters: `turns = 3.3`, radius `0.78`, height `2.1`.
- Equation: `(r cos t, r sin t, z(t))`.

### Helicoid Surface

- Status: exact ruled surface; board mesh uses 96 locked turn segments and 18 locked radial segments.
- Parameters: `turns = 2.3`, radial interval `[0.16, 1.10]`, height `1.9`.
- Equation: `(r cos v, r sin v, z(v))`.

## Exact Tesseract Board Shape

### Tesseract Projection

- Status: exact 4D hypercube graph projected into 3D.
- 4D vertices: `(±1, ±1, ±1, ±1)`, 16 total.
- Edges: pairs of vertices differing in exactly one coordinate, 32 total.
- Projection:
  - Classic: outer and inner cube projection based on W coordinate.
  - Rotated: 4D rotations in coordinate planes followed by perspective projection.
- W-dimension connector edges are marked blue.
