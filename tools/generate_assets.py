from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "assets"
OUT.mkdir(parents=True, exist_ok=True)

SOURCE_FILES = {
    "training": "codex-clipboard-24764c49-8b6e-498c-bff4-5912f8c30f4f.png",
    "calendar": "codex-clipboard-883d714d-7caa-47e3-b376-0c7b36e7b9c5.png",
    "week_plan": "codex-clipboard-a7ab553f-77a3-47b2-9e92-430ea9245e42.png",
    "metrics": "codex-clipboard-9f8ac166-cb1a-4368-9f3c-80cb859fc1f4.png",
    "feedback": "codex-clipboard-38608234-92fa-4fa9-a2bf-05b5ed066123.png",
    "iteration": "codex-clipboard-e0ef723d-04a1-4a4d-884a-2e313e1b977b.png",
    "vercel": "codex-clipboard-6351f9b6-db1f-4465-a407-9a513ec0abec.png",
    "brief": "codex-clipboard-462eb78d-486d-4415-a161-49721d392215.png",
}

CREAM = "#f4efe6"
CREAM_2 = "#e9e3d8"
WHITE = "#fffdf8"
BLACK = "#101010"
INK = "#1f1f1f"
MUTED = "#716b63"
LINE = "#d8d0c4"


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts") / name,
        Path("/usr/share/fonts/truetype/dejavu") / name,
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


TITLE = font("segoeuib.ttf", 42)
HEAD = font("segoeuib.ttf", 28)
REG = font("segoeui.ttf", 22)
MED = font("seguisb.ttf", 22)
SMALL = font("segoeui.ttf", 17)
SMALL_BOLD = font("segoeuib.ttf", 17)
BIG = font("segoeuib.ttf", 76)


def source_dirs() -> list[Path]:
    dirs: list[Path] = []
    env = os.environ.get("PORTFOLIO_SCREENSHOT_DIR")
    if env:
        dirs.append(Path(env))
    dirs.append(Path.home() / "AppData" / "Local" / "Temp")
    dirs.append(ROOT / "tools" / "private-screenshots")
    return dirs


def load_source(key: str) -> Image.Image | None:
    filename = SOURCE_FILES[key]
    for directory in source_dirs():
        path = directory / filename
        if path.exists():
            return Image.open(path).convert("RGB")
    return None


def neutralize(img: Image.Image, color: float = 0.08, contrast: float = 0.95, brightness: float = 1.04) -> Image.Image:
    img = ImageEnhance.Color(img).enhance(color)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Brightness(img).enhance(brightness)
    tint = Image.new("RGB", img.size, CREAM)
    return Image.blend(img, tint, 0.10)


def crop(img: Image.Image, box: tuple[int, int, int, int]) -> Image.Image:
    x1, y1, x2, y2 = box
    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(img.width, x2)
    y2 = min(img.height, y2)
    return img.crop((x1, y1, x2, y2))


