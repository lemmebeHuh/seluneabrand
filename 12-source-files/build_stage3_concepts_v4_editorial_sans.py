"""
SELUNÉA — Stage 3 Logo Concept Vector Builder (v4 — Owner Reference Style: High-Contrast Editorial Sans)
Absorbs the owner's preferred stylistic grammar (high-contrast serif-less fashion-editorial sans,
graceful bespoke typographic curve, airy negative-space precision) while keeping 100% original
SELUNÉA "Lunar Elegance" identity and SELUNÉA palette (black-first for Stage 4 checkpoint).

Produces three genuinely distinct concepts:
  Concept A — THE LUMINOUS WORDMARK (Hero couture high-contrast sans SELUNÉA with L-U lunar
              cradle swash, airy architectural E/É/A hairlines, 30° moonlight É sliver + minimal Halo mark)
  Concept B — THE LUNAR EMBLEM (Acclaimed tri-phase negative-space circular emblem + clean
              high-contrast editorial sans SELUNÉA lockup)
  Concept C — THE CELESTIAL MONOGRAM (Serif-less high-contrast sculptural S monogram cradled
              by twin non-overlapping 132° orbital phase arcs + clean high-contrast sans lockup)
"""

import math
from pathlib import Path

OUT_DIR = Path(r"c:\Users\ridwa\Desktop\selunea\selunea-brand-identity\04-logo-concepts")
OUT_DIR.mkdir(parents=True, exist_ok=True)

INK = "#111111"


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
# HIGH-CONTRAST FASHION-EDITORIAL SANS GLYPH LIBRARY (100-unit cap height)
# Serif-less architectural precision, ~3.4:1 thick-to-thin contrast,
# calibrated for skincare packaging durability & couture poise.
# ---------------------------------------------------------------------------

def glyph_S_hc_sans():
    """
    Sleek serif-less high-contrast fashion-editorial S.
    Clean open hairline terminals (no Roman serif brackets!), lush sweeping
    diagonal spine (~14.2 units), grounded lower bowl, optical overshoot (-2.2 / 102.2).
    """
    p = [
        # Upper-right clean angled hairline terminal
        ("M", 53.0, 14.5),
        ("L", 49.4, 16.4),
        # Inner upper arch (thin hairline ~3.8)
        ("C", 45.6, 7.6, 38.4, 2.2, 28.4, 2.2),
        ("C", 17.8, 2.2, 12.2, 8.6, 12.2, 16.8),
        ("C", 12.2, 26.2, 19.8, 32.0, 34.4, 38.6),
        # Bold outer lower belly sweeping to bottom-right
        ("C", 51.8, 46.6, 59.0, 55.4, 59.0, 71.0),
        ("C", 59.0, 90.0, 45.0, 102.2, 27.6, 102.2),
        ("C", 15.2, 102.2, 5.8, 95.8, 1.4, 85.4),
        # Clean serif-less lower-left open terminal
        ("L", 5.2, 83.4),
        # Inner lower arch (thin hairline ~3.8)
        ("C", 9.0, 92.6, 16.8, 97.8, 27.8, 97.8),
        ("C", 39.2, 97.8, 46.2, 89.8, 46.2, 77.6),
        ("C", 46.2, 66.2, 38.6, 59.8, 23.6, 53.0),
        # Bold outer upper spine rising to top-left shoulder
        ("C", 8.2, 46.0, 2.2, 37.6, 2.2, 24.4),
        ("C", 2.2, 7.8, 14.4, -2.2, 29.8, -2.2),
        ("C", 41.2, -2.2, 49.2, 4.0, 53.0, 14.5),
        ("Z",),
    ]
    return [p], 61.0


def glyph_E_hc_sans(has_acute=False, couture_break=False, sw=12.6, hw=3.7):
    """High-contrast serif-less E (and É with 30° moonlight sliver)."""
    w_top = 52.0
    w_mid = 46.0
    w_bot = 55.0
    paths = [
        rect_tok(0, 0, sw, 100),
        rect_tok(0, 0, w_top, hw),
        rect_tok(0, 100 - hw, w_bot, hw),
    ]
    if couture_break:
        # Airy architectural floating middle bar (poised 7-unit breath from vertical stem)
        paths.append(rect_tok(sw + 7.0, 47.0, w_mid - (sw + 7.0), hw))
    else:
        paths.append(rect_tok(0, 47.0, w_mid, hw))

    if has_acute:
        # Signature SELUNÉA 30° sculpted moonlight sliver acute accent
        paths.append([
            ("M", 21.0, -9.5),
            ("C", 28.0, -15.2, 35.5, -21.8, 42.0, -30.0),
            ("C", 44.4, -33.0, 48.8, -31.8, 49.0, -27.8),
            ("C", 49.2, -23.4, 37.6, -13.2, 23.2, -7.4),
            ("C", 21.2, -6.6, 19.6, -8.2, 21.0, -9.5),
            ("Z",),
        ])
    return paths, 56.5


