#!/usr/bin/env python3
"""Build a UGS-v2 PDF from a given Markdown source using reportlab.

Usage: python build_pdf.py <src.md> <out.pdf>
Single source of truth is the .md file. Subset Markdown parser:
headings, paragraphs, bullet/numeric lists, fenced code, tables,
blockquotes, horizontal rules.
"""
import re
import sys

from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable, ListFlowable, ListItem, Paragraph, SimpleDocTemplate,
    Spacer, Table, TableStyle,
)

SRC = sys.argv[1] if len(sys.argv) > 1 else "README.md"
OUT = sys.argv[2] if len(sys.argv) > 2 else "UGS-v2.pdf"

# ---- fonts: register a Unicode TTF for Cyrillic; fall back gracefully
FONT = "Helvetica"
BOLD = "Helvetica-Bold"
_candidates = [
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\DejaVuSans.ttf",
    r"C:\Windows\Fonts\segoeui.ttf",
]
_bold_candidates = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\DejaVuSans-Bold.ttf",
    r"C:\Windows\Fonts\segoeuib.ttf",
]
for c in _candidates:
    try:
        pdfmetrics.registerFont(TTFont("Body", c))
        FONT = "Body"
        break
    except Exception:
        pass
for c in _bold_candidates:
    try:
        pdfmetrics.registerFont(TTFont("BodyB", c))
        BOLD = "BodyB"
        break
    except Exception:
        pass


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName=BOLD, fontSize=18,
                    spaceBefore=10, spaceAfter=8, textColor="#10243e")
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName=BOLD, fontSize=13.5,
                    spaceBefore=12, spaceAfter=5, textColor="#16324f")
H3 = ParagraphStyle("H3", parent=ss["Heading3"], fontName=BOLD, fontSize=11.5,
                    spaceBefore=8, spaceAfter=3, textColor="#1f3d57")
BODY = ParagraphStyle("BODY", parent=ss["BodyText"], fontName=FONT, fontSize=10.2,
                      leading=14.5, spaceAfter=6, alignment=TA_LEFT)
QUOTE = ParagraphStyle("QUOTE", parent=BODY, leftIndent=14, fontName=FONT,
                       fontSize=10.2, leading=14.5, textColor="#33414f",
                       spaceBefore=4, spaceAfter=8)
CODE = ParagraphStyle("CODE", parent=BODY, fontName="Courier", fontSize=9,
                      leading=12, leftIndent=10, backColor="#f2f4f7",
                      borderPadding=6, spaceBefore=4, spaceAfter=8)
TITLE = ParagraphStyle("TITLE", parent=H1, fontSize=24, alignment=TA_CENTER,
                       spaceAfter=4, textColor="#0b1f33")
SUB = ParagraphStyle("SUB", parent=BODY, alignment=TA_CENTER, fontSize=11,
                     textColor="#445")
CELL = ParagraphStyle("CELL", parent=BODY, fontSize=9, leading=12, spaceAfter=0)
CELLH = ParagraphStyle("CELLH", parent=CELL, fontName=BOLD)


def parse_table(lines):
    rows = []
    for ln in lines:
        if re.match(r"^\s*\|?[\s:\-\|]+\|?\s*$", ln):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows.append(cells)
    header = rows[0]
    body = rows[1:]
    data = [[Paragraph(esc(h), CELLH) for h in header]]
    for r in body:
        data.append([Paragraph(esc(c), CELL) for c in r])
    ncol = len(header)
    widths = [(A4[0] - 4 * cm) / ncol] * ncol
    t = Table(data, colWidths=widths, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), "#16324f"),
        ("TEXTCOLOR", (0, 0), (-1, 0), "#ffffff"),
        ("GRID", (0, 0), (-1, -1), 0.4, "#9fb0c0"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), ["#ffffff", "#eef2f6"]),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def build():
    with open(SRC, encoding="utf-8") as f:
        raw = f.read()
    lines = raw.replace("\r\n", "\n").split("\n")

    flow = []
    i = 0
    n = len(lines)
    first_h1_done = False
    while i < n:
        ln = lines[i]
        stripped = ln.strip()

        if stripped.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            flow.append(Paragraph(esc("\n".join(buf).rstrip("\n")).replace("\n", "<br/>"), CODE))
            continue

        if re.match(r"^-{3,}$", stripped) or re.match(r"^\*{3,}$", stripped):
            flow.append(HRFlowable(width="100%", thickness=0.6,
                                   color="#bcc8d4", spaceBefore=4, spaceAfter=8))
            i += 1; continue

        m = re.match(r"^(#{1,3})\s+(.*)$", ln)
        if m:
            level = len(m.group(1)); text = m.group(2).strip()
            if level == 1 and not first_h1_done:
                flow.append(Spacer(1, 1.2 * cm))
                flow.append(Paragraph(esc(text), TITLE))
                first_h1_done = True
                i += 1; continue
            style = {1: H1, 2: H2, 3: H3}[level]
            flow.append(Paragraph(esc(text), style))
            i += 1; continue

        if stripped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip()); i += 1
            flow.append(Paragraph("<br/>".join(esc(b) for b in buf), QUOTE))
            continue

        if stripped.startswith("|"):
            buf = []
            while i < n and lines[i].strip().startswith("|"):
                buf.append(lines[i]); i += 1
            flow.append(parse_table(buf)); flow.append(Spacer(1, 4))
            continue

        if re.match(r"^\s*([-*]|\d+\.)\s+", ln):
            items = []
            while i < n and re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                content = re.split(r"^\s*([-*]|\d+\.)\s+", lines[i], maxsplit=1)[-1]
                items.append(ListItem(Paragraph(esc(content.strip()), BODY), leftIndent=10))
                i += 1
            flow.append(ListFlowable(items, bulletType="bullet", start="•", leftIndent=14))
            continue

        if stripped == "":
            i += 1; continue

        buf = [stripped]; i += 1
        while (i < n and lines[i].strip() != ""
               and not lines[i].strip().startswith(("#", ">", "|", "```"))
               and not re.match(r"^\s*([-*]|\d+\.)\s+", lines[i])
               and not re.match(r"^-{3,}$", lines[i].strip())):
            buf.append(lines[i].strip()); i += 1
        flow.append(Paragraph(esc(" ".join(buf)), BODY))

    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="UGS v2 Specification", author="Konstantin Parashchuk / SINT",
    )

    def footer(canvas, d):
        canvas.saveState()
        canvas.setFont(FONT, 8)
        canvas.setFillColor("#8a97a3")
        canvas.drawString(2 * cm, 1.1 * cm, "UGS v2 — Universal Generation Specification")
        canvas.drawRightString(A4[0] - 2 * cm, 1.1 * cm, "Page %d" % d.page)
        canvas.restoreState()

    doc.build(flow, onFirstPage=footer, onLaterPages=footer)
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
