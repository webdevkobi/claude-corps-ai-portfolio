from __future__ import annotations

from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "assets"
OUT.mkdir(parents=True, exist_ok=True)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts") / name,
        Path("/usr/share/fonts/truetype/dejavu") / name,
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


REG = font("segoeui.ttf", 24)
MED = font("seguisb.ttf", 24)
BOLD = font("segoeuib.ttf", 28)
TITLE = font("segoeuib.ttf", 42)
BIG = font("segoeuib.ttf", 74)
SMALL = font("segoeui.ttf", 18)
SMALL_BOLD = font("segoeuib.ttf", 18)

INK = "#20252b"
MUTED = "#68717c"
PAPER = "#f5f4ef"
SURFACE = "#ffffff"
LINE = "#d9d6ce"
TEAL = "#0f766e"
BLUE = "#255f85"
RUST = "#9a5c28"
SAGE = "#6d7f54"
AMBER = "#d99a32"


def rounded(draw: ImageDraw.ImageDraw, box, radius=18, fill=SURFACE, outline=LINE, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw: ImageDraw.ImageDraw, xy, value, fill=INK, font_=REG, width=None, line_spacing=8):
    if width is None:
        draw.text(xy, value, fill=fill, font=font_)
        return
    words = value.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=font_) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    x, y = xy
    ascent = font_.size if hasattr(font_, "size") else 22
    for line in lines:
        draw.text((x, y), line, fill=fill, font=font_)
        y += ascent + line_spacing


def pill(draw, xy, label, fill="#eef7f4", color=TEAL):
    x, y = xy
    w = int(draw.textlength(label, font=SMALL_BOLD)) + 28
    draw.rounded_rectangle((x, y, x + w, y + 34), radius=17, fill=fill, outline=None)
    draw.text((x + 14, y + 7), label, fill=color, font=SMALL_BOLD)
    return w


def blur_band(img: Image.Image, box, label="redacted"):
    crop = img.crop(box).filter(ImageFilter.GaussianBlur(10))
    overlay = Image.new("RGBA", crop.size, (255, 255, 255, 78))
    crop = Image.alpha_composite(crop.convert("RGBA"), overlay)
    img.paste(crop.convert("RGB"), box)
    draw = ImageDraw.Draw(img)
    x1, y1, x2, y2 = box
    label_width = int(draw.textlength(label, font=SMALL_BOLD)) + 30
    draw.rounded_rectangle((x1 + 10, y1 + 10, x1 + 10 + label_width, y1 + 42), radius=16, fill="#20252b")
    draw.text((x1 + 24, y1 + 17), label, fill="#fffaf0", font=SMALL_BOLD)


def base(title: str, subtitle: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (1400, 960), PAPER)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 1400, 96), fill="#20252b")
    draw.text((56, 28), title, fill="#fffaf0", font=TITLE)
    draw.text((58, 102), subtitle, fill=MUTED, font=REG)
    return img, draw


def save(img: Image.Image, name: str):
    img.save(OUT / name, quality=92)