def glyph_L_hc_sans(sw=12.6, hw=3.7, swash_under_u=False):
    """High-contrast serif-less L (optionally with graceful lunar cradle swash under U)."""
    paths = [rect_tok(0, 0, sw, 100)]
    if swash_under_u:
        # Clean horizontal foot transitioning into an ultra-graceful modulated lunar curve
        # cradling beneath the U bowl (highlighting L·U·N = Luna!), tapering cleanly to a fine tip!
        paths.append([
            ("M", 0, 100 - hw),
            ("L", 34.0, 100 - hw),
            # Upper edge of lunar cradle arc sweeping smoothly beneath U (U sits roughly x=62..132)
            ("C", 58.0, 100 - hw, 74.0, 113.0, 99.0, 113.0),
            ("C", 116.5, 113.0, 130.0, 105.8, 139.0, 96.2),
            ("L", 140.4, 97.6),
            # Lower edge of lunar cradle arc (subtly swells to ~5.6 units at trough for calligraphic poise)
            ("C", 130.5, 109.2, 116.5, 118.4, 98.5, 118.4),
            ("C", 71.5, 118.4, 54.5, 100.0, 32.0, 100.0),
            ("L", 0, 100.0),
            ("Z",),
        ])
        return paths, 53.0
    else:
        paths.append(rect_tok(0, 100 - hw, 50.0, hw))
        return paths, 52.0


def glyph_U_hc_sans(sw=12.6, hw=3.8):
    """High-contrast serif-less U: bold left stem, smooth modulated bottom bowl, crisp thin right hairline."""
    w = 68.0
    p = [
        ("M", 0, 0),
        ("L", sw, 0),
        ("L", sw, 64.0),
        ("C", sw, 85.0, sw + 8.5, 97.2, 36.5, 97.2),
        ("C", w - hw - 10.0, 97.2, w - hw, 85.5, w - hw, 64.0),
        ("L", w - hw, 0),
        ("L", w, 0),
        ("L", w, 64.0),
        ("C", w, 90.0, w - 12.0, 102.2, 35.0, 102.2),
        ("C", 12.5, 102.2, 0, 90.5, 0, 64.0),
        ("Z",),
    ]
    return [p], w


def glyph_N_hc_sans(sw=12.6, hw=3.8):
    """High-contrast serif-less N: crisp thin verticals + bold sweeping diagonal."""
    w = 72.0
    # Diagonal outer left from (0,0) to (w - sw - 2, 100)?
    # Better: classic high-contrast Didone/Optima N:
    # Left thin vertical (0..hw), right thin vertical (w-hw..w),
    # Bold diagonal running from top-left (0, 0) to bottom-right (w, 100) with sharp optical meet!
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


def glyph_A_hc_sans(sw=12.6, hw=3.8, couture_break=False):
    """
    High-contrast serif-less A: razor-thin left upstroke, bold right downstroke,
    clean flat-sculpted apex, and hairline crossbar (optionally airy open-left couture break!).
    """
    w = 74.0
    apex_x = 37.0
    apex_y = -1.6
    # Horizontal widths at y=100 for perpendicular thicknesses hw (~3.8) and sw (~12.6)
    # Angle of legs: dx=37, dy=101.6 => sin(theta) = 101.6 / hypot(37, 101.6) = 0.9396
    thin_h = hw / 0.9396  # ~4.04
    bold_h = sw / 0.9396  # ~13.41

    def lx(x0, y0, x1, y1, y):
        return x0 + (x1 - x0) * (y - y0) / (y1 - y0)

    paths = []
    if couture_break:
        # Couture architectural touch (inspired by editorial fashion sans):
        # Crisp thin left leg rises cleanly to apex with a tiny refined breath OR meets smoothly,
        # paired with a crisp detached hairline crossbar floating gracefully toward the bold right leg!
        # Left thin leg:
        paths.append([
            ("M", apex_x - 2.2, apex_y),
            ("L", apex_x + 1.4, apex_y),
            ("L", thin_h, 100.0),
            ("L", 0.0, 100.0),
            ("Z",),
        ])
        # Bold right leg (cleanly fused at apex):
        paths.append([
            ("M", apex_x - 2.2, apex_y),
            ("L", apex_x + 2.6, apex_y),
            ("L", w, 100.0),
            ("L", w - bold_h, 100.0),
            ("L", apex_x - 3.6, apex_y + 12.0),
            ("Z",),
        ])
        # Floating architectural crossbar (poised breath gap on left, anchored cleanly into right bold stem)
        yb = 65.5
        xl = lx(apex_x + 1.4, apex_y, thin_h, 100.0, yb) + 8.5
        xr = lx(apex_x - 3.6, apex_y + 12.0, w - bold_h, 100.0, yb) + 4.0
        paths.append(rect_tok(xl, yb, xr - xl, hw))
    else:
        # Clean connected architectural high-contrast A
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


