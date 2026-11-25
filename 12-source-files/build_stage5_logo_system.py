"""
SELUNÉA — Stage 5 Complete Production Logo Architecture Builder
Approved Direction:
  - Primary Logo: Couture High-Contrast Editorial Sans SELUNÉA (Concept A v4)
    with L→U lunar cradle swash, floating E/É/A architectural hairlines & 30° É light-sliver
  - Secondary Logo: Primary Wordmark + pure-vector tracked SKINCARE descriptor
  - Brand Mark: Tri-Phase Lunar Emblem (Concept B, 100/100 audit)
  - Monogram: Serif-Less High-Contrast Celestial S Seal (Concept C, 100/100 audit)
  - Lockups: Horizontal Lockup & Stacked Lockup
  - Small-Size Responsive Versions: Reinforced micro-print wordmark & 16px favicon mark
  - Irradiation-Compensated Reversed White Versions (optically thinned ~4% for dark grounds)
  - Pure vector <path> outlines throughout (ZERO <text>, ZERO <filter>, ZERO rasters).
"""

import math
from pathlib import Path

BASE = Path(r"c:\Users\ridwa\Desktop\selunea\selunea-brand-identity")
OUT = BASE / "05-logo-final"
SVG_DIR = OUT / "svg"
SVG_DIR.mkdir(parents=True, exist_ok=True)

ASH = "#34332F"
IVORY = "#F3F0E9"
CHAMPAGNE = "#C8B9A6"
BLACK = "#000000"
WHITE = "#FFFFFF"


def fmt(n: float) -> str:
    s = f"{n:.2f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def pt(x: float, y: float) -> str:
    return f"{fmt(x)} {fmt(y)}"


def transform_path_pts(d_tokens, ox, oy, scale):
    out = []
    for item in d_tokens:
        cmd = item[0]
        if cmd == "Z":
            out.append("Z")
        elif cmd == "A":
            rx, ry, rot, la, sw, x, y = item[1:]
            out.append(
                f"A {fmt(rx*scale)} {fmt(ry*scale)} {fmt(rot)} {la} {sw} "
                f"{fmt(ox + x*scale)} {fmt(oy + y*scale)}"
            )
        else:
            coords = item[1:]
            pts = []
            for i in range(0, len(coords), 2):
                pts.append(f"{fmt(ox + coords[i]*scale)} {fmt(oy + coords[i+1]*scale)}")
            out.append(f"{cmd} " + " ".join(pts))
    return " ".join(out)


def rect_tok(x, y, w, h):
    return [("M", x, y), ("L", x + w, y), ("L", x + w, y + h), ("L", x, y + h), ("Z",)]


# ---------------------------------------------------------------------------
# CORE COUTURE HIGH-CONTRAST EDITORIAL SANS GLYPHS (with optical thinning / small-size controls)
# ---------------------------------------------------------------------------

def glyph_S_hc(thin_delta=0.0):
    """High-contrast serif-less S. thin_delta > 0 reinforces hairlines (small-size); < 0 thins for white-on-dark."""
    # Base curves calibrated for normal optical weight; adjust inner curve subtly for irradiation/small cut
    d = thin_delta
    p = [
        ("M", 53.0, 14.5),
        ("L", 49.4 - d * 0.4, 16.4 + d * 0.5),
        ("C", 45.6, 7.6 + d * 0.8, 38.4, 2.2 + d * 1.1, 28.4, 2.2 + d * 1.1),
        ("C", 17.8, 2.2 + d * 1.1, 12.2 + d * 0.5, 8.6 + d * 0.5, 12.2 + d * 0.5, 16.8),
        ("C", 12.2 + d * 0.5, 26.2, 19.8, 32.0, 34.4, 38.6),
        ("C", 51.8, 46.6, 59.0, 55.4, 59.0, 71.0),
        ("C", 59.0, 90.0, 45.0, 102.2, 27.6, 102.2),
        ("C", 15.2, 102.2, 5.8, 95.8, 1.4, 85.4),
        ("L", 5.2 + d * 0.4, 83.4 - d * 0.5),
        ("C", 9.0, 92.6 - d * 0.8, 16.8, 97.8 - d * 1.1, 27.8, 97.8 - d * 1.1),
        ("C", 39.2, 97.8 - d * 1.1, 46.2 - d * 0.5, 89.8 - d * 0.4, 46.2 - d * 0.5, 77.6),
        ("C", 46.2 - d * 0.5, 66.2, 38.6, 59.8, 23.6, 53.0),
        ("C", 8.2, 46.0, 2.2, 37.6, 2.2, 24.4),
        ("C", 2.2, 7.8, 14.4, -2.2, 29.8, -2.2),
        ("C", 41.2, -2.2, 49.2, 4.0, 53.0, 14.5),
        ("Z",),
    ]
    return [p], 61.0