def content_system():
    img, draw = base(
        "Champions Voice Content OS",
        "Weekly human-in-the-loop review turns performance into the next 7-day plan.",
    )
    rounded(draw, (56, 162, 460, 408), fill="#ffffff")
    text(draw, (86, 190), "Creator Vision", font_=BOLD)
    text(
        draw,
        (86, 238),
        "Source of truth for voice, pillars, audience, proof points, and offers.",
        fill=MUTED,
        font_=REG,
        width=310,
    )
    for i, label in enumerate(["Identity", "Recruiting", "Systems", "Leadership"]):
        pill(draw, (86 + (i % 2) * 158, 326 + (i // 2) * 42), label, fill="#f1f4ed", color=SAGE)

    rounded(draw, (500, 162, 1328, 408), fill="#ffffff")
    text(draw, (530, 190), "Week 17 Review", font_=BOLD)
    for x, big, small, color in [
        (540, "250K+", "views on winning format", BLUE),
        (780, "~918", "follows from one format", TEAL),
        (1020, "20.7K", "followers in 2-3 months", RUST),
    ]:
        draw.text((x, 254), big, fill=color, font=BIG)
        text(draw, (x, 330), small, fill=MUTED, font_=SMALL_BOLD, width=170)

    rounded(draw, (56, 470, 1328, 866), fill="#ffffff")
    text(draw, (86, 500), "Next-week planning matrix", font_=BOLD)
    headers = ["Day", "Format", "Hook", "Human review", "AI iteration"]
    col_x = [86, 190, 420, 710, 1000]
    for x, header in zip(col_x, headers):
        draw.text((x, 562), header, fill=MUTED, font=SMALL_BOLD)
    rows = [
        ("Mon", "Recruiting deep-dive", "The DM that changed...", "Keep", "Expand proof"),
        ("Wed", "Split screen", "Amateur vs D1 vs Pro", "Repeat", "Sharper CTA"),
        ("Fri", "Playbook waitlist", "Systems I needed sooner", "Test", "Shorter intro"),
    ]
    y = 612
    for row in rows:
        draw.line((86, y - 18, 1286, y - 18), fill=LINE, width=2)
        for x, cell in zip(col_x, row):
            text(draw, (x, y), cell, font_=SMALL_BOLD if x == 86 else SMALL, width=210)
        y += 78
    blur_band(img, (700, 718, 1288, 820), "comments redacted")
    save(img, "content-system.png")


def lead_funnel():
    img, draw = base(
        "ManyChat to Notion Lead Funnel",
        "Instagram interest becomes an owned, auditable client list.",
    )
    steps = [
        ("Instagram CTA", "Follower sends keyword in DM", TEAL),
        ("ManyChat", "Collects email and source", BLUE),
        ("Validation", "Checks required fields", RUST),
        ("Notion DB", "Creates client-list record", SAGE),
    ]
    x = 70
    y = 180
    for i, (name, desc, color) in enumerate(steps):
        rounded(draw, (x, y, x + 270, y + 166), fill="#ffffff")
        draw.ellipse((x + 24, y + 28, x + 70, y + 74), fill=color)
        draw.text((x + 88, y + 30), name, fill=INK, font=BOLD)
        text(draw, (x + 28, y + 92), desc, fill=MUTED, font_=SMALL, width=214)
        if i < len(steps) - 1:
            draw.line((x + 282, y + 82, x + 330, y + 82), fill="#817a6f", width=4)
            draw.polygon([(x + 330, y + 82), (x + 316, y + 73), (x + 316, y + 91)], fill="#817a6f")
        x += 320

    rounded(draw, (70, 430, 780, 840), fill="#ffffff")
    text(draw, (102, 462), "Client list schema", font_=BOLD)
    for i, label in enumerate(["Name", "Email", "Instagram", "Source", "Lead Status", "Latest Interaction", "Notes"]):
        pill(draw, (102 + (i % 3) * 205, 522 + (i // 3) * 48), label, fill="#f1f4ed", color=INK)
    blur_band(img, (104, 648, 744, 792), "lead rows redacted")

    rounded(draw, (820, 430, 1328, 840), fill="#20252b", outline="#20252b")
    draw.text((858, 492), "350-400", fill="#fffaf0", font=BIG)
    text(draw, (862, 580), "emails captured in roughly 2-3 weeks", fill="#e9e2d6", font_=BOLD, width=360)
    text(
        draw,
        (862, 680),
        "Built as a practical connector, not a vanity automation: every record supports follow-up.",
        fill="#bfb7aa",
        font_=REG,
        width=370,
    )
    save(img, "lead-funnel.png")


def training_app():
    img, draw = base(
        "Private Driveline Training App",
        "Source-faithful training app built from exported history.",
    )
    draw.rounded_rectangle((56, 156, 280, 884), radius=22, fill="#172c37")
    draw.text((88, 198), "JD", fill="#d9f1e9", font=BIG)
    for i, label in enumerate(["Home", "Coach build", "Calendar", "Library"]):
        fill = "#d9f1e9" if i == 0 else "#27434f"
        color = "#073d32" if i == 0 else "#d9e5e6"
        draw.rounded_rectangle((84, 330 + i * 64, 250, 374 + i * 64), radius=12, fill=fill)
        draw.text((104, 340 + i * 64), label, fill=color, font=SMALL_BOLD)

    rounded(draw, (320, 156, 1328, 884), fill="#ffffff")
    text(draw, (358, 194), "Today's readiness check-in", font_=TITLE)
    text(draw, (360, 252), "Recommendations only select existing Driveline plan variants.", fill=MUTED, font_=REG)
    for x, big, small, color in [
        (360, "402", "calendar events", TEAL),
        (596, "98", "prescription variants", BLUE),
        (832, "2,374", "exercise rows", RUST),
    ]:
        rounded(draw, (x, 326, x + 200, 474), fill="#faf9f4")
        draw.text((x + 22, 350), big, fill=color, font=BIG)
        text(draw, (x + 24, 428), small, fill=MUTED, font_=SMALL_BOLD, width=140)

    rounded(draw, (358, 534, 728, 810), fill="#f1f4ed", outline="#d6dbc9")
    text(draw, (388, 566), "Calendar history", font_=BOLD)
    for i in range(5):
        y = 626 + i * 32
        draw.rounded_rectangle((390, y, 694, y + 18), radius=8, fill=["#0f766e", "#255f85", "#9a5c28", "#6d7f54", "#0f766e"][i])

    rounded(draw, (764, 534, 1288, 810), fill="#f8f7f2")
    text(draw, (794, 566), "Workout detail", font_=BOLD)
    for i in range(4):
        y = 630 + i * 40
        draw.text((800, y), f"A{i + 1}", fill=RUST, font=SMALL_BOLD)
        draw.rounded_rectangle((860, y - 4, 1238, y + 22), radius=12, fill="#e7e1d8")
    blur_band(img, (852, 622, 1248, 786), "prescriptions redacted")
    save(img, "training-app.png")


def daily_brief():
    img, draw = base(
        "Daily Inbox Brief",
        "8:00 AM dashboard for brand deals, opportunities, and filtered noise.",
    )
    stats = [("0", "Brand deals", TEAL), ("2", "Opportunities", AMBER), ("26", "Filtered out", MUTED)]
    for i, (n, label, color) in enumerate(stats):
        x = 70 + i * 420
        rounded(draw, (x, 170, x + 360, 316), fill="#ffffff")
        draw.text((x + 30, 194), n, fill=color, font=BIG)
        draw.text((x + 34, 268), label, fill=MUTED, font=SMALL_BOLD)

    rounded(draw, (70, 390, 1330, 830), fill="#ffffff")
    text(draw, (104, 426), "Opportunities & important", font_=BOLD)
    cards = [
        ("Warm referral source", "Thank contact, watch for referrals"),
        ("Booked consult", "Prep, run call, follow up"),
    ]
    y = 494
    for title, action in cards:
        rounded(draw, (104, y, 1296, y + 130), fill="#fbfaf6")
        text(draw, (136, y + 24), title, font_=BOLD)
        text(draw, (136, y + 68), "From: [private contact] <redacted@example.com>", fill=MUTED, font_=SMALL)
        pill(draw, (984, y + 28), "Worth a look", fill="#fff1d8", color=RUST)
        text(draw, (984, y + 76), action, fill=INK, font_=SMALL_BOLD, width=250)
        blur_band(img, (132, y + 58, 720, y + 104), "email redacted")
        y += 154
    save(img, "daily-brief.png")


def shopify_ops():
    img, draw = base(
        "Champions Voice Shopify Web Ops",
        "AI-assisted website manager with deployment guardrails and QA notes.",
    )
    rounded(draw, (70, 164, 600, 392), fill="#ffffff")
    text(draw, (104, 202), "Deployment guardrail", font_=BOLD)
    draw.rounded_rectangle((104, 260, 562, 326), radius=14, fill="#fff1d8", outline="#ead3a5")
    text(draw, (128, 278), "Sandbox detected as live: hold push", fill=RUST, font_=MED, width=390)

    rounded(draw, (640, 164, 1330, 392), fill="#20252b", outline="#20252b")
    draw.text((682, 216), "0", fill="#fffaf0", font=BIG)
    text(draw, (780, 232), "Theme Check errors on latest local batch", fill="#e9e2d6", font_=BOLD, width=430)
    text(draw, (682, 316), "41 warnings documented, no live promotion without approval.", fill="#bfb7aa", font_=SMALL, width=520)

    rounded(draw, (70, 458, 1330, 852), fill="#ffffff")
    text(draw, (104, 492), "Verified work paths", font_=BOLD)
    items = [
        ("Search/cart empty states", "Playbook waitlist CTAs, no duplicate fallback copy"),
        ("Accessibility", "Heading hierarchy, focus-visible outlines, reduced-motion handling"),
        ("Mobile QA", "390px checks for header, email forms, CTAs, and product paths"),
        ("Runbook", "Daily dashboard tracks blockers, shipped changes, and next batch"),
    ]
    y = 558
    for title, desc in items:
        draw.ellipse((110, y + 4, 132, y + 26), fill=TEAL)
        text(draw, (154, y), title, font_=SMALL_BOLD)
        text(draw, (420, y), desc, fill=MUTED, font_=SMALL, width=760)
        y += 62
    save(img, "shopify-ops.png")


def og_image():
    img = Image.new("RGB", (1200, 630), "#20252b")
    draw = ImageDraw.Draw(img)
    draw.text((70, 70), "Jakobi Davis", fill="#fffaf0", font=font("segoeuib.ttf", 68))
    text(
        draw,
        (76, 170),
        "Claude Corps AI Portfolio",
        fill="#d9f1e9",
        font_=font("segoeui.ttf", 38),
        width=760,
    )
    text(
        draw,
        (78, 270),
        "AI workflows, automations, training tools, lead systems, and handoff-ready operations.",
        fill="#c7c0b5",
        font_=font("segoeui.ttf", 34),
        width=780,
    )
    for i, label in enumerate(["20.7K followers", "350-400 leads", "2,374 rows", "8 AM brief"]):
        x = 76 + i * 270
        draw.rounded_rectangle((x, 474, x + 230, 548), radius=16, fill="#fffaf0")
        draw.text((x + 24, 500), label, fill=INK, font=font("segoeuib.ttf", 24))
    img.save(OUT / "og-image.png", quality=92)


if __name__ == "__main__":
    content_system()
    lead_funnel()
    training_app()
    daily_brief()
    shopify_ops()
    og_image()
