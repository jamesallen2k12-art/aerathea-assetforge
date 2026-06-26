#!/usr/bin/env python3
"""Build a deterministic Aerathea race scale reference chart.

This chart is intentionally geometric: concept-art lineups are useful for mood,
but this one is the scale authority. Heights are drawn from feet/inches ranges
so body package, collision, door, stair, and gear work can check actual scale.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT_REVIEW_SVG = ROOT / "docs/assets/reference/AET_Race_Size_Comparison_A04_Review.svg"
OUT_APPROVED_SVG = ROOT / "docs/assets/reference/AET_Race_Size_Comparison_A04.svg"

WIDTH = 4200
HEIGHT = 1480
BASELINE_Y = 1120
TOP_Y = 120
PX_PER_FOOT = (BASELINE_Y - TOP_Y) / 16.0


def inches(feet: int, extra: int = 0) -> int:
    return feet * 12 + extra


@dataclass(frozen=True)
class RaceEntry:
    label: str
    range_label: str
    min_inches: int
    max_inches: int
    color: str
    accent: str
    mass: float
    kind: str = "humanoid"

    @property
    def midpoint_inches(self) -> float:
        return (self.min_inches + self.max_inches) / 2.0


ENTRIES = [
    RaceEntry("Gnome (F)", "3'-3'6\"", inches(3), inches(3, 6), "#9a6a26", "#2e5b7c", 0.66, "gnome"),
    RaceEntry("Gnome (M)", "3'4\"-4'", inches(3, 4), inches(4), "#9a6a26", "#2e5b7c", 0.72, "gnome"),
    RaceEntry("Drakhar (F)", "3'6\"-4'2\"", inches(3, 6), inches(4, 2), "#8e8a3a", "#d17a36", 0.74, "lizard"),
    RaceEntry("Drakhar (M)", "4'-4'6\"", inches(4), inches(4, 6), "#8e8a3a", "#d17a36", 0.8, "lizard"),
    RaceEntry("Dwarf (F)", "4'2\"-4'6\"", inches(4, 2), inches(4, 6), "#8a6f55", "#b28b38", 0.95, "dwarf"),
    RaceEntry("Dwarf (M)", "4'4\"-5'", inches(4, 4), inches(5), "#6d5d4f", "#c28b3c", 1.05, "dwarf"),
    RaceEntry("Elf (F)", "5'2\"-5'8\"", inches(5, 2), inches(5, 8), "#d8d6cd", "#87a6c8", 0.72, "elf"),
    RaceEntry("Elf (M)", "5'8\"-6'", inches(5, 8), inches(6), "#c5ced0", "#7ea3c8", 0.78, "elf"),
    RaceEntry("Dark Elf (F)", "5'2\"-5'8\"", inches(5, 2), inches(5, 8), "#4f465e", "#8c62bf", 0.72, "elf"),
    RaceEntry("Dark Elf (M)", "5'8\"-6'", inches(5, 8), inches(6), "#40394e", "#9a72cc", 0.78, "elf"),
    RaceEntry("Orc (F)", "6'2\"-6'8\"", inches(6, 2), inches(6, 8), "#6c7e3d", "#8d4a2e", 1.02, "orc"),
    RaceEntry("Orc (M)", "6'6\"-7'", inches(6, 6), inches(7), "#617136", "#8d4a2e", 1.12, "orc"),
    RaceEntry("Basari (F)", "6-7'", inches(6), inches(7), "#b78d3c", "#f1dc93", 0.82, "anubian"),
    RaceEntry("Basari (M)", "7-8'", inches(7), inches(8), "#a77d35", "#f1dc93", 0.92, "anubian"),
    RaceEntry("Valar (F)", "6'6\"-7'", inches(6, 6), inches(7), "#d9dde3", "#d6bd6a", 0.78, "valar"),
    RaceEntry("Valar (M)", "6'10\"-7'4\"", inches(6, 10), inches(7, 4), "#d6d7dc", "#d6bd6a", 0.88, "valar"),
    RaceEntry("Minotaur (F)", "7'-8'", inches(7), inches(8), "#8b6040", "#c08a45", 1.18, "minotaur"),
    RaceEntry("Minotaur (M)", "8-9'", inches(8), inches(9), "#7b5134", "#bd8540", 1.38, "minotaur"),
    RaceEntry("Anubisath (F)", "7'6\"-8'", inches(7, 6), inches(8), "#25272d", "#d2a94b", 0.92, "anubian"),
    RaceEntry("Anubisath (M)", "7'10\"-8'4\"", inches(7, 10), inches(8, 4), "#24262c", "#d2a94b", 1.03, "anubian"),
    RaceEntry("Giant (F)", "14'-15'", inches(14), inches(15), "#7890a3", "#d5c1a0", 1.48, "giant"),
    RaceEntry("Giant (M)", "14'10\"-16'", inches(14, 10), inches(16), "#6c8194", "#d5c1a0", 1.78, "giant"),
]


def race_name(entry: RaceEntry) -> str:
    return entry.label.rsplit(" ", 1)[0]


def sex_order(entry: RaceEntry) -> int:
    return 0 if "(F)" in entry.label else 1


def sorted_by_race_scale(entries: list[RaceEntry]) -> list[RaceEntry]:
    groups: dict[str, list[RaceEntry]] = {}
    race_order: dict[str, int] = {}
    for entry in entries:
        race = race_name(entry)
        race_order.setdefault(race, len(race_order))
        groups.setdefault(race, []).append(entry)

    def group_sort_key(item: tuple[str, list[RaceEntry]]) -> tuple[float, float, int]:
        race, race_entries = item
        average_midpoint = sum(entry.midpoint_inches for entry in race_entries) / len(race_entries)
        lowest_minimum = min(entry.min_inches for entry in race_entries)
        return average_midpoint, lowest_minimum, race_order[race]

    ordered: list[RaceEntry] = []
    for _, race_entries in sorted(groups.items(), key=group_sort_key):
        ordered.extend(sorted(race_entries, key=sex_order))
    return ordered


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def label_svg(text: str, x: float, y: float, size: int = 22) -> str:
    if len(text) <= 12:
        return f'<text x="{x}" y="{y}" font-size="{size}" font-family="serif" text-anchor="middle" fill="#211d18">{esc(text)}</text>'

    if "(" in text:
        first, second = text.split("(", 1)
        lines = [first.strip(), "(" + second]
    elif " " in text:
        first, second = text.split(" ", 1)
        lines = [first.strip(), second.strip()]
    else:
        lines = [text]

    tspans = []
    for index, line in enumerate(lines):
        dy = 0 if index == 0 else size * 1.05
        tspans.append(f'<tspan x="{x}" dy="{dy}">{esc(line)}</tspan>')
    return f'<text x="{x}" y="{y}" font-size="{size}" font-family="serif" text-anchor="middle" fill="#211d18">{"".join(tspans)}</text>'


def y_for_inches(value: float) -> float:
    return BASELINE_Y - (value / 12.0) * PX_PER_FOOT


def figure_width(entry: RaceEntry) -> float:
    return 36.0 * entry.mass


def draw_humanoid(entry: RaceEntry, x: float) -> str:
    h = (entry.max_inches / 12.0) * PX_PER_FOOT
    top = BASELINE_Y - h
    w = figure_width(entry)
    cx = x
    head_r = max(11.0, min(27.0, h * 0.055))
    head_cy = top + head_r
    shoulder_y = top + h * 0.23
    hip_y = top + h * 0.63
    foot_y = BASELINE_Y
    torso_w = w * 0.78
    hip_w = w * 0.54

    ears = ""
    if entry.kind == "gnome":
        ears = (
            f'<polygon points="{cx-head_r*0.72},{head_cy-head_r*0.1} {cx-head_r*1.2},{head_cy+head_r*0.08} {cx-head_r*0.72},{head_cy+head_r*0.28}" fill="{entry.color}" stroke="#3a3128" stroke-width="2"/>'
            f'<polygon points="{cx+head_r*0.72},{head_cy-head_r*0.1} {cx+head_r*1.2},{head_cy+head_r*0.08} {cx+head_r*0.72},{head_cy+head_r*0.28}" fill="{entry.color}" stroke="#3a3128" stroke-width="2"/>'
        )
    elif entry.kind == "elf":
        ears = (
            f'<polygon points="{cx-head_r*0.85},{head_cy-head_r*0.2} {cx-head_r*1.65},{head_cy} {cx-head_r*0.82},{head_cy+head_r*0.2}" fill="{entry.color}" stroke="#3a3128" stroke-width="2"/>'
            f'<polygon points="{cx+head_r*0.85},{head_cy-head_r*0.2} {cx+head_r*1.65},{head_cy} {cx+head_r*0.82},{head_cy+head_r*0.2}" fill="{entry.color}" stroke="#3a3128" stroke-width="2"/>'
        )

    beard = ""
    if entry.kind == "dwarf" and "(M)" in entry.label:
        beard = f'<path d="M {cx-head_r*0.6} {head_cy+head_r*0.55} Q {cx} {head_cy+head_r*2.2} {cx+head_r*0.6} {head_cy+head_r*0.55}" fill="#9f5d2d" opacity="0.9"/>'

    tail = ""
    if entry.kind == "lizard":
        tail = f'<path d="M {cx+hip_w*0.5} {hip_y+18} C {cx+w*1.0} {hip_y+35}, {cx+w*0.75} {foot_y-35}, {cx+w*1.25} {foot_y-25}" fill="none" stroke="{entry.color}" stroke-width="10" stroke-linecap="round"/>'

    return f"""
    <g class="figure">
      {tail}
      {ears}
      <ellipse cx="{cx}" cy="{head_cy}" rx="{head_r*0.82}" ry="{head_r}" fill="{entry.color}" stroke="#302820" stroke-width="2"/>
      {beard}
      <path d="M {cx-torso_w/2} {shoulder_y} L {cx+torso_w/2} {shoulder_y} L {cx+hip_w/2} {hip_y} L {cx-hip_w/2} {hip_y} Z" fill="{entry.color}" stroke="#302820" stroke-width="2"/>
      <path d="M {cx-torso_w/2} {shoulder_y+8} L {cx-w*0.78} {hip_y-10}" stroke="{entry.color}" stroke-width="{max(8,w*0.18)}" stroke-linecap="round"/>
      <path d="M {cx+torso_w/2} {shoulder_y+8} L {cx+w*0.78} {hip_y-10}" stroke="{entry.color}" stroke-width="{max(8,w*0.18)}" stroke-linecap="round"/>
      <path d="M {cx-hip_w/3} {hip_y} L {cx-w*0.35} {foot_y-8}" stroke="{entry.color}" stroke-width="{max(10,w*0.2)}" stroke-linecap="round"/>
      <path d="M {cx+hip_w/3} {hip_y} L {cx+w*0.35} {foot_y-8}" stroke="{entry.color}" stroke-width="{max(10,w*0.2)}" stroke-linecap="round"/>
      <path d="M {cx-torso_w*0.4} {shoulder_y+20} L {cx+torso_w*0.38} {hip_y-16}" stroke="{entry.accent}" stroke-width="5" opacity="0.75"/>
      <ellipse cx="{cx-w*0.35}" cy="{foot_y-6}" rx="{max(9,w*0.22)}" ry="6" fill="#2c241f"/>
      <ellipse cx="{cx+w*0.35}" cy="{foot_y-6}" rx="{max(9,w*0.22)}" ry="6" fill="#2c241f"/>
    </g>
    """


def draw_minotaur(entry: RaceEntry, x: float) -> str:
    h = (entry.max_inches / 12.0) * PX_PER_FOOT
    top = BASELINE_Y - h
    w = figure_width(entry)
    cx = x
    horn_y = top + 18.0
    head_cy = top + max(34.0, h * 0.11)
    shoulder_y = top + h * 0.18
    hip_y = top + h * 0.58
    head_w = w * 0.56
    body_w = w * 0.94

    return f"""
    <g class="figure">
      <path d="M {cx-head_w*0.35} {horn_y+28} C {cx-head_w*1.25} {horn_y+8}, {cx-head_w*1.2} {horn_y-18}, {cx-head_w*0.48} {horn_y+2}" fill="none" stroke="#d7c08e" stroke-width="9" stroke-linecap="round"/>
      <path d="M {cx+head_w*0.35} {horn_y+28} C {cx+head_w*1.25} {horn_y+8}, {cx+head_w*1.2} {horn_y-18}, {cx+head_w*0.48} {horn_y+2}" fill="none" stroke="#d7c08e" stroke-width="9" stroke-linecap="round"/>
      <ellipse cx="{cx}" cy="{head_cy}" rx="{head_w*0.42}" ry="{head_w*0.5}" fill="{entry.color}" stroke="#302820" stroke-width="2"/>
      <line x1="{cx}" y1="{head_cy+head_w*0.35}" x2="{cx}" y2="{shoulder_y+8}" stroke="{entry.color}" stroke-width="{w*0.24}" stroke-linecap="round"/>
      <path d="M {cx-body_w/2} {shoulder_y} L {cx+body_w/2} {shoulder_y} L {cx+w*0.34} {hip_y} L {cx-w*0.34} {hip_y} Z" fill="{entry.color}" stroke="#302820" stroke-width="2"/>
      <path d="M {cx-body_w/2} {shoulder_y+10} L {cx-w*0.75} {hip_y-8}" stroke="{entry.color}" stroke-width="{w*0.18}" stroke-linecap="round"/>
      <path d="M {cx+body_w/2} {shoulder_y+10} L {cx+w*0.75} {hip_y-8}" stroke="{entry.color}" stroke-width="{w*0.18}" stroke-linecap="round"/>
      <path d="M {cx-w*0.22} {hip_y} L {cx-w*0.34} {BASELINE_Y-10}" stroke="{entry.color}" stroke-width="{w*0.21}" stroke-linecap="round"/>
      <path d="M {cx+w*0.22} {hip_y} L {cx+w*0.34} {BASELINE_Y-10}" stroke="{entry.color}" stroke-width="{w*0.21}" stroke-linecap="round"/>
      <path d="M {cx-body_w*0.35} {shoulder_y+16} L {cx+body_w*0.35} {hip_y-18}" stroke="{entry.accent}" stroke-width="6" opacity="0.75"/>
      <ellipse cx="{cx-w*0.36}" cy="{BASELINE_Y-7}" rx="{w*0.26}" ry="7" fill="#2c241f"/>
      <ellipse cx="{cx+w*0.36}" cy="{BASELINE_Y-7}" rx="{w*0.26}" ry="7" fill="#2c241f"/>
    </g>
    """


def draw_figure(entry: RaceEntry, x: float) -> str:
    if entry.kind == "minotaur":
        return draw_minotaur(entry, x)
    return draw_humanoid(entry, x)


def draw_range(entry: RaceEntry, x: float) -> str:
    y_min = y_for_inches(entry.min_inches)
    y_max = y_for_inches(entry.max_inches)
    line_x = x + figure_width(entry) * 0.62
    return f"""
    <g class="range">
      <line x1="{line_x}" y1="{y_max}" x2="{line_x}" y2="{y_min}" stroke="#2d2924" stroke-width="2"/>
      <line x1="{line_x-10}" y1="{y_max}" x2="{line_x+10}" y2="{y_max}" stroke="#2d2924" stroke-width="2"/>
      <line x1="{line_x-10}" y1="{y_min}" x2="{line_x+10}" y2="{y_min}" stroke="#2d2924" stroke-width="2"/>
      <text x="{x}" y="{y_max-18}" font-size="24" font-family="serif" text-anchor="middle" fill="#211d18">{esc(entry.range_label)}</text>
    </g>
    """


def draw_badge(entry: RaceEntry, x: float, y: float) -> str:
    icon = entry.label.split(" ", 1)[0].lower()
    if entry.label.startswith("Dark Elf"):
        icon = "dark_elf"
    elif entry.label.startswith("Anubisath"):
        icon = "anubisath"

    base = [
        f'<circle cx="{x}" cy="{y}" r="28" fill="{entry.color}" stroke="#3b332b" stroke-width="3"/>',
    ]

    if icon == "gnome":
        base.append(f'<circle cx="{x}" cy="{y}" r="13" fill="none" stroke="{entry.accent}" stroke-width="5"/>')
        for angle in range(0, 360, 60):
            base.append(f'<line x1="{x}" y1="{y-24}" x2="{x}" y2="{y-15}" stroke="{entry.accent}" stroke-width="4" transform="rotate({angle} {x} {y})"/>')
    elif icon == "dwarf":
        base.append(f'<path d="M {x-18} {y+12} L {x} {y-16} L {x+18} {y+12} Z" fill="none" stroke="{entry.accent}" stroke-width="5"/>')
        base.append(f'<path d="M {x-24} {y+14} L {x+24} {y+14}" stroke="{entry.accent}" stroke-width="4"/>')
    elif icon == "drakhar":
        base.append(f'<ellipse cx="{x}" cy="{y}" rx="20" ry="12" fill="none" stroke="{entry.accent}" stroke-width="5"/>')
        base.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{entry.accent}"/>')
    elif icon == "elf":
        base.append(f'<path d="M {x-5} {y+16} C {x-24} {y-4}, {x-6} {y-22}, {x+15} {y-18} C {x+13} {y+2}, {x+6} {y+12}, {x-5} {y+16} Z" fill="none" stroke="{entry.accent}" stroke-width="5"/>')
    elif icon == "dark_elf":
        base.append(f'<circle cx="{x+4}" cy="{y}" r="17" fill="{entry.accent}" opacity="0.95"/>')
        base.append(f'<circle cx="{x+12}" cy="{y-2}" r="17" fill="{entry.color}"/>')
    elif icon == "orc":
        base.append(f'<path d="M {x-16} {y-4} Q {x} {y-18} {x+16} {y-4} L {x+10} {y+16} L {x-10} {y+16} Z" fill="none" stroke="{entry.accent}" stroke-width="5"/>')
    elif icon == "basari":
        base.append(f'<circle cx="{x}" cy="{y}" r="10" fill="{entry.accent}"/>')
        for angle in range(0, 360, 45):
            base.append(f'<line x1="{x}" y1="{y-24}" x2="{x}" y2="{y-15}" stroke="{entry.accent}" stroke-width="4" transform="rotate({angle} {x} {y})"/>')
    elif icon == "valar":
        points = [
            (x, y - 22),
            (x + 6, y - 6),
            (x + 22, y),
            (x + 6, y + 6),
            (x, y + 22),
            (x - 6, y + 6),
            (x - 22, y),
            (x - 6, y - 6),
        ]
        base.append('<polygon points="{}" fill="none" stroke="{}" stroke-width="5"/>'.format(
            " ".join(f"{px},{py}" for px, py in points),
            entry.accent,
        ))
    elif icon == "minotaur":
        base.append(f'<path d="M {x-5} {y+12} C {x-28} {y-2}, {x-25} {y-22}, {x-5} {y-8}" fill="none" stroke="{entry.accent}" stroke-width="6" stroke-linecap="round"/>')
        base.append(f'<path d="M {x+5} {y+12} C {x+28} {y-2}, {x+25} {y-22}, {x+5} {y-8}" fill="none" stroke="{entry.accent}" stroke-width="6" stroke-linecap="round"/>')
    elif icon == "anubisath":
        base.append(f'<path d="M {x-14} {y+15} L {x} {y-20} L {x+14} {y+15} Z" fill="none" stroke="{entry.accent}" stroke-width="5"/>')
        base.append(f'<path d="M {x-18} {y-8} L {x-5} {y-20} M {x+18} {y-8} L {x+5} {y-20}" stroke="{entry.accent}" stroke-width="5"/>')
    elif icon == "giant":
        base.append(f'<path d="M {x-24} {y+16} L {x-8} {y-10} L {x} {y+2} L {x+10} {y-18} L {x+24} {y+16} Z" fill="none" stroke="{entry.accent}" stroke-width="5"/>')

    return f'<g class="badge">{"".join(base)}</g>'


def build_svg(subtitle: str, footer: str) -> str:
    entries = sorted_by_race_scale(ENTRIES)
    margin_left = 135
    spacing = (WIDTH - margin_left - 180) / (len(entries) - 1)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        '<rect width="100%" height="100%" fill="#d8d0c0"/>',
        '<rect x="0" y="0" width="100%" height="100%" fill="#f2eadb" opacity="0.45"/>',
        f'<text x="{WIDTH/2}" y="72" font-size="62" font-family="serif" letter-spacing="12" text-anchor="middle" fill="#251f18">AERATHEA</text>',
        f'<text x="{WIDTH/2}" y="124" font-size="34" font-family="serif" letter-spacing="10" text-anchor="middle" fill="#251f18">{esc(subtitle)}</text>',
        '<text x="30" y="105" font-size="20" font-family="serif" fill="#211d18">HEIGHT (FT)</text>',
    ]

    for foot in range(0, 17):
        y = BASELINE_Y - foot * PX_PER_FOOT
        parts.append(f'<line x1="88" y1="{y:.2f}" x2="{WIDTH-40}" y2="{y:.2f}" stroke="#857c70" stroke-width="1" stroke-dasharray="8 8" opacity="0.55"/>')
        parts.append(f'<text x="70" y="{y+8:.2f}" font-size="24" font-family="serif" text-anchor="end" fill="#211d18">{foot}</text>')
    parts.append(f'<line x1="88" y1="{BASELINE_Y}" x2="{WIDTH-40}" y2="{BASELINE_Y}" stroke="#2b251f" stroke-width="3"/>')
    parts.append(f'<line x1="88" y1="{TOP_Y}" x2="88" y2="{BASELINE_Y}" stroke="#2b251f" stroke-width="3"/>')

    for index, entry in enumerate(entries):
        x = margin_left + index * spacing
        parts.append(draw_range(entry, x))
        parts.append(draw_figure(entry, x))
        parts.append(label_svg(entry.label, x, BASELINE_Y + 62))
        parts.append(draw_badge(entry, x, BASELINE_Y + 132))
    parts.append(f'<text x="{WIDTH/2}" y="1430" font-size="22" font-family="serif" text-anchor="middle" fill="#473f34">{esc(footer)}</text>')
    parts.append("</svg>")
    return "\n".join(line.rstrip() for part in parts for line in part.splitlines())


def main() -> None:
    OUT_REVIEW_SVG.parent.mkdir(parents=True, exist_ok=True)
    OUT_REVIEW_SVG.write_text(
        build_svg(
            "RACE SIZE REVIEW CHART A04",
            "Review chart generated from updated Aerathea race scale data. Race groups are ordered shortest to tallest; figure tops align to maximum listed height.",
        ),
        encoding="utf-8",
    )
    OUT_APPROVED_SVG.write_text(
        build_svg(
            "RACE SIZE COMPARISON CHART A04",
            "Approved Aerathea race scale reference. Race groups are ordered shortest to tallest; figure tops align to maximum listed height.",
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
