#!/usr/bin/env python3
"""Render a 6 x 9 inch back-cover proof from the canonical author text."""

import argparse
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


def render(source: Path, output: Path) -> None:
    pdfmetrics.registerFont(TTFont("CoverSerif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))
    pdfmetrics.registerFont(TTFont("CoverSerifBold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"))
    blocks = source.read_text().strip().split("\n\n")
    title = blocks.pop(0).removeprefix("# ")
    width, height = 432, 648
    left, measure = 39, 354
    ink, accent, paper = map(HexColor, ("#26221a", "#1f3a5f", "#f7f2e8"))
    body = ParagraphStyle("Body", fontName="CoverSerif", fontSize=10.2,
                          leading=13.3, textColor=ink)
    opening = ParagraphStyle("Opening", parent=body, fontName="CoverSerifBold",
                             fontSize=14.7, leading=19)
    layout = []
    for index, block in enumerate(blocks):
        paragraph = Paragraph(escape(block.replace("\n", " ")), opening if index == 0 else body)
        _, paragraph_height = paragraph.wrap(measure, height)
        layout.append((paragraph, paragraph_height, 11 if index == 0 else 6))
    needed = sum(h + gap for _, h, gap in layout)
    top = 557
    if top - needed < 42:
        raise ValueError(f"Cover text exceeds the safe area by {42 - (top - needed):.1f} pt")

    output.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output), pagesize=(width, height))
    c.setTitle("System 3 - Back Cover")
    c.setAuthor("Hani M.M. Al-Shater")
    c.setFillColor(paper)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.setFillColor(accent)
    c.setFont("CoverSerif", 17)
    c.drawString(left, 593, title)
    c.setStrokeColor(accent)
    c.setLineWidth(0.5)
    c.line(left, 580, left + measure, 580)
    y = top
    for paragraph, paragraph_height, gap in layout:
        paragraph.drawOn(c, left, y - paragraph_height)
        y -= paragraph_height + gap
    c.showPage()
    c.save()
    print(f"{output}: one 6 x 9 inch page; text ends {y:.1f} pt above the bottom")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--source", type=Path,
                        default=Path(__file__).resolve().parents[1] / "chapters/about-the-author.md")
    args = parser.parse_args()
    render(args.source, args.output)