def glyph_E_hc(has_acute=False, couture_break=True, sw=12.6, hw=3.7):
    w_top = 52.0
    w_mid = 46.0
    w_bot = 55.0
    paths = [
        rect_tok(0, 0, sw, 100),
        rect_tok(0, 0, w_top, hw),
        rect_tok(0, 100 - hw, w_bot, hw),
    ]
    if couture_break:
        paths.append(rect_tok(sw + 7.0, 47.0, w_mid - (sw + 7.0), hw))
    else:
        paths.append(rect_tok(0, 47.0, w_mid, hw))
    if has_acute:
        paths.append([
            ("M", 21.0, -9.5),
            ("C", 28.0, -15.2, 35.5, -21.8, 42.0, -30.0),
            ("C", 44.4, -33.0, 48.8, -31.8, 49.0, -27.8),
            ("C", 49.2, -23.4, 37.6, -13.2, 23.2, -7.4),
            ("C", 21.2, -6.6, 19.6, -8.2, 21.0, -9.5),
            ("Z",),
        ])
    return paths, 56.5


def glyph_L_hc(sw=12.6, hw=3.7, swash_under_u=True):
    paths = [rect_tok(0, 0, sw, 100)]
    if swash_under_u:
        # Calibrated lunar cradle swash under U (thickness scales cleanly with hw)
        t_mid = max(5.2, hw * 1.48)
        paths.append([
            ("M", 0, 100 - hw),
            ("L", 34.0, 100 - hw),
            ("C", 58.0, 100 - hw, 74.0, 113.0, 99.0, 113.0),
            ("C", 116.5, 113.0, 130.0, 105.8, 139.0, 96.2),
            ("L", 140.4, 97.6 + (hw - 3.7) * 0.4),
            ("C", 130.5, 109.2, 116.5, 113.0 + t_mid, 98.5, 113.0 + t_mid),
            ("C", 71.5, 113.0 + t_mid, 54.5, 100.0, 32.0, 100.0),
            ("L", 0, 100.0),
            ("Z",),
        ])
        return paths, 53.0
    else:
        paths.append(rect_tok(0, 100 - hw, 50.0, hw))
        return paths, 52.0


def glyph_U_hc(sw=12.6, hw=3.8):
    w = 68.0
    p = [
        ("M", 0, 0),
        ("L", sw, 0),
        ("L", sw, 64.0),
        ("C", sw, 85.0, sw + 8.5, 101.0 - hw, 36.5, 101.0 - hw),
        ("C", w - hw - 10.0, 101.0 - hw, w - hw, 85.5, w - hw, 64.0),
        ("L", w - hw, 0),
        ("L", w, 0),
        ("L", w, 64.0),
        ("C", w, 90.0, w - 12.0, 102.2, 35.0, 102.2),
        ("C", 12.5, 102.2, 0, 90.5, 0, 64.0),
        ("Z",),
    ]
    return [p], w


