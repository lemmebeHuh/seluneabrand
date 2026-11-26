"""
SELUNÉA — Brand Mark Exploration Options (4 Distinct Directions)
Pairs each candidate Brand Mark with the approved SELUNÉA Couture High-Contrast
Editorial Sans wordmark, keeping 100% pure vector <path> outlines (zero <text>,
zero <filter>, zero rasters, real fill-rule="evenodd" cutouts).

Options:
  1. Eclipse Halo        — Unbroken continuous eccentric ring (30° luminous axis)
  2. Lunar Equinox       — Offset dual-hemisphere horizon (day/night skin rhythm)
  3. Four-Phase Radiance — Soft 4-phase lunar bloom around a serene pearl negative-space core
  4. Dual-Phase S        — Two interlocking lunar phase arcs forming an iconic sculptural S
"""

import math
import sys
from pathlib import Path

BASE = Path(r"c:\Users\ridwa\Desktop\selunea\selunea-brand-identity")
OUT = BASE / "04-logo-concepts" / "brand-mark-options"
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
# OPTION 1: THE ECLIPSE HALO (Continuous Waxing–Waning Ring, 30° Axis)
# ---------------------------------------------------------------------------

def build_opt1_paths():
    cx, cy = 128.0, 128.0
    Ro, Ri = 98.0, 66.0
    ang = math.radians(-30.0)
    shift = 16.0
    ix = cx + shift * math.cos(ang)
    iy = cy + shift * math.sin(ang)
    d = (
        f"M {fmt(cx)} {fmt(cy - Ro)} "
        f"A {fmt(Ro)} {fmt(Ro)} 0 1 1 {fmt(cx)} {fmt(cy + Ro)} "
        f"A {fmt(Ro)} {fmt(Ro)} 0 1 1 {fmt(cx)} {fmt(cy - Ro)} Z "
        f"M {fmt(ix)} {fmt(iy - Ri)} "
        f"A {fmt(Ri)} {fmt(Ri)} 0 1 0 {fmt(ix)} {fmt(iy + Ri)} "
        f"A {fmt(Ri)} {fmt(Ri)} 0 1 0 {fmt(ix)} {fmt(iy - Ri)} Z"
    )
    return [f'<path fill-rule="evenodd" d="{d}"/>']


# ---------------------------------------------------------------------------
# OPTION 2: THE LUNAR EQUINOX (Offset Dual-Hemisphere Horizon)
# Two pure semicircular lunar phases gliding horizontally across a calm
# 18-unit negative-space horizon channel, subtly balanced by a quiet core void.
# ---------------------------------------------------------------------------

def build_opt2_paths():
    # Upper hemisphere: radius 88, flat horizon at y = 119, shifted right to cx = 140
    # Lower hemisphere: radius 88, flat horizon at y = 137, shifted left to cx = 116
    # Horizon negative-space channel = 18 units (crisp at 16 px!)
    # Total X span: 116 - 88 = 28 to 140 + 88 = 228 (exact L28/R28 symmetry!)
    # Total Y span: 119 - 88 = 31 to 137 + 88 = 225 (exact T31/B31 symmetry!)
    R = 88.0
    top_cx, top_y = 140.0, 119.0
    bot_cx, bot_y = 116.0, 137.0

    # Upper dome (from left end to right end arching upward: sweep=1)
    top_d = (
        f"M {fmt(top_cx - R)} {fmt(top_y)} "
        f"A {fmt(R)} {fmt(R)} 0 0 1 {fmt(top_cx + R)} {fmt(top_y)} Z"
    )
    # Lower dome (from right end to left end arching downward: sweep=1)
    bot_d = (
        f"M {fmt(bot_cx + R)} {fmt(bot_y)} "
        f"A {fmt(R)} {fmt(R)} 0 0 1 {fmt(bot_cx - R)} {fmt(bot_y)} Z"
    )
    return [f'<path d="{top_d}"/>', f'<path d="{bot_d}"/>']


# ---------------------------------------------------------------------------
# OPTION 3: FOUR-PHASE RADIANCE (Soft Sculptural Lunar Petal Vessel)
# Four identical pure-arc lunar phases arranged radially around a serene
# circular negative-space pearl core — soft feminine luxury, zero pointy sparkle!
# ---------------------------------------------------------------------------

