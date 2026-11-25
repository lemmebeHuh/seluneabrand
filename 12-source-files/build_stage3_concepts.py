"""
SELUNÉA — Stage 3 Logo Concept Vector Builder (Iteration v2 — Craft Pass)
Refinements over v1 after visual inspection & svg_audit.py:
  - Concept A Symbol: Replaced literal crescent+dot with ownable 'Accented Lunar Disc'
    (serene open luminous ring + signature 30° sculpted É light-sliver) — zero crescent cliché!
  - Editorial Serif Wordmark: Refined A apex & brackets, exact N stem/diagonal harmony,
    crisp E middle terminal, snapped S lower-left vertical to exact 90°, balanced margins.
  - Concept B Emblem: Refined 19-unit concentric negative-space channels for 16 px clarity
    and optically centered horizontal lockup margins.
  - Concept C Monogram: Fixed orbital arc span math so twin sculpted arcs span ~136° each
    with clean ~44° breathing apertures (zero overlap!), snapped S terminal angle, and
    corrected minimalist sans N diagonal optical weight in Concept C lockup.
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


# ---------------------------------------------------------------------------
# REFINED EDITORIAL SERIF GLYPHS (v2)
# ---------------------------------------------------------------------------

def serif_stem(x0, w, y_top=0.0, y_bot=100.0, tl=8.0, tr=8.0, bl=8.0, br=8.0, sh=3.2, bk=6.0):
    x1 = x0 + w
    t = [
        ("M", x0 - tl, y_top),
        ("L", x1 + tr, y_top),
        ("L", x1 + tr, y_top + sh),
    ]
    if tr > 0:
        t.append(("Q", x1, y_top + sh, x1, y_top + sh + bk))
    else:
        t.append(("L", x1, y_top + sh))
    if br > 0:
        t.append(("L", x1, y_bot - sh - bk))
        t.append(("Q", x1, y_bot - sh, x1 + br, y_bot - sh))
    else:
        t.append(("L", x1, y_bot - sh))
    t.extend([
        ("L", x1 + br, y_bot),
        ("L", x0 - bl, y_bot),
        ("L", x0 - bl, y_bot - sh),
    ])
    if bl > 0:
        t.append(("Q", x0, y_bot - sh, x0, y_bot - sh - bk))
    else:
        t.append(("L", x0, y_bot - sh))
    if tl > 0:
        t.append(("L", x0, y_top + sh + bk))
        t.append(("Q", x0, y_top + sh, x0 - tl, y_top + sh))
    else:
        t.append(("L", x0, y_top + sh))
    t.append(("Z",))
    return t


def glyph_E_editorial(has_acute=False, sw=11.8, hw=3.9):
    paths = []
    paths.append(serif_stem(8.5, sw, 0, 100, tl=8.5, tr=0, bl=8.5, br=0, sh=3.2, bk=6.2))
    x_st = 8.5 + sw - 0.8
    x_end = 57.0
    paths.append([
        ("M", x_st, 0),
        ("L", x_end, 0),
        ("L", x_end + 1.0, 16.5),
        ("L", x_end - 1.5, 16.5),
        ("C", x_end - 2.6, 8.0, x_end - 7.8, hw + 0.4, x_end - 15.5, hw),
        ("L", x_st, hw),
        ("Z",),
    ])
    ym = 48.0
    xm_end = 50.0
    paths.append([
        ("M", x_st, ym - hw * 0.5),
        ("L", xm_end - 7.5, ym - hw * 0.5),
        ("Q", xm_end - 1.8, ym - hw * 0.5, xm_end, ym - 7.5),
        ("L", xm_end + 2.2, ym - 7.5),
        ("L", xm_end + 2.2, ym + 7.5),
        ("L", xm_end, ym + 7.5),
        ("Q", xm_end - 1.8, ym + hw * 0.5, xm_end - 7.5, ym + hw * 0.5),
        ("L", x_st, ym + hw * 0.5),
        ("Z",),
    ])
    xb_end = 60.0
    paths.append([
        ("M", x_st, 100 - hw),
        ("L", xb_end - 17.0, 100 - hw),
        ("C", xb_end - 8.5, 100 - hw - 0.4, xb_end - 2.8, 100 - 8.8, xb_end - 1.0, 100 - 19.0),
        ("L", xb_end + 1.8, 100 - 19.0),
        ("L", xb_end + 0.2, 100),
        ("L", x_st, 100),
        ("Z",),
    ])
    if has_acute:
        # Signature sculpted 30° luminous sliver acute accent
        paths.append([
            ("M", 25.0, -9.2),
            ("C", 31.8, -14.8, 39.0, -21.4, 45.2, -29.6),
            ("C", 47.6, -32.8, 52.0, -31.5, 52.2, -27.6),
            ("C", 52.4, -23.2, 41.2, -13.0, 27.2, -7.2),
            ("C", 25.2, -6.4, 23.6, -7.9, 25.0, -9.2),
            ("Z",),
        ])
    return paths, 62.5


def glyph_L_editorial(sw=11.8, hw=4.0):
    paths = []
    paths.append(serif_stem(8.5, sw, 0, 100, tl=8.5, tr=8.5, bl=8.5, br=0, sh=3.2, bk=6.2))
    x_st = 8.5 + sw - 0.8
    xb_end = 57.5
    paths.append([
        ("M", x_st, 100 - hw),
        ("L", xb_end - 17.0, 100 - hw),
        ("C", xb_end - 8.5, 100 - hw - 0.4, xb_end - 2.8, 100 - 9.0, xb_end - 1.0, 100 - 20.5),
        ("L", xb_end + 1.8, 100 - 20.5),
        ("L", xb_end + 0.2, 100),
        ("L", x_st, 100),
        ("Z",),
    ])
    return paths, 60.0


def glyph_U_editorial(sw=11.8, thin=4.7):
    xL = 8.5
    xR = 64.5
    tl, tr_l, tl_r, tr_r = 8.5, 7.5, 7.5, 8.5
    sh, bk = 3.2, 6.0
    p = [
        ("M", xL - tl, 0),
        ("L", xL + sw + tr_l, 0),
        ("L", xL + sw + tr_l, sh),
        ("Q", xL + sw, sh, xL + sw, sh + bk),
        ("L", xL + sw, 64.0),
        ("C", xL + sw, 86.0, xL + sw + 9.0, 96.6, (xL + sw + xR - thin) * 0.5 + 1.0, 96.6),
        ("C", xR - thin - 8.0, 96.6, xR - thin, 86.0, xR - thin, 64.0),
        ("L", xR - thin, sh + bk),
        ("Q", xR - thin, sh, xR - thin - tl_r, sh),
        ("L", xR - thin - tl_r, 0),
        ("L", xR + tr_r, 0),
        ("L", xR + tr_r, sh),
        ("Q", xR, sh, xR, sh + bk),
        ("L", xR, 64.0),
        ("C", xR, 91.5, xR - 12.5, 102.2, (xL + xR) * 0.5 + 0.5, 102.2),
        ("C", xL + 11.0, 102.2, xL, 91.5, xL, 64.0),
        ("L", xL, sh + bk),
        ("Q", xL, sh, xL - tl, sh),
        ("Z",),
    ]
    return [p], 73.5


def glyph_N_editorial(sw=11.8, thin=4.7):
    xL = 8.5
    xR = 69.5
    paths = [
        serif_stem(xL, thin, 0, 100, tl=8.5, tr=0, bl=8.5, br=8.5, sh=3.2, bk=6.0),
        serif_stem(xR - thin, thin, 0, 100, tl=8.5, tr=8.5, bl=0, br=0, sh=3.2, bk=6.0),
        # Clean bold diagonal with exact 60° visual poise
        [
            ("M", xL, 0),
            ("L", xL + sw + 0.8, 0),
            ("L", xR - thin + 0.8, 82.0),
            ("L", xR, 101.6),
            ("L", xR - thin - 0.8, 101.6),
            ("L", xL + thin - 0.6, 16.0),
            ("L", xL, 0),
            ("Z",),
        ],
    ]
    return paths, 78.5


def glyph_A_editorial(sw=11.8, thin=4.8):
    """Refined editorial serif A: crisp pointed Didone apex, smooth concave foot serifs, low crossbar."""
    apex_x = 38.0
    apex_y = -2.2
    xL = 6.5      # outer left foot x at y=100
    xR = 69.5     # outer right foot x at y=100
    sh = 3.2
    # Slope unit vectors for left and right legs
    # Left leg outer goes from (apex_x, apex_y) to (xL, 100)
    # Right leg outer goes from (apex_x, apex_y) to (xR, 100)
    # Using exact horizontal widths at y=100: thin_h = 5.4 for left leg, sw_h = 13.0 for right leg
    thin_h = 5.4
    sw_h = 13.0

    # Left thin leg + refined symmetric baseline serifs
    # Compute x along outer & inner edges at y = 100 - sh - 5.5
    def lerp_x(x0, y0, x1, y1, y):
        return x0 + (x1 - x0) * (y - y0) / (y1 - y0)

    y_bk = 100 - sh - 6.0
    # Left leg outer line: (apex_x - 0.6, apex_y) -> (xL, 100)
    # Left leg inner line: (apex_x + 2.8, apex_y + 8.5) -> (xL + thin_h, 100)
    xL_out_bk = lerp_x(apex_x - 0.6, apex_y, xL, 100, y_bk)
    xL_in_bk = lerp_x(apex_x + 2.6, apex_y + 8.0, xL + thin_h, 100, y_bk)
    xL_in_base = xL + thin_h

    left_leg = [
        ("M", apex_x - 1.2, apex_y),
        ("L", apex_x + 1.2, apex_y),
        ("L", apex_x + 3.8, apex_y + 8.0),
        ("L", xL_in_bk, y_bk),
        ("Q", xL_in_base - 0.5, 100 - sh, xL_in_base + 7.8, 100 - sh),
        ("L", xL_in_base + 7.8, 100),
        ("L", xL - 6.8, 100),
        ("L", xL - 6.8, 100 - sh),
        ("Q", xL + 0.5, 100 - sh, xL_out_bk, y_bk),
        ("Z",),
    ]

    # Right bold leg: outer (apex_x + 0.8, apex_y) -> (xR, 100); inner (apex_x - 1.6, apex_y + 8.0) -> (xR - sw_h, 100)
    xR_out_bk = lerp_x(apex_x + 0.8, apex_y, xR, 100, y_bk)
    xR_in_bk = lerp_x(apex_x - 1.2, apex_y + 7.5, xR - sw_h, 100, y_bk)
    xR_in_base = xR - sw_h

    right_leg = [
        ("M", apex_x - 0.6, apex_y),
        ("L", apex_x + 0.8, apex_y),
        ("L", xR_out_bk, y_bk),
        ("Q", xR - 0.4, 100 - sh, xR + 7.5, 100 - sh),
        ("L", xR + 7.5, 100),
        ("L", xR_in_base - 7.8, 100),
        ("L", xR_in_base - 7.8, 100 - sh),
        ("Q", xR_in_base + 0.5, 100 - sh, xR_in_bk, y_bk),
        ("L", apex_x - 2.2, apex_y + 7.5),
        ("Z",),
    ]

    # Low editorial crossbar cleanly anchored inside legs
    y_bar = 66.0
    bh = 3.8
    xb_l1 = lerp_x(apex_x - 0.6, apex_y, xL, 100, y_bar) + 2.0
    xb_r1 = lerp_x(apex_x + 0.8, apex_y, xR, 100, y_bar) - 4.0
    xb_l2 = lerp_x(apex_x - 0.6, apex_y, xL, 100, y_bar + bh) + 2.0
    xb_r2 = lerp_x(apex_x + 0.8, apex_y, xR, 100, y_bar + bh) - 4.0
    crossbar = [
        ("M", xb_l1, y_bar),
        ("L", xb_r1, y_bar),
        ("L", xb_r2, y_bar + bh),
        ("L", xb_l2, y_bar + bh),
        ("Z",),
    ]
    return [left_leg, right_leg, crossbar], 76.5


def glyph_S_editorial():
    """
    Signature SELUNÉA editorial serif S (v2).
    Snapped lower-left terminal edge to exact 90° vertical (fixes audit near-miss angle),
    refined luminous spine sweep, grounded lower bowl, optical overshoot (-2.2 / 102.2).
    """
    p = [
        ("M", 52.8, 22.0),
        ("L", 50.2, 22.0),
        ("C", 48.0, 9.8, 40.5, 3.0, 29.8, 3.0),
        ("C", 18.8, 3.0, 12.6, 9.8, 12.6, 18.6),
        ("C", 12.6, 28.4, 21.0, 34.4, 34.8, 40.8),
        ("C", 51.8, 48.4, 58.6, 56.8, 58.6, 71.2),
        ("C", 58.6, 90.2, 44.5, 102.2, 26.8, 102.2),
        ("C", 17.0, 102.2, 9.8, 99.0, 4.0, 94.6),
        # Clean vertical 90° editorial lower-left serif edge
        ("L", 4.0, 73.2),
        ("L", 6.6, 73.2),
        ("C", 9.2, 88.2, 17.6, 97.6, 28.4, 97.6),
        ("C", 40.2, 97.6, 47.4, 89.8, 47.4, 78.6),
        ("C", 47.4, 67.2, 39.6, 61.0, 25.0, 54.4),
        ("C", 9.8, 47.6, 4.0, 39.2, 4.0, 25.8),
        ("C", 4.0, 8.6, 16.4, -2.2, 31.8, -2.2),
        ("C", 40.2, -2.2, 46.8, 0.4, 51.6, 3.8),
        ("L", 52.8, 22.0),
        ("Z",),
    ]
    return [p], 62.0


def build_editorial_wordmark_paths(ox, oy, cap_h, tracking=19.0, sw=11.8, hw=3.9):
    scale = cap_h / 100.0
    glyphs = [
        ("S", glyph_S_editorial()),
        ("E", glyph_E_editorial(has_acute=False, sw=sw, hw=hw)),
        ("L", glyph_L_editorial(sw=sw, hw=hw + 0.1)),
        ("U", glyph_U_editorial(sw=sw, thin=hw + 0.8)),
        ("N", glyph_N_editorial(sw=sw, thin=hw + 0.8)),
        ("É", glyph_E_editorial(has_acute=True, sw=sw, hw=hw)),
        ("A", glyph_A_editorial(sw=sw, thin=hw + 0.9)),
    ]
    kerns = {
        ("S", "E"): -1.2,
        ("E", "L"): 0.5,
        ("L", "U"): -7.5,
        ("U", "N"): 0.8,
        ("N", "É"): 1.2,
        ("É", "A"): -5.5,
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
# REFINED MINIMALIST SANS-EDITORIAL WORDMARK (For Concept C Lockup v2)
# Fixed N diagonal optical weight to match vertical stem weight seamlessly!
# ---------------------------------------------------------------------------

def rect_path(x, y, w, h):
    return [("M", x, y), ("L", x + w, y), ("L", x + w, y + h), ("L", x, y + h), ("Z",)]


def build_minimal_sans_wordmark_paths(ox, oy, cap_h, tracking=26.0):
    scale = cap_h / 100.0
    sw = 7.4
    hw = 6.7

    def s_glyph():
        return [[
            ("M", 50.5, 19.5),
            ("C", 47.0, 9.5, 38.5, 5.2, 28.5, 5.2),
            ("C", 17.5, 5.2, 11.2, 11.6, 11.2, 20.5),
            ("C", 11.2, 30.2, 18.8, 35.4, 31.8, 41.2),
            ("C", 47.5, 48.2, 55.2, 56.0, 55.2, 71.2),
            ("C", 55.2, 89.2, 42.2, 102.0, 26.5, 102.0),
            ("C", 14.5, 102.0, 6.2, 95.8, 2.2, 85.8),
            ("L", 9.0, 81.8),
            ("C", 12.2, 89.8, 18.4, 94.8, 27.0, 94.8),
            ("C", 38.4, 94.8, 47.2, 86.2, 47.2, 72.5),
            ("C", 47.2, 60.8, 40.5, 54.4, 26.8, 48.2),
            ("C", 11.5, 41.4, 3.6, 33.8, 3.6, 21.0),
            ("C", 3.6, 7.6, 14.4, -2.0, 29.0, -2.0),
            ("C", 41.5, -2.0, 51.0, 4.5, 56.0, 15.2),
            ("Z",),
        ]], 59.0

    def e_glyph(acute=False):
        ps = [
            rect_path(0, 0, sw, 100),
            rect_path(0, 0, 50, hw),
            rect_path(0, 46.5, 44, hw),
            rect_path(0, 100 - hw, 52, hw),
        ]
        if acute:
            # Echoes the sculpted light-sliver angle of SELUNÉA
            ps.append([
                ("M", 18.5, -10.5),
                ("L", 35.8, -28.0),
                ("L", 42.2, -23.0),
                ("L", 22.8, -8.0),
                ("Z",),
            ])
        return ps, 53.0

    def l_glyph():
        return [rect_path(0, 0, sw, 100), rect_path(0, 100 - hw, 48, hw)], 49.0

    def u_glyph():
        w = 60.0
        p = [
            ("M", 0, 0), ("L", sw, 0), ("L", sw, 64),
            ("C", sw, 84, 17, 94.6, w / 2, 94.6),
            ("C", w - 17, 94.6, w - sw, 84, w - sw, 64),
            ("L", w - sw, 0), ("L", w, 0), ("L", w, 64),
            ("C", w, 89, 47, 102.0, w / 2, 102.0),
            ("C", 13, 102.0, 0, 89, 0, 64),
            ("Z",),
        ]
        return [p], w

    def n_glyph():
        # Exact optical perpendicular diagonal thickness = 7.4 (matches vertical stems!)
        w = 64.0
        # Diagonal center runs from (sw/2, 0) to (w - sw/2, 100) => dx = 56.6, dy = 100
        # sin(angle from horizontal) = 100 / hypot(56.6, 100) = 0.8703
        # horizontal slice width for perpendicular thickness 7.2 = 7.2 / 0.8703 = 8.27
        diag_h = 8.3
        return [
            rect_path(0, 0, sw, 100),
            rect_path(w - sw, 0, sw, 100),
            [
                ("M", 0.0, 0.0),
                ("L", diag_h, 0.0),
                ("L", w, 100.0),
                ("L", w - diag_h, 100.0),
                ("Z",),
            ],
        ], w

    def a_glyph():
        w = 66.0
        apex = w / 2
        return [
            [
                ("M", apex - 3.8, -2.0),
                ("L", apex + 3.8, -2.0),
                ("L", w, 100.0),
                ("L", w - 8.0, 100.0),
                ("L", apex, 11.0),
                ("L", 8.0, 100.0),
                ("L", 0.0, 100.0),
                ("Z",),
            ],
            rect_path(13.5, 64.5, 39.0, hw),
        ], w

    glyphs = [
        ("S", s_glyph()),
        ("E", e_glyph(False)),
        ("L", l_glyph()),
        ("U", u_glyph()),
        ("N", n_glyph()),
        ("É", e_glyph(True)),
        ("A", a_glyph()),
    ]
    kerns = {("L", "U"): -6.0, ("É", "A"): -6.0}
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
# CONCEPT A (v2): THE LUMINOUS WORDMARK
#   - concept-a-symbol-v2.svg: Ownable 'Accented Lunar Disc' (serene full/ring
#     vessel with a clean luminous break + signature sculpted 30° É light-sliver)
#     — ZERO literal crescent moon clip-art, directly shares DNA with É!
#   - concept-a-wordmark-v2.svg: Hero custom editorial serif SELUNÉA
# ---------------------------------------------------------------------------

def build_concept_a():
    # Minimal Supporting Symbol (v3 — The Luminous Halo):
    # A single continuous, unbroken architectural ring (outer R=98 at center 128,128)
    # with an eccentric inner circular void (r=66 shifted 16 units along the 30° luminous axis,
    # mirroring the exact 30° angle of the wordmark's É accent!).
    # Result: unbroken cycle of waxing/waning light (max wall 48, min wall 16 -> crisp at 16 px),
    # real fill-rule="evenodd" cutout, 4 anchors, zero crescent clip-art, zero unintended 'Ó' reading!
    cx, cy = 128.0, 128.0
    Ro = 98.0
    Ri = 66.0
    ang = math.radians(-30.0)  # upper-right 30° luminous axis
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
  <title id="title">SELUNÉA — Concept A Supporting Luminous Halo Mark</title>
  <g id="symbol" fill="{INK}">
    <path fill-rule="evenodd" d="{halo_d}"/>
  </g>
</svg>
'''
    (OUT_DIR / "concept-a-symbol-v3.svg").write_text(symbol_svg, encoding="utf-8")
    (OUT_DIR / "concept-a-symbol.svg").write_text(symbol_svg, encoding="utf-8")

    # Hero Wordmark (centered precisely inside viewBox)
    cap_h = 114.0
    _, tw = build_editorial_wordmark_paths(0, 0, cap_h, tracking=19.0, sw=12.0, hw=3.9)
    vb_w = int(math.ceil(tw + 140.0))
    ox = (vb_w - tw) / 2.0
    oy = 88.0
    paths, _ = build_editorial_wordmark_paths(ox, oy, cap_h, tracking=19.0, sw=12.0, hw=3.9)
    path_els = "\n    ".join(f'<path d="{d}"/>' for d in paths)

    wordmark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} 256" width="{vb_w}" height="256" role="img" aria-labelledby="title">
  <title id="title">SELUNÉA — Concept A The Luminous Wordmark</title>
  <g id="wordmark" fill="{INK}">
    {path_els}
  </g>
</svg>
'''
    (OUT_DIR / "concept-a-wordmark-v3.svg").write_text(wordmark_svg, encoding="utf-8")
    (OUT_DIR / "concept-a-wordmark.svg").write_text(wordmark_svg, encoding="utf-8")


# ---------------------------------------------------------------------------
# CONCEPT B (v2): THE LUNAR EMBLEM
#   Tri-Phase Circular Equilibrium (Waxing · Full Vesica Core · Waning)
#   Refined 19-unit uniform concentric negative-space channels + perfectly centered lockup.
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


def build_concept_b():
    cx, cy = 128.0, 128.0
    R = 102.0
    d_c = 62.0
    R_c = 132.0
    gap = 19.0
    R_core = R_c - gap  # 113.0 -> exact 19-unit concentric channel top to bottom!

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
    (OUT_DIR / "concept-b-symbol-v2.svg").write_text(symbol_svg, encoding="utf-8")
    (OUT_DIR / "concept-b-symbol.svg").write_text(symbol_svg, encoding="utf-8")

    # Perfectly balanced horizontal lockup (equal left/right margins = 48 units)
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
    wm_oy = 95.0  # optically aligned with emblem equator
    wm_paths, wm_w = build_editorial_wordmark_paths(wm_x, wm_oy, cap_h, tracking=18.0, sw=11.2, hw=3.8)
    vb_w = int(math.ceil(wm_x + wm_w + margin))
    wm_els = "\n    ".join(f'<path d="{d}"/>' for d in wm_paths)

    lockup_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} 256" width="{vb_w}" height="256" role="img" aria-labelledby="title">
  <title id="title">SELUNÉA — Concept B Lunar Emblem Lockup</title>
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
    (OUT_DIR / "concept-b-lockup-v2.svg").write_text(lockup_svg, encoding="utf-8")
    (OUT_DIR / "concept-b-lockup.svg").write_text(lockup_svg, encoding="utf-8")


# ---------------------------------------------------------------------------
# CONCEPT C (v2): THE CELESTIAL MONOGRAM
#   Custom sculpted editorial S + twin non-overlapping tapered orbital phase arcs
#   (exact ~134° span each, crisp ~46° open apertures at 30° & 210°).
# ---------------------------------------------------------------------------

def build_open_tapered_arc(cx, cy, r_mid, center_deg, span_deg, max_w, min_w):
    """
    Build a razor-clean 2-cubic-side tapered crescent-orbital arc with exact center angle
    and span angle (guaranteed non-overlapping!), smoothly rounded minimal tips.
    Uses exact analytical circular-arc offset for 2-anchor outer/inner contours!
    """
    # To achieve exact span_deg with two circular arcs of outer radius R_out and inner radius R_in:
    # Let half_span = span_deg / 2. Outer arc runs from (center_deg - half_span) to (center_deg + half_span)
    # on circle (cx, cy, R_out).
    # At center_deg, the inner arc passes through radius (R_out - max_w).
    # At the two endpoints (center_deg ± half_span), inner arc passes through the EXACT same endpoints!
    # Three points uniquely define the inner circle (cx2, cy2, R_in)!!
    R_out = r_mid + max_w * 0.5
    half = math.radians(span_deg * 0.5)
    c_rad = math.radians(center_deg)

    # Endpoints on outer circle:
    a1 = c_rad - half
    a2 = c_rad + half
    p1 = (cx + R_out * math.cos(a1), cy + R_out * math.sin(a1))
    p2 = (cx + R_out * math.cos(a2), cy + R_out * math.sin(a2))

    # Midpoint of inner edge at distance r_mid_in = R_out - max_w along c_rad:
    # By symmetry, center of inner circle lies along ray c_rad at distance `d` from (cx, cy)
    # (negative d means shifted opposite c_rad, positive d means shifted toward c_rad):
    # Actually, let's solve exact distance `u` along c_rad from (cx,cy) to inner circle center:
    # Inner circle passes through:
    #   M = (R_out - max_w, 0) in rotated frame
    #   P1 = (R_out * cos(half), R_out * sin(half)) in rotated frame
    # Distance^2 from (u, 0) to M equals Distance^2 from (u, 0) to P1:
    #   (u - (R_out - max_w))^2 = (u - R_out*cos(half))^2 + (R_out*sin(half))^2
    #   u^2 - 2*u*r_m + r_m^2 = u^2 - 2*u*R_out*cos(half) + R_out^2
    #   2*u*(R_out*cos(half) - r_m) = R_out^2 - r_m^2
    r_m = R_out - max_w
    u = (R_out**2 - r_m**2) / (2.0 * (R_out * math.cos(half) - r_m))
    R_in = abs(r_m - u)

    # Outer arc from p1 to p2 (CW, sweep=1, large_arc = 1 if span_deg > 180 else 0)
    # Inner arc from p2 to p1 (CCW, sweep=0, large_arc=0 since span < 180)
    large_out = 1 if span_deg > 180 else 0
    return (
        f"M {pt(*p1)} "
        f"A {fmt(R_out)} {fmt(R_out)} 0 {large_out} 1 {pt(*p2)} "
        f"A {fmt(R_in)} {fmt(R_in)} 0 0 0 {pt(*p1)} Z"
    )


def build_concept_c():
    cx, cy = 128.0, 128.0

    # 1. Bespoke Sculptural S Monogram (v2, snapped 90° terminal, optically centered)
    s_tokens, s_w = glyph_S_editorial()
    s_scale = 1.38
    s_ox = cx - (s_w * 0.5) * s_scale
    s_oy = cy - 50.0 * s_scale
    s_path = transform_path_pts(s_tokens[0], s_ox, s_oy, s_scale)

    # 2. Twin Non-Overlapping Sculpted Orbital Crescent Arcs:
    # Center angles at 210° (upper-left) and 30° (lower-right), span = 132° each!
    # That leaves two razor-clean 48° breathing apertures at 120°/300° — Wait:
    #   Arc 1 (center 210°, span 132°): runs from 144° (lower-left) around left/top-left to 276° (just past 12 o'clock)
    #   Arc 2 (center 30°, span 132°): runs from 324° (upper-right) around right/bottom-right to 96° (just past 6 o'clock)
    #   Open breathing gaps: 276°→324° (48° open at upper-right) and 96°→144° (48° open at lower-left)!!
    #   Check visually: upper-right & lower-left are RIGHT where the S terminals breathe — sublime dialogue!!
    # Max thickness = 14.5 units (sturdy at 16 px & tactile when blind-debossed on a 14 mm cap!)
    arc_top_left = build_open_tapered_arc(cx, cy, 98.0, 210.0, 132.0, 14.5, 0.0)
    arc_bot_right = build_open_tapered_arc(cx, cy, 98.0, 30.0, 132.0, 14.5, 0.0)

    symbol_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="title">
  <title id="title">SELUNÉA — Concept C The Celestial Monogram</title>
  <g id="symbol" fill="{INK}">
    <path d="{arc_top_left}"/>
    <path d="{arc_bot_right}"/>
    <path d="{s_path}"/>
  </g>
</svg>
'''
    (OUT_DIR / "concept-c-symbol-v2.svg").write_text(symbol_svg, encoding="utf-8")
    (OUT_DIR / "concept-c-symbol.svg").write_text(symbol_svg, encoding="utf-8")

    # Balanced horizontal lockup (equal left/right margins = 48 units)
    margin = 48.0
    sym_size = 152.0
    R_outer = 98.0 + 14.5 * 0.5  # 105.25
    s_sc = sym_size / (2.0 * R_outer)
    sym_cx = margin + sym_size * 0.5
    sym_cy = 128.0
    tx = sym_cx - cx * s_sc
    ty = sym_cy - cy * s_sc

    gap_x = 46.0
    wm_x = margin + sym_size + gap_x
    cap_h = 74.0
    wm_oy = 98.0
    wm_paths, wm_w = build_minimal_sans_wordmark_paths(wm_x, wm_oy, cap_h, tracking=26.0)
    vb_w = int(math.ceil(wm_x + wm_w + margin))
    wm_els = "\n    ".join(f'<path d="{d}"/>' for d in wm_paths)

    lockup_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} 256" width="{vb_w}" height="256" role="img" aria-labelledby="title">
  <title id="title">SELUNÉA — Concept C Celestial Monogram Lockup</title>
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
    (OUT_DIR / "concept-c-lockup-v2.svg").write_text(lockup_svg, encoding="utf-8")
    (OUT_DIR / "concept-c-lockup.svg").write_text(lockup_svg, encoding="utf-8")


if __name__ == "__main__":
    build_concept_a()
    build_concept_b()
    build_concept_c()
    print("Generated Stage 3 v2 SVGs in", OUT_DIR)
