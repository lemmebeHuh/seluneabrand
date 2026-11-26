"""
SELUNÉA — Brand Mark Exploration Round 2 (Options 05–08)
Deeply aligned with SELUNÉA's "Lunar Elegance" contemporary skincare identity
and the high-contrast couture curves of the approved SELUNÉA wordmark.

Options:
  05. The Lunar Cradle   — Sculptural horizontal crescent-cradle gently holding a full-phase pearl orb
  06. The Celestial Arch — Minimalist beauty-vessel arch with a carved negative-space rising moon phase
  07. The Waxing Drop    — Pure serum-pearl silhouette with an eccentric circular lunar-phase cutout
  08. The Phase Mirror   — Twin high-contrast calligraphic crescent arcs framing a quiet luminous column
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
# OPTION 05: THE LUNAR CRADLE (Echoes the L→U cradle of SELUNÉA!)
# A calm horizontal waxing-bowl crescent cradling a serene full-phase pearl orb.
# ---------------------------------------------------------------------------

def build_opt5_paths():
    cx = 128.0
    # Lower horizontal lunar cradle: pure 2-arc symmetrical crescent centered at bottom (90° in SVG y-down)
    # Outer arc R_out = 96 centered at (128, 128), span = 156° around bottom (from 12° to 168°)
    # Max thickness at bottom = 36 units (sturdy, lush, crisp at 16 px!)
    cradle_d = s5.build_open_tapered_arc(cx, 128.0, 78.0, 90.0, 156.0, 36.0)
    # Poised full-phase pearl orb resting gently above the cradle
    orb_cy, orb_r = 92.0, 34.0
    orb_d = (
        f"M {fmt(cx)} {fmt(orb_cy - orb_r)} "
        f"A {fmt(orb_r)} {fmt(orb_r)} 0 1 1 {fmt(cx)} {fmt(orb_cy + orb_r)} "
        f"A {fmt(orb_r)} {fmt(orb_r)} 0 1 1 {fmt(cx)} {fmt(orb_cy - orb_r)} Z"
    )
    return [f'<path d="{cradle_d}"/>', f'<path d="{orb_d}"/>']


# ---------------------------------------------------------------------------
# OPTION 06: THE CELESTIAL ARCH (Beauty Vessel Portal + Carved Rising Phase)
# Calm architectural arch (like a frosted skincare vessel / moonlit sanctuary)
# with a real evenodd negative-space crescent-phase portal carved cleanly inside.
# ---------------------------------------------------------------------------

def build_opt6_paths():
    # Outer arch: width 164 (x = 46..210), height 196 (y = 30..226), top semicircle r = 82 at (128, 112)
    outer = (
        "M 46 226 L 46 112 "
        "A 82 82 0 0 1 210 112 "
        "L 210 226 Z"
    )
    # Inner negative-space sanctuary void (evenodd):
    # A serene circular lunar window (r = 46 centered at 128, 118) with a soft rising inner phase dome
    # Wait: even cleaner and more unmistakably lunar — carve an eccentric luminous lunar orb (r = 48 at 128, 114)
    # AND a clean vertical horizon slit (width 18) descending to the base like moonlight reflected on water!
    # Let's check: arch with circular window + clean vertical reflection stem = pure architectural beauty icon!
    # Wait — make it purely LUNAR: inside the solid arch, carve a clean circular lunar-phase window (r = 50 at 128, 112)
    # containing a smaller solid offset waxing phase disc (r = 34 shifted slightly right-down to 140, 120) —
    # giving a gorgeous negative-space crescent glow INSIDE the calm skincare arch!!
    r_win = 52.0
    wx, wy = 128.0, 114.0
    inner_hole = (
        f"M {fmt(wx)} {fmt(wy - r_win)} "
        f"A {fmt(r_win)} {fmt(r_win)} 0 1 0 {fmt(wx)} {fmt(wy + r_win)} "
        f"A {fmt(r_win)} {fmt(r_win)} 0 1 0 {fmt(wx)} {fmt(wy - r_win)} Z"
    )
    # Solid inner waxing orb inside the negative-space window (shifted +12, +8 for graceful crescent light!)
    r_orb = 34.0
    ox, oy = 140.0, 122.0
    inner_orb = (
        f"M {fmt(ox)} {fmt(oy - r_orb)} "
        f"A {fmt(r_orb)} {fmt(r_orb)} 0 1 1 {fmt(ox)} {fmt(oy + r_orb)} "
        f"A {fmt(r_orb)} {fmt(r_orb)} 0 1 1 {fmt(ox)} {fmt(oy - r_orb)} Z"
    )
    return [f'<path fill-rule="evenodd" d="{outer} {inner_hole}"/>', f'<path d="{inner_orb}"/>']


# ---------------------------------------------------------------------------
# OPTION 07: THE WAXING DROP (Sculptural Serum-Pearl + Eccentric Lunar Void)
# Minimalist skincare essence silhouette containing a real evenodd eccentric
# circular lunar-phase void — unites skincare hydration + moon phase cleanly.
# ---------------------------------------------------------------------------

def build_opt7_paths():
    # Outer sculptural droplet/pearl: apex at (128, 24), lush circular belly centered at (128, 152), R = 78
    # Smooth tangent transition from apex to circular belly!
    outer = (
        "M 128 24 "
        "C 156 68 206 108 206 152 "
        "A 78 78 0 1 1 50 152 "
        "C 50 108 100 68 128 24 Z"
    )
    # Eccentric circular lunar-phase void (r = 44 shifted slightly upper-right to (140, 146)
    # so the lower-left swells into a lush lunar crescent belly of ~34 units, min wall ~18 units -> crisp at 16 px!)
    vx, vy, vr = 140.0, 148.0, 44.0
    hole = (
        f"M {fmt(vx)} {fmt(vy - vr)} "
        f"A {fmt(vr)} {fmt(vr)} 0 1 0 {fmt(vx)} {fmt(vy + vr)} "
        f"A {fmt(vr)} {fmt(vr)} 0 1 0 {fmt(vx)} {fmt(vy - vr)} Z"
    )
    return [f'<path fill-rule="evenodd" d="{outer} {hole}"/>']


# ---------------------------------------------------------------------------
# OPTION 08: THE PHASE MIRROR (Twin High-Contrast Calligraphic Vertical Arcs)
# Two opposing high-contrast lunar crescents framing a calm luminous oval mirror
# with a subtle central full-phase pearl point — pure couture editorial poise.
# ---------------------------------------------------------------------------

def build_opt8_paths():
    cx, cy = 128.0, 128.0
    # Left waxing calligraphic arc (centered at 180°, span 136°, max thickness 30)
    # Right waning calligraphic arc (centered at 0°, span 136°, max thickness 30)
    # Leaves generous 44° luminous breathing apertures at top (270°) and bottom (90°)!
    left_arc = s5.build_open_tapered_arc(cx, cy, 84.0, 180.0, 136.0, 30.0)
    right_arc = s5.build_open_tapered_arc(cx, cy, 84.0, 0.0, 136.0, 30.0)
    # Serene central luminous pearl disc (r = 24) floating inside the twin mirror arcs
    r_mid = 24.0
    mid_d = (
        f"M {fmt(cx)} {fmt(cy - r_mid)} "
        f"A {fmt(r_mid)} {fmt(r_mid)} 0 1 1 {fmt(cx)} {fmt(cy + r_mid)} "
        f"A {fmt(r_mid)} {fmt(r_mid)} 0 1 1 {fmt(cx)} {fmt(cy - r_mid)} Z"
    )
    return [f'<path d="{left_arc}"/>', f'<path d="{right_arc}"/>', f'<path d="{mid_d}"/>']


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
    cards_html = []
    for num, name, subtitle, idea, sym_file, lock_file in options:
        sym_svg = (OUT / sym_file).read_text(encoding="utf-8")
        lock_svg = (OUT / lock_file).read_text(encoding="utf-8")
        sym_white = sym_svg.replace(f'fill="{INK}"', 'fill="#F3F0E9"')

        cards_html.append(f"""
        <article class="opt-card">
          <div class="opt-top">
            <span class="opt-num">OPTION {num}</span>
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
<title>SELUNÉA — Brand Mark Options Round 2 (05–08)</title>
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
  .opt-scales {{ display:flex; align-items:flex-end; gap:26px; padding:4px 6px; }}
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
      <div class="eyebrow">Brand Mark Exploration · Round 2 (Skincare-Native Lunar Elegance)</div>
      <h1>Four Refined <em>Brand Mark</em> Options (05–08)</h1>
    </div>
    <div class="sub">
      <strong>SELUNÉA · Presented for NANA</strong><br/>
      100% Pure Vector Outlines · Paired with Approved SELUNÉA Wordmark
    </div>
  </header>
  <section class="grid">
    {"".join(cards_html)}
  </section>