def glyph_N_hc(sw=12.6, hw=3.8):
    w = 72.0
    paths = [
        rect_tok(0, 0, hw, 100),
        rect_tok(w - hw, 0, hw, 100),
        [
            ("M", 0.0, 0.0),
            ("L", sw + 0.4, 0.0),
            ("L", w, 87.0),
            ("L", w, 100.0),
            ("L", w - sw - 0.4, 100.0),
            ("L", 0.0, 13.0),
            ("Z",),
        ],
    ]
    return paths, w


def glyph_A_hc(sw=12.6, hw=3.8, couture_break=True):
    w = 74.0
    apex_x = 37.0
    apex_y = -1.6
    thin_h = hw / 0.9396
    bold_h = sw / 0.9396

    def lx(x0, y0, x1, y1, y):
        return x0 + (x1 - x0) * (y - y0) / (y1 - y0)

    paths = []
    if couture_break:
        paths.append([
            ("M", apex_x - 2.2, apex_y),
            ("L", apex_x + 1.4, apex_y),
            ("L", thin_h, 100.0),
            ("L", 0.0, 100.0),
            ("Z",),
        ])
        paths.append([
            ("M", apex_x - 2.2, apex_y),
            ("L", apex_x + 2.6, apex_y),
            ("L", w, 100.0),
            ("L", w - bold_h, 100.0),
            ("L", apex_x - 3.6, apex_y + 12.0),
            ("Z",),
        ])
        yb = 65.5
        xl = lx(apex_x + 1.4, apex_y, thin_h, 100.0, yb) + 8.5
        xr = lx(apex_x - 3.6, apex_y + 12.0, w - bold_h, 100.0, yb) + 4.0
        paths.append(rect_tok(xl, yb, xr - xl, hw))
    else:
        paths.append([
            ("M", apex_x - 2.2, apex_y),
            ("L", apex_x + 2.6, apex_y),
            ("L", w, 100.0),
            ("L", w - bold_h, 100.0),
            ("L", apex_x - 2.0, apex_y + 13.5),
            ("L", thin_h, 100.0),
            ("L", 0.0, 100.0),
            ("Z",),
        ])
        yb = 66.0
        xl = lx(apex_x - 2.2, apex_y, 0.0, 100.0, yb) + 2.0
        xr = lx(apex_x + 2.6, apex_y, w, 100.0, yb) - 4.0
        paths.append(rect_tok(xl, yb, xr - xl, hw))
    return paths, w


def build_wordmark(ox, oy, cap_h, tracking=20.0, couture=True, sw=12.6, hw=3.7, s_thin_delta=0.0):
    scale = cap_h / 100.0
    glyphs = [
        ("S", glyph_S_hc(thin_delta=s_thin_delta)),
        ("E", glyph_E_hc(has_acute=False, couture_break=couture, sw=sw, hw=hw)),
        ("L", glyph_L_hc(sw=sw, hw=hw, swash_under_u=couture)),
        ("U", glyph_U_hc(sw=sw, hw=hw + 0.1)),
        ("N", glyph_N_hc(sw=sw, hw=hw + 0.1)),
        ("É", glyph_E_hc(has_acute=True, couture_break=couture, sw=sw, hw=hw)),
        ("A", glyph_A_hc(sw=sw, hw=hw + 0.1, couture_break=couture)),
    ]
    kerns = {
        ("S", "E"): -1.0,
        ("E", "L"): 1.5,
        ("L", "U"): -9.0 if couture else -7.5,
        ("U", "N"): 1.5,
        ("N", "É"): 1.5,
        ("É", "A"): -7.0,
    }
    x = 0.0
    all_paths = []
    for idx, (ch, (gpaths, adv)) in enumerate(glyphs):
        if idx > 0:
            prev = glyphs[idx - 1][0]
            x += tracking + kerns.get((prev, ch), 0.0)
        for gp in gpaths:
            all_paths.append(transform_path_pts(gp, ox + x * scale, oy, scale))
        x += adv
    return all_paths, x * scale


# ---------------------------------------------------------------------------
# PURE-VECTOR GEOMETRIC SANS DESCRIPTOR ("SKINCARE") FOR SECONDARY LOGO
# Zero <text> elements! Clean 100-unit geometric sans uppercase glyphs.
# ---------------------------------------------------------------------------