def build_hc_sans_wordmark(ox, oy, cap_h, tracking=21.0, couture=False, sw=12.6, hw=3.7):
    """Build SELUNÉA in custom High-Contrast Fashion-Editorial Sans (pure vector paths)."""
    scale = cap_h / 100.0
    glyphs = [
        ("S", glyph_S_hc_sans()),
        ("E", glyph_E_hc_sans(has_acute=False, couture_break=couture, sw=sw, hw=hw)),
        ("L", glyph_L_hc_sans(sw=sw, hw=hw, swash_under_u=couture)),
        ("U", glyph_U_hc_sans(sw=sw, hw=hw + 0.1)),
        ("N", glyph_N_hc_sans(sw=sw, hw=hw + 0.1)),
        ("É", glyph_E_hc_sans(has_acute=True, couture_break=couture, sw=sw, hw=hw)),
        ("A", glyph_A_hc_sans(sw=sw, hw=hw + 0.1, couture_break=couture)),
    ]
    kerns = {
        ("S", "E"): -1.0,
        ("E", "L"): 1.5,
        ("L", "U"): -9.0 if couture else -7.5,  # Tighter poetic embrace when L cradles U!
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
# GEOMETRIC HELPERS FOR SYMBOLS
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


def build_open_tapered_arc(cx, cy, r_mid, center_deg, span_deg, max_w):
    R_out = r_mid + max_w * 0.5
    half = math.radians(span_deg * 0.5)
    c_rad = math.radians(center_deg)
    a1 = c_rad - half
    a2 = c_rad + half
    p1 = (cx + R_out * math.cos(a1), cy + R_out * math.sin(a1))
    p2 = (cx + R_out * math.cos(a2), cy + R_out * math.sin(a2))
    r_m = R_out - max_w
    u = (R_out**2 - r_m**2) / (2.0 * (R_out * math.cos(half) - r_m))
    R_in = abs(r_m - u)
    large_out = 1 if span_deg > 180 else 0
    return (
        f"M {pt(*p1)} "
        f"A {fmt(R_out)} {fmt(R_out)} 0 {large_out} 1 {pt(*p2)} "
        f"A {fmt(R_in)} {fmt(R_in)} 0 0 0 {pt(*p1)} Z"
    )


# ---------------------------------------------------------------------------
# CONCEPT A (v4): THE LUMINOUS WORDMARK (Owner Couture High-Contrast Sans Hero)
# ---------------------------------------------------------------------------

def build_concept_a():
    # Minimal Supporting Symbol: Continuous Luminous Eclipse Halo (100/100, 6 anchors, evenodd)
    cx, cy = 128.0, 128.0
    Ro, Ri = 98.0, 66.0
    ang = math.radians(-30.0)
    shift = 16.0
    ix = cx + shift * math.cos(ang)
    iy = cy + shift * math.sin(ang)

    halo_d = (
        f"M {fmt(cx)} {fmt(cy - Ro)} "
        f"A {fmt(Ro)} {fmt(Ro)} 0 1 1 {fmt(cx)} {fmt(cy + Ro)} "
        f"A {fmt(Ro)} {fmt(Ro)} 0 1 1 {fmt(cx)} {fmt(cy - Ro)} Z "
        f"M {fmt(ix)} {fmt(iy - Ri)} "
        f"A {fmt(Ri)} {fmt(Ri)} 0 1 0 {fmt(ix)} {fmt(iy + Ri)} "
        f"A {fmt(Ri)} {fmt(Ri)} 0 1 0 {fmt(ix)} {fmt(iy - Ri)} Z"
    )
    symbol_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="title">
  <title id="title">SELUNÉA — Concept A Supporting Luminous Halo</title>
  <g id="symbol" fill="{INK}">
    <path fill-rule="evenodd" d="{halo_d}"/>
  </g>
</svg>
'''
    (OUT_DIR / "concept-a-symbol-v4.svg").write_text(symbol_svg, encoding="utf-8")
    (OUT_DIR / "concept-a-symbol.svg").write_text(symbol_svg, encoding="utf-8")

    # Hero Couture High-Contrast Sans Wordmark (with L→U lunar cradle swash, floating E/É/A hairlines & 30° É sliver)
    cap_h = 112.0
    _, tw = build_hc_sans_wordmark(0, 0, cap_h, tracking=20.0, couture=True, sw=12.8, hw=3.7)
    vb_w = int(math.ceil(tw + 140.0))
    ox = (vb_w - tw) / 2.0
    oy = 82.0  # leaves clean top room for É sliver (~46) and bottom room for L→U lunar cradle (~214)
    paths, _ = build_hc_sans_wordmark(ox, oy, cap_h, tracking=20.0, couture=True, sw=12.8, hw=3.7)
    path_els = "\n    ".join(f'<path d="{d}"/>' for d in paths)

    wordmark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} 256" width="{vb_w}" height="256" role="img" aria-labelledby="title">
  <title id="title">SELUNÉA — Concept A The Luminous Wordmark (Editorial Sans)</title>
  <g id="wordmark" fill="{INK}">
    {path_els}
  </g>
</svg>
'''
    (OUT_DIR / "concept-a-wordmark-v4.svg").write_text(wordmark_svg, encoding="utf-8")
    (OUT_DIR / "concept-a-wordmark.svg").write_text(wordmark_svg, encoding="utf-8")


# ---------------------------------------------------------------------------
# CONCEPT B (v4): THE LUNAR EMBLEM + HIGH-CONTRAST EDITORIAL SANS LOCKUP
# ---------------------------------------------------------------------------

def build_concept_b():
    cx, cy = 128.0, 128.0
    R = 102.0
    d_c = 62.0
    R_c = 132.0
    gap = 19.0
    R_core = R_c - gap

    L_top, L_bot = circle_intersections(cx, cy, R, cx + d_c, cy, R_c)
    left_d = (
        f"M {pt(*L_top)} "
        f"A {fmt(R)} {fmt(R)} 0 0 0 {pt(*L_bot)} "
        f"A {fmt(R_c)} {fmt(R_c)} 0 0 1 {pt(*L_top)} Z"
    )
    R_top, R_bot = circle_intersections(cx, cy, R, cx - d_c, cy, R_c)
    right_d = (
        f"M {pt(*R_top)} "
        f"A {fmt(R)} {fmt(R)} 0 0 1 {pt(*R_bot)} "
        f"A {fmt(R_c)} {fmt(R_c)} 0 0 0 {pt(*R_top)} Z"
    )
    C_top, C_bot = circle_intersections(cx + d_c, cy, R_core, cx - d_c, cy, R_core)
    core_d = (
        f"M {pt(*C_top)} "
        f"A {fmt(R_core)} {fmt(R_core)} 0 0 0 {pt(*C_bot)} "
        f"A {fmt(R_core)} {fmt(R_core)} 0 0 0 {pt(*C_top)} Z"
    )

    symbol_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="title">
  <title id="title">SELUNÉA — Concept B The Lunar Emblem</title>
  <g id="symbol" fill="{INK}">
    <path d="{left_d}"/>
    <path d="{core_d}"/>
    <path d="{right_d}"/>
  </g>
</svg>
'''
    (OUT_DIR / "concept-b-symbol-v4.svg").write_text(symbol_svg, encoding="utf-8")
    (OUT_DIR / "concept-b-symbol.svg").write_text(symbol_svg, encoding="utf-8")

    # Lockup: Lunar Emblem left + crisp High-Contrast Editorial Sans SELUNÉA right
    margin = 48.0
    sym_size = 148.0
    s_sc = sym_size / (2.0 * R)
    sym_cx = margin + sym_size * 0.5
    sym_cy = 128.0
    tx = sym_cx - cx * s_sc
    ty = sym_cy - cy * s_sc

    gap_x = 46.0
    wm_x = margin + sym_size + gap_x
    cap_h = 84.0
    wm_oy = 94.0
    wm_paths, wm_w = build_hc_sans_wordmark(wm_x, wm_oy, cap_h, tracking=21.0, couture=False, sw=12.0, hw=3.8)
    vb_w = int(math.ceil(wm_x + wm_w + margin))
    wm_els = "\n    ".join(f'<path d="{d}"/>' for d in wm_paths)

    lockup_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} 256" width="{vb_w}" height="256" role="img" aria-labelledby="title">
  <title id="title">SELUNÉA — Concept B Lunar Emblem Lockup (Editorial Sans)</title>
  <g id="symbol" fill="{INK}" transform="translate({fmt(tx)} {fmt(ty)}) scale({fmt(s_sc)})">
    <path d="{left_d}"/>
    <path d="{core_d}"/>
    <path d="{right_d}"/>
  </g>
  <g id="wordmark" fill="{INK}">
    {wm_els}
  </g>
</svg>
'''
    (OUT_DIR / "concept-b-lockup-v4.svg").write_text(lockup_svg, encoding="utf-8")
    (OUT_DIR / "concept-b-lockup.svg").write_text(lockup_svg, encoding="utf-8")


# ---------------------------------------------------------------------------
# CONCEPT C (v4): THE CELESTIAL MONOGRAM (High-Contrast Sans S + Twin Orbital Arcs)
# ---------------------------------------------------------------------------

def build_concept_c():
    cx, cy = 128.0, 128.0

    # Sleek serif-less high-contrast sculptural S centered inside twin 132° orbital arcs
    s_tokens, s_w = glyph_S_hc_sans()
    s_scale = 1.40
    s_ox = cx - (s_w * 0.5) * s_scale
    s_oy = cy - 50.0 * s_scale
    s_path = transform_path_pts(s_tokens[0], s_ox, s_oy, s_scale)

    arc_top_left = build_open_tapered_arc(cx, cy, 98.0, 210.0, 132.0, 14.5)
    arc_bot_right = build_open_tapered_arc(cx, cy, 98.0, 30.0, 132.0, 14.5)

    symbol_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="title">
  <title id="title">SELUNÉA — Concept C The Celestial Monogram (Editorial Sans S)</title>
  <g id="symbol" fill="{INK}">
    <path d="{arc_top_left}"/>
    <path d="{arc_bot_right}"/>
    <path d="{s_path}"/>
  </g>
</svg>
'''
    (OUT_DIR / "concept-c-symbol-v4.svg").write_text(symbol_svg, encoding="utf-8")
    (OUT_DIR / "concept-c-symbol.svg").write_text(symbol_svg, encoding="utf-8")

    # Lockup: Monogram left + sleek High-Contrast Editorial Sans SELUNÉA right (with subtle couture breath)
    margin = 48.0
    sym_size = 152.0
    R_outer = 98.0 + 14.5 * 0.5
    s_sc = sym_size / (2.0 * R_outer)
    sym_cx = margin + sym_size * 0.5
    sym_cy = 128.0
    tx = sym_cx - cx * s_sc
    ty = sym_cy - cy * s_sc

    gap_x = 46.0
    wm_x = margin + sym_size + gap_x
    cap_h = 80.0
    wm_oy = 96.0
    wm_paths, wm_w = build_hc_sans_wordmark(wm_x, wm_oy, cap_h, tracking=23.0, couture=False, sw=11.6, hw=3.7)
    vb_w = int(math.ceil(wm_x + wm_w + margin))
    wm_els = "\n    ".join(f'<path d="{d}"/>' for d in wm_paths)

    lockup_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} 256" width="{vb_w}" height="256" role="img" aria-labelledby="title">
  <title id="title">SELUNÉA — Concept C Celestial Monogram Lockup (Editorial Sans)</title>
  <g id="symbol" fill="{INK}" transform="translate({fmt(tx)} {fmt(ty)}) scale({fmt(s_sc)})">
    <path d="{arc_top_left}"/>
    <path d="{arc_bot_right}"/>
    <path d="{s_path}"/>
  </g>
  <g id="wordmark" fill="{INK}">
    {wm_els}
  </g>
</svg>
'''
    (OUT_DIR / "concept-c-lockup-v4.svg").write_text(lockup_svg, encoding="utf-8")
    (OUT_DIR / "concept-c-lockup.svg").write_text(lockup_svg, encoding="utf-8")


if __name__ == "__main__":
    build_concept_a()
    build_concept_b()
    build_concept_c()
    print("Generated Stage 3 v4 (Owner Editorial Sans Style) SVGs in", OUT_DIR)
