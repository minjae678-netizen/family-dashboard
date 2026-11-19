#!/usr/bin/env python3
# 우리 가족 오늘 보드 앱 아이콘 생성 (코랄 배경 + 흰 집 + 코랄 하트)
from PIL import Image, ImageDraw

CORAL = (232, 115, 74)
CORAL_DEEP = (216, 97, 58)


def house(draw, cx, cy, w, body_color=(255, 255, 255), heart_color=CORAL):
    """cx, cy 중심, 전체 폭 w 인 집(지붕+몸통)을 그리고 그 안에 하트를 그린다."""
    H = w * 0.94                      # 집 전체 높이
    top = cy - H / 2
    body_w = w * 0.70
    overlap = w * 0.06                # 지붕과 몸통이 겹치게
    roof_h = H * 0.48
    body_top = top + roof_h - overlap
    body_h = cy + H / 2 - body_top

    # 지붕
    draw.polygon(
        [(cx, top), (cx + w / 2, body_top + overlap * 1.2), (cx - w / 2, body_top + overlap * 1.2)],
        fill=body_color,
    )
    # 몸통
    draw.rounded_rectangle(
        [cx - body_w / 2, body_top, cx + body_w / 2, body_top + body_h],
        radius=w * 0.075,
        fill=body_color,
    )
    # 하트 (몸통 안쪽)
    hw = body_w * 0.42
    hcx = cx
    hcy = body_top + body_h * 0.50
    r = hw * 0.27
    draw.ellipse([hcx - hw / 2, hcy - r * 1.55, hcx - hw / 2 + 2 * r, hcy - r * 1.55 + 2 * r], fill=heart_color)
    draw.ellipse([hcx + hw / 2 - 2 * r, hcy - r * 1.55, hcx + hw / 2, hcy - r * 1.55 + 2 * r], fill=heart_color)
    draw.polygon(
        [(hcx - hw / 2, hcy - r * 0.55), (hcx + hw / 2, hcy - r * 0.55), (hcx, hcy + r * 1.45)],
        fill=heart_color,
    )


def gradient(size, top=CORAL, bottom=CORAL_DEEP):
    img = Image.new("RGB", (size, size), top)
    d = ImageDraw.Draw(img)
    for y in range(size):
        t = y / max(1, size - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(0, y), (size, y)], fill=c)
    return img


def make(size, path, maskable=False, radius_ratio=0.235):
    ss = 4
    S = size * ss
    base = gradient(S)
    d = ImageDraw.Draw(base)
    w = S * (0.50 if maskable else 0.58)   # 마스커블은 안전영역(가운데 80%) 안에
    house(d, S / 2, S / 2, w)
    if maskable:
        out = base.resize((size, size), Image.LANCZOS)
    else:
        mask = Image.new("L", (S, S), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * radius_ratio), fill=255)
        out = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        out.paste(base, (0, 0), mask)
        out = out.resize((size, size), Image.LANCZOS)
    out.save(path, "PNG", optimize=True)
    print("wrote", path, size)


make(192, "icon-192.png")
make(512, "icon-512.png")
make(512, "icon-maskable-512.png", maskable=True)
make(180, "icon-180.png")
