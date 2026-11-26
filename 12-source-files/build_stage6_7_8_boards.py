"""
SELUNÉA — Stages 6, 7 & 8 Visual Identity Boards, Packaging System,
Brand Applications & 15-Section Brand Guidelines Generator.
Embeds ONLY real Stage 5 vector SVG masters (zero rasterized logos, zero invented claims).
"""

from pathlib import Path
import re

BASE = Path(r"c:\Users\ridwa\Desktop\selunea\selunea-brand-identity")
SVG_DIR = BASE / "05-logo-final" / "svg"
GFX_DIR = BASE / "07-graphic-assets"


def load_svg(path: Path, css_class: str = "", style: str = "") -> str:
    txt = path.read_text(encoding="utf-8").strip()
    # Remove id="title" collisions when embedding multiple SVGs inline
    txt = re.sub(r'\s+aria-labelledby="[^"]*"', "", txt)
    txt = re.sub(r'<title[^>]*>.*?</title>\s*', "", txt, flags=re.S)
    attrs = ""
    if css_class:
        attrs += f' class="{css_class}"'
    if style:
        attrs += f' style="{style}"'
    if attrs:
        txt = txt.replace("<svg ", f"<svg{attrs} ", 1)
    return txt


FONTS_HEAD = """<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet" />"""

TOKENS_CSS = (BASE / "06-color-typography" / "02-design-tokens.css").read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# STAGE 6 BOARD: COLOR SYSTEM, TYPOGRAPHY SYSTEM & GRAPHIC LANGUAGE
# ---------------------------------------------------------------------------

