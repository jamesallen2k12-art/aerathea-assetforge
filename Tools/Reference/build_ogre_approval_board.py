#!/usr/bin/env python3
"""Build an Ogre source-concept approval board for SK_OGR_Base_A01."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
CONCEPT_DIR = Path("/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS")
OUT = ROOT / "docs/assets/characters/SK_OGR_Base_A01/OGRE_APPROVAL_BOARD_A01.png"

BG = (229, 220, 205)
PANEL = (244, 238, 226)
INK = (38, 31, 25)
MUTED = (89, 75, 60)
LINE = (102, 83, 65)
ACCENT = (156, 78, 36)

CARD_W = 760
IMAGE_H = 310
LABEL_H = 62
GAP = 24
LEFT = 80
TOP = 86
COLS = 5


@dataclass(frozen=True)
class SourceCard:
    filename: str
    note: str


SECTIONS: list[tuple[str, list[SourceCard]]] = [
    (
        "Body And Class Direction",
        [
            SourceCard("Ogre Female.png", "Female body scale and armor mass"),
            SourceCard("OgreFemale2.png", "Female shaman/tek silhouette language"),
            SourceCard("OgreMale1.png", "Male body and Teknomancy hardware"),
            SourceCard("OgreMale2.png", "Necromancer body and green-black magic"),
            SourceCard("Ogremale4.png", "Male warrior mass and weapon scale"),
            SourceCard("OgreMaleTek.png", "Teknomancer class direction"),
            SourceCard("OgreWarrior.png", "Warrior class direction"),
            SourceCard("OgreShaman.png", "Shaman class direction"),
            SourceCard("OgreNecromancer.png", "Necromancer class direction"),
            SourceCard("OgreSentinel.png", "Sentinel/warband silhouette"),
            SourceCard("OgreSentinels.png", "Formation and repeated body language"),
            SourceCard("OgreSmiths.png", "Forge NPC and oversized craft culture"),
        ],
    ),
    (
        "Teknomancy And Gnome Mek Rivalry",
        [
            SourceCard("GnomevsOgre1.png", "Gnome Mek encounter scale"),
            SourceCard("GnomevsOgre2.png", "Ranged Teknomancy pressure"),
            SourceCard("GnomevsOgre3.png", "Blue Aetherium beam rivalry"),
            SourceCard("GnomevsOgre4.png", "Ogre warband against Mek pilot"),
            SourceCard("GnomevsOgre5.png", "Battlefield chaos and size contrast"),
            SourceCard("GnomevsOgre6.png", "Close-range Mek collision reference"),
            SourceCard("GnomevsOgre7.png", "Magic-tech beam duel reference"),
            SourceCard("GnomevsOgre9.png", "Warfront scale and terrain read"),
            SourceCard("GnomevsOgre10.png", "Forge/warcamp lighting reference"),
            SourceCard("GnomevsOgreandManticore8.png", "Encounter escalation reference"),
            SourceCard("OgreTekvsGnomeMek.png", "Primary Ogre Tek vs Gnome Mek source"),
        ],
    ),
    (
        "Settlement, Cairns, And Fortifications",
        [
            SourceCard("OgreBarracks.png", "Barracks interior and shield wall props"),
            SourceCard("OgreForge.png", "Forge, heat, and heavy workstations"),
            SourceCard("OgreFortress.png", "Fortress mass and silhouette"),
            SourceCard("OgreGate.png", "Gate scale and defensive entry"),
            SourceCard("OgreInn.png", "Civilian settlement building"),
            SourceCard("OgreNecropolis.png", "Necropolis and green-black cairns"),
            SourceCard("OgreShamanHut.png", "Shaman hut and ritual exterior"),
            SourceCard("OgreTekShop.png", "Tek shop interior and siege device cues"),
            SourceCard("Ogres1.png", "Interior hall and fire-lit settlement culture"),
            SourceCard("Ogres2.png", "Stone building and wall profile"),
            SourceCard("Ogres3.png", "Cairn field and necropolis color"),
            SourceCard("Ogres5.png", "Forge/interior production space"),
            SourceCard("Ogres6.png", "Settlement building and inn language"),
            SourceCard("Ogres7.png", "Cairn fortress and valley siting"),
            SourceCard("Ogres8 .png", "Heavy gate and filename normalization"),
            SourceCard("Ogres9.png", "Interior gathering hall"),
            SourceCard("Ogres10.png", "Tek forge and siege workshop"),
            SourceCard("Ogres11.png", "Siege yard and cannon scale"),
        ],
    ),
]


def font(size: int, serif: bool = False):
    candidates = [
        "DejaVuSerif.ttf" if serif else "DejaVuSans.ttf",
        "/usr/share/fonts/google-noto/NotoSerif-Regular.ttf" if serif else "/usr/share/fonts/google-noto/NotoSans-Regular.ttf",
        "/usr/share/fonts/liberation/LiberationSerif-Regular.ttf" if serif else "/usr/share/fonts/liberation/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except Exception:
            continue
    return None


TITLE_FONT = font(42, serif=True)
SUBTITLE_FONT = font(22)
SECTION_FONT = font(28, serif=True)
LABEL_FONT = font(18)
SMALL_FONT = font(15)


def text_lines(text: str, width: int) -> list[str]:
    return wrap(text, width=width, break_long_words=False) or [text]


def card_height() -> int:
    return IMAGE_H + LABEL_H


def total_height() -> int:
    y = TOP + 96
    for _, cards in SECTIONS:
        rows = (len(cards) + COLS - 1) // COLS
        y += 54 + rows * card_height() + (rows - 1) * GAP + 46
    return y + 70


def draw_card(draw: ImageDraw.ImageDraw, board: Image.Image, card: SourceCard, x: int, y: int) -> None:
    draw.rectangle((x, y, x + CARD_W, y + card_height()), fill=PANEL, outline=LINE, width=2)

    source = CONCEPT_DIR / card.filename
    if source.exists():
        img = Image.open(source).convert("RGB")
        img.thumbnail((CARD_W - 24, IMAGE_H - 20), Image.Resampling.LANCZOS)
        px = x + (CARD_W - img.width) // 2
        py = y + 10 + (IMAGE_H - 20 - img.height) // 2
        board.paste(img, (px, py))
    else:
        draw.rectangle((x + 12, y + 10, x + CARD_W - 12, y + IMAGE_H - 10), fill=(82, 70, 59))
        draw.text((x + CARD_W // 2, y + IMAGE_H // 2), "Missing source", fill=PANEL, font=LABEL_FONT, anchor="mm")

    label_y = y + IMAGE_H + 18
    draw.text((x + 18, label_y), card.filename, fill=INK, font=LABEL_FONT)
    for offset, line in enumerate(text_lines(card.note, 58)[:2]):
        draw.text((x + 18, label_y + 24 + offset * 18), line, fill=MUTED, font=SMALL_FONT)


def main() -> None:
    width = LEFT * 2 + COLS * CARD_W + (COLS - 1) * GAP
    height = total_height()
    board = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(board)

    draw.text((width // 2, 38), "SK_OGR_Base_A01 Ogre Approval Board A01", fill=INK, font=TITLE_FONT, anchor="mm")
    subtitle = "41 source files scanned: base bodies, class silhouettes, Gnome Mek rivalry, cairn fortifications, forge interiors, and settlement language."
    draw.text((width // 2, 74), subtitle, fill=MUTED, font=SUBTITLE_FONT, anchor="mm")
    draw.line((LEFT, 112, width - LEFT, 112), fill=ACCENT, width=4)

    y = TOP + 96
    for title, cards in SECTIONS:
        draw.text((LEFT, y), title, fill=INK, font=SECTION_FONT)
        y += 42
        rows = (len(cards) + COLS - 1) // COLS
        for index, card in enumerate(cards):
            row, col = divmod(index, COLS)
            x = LEFT + col * (CARD_W + GAP)
            cy = y + row * (card_height() + GAP)
            draw_card(draw, board, card, x, cy)
        y += rows * card_height() + (rows - 1) * GAP + 46

    footer = "Approval focus: confirm base body direction, choose male/female chart cutouts, then move Teknomancer to first class package."
    draw.text((width // 2, height - 44), footer, fill=MUTED, font=SUBTITLE_FONT, anchor="mm")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    board.save(OUT, quality=95)
    print(OUT)


if __name__ == "__main__":
    main()
