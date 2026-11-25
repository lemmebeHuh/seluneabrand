"""
SELUNÉA — Complete Responsive Brand Identity Showcase Website Builder
Output: c:/Users/ridwa/Desktop/selunea/selunea-brand-identity/index.html

Features:
- All visuals & brand identity chapters unified into one cohesive, mobile-responsive web portal
- Bespoke minimalist vector "by KALLA" studio signature mark (header badge & footer colophon)
- Owner attribution throughout: NANA (Founder & Owner · nana@selunea.com)
- Interactive Logo Surface Playground (switch live between Moon Ivory, Pure White, Midnight Ash,
  Sage Haze, Lavender Mist, Soft Nude — with automatic contrast-correct vector logo swaps)
- Click-to-copy Color Swatches with HEX, RGB, CMYK, Pantone approx & verified WCAG badges
- Complete Responsive 5-SKU Skincare Packaging Family + Folding Cartons + Cap Seals
- Interactive Full-Screen Lightbox Gallery for all presentation & visual boards (touch & keyboard friendly)
- Direct download / open links for SVG masters, high-res PNGs, Web Icons, and Brand Guidelines PDF
- True 3-state responsive layout (Mobile <640px, Tablet 640-1024px, Desktop >1024px),
  >=44x44px touch targets, zero horizontal overflow, labeled mobile menu drawer.
"""

from pathlib import Path
import re

BASE = Path(r"c:\Users\ridwa\Desktop\selunea\selunea-brand-identity")
SVG_DIR = BASE / "05-logo-final" / "svg"
GFX_DIR = BASE / "07-graphic-assets"


def load_svg(path: Path, css_class: str = "", style: str = "") -> str:
    txt = path.read_text(encoding="utf-8").strip()
    txt = re.sub(r'\s+aria-labelledby="[^"]*"', "", txt)
    txt = re.sub(r'<title[^>]*>.*?</title>\s*', "", txt, flags=re.S)
    # Remove fixed pixel width/height attributes on inline SVGs so viewBox + CSS control fluid mobile sizing cleanly
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


# Bespoke minimalist "by KALLA" studio mark (clean vector geometry, explicit aspect width so left-aligns cleanly)
def kalla_signature_svg(color="#34332F", accent="#C8B9A6", height=18):
    width = round(height * (186.0 / 28.0), 1)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 186 28" width="{width}" height="{height}" class="kalla-svg" role="img" aria-label="by KALLA">
  <!-- Minimalist Kalla emblem: poised open architectural K-diamond -->
  <g fill="{accent}">
    <path d="M 6 4 L 8.2 4 L 8.2 24 L 6 24 Z"/>
    <path d="M 9.4 14 L 17.8 4 L 20.4 4 L 12.0 14 L 20.4 24 L 17.8 24 Z"/>
    <circle cx="2.2" cy="14" r="2.1"/>
  </g>
  <!-- Crisp editorial label -->
  <text x="30" y="18.5" fill="{color}" font-family="'DM Sans', sans-serif" font-size="10.5" letter-spacing="2.4" opacity="0.72">BY</text>
  <text x="54" y="19" fill="{color}" font-family="'Cormorant Garamond', Georgia, serif" font-size="18" font-weight="600" letter-spacing="4.2">KALLA</text>