def build_descriptor_skincare(ox, oy, cap_h, tracking=56.0):
    scale = cap_h / 100.0
    sw = 11.5
    hw = 10.5

    def g_S():
        return [[
            ("M", 54.0, 20.0), ("C", 49.5, 9.0, 40.5, 4.5, 30.0, 4.5),
            ("C", 18.0, 4.5, 11.5, 11.5, 11.5, 21.0), ("C", 11.5, 30.5, 19.0, 36.0, 33.0, 42.0),
            ("C", 49.5, 49.0, 58.0, 57.5, 58.0, 73.0), ("C", 58.0, 91.0, 44.5, 102.0, 28.0, 102.0),
            ("C", 14.5, 102.0, 5.5, 95.5, 1.5, 84.5), ("L", 11.5, 79.5),
            ("C", 15.0, 88.0, 21.0, 92.5, 29.0, 92.5), ("C", 40.0, 92.5, 47.0, 84.5, 47.0, 73.5),
            ("C", 47.0, 62.5, 40.0, 56.5, 26.5, 50.5), ("C", 10.5, 43.5, 2.0, 35.5, 2.0, 21.5),
            ("C", 2.0, 7.5, 13.5, -2.0, 30.0, -2.0), ("C", 43.5, -2.0, 53.5, 4.5, 60.0, 15.0),
            ("Z",),
        ]], 60.0

    def g_K():
        return [
            rect_tok(0, 0, sw, 100),
            [("M", sw - 0.5, 48.0), ("L", 46.5, 0), ("L", 59.5, 0), ("L", 22.0, 47.0), ("L", 61.5, 100), ("L", 47.5, 100), ("L", 14.0, 54.0), ("L", sw - 0.5, 62.0), ("Z",)],
        ], 62.0

    def g_I():
        return [rect_tok(0, 0, sw, 100)], sw

    def g_N():
        w = 66.0
        return [
            rect_tok(0, 0, sw, 100),
            rect_tok(w - sw, 0, sw, 100),
            [("M", 0, 0), ("L", 12.0, 0), ("L", w, 86.0), ("L", w, 100), ("L", w - 12.0, 100), ("L", 0, 14.0), ("Z",)],
        ], w

    def g_C():
        return [[
            ("M", 63.0, 22.0),
            ("C", 57.5, 12.0, 48.0, 7.0, 36.5, 7.0),
            ("C", 19.5, 7.0, 11.5, 21.5, 11.5, 50.0),
            ("C", 11.5, 78.5, 19.5, 93.0, 36.5, 93.0),
            ("C", 48.0, 93.0, 57.5, 88.0, 63.0, 78.0),
            ("L", 72.0, 83.5),
            ("C", 64.5, 96.0, 52.0, 102.2, 36.0, 102.2),
            ("C", 13.0, 102.2, 0.0, 83.0, 0.0, 50.0),
            ("C", 0.0, 17.0, 13.0, -2.2, 36.0, -2.2),
            ("C", 52.0, -2.2, 64.5, 4.0, 72.0, 16.5),
            ("Z",),
        ]], 72.0

    def g_A():
        w = 68.0
        ax = w / 2
        return [
            [("M", ax - 5.8, -1.5), ("L", ax + 5.8, -1.5), ("L", w, 100), ("L", w - 12.2, 100), ("L", ax, 15.0), ("L", 12.2, 100), ("L", 0, 100), ("Z",)],
            rect_tok(14.5, 64.0, 39.0, hw),
        ], w

    def g_R():
        # Clean geometric sans R with evenodd bowl
        bowl = [
            ("M", 0, 0), ("L", 34.0, 0),
            ("C", 52.0, 0, 61.5, 11.0, 61.5, 28.0),
            ("C", 61.5, 43.0, 53.5, 53.0, 39.5, 55.5),
            ("L", 64.0, 100), ("L", 50.5, 100), ("L", 28.0, 56.5),
            ("L", sw, 56.5), ("L", sw, 100), ("L", 0, 100), ("Z",),
            ("M", sw, hw), ("L", sw, 46.5), ("L", 33.0, 46.5),
            ("C", 44.5, 46.5, 50.0, 39.5, 50.0, 28.5),
            ("C", 50.0, 17.5, 44.5, hw, 33.0, hw), ("Z",),
        ]
        return [bowl], 64.0

    def g_E():
        return [
            rect_tok(0, 0, sw, 100),
            rect_tok(0, 0, 54.0, hw),
            rect_tok(0, 44.5, 47.0, hw),
            rect_tok(0, 100 - hw, 56.0, hw),
        ], 56.0

    letters = [
        ("S", g_S()), ("K", g_K()), ("I", g_I()), ("N", g_N()),
        ("C", g_C()), ("A", g_A()), ("R", g_R()), ("E", g_E()),
    ]
    x = 0.0
    out = []
    for idx, (ch, (gps, adv)) in enumerate(letters):
        if idx > 0:
            x += tracking
        for gp in gps:
            out.append((transform_path_pts(gp, ox + x * scale, oy, scale), ch == "R"))
        x += adv
    return out, x * scale