def build_stage6_board():
    wm_ash = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:44px;width:auto;")
    mark_ash = load_svg(SVG_DIR / "selunea-brand-mark-midnight-ash.svg", style="height:46px;width:46px;")
    divider_svg = load_svg(GFX_DIR / "lunar-phase-divider.svg", style="width:100%;height:auto;")
    orbital_svg = load_svg(GFX_DIR / "orbital-frame-accent.svg", style="width:140px;height:140px;")
    pattern_svg = load_svg(GFX_DIR / "phase-pattern-tile.svg", style="width:140px;height:140px;border-radius:8px;")
    pearl_svg = load_svg(GFX_DIR / "pearl-luminosity-backdrop.svg", style="width:100%;height:140px;object-fit:cover;border-radius:8px;")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>SELUNÉA — Stage 6 Color, Typography &amp; Graphic System</title>
{FONTS_HEAD}
<style>
{TOKENS_CSS}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{
  background: var(--selunea-ivory);
  color: var(--selunea-ash);
  font-family: var(--font-sans);
  width: 1600px;
  padding: 52px 60px 60px;
  -webkit-font-smoothing: antialiased;
}}
.header {{
  display:flex; justify-content:space-between; align-items:flex-end;
  padding-bottom:24px; border-bottom:1px solid var(--selunea-line); margin-bottom:32px;
}}
.eyebrow {{ font-size:11px; letter-spacing:0.22em; text-transform:uppercase; color:var(--selunea-ash-soft); margin-bottom:8px; }}
.h1 {{ font-family:var(--font-display); font-size:46px; font-weight:500; line-height:1.05; }}
.h1 em {{ font-style:italic; font-weight:400; }}
.grid2 {{ display:grid; grid-template-columns:1.15fr 1fr; gap:28px; margin-bottom:28px; }}
.card {{ background:var(--selunea-ivory-tint); border:1px solid var(--selunea-line); border-radius:14px; padding:28px 30px; }}
.label {{ font-size:10.5px; letter-spacing:0.18em; text-transform:uppercase; color:var(--selunea-ash-soft); margin-bottom:18px; display:flex; justify-content:space-between; }}
.swatches {{ display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-bottom:18px; }}
.sw {{ border-radius:10px; overflow:hidden; border:1px solid var(--selunea-line); background:#fff; }}
.sw-top {{ height:92px; padding:12px; display:flex; align-items:flex-end; font-size:10px; font-weight:500; letter-spacing:0.08em; }}
.sw-bot {{ padding:11px 12px; font-size:11px; line-height:1.45; }}
.sw-bot strong {{ display:block; font-size:12px; margin-bottom:2px; }}
.mono {{ font-family:ui-monospace,Menlo,monospace; font-size:10px; color:var(--selunea-ash-soft); display:block; }}
.sku-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; }}
.sku-card {{ border-radius:10px; padding:14px 16px; border:1px solid rgba(52,51,47,0.09); }}
.sku-card strong {{ font-size:12.5px; display:block; margin-bottom:3px; }}
.sku-card span {{ font-size:10.5px; color:var(--selunea-ash-soft); display:block; line-height:1.4; }}
.type-row {{ padding:16px 0; border-bottom:1px solid var(--selunea-line); display:grid; grid-template-columns:180px 1fr; gap:18px; align-items:center; }}
.type-row:last-child {{ border-bottom:none; padding-bottom:0; }}
.type-meta {{ font-size:10.5px; color:var(--selunea-ash-soft); line-height:1.5; }}
.type-meta strong {{ display:block; color:var(--selunea-ash); text-transform:uppercase; letter-spacing:0.12em; font-size:10px; margin-bottom:2px; }}
.gfx-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:18px; }}
.gfx-tile {{ background:var(--selunea-ivory); border:1px solid var(--selunea-line); border-radius:10px; padding:18px; display:flex; flex-direction:column; align-items:center; justify-content:space-between; text-align:center; gap:12px; }}
.gfx-tile h4 {{ font-size:11.5px; letter-spacing:0.06em; font-weight:500; }}
.gfx-tile p {{ font-size:10.5px; color:var(--selunea-ash-soft); line-height:1.4; }}
</style>
</head>
<body>
  <header class="header">
    <div>
      <div class="eyebrow">Stage 06 · Complete Visual Identity Architecture</div>
      <h1 class="h1">Color, Typography &amp; <em>Graphic Language</em></h1>
    </div>
    <div style="display:flex;align-items:center;gap:16px;">{mark_ash}{wm_ash}</div>
  </header>

  <section class="grid2">
    <div class="card">
      <div class="label"><span>01 · Brand Color Hierarchy</span><span>60% Ivory · 25% Ash · 10% Champagne · 5% Silver</span></div>
      <div class="swatches">
        <div class="sw">
          <div class="sw-top" style="background:#F3F0E9;color:#34332F;">PRIMARY CANVAS</div>
          <div class="sw-bot"><strong>Moon Ivory</strong><span class="mono">#F3F0E9 · RGB 243 240 233</span><span class="mono">CMYK 0 1 4 5 · AAA vs Ash</span></div>
        </div>
        <div class="sw">
          <div class="sw-top" style="background:#34332F;color:#F3F0E9;">PRIMARY INK</div>
          <div class="sw-bot"><strong>Midnight Ash</strong><span class="mono">#34332F · RGB 52 51 47</span><span class="mono">CMYK 0 2 10 80 · Black 7 C</span></div>
        </div>
        <div class="sw">
          <div class="sw-top" style="background:#C8B9A6;color:#34332F;">WARM ACCENT</div>
          <div class="sw-bot"><strong>Champagne Beige</strong><span class="mono">#C8B9A6 · RGB 200 185 166</span><span class="mono">CMYK 0 8 17 22 · Foil 872 C</span></div>
        </div>
        <div class="sw">
          <div class="sw-top" style="background:#B8B7B1;color:#34332F;">COOL METALLIC</div>
          <div class="sw-bot"><strong>Lunar Silver</strong><span class="mono">#B8B7B1 · RGB 184 183 177</span><span class="mono">CMYK 0 1 4 28 · Foil 877 C</span></div>
        </div>
      </div>
      <div class="label" style="margin-bottom:12px;"><span>Product Category Accent System (Supporting Palette · AAA vs Midnight Ash)</span></div>
      <div class="sku-grid">
        <div class="sku-card" style="background:#D9DFD5;">
          <strong>Sage Haze · #D9DFD5</strong>
          <span>Purify &amp; Balance → <b>Facial Cleanser</b><br/>CMYK 3 0 4 13 · 9.31:1 vs Ash</span>
        </div>
        <div class="sku-card" style="background:#DCD9E2;">
          <strong>Lavender Mist · #DCD9E2</strong>
          <span>Prepare &amp; Treat → <b>Toner &amp; Serum</b><br/>CMYK 3 4 0 11 · 9.07:1 vs Ash</span>
        </div>
        <div class="sku-card" style="background:#E4DAD0;">
          <strong>Soft Nude · #E4DAD0</strong>
          <span>Nourish &amp; Shield → <b>Moisturizer &amp; Sunscreen</b><br/>CMYK 0 4 9 11 · 9.18:1 vs Ash</span>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="label"><span>02 · Typography System (SIL OFL · Max 2 Families)</span><span>Editorial Poise + Clarity</span></div>
      <div class="type-row">
        <div class="type-meta"><strong>Logo Wordmark</strong>Custom Couture Sans<br/>Outlined Vector Only</div>
        <div>{load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:40px;width:auto;")}</div>
      </div>
      <div class="type-row">
        <div class="type-meta"><strong>Display / Campaign</strong>Cormorant Garamond<br/>400 / 500 / Italic</div>
        <div style="font-family:var(--font-display);font-size:34px;line-height:1.1;">Beauty in <em>Every Phase.</em></div>
      </div>
      <div class="type-row">
        <div class="type-meta"><strong>Headings / Sub-copy</strong>DM Sans Medium<br/>16–22 px · +0.02em</div>
        <div style="font-size:19px;font-weight:500;">Skincare for every version of you.</div>
      </div>
      <div class="type-row">
        <div class="type-meta"><strong>Body Copy</strong>DM Sans Regular<br/>14–16 px · 1.65 lh</div>
        <div style="font-size:13.5px;color:var(--selunea-ash-soft);line-height:1.6;">Inspired by the phases of the moon, Selunéa honors the evolving rhythm of your skin with calm, consistent daily care.</div>
      </div>
      <div class="type-row">
        <div class="type-meta"><strong>Product Information</strong>DM Sans Medium Caps<br/>10–11 px · +0.18em</div>
        <div style="font-size:11px;font-weight:500;letter-spacing:0.18em;text-transform:uppercase;">FACIAL CLEANSER &nbsp;·&nbsp; PHASE 01 &nbsp;·&nbsp; 120 ML / 4.0 FL. OZ.</div>
      </div>
    </div>
  </section>

  <section class="card">
    <div class="label"><span>03 · Supporting Graphic Language (Vector Assets in 07-graphic-assets/)</span><span>Derived Strictly from Lunar Geometry</span></div>
    <div class="gfx-grid">
      <div class="gfx-tile">
        <div style="width:100%;padding:48px 0;">{divider_svg}</div>
        <div><h4>Five-Phase Horizon Divider</h4><p>Editorial section separator for cartons, inserts &amp; web chapters.</p></div>
      </div>
      <div class="gfx-tile">
        <div>{orbital_svg}</div>
        <div><h4>Concentric Orbital Frame</h4><p>Subtle framing halo behind campaign product photography.</p></div>
      </div>
      <div class="gfx-tile">
        <div>{pattern_svg}</div>
        <div><h4>Seamless Phase Liner Pattern</h4><p>Tissue paper, box interior print &amp; blind-embossed collateral.</p></div>
      </div>
      <div class="gfx-tile">
        <div style="width:100%;">{pearl_svg}</div>
        <div><h4>Pearl Luminosity Surface</h4><p>Soft directional moonlight glow for digital cards &amp; lookbooks.</p></div>
      </div>
    </div>
  </section>
</body>
</html>
"""
    (BASE / "06-color-typography" / "03-color-typography-board.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
# STAGE 7A BOARD: COMPLETE 5-SKU PACKAGING FAMILY + FOLDING CARTONS
# Zero invented ingredient claims, SPF numbers, certifications, or efficacy claims!
# ---------------------------------------------------------------------------

def build_packaging_board():
    wm_ash = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="width:74%;height:auto;")
    wm_sm = load_svg(SVG_DIR / "selunea-wordmark-small-responsive.svg", style="width:68%;height:auto;")
    wm_hdr = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:36px;width:auto;")
    mark_ash = load_svg(SVG_DIR / "selunea-brand-mark-midnight-ash.svg", style="width:28px;height:28px;")
    mark_lg = load_svg(SVG_DIR / "selunea-brand-mark-midnight-ash.svg", style="width:36px;height:36px;")
    mono_ash = load_svg(SVG_DIR / "selunea-monogram-s-midnight-ash.svg", style="width:30px;height:30px;opacity:0.42;")
    mono_champ = load_svg(SVG_DIR / "selunea-monogram-s-champagne.svg", style="width:32px;height:32px;")
    stacked_ash = load_svg(SVG_DIR / "selunea-stacked-lockup-midnight-ash.svg", style="width:82%;height:auto;")
    pattern_bg = load_svg(GFX_DIR / "phase-pattern-tile.svg", style="width:100%;height:100%;object-fit:cover;opacity:0.75;")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>SELUNÉA — Stage 7 Skincare Packaging Family (5 SKUs + Cartons)</title>
{FONTS_HEAD}
<style>
{TOKENS_CSS}
* {{ box-sizing:border-box; margin:0; padding:0; }}
@page {{ size: 1600px 1260px; margin: 0; }}
@media print {{ body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }} }}
body {{
  background: var(--selunea-ivory);
  color: var(--selunea-ash);
  font-family: var(--font-sans);
  width: 1600px;
  padding: 50px 58px 58px;
  -webkit-font-smoothing: antialiased;
}}
.header {{
  display:flex; justify-content:space-between; align-items:flex-end;
  padding-bottom:22px; border-bottom:1px solid var(--selunea-line); margin-bottom:28px;
}}
.eyebrow {{ font-size:11px; letter-spacing:0.22em; text-transform:uppercase; color:var(--selunea-ash-soft); margin-bottom:8px; }}
.h1 {{ font-family:var(--font-display); font-size:44px; font-weight:500; line-height:1.05; }}
.h1 em {{ font-style:italic; font-weight:400; }}

/* Product Family Stage */
.stage {{
  background: linear-gradient(180deg, #FAF8F4 0%, #EFECE4 74%, #E6E0D5 74.2%, #DDD5C7 100%);
  border: 1px solid var(--selunea-line);
  border-radius: 18px;
  padding: 46px 40px 42px;
  margin-bottom: 26px;
}}
.stage-title {{
  font-size:10.5px; letter-spacing:0.2em; text-transform:uppercase; color:var(--selunea-ash-soft);
  display:flex; justify-content:space-between; margin-bottom:36px;
}}
.family-row {{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 24px;
  align-items: end;
}}
.sku-col {{
  display: flex; flex-direction: column; align-items: center;
}}
.vessel-wrap {{
  height: 390px;
  display: flex; flex-direction: column; align-items: center; justify-content: flex-end;
  position: relative;
}}
.shadow-floor {{
  width: 120px; height: 14px; border-radius: 50%;
  background: radial-gradient(ellipse, rgba(52,51,47,0.22) 0%, rgba(52,51,47,0) 72%);
  margin-top: -6px;
}}

/* Common Front-of-Pack Label System */
.fop {{
  display:flex; flex-direction:column; align-items:center; justify-content:space-between;
  text-align:center; width:100%; height:100%; padding:22px 14px 18px;
}}
.fop-top {{ display:flex; flex-direction:column; align-items:center; gap:6px; width:100%; }}
.fop-mid {{ display:flex; flex-direction:column; align-items:center; gap:5px; }}
.fop-cat {{ font-size:8.5px; letter-spacing:0.22em; text-transform:uppercase; color:var(--selunea-ash-soft); }}
.fop-name {{ font-family:var(--font-display); font-size:21px; font-weight:500; line-height:1.05; color:var(--selunea-ash); }}
.fop-band {{ height:6px; width:36px; border-radius:99px; margin:3px 0; }}
.fop-net {{ font-size:8.5px; letter-spacing:0.16em; text-transform:uppercase; color:var(--selunea-ash-soft); }}

/* 1. Facial Cleanser — Matte Ivory Squeeze Tube */
.tube-body {{
  width: 128px; height: 288px;
  background: linear-gradient(90deg, #E8E3D8 0%, #F7F5EF 28%, #F3F0E9 65%, #DED8CC 100%);
  border-radius: 8px 8px 26px 26px;
  border: 1px solid rgba(52,51,47,0.12);
  box-shadow: inset 8px 0 14px rgba(255,255,255,0.6), 0 12px 24px rgba(52,51,47,0.09);
  position: relative; overflow: hidden;
}}
.tube-crimp {{
  height: 16px; width: 100%;
  background: repeating-linear-gradient(90deg, rgba(52,51,47,0.05) 0 4px, transparent 4px 8px), #ECE7DC;
  border-bottom: 1px solid rgba(52,51,47,0.1);
}}
.tube-cap {{
  width: 72px; height: 42px;
  background: linear-gradient(90deg, #DDD7CB 0%, #F3F0E9 35%, #CFC8BB 100%);
  border: 1px solid rgba(52,51,47,0.14);
  border-top: none;
  border-radius: 0 0 8px 8px;
}}
.accent-strip {{ height: 22px; width: 100%; }}

/* 2. Toner — Frosted Tall Bottle + Lunar Silver Cap */
.toner-cap {{
  width: 58px; height: 46px;
  background: linear-gradient(90deg, #9C9B95 0%, #D5D4CE 32%, #B8B7B1 68%, #8F8E88 100%);
  border-radius: 6px 6px 2px 2px;
  border: 1px solid rgba(52,51,47,0.16);
}}
.toner-neck {{
  width: 44px; height: 12px; background: linear-gradient(90deg, #B8B7B1, #E5E4DF, #A7A6A0);
}}
.toner-body {{
  width: 118px; height: 292px;
  background: linear-gradient(90deg, rgba(226,225,222,0.88) 0%, rgba(252,251,249,0.94) 30%, rgba(240,238,242,0.92) 68%, rgba(210,208,212,0.88) 100%);
  border-radius: 26px 26px 12px 12px;
  border: 1px solid rgba(255,255,255,0.9);
  box-shadow: inset 10px 0 18px rgba(255,255,255,0.8), inset -8px 0 14px rgba(52,51,47,0.06), 0 14px 26px rgba(52,51,47,0.10);
  position: relative; overflow: hidden;
}}

/* 3. Serum — Frosted Dropper Bottle + Champagne Collar */
.dropper-bulb {{
  width: 34px; height: 48px;
  background: linear-gradient(90deg, #E2DDD2, #FAF8F4 38%, #D4CEC2);
  border-radius: 18px 18px 4px 4px;
  border: 1px solid rgba(52,51,47,0.12);
}}
.dropper-collar {{
  width: 52px; height: 24px;
  background: linear-gradient(90deg, #AF9E89 0%, #DFD3C3 34%, #C8B9A6 68%, #A18F7A 100%);
  border: 1px solid rgba(52,51,47,0.14);
  border-radius: 3px;
}}
.serum-body {{
  width: 110px; height: 204px;
  background: linear-gradient(90deg, rgba(226,223,229,0.9) 0%, rgba(255,254,252,0.96) 28%, rgba(241,238,244,0.92) 68%, rgba(212,208,218,0.88) 100%);
  border-radius: 24px 24px 10px 10px;
  border: 1px solid rgba(255,255,255,0.9);
  box-shadow: inset 10px 0 16px rgba(255,255,255,0.85), 0 12px 24px rgba(52,51,47,0.10);
  position: relative; overflow: hidden;
}}

/* 4. Moisturizer — Heavy Frosted Jar + Satin Lid */
.jar-lid {{
  width: 158px; height: 34px;
  background: linear-gradient(90deg, #B9A995 0%, #DED2C3 30%, #C8B9A6 66%, #A99883 100%);
  border-radius: 10px 10px 3px 3px;
  border: 1px solid rgba(52,51,47,0.14);
  display:flex; align-items:center; justify-content:center;
}}
.jar-body {{
  width: 162px; height: 136px;
  background: linear-gradient(90deg, #E2DAD0 0%, #FAF7F3 30%, #F1EAE2 68%, #D7CCC0 100%);
  border-radius: 4px 4px 22px 22px;
  border: 1px solid rgba(255,255,255,0.85);
  box-shadow: inset 12px 0 18px rgba(255,255,255,0.75), 0 14px 24px rgba(52,51,47,0.11);
  overflow: hidden;
}}

/* 5. Sunscreen — Sleek Flat-Oval Matte Tube */
.spf-body {{
  width: 120px; height: 224px;
  background: linear-gradient(90deg, #E8DFD5 0%, #F7F4EE 30%, #F3F0E9 68%, #DFD5C9 100%);
  border-radius: 16px 16px 28px 28px;
  border: 1px solid rgba(52,51,47,0.12);
  box-shadow: inset 8px 0 14px rgba(255,255,255,0.65), 0 12px 22px rgba(52,51,47,0.09);
  overflow: hidden;
}}
.spf-cap {{
  width: 68px; height: 38px;
  background: linear-gradient(90deg, #B9A995, #DED2C3 35%, #C8B9A6 70%, #A99883);
  border-radius: 0 0 10px 10px;
  border: 1px solid rgba(52,51,47,0.14);
  border-top: none;
}}

.sku-meta {{
  margin-top: 18px; text-align: center;
}}
.sku-meta strong {{ display:block; font-size:12.5px; font-weight:500; }}
.sku-meta span {{ font-size:10.5px; color:var(--selunea-ash-soft); }}

/* Bottom Row: Folding Cartons & Cap Seal Detail */
.bottom-grid {{ display:grid; grid-template-columns: 1.25fr 0.9fr 0.85fr; gap:24px; }}
.card {{ background:var(--selunea-ivory-tint); border:1px solid var(--selunea-line); border-radius:14px; padding:24px 28px; }}
.card-label {{ font-size:10px; letter-spacing:0.16em; text-transform:uppercase; color:var(--selunea-ash-soft); margin-bottom:18px; display:flex; justify-content:space-between; gap:14px; }}

.carton-pair {{ display:flex; gap:24px; justify-content:center; align-items:flex-end; padding:10px 0 4px; }}
.carton-front {{
  width: 176px; height: 274px;
  background: linear-gradient(145deg, #F8F6F0, #EFEBE2);
  border: 1px solid rgba(52,51,47,0.14);
  border-radius: 4px;
  box-shadow: 10px 12px 24px rgba(52,51,47,0.09);
  display:flex; flex-direction:column; justify-content:space-between; align-items:center;
  padding: 24px 16px 20px; text-align:center;
  position: relative;
}}
.carton-accent-top {{ position:absolute; top:0; left:0; right:0; height:10px; background:#DCD9E2; }}
.carton-side {{
  width: 96px; height: 274px;
  background: #EAE5DA;
  border: 1px solid rgba(52,51,47,0.14);
  border-radius: 4px;
  overflow: hidden; position:relative;
  box-shadow: 6px 10px 20px rgba(52,51,47,0.07);
}}
.carton-side-inner {{ position:absolute; inset:0; display:flex; align-items:center; justify-content:center; }}

.cap-demo {{ display:flex; gap:22px; justify-content:center; align-items:center; padding:24px 0 12px; }}
.cap-circle {{
  width: 122px; height: 122px; border-radius: 50%;
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  box-shadow: 0 10px 22px rgba(52,51,47,0.12);
}}
.cap-ivory {{
  background: radial-gradient(circle at 35% 30%, #FAF8F4, #ECE7DC 65%, #DED7C9);
  border: 1px solid rgba(52,51,47,0.12);
}}
.cap-ash {{
  background: radial-gradient(circle at 35% 30%, #44423D, #34332F 68%, #252421);
  border: 1px solid rgba(200,185,166,0.28);
}}
.spec-list {{ list-style:none; font-size:12px; line-height:1.85; color:var(--selunea-ash-soft); }}
.spec-list b {{ color:var(--selunea-ash); font-weight:500; }}
</style>
</head>
<body>
  <header class="header">
    <div>
      <div class="eyebrow">Stage 07 · Packaging Identity System (5-SKU Family)</div>
      <h1 class="h1">Coherent Skincare <em>Packaging Architecture</em></h1>
    </div>
    <div>{wm_hdr}</div>
  </header>

  <section class="stage">
    <div class="stage-title">
      <span>Complete Core Ritual Family · Consistent Front-of-Pack Hierarchy</span>
      <span>Matte Moon Ivory · Frosted Glass · Satin Champagne &amp; Lunar Silver · Zero Unverified Claims</span>
    </div>
    <div class="family-row">
      <!-- 01 FACIAL CLEANSER -->
      <div class="sku-col">
        <div class="vessel-wrap">
          <div class="tube-body">
            <div class="tube-crimp"></div>
            <div class="fop" style="height:248px;">
              <div class="fop-top">{mark_ash}{wm_ash}</div>
              <div class="fop-mid">
                <div class="fop-cat">Phase 01 · Cleanse</div>
                <div class="fop-name">Facial<br/>Cleanser</div>
                <div class="fop-band" style="background:#D9DFD5;"></div>
              </div>
              <div class="fop-net">120 mL / 4.0 FL. OZ.</div>
            </div>
            <div class="accent-strip" style="background:#D9DFD5;"></div>
          </div>
          <div class="tube-cap"></div>
          <div class="shadow-floor"></div>
        </div>
        <div class="sku-meta"><strong>01 · Facial Cleanser</strong><span>Matte Ivory Tube · Sage Haze Accent</span></div>
      </div>

      <!-- 02 TONER -->
      <div class="sku-col">
        <div class="vessel-wrap">
          <div class="toner-cap"></div>
          <div class="toner-neck"></div>
          <div class="toner-body">
            <div class="fop">
              <div class="fop-top">{mark_ash}{wm_ash}</div>
              <div class="fop-mid">
                <div class="fop-cat">Phase 02 · Prepare</div>
                <div class="fop-name">Balancing<br/>Toner</div>
                <div class="fop-band" style="background:#DCD9E2;"></div>
              </div>
              <div class="fop-net">150 mL / 5.0 FL. OZ.</div>
            </div>
          </div>
          <div class="shadow-floor"></div>
        </div>
        <div class="sku-meta"><strong>02 · Toner</strong><span>Frosted Glass · Silver Cap · Lavender Mist</span></div>
      </div>

      <!-- 03 SERUM -->
      <div class="sku-col">
        <div class="vessel-wrap">
          <div class="dropper-bulb"></div>
          <div class="dropper-collar"></div>
          <div class="serum-body">
            <div class="fop" style="padding:18px 10px 14px;">
              <div class="fop-top">{wm_sm}</div>
              <div class="fop-mid">
                <div class="fop-cat">Phase 03 · Treat</div>
                <div class="fop-name" style="font-size:19px;">Daily<br/>Serum</div>
                <div class="fop-band" style="background:#DCD9E2;"></div>
              </div>
              <div class="fop-net">30 mL / 1.0 FL. OZ.</div>
            </div>
          </div>
          <div class="shadow-floor"></div>
        </div>
        <div class="sku-meta"><strong>03 · Serum</strong><span>Frosted Dropper · Champagne Collar</span></div>
      </div>

      <!-- 04 MOISTURIZER -->
      <div class="sku-col">
        <div class="vessel-wrap">
          <div class="jar-lid"></div>
          <div class="jar-body">
            <div class="fop" style="padding:14px 12px 12px;">
              <div class="fop-top">{wm_sm}</div>
              <div class="fop-mid">
                <div class="fop-cat">Phase 04 · Nourish</div>
                <div class="fop-name" style="font-size:18px;">Moisturizer</div>
                <div class="fop-band" style="background:#E4DAD0;"></div>
              </div>
              <div class="fop-net">50 mL / 1.7 FL. OZ.</div>
            </div>
          </div>
          <div class="shadow-floor" style="width:154px;"></div>
        </div>
        <div class="sku-meta"><strong>04 · Moisturizer</strong><span>Frosted Glass Jar · Soft Nude Accent</span></div>
      </div>

      <!-- 05 SUNSCREEN -->
      <div class="sku-col">
        <div class="vessel-wrap">
          <div class="spf-body">
            <div class="fop" style="height:202px;padding:18px 12px 14px;">
              <div class="fop-top">{mark_ash}{wm_sm}</div>
              <div class="fop-mid">
                <div class="fop-cat">Phase 05 · Shield</div>
                <div class="fop-name" style="font-size:19px;">Daily<br/>Sunscreen</div>
                <div class="fop-band" style="background:#E4DAD0;"></div>
              </div>
              <div class="fop-net">50 mL / 1.7 FL. OZ.</div>
            </div>
            <div class="accent-strip" style="background:#E4DAD0;"></div>
          </div>
          <div class="spf-cap"></div>
          <div class="shadow-floor"></div>
        </div>
        <div class="sku-meta"><strong>05 · Sunscreen</strong><span>Matte Oval Tube · Soft Nude Accent</span></div>
      </div>
    </div>
  </section>

  <section class="bottom-grid">
    <div class="card">
      <div class="card-label"><span>Folding Carton Architecture</span><span>Front + Patterned Side Face</span></div>
      <div class="carton-pair">
        <div class="carton-front">
          <div class="carton-accent-top"></div>
          <div style="margin-top:8px;">{stacked_ash}</div>
          <div>
            <div class="fop-cat" style="margin-bottom:4px;">Phase 03 · Treat</div>
            <div class="fop-name" style="font-size:23px;">Daily Serum</div>
            <div style="font-size:10px;color:var(--selunea-ash-soft);margin-top:4px;font-style:italic;font-family:var(--font-display);font-size:14px;">Beauty in Every Phase.</div>
          </div>
          <div class="fop-net">30 mL / 1.0 FL. OZ.</div>
        </div>
        <div class="carton-side">
          <div class="carton-side-inner">{pattern_bg}</div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-label"><span>Top-of-Cap &amp; Jar Lid Seals</span><span>Blind Deboss &amp; Satin Foil</span></div>
      <div class="cap-demo">
        <div style="text-align:center;">
          <div class="cap-circle cap-ivory">{load_svg(SVG_DIR / "selunea-monogram-s-midnight-ash.svg", style="width:62px;height:62px;opacity:0.35;")}</div>
          <div style="font-size:10.5px;color:var(--selunea-ash-soft);margin-top:10px;">Blind Deboss · Matte Ivory Lid</div>
        </div>
        <div style="text-align:center;">
          <div class="cap-circle cap-ash">{load_svg(SVG_DIR / "selunea-monogram-s-champagne.svg", style="width:62px;height:62px;")}</div>
          <div style="font-size:10.5px;color:var(--selunea-ash-soft);margin-top:10px;">Champagne Foil · Ash Seal</div>
        </div>
      </div>
      <p style="font-size:11.5px;color:var(--selunea-ash-soft);line-height:1.55;text-align:center;margin-top:8px;">
        180° symmetric Celestial S Monogram keeps round dropper caps and moisturizer lids optically balanced from every angle.
      </p>
    </div>

    <div class="card">
      <div class="card-label"><span>Production Rules</span><span>Compliance</span></div>
      <ul class="spec-list">
        <li><b>Surface Finish:</b> Soft-touch matte Moon Ivory cartons (350 gsm FSC uncoated) &amp; acid-etched frosted glass.</li>
        <li><b>Logo Print:</b> Single-color Midnight Ash silkscreen (bottles/tubes); satin Champagne micro-foil on outer cartons.</li>
        <li><b>Hierarchy Lock:</b> Brand Mark / Wordmark top-third → Phase &amp; Product Name center → Net Content placeholder bottom.</li>
        <li><b>Small Vessel Rule:</b> Serum (30 mL) &amp; Jar (50 mL) use the reinforced Small-Size Responsive Wordmark for sharp ink fidelity.</li>
        <li><b>Claims Policy:</b> Zero invented ingredient percentages, SPF numbers, certifications, or efficacy claims.</li>
      </ul>
    </div>
  </section>
</body>
</html>
"""
    (BASE / "08-packaging" / "01-skincare-packaging-family.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
# STAGE 7B BOARD: STATIONERY & BRAND COLLATERAL
# ---------------------------------------------------------------------------

def build_stationery_collateral_board():
    wm_ash = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:28px;width:auto;")
    wm_champ = load_svg(SVG_DIR / "selunea-primary-wordmark-champagne.svg", style="height:26px;width:auto;")
    wm_white = load_svg(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", style="height:30px;width:auto;")
    hdr_wm = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:36px;width:auto;")
    stacked_ash = load_svg(SVG_DIR / "selunea-stacked-lockup-midnight-ash.svg", style="width:146px;height:auto;")
    mark_ash = load_svg(SVG_DIR / "selunea-brand-mark-midnight-ash.svg", style="width:32px;height:32px;")
    mark_champ = load_svg(SVG_DIR / "selunea-brand-mark-champagne.svg", style="width:42px;height:42px;")
    mono_ash = load_svg(SVG_DIR / "selunea-monogram-s-midnight-ash.svg", style="width:44px;height:44px;")
    mono_ivory = load_svg(SVG_DIR / "selunea-monogram-s-white-reversed.svg", style="width:44px;height:44px;")
    divider = load_svg(GFX_DIR / "lunar-phase-divider.svg", style="width:220px;height:auto;")
    pattern = load_svg(GFX_DIR / "phase-pattern-tile.svg", style="width:100%;height:100%;object-fit:cover;")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>SELUNÉA — Stage 7 Stationery &amp; Brand Collateral</title>
{FONTS_HEAD}
<style>
{TOKENS_CSS}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{
  background: var(--selunea-ivory); color: var(--selunea-ash);
  font-family: var(--font-sans); width: 1600px; padding: 50px 58px 58px;
  -webkit-font-smoothing: antialiased;
}}
.header {{ display:flex; justify-content:space-between; align-items:flex-end; padding-bottom:22px; border-bottom:1px solid var(--selunea-line); margin-bottom:28px; }}
.eyebrow {{ font-size:11px; letter-spacing:0.22em; text-transform:uppercase; color:var(--selunea-ash-soft); margin-bottom:8px; }}
.h1 {{ font-family:var(--font-display); font-size:44px; font-weight:500; line-height:1.05; }}
.h1 em {{ font-style:italic; font-weight:400; }}
.grid-top {{ display:grid; grid-template-columns:1.1fr 1fr 1fr; gap:24px; margin-bottom:24px; }}
.grid-bot {{ display:grid; grid-template-columns:1fr 1fr 1.15fr; gap:24px; }}
.card {{ background:var(--selunea-ivory-tint); border:1px solid var(--selunea-line); border-radius:14px; padding:24px 26px; }}
.label {{ font-size:10px; letter-spacing:0.18em; text-transform:uppercase; color:var(--selunea-ash-soft); margin-bottom:18px; display:flex; justify-content:space-between; }}

/* Business Cards */
.bcard-stack {{ display:flex; flex-direction:column; gap:16px; align-items:center; }}
.bcard {{
  width: 340px; height: 194px; border-radius: 6px; padding: 24px 26px;
  box-shadow: 0 12px 24px rgba(52,51,47,0.10);
  display:flex; flex-direction:column; justify-content:space-between;
}}
.bcard-front {{ background: var(--selunea-ivory); border:1px solid var(--selunea-line); }}
.bcard-back {{ background: var(--selunea-ash); color: var(--selunea-ivory); align-items:center; justify-content:center; gap:12px; }}

/* Thank You & Insert */
.ty-card {{
  background: var(--selunea-ivory); border:1px solid var(--selunea-line); border-radius:8px;
  padding:30px 26px; text-align:center; box-shadow:0 12px 24px rgba(52,51,47,0.08);
  height: 360px; display:flex; flex-direction:column; justify-content:space-between; align-items:center;
}}
.insert-card {{
  background: #FFFFFF; border:1px solid var(--selunea-line); border-radius:8px;
  padding:26px; height:360px; display:flex; flex-direction:column; justify-content:space-between;
  box-shadow:0 12px 24px rgba(52,51,47,0.06);
}}
.step-row {{ display:flex; gap:12px; align-items:baseline; padding:8px 0; border-bottom:1px solid var(--selunea-line); font-size:11.5px; }}
.step-row:last-child {{ border-bottom:none; }}
.step-num {{ font-family:var(--font-display); font-size:18px; color:var(--selunea-champagne); width:24px; }}

/* Shopping Bag */
.bag-stage {{ display:flex; flex-direction:column; align-items:center; padding-top:8px; }}
.bag-handles {{ width:90px; height:42px; border:3px solid #C8B9A6; border-bottom:none; border-radius:45px 45px 0 0; margin-bottom:-4px; }}
.bag-body {{
  width:246px; height:276px;
  background: linear-gradient(155deg, #F8F6F0 0%, #EFEBE2 65%, #E5DFD3 100%);
  border:1px solid rgba(52,51,47,0.14); border-radius:4px;
  box-shadow: 12px 14px 26px rgba(52,51,47,0.10);
  display:flex; flex-direction:column; align-items:center; justify-content:center; gap:18px;
  position:relative;
}}
.bag-fold {{ position:absolute; top:0; left:0; right:0; height:18px; border-bottom:1px solid rgba(52,51,47,0.08); background:rgba(52,51,47,0.02); }}

/* Tissue & Stickers */
.tissue-box {{
  height:184px; border-radius:10px; overflow:hidden; border:1px solid var(--selunea-line);
  position:relative; margin-bottom:16px;
}}
.sticker-row {{ display:flex; justify-content:space-around; align-items:center; padding-top:6px; }}
.sticker {{
  width:84px; height:84px; border-radius:50%; display:flex; align-items:center; justify-content:center;
  box-shadow:0 6px 14px rgba(52,51,47,0.10);
}}

/* Shipping Mailer */
.mailer {{
  background: var(--selunea-ivory); border:1px solid rgba(52,51,47,0.15); border-radius:10px;
  overflow:hidden; box-shadow:0 14px 26px rgba(52,51,47,0.09); height:300px; display:flex; flex-direction:column;
}}
.mailer-lid {{
  background: var(--selunea-ash); color: var(--selunea-ivory);
  padding: 28px 26px; text-align:center; display:flex; flex-direction:column; align-items:center; gap:10px;
}}
.mailer-tray {{
  flex:1; background: linear-gradient(180deg, #ECE7DC, #F3F0E9);
  display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px; padding:18px;
  border-top: 4px solid #C8B9A6;
}}
</style>
</head>
<body>
  <header class="header">
    <div>
      <div class="eyebrow">Stage 07 · Brand Applications (Stationery &amp; Collateral)</div>
      <h1 class="h1">Tactile Print, <em>Stationery &amp; Unboxing</em></h1>
    </div>
    <div>{hdr_wm}</div>
  </header>

  <section class="grid-top">
    <div class="card">
      <div class="label"><span>Business Cards · 85 × 55 mm</span><span>Uncoated Cotton + Foil</span></div>
      <div class="bcard-stack">
        <div class="bcard bcard-front">
          <div style="display:flex;justify-content:space-between;align-items:center;">{wm_ash}{mark_ash}</div>
          <div style="display:flex;justify-content:space-between;align-items:flex-end;">
            <div>
              <div style="font-family:var(--font-display);font-size:22px;font-weight:600;letter-spacing:0.06em;">NANA</div>
              <div style="font-size:9.5px;letter-spacing:0.16em;text-transform:uppercase;color:var(--selunea-ash-soft);">Founder &amp; Owner</div>
            </div>
            <div style="text-align:right;font-size:10px;color:var(--selunea-ash-soft);line-height:1.55;">
              nana@selunea.com<br/>@selunea.skin · selunea.com
            </div>
          </div>
        </div>
        <div class="bcard bcard-back">
          {mark_champ}
          {wm_champ}
          <div style="font-family:var(--font-display);font-style:italic;font-size:14px;color:#C8B9A6;">Beauty in Every Phase.</div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="label"><span>Thank-You Card · A6</span><span>Unboxing Moment</span></div>
      <div class="ty-card">
        <div>{mark_ash}</div>
        <div>
          <div style="font-size:10px;letter-spacing:0.22em;text-transform:uppercase;color:var(--selunea-ash-soft);margin-bottom:10px;">A Quiet Note</div>
          <div style="font-family:var(--font-display);font-size:32px;line-height:1.15;margin-bottom:12px;">Thank you for choosing<br/><em>gentle consistency.</em></div>
          <p style="font-size:12px;color:var(--selunea-ash-soft);line-height:1.6;max-width:280px;margin:0 auto;">
            Your skin shifts with every season and cycle. May this daily ritual meet you exactly where you are today.
          </p>
        </div>
        <div>{divider}</div>
      </div>
    </div>

    <div class="card">
      <div class="label"><span>Packaging Insert</span><span>5-Phase Ritual Card</span></div>
      <div class="insert-card">
        <div style="display:flex;justify-content:space-between;align-items:center;">
          <span style="font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:var(--selunea-ash-soft);">Your Daily Ritual</span>
          {wm_ash}
        </div>
        <div>
          <div class="step-row"><span class="step-num">01</span><b>Facial Cleanser</b><span style="margin-left:auto;color:var(--selunea-ash-soft);">Purify</span></div>
          <div class="step-row"><span class="step-num">02</span><b>Balancing Toner</b><span style="margin-left:auto;color:var(--selunea-ash-soft);">Prepare</span></div>
          <div class="step-row"><span class="step-num">03</span><b>Daily Serum</b><span style="margin-left:auto;color:var(--selunea-ash-soft);">Treat</span></div>
          <div class="step-row"><span class="step-num">04</span><b>Moisturizer</b><span style="margin-left:auto;color:var(--selunea-ash-soft);">Nourish</span></div>
          <div class="step-row"><span class="step-num">05</span><b>Daily Sunscreen</b><span style="margin-left:auto;color:var(--selunea-ash-soft);">Shield</span></div>
        </div>
        <div style="font-family:var(--font-display);font-style:italic;font-size:15px;color:var(--selunea-ash-soft);text-align:center;">Skincare for every version of you.</div>
      </div>
    </div>
  </section>

  <section class="grid-bot">
    <div class="card">
      <div class="label"><span>Boutique Shopping Bag</span><span>Matte Ivory + Champagne Ribbon</span></div>
      <div class="bag-stage">
        <div class="bag-handles"></div>
        <div class="bag-body">
          <div class="bag-fold"></div>
          {stacked_ash}
          <div style="font-size:9px;letter-spacing:0.22em;text-transform:uppercase;color:var(--selunea-ash-soft);">Beauty in Every Phase</div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="label"><span>Tissue Paper &amp; Seal Stickers</span><span>Seamless Pattern + S Monogram</span></div>
      <div class="tissue-box">{pattern}</div>
      <div class="sticker-row">
        <div class="sticker" style="background:#F3F0E9;border:1px solid var(--selunea-line);">{mono_ash}</div>
        <div class="sticker" style="background:#34332F;">{mono_ivory}</div>
        <div class="sticker" style="background:#C8B9A6;">{mono_ash}</div>
      </div>
      <div style="text-align:center;font-size:10.5px;color:var(--selunea-ash-soft);margin-top:12px;">35 mm Circular Seal Stickers · Ivory, Midnight Ash &amp; Champagne Foil</div>
    </div>

    <div class="card">
      <div class="label"><span>E-Commerce Shipping Mailer Box</span><span>Exterior Ivory · Interior Ash Surprise</span></div>
      <div class="mailer">
        <div class="mailer-lid">
          {wm_white}
          <div style="font-family:var(--font-display);font-style:italic;font-size:21px;color:#C8B9A6;">“Beauty in Every Phase.”</div>
          <div style="font-size:9.5px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(243,240,233,0.65);">Skincare for every version of you</div>
        </div>
        <div class="mailer-tray">
          <div style="display:flex;gap:14px;align-items:center;">
            <span style="width:42px;height:42px;border-radius:50%;background:#D9DFD5;display:inline-block;border:1px solid rgba(52,51,47,0.1);"></span>
            <span style="width:42px;height:42px;border-radius:50%;background:#DCD9E2;display:inline-block;border:1px solid rgba(52,51,47,0.1);"></span>
            <span style="width:42px;height:42px;border-radius:50%;background:#E4DAD0;display:inline-block;border:1px solid rgba(52,51,47,0.1);"></span>
          </div>
          <div style="font-size:11px;color:var(--selunea-ash-soft);margin-top:6px;">Wrapped in seamless Lunar Phase tissue paper &amp; sealed with S Monogram sticker</div>
        </div>
      </div>
    </div>
  </section>
</body>
</html>
"""
    (BASE / "09-brand-applications" / "01-stationery-and-collateral.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
# STAGE 7C BOARD: SOCIAL MEDIA SYSTEM, DIGITAL WEBSITE & ART DIRECTION
# ---------------------------------------------------------------------------

def build_social_digital_board():
    hdr_wm = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:36px;width:auto;")
    wm_nav = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:22px;width:auto;")
    wm_sm_w = load_svg(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", style="height:22px;width:auto;")
    mark_w = load_svg(SVG_DIR / "selunea-brand-mark-white-reversed.svg", style="width:32px;height:32px;")
    mark_ash = load_svg(SVG_DIR / "selunea-brand-mark-midnight-ash.svg", style="width:28px;height:28px;")
    mono_champ = load_svg(SVG_DIR / "selunea-monogram-s-champagne.svg", style="width:34px;height:34px;")
    orbital = load_svg(GFX_DIR / "orbital-frame-accent.svg", style="width:130px;height:130px;opacity:0.75;")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>SELUNÉA — Stage 7 Social Media, Digital &amp; Art Direction</title>
{FONTS_HEAD}
<style>
{TOKENS_CSS}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{
  background: var(--selunea-ivory); color: var(--selunea-ash);
  font-family: var(--font-sans); width: 1600px; padding: 50px 58px 58px;
  -webkit-font-smoothing: antialiased;
}}
.header {{ display:flex; justify-content:space-between; align-items:flex-end; padding-bottom:22px; border-bottom:1px solid var(--selunea-line); margin-bottom:28px; }}
.eyebrow {{ font-size:11px; letter-spacing:0.22em; text-transform:uppercase; color:var(--selunea-ash-soft); margin-bottom:8px; }}
.h1 {{ font-family:var(--font-display); font-size:44px; font-weight:500; line-height:1.05; }}
.h1 em {{ font-style:italic; font-weight:400; }}
.layout {{ display:grid; grid-template-columns: 0.95fr 1.35fr; gap:26px; margin-bottom:24px; }}
.card {{ background:var(--selunea-ivory-tint); border:1px solid var(--selunea-line); border-radius:14px; padding:24px 26px; }}
.label {{ font-size:10px; letter-spacing:0.18em; text-transform:uppercase; color:var(--selunea-ash-soft); margin-bottom:16px; display:flex; justify-content:space-between; }}

/* Instagram Mockup */
.ig-wrap {{ display:grid; grid-template-columns: 1.2fr 0.72fr; gap:16px; }}
.phone {{
  background:#FFFFFF; border:1px solid var(--selunea-line); border-radius:20px; padding:16px;
  box-shadow:0 12px 24px rgba(52,51,47,0.07);
}}
.ig-head {{ display:flex; gap:12px; align-items:center; margin-bottom:12px; }}
.ig-av {{ width:54px; height:54px; border-radius:50%; background:var(--selunea-ash); display:flex; align-items:center; justify-content:center; flex-shrink:0; }}
.ig-bio {{ font-size:10.5px; color:var(--selunea-ash-soft); line-height:1.45; margin-bottom:12px; }}
.ig-highlights {{ display:flex; gap:10px; margin-bottom:12px; }}
.hl {{ text-align:center; font-size:8.5px; color:var(--selunea-ash-soft); }}
.hl-dot {{ width:34px; height:34px; border-radius:50%; border:1px solid var(--selunea-line); margin:0 auto 4px; }}
.ig-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:6px; }}
.ig-tile {{
  aspect-ratio:1/1; border-radius:6px; padding:8px; display:flex; flex-direction:column;
  justify-content:center; align-items:center; text-align:center; font-size:9px;
}}
.story-col {{ display:flex; flex-direction:column; gap:12px; }}
.story {{
  border-radius:16px; padding:18px 14px; height:236px; display:flex; flex-direction:column;
  justify-content:space-between; align-items:center; text-align:center;
  box-shadow:0 10px 20px rgba(52,51,47,0.08);
}}

/* Website Desktop Mockup */
.browser {{
  background:#FFFFFF; border:1px solid var(--selunea-line); border-radius:14px; overflow:hidden;
  box-shadow:0 14px 28px rgba(52,51,47,0.08);
}}
.b-bar {{
  background:var(--selunea-ivory); padding:10px 18px; border-bottom:1px solid var(--selunea-line);
  display:flex; justify-content:space-between; align-items:center;
}}
.b-nav {{ display:flex; gap:20px; font-size:10.5px; letter-spacing:0.14em; text-transform:uppercase; color:var(--selunea-ash-soft); }}
.hero {{
  background: radial-gradient(circle at 75% 45%, #FFFFFF 0%, #F3F0E9 55%, #E4DAD0 100%);
  padding:32px 34px; display:grid; grid-template-columns:1.2fr 0.8fr; align-items:center; gap:20px;
  border-bottom:1px solid var(--selunea-line);
}}
.hero h2 {{ font-family:var(--font-display); font-size:40px; font-weight:500; line-height:1.08; margin:8px 0 10px; }}
.hero p {{ font-size:12px; color:var(--selunea-ash-soft); line-height:1.55; margin-bottom:16px; max-width:340px; }}
.btn {{ display:inline-block; background:var(--selunea-ash); color:var(--selunea-ivory); font-size:10px; letter-spacing:0.18em; text-transform:uppercase; padding:10px 20px; border-radius:999px; }}
.plp {{ padding:22px 30px 26px; background:#FAF8F4; }}
.plp-grid {{ display:grid; grid-template-columns:repeat(5,1fr); gap:12px; margin-top:12px; }}
.p-card {{ background:#FFFFFF; border:1px solid var(--selunea-line); border-radius:10px; padding:12px 10px; text-align:center; }}
.p-thumb {{ height:76px; border-radius:6px; margin-bottom:8px; display:flex; align-items:center; justify-content:center; }}
.p-card strong {{ display:block; font-family:var(--font-display); font-size:15px; font-weight:600; }}
.p-card span {{ font-size:9px; letter-spacing:0.12em; text-transform:uppercase; color:var(--selunea-ash-soft); }}

/* Art Direction Strip */
.art-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:18px; }}
.art-box {{ background:var(--selunea-ivory); border:1px solid var(--selunea-line); border-radius:10px; padding:16px 18px; }}
.art-box strong {{ display:block; font-size:11.5px; letter-spacing:0.06em; margin-bottom:5px; }}
.art-box p {{ font-size:11px; color:var(--selunea-ash-soft); line-height:1.5; }}
</style>
</head>
<body>
  <header class="header">
    <div>
      <div class="eyebrow">Stage 07 · Social Media, Digital Storefront &amp; Art Direction</div>
      <h1 class="h1">Digital Ecosystem &amp; <em>Editorial Campaign</em></h1>
    </div>
    <div>{hdr_wm}</div>
  </header>

  <section class="layout">
    <!-- Social Media Identity -->
    <div class="card">
      <div class="label"><span>Instagram Profile, Feed &amp; Stories</span><span>@selunea.skin</span></div>
      <div class="ig-wrap">
        <div class="phone">
          <div class="ig-head">
            <div class="ig-av">{mark_w}</div>
            <div>
              <div style="font-weight:600;font-size:12.5px;">selunea.skin</div>
              <div style="font-size:10px;color:var(--selunea-ash-soft);">Skincare · Lunar Elegance</div>
            </div>
          </div>
          <div class="ig-bio">
            <b>SELUNÉA</b> · Beauty in Every Phase.<br/>
            Skincare for every version of you.<br/>
            <span style="color:var(--selunea-ash);text-decoration:underline;">selunea.com</span>
          </div>
          <div class="ig-highlights">
            <div class="hl"><div class="hl-dot" style="background:#D9DFD5;"></div>Cleanse</div>
            <div class="hl"><div class="hl-dot" style="background:#DCD9E2;"></div>Serum</div>
            <div class="hl"><div class="hl-dot" style="background:#E4DAD0;"></div>Nourish</div>
            <div class="hl"><div class="hl-dot" style="background:#34332F;"></div>Ritual</div>
          </div>
          <div class="ig-grid">
            <div class="ig-tile" style="background:#34332F;color:#F3F0E9;">{mono_champ}</div>
            <div class="ig-tile" style="background:linear-gradient(135deg,#FAF8F4,#E4DAD0);font-family:var(--font-display);font-size:12px;font-style:italic;">Beauty in<br/>Every Phase.</div>
            <div class="ig-tile" style="background:#DCD9E2;"><span style="font-size:7.5px;letter-spacing:0.16em;">PHASE 03</span><b style="font-family:var(--font-display);font-size:13px;">Daily Serum</b></div>
            <div class="ig-tile" style="background:#D9DFD5;"><span style="font-size:7.5px;letter-spacing:0.16em;">PHASE 01</span><b style="font-family:var(--font-display);font-size:13px;">Cleanser</b></div>
            <div class="ig-tile" style="background:#F3F0E9;border:1px solid var(--selunea-line);">{mark_ash}</div>
            <div class="ig-tile" style="background:#E4DAD0;"><span style="font-size:7.5px;letter-spacing:0.16em;">PHASE 05</span><b style="font-family:var(--font-display);font-size:13px;">Sunscreen</b></div>
          </div>
        </div>

        <div class="story-col">
          <div class="story" style="background:linear-gradient(180deg,#34332F,#242320);color:#F3F0E9;">
            <div style="font-size:8.5px;letter-spacing:0.2em;color:#C8B9A6;">NEW ARRIVAL</div>
            <div>
              {wm_sm_w}
              <div style="font-family:var(--font-display);font-style:italic;font-size:21px;margin-top:8px;">Daily Serum</div>
            </div>
            <div style="font-size:8.5px;letter-spacing:0.16em;border:1px solid rgba(200,185,166,0.45);padding:6px 12px;border-radius:99px;color:#C8B9A6;">EXPLORE PHASE 03</div>
          </div>
          <div class="story" style="background:radial-gradient(circle at 30% 25%,#FFFFFF,#F3F0E9 55%,#DCD9E2);border:1px solid var(--selunea-line);">
            <div style="font-size:8.5px;letter-spacing:0.2em;color:var(--selunea-ash-soft);">DAILY RITUAL</div>
            <div style="font-family:var(--font-display);font-size:20px;line-height:1.15;">Skincare for<br/><em>every version</em><br/>of you.</div>
            <div>{mark_ash}</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Website Digital Direction -->
    <div class="card">
      <div class="label"><span>E-Commerce Storefront Direction</span><span>Homepage Hero + 5-SKU Listing System</span></div>
      <div class="browser">
        <div class="b-bar">
          <div>{wm_nav}</div>
          <div class="b-nav"><span>Shop Ritual</span><span>Philosophy</span><span>Journal</span><span>Bag (0)</span></div>
        </div>
        <div class="hero">
          <div>
            <div style="font-size:9.5px;letter-spacing:0.22em;text-transform:uppercase;color:var(--selunea-ash-soft);">Lunar Elegance Skincare</div>
            <h2>Beauty in <em>Every Phase.</em></h2>
            <p>Calm, consistent daily skincare shaped around the evolving rhythm of your skin — crafted for women who value quiet efficacy.</p>
            <span class="btn">Explore The 5-Step Ritual</span>
          </div>
          <div style="display:flex;justify-content:center;align-items:center;position:relative;">
            {orbital}
            <div style="position:absolute;width:62px;height:112px;border-radius:16px 16px 8px 8px;background:linear-gradient(90deg,#ECEAEF,#FFFFFF 35%,#DCD9E2);border:1px solid #fff;box-shadow:0 12px 24px rgba(52,51,47,0.12);display:flex;align-items:center;justify-content:center;">
              {mark_ash}
            </div>
          </div>
        </div>
        <div class="plp">
          <div style="display:flex;justify-content:space-between;align-items:baseline;">
            <span style="font-family:var(--font-display);font-size:20px;font-weight:500;">The Core Collection</span>
            <span style="font-size:9.5px;letter-spacing:0.16em;text-transform:uppercase;color:var(--selunea-ash-soft);">5 Daily Essentials</span>
          </div>
          <div class="plp-grid">
            <div class="p-card"><div class="p-thumb" style="background:#D9DFD5;">{mark_ash}</div><strong>Cleanser</strong><span>Phase 01 · 120 mL</span></div>
            <div class="p-card"><div class="p-thumb" style="background:#DCD9E2;">{mark_ash}</div><strong>Toner</strong><span>Phase 02 · 150 mL</span></div>
            <div class="p-card"><div class="p-thumb" style="background:#DCD9E2;">{mark_ash}</div><strong>Serum</strong><span>Phase 03 · 30 mL</span></div>
            <div class="p-card"><div class="p-thumb" style="background:#E4DAD0;">{mark_ash}</div><strong>Moisturizer</strong><span>Phase 04 · 50 mL</span></div>
            <div class="p-card"><div class="p-thumb" style="background:#E4DAD0;">{mark_ash}</div><strong>Sunscreen</strong><span>Phase 05 · 50 mL</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Art Direction & Photography Rules -->
  <section class="card">
    <div class="label"><span>Art Direction &amp; Editorial Photography System</span><span>Campaign Visual Principles</span></div>
    <div class="art-grid">
      <div class="art-box">
        <strong>01 · Soft Directional Lighting</strong>
        <p>Low-angle 45° morning or twilight light casting long, diffused shadows across travertine, matte plaster, and frosted glass vessels.</p>
      </div>
      <div class="art-box">
        <strong>02 · Authentic Natural Skin</strong>
        <p>Real skin pores, calm luminosity, minimal makeup, diverse women aged 20–35. Strictly avoid plastic over-retouching or artificial sheen.</p>
      </div>
      <div class="art-box">
        <strong>03 · Fluid &amp; Pearl Surfaces</strong>
        <p>Subtle water ripples, frosted glass caustics, and warm neutral silk/ceramic reflections echoing quiet moonlight without glitter.</p>
      </div>
      <div class="art-box">
        <strong>04 · Editorial Negative Space</strong>
        <p>Reserve ≥40% open Moon Ivory or warm stone breathing room in every composition so typography and vessels feel unhurried and serene.</p>
      </div>
    </div>
  </section>
</body>
</html>
"""
    (BASE / "09-brand-applications" / "02-social-and-digital.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
# STAGE 8: COMPLETE 15-SECTION BRAND GUIDELINE DOCUMENT (HTML -> PDF)
# ---------------------------------------------------------------------------

def build_brand_guidelines():
    wm_ash = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:46px;width:auto;")
    wm_cover = load_svg(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", style="height:70px;width:auto;")
    sec_ash = load_svg(SVG_DIR / "selunea-secondary-skincare-midnight-ash.svg", style="height:56px;width:auto;")
    mark_ash = load_svg(SVG_DIR / "selunea-brand-mark-midnight-ash.svg", style="height:76px;width:76px;")
    mark_cover = load_svg(SVG_DIR / "selunea-brand-mark-champagne.svg", style="height:82px;width:82px;")
    mono_ash = load_svg(SVG_DIR / "selunea-monogram-s-midnight-ash.svg", style="height:76px;width:76px;")
    horiz_ash = load_svg(SVG_DIR / "selunea-horizontal-lockup-midnight-ash.svg", style="height:52px;width:auto;")
    stacked_ash = load_svg(SVG_DIR / "selunea-stacked-lockup-midnight-ash.svg", style="height:88px;width:auto;")
    wm_white = load_svg(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", style="height:42px;width:auto;")
    wm_small = load_svg(SVG_DIR / "selunea-wordmark-small-responsive.svg", style="height:32px;width:auto;")
    divider = load_svg(GFX_DIR / "lunar-phase-divider.svg", style="width:320px;height:auto;")
    orbital = load_svg(GFX_DIR / "orbital-frame-accent.svg", style="width:110px;height:110px;")
    pattern = load_svg(GFX_DIR / "phase-pattern-tile.svg", style="width:110px;height:110px;border-radius:8px;")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>SELUNÉA — Brand Identity Guidelines</title>
{FONTS_HEAD}
<style>
{TOKENS_CSS}
@page {{ size: A4 landscape; margin: 0; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{
  font-family: var(--font-sans);
  color: var(--selunea-ash);
  background: #DCD7CD;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}
.page {{
  width: 297mm; height: 210mm;
  background: var(--selunea-ivory);
  margin: 0 auto 14px;
  padding: 18mm 20mm 16mm;
  position: relative;
  display: flex; flex-direction: column; justify-content: space-between;
  page-break-after: always;
  overflow: hidden;
}}
.page-dark {{ background: var(--selunea-ash); color: var(--selunea-ivory); }}
.p-head {{
  display:flex; justify-content:space-between; align-items:center;
  padding-bottom:10px; border-bottom:1px solid var(--selunea-line);
  font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:var(--selunea-ash-soft);
}}
.page-dark .p-head {{ border-color: var(--selunea-line-dark); color: var(--selunea-champagne); }}
.p-foot {{
  display:flex; justify-content:space-between; align-items:center;
  padding-top:10px; border-top:1px solid var(--selunea-line);
  font-size:8.5px; letter-spacing:0.16em; text-transform:uppercase; color:var(--selunea-ash-soft);
}}
.page-dark .p-foot {{ border-color: var(--selunea-line-dark); color: rgba(243,240,233,0.55); }}
.sec-title {{ font-family:var(--font-display); font-size:34px; font-weight:500; line-height:1.1; margin-bottom:14px; }}
.sec-title em {{ font-style:italic; font-weight:400; }}
.lead {{ font-size:12.5px; line-height:1.65; color:var(--selunea-ash-soft); max-width:740px; }}
.cols2 {{ display:grid; grid-template-columns:1fr 1fr; gap:20px; }}
.cols3 {{ display:grid; grid-template-columns:repeat(3,1fr); gap:16px; }}
.cols4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:14px; }}
.box {{ background:#FAF8F4; border:1px solid var(--selunea-line); border-radius:10px; padding:16px 18px; }}
.box h3 {{ font-size:10px; letter-spacing:0.16em; text-transform:uppercase; color:var(--selunea-ash-soft); margin-bottom:8px; }}
.box p, .box li {{ font-size:11px; line-height:1.6; color:var(--selunea-ash-soft); }}
.box ul {{ list-style:none; }}
.box li::before {{ content:'— '; color:var(--selunea-champagne); }}
.logo-cell {{
  background:#FFFFFF; border:1px solid var(--selunea-line); border-radius:10px;
  padding:16px; display:flex; flex-direction:column; align-items:center; justify-content:space-between;
  min-height:132px; text-align:center;
}}
.logo-cell.dark {{ background:var(--selunea-ash); border-color:var(--selunea-ash); color:var(--selunea-ivory); }}
.logo-cell span {{ font-size:9px; letter-spacing:0.14em; text-transform:uppercase; opacity:0.7; margin-top:10px; }}
.clearspace-box {{
  border: 1.5px dashed #C8B9A6; padding: 26px 42px; display:inline-block; position:relative;
  background:#FFFFFF; border-radius:8px;
}}
.cs-tag {{ position:absolute; font-size:9px; font-weight:600; color:#9E8A72; background:#F3F0E9; padding:1px 5px; border-radius:3px; }}
table.spec {{ width:100%; border-collapse:collapse; font-size:10.5px; }}
table.spec th {{ text-align:left; font-size:9px; letter-spacing:0.14em; text-transform:uppercase; color:var(--selunea-ash-soft); padding:7px 8px; border-bottom:1px solid var(--selunea-ash); }}
table.spec td {{ padding:7px 8px; border-bottom:1px solid var(--selunea-line); }}
.misuse-card {{
  background:#FFFFFF; border:1px solid rgba(155,58,52,0.25); border-radius:8px; padding:12px;
  text-align:center; position:relative;
}}
.misuse-x {{
  position:absolute; top:8px; right:10px; color:#A83832; font-weight:600; font-size:12px;
}}
.misuse-card p {{ font-size:9.5px; color:#7A2B26; margin-top:8px; }}
</style>
</head>
<body>

  <!-- PAGE 1: COVER -->
  <section class="page page-dark">
    <div class="p-head">
      <span>SELUNÉA · Brand Identity Guidelines</span>
      <span>Edition 1.0 · Production Ready</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:22px;">
      {mark_cover}
      {wm_cover}
      <div style="font-family:var(--font-display);font-style:italic;font-size:28px;color:#C8B9A6;margin-top:4px;">“Beauty in Every Phase.”</div>
      <div style="font-size:11px;letter-spacing:0.24em;text-transform:uppercase;color:rgba(243,240,233,0.7);">
        Creative Direction: Lunar Elegance &nbsp;·&nbsp; Contemporary Skincare Identity
      </div>
    </div>
    <div class="p-foot">
      <span>Skincare for every version of you.</span>
      <span>01 / 07</span>
    </div>
  </section>

  <!-- PAGE 2: SECTIONS 1–4 (BRAND STRATEGY) -->
  <section class="page">
    <div class="p-head"><span>01–04 · Brand Foundation</span><span>SELUNÉA Brand Guidelines</span></div>
    <div>
      <h2 class="sec-title">01–04 · Brand Introduction, Philosophy, <em>Positioning &amp; Personality</em></h2>
      <p class="lead" style="margin-bottom:18px;">
        SELUNÉA is an affordable-premium contemporary skincare brand crafted for women aged 20–35. Rather than promising instant overnight miracles, Selunéa celebrates the evolving rhythm of real skin and the quiet power of consistent daily self-care.
      </p>
      <div class="cols2" style="margin-bottom:16px;">
        <div class="box">
          <h3>01 · Brand Introduction &amp; 02 · Philosophy</h3>
          <p>Inspired by the phases of the moon, Selunéa reflects how skin naturally shifts across stress, climate, and monthly cycles. Every formulation and visual touchpoint expresses calm equilibrium — anchored by our core message <b>“Beauty in Every Phase.”</b> and supporting tagline <b>“Skincare for every version of you.”</b></p>
        </div>
        <div class="box">
          <h3>03 · Brand Positioning</h3>
          <p><b>Affordable Premium Skincare:</b> Occupies the refined editorial territory between cold clinical ingredient brands and inaccessible heritage luxury. Visually composed and tactile (frosted glass, matte ivory, disciplined negative space), yet emotionally warm and inviting for daily use.</p>
        </div>
      </div>
      <div class="cols3">
        <div class="box">
          <h3>04 · Brand Personality</h3>
          <ul>
            <li>Refined &amp; Sophisticated</li>
            <li>Feminine &amp; Approachable</li>
            <li>Calm, Confident &amp; Timeless</li>
          </ul>
        </div>
        <div class="box">
          <h3>Creative Pillars (Embrace)</h3>
          <ul>
            <li>Modern feminine minimalism</li>
            <li>Subtle lunar geometry &amp; negative space</li>
            <li>High-contrast couture editorial clarity</li>
          </ul>
        </div>
        <div class="box">
          <h3>Category Guardrails (Avoid)</h3>
          <ul>
            <li>Generic crescent moon &amp; star clip-art</li>
            <li>Astrology, tarot, or purple galaxy gradients</li>
            <li>Generic leaves or heavy gold framing</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="p-foot"><span>Sections 1–4 · Brand Strategy</span><span>02 / 07</span></div>
  </section>

  <!-- PAGE 3: SECTIONS 5–6 (LOGO CONCEPT & COMPLETE VARIATIONS) -->
  <section class="page">
    <div class="p-head"><span>05–06 · Logo System</span><span>SELUNÉA Brand Guidelines</span></div>
    <div>
      <h2 class="sec-title">05 · Logo Concept &amp; 06 · <em>Approved Logo Architecture</em></h2>
      <p class="lead" style="margin-bottom:14px;">
        Our bespoke high-contrast serif-less wordmark pairs architectural poise with a subtle <b>L→U lunar cradle swash</b> (highlighting the <em>LUN</em> root) and a 30° moonlight acute sliver on <b>É</b>. It works seamlessly alongside the <b>Celestial Lotus-Moon Brand Mark</b> and <b>Celestial S Monogram</b> across every bottle, cap, carton, and 16 px digital icon.
      </p>
      <div class="cols4" style="margin-bottom:14px;">
        <div class="logo-cell">{wm_ash}<span>Primary Wordmark (Midnight Ash)</span></div>
        <div class="logo-cell">{sec_ash}<span>Secondary Logo (With Descriptor)</span></div>
        <div class="logo-cell">{mark_ash}<span>Brand Mark (Celestial Lotus-Moon)</span></div>
        <div class="logo-cell">{mono_ash}<span>Monogram S (Caps &amp; Seals)</span></div>
      </div>
      <div class="cols4">
        <div class="logo-cell">{horiz_ash}<span>Horizontal Lockup</span></div>
        <div class="logo-cell">{stacked_ash}<span>Stacked Lockup (Cartons &amp; Bags)</span></div>
        <div class="logo-cell dark">{wm_white}<span>Reversed White (Irradiation-Thinned)</span></div>
        <div class="logo-cell">{wm_small}<span>Small-Size Responsive Cut (&lt;18 mm)</span></div>
      </div>
    </div>
    <div class="p-foot"><span>Sections 5–6 · Logo Architecture (Pure Outlined SVG Masters)</span><span>03 / 07</span></div>
  </section>

  <!-- PAGE 4: SECTIONS 7–9 (CLEAR SPACE, MINIMUM SIZE & INCORRECT USAGE) -->
  <section class="page">
    <div class="p-head"><span>07–09 · Logo Governance</span><span>SELUNÉA Brand Guidelines</span></div>
    <div>
      <h2 class="sec-title">07 · Clear Space, 08 · Minimum Sizes &amp; 09 · <em>Incorrect Usage</em></h2>
      <div class="cols2" style="margin-bottom:16px;align-items:center;">
        <div class="box" style="text-align:center;">
          <h3 style="text-align:left;">07 · Minimum Clear Space Rule (x = Cap Height of E)</h3>
          <div class="clearspace-box" style="margin:8px 0;">
            <span class="cs-tag" style="top:4px;left:50%;transform:translateX(-50%);">0.5x</span>
            <span class="cs-tag" style="bottom:4px;left:50%;transform:translateX(-50%);">0.5x</span>
            <span class="cs-tag" style="left:6px;top:50%;transform:translateY(-50%);">0.75x</span>
            <span class="cs-tag" style="right:6px;top:50%;transform:translateY(-50%);">0.75x</span>
            {wm_ash}
          </div>
          <p style="margin-top:8px;">Keep text, seams, borders, and neighboring elements outside the protected breathing zone.</p>
        </div>
        <div class="box">
          <h3>08 · Documented Minimum Sizes</h3>
          <table class="spec">
            <thead><tr><th>Logo Version</th><th>Print Min.</th><th>Digital Min.</th><th>Primary Application</th></tr></thead>
            <tbody>
              <tr><td><b>Primary Wordmark</b></td><td>24 mm wide</td><td>110 px wide</td><td>Bottles, cartons, desktop headers</td></tr>
              <tr><td><b>Small Responsive Wordmark</b></td><td>15 mm wide</td><td>72 px wide</td><td>30 mL serum, 50 mL jar, mobile nav</td></tr>
              <tr><td><b>Horizontal Lockup</b></td><td>32 mm wide</td><td>140 px wide</td><td>Stationery, email signatures, web</td></tr>
              <tr><td><b>Lunar Brand Mark</b></td><td>7 mm</td><td>16 px</td><td>Favicon, avatars, micro-stamps</td></tr>
              <tr><td><b>Celestial S Monogram</b></td><td>9 mm</td><td>24 px</td><td>12–14 mm dropper caps &amp; jar lids</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <h3 style="font-size:10px;letter-spacing:0.16em;text-transform:uppercase;color:var(--selunea-ash-soft);margin-bottom:10px;">09 · Incorrect Logo Usage (Strictly Prohibited)</h3>
      <div class="cols4">
        <div class="misuse-card">
          <span class="misuse-x">✕</span>
          <div style="transform:scaleX(1.38) scaleY(0.75);">{load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:28px;width:auto;")}</div>
          <p>Do not stretch or distort proportions</p>
        </div>
        <div class="misuse-card">
          <span class="misuse-x">✕</span>
          <div style="filter:drop-shadow(3px 4px 3px rgba(0,0,0,0.45));">{load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:28px;width:auto;")}</div>
          <p>Do not apply drop shadows, glow, or 3D bevels</p>
        </div>
        <div class="misuse-card" style="background:#F3F0E9;">
          <span class="misuse-x">✕</span>
          <div>{load_svg(SVG_DIR / "selunea-primary-wordmark-champagne.svg", style="height:28px;width:auto;")}</div>
          <p>Do not place low-contrast Champagne ink on Ivory</p>
        </div>
        <div class="misuse-card">
          <span class="misuse-x">✕</span>
          <div style="font-family:Georgia,serif;font-size:22px;letter-spacing:0.15em;">SELUNEA</div>
          <p>Do not re-type in stock fonts or omit the É accent</p>
        </div>
      </div>
    </div>
    <div class="p-foot"><span>Sections 7–9 · Logo Integrity Rules</span><span>04 / 07</span></div>
  </section>

  <!-- PAGE 5: SECTIONS 10–11 (COLOR & TYPOGRAPHY SPECS) -->
  <section class="page">
    <div class="p-head"><span>10–11 · Color &amp; Typography</span><span>SELUNÉA Brand Guidelines</span></div>
    <div>
      <h2 class="sec-title">10 · Color Specifications &amp; 11 · <em>Typography System</em></h2>
      <div class="cols2">
        <div class="box">
          <h3>10 · Master Color Table (Verify Pantone Physically Before Press)</h3>
          <table class="spec">
            <thead><tr><th>Swatch &amp; Name</th><th>HEX</th><th>CMYK (Approx)</th><th>Role &amp; WCAG</th></tr></thead>
            <tbody>
              <tr><td><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:#F3F0E9;border:1px solid #999;margin-right:6px;"></span><b>Moon Ivory</b></td><td>#F3F0E9</td><td>0 / 1 / 4 / 5</td><td>Canvas (58%) · AAA</td></tr>
              <tr><td><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:#34332F;margin-right:6px;"></span><b>Midnight Ash</b></td><td>#34332F</td><td>0 / 2 / 10 / 80</td><td>Logo/Ink (24%) · AAA</td></tr>
              <tr><td><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:#C8B9A6;margin-right:6px;"></span><b>Champagne Beige</b></td><td>#C8B9A6</td><td>0 / 8 / 17 / 22</td><td>Foil / On Ash (6.6:1)</td></tr>
              <tr><td><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:#B8B7B1;margin-right:6px;"></span><b>Lunar Silver</b></td><td>#B8B7B1</td><td>0 / 1 / 4 / 28</td><td>Metal / On Ash (6.3:1)</td></tr>
              <tr><td><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:#D9DFD5;border:1px solid #bbb;margin-right:6px;"></span><b>Sage Haze</b></td><td>#D9DFD5</td><td>3 / 0 / 4 / 13</td><td>SKU: Facial Cleanser</td></tr>
              <tr><td><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:#DCD9E2;border:1px solid #bbb;margin-right:6px;"></span><b>Lavender Mist</b></td><td>#DCD9E2</td><td>3 / 4 / 0 / 11</td><td>SKU: Toner &amp; Serum</td></tr>
              <tr><td><span style="display:inline-block;width:11px;height:11px;border-radius:50%;background:#E4DAD0;border:1px solid #bbb;margin-right:6px;"></span><b>Soft Nude</b></td><td>#E4DAD0</td><td>0 / 4 / 9 / 11</td><td>SKU: Moisturize / SPF</td></tr>
            </tbody>
          </table>
        </div>
        <div class="box">
          <h3>11 · Typography Hierarchy (SIL OFL Commercial Safe)</h3>
          <div style="margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid var(--selunea-line);">
            <div style="font-size:9px;letter-spacing:0.16em;text-transform:uppercase;color:var(--selunea-ash-soft);">Display &amp; Campaign · Cormorant Garamond</div>
            <div style="font-family:var(--font-display);font-size:30px;line-height:1.15;">Beauty in <em>Every Phase.</em></div>
          </div>
          <div style="margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid var(--selunea-line);">
            <div style="font-size:9px;letter-spacing:0.16em;text-transform:uppercase;color:var(--selunea-ash-soft);">Headings &amp; Body · DM Sans (400 / 500)</div>
            <div style="font-size:15px;font-weight:500;margin-bottom:4px;">Skincare for every version of you.</div>
            <div style="font-size:11px;color:var(--selunea-ash-soft);line-height:1.55;">Clean geometric neutrality keeps ritual steps, web navigation, and INCI packaging specs effortlessly legible without competing with the serif voice.</div>
          </div>
          <div>
            <div style="font-size:9px;letter-spacing:0.16em;text-transform:uppercase;color:var(--selunea-ash-soft);margin-bottom:4px;">Product Information · DM Sans Medium Uppercase (+0.18em)</div>
            <div style="font-size:10.5px;font-weight:500;letter-spacing:0.18em;text-transform:uppercase;">PHASE 03 · DAILY SERUM · 30 ML / 1.0 FL. OZ.</div>
          </div>
        </div>
      </div>
    </div>
    <div class="p-foot"><span>Sections 10–11 · Color &amp; Typography Standards</span><span>05 / 07</span></div>
  </section>

  <!-- PAGE 6: SECTIONS 12–13 (GRAPHIC ELEMENTS & PHOTOGRAPHY DIRECTION) -->
  <section class="page">
    <div class="p-head"><span>12–13 · Graphic Language &amp; Art Direction</span><span>SELUNÉA Brand Guidelines</span></div>
    <div>
      <h2 class="sec-title">12 · Graphic Elements &amp; 13 · <em>Editorial Photography Direction</em></h2>
      <div class="cols3" style="margin-bottom:18px;">
        <div class="box" style="text-align:center;">
          <h3>Phase Horizon Divider</h3>
          <div style="padding:36px 0;">{divider}</div>
          <p>Separates editorial chapters, thank-you notes, and carton back-panels.</p>
        </div>
        <div class="box" style="text-align:center;">
          <h3>Concentric Orbital Accent</h3>
          <div style="padding:4px 0;">{orbital}</div>
          <p>Frames hero bottles in web/social layouts with quiet celestial rhythm.</p>
        </div>
        <div class="box" style="text-align:center;">
          <h3>Seamless Tissue Pattern</h3>
          <div style="padding:4px 0;">{pattern}</div>
          <p>Derived directly from the Lunar Emblem for tissue paper &amp; carton liners.</p>
        </div>
      </div>
      <div class="box">
        <h3>13 · Editorial Photography Art Direction</h3>
        <div class="cols4" style="margin-top:6px;">
          <div><b>Lighting:</b><p>Soft 45° directional morning/dusk glow; diffused glass caustics; zero harsh flash.</p></div>
          <div><b>Skin Authenticity:</b><p>Natural pores, healthy hydration, real women 20–35; never over-retouched plastic skin.</p></div>
          <div><b>Materials &amp; Props:</b><p>Matte limestone, travertine, warm linen, frosted glass, subtle fluid water ripples.</p></div>
          <div><b>Composition:</b><p>≥40% calm negative space; warm Moon Ivory &amp; neutral stone tones; editorial stillness.</p></div>
        </div>
      </div>
    </div>
    <div class="p-foot"><span>Sections 12–13 · Supporting Visual System</span><span>06 / 07</span></div>
  </section>

  <!-- PAGE 7: SECTIONS 14–15 (PACKAGING & SOCIAL APPLICATIONS SUMMARY + HANDOVER) -->
  <section class="page">
    <div class="p-head"><span>14–15 · Applications &amp; Production Handover</span><span>SELUNÉA Brand Guidelines</span></div>
    <div>
      <h2 class="sec-title">14 · Packaging Applications &amp; 15 · <em>Social Media System</em></h2>
      <div class="cols2" style="margin-bottom:16px;">
        <div class="box">
          <h3>14 · Five-SKU Packaging Architecture</h3>
          <table class="spec">
            <thead><tr><th>Phase &amp; SKU</th><th>Vessel Format</th><th>Category Tint</th><th>Net Placeholder</th></tr></thead>
            <tbody>
              <tr><td><b>01 · Facial Cleanser</b></td><td>Matte Ivory Tube</td><td>Sage Haze (#D9DFD5)</td><td>120 mL</td></tr>
              <tr><td><b>02 · Balancing Toner</b></td><td>Frosted Glass Bottle + Silver Cap</td><td>Lavender Mist (#DCD9E2)</td><td>150 mL</td></tr>
              <tr><td><b>03 · Daily Serum</b></td><td>Frosted Dropper + Champagne Collar</td><td>Lavender Mist (#DCD9E2)</td><td>30 mL</td></tr>
              <tr><td><b>04 · Moisturizer</b></td><td>Frosted Heavy Glass Jar + Debossed Lid</td><td>Soft Nude (#E4DAD0)</td><td>50 mL</td></tr>
              <tr><td><b>05 · Daily Sunscreen</b></td><td>Matte Oval Tube + Champagne Cap</td><td>Soft Nude (#E4DAD0)</td><td>50 mL</td></tr>
            </tbody>
          </table>
          <p style="margin-top:8px;">Full visual lineup: <code>08-packaging/01-skincare-packaging-family.png</code></p>
        </div>
        <div class="box">
          <h3>15 · Social Media &amp; Digital Governance</h3>
          <ul>
            <li><b>Profile Avatar:</b> White Lunar Brand Mark centered on Midnight Ash circular tile (<code>#34332F</code>).</li>
            <li><b>Feed Rhythm:</b> Alternate macro frosted-glass product stills, natural skin editorial portraits, and quiet Moon Ivory typographic quote cards (never overcrowded text).</li>
            <li><b>Stories &amp; Campaigns:</b> Pair Cormorant Garamond italic headlines with DM Sans tracked phase tags; keep ≥35% clean margin around edges.</li>
            <li><b>Legal &amp; Pre-Press Notice:</b> Conduct formal trademark clearance &amp; physical Pantone/foil press proofs before mass packaging production.</li>
          </ul>
          <p style="margin-top:10px;">Full visual showcase: <code>09-brand-applications/02-social-and-digital.png</code></p>
        </div>
      </div>
      <div class="box" style="background:var(--selunea-ash);color:var(--selunea-ivory);display:flex;justify-content:space-between;align-items:center;">
        <div>
          <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:#C8B9A6;">Master File Directory</div>
          <div style="font-size:11.5px;margin-top:3px;">All vector SVG masters, transparent PNGs, web icons, packaging boards &amp; source scripts live in <code>selunea-brand-identity/</code>.</div>
        </div>
        <div>{wm_white}</div>
      </div>
    </div>
    <div class="p-foot"><span>Sections 14–15 · Production Ready</span><span>07 / 07</span></div>
  </section>

</body>
</html>
"""
    (BASE / "10-brand-guidelines" / "selunea-brand-guidelines.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
# STAGE 8B: CLIENT PRESENTATION BOARD SPEC (for logo-design presentation_board.py)
# ---------------------------------------------------------------------------

def build_presentation_spec():
    import json
    spec = {
        "brand": "SELUNÉA",
        "tagline": "Beauty in Every Phase.",
        "brief": "Complete brand identity for SELUNÉA, an affordable premium contemporary skincare brand for women aged 20–35. Creative direction: Lunar Elegance — refined feminine minimalism expressed through custom high-contrast couture typography, subtle lunar-phase negative space, and tactile matte ivory / frosted glass packaging.",
        "adjectives": ["Refined", "Feminine", "Calm", "Confident", "Timeless"],
        "industry": "retail",
        "mockups": ["shopping-bag", "box", "business-card", "website", "social", "tote"],
        "nav": ["Ritual", "Products", "Philosophy", "Journal"],
        "brand_color": "#34332F",
        "tile_color": "#34332F",
        "greyscale": False,
        "final": True,
        "round": 2,
        "concepts": [
            {
                "name": "SELUNÉA — Lunar Elegance Identity System",
                "symbol": "../05-logo-final/svg/selunea-brand-mark-midnight-ash.svg",
                "lockup": "../05-logo-final/svg/selunea-horizontal-lockup-midnight-ash.svg",
                "stacked": "../05-logo-final/svg/selunea-stacked-lockup-midnight-ash.svg",
                "avatar": "../05-logo-final/svg/selunea-brand-mark-small-responsive.svg",
                "symbol_on_tile": "../05-logo-final/svg/selunea-brand-mark-white-reversed.svg",
                "lockup_on_tile": "../05-logo-final/svg/selunea-horizontal-lockup-white-reversed.svg",
                "stacked_on_tile": "../05-logo-final/svg/selunea-stacked-lockup-white-reversed.svg",
                "symbol_on_dark": "../05-logo-final/svg/selunea-brand-mark-champagne.svg",
                "lockup_on_dark": "../05-logo-final/svg/selunea-horizontal-lockup-champagne.svg",
                "stacked_on_dark": "../05-logo-final/svg/selunea-stacked-lockup-champagne.svg",
                "idea": "A couture serif-less high-contrast SELUNÉA wordmark (with L→U lunar cradle swash & 30° É moonlight sliver) unified with a 100/100 Celestial Lotus-Moon Brand Mark and Celestial S Monogram.",
                "rationale": [
                    "Honors the owner's preferred sleek high-contrast fashion-editorial sans style while staying 100% original to SELUNÉA and its Moon Ivory / Midnight Ash / Champagne Beige palette.",
                    "Celestial Lotus-Moon Brand Mark scores 100/100 on automated vector audit with pure expanded outlines and survives 16 px favicons, frosted glass silkscreen, and Champagne foil jar lids effortlessly.",
                    "Includes dedicated irradiation-thinned reversed white artwork and reinforced small-size responsive cuts for 30 mL serum bottles and 16 px web icons."
                ]
            }
        ],
        "recommendation": "Approved final brand identity system ready for print proofing, packaging production, and digital launch (remember to complete formal trademark clearance and physical Pantone/foil press proofs prior to mass manufacturing)."
    }
    (BASE / "11-presentations" / "presentation-spec.json").write_text(json.dumps(spec, indent=2), encoding="utf-8")


if __name__ == "__main__":
    build_stage6_board()
    build_packaging_board()
    build_stationery_collateral_board()
    build_social_digital_board()
    build_brand_guidelines()
    build_presentation_spec()
    print("Built all Stage 6, 7 & 8 HTML boards and presentation spec successfully.")