</svg>'''


def build_website():
    # Load all real Stage 5 SVG masters inline
    wm_nav = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", css_class="nav-wm")
    wm_hero = load_svg(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", css_class="hero-wm")
    mark_hero = load_svg(SVG_DIR / "selunea-brand-mark-champagne.svg", css_class="hero-mark")

    # Playground SVGs (both dark-ink and light-ink pairs)
    wm_ash = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", css_class="pg-svg")
    wm_white = load_svg(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", css_class="pg-svg")
    wm_champ = load_svg(SVG_DIR / "selunea-primary-wordmark-champagne.svg", css_class="pg-svg")

    sec_ash = load_svg(SVG_DIR / "selunea-secondary-skincare-midnight-ash.svg", css_class="arch-svg")
    mark_ash = load_svg(SVG_DIR / "selunea-brand-mark-midnight-ash.svg", css_class="arch-svg-sq")
    mark_white = load_svg(SVG_DIR / "selunea-brand-mark-white-reversed.svg", css_class="arch-svg-sq")
    mono_ash = load_svg(SVG_DIR / "selunea-monogram-s-midnight-ash.svg", css_class="arch-svg-sq")
    mono_champ = load_svg(SVG_DIR / "selunea-monogram-s-champagne.svg", css_class="arch-svg-sq")
    horiz_ash = load_svg(SVG_DIR / "selunea-horizontal-lockup-midnight-ash.svg", css_class="arch-svg")
    stacked_ash = load_svg(SVG_DIR / "selunea-stacked-lockup-midnight-ash.svg", css_class="arch-svg-tall")
    wm_small = load_svg(SVG_DIR / "selunea-wordmark-small-responsive.svg", css_class="arch-svg-sm")
    wm_ash_sm = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", css_class="arch-svg")
    wm_white_arch = load_svg(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", css_class="arch-svg")

    # Graphic language SVGs
    divider_svg = load_svg(GFX_DIR / "lunar-phase-divider.svg", css_class="gfx-divider")
    orbital_svg = load_svg(GFX_DIR / "orbital-frame-accent.svg", css_class="gfx-sq")
    pattern_svg = load_svg(GFX_DIR / "phase-pattern-tile.svg", css_class="gfx-sq-rad")
    pearl_svg = load_svg(GFX_DIR / "pearl-luminosity-backdrop.svg", css_class="gfx-wide")

    # Small inline SVGs for business card preview & footer
    wm_card = load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:22px;width:auto;")
    mark_card = load_svg(SVG_DIR / "selunea-brand-mark-midnight-ash.svg", style="height:26px;width:26px;")
    mark_card_ch = load_svg(SVG_DIR / "selunea-brand-mark-champagne.svg", style="height:36px;width:36px;")
    wm_card_ch = load_svg(SVG_DIR / "selunea-primary-wordmark-champagne.svg", style="height:22px;width:auto;")
    wm_footer = load_svg(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", style="height:30px;width:auto;")

    kalla_light = kalla_signature_svg(color="#34332F", accent="#9F8B72", height=17)
    kalla_dark = kalla_signature_svg(color="#F3F0E9", accent="#C8B9A6", height=20)
    kalla_hero = kalla_signature_svg(color="#F3F0E9", accent="#C8B9A6", height=18)

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>SELUNÉA — Brand Identity Showcase by KALLA</title>
<meta name="description" content="Complete Brand Identity System for SELUNÉA (Beauty in Every Phase) — Presented for NANA, designed by KALLA." />
<link rel="icon" type="image/svg+xml" href="05-logo-final/web-icons/favicon.svg" />
<link rel="icon" href="05-logo-final/web-icons/favicon.ico" sizes="any" />
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
  }}

  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; scroll-padding-top: calc(var(--nav-h) + 16px); overflow-x: clip; }}
  body {{
    background: var(--ivory);
    color: var(--ash);
    font-family: var(--font-sans);
    font-size: 15px;
    line-height: 1.65;
    width: 100%;
    max-width: 100vw;
    overflow-x: clip;
    -webkit-font-smoothing: antialiased;
  }}
  img, svg {{ max-width: 100%; display: block; }}
  /* Prevent any CSS Grid or Flex child from blowing out 390px mobile viewport width */
  section, header, footer, .wrap, .editorial-panel, .playground, .pg-stage, .board-feature,
  .hero-grid > *, .strategy-grid > *, .arch-grid > *, .gov-grid > *, .color-grid > *,
  .type-stack > *, .gfx-grid > *, .sku-cards > *, .owner-spot > *, .boards-grid > *, .dl-grid > *, .footer-top > * {{
    min-width: 0;
  }}
  a {{ color: inherit; text-decoration: none; }}
  button {{ font-family: inherit; cursor: pointer; background: none; border: none; color: inherit; }}
  :focus-visible {{ outline: 2px solid var(--ash); outline-offset: 3px; border-radius: 4px; }}
  .dark-surface :focus-visible {{ outline-color: var(--champagne); }}

  .wrap {{
    width: 100%;
    max-width: var(--container);
    margin: 0 auto;
    padding: 0 20px;
  }}

  /* ---------------- STICKY NAVIGATION (COMPACT & MOBILE-FIRST) ---------------- */
  .topbar {{
    position: sticky; top: 0; z-index: 60;
    height: var(--nav-h);
    background: rgba(243, 240, 233, 0.94);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--line);
  }}
  .topbar-inner {{
    height: 100%;
    display: flex; align-items: center; justify-content: space-between; gap: 12px;
  }}
  .brand-lock {{
    display: flex; align-items: center; gap: 12px; min-width: 0;
  }}
  .nav-wm {{ height: 22px; width: auto; flex-shrink: 0; }}
  .nav-sep {{ width: 1px; height: 18px; background: var(--line); display: none; }}
  .nav-kalla {{ display: none; align-items: center; }}

  .nav-links {{
    display: none; align-items: center; gap: 6px;
  }}
  .nav-links a {{
    font-size: 12.5px; letter-spacing: 0.06em; color: var(--ash-soft);
    padding: 10px 12px; border-radius: 8px; transition: color 0.18s, background 0.18s;
  }}
  .nav-links a:hover, .nav-links a.active {{ color: var(--ash); background: rgba(52,51,47,0.06); }}

  .nav-actions {{ display: flex; align-items: center; gap: 8px; }}
  .btn-pdf-sm {{
    display: none;
    font-size: 11px; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase;
    padding: 10px 16px; border-radius: 999px;
    background: var(--ash); color: var(--ivory);
    min-height: 40px; align-items: center;
  }}
  .btn-pdf-sm:hover {{ background: var(--ash-deep); }}

  .menu-toggle {{
    display: inline-flex; align-items: center; gap: 8px;
    min-height: 44px; min-width: 44px; padding: 0 14px;
    border: 1px solid var(--line); border-radius: 999px;
    background: var(--ivory-card);
    font-size: 12px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase;
  }}
  .menu-toggle:active {{ background: var(--ivory-deep); }}

  /* Mobile Slide Drawer */
  .mobile-drawer {{
    display: none;
    position: fixed; inset: var(--nav-h) 0 0 0; z-index: 55;
    background: rgba(243, 240, 233, 0.98);
    padding: 20px 20px 36px;
    overflow-y: auto;
    border-top: 1px solid var(--line);
  }}
  .mobile-drawer.open {{ display: flex; flex-direction: column; justify-content: space-between; gap: 24px; }}
  .drawer-nav {{ display: flex; flex-direction: column; gap: 6px; }}
  .drawer-nav a {{
    display: flex; align-items: center; justify-content: space-between;
    min-height: 48px; padding: 12px 14px;
    border-bottom: 1px solid var(--line);
    font-family: var(--font-display); font-size: 24px; font-weight: 500;
  }}
  .drawer-nav a span.num {{
    font-family: var(--font-sans); font-size: 11px; letter-spacing: 0.16em; color: var(--ash-soft);
  }}
  .drawer-foot {{
    padding-top: 16px; display: flex; flex-direction: column; gap: 14px;
  }}

  /* ---------------- HERO SECTION (EDITORIAL DARK COVER) ---------------- */
  .hero {{
    background: var(--ash);
    color: var(--ivory);
    padding: 52px 0 60px;
    position: relative;
    overflow: hidden;
  }}
  .hero-grid {{
    display: grid; grid-template-columns: 1fr; gap: 36px; align-items: center;
  }}
  .hero-kicker {{
    font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase;
    color: var(--champagne); margin-bottom: 16px;
  }}
  .hero-brand-stack {{
    display: flex; flex-direction: column; align-items: flex-start; gap: 16px; margin-bottom: 22px;
  }}
  .hero-mark {{ width: 54px; height: 54px; }}
  .hero-wm {{ height: clamp(40px, 11vw, 68px); width: auto; max-width: 100%; margin-left: -10px; }}
  .hero-quote {{
    font-family: var(--font-display); font-style: italic; font-weight: 400;
    font-size: clamp(26px, 5vw, 40px); line-height: 1.18; color: var(--champagne);
    margin-bottom: 14px;
  }}
  .hero-sub {{
    font-size: 14.5px; color: rgba(243, 240, 233, 0.78); max-width: 540px; margin-bottom: 28px;
  }}
  .hero-cta-row {{
    display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 28px;
  }}
  .btn-primary {{
    display: inline-flex; align-items: center; justify-content: center; gap: 8px;
    min-height: 46px; padding: 0 24px; border-radius: 999px;
    background: var(--ivory); color: var(--ash);
    font-size: 12px; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase;
    transition: transform 0.15s, background 0.15s;
  }}
  .btn-primary:hover {{ background: #FFFFFF; }}
  .btn-outline-light {{
    display: inline-flex; align-items: center; justify-content: center; gap: 8px;
    min-height: 46px; padding: 0 22px; border-radius: 999px;
    border: 1px solid var(--line-dark); color: var(--ivory);
    font-size: 12px; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase;
    transition: border-color 0.15s, background 0.15s;
  }}
  .btn-outline-light:hover {{ border-color: var(--champagne); background: rgba(200,185,166,0.08); }}

  .hero-meta-bar {{
    display: grid; grid-template-columns: 1fr; gap: 14px;
    padding-top: 22px; border-top: 1px solid var(--line-dark);
  }}
  .meta-item small {{
    display: block; font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;
    color: rgba(243, 240, 233, 0.56); margin-bottom: 4px;
  }}
  .meta-item strong {{
    font-size: 13.5px; font-weight: 500; color: var(--ivory);
  }}

  .hero-preview-frame {{
    background: rgba(243, 240, 233, 0.05);
    border: 1px solid var(--line-dark);
    border-radius: var(--radius-md);
    padding: 14px;
  }}
  .hero-preview-frame img {{
    width: 100%; height: auto; border-radius: 10px;
  }}
  .hero-preview-cap {{
    display: flex; justify-content: space-between; align-items: center; gap: 10px;
    margin-top: 10px; font-size: 11px; color: rgba(243,240,233,0.68);
  }}

  /* ---------------- SHARED SECTION RHYTHM ---------------- */
  .section {{
    padding: 56px 0;
    border-bottom: 1px solid var(--line);
  }}
  .section-alt {{ background: var(--ivory-card); }}
  .section-head {{
    display: grid; grid-template-columns: 1fr; gap: 14px; margin-bottom: 32px;
  }}
  .sec-num {{
    font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--champagne-deep);
    margin-bottom: 8px;
  }}
  .sec-h2 {{
    font-family: var(--font-display); font-weight: 500;
    font-size: clamp(30px, 5vw, 46px); line-height: 1.08;
  }}
  .sec-h2 em {{ font-style: italic; font-weight: 400; }}
  .sec-desc {{ font-size: 14.5px; color: var(--ash-soft); max-width: 600px; }}

  /* ---------------- 01. STRATEGY & PHILOSOPHY ---------------- */
  .strategy-grid {{
    display: grid; grid-template-columns: 1fr; gap: 20px;
  }}
  .editorial-panel {{
    background: var(--ivory-card); border: 1px solid var(--line); border-radius: var(--radius-md);
    padding: 24px;
  }}
  .section-alt .editorial-panel {{ background: var(--ivory); }}
  .panel-label {{
    font-size: 10.5px; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--ash-soft); margin-bottom: 12px;
  }}
  .pillar-list {{ list-style: none; display: grid; gap: 10px; margin-top: 12px; }}
  .pillar-list li {{
    padding-left: 16px; position: relative; font-size: 14px; color: var(--ash-soft);
  }}
  .pillar-list li::before {{
    content: ''; position: absolute; left: 0; top: 10px; width: 6px; height: 1px; background: var(--champagne-deep);
  }}
  .pillar-list li b {{ color: var(--ash); font-weight: 500; }}
  .personality-tags {{
    display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px;
  }}
  .tag-soft {{
    font-size: 12px; padding: 6px 12px; border-radius: 6px;
    background: var(--ivory); border: 1px solid var(--line); color: var(--ash);
  }}

  /* ---------------- 02. INTERACTIVE LOGO PLAYGROUND & ARCHITECTURE ---------------- */
  .playground {{
    border: 1px solid var(--line); border-radius: var(--radius-md);
    overflow: hidden; margin-bottom: 28px;
  }}
  .pg-stage {{
    min-height: 220px; padding: 40px 24px;
    display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 18px;
    transition: background-color 0.25s ease;
    background: var(--ivory);
  }}
  .pg-svg {{ height: clamp(44px, 9vw, 76px); width: auto; }}
  .pg-caption {{ font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; opacity: 0.72; text-align: center; }}
  .pg-controls {{
    background: var(--white); border-top: 1px solid var(--line);
    padding: 14px 16px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px;
  }}
  .pg-swatches {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .surface-btn {{
    display: inline-flex; align-items: center; gap: 8px;
    min-height: 44px; padding: 0 14px; border-radius: 8px;
    border: 1px solid var(--line); font-size: 12px; font-weight: 500;
    background: var(--ivory-card); transition: border-color 0.15s;
  }}
  .surface-btn.active {{ border-color: var(--ash); background: var(--ivory); box-shadow: inset 0 0 0 1px var(--ash); }}
  .sw-chip {{ width: 14px; height: 14px; border-radius: 50%; border: 1px solid rgba(52,51,47,0.22); flex-shrink: 0; }}

  .arch-grid {{
    display: grid; grid-template-columns: 1fr; gap: 16px; margin-bottom: 24px;
  }}
  .arch-card {{
    background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md);
    padding: 24px 20px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 18px;
    min-width: 0;
  }}
  .arch-card.dark {{ background: var(--ash); border-color: var(--ash); color: var(--ivory); }}
  .arch-stage {{
    min-height: 108px; display: flex; align-items: center; justify-content: center;
  }}
  .arch-svg {{ max-height: 54px; width: auto; }}
  .arch-svg-sq {{ width: 78px; height: 78px; }}
  .arch-svg-tall {{ max-height: 92px; width: auto; }}
  .arch-svg-sm {{ max-height: 36px; width: auto; }}
  .arch-meta {{
    display: flex; justify-content: space-between; align-items: flex-end; gap: 10px;
    padding-top: 12px; border-top: 1px solid var(--line);
  }}
  .arch-card.dark .arch-meta {{ border-color: var(--line-dark); }}
  .arch-meta strong {{ display: block; font-size: 13px; font-weight: 500; }}
  .arch-meta span {{ font-size: 11.5px; color: var(--ash-soft); }}
  .arch-card.dark .arch-meta span {{ color: rgba(243,240,233,0.68); }}
  .dl-link {{
    font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; font-weight: 500;
    padding: 8px 12px; border-radius: 6px; border: 1px solid var(--line);
    min-height: 36px; display: inline-flex; align-items: center; white-space: nowrap;
  }}
  .arch-card.dark .dl-link {{ border-color: var(--line-dark); color: var(--champagne); }}
  .dl-link:hover {{ background: rgba(52,51,47,0.06); }}

  /* Clear space & Min size table */
  .gov-grid {{ display: grid; grid-template-columns: 1fr; gap: 20px; }}
  .table-scroll {{ width: 100%; max-width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; }}
  table.spec-table {{ width: 100%; min-width: 440px; border-collapse: collapse; font-size: 13px; }}
  table.spec-table th {{
    text-align: left; font-size: 10.5px; letter-spacing: 0.14em; text-transform: uppercase;
    color: var(--ash-soft); padding: 10px 10px; border-bottom: 1px solid var(--ash);
  }}
  table.spec-table td {{ padding: 10px 10px; border-bottom: 1px solid var(--line); }}

  /* ---------------- 03. COLOR SYSTEM (CLICK TO COPY) ---------------- */
  .prop-bar {{
    display: flex; height: 40px; border-radius: var(--radius-sm); overflow: hidden;
    border: 1px solid var(--line); margin-bottom: 24px; font-size: 11px; font-weight: 500;
  }}
  .prop-seg {{ display: flex; align-items: center; justify-content: center; overflow: hidden; white-space: nowrap; }}
  .color-grid {{ display: grid; grid-template-columns: 1fr; gap: 14px; margin-bottom: 24px; }}
  .swatch-btn {{
    text-align: left; width: 100%; background: var(--white);
    border: 1px solid var(--line); border-radius: var(--radius-md); overflow: hidden;
    transition: transform 0.15s, border-color 0.15s;
  }}
  .swatch-btn:hover {{ border-color: var(--ash); transform: translateY(-2px); }}
  .swatch-head {{
    height: 96px; padding: 14px; display: flex; justify-content: space-between; align-items: flex-end;
    font-size: 10.5px; letter-spacing: 0.12em; text-transform: uppercase; font-weight: 500;
  }}
  .swatch-body {{ padding: 14px 16px; }}
  .swatch-body strong {{ display: block; font-size: 14.5px; margin-bottom: 4px; }}
  .swatch-code {{
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 11.5px;
    color: var(--ash-soft); display: block; line-height: 1.5;
  }}
  .copy-hint {{ font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase; opacity: 0.7; }}

  /* ---------------- 04. TYPOGRAPHY & GRAPHIC LANGUAGE ---------------- */
  .type-stack {{ display: grid; grid-template-columns: 1fr; gap: 14px; margin-bottom: 28px; }}
  .type-item {{
    background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md);
    padding: 20px 22px; display: grid; grid-template-columns: 1fr; gap: 12px; align-items: center;
  }}
  .type-role small {{
    display: block; font-size: 10.5px; letter-spacing: 0.16em; text-transform: uppercase;
    color: var(--champagne-deep); margin-bottom: 3px;
  }}
  .type-role span {{ font-size: 12px; color: var(--ash-soft); }}

  .gfx-grid {{ display: grid; grid-template-columns: 1fr; gap: 16px; }}
  .gfx-card {{
    background: var(--ivory); border: 1px solid var(--line); border-radius: var(--radius-md);
    padding: 22px 18px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 14px;
  }}
  .gfx-stage {{ height: 132px; width: 100%; display: flex; align-items: center; justify-content: center; }}
  .gfx-divider {{ width: 100%; max-width: 320px; height: auto; }}
  .gfx-sq {{ width: 124px; height: 124px; }}
  .gfx-sq-rad {{ width: 124px; height: 124px; border-radius: 8px; border: 1px solid var(--line); }}
  .gfx-wide {{ width: 100%; height: 124px; object-fit: cover; border-radius: 8px; border: 1px solid var(--line); }}
  .gfx-card h3 {{ font-size: 13.5px; font-weight: 500; }}
  .gfx-card p {{ font-size: 12px; color: var(--ash-soft); }}

  /* ---------------- 05. PACKAGING & APPLICATIONS (BOARD GALLERY + LIGHTBOX) ---------------- */
  .sku-cards {{ display: grid; grid-template-columns: 1fr; gap: 12px; margin-bottom: 24px; }}
  .sku-item {{
    background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md);
    padding: 18px; display: flex; align-items: center; gap: 14px;
  }}
  .sku-dot {{
    width: 44px; height: 44px; border-radius: 50%; flex-shrink: 0;
    border: 1px solid rgba(52,51,47,0.12); display: flex; align-items: center; justify-content: center;
    font-family: var(--font-display); font-size: 17px; font-weight: 600;
  }}
  .sku-item strong {{ display: block; font-size: 14.5px; }}
  .sku-item span {{ font-size: 12px; color: var(--ash-soft); }}

  .board-feature {{
    background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md);
    overflow: hidden; margin-bottom: 20px;
  }}
  .board-trigger {{
    display: block; width: 100%; text-align: left; padding: 0; position: relative;
  }}
  .board-trigger img {{ width: 100%; height: auto; display: block; }}
  .board-bar {{
    padding: 14px 18px; border-top: 1px solid var(--line);
    display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 10px;
    background: var(--ivory-card);
  }}
  .board-bar strong {{ font-size: 13.5px; font-weight: 500; }}
  .board-bar span {{ font-size: 12px; color: var(--ash-soft); }}
  .zoom-pill {{
    font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; font-weight: 500;
    padding: 8px 14px; border-radius: 999px; border: 1px solid var(--line);
    background: var(--white); min-height: 38px; display: inline-flex; align-items: center;
  }}

  /* Owner NANA Stationery Spotlight */
  .owner-spot {{
    display: grid; grid-template-columns: 1fr; gap: 18px; margin-bottom: 24px;
  }}
  .bcard-live {{
    border-radius: 10px; padding: 24px; min-height: 190px;
    display: flex; flex-direction: column; justify-content: space-between;
    box-shadow: 0 12px 24px rgba(52,51,47,0.08);
  }}
  .bcard-live.ivory {{ background: var(--ivory); border: 1px solid var(--line); }}
  .bcard-live.ash {{ background: var(--ash); color: var(--ivory); align-items: center; justify-content: center; gap: 12px; text-align: center; }}

  /* Full Visual Boards Archive Grid */
  .boards-grid {{ display: grid; grid-template-columns: 1fr; gap: 18px; }}
  .board-thumb {{
    background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md);
    overflow: hidden; display: flex; flex-direction: column;
  }}
  .board-thumb-img {{
    aspect-ratio: 16 / 11; overflow: hidden; background: var(--ivory);
    border-bottom: 1px solid var(--line);
  }}
  .board-thumb-img img {{
    width: 100%; height: 100%; object-fit: cover; object-position: top center;
    transition: transform 0.3s ease;
  }}
  .board-thumb:hover .board-thumb-img img {{ transform: scale(1.02); }}
  .board-thumb-meta {{
    padding: 16px 18px; display: flex; justify-content: space-between; align-items: center; gap: 12px;
  }}
  .board-thumb-meta strong {{ display: block; font-size: 13.5px; font-weight: 500; }}
  .board-thumb-meta span {{ font-size: 11.5px; color: var(--ash-soft); }}

  /* Downloads & Handover Bar */
  .dl-grid {{ display: grid; grid-template-columns: 1fr; gap: 14px; }}
  .dl-card {{
    background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md);
    padding: 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 14px;
  }}
  .dl-card strong {{ font-size: 15px; display: block; margin-bottom: 4px; }}
  .dl-card p {{ font-size: 12.5px; color: var(--ash-soft); }}
  .dl-btn-row {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .btn-dark-sm {{
    display: inline-flex; align-items: center; justify-content: center;
    min-height: 44px; padding: 0 18px; border-radius: 999px;
    background: var(--ash); color: var(--ivory);
    font-size: 11.5px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase;
  }}
  .btn-light-sm {{
    display: inline-flex; align-items: center; justify-content: center;
    min-height: 44px; padding: 0 16px; border-radius: 999px;
    border: 1px solid var(--line); background: var(--ivory-card); color: var(--ash);
    font-size: 11.5px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase;
  }}

  /* ---------------- FOOTER (BY KALLA COLOPHON) ---------------- */
  .footer {{
    background: var(--ash); color: var(--ivory);
    padding: 52px 0 40px;
  }}
  .footer-top {{
    display: grid; grid-template-columns: 1fr; gap: 28px;
    padding-bottom: 32px; border-bottom: 1px solid var(--line-dark);
  }}
  .footer-quote {{
    font-family: var(--font-display); font-style: italic; font-size: 24px; color: var(--champagne);
    margin-top: 12px;
  }}
  .footer-col h4 {{
    font-size: 10.5px; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--champagne); margin-bottom: 12px;
  }}
  .footer-col p, .footer-col a {{
    font-size: 13px; color: rgba(243,240,233,0.74); line-height: 1.8; display: block;
  }}
  .footer-col a:hover {{ color: var(--ivory); }}
  .footer-bot {{
    padding-top: 24px; display: flex; flex-direction: column; gap: 16px;
    align-items: flex-start; justify-content: space-between;
    font-size: 12px; color: rgba(243,240,233,0.62);
  }}
  .kalla-badge {{
    display: inline-flex; align-items: center; gap: 10px;
    padding: 10px 16px; border-radius: 999px;
    border: 1px solid var(--line-dark); background: rgba(243,240,233,0.04);
  }}

  /* ---------------- LIGHTBOX MODAL ---------------- */
  .lightbox {{
    display: none; position: fixed; inset: 0; z-index: 100;
    background: rgba(28, 27, 24, 0.94);
    padding: 16px; flex-direction: column; align-items: center; justify-content: center; gap: 14px;
  }}
  .lightbox.open {{ display: flex; }}
  .lb-bar {{
    width: 100%; max-width: 1280px; display: flex; justify-content: space-between; align-items: center; gap: 12px;
    color: var(--ivory);
  }}
  .lb-title {{ font-size: 13px; letter-spacing: 0.08em; }}
  .lb-close {{
    min-width: 44px; min-height: 44px; padding: 0 18px; border-radius: 999px;
    border: 1px solid var(--line-dark); color: var(--ivory);
    font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase;
  }}
  .lb-img-wrap {{
    max-width: 1280px; max-height: calc(100dvh - 104px); overflow: auto;
    border-radius: 10px; background: var(--ivory);
  }}
  .lb-img-wrap img {{ width: auto; max-width: 100%; height: auto; max-height: calc(100dvh - 108px); object-fit: contain; }}

  /* Toast notification for Copy HEX */
  .toast {{
    position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%) translateY(16px);
    background: var(--ash); color: var(--ivory); border: 1px solid var(--line-dark);
    padding: 10px 18px; border-radius: 999px; font-size: 12.5px; letter-spacing: 0.06em;
    opacity: 0; pointer-events: none; transition: opacity 0.2s, transform 0.2s; z-index: 90;
  }}
  .toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}

  /* ---------------- TABLET BREAKPOINT (>= 640px) ---------------- */
  @media (min-width: 640px) {{
    .wrap {{ padding: 0 32px; }}
    .nav-sep, .nav-kalla {{ display: flex; }}
    .hero-meta-bar {{ grid-template-columns: repeat(3, 1fr); }}
    .strategy-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .arch-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .color-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .gfx-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .sku-cards {{ grid-template-columns: repeat(2, 1fr); }}
    .owner-spot {{ grid-template-columns: repeat(2, 1fr); }}
    .boards-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .dl-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .type-item {{ grid-template-columns: 200px 1fr; }}
    .footer-top {{ grid-template-columns: 1.4fr 1fr 1fr; }}
    .footer-bot {{ flex-direction: row; align-items: center; }}
  }}

  /* ---------------- DESKTOP BREAKPOINT (>= 1024px) ---------------- */
  @media (min-width: 1024px) {{
    :root {{ --nav-h: 68px; }}
    .wrap {{ padding: 0 40px; }}
    .nav-links {{ display: flex; }}
    .btn-pdf-sm {{ display: inline-flex; }}
    .menu-toggle {{ display: none; }}
    .hero {{ padding: 80px 0 88px; }}
    .hero-grid {{ grid-template-columns: 1.08fr 0.92fr; gap: 52px; }}
    .section {{ padding: 88px 0; }}
    .section-head {{ grid-template-columns: 1fr 1fr; align-items: end; gap: 36px; margin-bottom: 44px; }}
    .strategy-grid {{ grid-template-columns: 1.2fr 1fr 1fr; }}
    .arch-grid {{ grid-template-columns: repeat(4, 1fr); }}
    .gov-grid {{ grid-template-columns: 0.95fr 1.25fr; align-items: start; }}
    .color-grid {{ grid-template-columns: repeat(4, 1fr); }}
    .color-grid.sku-3 {{ grid-template-columns: repeat(3, 1fr); }}
    .gfx-grid {{ grid-template-columns: repeat(4, 1fr); }}
    .sku-cards {{ grid-template-columns: repeat(5, 1fr); }}
    .sku-item {{ flex-direction: column; text-align: center; padding: 20px 14px; }}
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

  <!-- MOBILE NAVIGATION DRAWER -->
  <div class="mobile-drawer" id="mobileDrawer" aria-hidden="true">
    <nav class="drawer-nav" aria-label="Navigasi Mobile">
      <a href="#strategy">Brand Strategy <span class="num">01</span></a>
      <a href="#logo-system">Logo Architecture <span class="num">02</span></a>
      <a href="#color-type">Color &amp; Typography <span class="num">03</span></a>
      <a href="#packaging">5-SKU Packaging <span class="num">04</span></a>
      <a href="#applications">Brand Applications <span class="num">05</span></a>
      <a href="#boards">Visual Boards &amp; PDF <span class="num">06</span></a>
    </nav>
    <div class="drawer-foot">
      <a href="10-brand-guidelines/selunea-brand-guidelines.pdf" target="_blank" class="btn-dark-sm" style="width:100%;">Open Brand Guidelines PDF</a>
      <div style="display:flex;justify-content:space-between;align-items:center;padding-top:6px;">
        <span style="font-size:11.5px;color:var(--ash-soft);">Presented for <b>NANA</b></span>
        {kalla_light}
      </div>
    </div>
  </div>

  <!-- HERO COVER -->
  <section class="hero dark-surface" id="top">
    <div class="wrap hero-grid">
      <div>
        <div class="hero-kicker">Complete Brand Identity Presentation · Lunar Elegance</div>
        <div class="hero-brand-stack">
          {mark_hero}
          {wm_hero}
        </div>
        <p class="hero-quote">“Beauty in Every Phase.”</p>
        <p class="hero-sub">
          Identitas visual lengkap untuk <strong>SELUNÉA</strong> — brand skincare <em>affordable premium</em> bagi perempuan usia 20–35 tahun. Memadukan tipografi <em>high-contrast editorial sans</em> yang anggun dengan geometri fase lunar abstrak yang tenang dan timeless.
        </p>
        <div class="hero-cta-row">
          <a href="#logo-system" class="btn-primary">Explore Identity</a>
          <a href="10-brand-guidelines/selunea-brand-guidelines.pdf" target="_blank" class="btn-outline-light">Open Brand Book PDF</a>
        </div>
        <div class="hero-meta-bar">
          <div class="meta-item">
            <small>Founder &amp; Owner</small>
            <strong>NANA</strong>
          </div>
          <div class="meta-item">
            <small>Tagline</small>
            <strong>Skincare for every version of you.</strong>
          </div>
          <div class="meta-item">
            <small>Identity &amp; Direction</small>
            <div style="margin-top:2px;">{kalla_hero}</div>
          </div>
        </div>
      </div>

      <div class="hero-preview-frame">
        <button type="button" class="board-trigger" data-lightbox="08-packaging/01-skincare-packaging-family.png" data-caption="SELUNÉA — Complete 5-SKU Skincare Packaging Architecture">
          <img src="08-packaging/01-skincare-packaging-family.png" alt="SELUNÉA 5-SKU Skincare Packaging Family" fetchpriority="high" width="1600" height="1260" />
        </button>
        <div class="hero-preview-cap">
          <span>5-SKU Packaging Family · Matte Ivory &amp; Frosted Glass</span>
          <span>Tap to zoom</span>
        </div>
      </div>
    </div>
  </section>

  <!-- 01 · BRAND STRATEGY & PHILOSOPHY -->
  <section class="section" id="strategy">
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
            <span class="tag-soft">Refined</span>
            <span class="tag-soft">Feminine</span>
            <span class="tag-soft">Calm</span>
            <span class="tag-soft">Confident</span>
            <span class="tag-soft">Sophisticated</span>
            <span class="tag-soft">Approachable</span>
            <span class="tag-soft">Timeless</span>
          </div>
        </div>

        <div class="editorial-panel">
          <div class="panel-label">Visual Principles (Embrace)</div>
          <ul class="pillar-list">
            <li><b>Modern Feminine Minimalism:</b> Ruang napas lega dan hierarki tenang.</li>
            <li><b>Couture High-Contrast Type:</b> Tipografi sans-editorial tajam dengan lengkung lunar halus pada <em>L–U</em> dan aksen <em>É</em>.</li>
            <li><b>Subtle Lunar Geometry:</b> Ekspresi fase bulan lewat <em>negative space</em> &amp; cahaya.</li>
            <li><b>Tactile Packaging:</b> Matte Moon Ivory, kaca frosted, aksen satin Champagne &amp; Lunar Silver.</li>
          </ul>
        </div>

        <div class="editorial-panel">
          <div class="panel-label">Category Guardrails (Avoid)</div>
          <ul class="pillar-list">
            <li><b>Nol Klise Bulan Sabit &amp; Bintang:</b> Bukan visual tarot atau astrologi.</li>
            <li><b>Nol Gradasi Ungu / Dekorasi Emas Ramai:</b> Tetap netral mineral dan kontemporer.</li>
            <li><b>Nol Klaim Palsu:</b> Tidak mengarang persentase bahan aktif, SPF, atau sertifikasi.</li>
            <li><b>Nol Font Mentah:</b> Seluruh master logo adalah <em>outlined vector paths</em> murni.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- 02 · LOGO SYSTEM & INTERACTIVE SURFACE PLAYGROUND -->
  <section class="section section-alt" id="logo-system">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">02 · Logo Architecture</div>
          <h2 class="sec-h2">Bespoke Wordmark &amp; <em>Lunar Marks</em></h2>
        </div>
        <p class="sec-desc">
          Wordmark <em>high-contrast serif-less</em> SELUNÉA dengan lengkung <strong>L→U</strong> (menyorot akar kata <em>LUNA</em>) dan aksen cahaya 30° pada <strong>É</strong>, dipadukan dengan Tri-Phase Lunar Brand Mark (skor audit 100/100) serta Celestial S Monogram khusus tutup botol.
        </p>
      </div>

      <!-- Interactive Surface Playground -->
      <div class="playground" aria-label="Interactive Logo Surface Preview">
        <div class="pg-stage" id="pgStage">
          <div id="pgLogoDark">{wm_ash}</div>
          <div id="pgLogoLight" style="display:none;">{wm_white}</div>
          <div id="pgLogoChamp" style="display:none;">{wm_champ}</div>
          <div class="pg-caption" id="pgCaption">Midnight Ash (#34332F) on Moon Ivory (#F3F0E9) · Contrast 11.11:1 (AAA)</div>
        </div>
        <div class="pg-controls">
          <span style="font-size:11.5px;letter-spacing:0.12em;text-transform:uppercase;color:var(--ash-soft);">Test Surface:</span>
          <div class="pg-swatches" role="group" aria-label="Pilih warna latar logo">
            <button type="button" class="surface-btn active" data-bg="#F3F0E9" data-mode="dark" data-cap="Midnight Ash (#34332F) on Moon Ivory (#F3F0E9) · Contrast 11.11:1 (AAA)">
              <span class="sw-chip" style="background:#F3F0E9;"></span>Moon Ivory
            </button>
            <button type="button" class="surface-btn" data-bg="#34332F" data-mode="light" data-cap="Irradiation-Thinned White (#FFFFFF) on Midnight Ash (#34332F) · Contrast 12.65:1 (AAA)">
              <span class="sw-chip" style="background:#34332F;"></span>Midnight Ash
            </button>
            <button type="button" class="surface-btn" data-bg="#34332F" data-mode="champ" data-cap="Champagne Beige (#C8B9A6) Foil on Midnight Ash (#34332F) · Contrast 6.59:1 (AA+)">
              <span class="sw-chip" style="background:#C8B9A6;"></span>Champagne Foil
            </button>
            <button type="button" class="surface-btn" data-bg="#D9DFD5" data-mode="dark" data-cap="Midnight Ash on Sage Haze (#D9DFD5 · Cleanser) · Contrast 9.31:1 (AAA)">
              <span class="sw-chip" style="background:#D9DFD5;"></span>Sage Haze
            </button>
            <button type="button" class="surface-btn" data-bg="#DCD9E2" data-mode="dark" data-cap="Midnight Ash on Lavender Mist (#DCD9E2 · Toner/Serum) · Contrast 9.07:1 (AAA)">
              <span class="sw-chip" style="background:#DCD9E2;"></span>Lavender Mist
            </button>
            <button type="button" class="surface-btn" data-bg="#E4DAD0" data-mode="dark" data-cap="Midnight Ash on Soft Nude (#E4DAD0 · Moisturizer/SPF) · Contrast 9.18:1 (AAA)">
              <span class="sw-chip" style="background:#E4DAD0;"></span>Soft Nude
            </button>
          </div>
        </div>
      </div>

      <!-- 8 Official Logo Variants -->
      <div class="arch-grid">
        <div class="arch-card">
          <div class="arch-stage">{wm_ash_sm}</div>
          <div class="arch-meta">
            <div><strong>Primary Wordmark</strong><span>Midnight Ash · Bottles &amp; Web</span></div>
            <a href="05-logo-final/svg/selunea-primary-wordmark-midnight-ash.svg" download class="dl-link">SVG</a>
          </div>
        </div>
        <div class="arch-card">
          <div class="arch-stage">{sec_ash}</div>
          <div class="arch-meta">
            <div><strong>Secondary Logo</strong><span>With Outlined Skincare Sub-line</span></div>
            <a href="05-logo-final/svg/selunea-secondary-skincare-midnight-ash.svg" download class="dl-link">SVG</a>
          </div>
        </div>
        <div class="arch-card">
          <div class="arch-stage">{mark_ash}</div>
          <div class="arch-meta">
            <div><strong>Brand Mark</strong><span>Tri-Phase Lunar · 100/100</span></div>
            <a href="05-logo-final/svg/selunea-brand-mark-midnight-ash.svg" download class="dl-link">SVG</a>
          </div>
        </div>
        <div class="arch-card">
          <div class="arch-stage">{mono_ash}</div>
          <div class="arch-meta">
            <div><strong>Celestial S Monogram</strong><span>Caps, Jar Lids &amp; Seals · 100/100</span></div>
            <a href="05-logo-final/svg/selunea-monogram-s-midnight-ash.svg" download class="dl-link">SVG</a>
          </div>
        </div>
        <div class="arch-card">
          <div class="arch-stage">{horiz_ash}</div>
          <div class="arch-meta">
            <div><strong>Horizontal Lockup</strong><span>Headers, Cards &amp; Signage</span></div>
            <a href="05-logo-final/svg/selunea-horizontal-lockup-midnight-ash.svg" download class="dl-link">SVG</a>
          </div>
        </div>
        <div class="arch-card">
          <div class="arch-stage">{stacked_ash}</div>
          <div class="arch-meta">
            <div><strong>Stacked Lockup</strong><span>Folding Cartons &amp; Bags</span></div>
            <a href="05-logo-final/svg/selunea-stacked-lockup-midnight-ash.svg" download class="dl-link">SVG</a>
          </div>
        </div>
        <div class="arch-card dark dark-surface">
          <div class="arch-stage">{wm_white_arch}</div>
          <div class="arch-meta">
            <div><strong>Reversed White</strong><span>Irradiation-Thinned (~4%)</span></div>
            <a href="05-logo-final/svg/selunea-primary-wordmark-white-reversed.svg" download class="dl-link">SVG</a>
          </div>
        </div>
        <div class="arch-card">
          <div class="arch-stage">{wm_small}</div>
          <div class="arch-meta">
            <div><strong>Small-Size Cut</strong><span>Reinforced for 30 mL / &lt;18 mm</span></div>
            <a href="05-logo-final/svg/selunea-wordmark-small-responsive.svg" download class="dl-link">SVG</a>
          </div>
        </div>
      </div>

      <!-- Clear Space & Minimum Sizes -->
      <div class="gov-grid">
        <div class="editorial-panel" style="text-align:center;">
          <div class="panel-label" style="text-align:left;">Clear Space &amp; Protection Rule</div>
          <div style="display:inline-block;border:1.5px dashed var(--champagne-deep);border-radius:10px;padding:24px 32px;background:var(--white);margin:10px 0;">
            {load_svg(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:36px;width:auto;")}
          </div>
          <p style="font-size:12.5px;color:var(--ash-soft);margin-top:8px;">
            Ruang aman minimum <strong>0.5x</strong> atas/bawah dan <strong>0.75x</strong> kiri/kanan (<em>x = tinggi huruf E</em>). Jangan pernah meregangkan, memberi bayangan, atau mengetik ulang dengan font stok tanpa aksen <strong>É</strong>.
          </p>
        </div>
        <div class="editorial-panel">
          <div class="panel-label">Minimum Reproduction Sizes</div>
          <div class="table-scroll">
            <table class="spec-table">
              <thead>
                <tr><th>Varian Logo</th><th>Cetak Min.</th><th>Digital Min.</th><th>Penggunaan Utama</th></tr>
              </thead>
              <tbody>
                <tr><td><b>Primary Wordmark</b></td><td>24 mm</td><td>110 px</td><td>Botol utama, karton, website</td></tr>
                <tr><td><b>Small Responsive Cut</b></td><td>15 mm</td><td>72 px</td><td>Serum 30 mL, jar 50 mL, mobile</td></tr>
                <tr><td><b>Horizontal Lockup</b></td><td>32 mm</td><td>140 px</td><td>Kartu nama, header desktop</td></tr>
                <tr><td><b>Lunar Brand Mark</b></td><td>7 mm</td><td>16 px</td><td>Favicon, avatar sosial, stempel</td></tr>
                <tr><td><b>Celestial S Monogram</b></td><td>9 mm</td><td>24 px</td><td>Tutup botol 12–14 mm, segel foil</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 03 · COLOR SYSTEM, TYPOGRAPHY & GRAPHIC LANGUAGE -->
  <section class="section" id="color-type">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">03 · Color, Typography &amp; Graphic System</div>
          <h2 class="sec-h2">Mineral Palette &amp; <em>Editorial Voice</em></h2>
        </div>
        <p class="sec-desc">
          Hierarki proporsi <strong>60 / 25 / 10 / 5</strong> menjaga visual tetap tenang dan kontras AAA. Ketuk salah satu swatch warna di bawah untuk menyalin kode HEX langsung ke clipboard.
        </p>
      </div>

      <!-- Proportion Scale -->
      <div class="prop-bar" aria-label="Proporsi warna brand">
        <div class="prop-seg" style="width:58%;background:#F3F0E9;color:#34332F;">58% Moon Ivory</div>
        <div class="prop-seg" style="width:24%;background:#34332F;color:#F3F0E9;">24% Ash</div>
        <div class="prop-seg" style="width:12%;background:#C8B9A6;color:#34332F;">12%</div>
        <div class="prop-seg" style="width:6%;background:#B8B7B1;color:#34332F;">6%</div>
      </div>

      <!-- Primary & Secondary Swatches -->
      <div class="color-grid">
        <button type="button" class="swatch-btn" data-copy="#F3F0E9">
          <div class="swatch-head" style="background:#F3F0E9;color:#34332F;"><span>Primary Canvas</span><span class="copy-hint">Copy</span></div>
          <div class="swatch-body">
            <strong>Moon Ivory</strong>
            <span class="swatch-code">#F3F0E9 · RGB 243 240 233</span>
            <span class="swatch-code">CMYK 0 1 4 5 · 11.11:1 vs Ash</span>
          </div>
        </button>
        <button type="button" class="swatch-btn" data-copy="#34332F">
          <div class="swatch-head" style="background:#34332F;color:#F3F0E9;"><span>Primary Ink</span><span class="copy-hint">Copy</span></div>
          <div class="swatch-body">
            <strong>Midnight Ash</strong>
            <span class="swatch-code">#34332F · RGB 52 51 47</span>
            <span class="swatch-code">CMYK 0 2 10 80 · Black 7 C</span>
          </div>
        </button>
        <button type="button" class="swatch-btn" data-copy="#C8B9A6">
          <div class="swatch-head" style="background:#C8B9A6;color:#34332F;"><span>Warm Accent</span><span class="copy-hint">Copy</span></div>
          <div class="swatch-body">
            <strong>Champagne Beige</strong>
            <span class="swatch-code">#C8B9A6 · RGB 200 185 166</span>
            <span class="swatch-code">Foil 872 C · 6.59:1 on Ash</span>
          </div>
        </button>
        <button type="button" class="swatch-btn" data-copy="#B8B7B1">
          <div class="swatch-head" style="background:#B8B7B1;color:#34332F;"><span>Cool Metallic</span><span class="copy-hint">Copy</span></div>
          <div class="swatch-body">
            <strong>Lunar Silver</strong>
            <span class="swatch-code">#B8B7B1 · RGB 184 183 177</span>
            <span class="swatch-code">Foil 877 C · 6.29:1 on Ash</span>
          </div>
        </button>
      </div>

      <!-- Supporting Category Accent Swatches -->
      <div class="panel-label" style="margin-bottom:12px;">Product Category Color System (AAA Contrast vs Midnight Ash)</div>
      <div class="color-grid sku-3" style="margin-bottom:36px;">
        <button type="button" class="swatch-btn" data-copy="#D9DFD5">
          <div class="swatch-head" style="background:#D9DFD5;color:#34332F;height:64px;"><span>Phase 01 · Cleanse</span><span class="copy-hint">Copy</span></div>
          <div class="swatch-body">
            <strong>Sage Haze · Facial Cleanser</strong>
            <span class="swatch-code">#D9DFD5 · CMYK 3 0 4 13 · 9.31:1 vs Ash</span>
          </div>
        </button>
        <button type="button" class="swatch-btn" data-copy="#DCD9E2">
          <div class="swatch-head" style="background:#DCD9E2;color:#34332F;height:64px;"><span>Phase 02–03 · Treat</span><span class="copy-hint">Copy</span></div>
          <div class="swatch-body">
            <strong>Lavender Mist · Toner &amp; Serum</strong>
            <span class="swatch-code">#DCD9E2 · CMYK 3 4 0 11 · 9.07:1 vs Ash</span>
          </div>
        </button>
        <button type="button" class="swatch-btn" data-copy="#E4DAD0">
          <div class="swatch-head" style="background:#E4DAD0;color:#34332F;height:64px;"><span>Phase 04–05 · Nourish &amp; Shield</span><span class="copy-hint">Copy</span></div>
          <div class="swatch-body">
            <strong>Soft Nude · Moisturizer &amp; Sunscreen</strong>
            <span class="swatch-code">#E4DAD0 · CMYK 0 4 9 11 · 9.18:1 vs Ash</span>
          </div>
        </button>
      </div>

      <!-- Typography Hierarchy -->
      <div class="panel-label" style="margin-bottom:12px;">Typography Hierarchy (SIL Open Font License · Max 2 Families)</div>
      <div class="type-stack">
        <div class="type-item">
          <div class="type-role"><small>Display &amp; Campaign</small><span>Cormorant Garamond · 400 / 500 / Italic</span></div>
          <div style="font-family:var(--font-display);font-size:clamp(28px,4.5vw,40px);line-height:1.12;">Beauty in <em>Every Phase.</em></div>
        </div>
        <div class="type-item">
          <div class="type-role"><small>Headings &amp; Sub-Copy</small><span>DM Sans Medium · 18–22 px</span></div>
          <div style="font-size:19px;font-weight:500;">Skincare for every version of you.</div>
        </div>
        <div class="type-item">
          <div class="type-role"><small>Body &amp; Digital Copy</small><span>DM Sans Regular · 14–16 px · 1.65 lh</span></div>
          <div style="font-size:14.5px;color:var(--ash-soft);">Ritual harian yang tenang, seimbang, dan dapat diandalkan di setiap fase perubahan kulit Anda.</div>
        </div>
        <div class="type-item">
          <div class="type-role"><small>Product Specs / Packaging</small><span>DM Sans Medium Uppercase · +0.18em</span></div>
          <div style="font-size:11.5px;font-weight:500;letter-spacing:0.18em;text-transform:uppercase;">PHASE 03 · DAILY SERUM · 30 ML / 1.0 FL. OZ.</div>
        </div>
      </div>

      <!-- Supporting Graphic Language -->
      <div class="panel-label" style="margin-bottom:12px;">Supporting Graphic Language (Master SVG Assets)</div>
      <div class="gfx-grid">
        <div class="gfx-card">
          <div class="gfx-stage">{divider_svg}</div>
          <div><h3>Five-Phase Horizon Divider</h3><p>Pemisah bab editorial pada karton, kartu insert, dan website.</p></div>
        </div>
        <div class="gfx-card">
          <div class="gfx-stage">{orbital_svg}</div>
          <div><h3>Concentric Orbital Frame</h3><p>Aksen orbit halus untuk membingkai foto botol kampanye.</p></div>
        </div>
        <div class="gfx-card">
          <div class="gfx-stage">{pattern_svg}</div>
          <div><h3>Seamless Phase Pattern</h3><p>Motif berulang untuk tissue paper, inner carton, dan blind emboss.</p></div>
        </div>
        <div class="gfx-card">
          <div class="gfx-stage">{pearl_svg}</div>
          <div><h3>Pearl Luminosity Surface</h3><p>Latar cahaya lembut bernuansa mutiara untuk kartu digital &amp; lookbook.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- 04 · PACKAGING IDENTITY (5 SKUs) -->
  <section class="section section-alt" id="packaging">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">04 · Skincare Packaging Identity</div>
          <h2 class="sec-h2">Five-Phase <em>Product Family</em></h2>
        </div>
        <p class="sec-desc">
          Sistem kemasan koheren untuk 5 lini inti SELUNÉA dengan penempatan logo seragam, hierarki nama produk jernih, kode warna kategori halus, dan segel monogram <strong>S</strong> pada tutup botol.
        </p>
      </div>

      <div class="sku-cards">
        <div class="sku-item">
          <div class="sku-dot" style="background:var(--sage);">01</div>
          <div><strong>Facial Cleanser</strong><span>Matte Ivory Tube · 120 mL</span></div>
        </div>
        <div class="sku-item">
          <div class="sku-dot" style="background:var(--lavender);">02</div>
          <div><strong>Balancing Toner</strong><span>Frosted Bottle · 150 mL</span></div>
        </div>
        <div class="sku-item">
          <div class="sku-dot" style="background:var(--lavender);">03</div>
          <div><strong>Daily Serum</strong><span>Frosted Dropper · 30 mL</span></div>
        </div>
        <div class="sku-item">
          <div class="sku-dot" style="background:var(--nude);">04</div>
          <div><strong>Moisturizer</strong><span>Frosted Glass Jar · 50 mL</span></div>
        </div>
        <div class="sku-item">
          <div class="sku-dot" style="background:var(--nude);">05</div>
          <div><strong>Daily Sunscreen</strong><span>Matte Oval Tube · 50 mL</span></div>
        </div>
      </div>

      <div class="board-feature">
        <button type="button" class="board-trigger" data-lightbox="08-packaging/01-skincare-packaging-family.png" data-caption="SELUNÉA — 5-SKU Skincare Packaging Family, Folding Cartons &amp; Cap Seals">
          <img src="08-packaging/01-skincare-packaging-family.png" alt="SELUNÉA Packaging Architecture" loading="lazy" width="1600" height="1260" />
        </button>
        <div class="board-bar">
          <div>
            <strong>5-SKU Packaging Lineup, Folding Cartons &amp; Blind-Deboss Cap Seals</strong>
            <span> · Matte Moon Ivory · Frosted Glass · Satin Champagne &amp; Lunar Silver</span>
          </div>
          <button type="button" class="zoom-pill" data-lightbox="08-packaging/01-skincare-packaging-family.png" data-caption="SELUNÉA — 5-SKU Skincare Packaging Family">Zoom Fullscreen</button>
        </div>
      </div>
    </div>
  </section>

  <!-- 05 · BRAND APPLICATIONS (STATIONERY FOR NANA, COLLATERAL, SOCIAL & DIGITAL) -->
  <section class="section" id="applications">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">05 · Brand Applications &amp; Art Direction</div>
          <h2 class="sec-h2">Print, Unboxing &amp; <em>Digital Presence</em></h2>
        </div>
        <p class="sec-desc">
          Penerapan identitas SELUNÉA yang konsisten mulai dari kartu nama resmi untuk <strong>NANA (Founder &amp; Owner)</strong>, pengalaman unboxing, hingga sistem konten Instagram dan e-commerce.
        </p>
      </div>

      <!-- Live Owner Business Card Preview -->
      <div class="owner-spot">
        <div class="bcard-live ivory">
          <div style="display:flex;justify-content:space-between;align-items:center;">{wm_card}{mark_card}</div>
          <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap;">
            <div>
              <div style="font-family:var(--font-display);font-size:26px;font-weight:600;letter-spacing:0.06em;line-height:1.1;">NANA</div>
              <div style="font-size:10.5px;letter-spacing:0.16em;text-transform:uppercase;color:var(--ash-soft);">Founder &amp; Owner</div>
            </div>
            <div style="text-align:right;font-size:11.5px;color:var(--ash-soft);line-height:1.55;">
              nana@selunea.com<br/>@selunea.skin · selunea.com
            </div>
          </div>
        </div>
        <div class="bcard-live ash dark-surface">
          {mark_card_ch}
          {wm_card_ch}
          <div style="font-family:var(--font-display);font-style:italic;font-size:16px;color:var(--champagne);">Beauty in Every Phase.</div>
        </div>
      </div>

      <div class="boards-grid" style="grid-template-columns:1fr;">
        <div class="board-feature" style="margin-bottom:0;">
          <button type="button" class="board-trigger" data-lightbox="09-brand-applications/01-stationery-and-collateral.png" data-caption="SELUNÉA — Stationery (NANA — Founder &amp; Owner), Shopping Bag, Tissue Paper &amp; Mailer Box">
            <img src="09-brand-applications/01-stationery-and-collateral.png" alt="SELUNÉA Stationery and Collateral" loading="lazy" width="1600" height="1200" />
          </button>
          <div class="board-bar">
            <div><strong>Stationery, Unboxing &amp; Brand Collateral</strong><span> · Business Card (NANA), Thank-You Card, Shopping Bag, Tissue &amp; Mailer Box</span></div>
            <button type="button" class="zoom-pill" data-lightbox="09-brand-applications/01-stationery-and-collateral.png" data-caption="SELUNÉA — Stationery &amp; Collateral">Zoom</button>
          </div>
        </div>

        <div class="board-feature" style="margin-bottom:0;">
          <button type="button" class="board-trigger" data-lightbox="09-brand-applications/02-social-and-digital.png" data-caption="SELUNÉA — Instagram Identity, E-Commerce Storefront &amp; Editorial Photography Art Direction">
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

  <!-- 06 · ALL VISUAL BOARDS GALLERY & PRODUCTION DOWNLOADS -->
  <section class="section section-alt" id="boards">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">06 · Complete Visual Archive &amp; Downloads</div>
          <h2 class="sec-h2">All Boards &amp; <em>Production Assets</em></h2>
        </div>
        <p class="sec-desc">
          Seluruh papan riset, eksplorasi konsep, presentasi klien, hingga Brand Guideline PDF 15 bab tersedia di satu tempat. Ketuk gambar untuk memperbesar.
        </p>
      </div>

      <div class="boards-grid" style="margin-bottom:36px;">
        <article class="board-thumb">
          <button type="button" class="board-thumb-img" data-lightbox="03-moodboard/01-lunar-elegance-moodboard.png" data-caption="Stage 02 — Lunar Elegance Visual Moodboard &amp; Typography Study">
            <img src="03-moodboard/01-lunar-elegance-moodboard.png" alt="Lunar Elegance Moodboard" loading="lazy" width="1600" height="1340" />
          </button>
          <div class="board-thumb-meta">
            <div><strong>01 · Moodboard &amp; Direction</strong><span>Materiality, WCAG &amp; Type Study</span></div>
            <button type="button" class="dl-link" data-lightbox="03-moodboard/01-lunar-elegance-moodboard.png" data-caption="Stage 02 — Moodboard">View</button>
          </div>
        </article>

        <article class="board-thumb">
          <button type="button" class="board-thumb-img" data-lightbox="04-logo-concepts/selunea-concepts-overview-v4.png" data-caption="Stage 03–04 — Three Logo Concepts Comparison (Owner Editorial-Sans Style)">
            <img src="04-logo-concepts/selunea-concepts-overview-v4.png" alt="Logo Concepts Comparison" loading="lazy" width="1440" height="900" />
          </button>
          <div class="board-thumb-meta">
            <div><strong>02 · Logo Concepts (A / B / C)</strong><span>Black-and-White Checkpoint + 16 px</span></div>
            <button type="button" class="dl-link" data-lightbox="04-logo-concepts/selunea-concepts-overview-v4.png" data-caption="Stage 03–04 — Logo Concepts">View</button>
          </div>
        </article>

        <article class="board-thumb">
          <button type="button" class="board-thumb-img" data-lightbox="06-color-typography/03-color-typography-board.png" data-caption="Stage 06 — Color System, Typography &amp; Graphic Language Spec Board">
            <img src="06-color-typography/03-color-typography-board.png" alt="Color and Typography Board" loading="lazy" width="1600" height="1180" />
          </button>
          <div class="board-thumb-meta">
            <div><strong>03 · Color &amp; Typography Spec</strong><span>Tokens, Contrast &amp; Graphic Assets</span></div>
            <button type="button" class="dl-link" data-lightbox="06-color-typography/03-color-typography-board.png" data-caption="Stage 06 — Color &amp; Typography Spec">View</button>
          </div>
        </article>

        <article class="board-thumb">
          <button type="button" class="board-thumb-img" data-lightbox="11-presentations/slides/slide-03.png" data-caption="Stage 08 — Client Presentation Final Logo Overview">
            <img src="11-presentations/slides/slide-03.png" alt="Client Presentation Logo Slide" loading="lazy" width="1440" height="900" />
          </button>
          <div class="board-thumb-meta">
            <div><strong>04 · Final Identity Slide</strong><span>Scale Ladder &amp; Champagne Reversed</span></div>
            <button type="button" class="dl-link" data-lightbox="11-presentations/slides/slide-03.png" data-caption="Final Identity Slide">View</button>
          </div>
        </article>

        <article class="board-thumb">
          <button type="button" class="board-thumb-img" data-lightbox="11-presentations/slides/slide-04.png" data-caption="Stage 08 — Real-World Retail &amp; Beauty Mockups (Featuring NANA)">
            <img src="11-presentations/slides/slide-04.png" alt="Real-World Retail Mockups" loading="lazy" width="1440" height="900" />
          </button>
          <div class="board-thumb-meta">
            <div><strong>05 · Brand Mockups Deck</strong><span>Bag, Box, Card (NANA), Web &amp; Tote</span></div>
            <button type="button" class="dl-link" data-lightbox="11-presentations/slides/slide-04.png" data-caption="Brand Mockups Deck">View</button>
          </div>
        </article>

        <article class="board-thumb">
          <button type="button" class="board-thumb-img" data-lightbox="10-brand-guidelines/brand-guidelines-preview-p1-p2.png" data-caption="Stage 08 — SELUNÉA 15-Section Brand Identity Guidelines (PDF Preview)">
            <img src="10-brand-guidelines/brand-guidelines-preview-p1-p2.png" alt="Brand Guidelines Cover Preview" loading="lazy" width="1200" height="1680" />
          </button>
          <div class="board-thumb-meta">
            <div><strong>06 · Brand Guidelines Manual</strong><span>15 Complete Chapters · A4 PDF</span></div>
            <button type="button" class="dl-link" data-lightbox="10-brand-guidelines/brand-guidelines-preview-p1-p2.png" data-caption="Brand Guidelines Preview">View</button>
          </div>
        </article>
      </div>

      <!-- Production Documents & Quick Open -->
      <div class="dl-grid">
        <div class="dl-card">
          <div>
            <strong>Brand Guidelines Document</strong>
            <p>Dokumen resmi 15 bab lengkap (Filosofi, Logo, Clear Space, Warna, Tipografi, Kemasan, Sosial Media) siap cetak &amp; presentasi.</p>
          </div>
          <div class="dl-btn-row">
            <a href="10-brand-guidelines/selunea-brand-guidelines.pdf" target="_blank" class="btn-dark-sm">Open PDF</a>
            <a href="10-brand-guidelines/selunea-brand-guidelines.html" target="_blank" class="btn-light-sm">HTML Version</a>
          </div>
        </div>
        <div class="dl-card">
          <div>
            <strong>Client Presentation &amp; Packaging PDF</strong>
            <p>Deck presentasi 5 slide beserta lembar arsitektur kemasan 5 SKU beresolusi vektor tajam.</p>
          </div>
          <div class="dl-btn-row">
            <a href="11-presentations/selunea-client-presentation.pdf" target="_blank" class="btn-dark-sm">Presentation PDF</a>
            <a href="08-packaging/01-skincare-packaging-family.pdf" target="_blank" class="btn-light-sm">Packaging PDF</a>
          </div>
        </div>
        <div class="dl-card">
          <div>
            <strong>Master Vector &amp; Web Icon Kit</strong>
            <p>Termasuk seluruh SVG master (audit 100/100), PNG transparan 1600 px, <code>favicon.ico</code>, app icon, dan design tokens JSON/CSS.</p>
          </div>
          <div class="dl-btn-row">
            <a href="05-logo-final/png/selunea-primary-wordmark-midnight-ash-1600.png" download class="btn-dark-sm">Primary PNG</a>
            <a href="06-color-typography/01-design-tokens.json" target="_blank" class="btn-light-sm">Tokens JSON</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER COLOPHON (BY KALLA) -->
  <footer class="footer dark-surface">
    <div class="wrap">
      <div class="footer-top">
        <div>
          {wm_footer}
          <div class="footer-quote">“Beauty in Every Phase.”</div>
          <p style="font-size:13px;color:rgba(243,240,233,0.68);margin-top:8px;max-width:340px;">
            Skincare for every version of you. Brand Identity System prepared exclusively for <strong>NANA</strong> (Founder &amp; Owner).
          </p>
        </div>
        <div class="footer-col">
          <h4>Sections</h4>
          <a href="#strategy">Brand Strategy</a>
          <a href="#logo-system">Logo Architecture</a>
          <a href="#color-type">Color &amp; Typography</a>
          <a href="#packaging">5-SKU Packaging</a>
          <a href="#applications">Applications &amp; Social</a>
        </div>
        <div class="footer-col">
          <h4>Production Notes</h4>
          <p>Silakan lakukan pencarian merek dagang resmi (Kelas 3 Kosmetik) serta proofing fisik Pantone, sablon kaca frosted, dan foil Champagne sebelum cetak massal.</p>
        </div>
      </div>

      <div class="footer-bot">
        <span>© SELUNÉA · Owner: NANA · All Vector Masters Outlined</span>
        <div class="kalla-badge" aria-label="Identity designed by KALLA">
          {kalla_dark}
        </div>
      </div>
    </div>
  </footer>

  <!-- FULLSCREEN LIGHTBOX -->
  <div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Visual Board Preview">
    <div class="lb-bar">
      <span class="lb-title" id="lbCaption"></span>
      <button type="button" class="lb-close" id="lbClose">Close ✕</button>
    </div>
    <div class="lb-img-wrap">
      <img id="lbImg" src="" alt="Expanded board preview" />
    </div>
  </div>

  <!-- COPY TOAST -->
  <div class="toast" id="toast" role="status" aria-live="polite"></div>

<script>
  // 1. Mobile Navigation Drawer
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

  // 2. Interactive Logo Surface Playground
  const pgStage = document.getElementById('pgStage');
  const pgDark = document.getElementById('pgLogoDark');
  const pgLight = document.getElementById('pgLogoLight');
  const pgChamp = document.getElementById('pgLogoChamp');
  const pgCap = document.getElementById('pgCaption');
  document.querySelectorAll('.surface-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      document.querySelectorAll('.surface-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const bg = btn.dataset.bg;
      const mode = btn.dataset.mode;
      pgStage.style.backgroundColor = bg;
      pgDark.style.display = mode === 'dark' ? 'block' : 'none';
      pgLight.style.display = mode === 'light' ? 'block' : 'none';
      pgChamp.style.display = mode === 'champ' ? 'block' : 'none';
      pgCap.style.color = mode === 'dark' ? '#34332F' : '#F3F0E9';
      pgCap.textContent = btn.dataset.cap;
    }});
  }});

  // 3. Click-to-copy Color HEX
  const toast = document.getElementById('toast');
  let toastTimer = null;
  function showToast(msg) {{
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 2000);
  }}
  document.querySelectorAll('[data-copy]').forEach(btn => {{
    btn.addEventListener('click', async () => {{
      const hex = btn.dataset.copy;
      try {{ await navigator.clipboard.writeText(hex); }} catch (e) {{}}
      showToast('Copied ' + hex);
    }});
  }});

  // 4. Lightbox Modal for Full Visual Boards
  const lb = document.getElementById('lightbox');
  const lbImg = document.getElementById('lbImg');
  const lbCap = document.getElementById('lbCaption');
  const lbClose = document.getElementById('lbClose');
  function openLightbox(src, cap) {{
    lbImg.src = src;
    lbCap.textContent = cap || '';
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
    lbClose.focus();
  }}
  function closeLightbox() {{
    lb.classList.remove('open');
    document.body.style.overflow = '';
  }}
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
    print("Built responsive all-in-one showcase website:", out_file)


if __name__ == "__main__":
    build_website()
