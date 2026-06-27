"""Shared Aerathea startup review marker definitions.

The DCC proof renderer and Unreal runtime-review prep import this file so the
debug alignment markers cannot drift between tools.
"""

REVIEW_MARKER_TAG = "AET_REVIEW_MARKER"

# Corners are ordered clockwise from a top-down Unreal +Z view.  The E point is
# deliberately above the floor plane so it proves the up vector and catches
# mirrored/underside captures.
REVIEW_ALIGNMENT_MARKERS = [
    {
        "id": "A",
        "label": "A",
        "location": (-1000.0, -1000.0, 70.0),
        "color": (1.0, 0.05, 0.04, 1.0),
    },
    {
        "id": "B",
        "label": "B",
        "location": (1000.0, -1000.0, 70.0),
        "color": (0.05, 0.9, 0.15, 1.0),
    },
    {
        "id": "C",
        "label": "C",
        "location": (1000.0, 1000.0, 70.0),
        "color": (0.1, 0.25, 1.0, 1.0),
    },
    {
        "id": "D",
        "label": "D",
        "location": (-1000.0, 1000.0, 70.0),
        "color": (1.0, 0.88, 0.05, 1.0),
    },
    {
        "id": "E",
        "label": "E",
        "location": (-70.0, 160.0, 540.0),
        "color": (1.0, 0.1, 1.0, 1.0),
    },
]