# ---------------------------------------------------------------------------
# BRAND MARK (LUNAR EMBLEM) & MONOGRAM (CELESTIAL S) PATH BUILDERS
# ---------------------------------------------------------------------------

def circle_intersections(x0, y0, r0, x1, y1, r1):
    dx, dy = x1 - x0, y1 - y0
    d = math.hypot(dx, dy)
    a = (r0**2 - r1**2 + d**2) / (2 * d)
    h = math.sqrt(max(0.0, r0**2 - a**2))
    xm = x0 + a * dx / d
    ym = y0 + a * dy / d
    rx = -dy * (h / d)
    ry = dx * (h / d)
    p1 = (xm + rx, ym + ry)
    p2 = (xm - rx, ym - ry)
    return (p1, p2) if p1[1] < p2[1] else (p2, p1)


def build_lunar_emblem_paths(R=102.0, gap=19.0):
    cx, cy = 128.0, 128.0
    d_c = 62.0
    R_c = 132.0
    R_core = R_c - gap
    L_top, L_bot = circle_intersections(cx, cy, R, cx + d_c, cy, R_c)
    left_d = f"M {pt(*L_top)} A {fmt(R)} {fmt(R)} 0 0 0 {pt(*L_bot)} A {fmt(R_c)} {fmt(R_c)} 0 0 1 {pt(*L_top)} Z"
    R_top, R_bot = circle_intersections(cx, cy, R, cx - d_c, cy, R_c)
    right_d = f"M {pt(*R_top)} A {fmt(R)} {fmt(R)} 0 0 1 {pt(*R_bot)} A {fmt(R_c)} {fmt(R_c)} 0 0 0 {pt(*R_top)} Z"
    C_top, C_bot = circle_intersections(cx + d_c, cy, R_core, cx - d_c, cy, R_core)
    core_d = f"M {pt(*C_top)} A {fmt(R_core)} {fmt(R_core)} 0 0 0 {pt(*C_bot)} A {fmt(R_core)} {fmt(R_core)} 0 0 0 {pt(*C_top)} Z"
    return [left_d, core_d, right_d]


def build_open_tapered_arc(cx, cy, r_mid, center_deg, span_deg, max_w):
    R_out = r_mid + max_w * 0.5
    half = math.radians(span_deg * 0.5)
    c_rad = math.radians(center_deg)
    a1, a2 = c_rad - half, c_rad + half
    p1 = (cx + R_out * math.cos(a1), cy + R_out * math.sin(a1))
    p2 = (cx + R_out * math.cos(a2), cy + R_out * math.sin(a2))
    r_m = R_out - max_w
    u = (R_out**2 - r_m**2) / (2.0 * (R_out * math.cos(half) - r_m))
    R_in = abs(r_m - u)
    large_out = 1 if span_deg > 180 else 0
    return f"M {pt(*p1)} A {fmt(R_out)} {fmt(R_out)} 0 {large_out} 1 {pt(*p2)} A {fmt(R_in)} {fmt(R_in)} 0 0 0 {pt(*p1)} Z"


