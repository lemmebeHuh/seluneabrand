"""
SELUNÉA — Client-Style Brand Mark Exploration (5 Delicate Feminine Skincare Options)
Synthesizes the aesthetic DNA of the client's 3 references (VŌW, mora, sérea, BRISIA,
SĀNIA, DHIMĪ): airy monoline interlacing, rhythmic radiant lunar rays, graceful symmetric
beauty emblems, and fine-framed S crests — translated into 100% ORIGINAL SELUNÉA
("Lunar Elegance") marks paired with the approved SELUNÉA Couture Wordmark.

5 Options:
  01. Lunar Halo Rays      — Modulated radiant moonbeam ring (gorgeous on round jar lids!)
  02. Woven Lunar Drop     — Airy monoline skincare droplet woven with intersecting moon-phase arcs
  03. Celestial Lotus-Moon — Graceful 4-fold symmetric monoline lunar-petal emblem
  04. Orbital S Crest      — SELUNÉA's couture high-contrast S cradled inside a fine lunar droplet-orbit frame
  05. Continuous Lunar Knot — Unbroken flowing monoline 4-phase loop (cyclical self-care)
"""

import math
import sys
from pathlib import Path

BASE = Path(r"c:\Users\ridwa\Desktop\selunea\selunea-brand-identity")
OUT = BASE / "04-logo-concepts" / "brand-mark-client-style"
OUT.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(BASE / "12-source-files"))
import build_stage5_logo_system as s5

INK = "#34332F"


def fmt(n: float) -> str:
    s = f"{n:.2f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def pt(x: float, y: float) -> str:
    return f"{fmt(x)} {fmt(y)}"


