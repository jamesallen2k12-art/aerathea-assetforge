#!/usr/bin/env python3
"""Build the A05 Ogre review revision of the Aerathea race scale chart."""

from __future__ import annotations

import build_race_size_chart as chart


OUT_REVIEW_SVG = chart.ROOT / "docs/assets/reference/AET_Race_Size_Comparison_A05_OgreReview.svg"


def main() -> None:
    chart.WIDTH = 4550
    chart.ENTRIES = [
        *chart.ENTRIES,
        chart.RaceEntry(
            "Ogre (F)",
            "10'-10'6\"",
            chart.inches(10),
            chart.inches(10, 6),
            "#75624d",
            "#d06a2c",
            1.42,
            "ogre",
        ),
        chart.RaceEntry(
            "Ogre (M)",
            "10'4\"-11'",
            chart.inches(10, 4),
            chart.inches(11),
            "#665540",
            "#d06a2c",
            1.62,
            "ogre",
        ),
    ]

    OUT_REVIEW_SVG.parent.mkdir(parents=True, exist_ok=True)
    OUT_REVIEW_SVG.write_text(
        chart.build_svg(
            "RACE SIZE REVIEW CHART A05",
            "Ogre review revision generated after A04 approval. Ogres sit above Minotaurs and Anubisath/Sutekh, below Giants.",
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
