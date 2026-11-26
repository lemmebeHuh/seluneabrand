"""
SELUNÉA — Interactive Responsive Brand Identity Showcase Website Builder (True 60fps Path-Morph Edition)
Output: c:/Users/ridwa/Desktop/selunea/selunea-brand-identity/index.html

Upgrade in this edition:
- TRUE 60FPS GEOMETRIC SVG PATH MORPHING:
  Every one of the 4 selectable Brand Marks (Tri-Phase Lunar, Option 01 Eclipse Halo,
  Option 02 Lunar Equinox, Option 04 Dual-Phase S) is arc-length-sampled in Python into
  3 canonical 64-point closed contours (aligned clockwise from topmost point so contours
  never twist or bowtie!).
  On click, requestAnimationFrame smoothly interpolates every single (x, y) vertex with
  silky cubic-in-out easing inside a single <path fill-rule="evenodd"> — ZERO filter jank,
  ZERO blur lag, butter-smooth 60fps liquid geometry across desktop & mobile! At t=1.0, it
  snaps cleanly to the exact analytical vector SVG curves.
- Clarified the confirmation button ("Salin Konfirmasi untuk KALLA" + clear helper note explaining
  it copies a ready-to-paste confirmation message for WhatsApp/chat).
"""

import math
import json
import re
from pathlib import Path

BASE = Path(r"c:\Users\ridwa\Desktop\selunea\selunea-brand-identity")
SVG_DIR = BASE / "05-logo-final" / "svg"
OPT_DIR = BASE / "04-logo-concepts" / "brand-mark-options"
GFX_DIR = BASE / "07-graphic-assets"

N_PTS = 56  # Smooth, lightweight closed contour resolution (56 pts x 3 subpaths = ultra-fast 60fps!)


# ---------------------------------------------------------------------------
# ARC-LENGTH CONTOUR SAMPLERS FOR TRUE 60FPS GEOMETRIC PATH MORPHING
# ---------------------------------------------------------------------------

def sample_cubic(p0, p1, p2, p3, steps=24):
    pts = []
    for i in range(steps):
        t = i / steps
        mt = 1.0 - t
        x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def sample_line(p0, p1, steps=12):
    return [(p0[0] + (p1[0] - p0[0]) * i / steps, p0[1] + (p1[1] - p0[1]) * i / steps) for i in range(steps)]


def sample_arc_circle(cx, cy, r, a_start, a_end, ccw=False, steps=48):
    """Sample circular arc from angle a_start to a_end (radians in SVG y-down coords)."""
    if ccw:
        diff = (a_start - a_end) % (2 * math.pi)
        if diff == 0:
            diff = 2 * math.pi
        return [(cx + r * math.cos(a_start - diff * i / steps), cy + r * math.sin(a_start - diff * i / steps)) for i in range(steps)]
    else:
        diff = (a_end - a_start) % (2 * math.pi)
        if diff == 0:
            diff = 2 * math.pi
        return [(cx + r * math.cos(a_start + diff * i / steps), cy + r * math.sin(a_start + diff * i / steps)) for i in range(steps)]


def resample_closed(raw_pts, n=N_PTS):
    """Resample a closed polygon uniformly by arc length, orient clockwise, and align start to topmost point."""
    # Ensure clockwise orientation in SVG y-down (positive signed area)
    area = 0.0
    m = len(raw_pts)
    for i in range(m):
        x1, y1 = raw_pts[i]
        x2, y2 = raw_pts[(i + 1) % m]
        area += (x1 * y2 - x2 * y1)
    pts = list(raw_pts) if area >= 0 else list(reversed(raw_pts))

    # Compute cumulative arc lengths around closed loop
    closed = pts + [pts[0]]
    cum = [0.0]
    for i in range(len(pts)):
        d = math.hypot(closed[i + 1][0] - closed[i][0], closed[i + 1][1] - closed[i][1])
        cum.append(cum[-1] + d)
    total = cum[-1]
    if total < 1e-6:
        return [[round(pts[0][0], 1), round(pts[0][1], 1)]] * n

    out = []
    seg = 0
    for k in range(n):
        target = (k / n) * total
        while seg < len(pts) - 1 and cum[seg + 1] < target:
            seg += 1
        seg_len = cum[seg + 1] - cum[seg]
        u = 0.0 if seg_len < 1e-9 else (target - cum[seg]) / seg_len
        x = closed[seg][0] + (closed[seg + 1][0] - closed[seg][0]) * u
        y = closed[seg][1] + (closed[seg + 1][1] - closed[seg][1]) * u
        out.append((x, y))

    # Align index 0 to the topmost (minimum y, tie-break closest to center x) so shapes never twist!
    top_idx = min(range(n), key=lambda i: (out[i][1], abs(out[i][0] - 128.0)))
    aligned = out[top_idx:] + out[:top_idx]
    return [[round(p[0], 1), round(p[1], 1)] for p in aligned]


def collapsed_ring(cx=128.0, cy=128.0, r=0.05, n=N_PTS):
    """Tiny vanished circle at (cx, cy) so contour count matches cleanly (3 contours per mark)."""
    return [[round(cx + r * math.cos(-math.pi / 2 + 2 * math.pi * i / n), 1),
             round(cy + r * math.sin(-math.pi / 2 + 2 * math.pi * i / n), 1)] for i in range(n)]


def circle_intersections(x0, y0, r0, x1, y1, r1):
    dx, dy = x1 - x0, y1 - y0
    d = math.hypot(dx, dy)
    a = (r0**2 - r1**2 + d**2) / (2 * d)
    h = math.sqrt(max(0.0, r0**2 - a**2))
    xm, ym = x0 + a * dx / d, y0 + a * dy / d
    rx, ry = -dy * (h / d), dx * (h / d)
    p1, p2 = (xm + rx, ym + ry), (xm - rx, ym - ry)
    return (p1, p2) if p1[1] < p2[1] else (p2, p1)


def sample_tri_phase_contours():
    cx, cy, R, d_c, R_c, gap = 128.0, 128.0, 102.0, 62.0, 132.0, 19.0
    R_core = R_c - gap
    # Left crescent
    lt, lb = circle_intersections(cx, cy, R, cx + d_c, cy, R_c)
    left_raw = (
        sample_arc_circle(cx, cy, R, math.atan2(lt[1] - cy, lt[0] - cx), math.atan2(lb[1] - cy, lb[0] - cx), ccw=True, steps=40)
        + sample_arc_circle(cx + d_c, cy, R_c, math.atan2(lb[1] - cy, lb[0] - (cx + d_c)), math.atan2(lt[1] - cy, lt[0] - (cx + d_c)), ccw=False, steps=40)
    )
    # Center vesica core
    ct, cb = circle_intersections(cx + d_c, cy, R_core, cx - d_c, cy, R_core)
    core_raw = (
        sample_arc_circle(cx + d_c, cy, R_core, math.atan2(ct[1] - cy, ct[0] - (cx + d_c)), math.atan2(cb[1] - cy, cb[0] - (cx + d_c)), ccw=True, steps=40)
        + sample_arc_circle(cx - d_c, cy, R_core, math.atan2(cb[1] - cy, cb[0] - (cx - d_c)), math.atan2(ct[1] - cy, ct[0] - (cx - d_c)), ccw=True, steps=40)
    )
    # Right crescent
    rt, rb = circle_intersections(cx, cy, R, cx - d_c, cy, R_c)
    right_raw = (
        sample_arc_circle(cx, cy, R, math.atan2(rt[1] - cy, rt[0] - cx), math.atan2(rb[1] - cy, rb[0] - cx), ccw=False, steps=40)
        + sample_arc_circle(cx - d_c, cy, R_c, math.atan2(rb[1] - cy, rb[0] - (cx - d_c)), math.atan2(rt[1] - cy, rt[0] - (cx - d_c)), ccw=True, steps=40)
    )
    return [resample_closed(left_raw), resample_closed(core_raw), resample_closed(right_raw)]


def sample_eclipse_halo_contours():
    cx, cy, Ro, Ri = 128.0, 128.0, 98.0, 66.0
    ang = math.radians(-30.0)
    ix, iy = cx + 16.0 * math.cos(ang), cy + 16.0 * math.sin(ang)
    outer = resample_closed([(cx + Ro * math.cos(2 * math.pi * i / 96), cy + Ro * math.sin(2 * math.pi * i / 96)) for i in range(96)])
    inner = resample_closed([(ix + Ri * math.cos(2 * math.pi * i / 96), iy + Ri * math.sin(2 * math.pi * i / 96)) for i in range(96)])
    # Slot 0 = outer ring, Slot 1 = inner hole (evenodd carves it!), Slot 2 = collapsed dot at rim
    return [outer, inner, collapsed_ring(196.0, 128.0, 0.05)]


def sample_lunar_equinox_contours():
    R = 88.0
    # Upper dome at (140, 119)
    top_raw = (
        sample_arc_circle(140.0, 119.0, R, math.pi, 0.0, ccw=False, steps=48)
        + sample_line((140.0 + R, 119.0), (140.0 - R, 119.0), steps=24)
    )
    # Lower dome at (116, 137)
    bot_raw = (
        sample_arc_circle(116.0, 137.0, R, 0.0, math.pi, ccw=False, steps=48)
        + sample_line((116.0 - R, 137.0), (116.0 + R, 137.0), steps=24)
    )
    # Slot 0 = upper dome, Slot 1 = vanished center point, Slot 2 = lower dome
    return [resample_closed(top_raw), collapsed_ring(128.0, 128.0, 0.05), resample_closed(bot_raw)]


def sample_dual_phase_s_contours():
    # Upper S hook (exact coordinates from build_brand_mark_options.py)
    u = (
        sample_cubic((184, 62), (172, 34), (148, 22), (122, 22), 20)
        + sample_cubic((122, 22), (82, 22), (54, 48), (54, 84), 20)
        + sample_cubic((54, 84), (54, 112), (74, 130), (108, 142), 20)
        + sample_line((108, 142), (124, 118), 8)
        + sample_cubic((124, 118), (98, 108), (86, 96), (86, 80), 20)
        + sample_cubic((86, 80), (86, 58), (104, 42), (128, 42), 20)
        + sample_cubic((128, 42), (150, 42), (166, 52), (174, 68), 16)
        + sample_line((174, 68), (184, 62), 6)
    )
    # Lower S hook (exact 180° rotational mirror)
    l = [(256.0 - x, 256.0 - y) for (x, y) in u]
    return [resample_closed(u), collapsed_ring(128.0, 128.0, 0.05), resample_closed(l)]


def strip_svg_outer(path: Path) -> str:
    txt = path.read_text(encoding="utf-8").strip()
    txt = re.sub(r'<title[^>]*>.*?</title>\s*', "", txt, flags=re.S)
    m = re.search(r'<svg[^>]*>(.*)</svg>', txt, flags=re.S)
    inner = m.group(1).strip() if m else txt
    inner = re.sub(r'fill="#[0-9a-fA-F]{3,6}"', 'fill="currentColor"', inner)
    return inner


def load_svg_inline(path: Path, css_class: str = "", style: str = "") -> str:
    txt = path.read_text(encoding="utf-8").strip()
    txt = re.sub(r'\s+aria-labelledby="[^"]*"', "", txt)
    txt = re.sub(r'<title[^>]*>.*?</title>\s*', "", txt, flags=re.S)
    txt = re.sub(r'(<svg\b[^>]*?)\s+width="[^"]*"', r'\1', txt, count=1)
    txt = re.sub(r'(<svg\b[^>]*?)\s+height="[^"]*"', r'\1', txt, count=1)
    attrs = ""
    if css_class:
        attrs += f' class="{css_class}"'
    if style:
        attrs += f' style="{style}"'
    if attrs:
        txt = txt.replace("<svg ", f"<svg{attrs} ", 1)
    return txt


def kalla_signature_svg(color="#34332F", accent="#C8B9A6", height=18):
    width = round(height * (186.0 / 28.0), 1)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 186 28" width="{width}" height="{height}" class="kalla-svg" role="img" aria-label="by KALLA">
  <g fill="{accent}">
    <path d="M 6 4 L 8.2 4 L 8.2 24 L 6 24 Z"/>
    <path d="M 9.4 14 L 17.8 4 L 20.4 4 L 12.0 14 L 20.4 24 L 17.8 24 Z"/>
    <circle cx="2.2" cy="14" r="2.1"/>
  </g>
  <text x="30" y="18.5" fill="{color}" font-family="'DM Sans', sans-serif" font-size="10.5" letter-spacing="2.4" opacity="0.72">BY</text>
  <text x="54" y="19" fill="{color}" font-family="'Cormorant Garamond', Georgia, serif" font-size="18" font-weight="600" letter-spacing="4.2">KALLA</text>