def write_svg(path: Path, vb_w: int, vb_h: int, title: str, body: str):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} {vb_h}" width="{vb_w}" height="{vb_h}" role="img" aria-labelledby="title">
  <title id="title">{title}</title>
{body}
</svg>
'''
    path.write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------------------
# GEOMETRIC HELPERS FOR CLEAN FILLED STROKES & MODULATED RAYS (NO UNEXPANDED STROKE!)
# ---------------------------------------------------------------------------

def poly_offset_closed(pts, half_w):
    """Expand a closed smooth polyline into outer & inner rings (evenodd filled outline!)."""
    n = len(pts)
    outer, inner = [], []
    for i in range(n):
        p_prev = pts[(i - 1) % n]
        p_curr = pts[i]
        p_next = pts[(i + 1) % n]
        dx1, dy1 = p_curr[0] - p_prev[0], p_curr[1] - p_prev[1]
        l1 = math.hypot(dx1, dy1) or 1.0
        dx2, dy2 = p_next[0] - p_curr[0], p_next[1] - p_curr[1]
        l2 = math.hypot(dx2, dy2) or 1.0
        # Average unit normal
        nx = -(dy1 / l1 + dy2 / l2)
        ny = (dx1 / l1 + dx2 / l2)
        nl = math.hypot(nx, ny) or 1.0
        nx, ny = nx / nl, ny / nl
        outer.append((p_curr[0] + nx * half_w, p_curr[1] + ny * half_w))
        inner.append((p_curr[0] - nx * half_w, p_curr[1] - ny * half_w))
    d_out = "M " + " L ".join(pt(*p) for p in outer) + " Z"
    d_in = "M " + " L ".join(pt(*p) for p in reversed(inner)) + " Z"
    return f"{d_out} {d_in}"


def ribbon_open_path(pts, half_w, round_caps=True):
    """Expand an open smooth polyline into a clean filled vector ribbon path."""
    n = len(pts)
    left, right = [], []
    for i in range(n):
        if i == 0:
            dx, dy = pts[1][0] - pts[0][0], pts[1][1] - pts[0][1]
        elif i == n - 1:
            dx, dy = pts[-1][0] - pts[-2][0], pts[-1][1] - pts[-2][1]
        else:
            dx, dy = pts[i + 1][0] - pts[i - 1][0], pts[i + 1][1] - pts[i - 1][1]
        l = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / l, dx / l
        left.append((pts[i][0] + nx * half_w, pts[i][1] + ny * half_w))
        right.append((pts[i][0] - nx * half_w, pts[i][1] - ny * half_w))
    if round_caps:
        d = (
            f"M {pt(*left[0])} "
            + " ".join(f"L {pt(*p)}" for p in left[1:])
            + f" A {fmt(half_w)} {fmt(half_w)} 0 0 1 {pt(*right[-1])} "
            + " ".join(f"L {pt(*p)}" for p in reversed(right[:-1]))
            + f" A {fmt(half_w)} {fmt(half_w)} 0 0 1 {pt(*left[0])} Z"
        )
    else:
        d = (
            f"M {pt(*left[0])} "
            + " ".join(f"L {pt(*p)}" for p in left[1:])
            + f" L {pt(*right[-1])} "
            + " ".join(f"L {pt(*p)}" for p in reversed(right[:-1]))
            + " Z"
        )
    return d


def sample_cubic(p0, p1, p2, p3, steps=28):
    out = []
    for i in range(steps + 1):
        t = i / steps
        mt = 1.0 - t
        x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
        out.append((x, y))
    return out


# ---------------------------------------------------------------------------
# OPTION 01: LUNAR HALO RAYS (Radiant Modulated Moonbeam Ring — Mora-Inspired Elegance!)
# 24 rhythmic radial moonbeams arranged around a serene open circular center.
# Unlike a plain sun, the beam weights modulate smoothly along a 30° lunar phase axis
# (lush wide glowing beams on the waxing side tapering to delicate moonlight threads on
# the waning side) — unmistakably lunar, ultra-luxe on jar lids & cartons!
# ---------------------------------------------------------------------------

def build_client_opt1():
    cx, cy = 128.0, 128.0
    r_in = 46.0
    r_out = 102.0
    n_rays = 24
    # Lunar radiance axis at -30° (upper-right waxing peak -> lower-left delicate waning)
    phase_axis = math.radians(-30.0)
    paths = []

    for i in range(n_rays):
        ang = (2.0 * math.pi * i) / n_rays
        # Cosine alignment with lunar axis: +1 at waxing peak, -1 at waning rest
        align = math.cos(ang - phase_axis)
        # Smooth organic modulation: half-angle of each ray varies from delicate 2.4° to bold 5.6°
        # plus subtle radial inner/outer rhythm for artisanal beauty feel!
        half_ang = math.radians(2.2 + 3.0 * ((align + 1.0) * 0.5) ** 1.4)
        # Slight alternating length cadence (long/medium) for airy couture sparkle
        r_tip = r_out if (i % 2 == 0) else (r_out - 9.0)
        # Inner radius slightly narrower on waxing side so the center feels gently crescent-lit!
        r_base = r_in - 3.5 * align

        # Crisp tapered wedge ray (slightly wider at outer rim than inner base)
        ha_in = half_ang * 0.62
        ha_out = half_ang * 1.05

        p1 = (cx + r_base * math.cos(ang - ha_in), cy + r_base * math.sin(ang - ha_in))
        p2 = (cx + r_tip * math.cos(ang - ha_out), cy + r_tip * math.sin(ang - ha_out))
        p3 = (cx + r_tip * math.cos(ang + ha_out), cy + r_tip * math.sin(ang + ha_out))
        p4 = (cx + r_base * math.cos(ang + ha_in), cy + r_base * math.sin(ang + ha_in))

        d = f"M {pt(*p1)} L {pt(*p2)} A {fmt(r_tip)} {fmt(r_tip)} 0 0 1 {pt(*p3)} L {pt(*p4)} A {fmt(r_base)} {fmt(r_base)} 0 0 0 {pt(*p1)} Z"
        paths.append(f'<path d="{d}"/>')

    return paths


# ---------------------------------------------------------------------------
# OPTION 02: WOVEN LUNAR DROP (Airy Monoline Skincare Droplet + Moon Phases — VŌW-Inspired!)
# A graceful teardrop silhouette woven internally by balanced intersecting lunar arcs
# and a quiet central luminous vesica — feels pure skincare, airy, botanical-lunar luxury!
# ---------------------------------------------------------------------------

def build_client_opt2():
    # Clean crisp monoline stroke width = 7.4 units on 256x256 (delicate yet strong on print!)
    sw = 7.4
    # Outer teardrop silhouette: apex (128, 28), rounded lower bowl centered at (128, 152), R=76
    outer_d = (
        "M 128 28 "
        "C 156 68 204 106 204 152 "
        "A 76 76 0 1 1 52 152 "
        "C 52 106 100 68 128 28 Z"
    )
    # Exact boundary-to-boundary woven lunar arcs (zero floating endpoints!):
    # 1. Central serene vertical lunar vesica rising cleanly from base (128, 228) to inner peak (128, 76)
    inner_left = "M 128 228 C 90 194 92 128 128 76"
    inner_right = "M 128 228 C 166 194 164 128 128 76"
    # 2. Symmetric woven waxing/waning sweeps connecting exact lower arc points (40° from base)
    #    to exact opposite upper shoulder points (t=0.35 on outer cubic) — silky lattice!
    side_left = "M 79.15 210.22 C 88 156 126 122 189.27 106.2"
    side_right = "M 176.85 210.22 C 168 156 130 122 66.73 106.2"
    # 3. Quiet luminous lunar pearl nestled in the lower vesica chamber (128, 174)
    pearl = "M 128 166.5 A 7.5 7.5 0 1 1 128 181.5 A 7.5 7.5 0 1 1 128 166.5 Z"

    return [
        f'<g fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">',
        f'  <path d="{outer_d}"/>',
        f'  <path d="{inner_left}"/>',
        f'  <path d="{inner_right}"/>',
        f'  <path d="{side_left}"/>',
        f'  <path d="{side_right}"/>',
        f'</g>',
        f'<path fill="{INK}" d="{pearl}"/>',
    ]


# ---------------------------------------------------------------------------
# OPTION 03: CELESTIAL LOTUS-MOON (Symmetric Airy Monoline Beauty Crest — BRISIA/Sérea-Inspired!)
# Four overlapping/interlaced fine-line lunar petal-rings arranged in poised 4-fold symmetry,
# plus 4 subtle corner phase arcs — pure feminine skincare couture emblem!
# ---------------------------------------------------------------------------

def build_client_opt3():
    cx, cy = 128.0, 128.0
    sw = 7.2
    paths = [f'<g fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">']

    # 4 primary pointed-lunar petals along N, E, S, W (smooth vesica petals from center out to R=96)
    for deg in (0, 90, 180, 270):
        rad = math.radians(deg)
        c, s = math.cos(rad), math.sin(rad)
        def rot(x, y): return (cx + x * c - y * s, cy + x * s + y * c)
        p0 = rot(0, 0)
        p_tip = rot(96, 0)
        c1 = rot(34, -44)
        c2 = rot(72, -32)
        c3 = rot(72, 32)
        c4 = rot(34, 44)
        d = f"M {pt(*p0)} C {pt(*c1)} {pt(*c2)} {pt(*p_tip)} C {pt(*c3)} {pt(*c4)} {pt(*p0)} Z"
        paths.append(f'  <path d="{d}"/>')

    # 4 secondary softer crescent-petals nestled diagonally at 45°, 135°, 225°, 315° (reaching R=80)
    for deg in (45, 135, 225, 315):
        rad = math.radians(deg)
        c, s = math.cos(rad), math.sin(rad)
        def rot(x, y): return (cx + x * c - y * s, cy + x * s + y * c)
        p_start = rot(36, -18)
        p_tip = rot(82, 0)
        p_end = rot(36, 18)
        c1 = rot(58, -32)
        c2 = rot(76, -20)
        c3 = rot(76, 20)
        c4 = rot(58, 32)
        d = f"M {pt(*p_start)} C {pt(*c1)} {pt(*c2)} {pt(*p_tip)} C {pt(*c3)} {pt(*c4)} {pt(*p_end)}"
        paths.append(f'  <path d="{d}"/>')

    paths.append('</g>')
    # Quiet luminous pearl core in the center
    paths.append(f'<circle cx="128" cy="128" r="9" fill="{INK}"/>')
    return paths


# ---------------------------------------------------------------------------
# OPTION 04: ORBITAL S CREST (Refined Teardrop-Framed Couture S — SĀNIA-Inspired, 100% SELUNÉA!)
# SELUNÉA's exact couture high-contrast serif-less S framed inside a serene fine-line
# skincare-droplet crest paired with a delicate eccentric lunar-orbit halo line!
# ---------------------------------------------------------------------------

def build_client_opt4():
    # Outer serene skincare droplet frame (fine-line architectural elegance, stroke=6.4)
    drop_d = (
        "M 128 24 "
        "C 158 66 206 106 206 154 "
        "A 78 78 0 1 1 50 154 "
        "C 50 106 98 66 128 24 Z"
    )
    # Crisp 100%-opaque fine lunar crescent contour hugging the lower-left curve (print-ready, no opacity!)
    inner_arc = "M 67 166 A 64 64 0 0 0 152 214"

    # SELUNÉA's exact Couture High-Contrast S optically centered in the droplet belly
    s_tokens, s_w = s5.glyph_S_hc()
    s_sc = 1.02
    s_ox = 128.0 - (s_w * 0.5) * s_sc
    s_oy = 156.5 - 50.0 * s_sc
    s_d = s5.transform_path_pts(s_tokens[0], s_ox, s_oy, s_sc)

    return [
        f'<g fill="none" stroke="{INK}" stroke-linecap="round" stroke-linejoin="round">',
        f'  <path d="{drop_d}" stroke-width="6.4"/>',
        f'  <path d="{inner_arc}" stroke-width="3.0"/>',
        f'</g>',
        f'<path fill="{INK}" d="{s_d}"/>',
    ]


# ---------------------------------------------------------------------------
# OPTION 05: CONTINUOUS LUNAR KNOT (Unbroken Monoline 4-Phase Ribbon — DHIMĪ-Inspired!)
# One continuous, hypnotic, perfectly symmetric monoline ribbon looping seamlessly
# through 4 gentle lunar-crescent lobes — pure minimal couture skincare emblem!
# ---------------------------------------------------------------------------

def build_client_opt5():
    # Parametric continuous 4-lobe lunar knot (epitrochoid/rosette-inspired smooth closed curve!)
    # r(t) = R0 + A * cos(4t) with looped corners:
    # Classic sculptural beauty knot:
    # x(t) = 128 + 64*cos(t) + 28*cos(3t)  (Wait: cos(t) + cos(3t) has 2 lobes; for 4 symmetric rounded
    # corner loops like a luxury couture emblem: x(t) = 128 + R1*cos(t) - R2*cos(3t), y(t) = 128 + R1*sin(t) + R2*sin(3t)
    # Wait: let's check hypotrochoid / epitrochoid with 4-fold symmetry!
    # Epitrochoid with k=4 loops around center:
    #   x(t) = 128 + 58*cos(t) - 34*cos(5t)? No, let's check:
    #   k=4 inward-looping knot (like a luxury quatrefoil silk ribbon):
    #   x(t) = 128 + 62*cos(t) + 28*cos(3t) -> let's test the exact 4-loop curve:
    #   For 4-fold symmetry under 90° rotation: frequency difference must be 4 -> (cos(t), sin(t)) and (cos(-3t), sin(-3t))!
    #   YES!! Check rotation by +90°: t -> t + pi/2:
    #     cos(t + pi/2) = -sin(t), sin(t + pi/2) = cos(t)
    #     cos(-3t - 3pi/2) = -sin(-3t) = sin(3t), sin(-3t - 3pi/2) = cos(-3t) = cos(3t)
    #   SO: x(t) = 128 + A*cos(t) + B*cos(3t)  and  y(t) = 128 + A*sin(t) - B*sin(3t)!!
    #   WAIT A SECOND!! Check (A=60, B=34) rotated 45°:
    #   At t=0: (128+94, 128) = outer tip 94!
    #   When B > A/3 (34 > 20), it forms 4 GRACEFUL, IDENTICAL, ROUNDED SILK LOOPS at the 4 corners
    #   with gentle concave lunar arcs bridging them around a serene open square-diamond heart!!
    #   AND it is ONE SINGLE UNBROKEN CONTINUOUS MATHEMATICAL LINE!!
    cx, cy = 128.0, 128.0
    # Scaled cleanly so the 45°-rotated 4-lobe knot fills ~74% of the 256x256 canvas
    # with generous, airy luxury corner loops (margins ~31px, matching Options 01-04)
    A, B = 78.0, 46.0
    rot_off = math.pi / 4.0  # 45° poise so 4 loops sit gracefully at NE, SE, SW, NW!
    steps = 160
    pts = []
    for i in range(steps):
        t = (2.0 * math.pi * i) / steps
        x0 = A * math.cos(t) + B * math.cos(3.0 * t)
        y0 = A * math.sin(t) - B * math.sin(3.0 * t)
        # Rotate by 45°
        xr = x0 * math.cos(rot_off) - y0 * math.sin(rot_off)
        yr = x0 * math.sin(rot_off) + y0 * math.cos(rot_off)
        pts.append((cx + xr, cy + yr))

    # Build smooth SVG path (close cleanly)
    d = "M " + " L ".join(pt(*p) for p in pts) + " Z"
    return [
        f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="7.8" stroke-linecap="round" stroke-linejoin="round"/>',
        f'<circle cx="128" cy="128" r="9.5" fill="{INK}"/>',
    ]


def build_lockup(mark_xml_list, filename, title):
    margin = 48.0
    sym_size = 148.0
    s_sc = sym_size / 204.0
    tx = (margin + sym_size * 0.5) - 128.0 * s_sc
    ty = 128.0 - 128.0 * s_sc
    wm_x = margin + sym_size + 46.0
    h_cap = 86.0
    h_oy = 88.0
    wm_paths, h_wm_w = s5.build_wordmark(wm_x, h_oy, h_cap, tracking=20.0, couture=True, sw=12.6, hw=3.8)
    vb_w = int(math.ceil(wm_x + h_wm_w + margin))

    mark_xml = "\n    ".join(mark_xml_list)
    wm_xml = "\n    ".join(f'<path d="{d}"/>' for d in wm_paths)
    body = (
        f'  <g id="symbol" transform="translate({fmt(tx)} {fmt(ty)}) scale({fmt(s_sc)})">\n'
        f'    {mark_xml}\n'
        f'  </g>\n'
        f'  <g id="wordmark" fill="{INK}">\n'
        f'    {wm_xml}\n'
        f'  </g>'
    )
    write_svg(OUT / filename, vb_w, 256, title, body)


def build_5_option_board(options):
    cards = []
    for num, name, ref_vibe, idea, sym_f, lock_f in options:
        sym_svg = (OUT / sym_f).read_text(encoding="utf-8")
        lock_svg = (OUT / lock_f).read_text(encoding="utf-8")
        sym_ivory = sym_svg.replace(INK, "#F3F0E9")
        sym_champ = sym_svg.replace(INK, "#C8B9A6")

        cards.append(f"""
        <article class="card">
          <div class="card-top">
            <span class="num">OPTION {num}</span>
            <span class="tag">{ref_vibe}</span>
          </div>
          <div class="stage-row">
            <div class="box-light">{sym_svg}</div>
            <div class="box-lid" title="Jar Lid Preview">
              <div class="jar-lid-mock">{sym_champ}</div>
              <span class="mini-cap">Jar Lid Foil</span>
            </div>
            <div class="box-dark">
              {sym_ivory}
              <span class="mini-cap">Midnight Ash</span>
            </div>
          </div>
          <div class="lockup-strip">{lock_svg}</div>
          <div class="meta-row">
            <div class="info">
              <h3>{name}</h3>
              <p>{idea}</p>
            </div>
            <div class="scales">
              <div class="sc"><div class="s48">{sym_svg}</div><span>48</span></div>
              <div class="sc"><div class="s24">{sym_svg}</div><span>24</span></div>
            </div>
          </div>
        </article>
        """)

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<title>SELUNÉA — 5 Client-Style Brand Mark Options</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet" />
<style>
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{
    background:#F3F0E9; color:#34332F; font-family:'DM Sans',sans-serif;
    width:1560px; padding:48px 54px 56px; -webkit-font-smoothing:antialiased;
  }}
  header {{
    display:flex; justify-content:space-between; align-items:flex-end;
    padding-bottom:22px; border-bottom:1px solid rgba(52,51,47,0.14); margin-bottom:28px;
  }}
  .eyebrow {{ font-size:11px; letter-spacing:0.2em; text-transform:uppercase; color:#5B5953; margin-bottom:6px; }}
  h1 {{ font-family:'Cormorant Garamond',serif; font-size:44px; font-weight:500; line-height:1.05; }}
  h1 em {{ font-style:italic; font-weight:400; }}
  .sub {{ font-size:12.5px; color:#5B5953; text-align:right; line-height:1.6; }}

  /* Top 3 cards + Bottom 2 centered wide cards */
  .grid-top {{ display:grid; grid-template-columns:repeat(3, 1fr); gap:22px; margin-bottom:22px; }}
  .grid-bot {{ display:grid; grid-template-columns:repeat(2, 1fr); gap:22px; max-width:1040px; margin:0 auto; }}

  .card {{
    background:#FAF8F4; border:1px solid rgba(52,51,47,0.13); border-radius:16px;
    padding:20px 22px; display:flex; flex-direction:column; gap:14px;
  }}
  .card-top {{ display:flex; justify-content:space-between; align-items:center; font-size:10px; letter-spacing:0.16em; text-transform:uppercase; color:#5B5953; }}
  .num {{ font-weight:600; color:#34332F; }}
  .stage-row {{ display:grid; grid-template-columns:1.25fr 0.95fr 0.95fr; gap:10px; }}
  .box-light {{
    background:#FFFFFF; border:1px solid rgba(52,51,47,0.08); border-radius:12px;
    height:152px; display:flex; align-items:center; justify-content:center;
  }}
  .box-light svg {{ width:110px; height:110px; display:block; }}
  .box-lid {{
    background:linear-gradient(145deg,#EFECE4,#E3DDD1); border:1px solid rgba(52,51,47,0.08); border-radius:12px;
    height:152px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px;
  }}
  .jar-lid-mock {{
    width:92px; height:92px; border-radius:50%;
    background:radial-gradient(circle at 32% 28%, #474540, #34332F 68%, #242320);
    box-shadow:0 8px 18px rgba(52,51,47,0.22);
    display:flex; align-items:center; justify-content:center;
  }}
  .jar-lid-mock svg {{ width:58px; height:58px; display:block; }}
  .box-dark {{
    background:#34332F; border-radius:12px; height:152px;
    display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px;
  }}
  .box-dark svg {{ width:76px; height:76px; display:block; }}
  .mini-cap {{ font-size:8.5px; letter-spacing:0.14em; text-transform:uppercase; opacity:0.7; }}
  .box-dark .mini-cap {{ color:#C8B9A6; }}

  .lockup-strip {{
    background:#FFFFFF; border:1px solid rgba(52,51,47,0.08); border-radius:10px;
    padding:14px 16px; display:flex; align-items:center; justify-content:center;
  }}
  .lockup-strip svg {{ height:40px; width:auto; display:block; }}

  .meta-row {{
    display:flex; justify-content:space-between; align-items:flex-end; gap:14px;
    padding-top:10px; border-top:1px solid rgba(52,51,47,0.1);
  }}
  .info h3 {{ font-family:'Cormorant Garamond',serif; font-size:24px; font-weight:600; margin-bottom:4px; }}
  .info p {{ font-size:12px; color:#5B5953; line-height:1.5; }}
  .scales {{ display:flex; align-items:flex-end; gap:12px; flex-shrink:0; }}
  .sc {{ display:flex; flex-direction:column; align-items:center; gap:4px; font-size:9.5px; color:#5B5953; }}
  .s48 svg {{ width:42px; height:42px; display:block; }}
  .s24 svg {{ width:22px; height:22px; display:block; }}
</style>
</head>
<body>
  <header>
    <div>
      <div class="eyebrow">Client Reference Direction · Delicate Feminine Beauty Emblems</div>
      <h1>Five New <em>Beauty-Style</em> Brand Marks</h1>
    </div>
    <div class="sub">
      <strong>SELUNÉA · Presented for NANA · by KALLA</strong><br/>
      Inspired by airy monoline, radiant rays &amp; beauty crests — 100% Original Lunar Elegance
    </div>
  </header>

  <section class="grid-top">
    {"".join(cards[:3])}
  </section>
  <section class="grid-bot">
    {"".join(cards[3:])}
  </section>
</body>
</html>
"""
    (OUT / "selunea-brand-mark-client-style-5-options.html").write_text(html, encoding="utf-8")


def main():
    options = [
        (
            "01", "Lunar Halo Rays", "Radiant Moonbeam · Jar-Lid Hero",
            "24 sinar cahaya bulan termodulasi (lebih penuh di sisi waxing, halus di sisi waning) melingkari pusat tenang — sangat mewah di tutup jar & karton.",
            "client-opt1-lunar-halo-rays.svg", "client-lockup1-lunar-halo-rays.svg",
            build_client_opt1(),
        ),
        (
            "02", "Woven Lunar Drop", "Airy Monoline Droplet · Botanical-Lunar",
            "Tetes esens skincare monoline yang dianyam oleh busur fase bulan bersilangan dengan mutiara kecil di pusat — ringan, feminin, dan sangat skincare.",
            "client-opt2-woven-lunar-drop.svg", "client-lockup2-woven-lunar-drop.svg",
            build_client_opt2(),
        ),
        (
            "03", "Celestial Lotus-Moon", "Symmetric Fine-Line Beauty Crest",
            "Empat kelopak fase bulan monoline simetris berpadu busur sekunder halus dan inti mutiara — nuansa quiet-luxury beauty maison yang timeless.",
            "client-opt3-celestial-lotus-moon.svg", "client-lockup3-celestial-lotus-moon.svg",
            build_client_opt3(),
        ),
        (
            "04", "Orbital S Crest", "Framed Couture S · Droplet Seal",
            "Huruf S couture khas SELUNÉA dibingkai tetes monoline ramping dengan aksen garis sabit halus — langsung terbaca inisial S dan elegan untuk tutup botol.",
            "client-opt4-orbital-s-crest.svg", "client-lockup4-orbital-s-crest.svg",
            build_client_opt4(),
        ),
        (
            "05", "Continuous Lunar Knot", "Unbroken Monoline Ribbon · 4 Phases",
            "Satu garis kontinu tanpa putus yang mengalun membentuk 4 lengkung fase bulan simetris — melambangkan perawatan diri yang berkesinambungan.",
            "client-opt5-continuous-lunar-knot.svg", "client-lockup5-continuous-lunar-knot.svg",
            build_client_opt5(),
        ),
    ]

    for num, name, vibe, idea, sym_f, lock_f, xml_list in options:
        if num == "01":
            body = f'  <g id="symbol" fill="{INK}">\n    ' + "\n    ".join(xml_list) + "\n  </g>"
        else:
            body = '  <g id="symbol">\n    ' + "\n    ".join(xml_list) + "\n  </g>"
        write_svg(OUT / sym_f, 256, 256, f"SELUNÉA Client-Style Brand Mark {num} — {name}", body)
        build_lockup(xml_list, lock_f, f"SELUNÉA Client-Style Lockup {num} — {name}")

    build_5_option_board([(n, nm, vb, id_, sf, lf) for n, nm, vb, id_, sf, lf, _ in options])
    print("Generated 5 Client-Style Beauty Brand Marks in", OUT)


if __name__ == "__main__":
    main()