def build_celestial_monogram_paths(arc_w=14.5, s_thin_delta=0.0):
    cx, cy = 128.0, 128.0
    s_tokens, s_w = glyph_S_hc(thin_delta=s_thin_delta)
    s_scale = 1.40
    s_ox = cx - (s_w * 0.5) * s_scale
    s_oy = cy - 50.0 * s_scale
    s_path = transform_path_pts(s_tokens[0], s_ox, s_oy, s_scale)
    arc1 = build_open_tapered_arc(cx, cy, 98.0, 210.0, 132.0, arc_w)
    arc2 = build_open_tapered_arc(cx, cy, 98.0, 30.0, 132.0, arc_w)
    return [arc1, arc2, s_path]


def write_svg(filename, vb_w, vb_h, title, body_xml):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} {vb_h}" width="{vb_w}" height="{vb_h}" role="img" aria-labelledby="title">
  <title id="title">{title}</title>
{body_xml}
</svg>
'''
    (SVG_DIR / filename).write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------------------
# GENERATE COMPLETE LOGO ARCHITECTURE (PRIMARY, SECONDARY, MARK, MONOGRAM,
# HORIZONTAL, STACKED, SMALL-SIZE RESPONSIVE, & IRRADIATION-THINNED WHITE)
# ---------------------------------------------------------------------------

def generate_all():
    # 1. PRIMARY LOGO (Couture Wordmark — Midnight Ash, Black, Irradiation-Thinned White, Champagne)
    cap_h = 112.0
    _, tw = build_wordmark(0, 0, cap_h, tracking=20.0, couture=True, sw=12.8, hw=3.7)
    vb_w = int(math.ceil(tw + 140.0))
    ox = (vb_w - tw) / 2.0
    oy = 82.0

    for suffix, color, sw, hw, s_d in [
        ("midnight-ash", ASH, 12.8, 3.7, 0.0),
        ("black", BLACK, 12.8, 3.7, 0.0),
        ("white-reversed", WHITE, 12.2, 3.45, -0.25),   # Irradiation-thinned ~4%!
        ("champagne", CHAMPAGNE, 12.8, 3.7, 0.0),
    ]:
        paths, _ = build_wordmark(ox, oy, cap_h, tracking=20.0, couture=True, sw=sw, hw=hw, s_thin_delta=s_d)
        els = "\n    ".join(f'<path d="{d}"/>' for d in paths)
        write_svg(
            f"selunea-primary-wordmark-{suffix}.svg",
            vb_w, 256,
            f"SELUNÉA Primary Logo ({suffix})",
            f'  <g id="wordmark" fill="{color}">\n    {els}\n  </g>'
        )

    # 2. SECONDARY LOGO (Primary Wordmark + Wide-Tracked SKINCARE Descriptor — Pure Vector Paths)
    desc_h = 18.0
    _, dw = build_descriptor_skincare(0, 0, desc_h, tracking=78.0)
    desc_ox = (vb_w - dw) / 2.0
    desc_oy = 216.0  # Clean breathing space below L→U lunar swash (which peaks at y ~ 198)
    for suffix, color, sw, hw, s_d in [
        ("midnight-ash", ASH, 12.8, 3.7, 0.0),
        ("black", BLACK, 12.8, 3.7, 0.0),
        ("white-reversed", WHITE, 12.2, 3.45, -0.25),
    ]:
        wm_paths, _ = build_wordmark(ox, 68.0, cap_h, tracking=20.0, couture=True, sw=sw, hw=hw, s_thin_delta=s_d)
        d_paths, _ = build_descriptor_skincare(desc_ox, desc_oy, desc_h, tracking=78.0)
        wm_els = "\n    ".join(f'<path d="{d}"/>' for d in wm_paths)
        d_els = "\n    ".join(
            f'<path{" fill-rule=\"evenodd\"" if eo else ""} d="{d}"/>' for d, eo in d_paths
        )
        write_svg(
            f"selunea-secondary-skincare-{suffix}.svg",
            vb_w, 280,
            f"SELUNÉA Secondary Logo with Skincare Descriptor ({suffix})",
            f'  <g id="wordmark" fill="{color}">\n    {wm_els}\n  </g>\n  <g id="descriptor" fill="{color}">\n    {d_els}\n  </g>'
        )

    # 3. BRAND MARK (Tri-Phase Lunar Emblem — Midnight Ash, Black, White-Reversed Thinned, Champagne, Small-Responsive)
    for suffix, color, gap in [
        ("midnight-ash", ASH, 19.0),
        ("black", BLACK, 19.0),
        ("white-reversed", WHITE, 20.5),  # Wider channel compensates irradiation bloom on dark!
        ("champagne", CHAMPAGNE, 19.0),
    ]:
        em_paths = build_lunar_emblem_paths(R=102.0, gap=gap)
        els = "\n    ".join(f'<path d="{d}"/>' for d in em_paths)
        write_svg(
            f"selunea-brand-mark-{suffix}.svg",
            256, 256,
            f"SELUNÉA Lunar Brand Mark ({suffix})",
            f'  <g id="symbol" fill="{color}">\n    {els}\n  </g>'
        )

    # Small-size responsive Brand Mark (extra-open 23-unit channels + bold footprint for 16 px favicon & micro-stamps)
    sm_em = build_lunar_emblem_paths(R=106.0, gap=23.0)
    write_svg(
        "selunea-brand-mark-small-responsive.svg",
        256, 256,
        "SELUNÉA Lunar Brand Mark (Small-Size 16px Responsive)",
        f'  <g id="symbol" fill="{ASH}">\n    ' + "\n    ".join(f'<path d="{d}"/>' for d in sm_em) + "\n  </g>"
    )

    # 4. MONOGRAM (Celestial High-Contrast S Seal — Caps, Jar Lids, Foil Stickers)
    for suffix, color, aw, sd in [
        ("midnight-ash", ASH, 14.5, 0.0),
        ("black", BLACK, 14.5, 0.0),
        ("white-reversed", WHITE, 13.6, -0.25),
        ("champagne", CHAMPAGNE, 14.5, 0.0),
    ]:
        m_paths = build_celestial_monogram_paths(arc_w=aw, s_thin_delta=sd)
        els = "\n    ".join(f'<path d="{d}"/>' for d in m_paths)
        write_svg(
            f"selunea-monogram-s-{suffix}.svg",
            256, 256,
            f"SELUNÉA Celestial S Monogram ({suffix})",
            f'  <g id="monogram" fill="{color}">\n    {els}\n  </g>'
        )

    # 5. HORIZONTAL LOCKUP (Lunar Emblem + Couture High-Contrast SELUNÉA)
    margin = 48.0
    sym_size = 148.0
    s_sc = sym_size / 204.0
    tx = (margin + sym_size * 0.5) - 128.0 * s_sc
    ty = 128.0 - 128.0 * s_sc
    wm_x = margin + sym_size + 48.0
    h_cap = 86.0
    h_oy = 88.0
    _, h_wm_w = build_wordmark(wm_x, h_oy, h_cap, tracking=20.0, couture=True, sw=12.6, hw=3.8)
    h_vb_w = int(math.ceil(wm_x + h_wm_w + margin))

    for suffix, color, gap, sw, hw, sd in [
        ("midnight-ash", ASH, 19.0, 12.6, 3.8, 0.0),
        ("black", BLACK, 19.0, 12.6, 3.8, 0.0),
        ("white-reversed", WHITE, 20.5, 12.0, 3.55, -0.25),
        ("champagne", CHAMPAGNE, 19.0, 12.6, 3.8, 0.0),
    ]:
        em_paths = build_lunar_emblem_paths(R=102.0, gap=gap)
        wm_paths, _ = build_wordmark(wm_x, h_oy, h_cap, tracking=20.0, couture=True, sw=sw, hw=hw, s_thin_delta=sd)
        em_els = "\n    ".join(f'<path d="{d}"/>' for d in em_paths)
        wm_els = "\n    ".join(f'<path d="{d}"/>' for d in wm_paths)
        write_svg(
            f"selunea-horizontal-lockup-{suffix}.svg",
            h_vb_w, 256,
            f"SELUNÉA Horizontal Lockup ({suffix})",
            f'  <g id="symbol" fill="{color}" transform="translate({fmt(tx)} {fmt(ty)}) scale({fmt(s_sc)})">\n    {em_els}\n  </g>\n  <g id="wordmark" fill="{color}">\n    {wm_els}\n  </g>'
        )

    # 6. STACKED LOCKUP (Lunar Emblem Centered Above Couture SELUNÉA — Cartons, Bags, Social)
    st_w, st_h = 640, 420
    st_sym = 136.0
    st_sc = st_sym / 204.0
    st_tx = (st_w * 0.5) - 128.0 * st_sc
    st_ty = 114.0 - 128.0 * st_sc
    st_cap = 84.0
    _, st_wm_w = build_wordmark(0, 0, st_cap, tracking=20.0, couture=True, sw=12.6, hw=3.8)
    st_ox = (st_w - st_wm_w) / 2.0
    st_oy = 248.0

    for suffix, color, gap, sw, hw, sd in [
        ("midnight-ash", ASH, 19.0, 12.6, 3.8, 0.0),
        ("black", BLACK, 19.0, 12.6, 3.8, 0.0),
        ("white-reversed", WHITE, 20.5, 12.0, 3.55, -0.25),
        ("champagne", CHAMPAGNE, 19.0, 12.6, 3.8, 0.0),
    ]:
        em_paths = build_lunar_emblem_paths(R=102.0, gap=gap)
        wm_paths, _ = build_wordmark(st_ox, st_oy, st_cap, tracking=20.0, couture=True, sw=sw, hw=hw, s_thin_delta=sd)
        em_els = "\n    ".join(f'<path d="{d}"/>' for d in em_paths)
        wm_els = "\n    ".join(f'<path d="{d}"/>' for d in wm_paths)
        write_svg(
            f"selunea-stacked-lockup-{suffix}.svg",
            st_w, st_h,
            f"SELUNÉA Stacked Lockup ({suffix})",
            f'  <g id="symbol" fill="{color}" transform="translate({fmt(st_tx)} {fmt(st_ty)}) scale({fmt(st_sc)})">\n    {em_els}\n  </g>\n  <g id="wordmark" fill="{color}">\n    {wm_els}\n  </g>'
        )

    # 7. SMALL-SIZE RESPONSIVE WORDMARK (Reinforced Hairlines hw=5.4, connected bars, clean L foot for <18mm tubes)
    sm_cap = 112.0
    _, sm_tw = build_wordmark(0, 0, sm_cap, tracking=24.0, couture=False, sw=13.4, hw=5.4, s_thin_delta=1.4)
    sm_vb_w = int(math.ceil(sm_tw + 140.0))
    sm_ox = (sm_vb_w - sm_tw) / 2.0
    sm_paths, _ = build_wordmark(sm_ox, 86.0, sm_cap, tracking=24.0, couture=False, sw=13.4, hw=5.4, s_thin_delta=1.4)
    write_svg(
        "selunea-wordmark-small-responsive.svg",
        sm_vb_w, 256,
        "SELUNÉA Wordmark (Small-Size Responsive Cut)",
        f'  <g id="wordmark" fill="{ASH}">\n    ' + "\n    ".join(f'<path d="{d}"/>' for d in sm_paths) + "\n  </g>"
    )

    print("Generated complete Stage 5 SVG master suite in", SVG_DIR)


if __name__ == "__main__":
    generate_all()