</svg>'''


def build_website():
    marks_data = [
        {
            "id": "tri-phase",
            "badge": "Original",
            "name": "Tri-Phase Lunar",
            "subtitle": "Tiga fase bulan dalam satu lingkaran",
            "note": "Brand mark awal: tiga fase bulan harmonis dipahat lewat kanal negative space konsentris. Skor audit 100/100.",
            "svgInner": strip_svg_outer(SVG_DIR / "selunea-brand-mark-midnight-ash.svg"),
            "contours": sample_tri_phase_contours(),
            "dlMark": "05-logo-final/svg/selunea-brand-mark-midnight-ash.svg",
            "dlLockup": "05-logo-final/svg/selunea-horizontal-lockup-midnight-ash.svg",
        },
        {
            "id": "opt1",
            "badge": "Option 01",
            "name": "The Eclipse Halo",
            "subtitle": "Cincin gerhana kontinu poros 30°",
            "note": "Opsi 01: cincin gerhana utuh dengan lubang eksentrik pada poros 30° (senada aksen É). Minimalis & ultra-tenang. Skor 100/100.",
            "svgInner": strip_svg_outer(OPT_DIR / "mark-opt1-eclipse-halo.svg"),
            "contours": sample_eclipse_halo_contours(),
            "dlMark": "04-logo-concepts/brand-mark-options/mark-opt1-eclipse-halo.svg",
            "dlLockup": "04-logo-concepts/brand-mark-options/lockup-opt1-eclipse-halo.svg",
        },
        {
            "id": "opt2",
            "badge": "Option 02",
            "name": "The Lunar Equinox",
            "subtitle": "Horizon siang–malam bergeser halus",
            "note": "Opsi 02: dua belahan bulan bergeser lembut melintasi horizon negative space — modern, editorial, sangat tajam di 16 px. Skor 100/100.",
            "svgInner": strip_svg_outer(OPT_DIR / "mark-opt2-lunar-equinox.svg"),
            "contours": sample_lunar_equinox_contours(),
            "dlMark": "04-logo-concepts/brand-mark-options/mark-opt2-lunar-equinox.svg",
            "dlLockup": "04-logo-concepts/brand-mark-options/lockup-opt2-lunar-equinox.svg",
        },
        {
            "id": "opt4",
            "badge": "Option 04",
            "name": "The Dual-Phase S",
            "subtitle": "Inisial S dari dua fase bulan",
            "note": "Opsi 04: dua lengkung fase bulan yang membentuk inisial S dengan irisan cahaya 30° di tengah — langsung mengikat nama SELUNÉA.",
            "svgInner": strip_svg_outer(OPT_DIR / "mark-opt4-dual-phase-s.svg"),
            "contours": sample_dual_phase_s_contours(),
            "dlMark": "04-logo-concepts/brand-mark-options/mark-opt4-dual-phase-s.svg",
            "dlLockup": "04-logo-concepts/brand-mark-options/lockup-opt4-dual-phase-s.svg",
        },
    ]

    default_inner = marks_data[0]["svgInner"]

    wm_inner = strip_svg_outer(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg")
    wm_sm_inner = strip_svg_outer(SVG_DIR / "selunea-wordmark-small-responsive.svg")
    sec_ash = load_svg_inline(SVG_DIR / "selunea-secondary-skincare-midnight-ash.svg", css_class="arch-svg")
    mono_ash = load_svg_inline(SVG_DIR / "selunea-monogram-s-midnight-ash.svg", css_class="arch-svg-sq")
    wm_ash_arch = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", css_class="arch-svg")
    wm_white_arch = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", css_class="arch-svg")

    wm_nav = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", css_class="nav-wm")
    wm_hero = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", css_class="hero-wm")
    wm_footer = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", style="height:30px;width:auto;")
    wm_card = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:22px;width:auto;")
    wm_card_ch = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-champagne.svg", style="height:22px;width:auto;")

    divider_svg = load_svg_inline(GFX_DIR / "lunar-phase-divider.svg", css_class="gfx-divider")
    orbital_svg = load_svg_inline(GFX_DIR / "orbital-frame-accent.svg", css_class="gfx-sq")
    pattern_svg = load_svg_inline(GFX_DIR / "phase-pattern-tile.svg", css_class="gfx-sq-rad")
    pearl_svg = load_svg_inline(GFX_DIR / "pearl-luminosity-backdrop.svg", css_class="gfx-wide")

    kalla_light = kalla_signature_svg(color="#34332F", accent="#9F8B72", height=17)
    kalla_dark = kalla_signature_svg(color="#F3F0E9", accent="#C8B9A6", height=20)
    kalla_hero = kalla_signature_svg(color="#F3F0E9", accent="#C8B9A6", height=18)

    def live_mark_slot(extra_class="", size_style=""):
        return (
            f'<span class="morph-slot {extra_class}" style="{size_style}" data-live-mark>'
            f'<svg viewBox="0 0 256 256" class="morph-svg" aria-hidden="true">'
            f'<g class="exact-layer">{default_inner}</g>'
            f'<path class="tween-layer" fill="currentColor" fill-rule="evenodd" d="" style="display:none;"/>'
            f'</svg>'
            f'</span>'
        )

    selector_cards = []
    for i, m in enumerate(marks_data):
        active_cls = " active" if i == 0 else ""
        selector_cards.append(f"""
        <button type="button" class="mark-opt-btn{active_cls}" data-select-mark="{m['id']}" aria-pressed="{'true' if i == 0 else 'false'}">
          <span class="opt-mini-svg">
            <svg viewBox="0 0 256 256" aria-hidden="true">{m['svgInner']}</svg>
          </span>
          <span class="opt-mini-text">
            <small>{m['badge']}</small>
            <strong>{m['name']}</strong>
          </span>
        </button>""")

    marks_json = json.dumps(marks_data, ensure_ascii=False, separators=(",", ":"))

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>SELUNÉA — Interactive Brand Identity by KALLA</title>
<meta name="description" content="Interactive Brand Identity Showcase for SELUNÉA (Beauty in Every Phase) — Presented for NANA, designed by KALLA." />
<link id="dynamicFavicon" rel="icon" type="image/svg+xml" href="05-logo-final/web-icons/favicon.svg" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet" />
<style>
  :root {{
    --ivory: #F3F0E9;
    --ivory-card: #FAF8F4;
    --ivory-deep: #E8E2D7;
    --ash: #34332F;
    --ash-soft: #5B5953;
    --ash-deep: #242320;
    --champagne: #C8B9A6;
    --champagne-deep: #9F8B72;
    --silver: #B8B7B1;
    --sage: #D9DFD5;
    --lavender: #DCD9E2;
    --nude: #E4DAD0;
    --white: #FFFFFF;
    --line: rgba(52, 51, 47, 0.13);
    --line-dark: rgba(200, 185, 166, 0.24);
    --font-display: 'Cormorant Garamond', Georgia, serif;
    --font-sans: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    --radius-sm: 8px;
    --radius-md: 14px;
    --radius-lg: 20px;
    --container: 1200px;
    --nav-h: 60px;
    --ease-luxury: cubic-bezier(0.22, 1, 0.36, 1);
  }}

  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; scroll-padding-top: calc(var(--nav-h) + 18px); overflow-x: clip; }}
  body {{
    background: var(--ivory);
    color: var(--ash);
    font-family: var(--font-sans);
    font-size: 15px;
    line-height: 1.65;
    width: 100%; max-width: 100vw;
    overflow-x: clip;
    -webkit-font-smoothing: antialiased;
  }}
  img, svg {{ max-width: 100%; display: block; }}
  a {{ color: inherit; text-decoration: none; }}
  button {{ font-family: inherit; cursor: pointer; background: none; border: none; color: inherit; }}
  :focus-visible {{ outline: 2px solid var(--ash); outline-offset: 3px; border-radius: 4px; }}
  .dark-surface :focus-visible {{ outline-color: var(--champagne); }}

  section, header, footer, .wrap, .editorial-panel, .playground, .pg-stage, .board-feature,
  .hero-grid > *, .strategy-grid > *, .arch-grid > *, .gov-grid > *, .color-grid > *,
  .type-stack > *, .gfx-grid > *, .owner-spot > *, .boards-grid > *, .dl-grid > *, .footer-top > * {{
    min-width: 0;
  }}

  .wrap {{ width: 100%; max-width: var(--container); margin: 0 auto; padding: 0 20px; }}

  /* ---------------- SILKY 60FPS TRUE PATH MORPH ---------------- */
  .morph-slot {{
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 64px; height: 64px;
    flex-shrink: 0;
    color: currentColor;
  }}
  .morph-svg {{
    width: 100%; height: 100%;
    overflow: visible;
    transform-origin: center center;
  }}
  .studio-note {{
    transition: opacity 220ms ease, transform 220ms var(--ease-luxury);
  }}
  .studio-note.is-fading {{
    opacity: 0;
    transform: translateY(4px);
  }}

  /* One-shot Editorial Scroll Reveal */
  .reveal {{
    opacity: 0;
    transform: translateY(18px);
    transition: opacity 620ms var(--ease-luxury), transform 620ms var(--ease-luxury);
  }}
  .reveal.in-view {{ opacity: 1; transform: translateY(0); }}
  @media (prefers-reduced-motion: reduce) {{
    .reveal, .studio-note {{ transition: none !important; opacity: 1 !important; transform: none !important; }}
  }}

  /* ---------------- STICKY NAVIGATION ---------------- */
  .topbar {{
    position: sticky; top: 0; z-index: 60;
    height: var(--nav-h);
    background: rgba(243, 240, 233, 0.94);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--line);
  }}
  .topbar-inner {{ height: 100%; display: flex; align-items: center; justify-content: space-between; gap: 12px; }}
  .brand-lock {{ display: flex; align-items: center; gap: 10px; min-width: 0; }}
  .nav-live-mark {{ width: 24px; height: 24px; color: var(--ash); }}
  .nav-wm {{ height: 21px; width: auto; flex-shrink: 0; }}
  .nav-sep {{ width: 1px; height: 18px; background: var(--line); display: none; }}
  .nav-kalla {{ display: none; align-items: center; }}

  .nav-links {{ display: none; align-items: center; gap: 4px; }}
  .nav-links a {{ font-size: 12.5px; letter-spacing: 0.05em; color: var(--ash-soft); padding: 10px 11px; border-radius: 8px; transition: color 0.18s, background 0.18s; }}
  .nav-links a:hover {{ color: var(--ash); background: rgba(52,51,47,0.06); }}

  .nav-actions {{ display: flex; align-items: center; gap: 8px; }}
  .btn-pdf-sm {{ display: none; font-size: 11px; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; padding: 10px 16px; border-radius: 999px; background: var(--ash); color: var(--ivory); min-height: 40px; align-items: center; }}
  .btn-pdf-sm:hover {{ background: var(--ash-deep); }}

  .menu-toggle {{ display: inline-flex; align-items: center; gap: 8px; min-height: 44px; min-width: 44px; padding: 0 14px; border: 1px solid var(--line); border-radius: 999px; background: var(--ivory-card); font-size: 12px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }}

  /* Mobile Drawer */
  .mobile-drawer {{ display: none; position: fixed; inset: var(--nav-h) 0 0 0; z-index: 55; background: rgba(243, 240, 233, 0.98); padding: 20px 20px 36px; overflow-y: auto; border-top: 1px solid var(--line); }}
  .mobile-drawer.open {{ display: flex; flex-direction: column; justify-content: space-between; gap: 24px; }}
  .drawer-nav {{ display: flex; flex-direction: column; gap: 4px; }}
  .drawer-nav a {{ display: flex; align-items: center; justify-content: space-between; min-height: 48px; padding: 12px 14px; border-bottom: 1px solid var(--line); font-family: var(--font-display); font-size: 24px; font-weight: 500; }}
  .drawer-nav a span.num {{ font-family: var(--font-sans); font-size: 11px; letter-spacing: 0.16em; color: var(--ash-soft); }}
  .drawer-foot {{ padding-top: 16px; display: flex; flex-direction: column; gap: 14px; }}

  /* ---------------- HERO + INTERACTIVE BRAND MARK STUDIO ---------------- */
  .hero {{ background: var(--ash); color: var(--ivory); padding: 44px 0 56px; position: relative; }}
  .hero-grid {{ display: grid; grid-template-columns: 1fr; gap: 32px; align-items: center; }}
  .hero-kicker {{ font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--champagne); margin-bottom: 16px; }}
  .hero-brand-stack {{ display: flex; flex-direction: column; align-items: flex-start; gap: 14px; margin-bottom: 18px; }}
  .hero-mark-slot {{ width: 64px; height: 64px; color: var(--champagne); }}
  .hero-wm {{ height: clamp(40px, 11vw, 66px); width: auto; max-width: 100%; margin-left: -10px; }}
  .hero-quote {{ font-family: var(--font-display); font-style: italic; font-weight: 400; font-size: clamp(26px, 5vw, 38px); line-height: 1.18; color: var(--champagne); margin-bottom: 12px; }}
  .hero-sub {{ font-size: 14.5px; color: rgba(243, 240, 233, 0.78); max-width: 520px; margin-bottom: 24px; }}
  .hero-meta-bar {{ display: grid; grid-template-columns: 1fr; gap: 14px; padding-top: 20px; border-top: 1px solid var(--line-dark); }}
  .meta-item small {{ display: block; font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(243, 240, 233, 0.56); margin-bottom: 4px; }}
  .meta-item strong {{ font-size: 13.5px; font-weight: 500; color: var(--ivory); }}

  .studio-panel {{ background: rgba(243, 240, 233, 0.055); border: 1px solid var(--line-dark); border-radius: var(--radius-lg); padding: 22px; }}
  .studio-head {{ display: flex; justify-content: space-between; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 16px; }}
  .studio-label {{ font-size: 10.5px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--champagne); }}
  .studio-active-pill {{ font-size: 11px; color: var(--ivory); background: rgba(200,185,166,0.16); border: 1px solid var(--line-dark); padding: 4px 11px; border-radius: 999px; }}

  .morph-preview-box {{
    background: var(--ivory); color: var(--ash); border-radius: var(--radius-md);
    padding: 28px 20px 22px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px;
    margin-bottom: 16px;
  }}
  .morph-hero-pair {{ display: flex; align-items: center; justify-content: center; gap: 18px; flex-wrap: wrap; }}
  .studio-big-mark {{ width: 78px; height: 78px; color: var(--ash); }}
  .studio-pair-wm {{ height: 34px; width: auto; color: var(--ash); }}
  .studio-note {{ font-size: 12px; color: var(--ash-soft); text-align: center; max-width: 420px; line-height: 1.5; min-height: 36px; }}

  .mark-options-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 14px; }}
  .mark-opt-btn {{
    display: flex; align-items: center; gap: 10px; text-align: left;
    min-height: 58px; padding: 10px 12px; border-radius: 12px;
    background: rgba(243, 240, 233, 0.05); border: 1px solid rgba(200, 185, 166, 0.2); color: var(--ivory);
    transition: background 0.24s var(--ease-luxury), border-color 0.24s var(--ease-luxury), transform 0.18s var(--ease-luxury);
  }}
  .mark-opt-btn:hover {{ background: rgba(243, 240, 233, 0.1); border-color: var(--champagne); }}
  .mark-opt-btn:active {{ transform: scale(0.98); }}
  .mark-opt-btn.active {{ background: var(--ivory); color: var(--ash); border-color: var(--ivory); box-shadow: 0 8px 20px rgba(0,0,0,0.22); }}
  .opt-mini-svg {{ width: 34px; height: 34px; border-radius: 8px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; padding: 5px; background: rgba(243,240,233,0.08); }}
  .mark-opt-btn.active .opt-mini-svg {{ background: rgba(52,51,47,0.08); }}
  .opt-mini-svg svg {{ width: 100%; height: 100%; }}
  .opt-mini-text small {{ display: block; font-size: 9.5px; letter-spacing: 0.14em; text-transform: uppercase; opacity: 0.68; line-height: 1.2; margin-bottom: 2px; }}
  .opt-mini-text strong {{ display: block; font-size: 12.5px; font-weight: 500; line-height: 1.2; }}

  .studio-actions {{ display: flex; flex-direction: column; gap: 8px; align-items: center; }}
  .btn-confirm-choice {{
    display: inline-flex; align-items: center; justify-content: center; gap: 8px;
    width: 100%; min-height: 44px; padding: 0 18px; border-radius: 999px;
    background: var(--champagne); color: var(--ash-deep);
    font-size: 11.5px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase;
    transition: background 0.18s, transform 0.15s;
  }}
  .btn-confirm-choice:hover {{ background: #D7C9B7; }}
  .btn-confirm-choice:active {{ transform: scale(0.98); }}
  .studio-helper {{ font-size: 11px; color: rgba(243,240,233,0.62); text-align: center; line-height: 1.45; }}

  /* Floating Quick Switcher */
  .floating-bar {{
    position: fixed; bottom: 16px; left: 50%; z-index: 50;
    transform: translateX(-50%) translateY(96px); opacity: 0; pointer-events: none;
    background: rgba(36, 35, 32, 0.94); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--line-dark); border-radius: 999px; padding: 6px 8px;
    display: flex; align-items: center; gap: 6px; box-shadow: 0 14px 36px rgba(0,0,0,0.28);
    transition: transform 360ms var(--ease-luxury), opacity 280ms ease; max-width: calc(100vw - 24px);
  }}
  .floating-bar.visible {{ transform: translateX(-50%) translateY(0); opacity: 1; pointer-events: auto; }}
  .fb-label {{ display: none; font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--champagne); padding: 0 10px 0 12px; white-space: nowrap; }}
  .fb-btn {{ min-width: 44px; min-height: 44px; padding: 0 10px; border-radius: 999px; display: inline-flex; align-items: center; justify-content: center; gap: 6px; color: rgba(243,240,233,0.75); font-size: 11px; font-weight: 500; transition: background 0.2s, color 0.2s; }}
  .fb-btn svg {{ width: 20px; height: 20px; flex-shrink: 0; }}
  .fb-btn span {{ display: none; }}
  .fb-btn.active {{ background: var(--ivory); color: var(--ash); }}

  /* ---------------- SHARED SECTIONS ---------------- */
  .section {{ padding: 56px 0; border-bottom: 1px solid var(--line); }}
  .section-alt {{ background: var(--ivory-card); }}
  .section-head {{ display: grid; grid-template-columns: 1fr; gap: 14px; margin-bottom: 32px; }}
  .sec-num {{ font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--champagne-deep); margin-bottom: 8px; }}
  .sec-h2 {{ font-family: var(--font-display); font-weight: 500; font-size: clamp(30px, 5vw, 46px); line-height: 1.08; }}
  .sec-h2 em {{ font-style: italic; font-weight: 400; }}
  .sec-desc {{ font-size: 14.5px; color: var(--ash-soft); max-width: 600px; }}

  /* ---------------- 01. STRATEGY ---------------- */
  .strategy-grid {{ display: grid; grid-template-columns: 1fr; gap: 20px; }}
  .editorial-panel {{ background: var(--ivory-card); border: 1px solid var(--line); border-radius: var(--radius-md); padding: 24px; }}
  .section-alt .editorial-panel {{ background: var(--ivory); }}
  .panel-label {{ font-size: 10.5px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--ash-soft); margin-bottom: 12px; }}
  .pillar-list {{ list-style: none; display: grid; gap: 10px; margin-top: 12px; }}
  .pillar-list li {{ padding-left: 16px; position: relative; font-size: 14px; color: var(--ash-soft); }}
  .pillar-list li::before {{ content: ''; position: absolute; left: 0; top: 10px; width: 6px; height: 1px; background: var(--champagne-deep); }}
  .pillar-list li b {{ color: var(--ash); font-weight: 500; }}
  .personality-tags {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }}
  .tag-soft {{ font-size: 12px; padding: 6px 12px; border-radius: 6px; background: var(--ivory); border: 1px solid var(--line); color: var(--ash); }}

  /* ---------------- 02. LOGO ARCHITECTURE ---------------- */
  .playground {{ border: 1px solid var(--line); border-radius: var(--radius-md); overflow: hidden; margin-bottom: 28px; }}
  .pg-stage {{
    min-height: 230px; padding: 40px 24px;
    display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 18px;
    transition: background-color 380ms var(--ease-luxury), color 380ms var(--ease-luxury);
    background: var(--ivory); color: var(--ash);
  }}
  .pg-lockup-live {{ display: flex; align-items: center; justify-content: center; gap: 20px; flex-wrap: wrap; }}
  .pg-mark-live {{ width: clamp(52px, 11vw, 72px); height: clamp(52px, 11vw, 72px); }}
  .pg-wm-live {{ height: clamp(34px, 7.5vw, 52px); width: auto; }}
  .pg-caption {{ font-size: 11.5px; letter-spacing: 0.1em; text-transform: uppercase; opacity: 0.72; text-align: center; }}
  .pg-controls {{ background: var(--white); border-top: 1px solid var(--line); padding: 14px 16px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px; }}
  .pg-swatches {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .surface-btn {{ display: inline-flex; align-items: center; gap: 8px; min-height: 44px; padding: 0 14px; border-radius: 8px; border: 1px solid var(--line); font-size: 12px; font-weight: 500; background: var(--ivory-card); transition: border-color 0.18s, background 0.18s; }}
  .surface-btn.active {{ border-color: var(--ash); background: var(--ivory); box-shadow: inset 0 0 0 1px var(--ash); }}
  .sw-chip {{ width: 14px; height: 14px; border-radius: 50%; border: 1px solid rgba(52,51,47,0.22); flex-shrink: 0; }}

  .arch-grid {{ display: grid; grid-template-columns: 1fr; gap: 16px; margin-bottom: 24px; }}
  .arch-card {{ background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); padding: 24px 20px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 18px; min-width: 0; }}
  .arch-card.dark {{ background: var(--ash); border-color: var(--ash); color: var(--ivory); }}
  .arch-stage {{ min-height: 108px; display: flex; align-items: center; justify-content: center; }}
  .arch-svg {{ max-height: 52px; width: auto; }}
  .arch-svg-sq {{ width: 76px; height: 76px; }}
  .live-hlock {{ display: flex; align-items: center; gap: 12px; }}
  .live-hlock .morph-slot {{ width: 42px; height: 42px; }}
  .live-hlock .hlock-wm {{ height: 26px; width: auto; }}
  .live-slock {{ display: flex; flex-direction: column; align-items: center; gap: 10px; }}
  .live-slock .morph-slot {{ width: 48px; height: 48px; }}
  .live-slock .slock-wm {{ height: 26px; width: auto; }}
  .app-icon-tile {{ width: 78px; height: 78px; border-radius: 18px; background: var(--ash); color: var(--ivory); display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 22px rgba(52,51,47,0.16); }}
  .app-icon-tile .morph-slot {{ width: 48px; height: 48px; }}

  .arch-meta {{ display: flex; justify-content: space-between; align-items: flex-end; gap: 10px; padding-top: 12px; border-top: 1px solid var(--line); }}
  .arch-card.dark .arch-meta {{ border-color: var(--line-dark); }}
  .arch-meta strong {{ display: block; font-size: 13px; font-weight: 500; }}
  .arch-meta span {{ font-size: 11.5px; color: var(--ash-soft); }}
  .arch-card.dark .arch-meta span {{ color: rgba(243,240,233,0.68); }}
  .dl-link {{ font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; font-weight: 500; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--line); min-height: 36px; display: inline-flex; align-items: center; white-space: nowrap; }}
  .arch-card.dark .dl-link {{ border-color: var(--line-dark); color: var(--champagne); }}

  /* ---------------- 03. COLOR, TYPE & GRAPHICS ---------------- */
  .prop-bar {{ display: flex; height: 40px; border-radius: var(--radius-sm); overflow: hidden; border: 1px solid var(--line); margin-bottom: 24px; font-size: 11px; font-weight: 500; }}
  .prop-seg {{ display: flex; align-items: center; justify-content: center; overflow: hidden; white-space: nowrap; }}
  .color-grid {{ display: grid; grid-template-columns: 1fr; gap: 14px; margin-bottom: 24px; }}
  .swatch-btn {{ text-align: left; width: 100%; background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); overflow: hidden; transition: transform 0.18s var(--ease-luxury), border-color 0.18s; }}
  .swatch-btn:hover {{ border-color: var(--ash); transform: translateY(-2px); }}
  .swatch-head {{ height: 92px; padding: 14px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10.5px; letter-spacing: 0.12em; text-transform: uppercase; font-weight: 500; }}
  .swatch-body {{ padding: 14px 16px; }}
  .swatch-body strong {{ display: block; font-size: 14.5px; margin-bottom: 4px; }}
  .swatch-code {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 11.5px; color: var(--ash-soft); display: block; line-height: 1.5; }}

  .type-stack {{ display: grid; grid-template-columns: 1fr; gap: 14px; margin-bottom: 28px; }}
  .type-item {{ background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); padding: 20px 22px; display: grid; grid-template-columns: 1fr; gap: 12px; align-items: center; }}
  .type-role small {{ display: block; font-size: 10.5px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--champagne-deep); margin-bottom: 3px; }}
  .type-role span {{ font-size: 12px; color: var(--ash-soft); }}

  .gfx-grid {{ display: grid; grid-template-columns: 1fr; gap: 16px; }}
  .gfx-card {{ background: var(--ivory); border: 1px solid var(--line); border-radius: var(--radius-md); padding: 22px 18px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 14px; }}
  .gfx-stage {{ height: 132px; width: 100%; display: flex; align-items: center; justify-content: center; }}
  .gfx-divider {{ width: 100%; max-width: 320px; height: auto; }}
  .gfx-sq {{ width: 124px; height: 124px; }}
  .gfx-sq-rad {{ width: 124px; height: 124px; border-radius: 8px; border: 1px solid var(--line); }}
  .gfx-wide {{ width: 100%; height: 124px; object-fit: cover; border-radius: 8px; border: 1px solid var(--line); }}
  .gfx-card h3 {{ font-size: 13.5px; font-weight: 500; }}
  .gfx-card p {{ font-size: 12px; color: var(--ash-soft); }}

  /* ---------------- 04. LIVE MORPHING 5-SKU PACKAGING SHELF ---------------- */
  .live-shelf-wrap {{
    background: linear-gradient(180deg, #FAF8F4 0%, #EFECE4 74%, #E6E0D5 74.2%, #DDD5C7 100%);
    border: 1px solid var(--line); border-radius: var(--radius-lg);
    padding: 28px 18px 26px; margin-bottom: 24px; overflow-x: auto; -webkit-overflow-scrolling: touch;
  }}
  .live-shelf-head {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; font-size: 10.5px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--ash-soft); margin-bottom: 24px; }}
  .live-shelf-row {{ display: grid; grid-template-columns: repeat(5, minmax(150px, 1fr)); gap: 18px; align-items: end; min-width: 820px; }}
  .v-col {{ display: flex; flex-direction: column; align-items: center; }}
  .v-stage {{ height: 300px; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; }}
  .v-fop {{ display: flex; flex-direction: column; align-items: center; justify-content: space-between; text-align: center; width: 100%; height: 100%; padding: 16px 10px 14px; color: var(--ash); }}
  .v-top {{ display: flex; flex-direction: column; align-items: center; gap: 5px; width: 100%; }}
  .v-mark {{ width: 22px; height: 22px; color: var(--ash); }}
  .v-wm {{ width: 66%; height: auto; color: var(--ash); }}
  .v-cat {{ font-size: 7.5px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--ash-soft); }}
  .v-name {{ font-family: var(--font-display); font-size: 18px; font-weight: 500; line-height: 1.05; }}
  .v-band {{ height: 5px; width: 30px; border-radius: 99px; margin: 4px auto 0; }}
  .v-net {{ font-size: 7.5px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--ash-soft); }}
  .v-label {{ margin-top: 14px; text-align: center; }}
  .v-label strong {{ display: block; font-size: 12.5px; font-weight: 500; }}
  .v-label span {{ font-size: 10.5px; color: var(--ash-soft); }}
  .v-shadow {{ width: 96px; height: 11px; border-radius: 50%; background: radial-gradient(ellipse, rgba(52,51,47,0.22) 0%, transparent 72%); margin-top: -4px; }}

  .v-tube {{ width: 108px; height: 228px; background: linear-gradient(90deg,#E8E3D8,#F7F5EF 30%,#F3F0E9 66%,#DED8CC); border-radius: 7px 7px 22px 22px; border: 1px solid rgba(52,51,47,0.12); overflow: hidden; box-shadow: inset 6px 0 12px rgba(255,255,255,0.6), 0 10px 20px rgba(52,51,47,0.09); }}
  .v-tube-cap {{ width: 60px; height: 32px; background: linear-gradient(90deg,#DDD7CB,#F3F0E9 35%,#CFC8BB); border: 1px solid rgba(52,51,47,0.14); border-top: none; border-radius: 0 0 7px 7px; }}
  .v-toner-cap {{ width: 48px; height: 38px; background: linear-gradient(90deg,#9C9B95,#D5D4CE 32%,#B8B7B1 68%,#8F8E88); border-radius: 5px 5px 2px 2px; border: 1px solid rgba(52,51,47,0.15); }}
  .v-toner {{ width: 100px; height: 234px; background: linear-gradient(90deg,rgba(226,225,222,0.9),rgba(253,252,250,0.96) 30%,rgba(240,238,242,0.92) 68%,rgba(210,208,212,0.88)); border-radius: 22px 22px 10px 10px; border: 1px solid rgba(255,255,255,0.9); box-shadow: inset 8px 0 14px rgba(255,255,255,0.85), 0 12px 22px rgba(52,51,47,0.1); }}
  .v-bulb {{ width: 28px; height: 38px; background: linear-gradient(90deg,#E2DDD2,#FAF8F4 38%,#D4CEC2); border-radius: 14px 14px 3px 3px; border: 1px solid rgba(52,51,47,0.12); }}
  .v-collar {{ width: 44px; height: 19px; background: linear-gradient(90deg,#AF9E89,#DFD3C3 34%,#C8B9A6 68%,#A18F7A); border-radius: 2px; border: 1px solid rgba(52,51,47,0.14); }}
  .v-serum {{ width: 94px; height: 170px; background: linear-gradient(90deg,rgba(226,223,229,0.92),rgba(255,254,252,0.96) 28%,rgba(241,238,244,0.92) 68%,rgba(212,208,218,0.88)); border-radius: 20px 20px 8px 8px; border: 1px solid rgba(255,255,255,0.9); box-shadow: inset 8px 0 14px rgba(255,255,255,0.85), 0 10px 20px rgba(52,51,47,0.1); }}
  .v-jar-lid {{ width: 132px; height: 28px; background: linear-gradient(90deg,#B9A995,#DED2C3 30%,#C8B9A6 66%,#A99883); border-radius: 8px 8px 2px 2px; border: 1px solid rgba(52,51,47,0.14); }}
  .v-jar {{ width: 136px; height: 118px; background: linear-gradient(90deg,#E2DAD0,#FAF7F3 30%,#F1EAE2 68%,#D7CCC0); border-radius: 4px 4px 18px 18px; border: 1px solid rgba(255,255,255,0.85); box-shadow: inset 10px 0 16px rgba(255,255,255,0.75), 0 12px 20px rgba(52,51,47,0.1); }}
  .v-spf {{ width: 102px; height: 186px; background: linear-gradient(90deg,#E8DFD5,#F7F4EE 30%,#F3F0E9 68%,#DFD5C9); border-radius: 14px 14px 24px 24px; border: 1px solid rgba(52,51,47,0.12); overflow: hidden; box-shadow: inset 6px 0 12px rgba(255,255,255,0.65), 0 10px 18px rgba(52,51,47,0.09); }}
  .v-spf-cap {{ width: 58px; height: 30px; background: linear-gradient(90deg,#B9A995,#DED2C3 35%,#C8B9A6 70%,#A99883); border-radius: 0 0 8px 8px; border: 1px solid rgba(52,51,47,0.14); border-top: none; }}

  /* ---------------- 05. APPLICATIONS & BOARDS ---------------- */
  .owner-spot {{ display: grid; grid-template-columns: 1fr; gap: 18px; margin-bottom: 24px; }}
  .bcard-live {{ border-radius: 10px; padding: 24px; min-height: 196px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 12px 24px rgba(52,51,47,0.08); }}
  .bcard-live.ivory {{ background: var(--ivory); border: 1px solid var(--line); }}
  .bcard-live.ash {{ background: var(--ash); color: var(--ivory); align-items: center; justify-content: center; gap: 12px; text-align: center; }}

  .board-feature {{ background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); overflow: hidden; margin-bottom: 20px; }}
  .board-trigger {{ display: block; width: 100%; text-align: left; padding: 0; }}
  .board-trigger img {{ width: 100%; height: auto; display: block; }}
  .board-bar {{ padding: 14px 18px; border-top: 1px solid var(--line); display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 10px; background: var(--ivory-card); }}
  .board-bar strong {{ font-size: 13.5px; font-weight: 500; }}
  .board-bar span {{ font-size: 12px; color: var(--ash-soft); }}
  .zoom-pill {{ font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; font-weight: 500; padding: 8px 14px; border-radius: 999px; border: 1px solid var(--line); background: var(--white); min-height: 38px; display: inline-flex; align-items: center; }}

  .boards-grid {{ display: grid; grid-template-columns: 1fr; gap: 18px; }}
  .board-thumb {{ background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); overflow: hidden; display: flex; flex-direction: column; }}
  .board-thumb-img {{ aspect-ratio: 16 / 11; overflow: hidden; background: var(--ivory); border-bottom: 1px solid var(--line); }}
  .board-thumb-img img {{ width: 100%; height: 100%; object-fit: cover; object-position: top center; transition: transform 0.35s var(--ease-luxury); }}
  .board-thumb:hover .board-thumb-img img {{ transform: scale(1.02); }}
  .board-thumb-meta {{ padding: 16px 18px; display: flex; justify-content: space-between; align-items: center; gap: 12px; }}
  .board-thumb-meta strong {{ display: block; font-size: 13.5px; font-weight: 500; }}
  .board-thumb-meta span {{ font-size: 11.5px; color: var(--ash-soft); }}

  .dl-grid {{ display: grid; grid-template-columns: 1fr; gap: 14px; }}
  .dl-card {{ background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); padding: 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 14px; }}
  .dl-card strong {{ font-size: 15px; display: block; margin-bottom: 4px; }}
  .dl-card p {{ font-size: 12.5px; color: var(--ash-soft); }}
  .dl-btn-row {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .btn-dark-sm {{ display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 18px; border-radius: 999px; background: var(--ash); color: var(--ivory); font-size: 11.5px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }}
  .btn-light-sm {{ display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 16px; border-radius: 999px; border: 1px solid var(--line); background: var(--ivory-card); color: var(--ash); font-size: 11.5px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }}

  /* ---------------- FOOTER ---------------- */
  .footer {{ background: var(--ash); color: var(--ivory); padding: 52px 0 92px; }}
  .footer-top {{ display: grid; grid-template-columns: 1fr; gap: 28px; padding-bottom: 32px; border-bottom: 1px solid var(--line-dark); }}
  .footer-quote {{ font-family: var(--font-display); font-style: italic; font-size: 24px; color: var(--champagne); margin-top: 12px; }}
  .footer-col h4 {{ font-size: 10.5px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--champagne); margin-bottom: 12px; }}
  .footer-col p, .footer-col a {{ font-size: 13px; color: rgba(243,240,233,0.74); line-height: 1.8; display: block; }}
  .footer-bot {{ padding-top: 24px; display: flex; flex-direction: column; gap: 16px; align-items: flex-start; justify-content: space-between; font-size: 12px; color: rgba(243,240,233,0.62); }}
  .kalla-badge {{ display: inline-flex; align-items: center; gap: 10px; padding: 10px 16px; border-radius: 999px; border: 1px solid var(--line-dark); background: rgba(243,240,233,0.04); }}

  /* Lightbox & Toast */
  .lightbox {{ display: none; position: fixed; inset: 0; z-index: 100; background: rgba(28, 27, 24, 0.94); padding: 16px; flex-direction: column; align-items: center; justify-content: center; gap: 14px; }}
  .lightbox.open {{ display: flex; }}
  .lb-bar {{ width: 100%; max-width: 1280px; display: flex; justify-content: space-between; align-items: center; gap: 12px; color: var(--ivory); }}
  .lb-title {{ font-size: 13px; letter-spacing: 0.08em; }}
  .lb-close {{ min-width: 44px; min-height: 44px; padding: 0 18px; border-radius: 999px; border: 1px solid var(--line-dark); color: var(--ivory); font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; }}
  .lb-img-wrap {{ max-width: 1280px; max-height: calc(100dvh - 104px); overflow: auto; border-radius: 10px; background: var(--ivory); }}
  .lb-img-wrap img {{ width: auto; max-width: 100%; height: auto; max-height: calc(100dvh - 108px); object-fit: contain; }}

  .toast {{
    position: fixed; bottom: 78px; left: 50%; transform: translateX(-50%) translateY(14px);
    background: var(--ash-deep); color: var(--ivory); border: 1px solid var(--champagne);
    padding: 10px 18px; border-radius: 999px; font-size: 12.5px; letter-spacing: 0.05em;
    opacity: 0; pointer-events: none; transition: opacity 0.22s, transform 0.22s var(--ease-luxury); z-index: 95;
    white-space: nowrap; max-width: calc(100vw - 32px); overflow: hidden; text-overflow: ellipsis;
  }}
  .toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}

  /* ---------------- TABLET (>= 640px) ---------------- */
  @media (min-width: 640px) {{
    .wrap {{ padding: 0 32px; }}
    .nav-sep, .nav-kalla {{ display: flex; }}
    .hero-meta-bar {{ grid-template-columns: repeat(3, 1fr); }}
    .strategy-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .arch-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .color-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .gfx-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .owner-spot {{ grid-template-columns: repeat(2, 1fr); }}
    .boards-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .dl-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .type-item {{ grid-template-columns: 200px 1fr; }}
    .footer-top {{ grid-template-columns: 1.4fr 1fr 1fr; }}
    .footer-bot {{ flex-direction: row; align-items: center; }}
    .fb-label {{ display: inline; }}
    .fb-btn {{ padding: 0 14px; }}
    .fb-btn span {{ display: inline; }}
  }}

  /* ---------------- DESKTOP (>= 1024px) ---------------- */
  @media (min-width: 1024px) {{
    :root {{ --nav-h: 68px; }}
    .wrap {{ padding: 0 40px; }}
    .nav-links {{ display: flex; }}
    .btn-pdf-sm {{ display: inline-flex; }}
    .menu-toggle {{ display: none; }}
    .hero {{ padding: 68px 0 76px; }}
    .hero-grid {{ grid-template-columns: 0.96fr 1.04fr; gap: 48px; }}
    .section {{ padding: 84px 0; }}
    .section-head {{ grid-template-columns: 1fr 1fr; align-items: end; gap: 36px; margin-bottom: 44px; }}
    .strategy-grid {{ grid-template-columns: 1.2fr 1fr 1fr; }}
    .arch-grid {{ grid-template-columns: repeat(4, 1fr); }}
    .color-grid {{ grid-template-columns: repeat(4, 1fr); }}
    .color-grid.sku-3 {{ grid-template-columns: repeat(3, 1fr); }}
    .gfx-grid {{ grid-template-columns: repeat(4, 1fr); }}
    .boards-grid {{ grid-template-columns: repeat(3, 1fr); }}
    .dl-grid {{ grid-template-columns: repeat(3, 1fr); }}
  }}
</style>
</head>
<body>

  <!-- STICKY HEADER -->
  <header class="topbar">
    <div class="wrap topbar-inner">
      <a href="#top" class="brand-lock" aria-label="SELUNÉA Home">
        {live_mark_slot("nav-live-mark")}
        {wm_nav}
        <span class="nav-sep" aria-hidden="true"></span>
        <span class="nav-kalla">{kalla_light}</span>
      </a>

      <nav class="nav-links" aria-label="Navigasi Utama">
        <a href="#strategy">Strategy</a>
        <a href="#logo-system">Logo</a>
        <a href="#color-type">Color &amp; Type</a>
        <a href="#packaging">Packaging</a>
        <a href="#applications">Applications</a>
        <a href="#boards">All Boards</a>
      </nav>

      <div class="nav-actions">
        <a href="10-brand-guidelines/selunea-brand-guidelines.pdf" target="_blank" class="btn-pdf-sm">Brand Book PDF</a>
        <button type="button" class="menu-toggle" id="menuBtn" aria-expanded="false" aria-controls="mobileDrawer">
          <span>Menu</span>
          <svg width="16" height="12" viewBox="0 0 16 12" fill="none" aria-hidden="true">
            <path d="M1 1.5H15M1 6H15M1 10.5H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
        </button>
      </div>
    </div>
  </header>

  <!-- MOBILE DRAWER -->
  <div class="mobile-drawer" id="mobileDrawer" aria-hidden="true">
    <nav class="drawer-nav" aria-label="Navigasi Mobile">
      <a href="#top">Pilih Brand Mark <span class="num">00</span></a>
      <a href="#strategy">Brand Strategy <span class="num">01</span></a>
      <a href="#logo-system">Logo Architecture <span class="num">02</span></a>
      <a href="#color-type">Color &amp; Typography <span class="num">03</span></a>
      <a href="#packaging">Live 5-SKU Packaging <span class="num">04</span></a>
      <a href="#applications">Brand Applications <span class="num">05</span></a>
      <a href="#boards">All Boards &amp; PDF <span class="num">06</span></a>
    </nav>
    <div class="drawer-foot">
      <a href="10-brand-guidelines/selunea-brand-guidelines.pdf" target="_blank" class="btn-dark-sm" style="width:100%;">Open Brand Guidelines PDF</a>
      <div style="display:flex;justify-content:space-between;align-items:center;padding-top:6px;">
        <span style="font-size:11.5px;color:var(--ash-soft);">Presented for <b>NANA</b></span>
        {kalla_light}
      </div>
    </div>
  </div>

  <!-- HERO + INTERACTIVE BRAND MARK STUDIO SELECTOR -->
  <section class="hero dark-surface" id="top">
    <div class="wrap hero-grid">
      <div>
        <div class="hero-kicker">Interactive Brand Identity Presentation · Lunar Elegance</div>
        <div class="hero-brand-stack">
          {live_mark_slot("hero-mark-slot")}
          {wm_hero}
        </div>
        <p class="hero-quote">“Beauty in Every Phase.”</p>
        <p class="hero-sub">
          Halo <strong>NANA</strong> — pilih salah satu dari <strong>4 opsi Brand Mark</strong> di panel samping/bawah. Bentuk logo akan langsung bermorfosis secara halus (<em>true vector morph</em>) dan diterapkan ke seluruh halaman: lockup, botol skincare 5 SKU, kartu nama, hingga ikon aplikasi.
        </p>
        <div class="hero-meta-bar">
          <div class="meta-item"><small>Founder &amp; Owner</small><strong>NANA</strong></div>
          <div class="meta-item"><small>Tagline</small><strong>Skincare for every version of you.</strong></div>
          <div class="meta-item"><small>Identity &amp; Direction</small><div style="margin-top:2px;">{kalla_hero}</div></div>
        </div>
      </div>

      <div class="studio-panel" aria-label="Brand Mark Interactive Selector">
        <div class="studio-head">
          <span class="studio-label">Brand Mark Studio · Live Morph</span>
          <span class="studio-active-pill" id="activeMarkBadge">Original · Tri-Phase Lunar</span>
        </div>

        <div class="morph-preview-box">
          <div class="morph-hero-pair">
            {live_mark_slot("studio-big-mark")}
            <svg viewBox="0 0 755 256" class="studio-pair-wm" aria-label="SELUNÉA">{wm_inner}</svg>
          </div>
          <p class="studio-note" id="studioNote">
            Brand mark awal: tiga fase bulan harmonis dipahat lewat kanal negative space konsentris. Skor audit 100/100.
          </p>
        </div>

        <div class="mark-options-grid" role="group" aria-label="Pilih opsi Brand Mark SELUNÉA">
          {"".join(selector_cards)}
        </div>

        <div class="studio-actions">
          <button type="button" class="btn-confirm-choice" id="copyChoiceBtn">
            Salin Pesan Konfirmasi Pilihan
          </button>
          <span class="studio-helper">Salin teks pilihan Brand Mark Anda untuk langsung di-paste ke WhatsApp / chat KALLA.</span>
        </div>
      </div>
    </div>
  </section>

  <!-- FLOATING QUICK MORPH SWITCHER -->
  <div class="floating-bar dark-surface" id="floatingBar" aria-label="Quick Brand Mark Switcher">
    <span class="fb-label">Brand Mark</span>
    {"".join(f'<button type="button" class="fb-btn{" active" if i==0 else ""}" data-select-mark="{m["id"]}" title="{m["name"]}"><svg viewBox="0 0 256 256" aria-hidden="true">{m["svgInner"]}</svg><span>{m["badge"]}</span></button>' for i, m in enumerate(marks_data))}
  </div>

  <!-- 01 · BRAND STRATEGY -->
  <section class="section reveal" id="strategy">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">01 · Brand Foundation</div>
          <h2 class="sec-h2">Lunar Elegance, <em>Refined Calm</em></h2>
        </div>
        <p class="sec-desc">
          Terinspirasi dari fase bulan yang selalu berubah namun tetap utuh, SELUNÉA merayakan ritme alami kulit dan pentingnya perawatan harian yang konsisten — tanpa klise astrologi, parfum, atau dekorasi emas berlebihan.
        </p>
      </div>
      <div class="strategy-grid">
        <div class="editorial-panel">
          <div class="panel-label">Brand Philosophy &amp; Positioning</div>
          <p style="font-size:14px;color:var(--ash-soft);margin-bottom:12px;">
            <strong style="color:var(--ash);">Affordable Premium Skincare:</strong> Menempati ruang editorial modern yang elegan secara visual namun tetap hangat dan mudah dijangkau sehari-hari oleh perempuan usia 20–35 tahun.
          </p>
          <div class="personality-tags">
            <span class="tag-soft">Refined</span><span class="tag-soft">Feminine</span><span class="tag-soft">Calm</span>
            <span class="tag-soft">Confident</span><span class="tag-soft">Sophisticated</span><span class="tag-soft">Approachable</span><span class="tag-soft">Timeless</span>
          </div>
        </div>
        <div class="editorial-panel">
          <div class="panel-label">Visual Principles (Embrace)</div>
          <ul class="pillar-list">
            <li><b>Modern Feminine Minimalism:</b> Ruang napas lega dan hierarki tenang.</li>
            <li><b>Couture High-Contrast Type:</b> Tipografi sans-editorial tajam dengan lengkung lunar <em>L–U</em> dan aksen <em>É</em>.</li>
            <li><b>Subtle Lunar Geometry:</b> Ekspresi fase bulan lewat <em>negative space</em> &amp; cahaya.</li>
            <li><b>Tactile Packaging:</b> Matte Moon Ivory, kaca frosted, satin Champagne &amp; Lunar Silver.</li>
          </ul>
        </div>
        <div class="editorial-panel">
          <div class="panel-label">Category Guardrails (Avoid)</div>
          <ul class="pillar-list">
            <li><b>Nol Klise Bulan Sabit &amp; Bintang:</b> Bukan visual tarot atau astrologi.</li>
            <li><b>Nol Gradasi Ungu / Emas Ramai:</b> Tetap netral mineral dan kontemporer.</li>
            <li><b>Nol Klaim Palsu:</b> Tidak mengarang persentase bahan aktif, SPF, atau sertifikasi.</li>
            <li><b>Nol Font Mentah:</b> Seluruh master logo adalah <em>outlined vector paths</em> murni.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- 02 · LOGO ARCHITECTURE -->
  <section class="section section-alt reveal" id="logo-system">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">02 · Live Logo Architecture</div>
          <h2 class="sec-h2">Bespoke Wordmark &amp; <em>Selected Mark</em></h2>
        </div>
        <p class="sec-desc">
          Seluruh lockup, app icon, dan uji kontras latar di bawah ini otomatis mengikuti Brand Mark yang sedang Anda pilih (<strong id="inlineMarkName">Tri-Phase Lunar</strong>).
        </p>
      </div>

      <div class="playground" aria-label="Interactive Logo Surface Preview">
        <div class="pg-stage" id="pgStage">
          <div class="pg-lockup-live">
            {live_mark_slot("pg-mark-live")}
            <svg viewBox="0 0 755 256" class="pg-wm-live" aria-label="SELUNÉA">{wm_inner}</svg>
          </div>
          <div class="pg-caption" id="pgCaption">Midnight Ash (#34332F) on Moon Ivory (#F3F0E9) · Contrast 11.11:1 (AAA)</div>
        </div>
        <div class="pg-controls">
          <span style="font-size:11.5px;letter-spacing:0.12em;text-transform:uppercase;color:var(--ash-soft);">Test Surface:</span>
          <div class="pg-swatches" role="group" aria-label="Pilih warna latar logo">
            <button type="button" class="surface-btn active" data-bg="#F3F0E9" data-fg="#34332F" data-cap="Midnight Ash (#34332F) on Moon Ivory (#F3F0E9) · Contrast 11.11:1 (AAA)"><span class="sw-chip" style="background:#F3F0E9;"></span>Moon Ivory</button>
            <button type="button" class="surface-btn" data-bg="#34332F" data-fg="#FFFFFF" data-cap="Reversed White (#FFFFFF) on Midnight Ash (#34332F) · Contrast 12.65:1 (AAA)"><span class="sw-chip" style="background:#34332F;"></span>Midnight Ash</button>
            <button type="button" class="surface-btn" data-bg="#34332F" data-fg="#C8B9A6" data-cap="Champagne Beige (#C8B9A6) Foil on Midnight Ash (#34332F) · Contrast 6.59:1 (AA+)"><span class="sw-chip" style="background:#C8B9A6;"></span>Champagne Foil</button>
            <button type="button" class="surface-btn" data-bg="#D9DFD5" data-fg="#34332F" data-cap="Midnight Ash on Sage Haze (#D9DFD5 · Cleanser) · Contrast 9.31:1 (AAA)"><span class="sw-chip" style="background:#D9DFD5;"></span>Sage Haze</button>
            <button type="button" class="surface-btn" data-bg="#DCD9E2" data-fg="#34332F" data-cap="Midnight Ash on Lavender Mist (#DCD9E2 · Toner/Serum) · Contrast 9.07:1 (AAA)"><span class="sw-chip" style="background:#DCD9E2;"></span>Lavender Mist</button>
            <button type="button" class="surface-btn" data-bg="#E4DAD0" data-fg="#34332F" data-cap="Midnight Ash on Soft Nude (#E4DAD0 · Moisturizer/SPF) · Contrast 9.18:1 (AAA)"><span class="sw-chip" style="background:#E4DAD0;"></span>Soft Nude</button>
          </div>
        </div>
      </div>

      <div class="arch-grid">
        <div class="arch-card"><div class="arch-stage">{wm_ash_arch}</div><div class="arch-meta"><div><strong>Primary Wordmark</strong><span>Midnight Ash · Bottles &amp; Web</span></div><a href="05-logo-final/svg/selunea-primary-wordmark-midnight-ash.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card"><div class="arch-stage">{sec_ash}</div><div class="arch-meta"><div><strong>Secondary Logo</strong><span>With Outlined Skincare Sub-line</span></div><a href="05-logo-final/svg/selunea-secondary-skincare-midnight-ash.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card"><div class="arch-stage">{live_mark_slot("arch-svg-sq")}</div><div class="arch-meta"><div><strong>Selected Brand Mark</strong><span id="archMarkSub">Tri-Phase Lunar</span></div><a id="dlMarkLink" href="05-logo-final/svg/selunea-brand-mark-midnight-ash.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card"><div class="arch-stage">{mono_ash}</div><div class="arch-meta"><div><strong>Celestial S Monogram</strong><span>Caps, Jar Lids &amp; Foil Seals</span></div><a href="05-logo-final/svg/selunea-monogram-s-midnight-ash.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card"><div class="arch-stage"><div class="live-hlock">{live_mark_slot()}<svg viewBox="0 0 755 256" class="hlock-wm" aria-hidden="true">{wm_inner}</svg></div></div><div class="arch-meta"><div><strong>Horizontal Lockup</strong><span>Live with Selected Mark</span></div><a id="dlLockupLink" href="05-logo-final/svg/selunea-horizontal-lockup-midnight-ash.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card"><div class="arch-stage"><div class="live-slock">{live_mark_slot()}<svg viewBox="0 0 755 256" class="slock-wm" aria-hidden="true">{wm_inner}</svg></div></div><div class="arch-meta"><div><strong>Stacked Lockup</strong><span>Folding Cartons &amp; Bags</span></div><span style="font-size:10px;color:var(--ash-soft);letter-spacing:0.1em;text-transform:uppercase;">Live</span></div></div>
        <div class="arch-card dark dark-surface"><div class="arch-stage">{wm_white_arch}</div><div class="arch-meta"><div><strong>Reversed White</strong><span>Irradiation-Thinned (~4%)</span></div><a href="05-logo-final/svg/selunea-primary-wordmark-white-reversed.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card"><div class="arch-stage"><div class="app-icon-tile">{live_mark_slot()}</div></div><div class="arch-meta"><div><strong>App &amp; Social Icon</strong><span>Live Midnight Ash Tile</span></div><span style="font-size:10px;color:var(--ash-soft);letter-spacing:0.1em;text-transform:uppercase;">16–512 px</span></div></div>
      </div>
    </div>
  </section>

  <!-- 03 · COLOR SYSTEM, TYPOGRAPHY & GRAPHIC LANGUAGE -->
  <section class="section reveal" id="color-type">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">03 · Color, Typography &amp; Graphic System</div>
          <h2 class="sec-h2">Mineral Palette &amp; <em>Editorial Voice</em></h2>
        </div>
        <p class="sec-desc">Proporsi <strong>60 / 25 / 10 / 5</strong> menjaga visual tetap tenang dengan kontras AAA. Ketuk swatch warna untuk menyalin kode HEX.</p>
      </div>

      <div class="prop-bar" aria-label="Proporsi warna brand">
        <div class="prop-seg" style="width:58%;background:#F3F0E9;color:#34332F;">58% Moon Ivory</div>
        <div class="prop-seg" style="width:24%;background:#34332F;color:#F3F0E9;">24% Ash</div>
        <div class="prop-seg" style="width:12%;background:#C8B9A6;color:#34332F;">12%</div>
        <div class="prop-seg" style="width:6%;background:#B8B7B1;color:#34332F;">6%</div>
      </div>

      <div class="color-grid">
        <button type="button" class="swatch-btn" data-copy="#F3F0E9"><div class="swatch-head" style="background:#F3F0E9;color:#34332F;"><span>Primary Canvas</span><span>Copy</span></div><div class="swatch-body"><strong>Moon Ivory</strong><span class="swatch-code">#F3F0E9 · RGB 243 240 233</span><span class="swatch-code">CMYK 0 1 4 5 · 11.11:1 vs Ash</span></div></button>
        <button type="button" class="swatch-btn" data-copy="#34332F"><div class="swatch-head" style="background:#34332F;color:#F3F0E9;"><span>Primary Ink</span><span>Copy</span></div><div class="swatch-body"><strong>Midnight Ash</strong><span class="swatch-code">#34332F · RGB 52 51 47</span><span class="swatch-code">CMYK 0 2 10 80 · Black 7 C</span></div></button>
        <button type="button" class="swatch-btn" data-copy="#C8B9A6"><div class="swatch-head" style="background:#C8B9A6;color:#34332F;"><span>Warm Accent</span><span>Copy</span></div><div class="swatch-body"><strong>Champagne Beige</strong><span class="swatch-code">#C8B9A6 · RGB 200 185 166</span><span class="swatch-code">Foil 872 C · 6.59:1 on Ash</span></div></button>
        <button type="button" class="swatch-btn" data-copy="#B8B7B1"><div class="swatch-head" style="background:#B8B7B1;color:#34332F;"><span>Cool Metallic</span><span>Copy</span></div><div class="swatch-body"><strong>Lunar Silver</strong><span class="swatch-code">#B8B7B1 · RGB 184 183 177</span><span class="swatch-code">Foil 877 C · 6.29:1 on Ash</span></div></button>
      </div>

      <div class="panel-label" style="margin-bottom:12px;">Product Category Accents (AAA vs Midnight Ash)</div>
      <div class="color-grid sku-3" style="margin-bottom:36px;">
        <button type="button" class="swatch-btn" data-copy="#D9DFD5"><div class="swatch-head" style="background:#D9DFD5;color:#34332F;height:64px;"><span>Phase 01 · Cleanse</span><span>Copy</span></div><div class="swatch-body"><strong>Sage Haze · Facial Cleanser</strong><span class="swatch-code">#D9DFD5 · 9.31:1 vs Ash</span></div></button>
        <button type="button" class="swatch-btn" data-copy="#DCD9E2"><div class="swatch-head" style="background:#DCD9E2;color:#34332F;height:64px;"><span>Phase 02–03 · Treat</span><span>Copy</span></div><div class="swatch-body"><strong>Lavender Mist · Toner &amp; Serum</strong><span class="swatch-code">#DCD9E2 · 9.07:1 vs Ash</span></div></button>
        <button type="button" class="swatch-btn" data-copy="#E4DAD0"><div class="swatch-head" style="background:#E4DAD0;color:#34332F;height:64px;"><span>Phase 04–05 · Nourish &amp; Shield</span><span>Copy</span></div><div class="swatch-body"><strong>Soft Nude · Moisturizer &amp; Sunscreen</strong><span class="swatch-code">#E4DAD0 · 9.18:1 vs Ash</span></div></button>
      </div>

      <div class="panel-label" style="margin-bottom:12px;">Typography Hierarchy (SIL OFL · Max 2 Families)</div>
      <div class="type-stack">
        <div class="type-item"><div class="type-role"><small>Display &amp; Campaign</small><span>Cormorant Garamond · 400 / 500 / Italic</span></div><div style="font-family:var(--font-display);font-size:clamp(28px,4.5vw,40px);line-height:1.12;">Beauty in <em>Every Phase.</em></div></div>
        <div class="type-item"><div class="type-role"><small>Headings &amp; Sub-Copy</small><span>DM Sans Medium · 18–22 px</span></div><div style="font-size:19px;font-weight:500;">Skincare for every version of you.</div></div>
        <div class="type-item"><div class="type-role"><small>Product Specs / Packaging</small><span>DM Sans Medium Uppercase · +0.18em</span></div><div style="font-size:11.5px;font-weight:500;letter-spacing:0.18em;text-transform:uppercase;">PHASE 03 · DAILY SERUM · 30 ML / 1.0 FL. OZ.</div></div>
      </div>

      <div class="panel-label" style="margin-bottom:12px;">Supporting Graphic Language</div>
      <div class="gfx-grid">
        <div class="gfx-card"><div class="gfx-stage">{divider_svg}</div><div><h3>Five-Phase Horizon Divider</h3><p>Pemisah bab editorial pada karton &amp; kartu insert.</p></div></div>
        <div class="gfx-card"><div class="gfx-stage">{orbital_svg}</div><div><h3>Concentric Orbital Frame</h3><p>Aksen orbit halus untuk membingkai foto botol.</p></div></div>
        <div class="gfx-card"><div class="gfx-stage">{pattern_svg}</div><div><h3>Seamless Phase Pattern</h3><p>Motif tissue paper, inner carton &amp; blind emboss.</p></div></div>
        <div class="gfx-card"><div class="gfx-stage">{pearl_svg}</div><div><h3>Pearl Luminosity Surface</h3><p>Latar cahaya mutiara lembut untuk kartu digital.</p></div></div>
      </div>
    </div>
  </section>

  <!-- 04 · LIVE MORPHING 5-SKU PACKAGING FAMILY -->
  <section class="section section-alt reveal" id="packaging">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">04 · Live 5-SKU Packaging Preview</div>
          <h2 class="sec-h2">Five-Phase <em>Product Family</em></h2>
        </div>
        <p class="sec-desc">Ganti opsi Brand Mark di tombol mengambang bawah atau di bagian atas — seluruh <strong>5 kemasan skincare SELUNÉA</strong> di rak ini langsung bermorfosis mengikuti pilihan Anda.</p>
      </div>

      <div class="live-shelf-wrap">
        <div class="live-shelf-head">
          <span>Live Packaging Mockup · Updates with Selected Brand Mark</span>
          <span>Geser ke samping pada layar ponsel →</span>
        </div>
        <div class="live-shelf-row">
          <div class="v-col"><div class="v-stage"><div class="v-tube"><div class="v-fop" style="height:212px;"><div class="v-top">{live_mark_slot("v-mark")}<svg viewBox="0 0 755 256" class="v-wm" aria-hidden="true">{wm_inner}</svg></div><div><div class="v-cat">Phase 01 · Cleanse</div><div class="v-name">Facial<br/>Cleanser</div><div class="v-band" style="background:var(--sage);"></div></div><div class="v-net">120 mL</div></div><div style="height:16px;background:var(--sage);"></div></div><div class="v-tube-cap"></div><div class="v-shadow"></div></div><div class="v-label"><strong>01 · Cleanser</strong><span>Sage Haze · Tube</span></div></div>
          <div class="v-col"><div class="v-stage"><div class="v-toner-cap"></div><div class="v-toner"><div class="v-fop"><div class="v-top">{live_mark_slot("v-mark")}<svg viewBox="0 0 755 256" class="v-wm" aria-hidden="true">{wm_inner}</svg></div><div><div class="v-cat">Phase 02 · Prepare</div><div class="v-name">Balancing<br/>Toner</div><div class="v-band" style="background:var(--lavender);"></div></div><div class="v-net">150 mL</div></div></div><div class="v-shadow"></div></div><div class="v-label"><strong>02 · Toner</strong><span>Frosted · Silver Cap</span></div></div>
          <div class="v-col"><div class="v-stage"><div class="v-bulb"></div><div class="v-collar"></div><div class="v-serum"><div class="v-fop" style="padding:12px 8px;"><div class="v-top">{live_mark_slot("v-mark", "width:18px;height:18px;")}<svg viewBox="0 0 782 256" class="v-wm" aria-hidden="true">{wm_sm_inner}</svg></div><div><div class="v-cat">Phase 03 · Treat</div><div class="v-name" style="font-size:16px;">Daily<br/>Serum</div><div class="v-band" style="background:var(--lavender);"></div></div><div class="v-net">30 mL</div></div></div><div class="v-shadow"></div></div><div class="v-label"><strong>03 · Serum</strong><span>Champagne Dropper</span></div></div>
          <div class="v-col"><div class="v-stage"><div class="v-jar-lid"></div><div class="v-jar"><div class="v-fop" style="padding:10px 10px 8px;"><div class="v-top" style="gap:3px;">{live_mark_slot("v-mark", "width:17px;height:17px;")}<svg viewBox="0 0 782 256" class="v-wm" style="width:56%;" aria-hidden="true">{wm_sm_inner}</svg></div><div><div class="v-name" style="font-size:16px;">Moisturizer</div><div class="v-band" style="background:var(--nude);"></div></div><div class="v-net">50 mL</div></div></div><div class="v-shadow" style="width:124px;"></div></div><div class="v-label"><strong>04 · Moisturizer</strong><span>Frosted Jar · Nude</span></div></div>
          <div class="v-col"><div class="v-stage"><div class="v-spf"><div class="v-fop" style="height:170px;padding:12px 8px 10px;"><div class="v-top">{live_mark_slot("v-mark", "width:19px;height:19px;")}<svg viewBox="0 0 782 256" class="v-wm" aria-hidden="true">{wm_sm_inner}</svg></div><div><div class="v-cat">Phase 05 · Shield</div><div class="v-name" style="font-size:16px;">Daily<br/>Sunscreen</div><div class="v-band" style="background:var(--nude);"></div></div><div class="v-net">50 mL</div></div><div style="height:16px;background:var(--nude);"></div></div><div class="v-spf-cap"></div><div class="v-shadow"></div></div><div class="v-label"><strong>05 · Sunscreen</strong><span>Matte Oval Tube</span></div></div>
        </div>
      </div>

      <div class="board-feature" style="margin-bottom:0;">
        <button type="button" class="board-trigger" data-lightbox="08-packaging/01-skincare-packaging-family.png" data-caption="SELUNÉA — Full Packaging Architecture Spec Board">
          <img src="08-packaging/01-skincare-packaging-family.png" alt="SELUNÉA Packaging Architecture" loading="lazy" width="1600" height="1260" />
        </button>
        <div class="board-bar">
          <div><strong>Full Packaging Spec Board</strong><span> · Folding Cartons, Blind-Deboss Cap Seals &amp; Production Rules</span></div>
          <button type="button" class="zoom-pill" data-lightbox="08-packaging/01-skincare-packaging-family.png" data-caption="SELUNÉA — Full Packaging Spec Board">Zoom Fullscreen</button>
        </div>
      </div>
    </div>
  </section>

  <!-- 05 · BRAND APPLICATIONS -->
  <section class="section reveal" id="applications">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">05 · Brand Applications &amp; Art Direction</div>
          <h2 class="sec-h2">Print, Unboxing &amp; <em>Digital Presence</em></h2>
        </div>
        <p class="sec-desc">Kartu nama resmi <strong>NANA (Founder &amp; Owner)</strong> ikut bermorfosis secara langsung sesuai Brand Mark yang dipilih.</p>
      </div>

      <div class="owner-spot">
        <div class="bcard-live ivory">
          <div style="display:flex;justify-content:space-between;align-items:center;">{wm_card}{live_mark_slot("", "width:28px;height:28px;color:#34332F;")}</div>
          <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap;">
            <div>
              <div style="font-family:var(--font-display);font-size:26px;font-weight:600;letter-spacing:0.06em;line-height:1.1;">NANA</div>
              <div style="font-size:10.5px;letter-spacing:0.16em;text-transform:uppercase;color:var(--ash-soft);">Founder &amp; Owner</div>
            </div>
            <div style="text-align:right;font-size:11.5px;color:var(--ash-soft);line-height:1.55;">nana@selunea.com<br/>@selunea.skin · selunea.com</div>
          </div>
        </div>
        <div class="bcard-live ash dark-surface">
          {live_mark_slot("", "width:42px;height:42px;color:#C8B9A6;")}
          {wm_card_ch}
          <div style="font-family:var(--font-display);font-style:italic;font-size:16px;color:var(--champagne);">Beauty in Every Phase.</div>
        </div>
      </div>

      <div class="boards-grid" style="grid-template-columns:1fr;">
        <div class="board-feature" style="margin-bottom:0;">
          <button type="button" class="board-trigger" data-lightbox="09-brand-applications/01-stationery-and-collateral.png" data-caption="SELUNÉA — Stationery (NANA), Shopping Bag, Tissue Paper &amp; Mailer Box">
            <img src="09-brand-applications/01-stationery-and-collateral.png" alt="SELUNÉA Stationery and Collateral" loading="lazy" width="1600" height="1200" />
          </button>
          <div class="board-bar">
            <div><strong>Stationery, Unboxing &amp; Brand Collateral</strong><span> · Business Card (NANA), Thank-You Card, Shopping Bag, Tissue &amp; Mailer Box</span></div>
            <button type="button" class="zoom-pill" data-lightbox="09-brand-applications/01-stationery-and-collateral.png" data-caption="SELUNÉA — Stationery &amp; Collateral">Zoom</button>
          </div>
        </div>
        <div class="board-feature" style="margin-bottom:0;">
          <button type="button" class="board-trigger" data-lightbox="09-brand-applications/02-social-and-digital.png" data-caption="SELUNÉA — Instagram Identity, E-Commerce Storefront &amp; Art Direction">
            <img src="09-brand-applications/02-social-and-digital.png" alt="SELUNÉA Social Media and Digital Ecosystem" loading="lazy" width="1600" height="1180" />
          </button>
          <div class="board-bar">
            <div><strong>Social Media, Digital Storefront &amp; Art Direction</strong><span> · @selunea.skin, Homepage Hero, 5-SKU Listing &amp; Photography Rules</span></div>
            <button type="button" class="zoom-pill" data-lightbox="09-brand-applications/02-social-and-digital.png" data-caption="SELUNÉA — Social, Digital &amp; Art Direction">Zoom</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 06 · ALL VISUAL BOARDS & DOWNLOADS -->
  <section class="section section-alt reveal" id="boards">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">06 · Complete Visual Archive &amp; Downloads</div>
          <h2 class="sec-h2">All Boards &amp; <em>Production Assets</em></h2>
        </div>
        <p class="sec-desc">Seluruh papan riset, opsi brand mark, presentasi klien, hingga Brand Guideline PDF 15 bab tersedia di sini.</p>
      </div>

      <div class="boards-grid" style="margin-bottom:36px;">
        <article class="board-thumb"><button type="button" class="board-thumb-img" data-lightbox="03-moodboard/01-lunar-elegance-moodboard.png" data-caption="Stage 02 — Lunar Elegance Visual Moodboard"><img src="03-moodboard/01-lunar-elegance-moodboard.png" alt="Moodboard" loading="lazy" width="1600" height="1340" /></button><div class="board-thumb-meta"><div><strong>01 · Moodboard &amp; Direction</strong><span>Materiality, WCAG &amp; Type Study</span></div><button type="button" class="dl-link" data-lightbox="03-moodboard/01-lunar-elegance-moodboard.png" data-caption="Moodboard">View</button></div></article>
        <article class="board-thumb"><button type="button" class="board-thumb-img" data-lightbox="04-logo-concepts/brand-mark-options/selunea-brand-mark-options.png" data-caption="Brand Mark Exploration Sheet (Options 01–04)"><img src="04-logo-concepts/brand-mark-options/selunea-brand-mark-options.png" alt="Brand Mark Options" loading="lazy" width="1520" height="1360" /></button><div class="board-thumb-meta"><div><strong>02 · Brand Mark Options</strong><span>Eclipse Halo, Equinox &amp; Dual-S</span></div><button type="button" class="dl-link" data-lightbox="04-logo-concepts/brand-mark-options/selunea-brand-mark-options.png" data-caption="Brand Mark Options">View</button></div></article>
        <article class="board-thumb"><button type="button" class="board-thumb-img" data-lightbox="06-color-typography/03-color-typography-board.png" data-caption="Stage 06 — Color, Typography &amp; Graphic Spec Board"><img src="06-color-typography/03-color-typography-board.png" alt="Color Typography Board" loading="lazy" width="1600" height="1180" /></button><div class="board-thumb-meta"><div><strong>03 · Color &amp; Typography Spec</strong><span>Tokens, Contrast &amp; Graphic Assets</span></div><button type="button" class="dl-link" data-lightbox="06-color-typography/03-color-typography-board.png" data-caption="Color &amp; Typography Spec">View</button></div></article>
        <article class="board-thumb"><button type="button" class="board-thumb-img" data-lightbox="11-presentations/slides/slide-03.png" data-caption="Client Presentation — Final Identity Slide"><img src="11-presentations/slides/slide-03.png" alt="Final Identity Slide" loading="lazy" width="1440" height="900" /></button><div class="board-thumb-meta"><div><strong>04 · Final Identity Slide</strong><span>Scale Ladder &amp; Champagne Reversed</span></div><button type="button" class="dl-link" data-lightbox="11-presentations/slides/slide-03.png" data-caption="Final Identity Slide">View</button></div></article>
        <article class="board-thumb"><button type="button" class="board-thumb-img" data-lightbox="11-presentations/slides/slide-04.png" data-caption="Client Presentation — Retail &amp; Beauty Mockups (NANA)"><img src="11-presentations/slides/slide-04.png" alt="Retail Mockups" loading="lazy" width="1440" height="900" /></button><div class="board-thumb-meta"><div><strong>05 · Brand Mockups Deck</strong><span>Bag, Box, Card (NANA), Web &amp; Tote</span></div><button type="button" class="dl-link" data-lightbox="11-presentations/slides/slide-04.png" data-caption="Brand Mockups Deck">View</button></div></article>
        <article class="board-thumb"><button type="button" class="board-thumb-img" data-lightbox="10-brand-guidelines/brand-guidelines-preview-p1-p2.png" data-caption="SELUNÉA 15-Section Brand Guidelines PDF Preview"><img src="10-brand-guidelines/brand-guidelines-preview-p1-p2.png" alt="Brand Guidelines" loading="lazy" width="1200" height="1680" /></button><div class="board-thumb-meta"><div><strong>06 · Brand Guidelines Manual</strong><span>15 Complete Chapters · A4 PDF</span></div><button type="button" class="dl-link" data-lightbox="10-brand-guidelines/brand-guidelines-preview-p1-p2.png" data-caption="Brand Guidelines Manual">View</button></div></article>
      </div>

      <div class="dl-grid">
        <div class="dl-card"><div><strong>Brand Guidelines Document</strong><p>Dokumen resmi 15 bab lengkap siap cetak &amp; presentasi.</p></div><div class="dl-btn-row"><a href="10-brand-guidelines/selunea-brand-guidelines.pdf" target="_blank" class="btn-dark-sm">Open PDF</a><a href="10-brand-guidelines/selunea-brand-guidelines.html" target="_blank" class="btn-light-sm">HTML Version</a></div></div>
        <div class="dl-card"><div><strong>Client Presentation &amp; Packaging PDF</strong><p>Deck presentasi 5 slide beserta lembar kemasan 5 SKU beresolusi vektor.</p></div><div class="dl-btn-row"><a href="11-presentations/selunea-client-presentation.pdf" target="_blank" class="btn-dark-sm">Presentation PDF</a><a href="08-packaging/01-skincare-packaging-family.pdf" target="_blank" class="btn-light-sm">Packaging PDF</a></div></div>
        <div class="dl-card"><div><strong>Master Vector &amp; Design Tokens</strong><p>Seluruh SVG master (audit 100/100), PNG 1600 px, dan design tokens JSON/CSS.</p></div><div class="dl-btn-row"><a href="05-logo-final/png/selunea-primary-wordmark-midnight-ash-1600.png" download class="btn-dark-sm">Primary PNG</a><a href="06-color-typography/01-design-tokens.json" target="_blank" class="btn-light-sm">Tokens JSON</a></div></div>
      </div>
    </div>
  </section>

  <!-- FOOTER COLOPHON -->
  <footer class="footer dark-surface">
    <div class="wrap">
      <div class="footer-top">
        <div>
          <div style="display:flex;align-items:center;gap:14px;">{live_mark_slot("", "width:34px;height:34px;color:#C8B9A6;")}{wm_footer}</div>
          <div class="footer-quote">“Beauty in Every Phase.”</div>
          <p style="font-size:13px;color:rgba(243,240,233,0.68);margin-top:8px;max-width:340px;">Skincare for every version of you. Brand Identity System prepared exclusively for <strong>NANA</strong> (Founder &amp; Owner).</p>
        </div>
        <div class="footer-col">
          <h4>Sections</h4>
          <a href="#top">Pilih Brand Mark</a>
          <a href="#strategy">Brand Strategy</a>
          <a href="#logo-system">Logo Architecture</a>
          <a href="#packaging">Live 5-SKU Packaging</a>
          <a href="#boards">All Boards &amp; PDF</a>
        </div>
        <div class="footer-col">
          <h4>Production Notes</h4>
          <p>Silakan lakukan pencarian merek dagang resmi (Kelas 3 Kosmetik) serta proofing fisik Pantone, sablon kaca frosted, dan foil Champagne sebelum produksi massal.</p>
        </div>
      </div>
      <div class="footer-bot">
        <span>© SELUNÉA · Owner: NANA · All Vector Masters Outlined</span>
        <div class="kalla-badge" aria-label="Identity designed by KALLA">{kalla_dark}</div>
      </div>
    </div>
  </footer>

  <!-- LIGHTBOX -->
  <div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Visual Board Preview">
    <div class="lb-bar"><span class="lb-title" id="lbCaption"></span><button type="button" class="lb-close" id="lbClose">Close ✕</button></div>
    <div class="lb-img-wrap"><img id="lbImg" src="" alt="Expanded board preview" /></div>
  </div>

  <!-- TOAST -->
  <div class="toast" id="toast" role="status" aria-live="polite"></div>

<script>
  const BRAND_MARKS = {marks_json};
  const MARK_MAP = Object.fromEntries(BRAND_MARKS.map(m => [m.id, m]));
  let currentMarkId = 'tri-phase';
  let currentContours = MARK_MAP[currentMarkId].contours;
  let animFrameId = null;

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const slots = Array.from(document.querySelectorAll('[data-live-mark]')).map(el => ({{
    exact: el.querySelector('.exact-layer'),
    tween: el.querySelector('.tween-layer'),
  }}));

  const toast = document.getElementById('toast');
  let toastTimer = null;
  function showToast(msg) {{
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 2500);
  }}

  function buildPathD(contours) {{
    let d = '';
    for (let c = 0; c < contours.length; c++) {{
      const pts = contours[c];
      if (!pts.length) continue;
      d += 'M' + pts[0][0].toFixed(1) + ' ' + pts[0][1].toFixed(1);
      for (let i = 1; i < pts.length; i++) {{
        d += 'L' + pts[i][0].toFixed(1) + ' ' + pts[i][1].toFixed(1);
      }}
      d += 'Z';
    }}
    return d;
  }}

  function interpolateContours(fromC, toC, ease) {{
    const out = [];
    for (let c = 0; c < fromC.length; c++) {{
      const f = fromC[c], t = toC[c], arr = [];
      for (let i = 0; i < f.length; i++) {{
        arr.push([
          f[i][0] + (t[i][0] - f[i][0]) * ease,
          f[i][1] + (t[i][1] - f[i][1]) * ease
        ]);
      }}
      out.push(arr);
    }}
    return out;
  }}

  // Silky quintic in-out easing (zero abrupt acceleration or snap!)
  function easeInOutQuint(x) {{
    return x < 0.5 ? 16 * x * x * x * x * x : 1 - Math.pow(-2 * x + 2, 5) / 2;
  }}

  function updateDynamicFavicon(mark) {{
    const svgStr = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256"><rect width="256" height="256" rx="56" fill="#34332F"/><g transform="translate(38 38) scale(0.703)" style="color:#F3F0E9">${{mark.svgInner.replace(/currentColor/g, '#F3F0E9')}}</g></svg>`;
    const link = document.getElementById('dynamicFavicon');
    if (link) link.href = 'data:image/svg+xml,' + encodeURIComponent(svgStr);
  }}

  function applyBrandMark(markId, animate = true) {{
    const mark = MARK_MAP[markId];
    if (!mark) return;
    const changed = markId !== currentMarkId;
    const startContours = currentContours;
    const targetContours = mark.contours;
    currentMarkId = markId;
    try {{ localStorage.setItem('selunea_brand_mark', markId); }} catch (e) {{}}

    // Active buttons
    document.querySelectorAll('[data-select-mark]').forEach(btn => {{
      const isAct = btn.dataset.selectMark === markId;
      btn.classList.toggle('active', isAct);
      if (btn.hasAttribute('aria-pressed')) btn.setAttribute('aria-pressed', String(isAct));
    }});

    // Smooth note cross-fade
    const noteEl = document.getElementById('studioNote');
    document.getElementById('activeMarkBadge').textContent = mark.badge + ' · ' + mark.name;
    document.getElementById('inlineMarkName').textContent = mark.name;
    document.getElementById('archMarkSub').textContent = mark.badge + ' · ' + mark.name;
    document.getElementById('dlMarkLink').href = mark.dlMark;
    document.getElementById('dlLockupLink').href = mark.dlLockup;
    updateDynamicFavicon(mark);

    if (animate && changed && !reducedMotion) {{
      noteEl.classList.add('is-fading');
      setTimeout(() => {{ noteEl.textContent = mark.note; noteEl.classList.remove('is-fading'); }}, 160);
    }} else {{
      noteEl.textContent = mark.note;
    }}

    // Cancel any in-flight morph cleanly (interruptible mid-flight!)
    if (animFrameId) {{ cancelAnimationFrame(animFrameId); animFrameId = null; }}

    if (!animate || !changed || reducedMotion) {{
      currentContours = targetContours;
      slots.forEach(s => {{
        s.exact.innerHTML = mark.svgInner;
        s.exact.style.display = '';
        s.tween.style.display = 'none';
      }});
      return;
    }}

    // Switch all slots to live vertex-interpolated tween path
    slots.forEach(s => {{
      s.exact.style.display = 'none';
      s.tween.style.display = '';
    }});

    const duration = 620;
    const t0 = performance.now();

    function step(now) {{
      const raw = Math.min(1, (now - t0) / duration);
      const e = easeInOutQuint(raw);
      const interp = interpolateContours(startContours, targetContours, e);
      currentContours = interp;
      const d = buildPathD(interp);
      for (let i = 0; i < slots.length; i++) {{
        slots[i].tween.setAttribute('d', d);
      }}
      if (raw < 1) {{
        animFrameId = requestAnimationFrame(step);
      }} else {{
        animFrameId = null;
        currentContours = targetContours;
        for (let i = 0; i < slots.length; i++) {{
          slots[i].exact.innerHTML = mark.svgInner;
          slots[i].exact.style.display = '';
          slots[i].tween.style.display = 'none';
        }}
      }}
    }}
    animFrameId = requestAnimationFrame(step);
  }}

  document.querySelectorAll('[data-select-mark]').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const id = btn.dataset.selectMark;
      if (id === currentMarkId) return;
      applyBrandMark(id, true);
      const m = MARK_MAP[id];
      showToast('Brand Mark aktif: ' + m.badge + ' — ' + m.name);
    }});
  }});

  try {{
    const saved = localStorage.getItem('selunea_brand_mark');
    if (saved && MARK_MAP[saved]) applyBrandMark(saved, false);
  }} catch (e) {{}}

  document.getElementById('copyChoiceBtn').addEventListener('click', async () => {{
    const m = MARK_MAP[currentMarkId];
    const msg = `Halo KALLA, saya (NANA) memilih Brand Mark "${{m.badge}} — ${{m.name}}" untuk identitas final SELUNÉA.`;
    try {{ await navigator.clipboard.writeText(msg); }} catch (e) {{}}
    showToast('Pesan konfirmasi tersalin — siap kirim ke KALLA');
  }});

  // Floating Quick Switcher & Editorial Reveal
  const heroEl = document.getElementById('top');
  const floatingBar = document.getElementById('floatingBar');
  if ('IntersectionObserver' in window) {{
    new IntersectionObserver(([entry]) => {{
      floatingBar.classList.toggle('visible', !entry.isIntersecting);
    }}, {{ threshold: 0.12 }}).observe(heroEl);

    const revObs = new IntersectionObserver((entries, obs) => {{
      entries.forEach(e => {{
        if (e.isIntersecting) {{ e.target.classList.add('in-view'); obs.unobserve(e.target); }}
      }});
    }}, {{ threshold: 0.08 }});
    document.querySelectorAll('.reveal').forEach(el => revObs.observe(el));
  }} else {{
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('in-view'));
  }}

  // Mobile Drawer
  const menuBtn = document.getElementById('menuBtn');
  const drawer = document.getElementById('mobileDrawer');
  function setDrawer(open) {{
    drawer.classList.toggle('open', open);
    drawer.setAttribute('aria-hidden', String(!open));
    menuBtn.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
  }}
  menuBtn.addEventListener('click', () => setDrawer(!drawer.classList.contains('open')));
  drawer.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setDrawer(false)));

  // Surface Playground
  const pgStage = document.getElementById('pgStage');
  const pgCap = document.getElementById('pgCaption');
  document.querySelectorAll('.surface-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      document.querySelectorAll('.surface-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      pgStage.style.backgroundColor = btn.dataset.bg;
      pgStage.style.color = btn.dataset.fg;
      pgCap.textContent = btn.dataset.cap;
    }});
  }});

  // Copy HEX
  document.querySelectorAll('[data-copy]').forEach(btn => {{
    btn.addEventListener('click', async () => {{
      const hex = btn.dataset.copy;
      try {{ await navigator.clipboard.writeText(hex); }} catch (e) {{}}
      showToast('Copied ' + hex);
    }});
  }});

  // Lightbox
  const lb = document.getElementById('lightbox');
  const lbImg = document.getElementById('lbImg');
  const lbCap = document.getElementById('lbCaption');
  const lbClose = document.getElementById('lbClose');
  function openLightbox(src, cap) {{
    lbImg.src = src; lbCap.textContent = cap || ''; lb.classList.add('open');
    document.body.style.overflow = 'hidden'; lbClose.focus();
  }}
  function closeLightbox() {{ lb.classList.remove('open'); document.body.style.overflow = ''; }}
  document.querySelectorAll('[data-lightbox]').forEach(el => {{
    el.addEventListener('click', () => openLightbox(el.dataset.lightbox, el.dataset.caption));
  }});
  lbClose.addEventListener('click', closeLightbox);
  lb.addEventListener('click', (e) => {{ if (e.target === lb) closeLightbox(); }});
  document.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape') {{
      if (lb.classList.contains('open')) closeLightbox();
      if (drawer.classList.contains('open')) setDrawer(false);
    }}
  }});
</script>
</body>
</html>
"""
    out_file = BASE / "index.html"
    out_file.write_text(html, encoding="utf-8")
    print("Built true 60fps geometric path-morph showcase:", out_file)


if __name__ == "__main__":
    build_website()
