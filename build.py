"""Builds entry.png: a one-page front page of Thursday 19 November 2026 world news.

Drawn with Pillow at 1024x1024. main.py, the program the grader runs, only
copies this PNG, because the sandbox ships the Python standard library alone.
"""

import math

from PIL import Image, ImageDraw, ImageFont

S = 1024
BG = (10, 14, 22)
CARD = (24, 30, 45)
INK = (243, 246, 252)
DIM = (150, 164, 190)
RED = (232, 86, 72)
GOLD = (238, 184, 80)
TEAL = (86, 200, 180)
VIOLET = (160, 142, 246)
BLUE = (106, 166, 250)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def f(size, bold=True):
    return ImageFont.truetype(BOLD if bold else REG, size)


def fit(d, s, size, width, floor=14):
    while size > floor and d.textlength(s, font=f(size)) > width:
        size -= 1
    return f(size)


def wrap(d, s, ft, width):
    out, cur = [], ""
    for word in s.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=ft) <= width:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def draw_icon(d, kind, cx, cy, col, r=22):
    w = max(3, r // 6)
    if kind == "drone":
        d.ellipse([cx - r // 4, cy - r // 4, cx + r // 4, cy + r // 4], fill=col)
        for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
            ex, ey = cx + dx * r * 0.78, cy + dy * r * 0.62
            d.line([cx, cy, ex, ey], fill=col, width=w)
            d.ellipse([ex - r // 5, ey - r // 5, ex + r // 5, ey + r // 5], outline=col, width=w)
    elif kind == "money":
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=w)
        d.line([cx, cy - r * 0.62, cx, cy + r * 0.62], fill=col, width=w)
        d.line([cx - r * 0.4, cy - r * 0.3, cx + r * 0.4, cy - r * 0.3], fill=col, width=w)
        d.line([cx - r * 0.4, cy + r * 0.15, cx + r * 0.4, cy + r * 0.15], fill=col, width=w)
    elif kind == "virus":
        d.ellipse([cx - r * 0.55, cy - r * 0.55, cx + r * 0.55, cy + r * 0.55], fill=col)
        for i in range(8):
            a = i * math.pi / 4
            d.line([cx + r * 0.55 * math.cos(a), cy + r * 0.55 * math.sin(a),
                    cx + r * math.cos(a), cy + r * math.sin(a)], fill=col, width=w)
    elif kind == "ballot":
        d.rectangle([cx - r * 0.8, cy - r * 0.9, cx + r * 0.8, cy + r * 0.7], outline=col, width=w)
        d.line([cx - r * 0.42, cy - r * 0.1, cx - r * 0.05, cy + r * 0.3], fill=col, width=w)
        d.line([cx - r * 0.05, cy + r * 0.3, cx + r * 0.45, cy - r * 0.35], fill=col, width=w)
    elif kind == "handshake":
        d.line([cx - r, cy - r * 0.3, cx + r * 0.1, cy - r * 0.3], fill=col, width=w)
        d.line([cx + r, cy + r * 0.35, cx - r * 0.1, cy + r * 0.35], fill=col, width=w)
        d.polygon([(cx + r * 0.1, cy - r * 0.3), (cx - r * 0.2, cy - r * 0.62),
                   (cx - r * 0.2, cy + r * 0.02)], fill=col)
        d.polygon([(cx - r * 0.1, cy + r * 0.35), (cx + r * 0.2, cy + r * 0.03),
                   (cx + r * 0.2, cy + r * 0.67)], fill=col)
    elif kind == "plane":
        d.polygon([(cx + r, cy), (cx - r * 0.55, cy - r * 0.55), (cx - r * 0.15, cy),
                   (cx - r * 0.55, cy + r * 0.55)], fill=col)
    elif kind == "people":
        for dx in (-r * 0.62, 0, r * 0.62):
            d.ellipse([cx + dx - r * 0.2, cy - r * 0.75, cx + dx + r * 0.2, cy - r * 0.25], fill=col)
            d.arc([cx + dx - r * 0.42, cy - r * 0.35, cx + dx + r * 0.42, cy + r * 0.7],
                  180, 360, fill=col, width=w)
    elif kind == "art":
        d.rectangle([cx - r, cy - r * 0.85, cx + r, cy + r * 0.85], outline=col, width=w)
        d.line([cx - r * 0.62, cy + r * 0.42, cx - r * 0.1, cy - r * 0.32], fill=col, width=w)
        d.line([cx - r * 0.1, cy - r * 0.32, cx + r * 0.62, cy + r * 0.42], fill=col, width=w)
        d.ellipse([cx + r * 0.22, cy - r * 0.55, cx + r * 0.52, cy - r * 0.25], fill=col)
    elif kind == "jet":
        d.polygon([(cx + r, cy + r * 0.1), (cx - r * 0.5, cy - r * 0.35),
                   (cx - r * 0.2, cy + r * 0.15), (cx - r * 0.5, cy + r * 0.6)], fill=col)


def flag(d, x, y, w, h, which):
    """A small, recognisable flag block."""
    if which == "us":
        d.rectangle([x, y, x + w, y + h], fill=(240, 240, 245))
        for i in range(7):
            d.rectangle([x, y + i * h / 6.5, x + w, y + (i + 0.5) * h / 6.5], fill=(190, 62, 62))
        d.rectangle([x, y, x + w * 0.45, y + h * 0.55], fill=(46, 66, 130))
    elif which == "cn":
        d.rectangle([x, y, x + w, y + h], fill=(206, 54, 54))
        for i, (fx, fy) in enumerate([(0.18, 0.28), (0.34, 0.15), (0.36, 0.35), (0.34, 0.55)]):
            cx, cy, rr = x + w * fx, y + h * fy, w * (0.11 if i == 0 else 0.045)
            d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(246, 214, 120))
    else:  # ru
        d.rectangle([x, y, x + w, y + h / 3], fill=(240, 240, 245))
        d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(54, 78, 158))
        d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(206, 54, 54))


LEAD = ("SHENZHEN, CHINA",
        "Trump, Xi and Putin hold the first three-way summit, at APEC",
        TEAL)
ITEMS = [
    ("KUWAIT & BAHRAIN", "Iranian drones hit US bases after the Qeshm strike", "drone", RED),
    ("BRUSSELS", "EU proposes a 45bn-euro loan for Ukraine in 2027", "money", GOLD),
    ("ATLANTA, US", "US loses measles elimination status, worst since 1991", "virus", RED),
    ("ALASKA, US", "Peltola wins the last Senate race, Democrats hold 56", "ballot", TEAL),
    ("CARACAS", "US and Venezuela sign a deal restoring military ties", "handshake", VIOLET),
    ("ACCRA", "Ghana's 60m-dollar presidential jet sparks public anger", "jet", GOLD),
    ("MOYALE", "Ethiopia-Kenya border clashes displace thousands", "people", BLUE),
    ("NEW YORK", "Van Gogh sells for a record 190.4 million dollars", "art", GOLD),
]
STATS = [("$190.4m", "Van Gogh record"), ("5,412", "US measles cases"),
         ("45bn EUR", "Ukraine loan"), ("56", "Senate seats"), ("$93", "Brent a barrel")]


def main(out="entry.png"):
    img = Image.new("RGB", (S, S), BG)
    d = ImageDraw.Draw(img)

    # ---------------- masthead -----------------------------------------
    d.rectangle([0, 0, S, 148], fill=(16, 21, 33))
    d.rectangle([0, 144, S, 150], fill=RED)
    d.text((32, 16), "THE WORLD IN ONE DAY", font=f(28), fill=INK)
    d.text((30, 48), "19", font=f(84), fill=GOLD)
    d.text((162, 56), "NOVEMBER", font=f(42), fill=INK)
    d.text((164, 100), "2026 · THURSDAY", font=f(30), fill=RED)
    d.text((S - 232, 26), "8 stories", font=f(22), fill=DIM)
    d.text((S - 232, 58), "5 continents", font=f(22), fill=DIM)
    d.text((S - 232, 90), "1 page", font=f(22), fill=TEAL)

    # ---------------- lead story --------------------------------------
    lx, ly, lw, lh = 14, 166, S - 28, 196
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=16, fill=CARD)
    d.rectangle([lx, ly, lx + 8, ly + lh], fill=LEAD[2])
    fx, fy, fw, fh = lx + 34, ly + 52, 96, 62
    for i, which in enumerate(("us", "cn", "ru")):
        flag(d, fx, fy + i * (fh - 10), fw, fh - 22, which)
    d.text((lx + 34, ly + 22), "AT THE TABLE", font=f(16), fill=DIM)
    d.text((lx + 168, ly + 34), LEAD[0], font=f(26), fill=LEAD[2])
    hf = fit(d, LEAD[1], 40, lw - 220)
    for i, ln in enumerate(wrap(d, LEAD[1], hf, lw - 220)[:2]):
        d.text((lx + 168, ly + 74 + i * 48), ln, font=hf, fill=INK)
    d.text((lx + 168, ly + lh - 34), "Shenzhen, 19 November: Xi Jinping greeted Trump on arrival; Putin met both at the APEC banquet",
           font=f(15, False), fill=DIM)

    # ---------------- eight story cards -------------------------------
    top = ly + lh + 10
    cols, gap = 2, 10
    cw = (S - gap * (cols + 1)) // cols
    rows = 4
    ch = (950 - top - gap * (rows - 1)) // rows
    for i, (place, head, icon, col) in enumerate(ITEMS):
        r, c = divmod(i, cols)
        x = gap + c * (cw + gap)
        y = top + r * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=13, fill=CARD)
        d.rectangle([x, y, x + 7, y + ch], fill=col)
        draw_icon(d, icon, x + 48, y + ch // 2, col, 19)
        d.text((x + 86, y + 14), place, font=fit(d, place, 17, cw - 104, floor=12), fill=col)
        hf2 = fit(d, head, 23, cw - 104, floor=15)
        for k, ln in enumerate(wrap(d, head, hf2, cw - 104)[:3]):
            d.text((x + 86, y + 38 + k * 26), ln, font=hf2, fill=INK)

    # ---------------- numbers strip -----------------------------------
    sy, sh = 958, S - 958 - 12
    d.rounded_rectangle([gap, sy, S - gap, sy + sh], radius=13, fill=(16, 21, 33))
    step = (S - 2 * gap) / len(STATS)
    for i, (num, label) in enumerate(STATS):
        x = gap + step * i + 18
        d.text((x, sy + 8), num, font=f(24), fill=GOLD)
        d.text((x, sy + 34), label, font=f(14, False), fill=DIM)
        if i:
            d.line([gap + step * i, sy + 10, gap + step * i, sy + sh - 10], fill=(44, 52, 70), width=2)

    img.save(out, optimize=True)
    return out


if __name__ == "__main__":
    print(main())