</body>
</html>
"""
    (OUT / "selunea-brand-mark-options-round2.html").write_text(html, encoding="utf-8")


def main():
    options = [
        (
            "05", "The Lunar Cradle", "Gentle Care · Echoes L→U Curve",
            "Lengkungan lunar lembut di bawah yang menopang mutiara purnama — langsung selaras dengan lengkung L→U pada wordmark SELUNÉA, hangat, feminin, dan menenangkan.",
            "mark-opt5-lunar-cradle.svg", "lockup-opt5-lunar-cradle.svg",
            build_opt5_paths(),
        ),
        (
            "06", "The Celestial Arch", "Skincare Vessel · Sanctuary Portal",
            "Siluet lengkung botol skincare arsitektural dengan jendela fase bulan negative space di dalamnya — terasa dewasa, modern maison, dan kokoh di karton maupun favicon.",
            "mark-opt6-celestial-arch.svg", "lockup-opt6-celestial-arch.svg",
            build_opt6_paths(),
        ),
        (
            "07", "The Waxing Drop", "Serum Essence + Moon Phase",
            "Bentuk tetes esens skincare minimalis dengan ruang kosong melingkar eksentrik di dalamnya — menyatukan makna hidrasi kulit dan fase bulan dalam satu bentuk ikonik.",
            "mark-opt7-waxing-drop.svg", "lockup-opt7-waxing-drop.svg",
            build_opt7_paths(),
        ),
        (
            "08", "The Phase Mirror", "High-Contrast Couture · Editorial",
            "Dua busur kaligrafis kontras tebal–tipis (senada stroke SELUNÉA) membingkai inti mutiara di tengah — terasa seperti cermin rias mewah dan cahaya bulan yang tenang.",
            "mark-opt8-phase-mirror.svg", "lockup-opt8-phase-mirror.svg",
            build_opt8_paths(),
        ),
    ]

    for num, name, sub, idea, sym_f, lock_f, paths in options:
        body = f'  <g id="symbol" fill="{INK}">\n    ' + "\n    ".join(paths) + "\n  </g>"
        write_svg(OUT / sym_f, 256, 256, f"SELUNÉA Brand Mark Option {num} — {name}", body)
        build_lockup(paths, lock_f, f"SELUNÉA Lockup Option {num} — {name}")

    build_comparison_board([(n, nm, sb, id_, sf, lf) for n, nm, sb, id_, sf, lf, _ in options])
    print("Generated Round 2 Brand Mark options (05–08) in", OUT)


if __name__ == "__main__":
    main()
