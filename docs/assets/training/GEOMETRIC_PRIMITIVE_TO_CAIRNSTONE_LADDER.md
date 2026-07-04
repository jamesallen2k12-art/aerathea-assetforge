# Geometric Primitive To Cairnstone Training Ladder

This training lane exists because the Blood Axe A1 cairnstone attempts were not close enough. Stop repairing rejected cairn images here. Build from primitives first, then combine only the approved primitive forms into cairn stones.

## Status

- Current lane: primitive fundamentals
- Current stage: `P01C Perpendicular-To-Y Bisection Board`
- Cairn target images: blocked until primitive stages are approved
- Paint, texture, rope, chips, LODs, FBX, Unreal import: blocked until primitive composition is approved

## Rule

Do not start with the Blood Axe cairn concept image. Start with basic forms, prove the form language, then build upward.

## Stage Ladder

### P01 Basic Primitive Board

Goal: Build clean readable primitives with stable camera and lighting.

Allowed forms:

- Cube
- Rectangular slab
- Slanted parallelepiped
- Hexagonal prism
- Smooth cylinder
- Cone
- Smooth sphere
- Oval egg
- Tetrahedron
- Octa cut
- Icosahedron
- Dodecahedron
- Pentagonal trapezohedron / D10 reference form, matched to `docs/assets/reference/geometric_image_training/REF_AET_GeometricImageTraining_pentagonal_trapezohedron.png`
- Zocchihedron / high-facet rounded form

Approval question: Are the basic shapes readable and clean enough to use as construction pieces?

### P01B Primitive Bisection Board

Goal: Bisect each approved P01 primitive evenly, separate the halves, and expose the cut face so the internal volume and silhouette behavior are readable. Smooth forms use a centered meridian cut. Faceted or asymmetric forms use the most logical symmetry, edge, diagonal, slant, or median path available.

Approval question: Do the cut primitives remain understandable as construction pieces after being split?

### P01C Perpendicular-To-Y Bisection Board

Goal: Bisect each approved P01 primitive with one consistent visual rule: cut across the form at 90 degrees to the requested Y direction, producing upper and lower halves rather than front/back halves. Separate and open the halves so the perpendicular cut faces remain readable.

Approval question: Do the primitives still read correctly when every shape is split perpendicular to the Y direction?

### P02 Primitive Transform Board

Goal: Show the same primitives scaled, rotated, tilted, and overlapped without becoming confusing.

Approval question: Can the primitives be transformed while staying readable?

### P03 Single Stone From Primitives

Goal: Build one simple stone from one slab plus one or two wedge cuts. No texture, no paint.

Approval question: Does a primitive slab start to read as a stone without adding surface detail?

### P04 Three-Stone Stack

Goal: Build a small stack from three approved primitive stones. No cairn concept target yet.

Approval question: Does the stack read as balanced physical mass?

### P05 Simple Cairn Cluster

Goal: Build a five-to-seven mass cairn from approved primitive stones. Still no paint or final concept match.

Approval question: Does the cluster read as a believable cairn silhouette?

### P06 Cairnstone Direction Sheet

Goal: Only after P01-P05 pass, compare primitive cairn compositions against Aerathea cairnstone concepts.

Approval question: Which primitive composition should become the production scaffold?

### P07 Detail Tier One

Goal: Add large chips and broken planes only. No texture or paint.

Approval question: Do the chips improve the form without hiding bad massing?

### P08 Material And Paint Tier

Goal: Add stone material, surface pigment masks, and restrained rope only after the primitive sculpture is approved.

Approval question: Does the material support the form without redefining the silhouette?

## Current P01 Output

- Builder: `Tools/DCC/build_geometric_primitive_fundamentals.py`
- Blender source: `SourceAssets/Blender/Props/Training/GeometricPrimitives/P01_BasicPrimitiveBoard/P01_BasicPrimitiveBoard.blend`
- Review image: `docs/assets/training/geometric_primitives/P01_BasicPrimitiveBoard.png`
- Source reference sheet: `docs/assets/reference/geometric_image_training/REF_AET_GeometricImageTraining_Primitives_A01.png`

## Current P01C Output

- Builder: `Tools/DCC/build_geometric_primitive_y_axis_bisections.py`
- Blender source: `SourceAssets/Blender/Props/Training/GeometricPrimitives/P01C_YAxis90BisectionBoard/P01C_YAxis90BisectionBoard.blend`
- Review image: `docs/assets/training/geometric_primitives/P01C_YAxis90BisectionBoard.png`

## Recommended Next Step

Review `P01C_YAxis90BisectionBoard.png`. If the perpendicular-to-Y bisections are approved, continue to `P02 Primitive Transform Board`. If not, fix the split presentation before any cairn work resumes.