def fit_contain(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    scale = min(target_w / img.width, target_h / img.height)
    resized = img.resize((max(1, int(img.width * scale)), max(1, int(img.height * scale))), Image.LANCZOS)
    canvas = Image.new("RGB", size, CREAM_2)
    x = (target_w - resized.width) // 2
    y = (target_h - resized.height) // 2
    canvas.paste(resized, (x, y))
    return canvas


def fit_cover(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    scale = max(target_w / img.width, target_h / img.height)
    resized = img.resize((max(1, int(img.width * scale)), max(1, int(img.height * scale))), Image.LANCZOS)
    x = (resized.width - target_w) // 2
    y = (resized.height - target_h) // 2
    return resized.crop((x, y, x + target_w, y + target_h))


def blur_regions(img: Image.Image, regions: list[tuple[int, int, int, int]], label: str | None = None) -> Image.Image:
    img = img.copy()
    draw = ImageDraw.Draw(img)
    for region in regions:
        x1, y1, x2, y2 = region
        blurred = img.crop(region).filter(ImageFilter.GaussianBlur(12))
        overlay = Image.new("RGB", blurred.size, CREAM)
        blurred = Image.blend(blurred, overlay, 0.86 if label else 0.42)
        img.paste(blurred, region)
        if label:
            text_w = int(draw.textlength(label, font=SMALL_BOLD)) + 24
            draw.rounded_rectangle((x1 + 8, y1 + 8, x1 + 8 + text_w, y1 + 36), radius=8, fill=BLACK)
            draw.text((x1 + 20, y1 + 13), label, fill=WHITE, font=SMALL_BOLD)
    return img


def wrap(draw: ImageDraw.ImageDraw, value: str, width: int, font_: ImageFont.FreeTypeFont) -> list[str]:
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
    return lines


def draw_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, width: int | None = None, fill=INK, font_=REG):
    x, y = xy
    if width is None:
        draw.text((x, y), value, fill=fill, font=font_)
        return
    for line in wrap(draw, value, width, font_):
        draw.text((x, y), line, fill=fill, font=font_)
        y += font_.size + 8


def shadow(canvas: Image.Image, box: tuple[int, int, int, int], radius: int = 8, opacity: int = 38):
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    x1, y1, x2, y2 = box
    draw.rounded_rectangle((x1, y1, x2, y2), radius=radius, fill=(0, 0, 0, opacity))
    layer = layer.filter(ImageFilter.GaussianBlur(22))
    canvas.alpha_composite(layer)


def glass_rect(canvas: Image.Image, box: tuple[int, int, int, int], fill=(255, 253, 248, 142)):
    shadow(canvas, box)
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(box, radius=8, fill=fill, outline=(255, 255, 255, 170), width=2)
    x1, y1, x2, _ = box
    draw.line((x1 + 12, y1 + 12, x2 - 12, y1 + 12), fill=(255, 255, 255, 155), width=1)


def paste_panel(
    canvas: Image.Image,
    img: Image.Image,
    box: tuple[int, int, int, int],
    mode: str = "contain",
    label: str | None = None,
):
    glass_rect(canvas, box)
    x1, y1, x2, y2 = box
    inset = 16
    inner = (x2 - x1 - inset * 2, y2 - y1 - inset * 2 - (34 if label else 0))
    image = fit_cover(img, inner) if mode == "cover" else fit_contain(img, inner)
    canvas.paste(image, (x1 + inset, y1 + inset + (34 if label else 0)))
    draw = ImageDraw.Draw(canvas)
    if label:
        draw.text((x1 + inset, y1 + 14), label, fill=INK, font=SMALL_BOLD)


def board(title: str, subtitle: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    canvas = Image.new("RGBA", (1400, 960), CREAM)
    draw = ImageDraw.Draw(canvas)
    for y in range(0, 960, 2):
        shade = 245 - int((y / 960) * 9)
        draw.line((0, y, 1400, y), fill=(shade, shade - 5, shade - 14, 255))
    draw.rounded_rectangle((44, 30, 1356, 120), radius=8, fill=BLACK)
    draw.text((76, 52), title, fill=WHITE, font=TITLE)
    draw_text(draw, (78, 138), subtitle, 980, fill=MUTED, font_=REG)
    return canvas, draw


def fallback(title: str, subtitle: str, name: str):
    canvas, draw = board(title, subtitle)
    glass_rect(canvas, (94, 260, 1306, 810))
    draw_text(draw, (154, 320), "Sanitized evidence capture", 560, fill=INK, font_=HEAD)
    draw_text(draw, (154, 380), "Private source screenshots are local-only. This public artifact preserves the workflow without exposing raw records.", 820, fill=MUTED, font_=REG)
    draw.text((154, 540), "Privacy boundary kept", fill=INK, font=BIG)
    canvas.convert("RGB").save(OUT / name, quality=92)


def content_system():
    sources = {key: load_source(key) for key in ["calendar", "week_plan", "metrics", "feedback", "iteration"]}
    if not all(sources.values()):
        return fallback("Champions Voice Content OS", "Weekly review becomes next-week strategy.", "content-system.png")

    calendar = neutralize(crop(sources["calendar"], (112, 86, 1448, 806)))
    week_plan = neutralize(crop(sources["week_plan"], (250, 72, 1404, 816)))
    metrics = neutralize(crop(sources["metrics"], (0, 140, 1150, 352)))
    metrics = blur_regions(metrics, [(150, 0, metrics.width, 46)], "links redacted")
    iteration = neutralize(crop(sources["iteration"], (18, 44, 1110, 606)))

    canvas, draw = board(
        "Champions Voice Content OS",
        "Real Notion workflow: calendar, weekly matrix, metrics review, and next-week iteration plan.",
    )
    paste_panel(canvas, calendar, (56, 198, 710, 506), "cover", "Weekly content database")
    paste_panel(canvas, week_plan, (734, 198, 1344, 506), "cover", "Seven-day content matrix")
    paste_panel(canvas, metrics, (56, 540, 710, 842), "cover", "Performance metrics, links redacted")
    paste_panel(canvas, iteration, (734, 540, 1344, 842), "cover", "AI-ready iteration brief")
    draw.text((76, 880), "20.7K followers", fill=BLACK, font=HEAD)
    draw_text(draw, (314, 884), "Human review selects what to repeat, improve, or stop before AI generates the next plan.", 820, fill=MUTED, font_=REG)
    canvas.convert("RGB").save(OUT / "content-system.png", quality=92)


def training_app():
    src = load_source("training")
    if not src:
        return fallback("Private Driveline Training App", "Source-faithful personal training tool.", "training-app.png")
    shot = neutralize(src, color=0.20, contrast=0.96)
    shot = blur_regions(shot, [(440, 174, 838, 216)], None)

    canvas, draw = board(
        "Private Driveline Training App",
        "Mobile and desktop training app built from exported workout history.",
    )
    paste_panel(canvas, shot, (56, 190, 1344, 820), "contain", "Live app dashboard")
    draw.text((76, 864), "402 events  |  98 variants  |  2,374 exercise rows", fill=BLACK, font=HEAD)
    draw_text(draw, (76, 908), "Recommendations stay source-faithful and never invent replacement workouts.", 980, fill=MUTED, font_=REG)
    canvas.convert("RGB").save(OUT / "training-app.png", quality=92)


def lead_funnel():
    src = load_source("vercel")
    if not src:
        return fallback("ManyChat to Notion Lead Funnel", "Deployed connector evidence, redacted for privacy.", "lead-funnel.png")
    shot = neutralize(crop(src, (260, 68, 1454, 710)), color=0.10, brightness=1.02)
    shot = blur_regions(
        shot,
        [
            (436, 76, 1062, 182),
            (430, 206, 1068, 274),
            (0, 0, 206, 58),
            (0, 522, 260, 642),
        ],
        "private",
    )

    canvas, draw = board(
        "ManyChat to Notion Lead Funnel",
        "Production connector evidence with deployment details and account data redacted.",
    )
    paste_panel(canvas, shot, (56, 190, 1344, 758), "cover", "Vercel deployment overview")
    glass_rect(canvas, (116, 792, 1284, 902), fill=(255, 253, 248, 178))
    draw.text((148, 824), "Instagram DM", fill=BLACK, font=MED)
    draw.line((300, 838, 430, 838), fill=BLACK, width=3)
    draw.text((458, 824), "ManyChat capture", fill=BLACK, font=MED)
    draw.line((682, 838, 812, 838), fill=BLACK, width=3)
    draw.text((840, 824), "Notion client list", fill=BLACK, font=MED)
    draw_text(draw, (148, 866), "350-400 emails captured in 2-3 weeks, without publishing private contacts.", 960, fill=MUTED, font_=SMALL)
    canvas.convert("RGB").save(OUT / "lead-funnel.png", quality=92)


def daily_brief():
    src = load_source("brief")
    if not src:
        return fallback("Daily Inbox Brief", "Morning triage dashboard.", "daily-brief.png")
    shot = neutralize(crop(src, (0, 0, 930, 772)), color=0.08)
    shot = blur_regions(
        shot,
        [
            (42, 382, 890, 520),
            (42, 542, 890, 678),
            (42, 704, 890, 772),
        ],
        "email redacted",
    )

    canvas, draw = board(
        "Daily Inbox Brief",
        "8 AM operating dashboard for deals, opportunities, and drafts.",
    )
    paste_panel(canvas, shot, (56, 190, 894, 852), "contain", "Inbox dashboard, private emails blurred")
    glass_rect(canvas, (930, 190, 1344, 852), fill=(255, 253, 248, 166))
    draw.text((966, 238), "Morning triage", fill=BLACK, font=HEAD)
    draw_text(draw, (966, 296), "The brief separates signal from noise before the day starts.", 300, fill=MUTED, font_=REG)
    for i, (value, label) in enumerate([("0", "brand deals"), ("3", "opportunities"), ("25", "drafts ready")]):
        y = 430 + i * 116
        draw.text((966, y), value, fill=BLACK, font=BIG)
        draw.text((1064, y + 34), label, fill=MUTED, font=MED)
    canvas.convert("RGB").save(OUT / "daily-brief.png", quality=92)


def shopify_ops():
    canvas, draw = board(
        "Champions Voice Shopify Web Ops",
        "Safe website operations with explicit review gates and deployment holds.",
    )
    glass_rect(canvas, (70, 190, 640, 392), fill=(255, 253, 248, 168))
    draw.text((108, 232), "Deployment judgment", fill=BLACK, font=HEAD)
    draw_text(draw, (108, 292), "Held deploy when the supposed sandbox was discovered to be live.", 450, fill=MUTED, font_=REG)
    glass_rect(canvas, (690, 190, 1330, 392), fill=(16, 16, 16, 236))
    draw.text((738, 246), "0", fill=WHITE, font=BIG)
    draw_text(draw, (842, 258), "Theme Check errors on latest local batch", 380, fill=WHITE, font_=HEAD)
    draw_text(draw, (842, 322), "Warnings documented. Live promotion waits for approval.", 380, fill="#cfc7ba", font_=SMALL)

    glass_rect(canvas, (70, 452, 1330, 840), fill=(255, 253, 248, 156))
    draw.text((108, 498), "Verified work paths", fill=BLACK, font=HEAD)
    rows = [
        ("Search/cart states", "Waitlist CTAs, no duplicate fallback copy"),
        ("Accessibility", "Heading hierarchy, focus-visible outlines, reduced-motion handling"),
        ("Mobile QA", "390px checks for headers, forms, CTAs, and product paths"),
        ("Runbook", "Daily dashboard tracks blockers, shipped changes, and next batch"),
    ]
    y = 570
    for title, desc in rows:
        draw.rounded_rectangle((112, y + 4, 136, y + 28), radius=8, fill=BLACK)
        draw.text((166, y), title, fill=INK, font=MED)
        draw_text(draw, (450, y), desc, 700, fill=MUTED, font_=REG)
        y += 68
    canvas.convert("RGB").save(OUT / "shopify-ops.png", quality=92)


def og_image():
    canvas = Image.new("RGBA", (1200, 630), CREAM)
    draw = ImageDraw.Draw(canvas)
    glass_rect(canvas, (54, 48, 1146, 582), fill=(255, 253, 248, 150))
    draw.rounded_rectangle((96, 96, 1104, 176), radius=8, fill=BLACK)
    draw.text((128, 116), "Jakobi Davis", fill=WHITE, font=font("segoeuib.ttf", 50))
    draw.text((128, 238), "Claude Corps AI Portfolio", fill=BLACK, font=font("segoeuib.ttf", 58))
    draw_text(
        draw,
        (132, 330),
        "AI workflows, automations, training tools, lead systems, and handoff-ready operations.",
        820,
        fill=MUTED,
        font_=font("segoeui.ttf", 30),
    )
    for i, label in enumerate(["20.7K followers", "350-400 leads", "2,374 rows", "8 AM brief"]):
        x = 132 + i * 244
        draw.rounded_rectangle((x, 470, x + 206, 528), radius=8, fill=BLACK)
        draw.text((x + 20, 488), label, fill=WHITE, font=SMALL_BOLD)
    canvas.convert("RGB").save(OUT / "og-image.png", quality=92)


if __name__ == "__main__":
    content_system()
    training_app()
    lead_funnel()
    daily_brief()
    shopify_ops()
    og_image()