def build_opt3_paths():
    # Four smooth, bold, sculptural lunar-phase petals arranged around a calm central pearl disc (r=20)
    # Each petal is a clean 2-arc convex-outer / concave-inner crescent-petal hugging R_outer=100,
    # separated by generous 20-unit negative-space light channels — soft feminine beauty luxury,
    # zero spiky AI-sparkle points, ultra-crisp even at 16 px!
    cx, cy = 128.0, 128.0
    paths = []
    R_out = 98.0
    r_inner = 42.0
    # 4 smooth rounded lunar petals along N, E, S, W (each 56 units wide, crisp 20-unit gaps)
    for deg in (0.0, 90.0, 180.0, 270.0):
        rad = math.radians(deg)
        c, s = math.cos(rad), math.sin(rad)
        def rot(x, y):
            return (cx + x * c - y * s, cy + x * s + y * c)
        # Local petal along +X from x=40 to x=100, smooth rounded lunar dome
        p_in_top = rot(42.0, -18.0)
        p_out_top = rot(78.0, -34.0)
        p_tip = rot(100.0, 0.0)
        p_out_bot = rot(78.0, 34.0)
        p_in_bot = rot(42.0, 18.0)
        p_c1 = rot(56.0, -36.0)
        p_c2 = rot(98.0, -26.0)
        p_c3 = rot(98.0, 26.0)
        p_c4 = rot(56.0, 36.0)
        p_in_mid = rot(49.0, 0.0)
        d = (
            f"M {pt(*p_in_top)} "
            f"C {pt(*p_c1)} {pt(*p_c2)} {pt(*p_tip)} "
            f"C {pt(*p_c3)} {pt(*p_c4)} {pt(*p_in_bot)} "
            f"Q {pt(*p_in_mid)} {pt(*p_in_top)} Z"
        )
        paths.append(f'<path d="{d}"/>')

    # Calm central full-phase pearl disc
    r_core = 22.0
    core_d = (
        f"M {fmt(cx)} {fmt(cy - r_core)} "
        f"A {fmt(r_core)} {fmt(r_core)} 0 1 1 {fmt(cx)} {fmt(cy + r_core)} "
        f"A {fmt(r_core)} {fmt(r_core)} 0 1 1 {fmt(cx)} {fmt(cy - r_core)} Z"
    )
    paths.append(f'<path d="{core_d}"/>')
    return paths


# ---------------------------------------------------------------------------
# OPTION 4: THE DUAL-PHASE S (Lush High-Contrast S Split by 30° Lunar Light-Cut)
# Two harmonious, thick-to-thin opposing lunar phase arcs forming an unmistakable
# couture S with a serene 30° diagonal negative-space light channel at center.
# ---------------------------------------------------------------------------

def build_opt4_paths():
    # Upper waxing crescent-arch sweeping cleanly to the 30° central light-cut
    upper_d = (
        "M 184 62 "
        "C 172 34 148 22 122 22 "
        "C 82 22 54 48 54 84 "
        "C 54 112 74 130 108 142 "
        "L 124 118 "
        "C 98 108 86 96 86 80 "
        "C 86 58 104 42 128 42 "
        "C 150 42 166 52 174 68 Z"
    )
    # Lower waning crescent-arch (exact 180° rotational mirror around (128, 128)!)
    lower_d = (
        "M 72 194 "
        "C 84 222 108 234 134 234 "
        "C 174 234 202 208 202 172 "
        "C 202 144 182 126 148 114 "
        "L 132 138 "
        "C 158 148 170 160 170 176 "
        "C 170 198 152 214 128 214 "
        "C 106 214 90 204 82 188 Z"
    )
    return [f'<path d="{upper_d}"/>', f'<path d="{lower_d}"/>']


def build_lockup(mark_paths, filename, title):
    margin = 48.0
    sym_size = 148.0
    s_sc = sym_size / 204.0
    tx = (margin + sym_size * 0.5) - 128.0 * s_sc
    ty = 128.0 - 128.0 * s_sc
    wm_x = margin + sym_size + 48.0
    h_cap = 86.0
    h_oy = 88.0
    wm_paths, h_wm_w = s5.build_wordmark(wm_x, h_oy, h_cap, tracking=20.0, couture=True, sw=12.6, hw=3.8)
    vb_w = int(math.ceil(wm_x + h_wm_w + margin))

    mark_xml = "\n    ".join(mark_paths)
    wm_xml = "\n    ".join(f'<path d="{d}"/>' for d in wm_paths)
    body = (
        f'  <g id="symbol" fill="{INK}" transform="translate({fmt(tx)} {fmt(ty)}) scale({fmt(s_sc)})">\n'
        f'    {mark_xml}\n'
        f'  </g>\n'
        f'  <g id="wordmark" fill="{INK}">\n'
        f'    {wm_xml}\n'
        f'  </g>'
    )
    write_svg(OUT / filename, vb_w, 256, title, body)


def build_comparison_board(options):
    """Build a crisp 2x2 studio comparison board (HTML -> PNG) showing each option large,
    in lockup with SELUNÉA, at 64/32/16px, and reversed on Midnight Ash."""
    cards_html = []
    for idx, (num, name, subtitle, idea, sym_file, lock_file) in enumerate(options, 1):
        sym_svg = (OUT / sym_file).read_text(encoding="utf-8")
        lock_svg = (OUT / lock_file).read_text(encoding="utf-8")
        sym_white = sym_svg.replace(f'fill="{INK}"', 'fill="#F3F0E9"')

        cards_html.append(f"""
        <article class="opt-card">
          <div class="opt-top">
            <span class="opt-num">OPTION 0{idx}</span>
            <span class="opt-tag">{subtitle}</span>
          </div>
          <div class="opt-stage">
            <div class="stage-light">
              <div class="big-mark">{sym_svg}</div>
            </div>
            <div class="stage-dark">
              <div class="dark-mark">{sym_white}</div>
              <span class="dark-cap">On Midnight Ash</span>
            </div>
          </div>
          <div class="opt-lockup">
            {lock_svg}
          </div>
          <div class="opt-scales">
            <div class="sc-item"><div class="sc-64">{sym_svg}</div><span>64 px</span></div>
            <div class="sc-item"><div class="sc-32">{sym_svg}</div><span>32 px</span></div>
            <div class="sc-item"><div class="sc-16">{sym_svg}</div><span>16 px</span></div>
          </div>
          <div class="opt-info">
            <h3>{name}</h3>
            <p>{idea}</p>
          </div>
        </article>
        """)

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<title>SELUNÉA — Brand Mark Options Comparison</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet" />
<style>
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{
    background:#F3F0E9; color:#34332F; font-family:'DM Sans',sans-serif;
    width:1520px; padding:48px 54px 54px; -webkit-font-smoothing:antialiased;
  }}
  header {{
    display:flex; justify-content:space-between; align-items:flex-end;
    padding-bottom:22px; border-bottom:1px solid rgba(52,51,47,0.14); margin-bottom:30px;
  }}
  .eyebrow {{ font-size:11px; letter-spacing:0.2em; text-transform:uppercase; color:#5B5953; margin-bottom:6px; }}
  h1 {{ font-family:'Cormorant Garamond',serif; font-size:44px; font-weight:500; line-height:1.05; }}
  h1 em {{ font-style:italic; font-weight:400; }}
  .sub {{ font-size:13px; color:#5B5953; text-align:right; line-height:1.6; }}
  .grid {{ display:grid; grid-template-columns:1fr 1fr; gap:26px; }}
  .opt-card {{
    background:#FAF8F4; border:1px solid rgba(52,51,47,0.13); border-radius:16px;
    padding:24px 26px; display:flex; flex-direction:column; gap:18px;
  }}
  .opt-top {{ display:flex; justify-content:space-between; align-items:center; font-size:10.5px; letter-spacing:0.18em; text-transform:uppercase; color:#5B5953; }}
  .opt-num {{ font-weight:600; color:#34332F; }}
  .opt-stage {{ display:grid; grid-template-columns:1.35fr 0.85fr; gap:14px; }}
  .stage-light {{
    background:#FFFFFF; border:1px solid rgba(52,51,47,0.08); border-radius:12px;
    height:184px; display:flex; align-items:center; justify-content:center;
  }}
  .stage-dark {{
    background:#34332F; border-radius:12px; height:184px;
    display:flex; flex-direction:column; align-items:center; justify-content:center; gap:10px;
  }}
  .big-mark svg {{ width:126px; height:126px; display:block; }}
  .dark-mark svg {{ width:88px; height:88px; display:block; }}
  .dark-cap {{ font-size:9.5px; letter-spacing:0.14em; text-transform:uppercase; color:#C8B9A6; }}
  .opt-lockup {{
    background:#FFFFFF; border:1px solid rgba(52,51,47,0.08); border-radius:10px;
    padding:16px 20px; display:flex; align-items:center; justify-content:center;
  }}
  .opt-lockup svg {{ height:46px; width:auto; display:block; }}
  .opt-scales {{
    display:flex; align-items:flex-end; gap:26px; padding:4px 6px;
  }}
  .sc-item {{ display:flex; flex-direction:column; align-items:center; gap:6px; }}
  .sc-item span {{ font-size:10px; color:#5B5953; }}
  .sc-64 svg {{ width:54px; height:54px; display:block; }}
  .sc-32 svg {{ width:32px; height:32px; display:block; }}
  .sc-16 svg {{ width:16px; height:16px; display:block; }}
  .opt-info {{ padding-top:12px; border-top:1px solid rgba(52,51,47,0.1); }}
  .opt-info h3 {{ font-family:'Cormorant Garamond',serif; font-size:26px; font-weight:600; margin-bottom:4px; }}
  .opt-info p {{ font-size:12.5px; color:#5B5953; line-height:1.55; }}
</style>
</head>
<body>
  <header>
    <div>
      <div class="eyebrow">Brand Mark Exploration · Paired with Approved SELUNÉA Wordmark</div>
      <h1>Four New <em>Brand Mark</em> Options</h1>
    </div>
    <div class="sub">
      <strong>SELUNÉA · Presented for NANA</strong><br/>
      100% Pure Vector Outlines · Tested at 64 / 32 / 16 px &amp; Dark Surface
    </div>
  </header>
  <section class="grid">
    {"".join(cards_html)}
  </section>
</body>
</html>
"""
    (OUT / "selunea-brand-mark-options.html").write_text(html, encoding="utf-8")


def main():
    options = [
        (
            "01", "The Eclipse Halo", "Continuous Cycle · Minimalist",
            "Cincin gerhana tak terputus dengan lubang eksentrik pada poros 30° (senada sudut aksen É). Sangat tenang, arsitektural, dan tajam hingga 16 px.",
            "mark-opt1-eclipse-halo.svg", "lockup-opt1-eclipse-halo.svg",
            build_opt1_paths(),
        ),
        (
            "02", "The Lunar Equinox", "Offset Horizon · Modern Editorial",
            "Dua belahan fase bulan yang bergeser lembut melintasi garis horizon negative space — melambangkan ritme siang–malam kulit dan keseimbangan tanpa klise.",
            "mark-opt2-lunar-equinox.svg", "lockup-opt2-lunar-equinox.svg",
            build_opt2_paths(),
        ),
        (
            "03", "Four-Phase Radiance", "Soft Lunar Bloom · Feminine Luxury",
            "Empat busur fase bulan melingkari inti mutiara di tengah — terasa lembut, feminin, dan ikonik untuk emboss tutup jar maupun stiker segel.",
            "mark-opt3-four-phase-radiance.svg", "lockup-opt3-four-phase-radiance.svg",
            build_opt3_paths(),
        ),
        (
            "04", "The Dual-Phase S", "Interlocking S · Monogram-Mark",
            "Dua busur fase bulan berlawanan yang saling mengunci membentuk huruf S yang luwes — memadukan inisial SELUNÉA dan siklus bulan dalam satu tanda kuat.",
            "mark-opt4-dual-phase-s.svg", "lockup-opt4-dual-phase-s.svg",
            build_opt4_paths(),
        ),
    ]

    for num, name, sub, idea, sym_f, lock_f, paths in options:
        body = f'  <g id="symbol" fill="{INK}">\n    ' + "\n    ".join(paths) + "\n  </g>"
        write_svg(OUT / sym_f, 256, 256, f"SELUNÉA Brand Mark Option {num} — {name}", body)
        build_lockup(paths, lock_f, f"SELUNÉA Lockup Option {num} — {name}")

    build_comparison_board([(n, nm, sb, id_, sf, lf) for n, nm, sb, id_, sf, lf, _ in options])
    print("Generated 4 Brand Mark options + lockups + comparison board in", OUT)


if __name__ == "__main__":
    main()
