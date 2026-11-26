"""
SELUNÉA — Final Responsive Brand Identity Showcase Website Builder
Approved Final Brand Mark: Celestial Lotus-Moon (Client Option 03, 100/100 pure outlined vector)
Output: c:/Users/ridwa/Desktop/selunea/selunea-brand-identity/index.html
"""

import json
import re
from pathlib import Path

BASE = Path(r"c:\Users\ridwa\Desktop\selunea\selunea-brand-identity")
SVG_DIR = BASE / "05-logo-final" / "svg"
GFX_DIR = BASE / "07-graphic-assets"


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
    # Final Approved Celestial Lotus-Moon Brand Mark (pure outlined vectors, currentColor-ready)
    mark_inner = strip_svg_outer(SVG_DIR / "selunea-brand-mark-midnight-ash.svg")
    wm_inner = strip_svg_outer(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg")
    wm_sm_inner = strip_svg_outer(SVG_DIR / "selunea-wordmark-small-responsive.svg")

    # Official SVG masters for Architecture & Chrome
    wm_nav = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", css_class="nav-wm")
    wm_hero = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", css_class="hero-wm")
    wm_footer = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", style="height:30px;width:auto;")
    wm_card = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", style="height:22px;width:auto;")
    wm_card_ch = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-champagne.svg", style="height:22px;width:auto;")

    wm_ash_arch = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg", css_class="arch-svg")
    sec_ash = load_svg_inline(SVG_DIR / "selunea-secondary-skincare-midnight-ash.svg", css_class="arch-svg")
    mark_ash_arch = load_svg_inline(SVG_DIR / "selunea-brand-mark-midnight-ash.svg", css_class="arch-svg-sq")
    mono_ash = load_svg_inline(SVG_DIR / "selunea-monogram-s-midnight-ash.svg", css_class="arch-svg-sq")
    hlock_ash = load_svg_inline(SVG_DIR / "selunea-horizontal-lockup-midnight-ash.svg", css_class="arch-svg")
    slock_ash = load_svg_inline(SVG_DIR / "selunea-stacked-lockup-midnight-ash.svg", css_class="arch-svg-tall")
    wm_white_arch = load_svg_inline(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg", css_class="arch-svg")
    mark_white_tile = load_svg_inline(SVG_DIR / "selunea-brand-mark-white-reversed.svg", style="width:48px;height:48px;")
    mark_champ_lid = load_svg_inline(SVG_DIR / "selunea-brand-mark-champagne.svg", style="width:54px;height:54px;")
    mark_ivory_rev = load_svg_inline(SVG_DIR / "selunea-brand-mark-white-reversed.svg", style="width:56px;height:56px;")

    # Supporting Graphic Assets
    divider_svg = load_svg_inline(GFX_DIR / "lunar-phase-divider.svg", css_class="gfx-divider")
    orbital_svg = load_svg_inline(GFX_DIR / "orbital-frame-accent.svg", css_class="gfx-sq")
    pattern_svg = load_svg_inline(GFX_DIR / "phase-pattern-tile.svg", css_class="gfx-sq-rad")
    pearl_svg = load_svg_inline(GFX_DIR / "pearl-luminosity-backdrop.svg", css_class="gfx-wide")

    # Studio Attribution (by KALLA)
    kalla_light = kalla_signature_svg(color="#34332F", accent="#9F8B72", height=17)
    kalla_dark = kalla_signature_svg(color="#F3F0E9", accent="#C8B9A6", height=20)
    kalla_hero = kalla_signature_svg(color="#F3F0E9", accent="#C8B9A6", height=18)

    def mark_svg(extra_class="", size_style=""):
        cls = f"brand-mark-svg {extra_class}".strip()
        st = f' style="{size_style}"' if size_style else ""
        return f'<svg viewBox="0 0 256 256" class="{cls}"{st} aria-hidden="true">{mark_inner}</svg>'

    # Dynamically collect real finalized production assets from disk (zero broken paths!)
    def list_rel(folder: Path, patterns, zip_folder: str):
        items = []
        for pat in patterns:
            for p in sorted(folder.glob(pat)):
                if p.is_file():
                    rel = p.relative_to(BASE).as_posix()
                    items.append({
                        "label": p.name,
                        "url": rel,
                        "zipPath": f"SELUNEA-Brand-Assets/{zip_folder}/{p.name}",
                        "sizeKb": max(1, round(p.stat().st_size / 1024)),
                    })
        return items

    asset_groups = [
        {
            "id": "logo-svg",
            "title": "Master Logo Suite (SVG)",
            "desc": "Brand Mark Celestial Lotus-Moon (100/100 outlined), Primary & Secondary Wordmark, S Monogram, Horizontal & Stacked Lockups.",
            "badge": "Vector · Outlined",
            "defaultChecked": True,
            "files": list_rel(SVG_DIR, ["*.svg"], "01-logo-svg"),
        },
        {
            "id": "logo-png",
            "title": "High-Res Logo PNGs",
            "desc": "File transparan siap pakai (1024–1600 px) dalam warna Midnight Ash, Black, Reversed White & Champagne.",
            "badge": "Transparent PNG",
            "defaultChecked": True,
            "files": list_rel(BASE / "05-logo-final" / "png", ["*.png"], "02-logo-png"),
        },
        {
            "id": "web-icons",
            "title": "Web Icons & Favicon Kit",
            "desc": "Favicon SVG/ICO, Apple Touch Icon, Android Chrome 192/512 px, dan Web Manifest dengan Celestial Lotus-Moon.",
            "badge": "Web & App Ready",
            "defaultChecked": True,
            "files": list_rel(BASE / "05-logo-final" / "web-icons", ["*.svg", "*.png", "*.ico", "*.webmanifest"], "03-web-icons"),
        },
        {
            "id": "brand-pdfs",
            "title": "Brand Guidelines & Presentation PDF",
            "desc": "Buku Panduan Brand 15 bab lengkap dan Deck Presentasi Klien 5 slide beresolusi vektor siap cetak.",
            "badge": "Official PDFs",
            "defaultChecked": True,
            "files": (
                list_rel(BASE / "10-brand-guidelines", ["selunea-brand-guidelines.pdf"], "04-brand-documents")
                + list_rel(BASE / "11-presentations", ["selunea-client-presentation.pdf"], "04-brand-documents")
            ),
        },
        {
            "id": "packaging-assets",
            "title": "5-SKU Packaging Architecture",
            "desc": "Lembar spesifikasi kemasan 5 SKU skincare, folding carton & cap seal dalam format PDF dan PNG hi-res.",
            "badge": "Packaging Print",
            "defaultChecked": True,
            "files": list_rel(BASE / "08-packaging", ["01-skincare-packaging-family.pdf", "01-skincare-packaging-family.png"], "05-packaging"),
        },
        {
            "id": "collateral-boards",
            "title": "Stationery, Social & Color Boards",
            "desc": "Kartu nama NANA, unboxing collateral, preview Instagram/e-commerce, dan papan spesifikasi warna & tipografi.",
            "badge": "Visual Boards",
            "defaultChecked": False,
            "files": (
                list_rel(BASE / "09-brand-applications", ["*.png"], "06-brand-boards")
                + list_rel(BASE / "06-color-typography", ["03-color-typography-board.png"], "06-brand-boards")
            ),
        },
        {
            "id": "graphics-tokens",
            "title": "Graphic Assets (SVG) & Design Tokens",
            "desc": "Pattern tissue seamless Celestial Lotus-Moon, lunar divider, orbital frame, serta tokens JSON & CSS.",
            "badge": "SVG & Code Tokens",
            "defaultChecked": False,
            "files": (
                list_rel(GFX_DIR, ["*.svg"], "07-graphics-and-tokens")
                + list_rel(BASE / "06-color-typography", ["01-design-tokens.json", "02-design-tokens.css"], "07-graphics-and-tokens")
            ),
        },
    ]

    asset_groups_json = json.dumps(asset_groups, ensure_ascii=False, separators=(",", ":"))

    asset_cards_html = []
    for g in asset_groups:
        checked_attr = " checked" if g["defaultChecked"] else ""
        active_cls = " selected" if g["defaultChecked"] else ""
        total_kb = sum(f["sizeKb"] for f in g["files"])
        size_str = f"{total_kb/1024:.1f} MB" if total_kb >= 1024 else f"{total_kb} KB"
        file_items = "".join(
            f'''<label class="file-row">
              <input type="checkbox" class="file-cb" data-group="{g['id']}" data-url="{f['url']}" data-zip="{f['zipPath']}"{checked_attr} />
              <span class="file-name">{f['label']}</span>
              <span class="file-size">{f['sizeKb']} KB</span>
            </label>'''
            for f in g["files"]
        )
        asset_cards_html.append(f'''
        <div class="asset-card{active_cls}" data-card-group="{g['id']}">
          <div class="asset-card-top">
            <label class="group-check-wrap">
              <input type="checkbox" class="group-cb" data-group-master="{g['id']}"{checked_attr} />
              <span class="custom-box" aria-hidden="true"></span>
              <span class="group-titles">
                <span class="asset-badge">{g['badge']}</span>
                <strong>{g['title']}</strong>
              </span>
            </label>
            <span class="group-count" data-group-count="{g['id']}">{len(g['files'])} file · {size_str}</span>
          </div>
          <p class="asset-desc">{g['desc']}</p>
          <details class="file-drawer">
            <summary>Pilih file satuan ({len(g['files'])})</summary>
            <div class="file-list">{file_items}</div>
          </details>
        </div>''')

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>SELUNÉA — Brand Identity System by KALLA</title>
<meta name="description" content="Official Brand Identity System for SELUNÉA (Beauty in Every Phase) — Celestial Lotus-Moon Brand Mark, presented for NANA, designed by KALLA." />
<link rel="icon" type="image/svg+xml" href="05-logo-final/web-icons/favicon.svg" />
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
  .hero-grid > *, .strategy-grid > *, .arch-grid > *, .color-grid > *,
  .type-stack > *, .gfx-grid > *, .owner-spot > *, .boards-grid > *, .dl-grid > *, .footer-top > * {{
    min-width: 0;
  }}

  .wrap {{ width: 100%; max-width: var(--container); margin: 0 auto; padding: 0 20px; }}
  .brand-mark-svg {{ flex-shrink: 0; color: currentColor; }}

  /* One-shot Editorial Scroll Reveal */
  .reveal {{
    opacity: 0;
    transform: translateY(18px);
    transition: opacity 620ms var(--ease-luxury), transform 620ms var(--ease-luxury);
  }}
  .reveal.in-view {{ opacity: 1; transform: translateY(0); }}
  @media (prefers-reduced-motion: reduce) {{
    .reveal {{ transition: none !important; opacity: 1 !important; transform: none !important; }}
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
  .nav-mark {{ width: 26px; height: 26px; color: var(--ash); }}
  .nav-wm {{ height: 21px; width: auto; flex-shrink: 0; }}
  .nav-sep {{ width: 1px; height: 18px; background: var(--line); display: none; }}
  .nav-kalla {{ display: none; align-items: center; }}

  .nav-links {{ display: none; align-items: center; gap: 4px; }}
  .nav-links a {{ font-size: 12.5px; letter-spacing: 0.05em; color: var(--ash-soft); padding: 10px 11px; border-radius: 8px; transition: color 0.18s, background 0.18s; }}
  .nav-links a:hover {{ color: var(--ash); background: rgba(52,51,47,0.06); }}

  .nav-actions {{ display: flex; align-items: center; gap: 8px; }}
  .btn-pdf-sm {{ display: none; font-size: 11px; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; padding: 10px 16px; border-radius: 999px; background: var(--ash); color: var(--ivory); min-height: 40px; align-items: center; transition: background 0.18s; }}
  .btn-pdf-sm:hover {{ background: var(--ash-deep); }}

  .menu-toggle {{ display: inline-flex; align-items: center; gap: 8px; min-height: 44px; min-width: 44px; padding: 0 14px; border: 1px solid var(--line); border-radius: 999px; background: var(--ivory-card); font-size: 12px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }}

  /* Mobile Drawer */
  .mobile-drawer {{ display: none; position: fixed; inset: var(--nav-h) 0 0 0; z-index: 55; background: rgba(243, 240, 233, 0.98); padding: 20px 20px 36px; overflow-y: auto; border-top: 1px solid var(--line); }}
  .mobile-drawer.open {{ display: flex; flex-direction: column; justify-content: space-between; gap: 24px; }}
  .drawer-nav {{ display: flex; flex-direction: column; gap: 4px; }}
  .drawer-nav a {{ display: flex; align-items: center; justify-content: space-between; min-height: 48px; padding: 12px 14px; border-bottom: 1px solid var(--line); font-family: var(--font-display); font-size: 24px; font-weight: 500; }}
  .drawer-nav a span.num {{ font-family: var(--font-sans); font-size: 11px; letter-spacing: 0.16em; color: var(--ash-soft); }}
  .drawer-foot {{ padding-top: 16px; display: flex; flex-direction: column; gap: 14px; }}

  /* ---------------- HERO + APPROVED IDENTITY SHOWCASE ---------------- */
  .hero {{ background: var(--ash); color: var(--ivory); padding: 48px 0 60px; position: relative; }}
  .hero-grid {{ display: grid; grid-template-columns: 1fr; gap: 36px; align-items: center; }}
  .hero-kicker {{ font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--champagne); margin-bottom: 16px; }}
  .hero-brand-stack {{ display: flex; flex-direction: column; align-items: flex-start; gap: 16px; margin-bottom: 18px; }}
  .hero-mark {{ width: 68px; height: 68px; color: var(--champagne); }}
  .hero-wm {{ height: clamp(40px, 11vw, 66px); width: auto; max-width: 100%; margin-left: -10px; }}
  .hero-quote {{ font-family: var(--font-display); font-style: italic; font-weight: 400; font-size: clamp(26px, 5vw, 38px); line-height: 1.18; color: var(--champagne); margin-bottom: 12px; }}
  .hero-sub {{ font-size: 14.5px; color: rgba(243, 240, 233, 0.8); max-width: 520px; margin-bottom: 24px; }}
  .hero-cta-row {{ display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 26px; }}
  .btn-ivory {{ display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 20px; border-radius: 999px; background: var(--ivory); color: var(--ash-deep); font-size: 11.5px; font-weight: 600; letter-spacing: 0.11em; text-transform: uppercase; transition: background 0.18s, transform 0.15s; }}
  .btn-ivory:hover {{ background: #FFFFFF; }}
  .btn-outline-champ {{ display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 20px; border-radius: 999px; border: 1px solid var(--line-dark); color: var(--champagne); font-size: 11.5px; font-weight: 500; letter-spacing: 0.11em; text-transform: uppercase; transition: background 0.18s, border-color 0.18s; }}
  .btn-outline-champ:hover {{ background: rgba(200,185,166,0.12); border-color: var(--champagne); }}
  .hero-meta-bar {{ display: grid; grid-template-columns: 1fr; gap: 14px; padding-top: 20px; border-top: 1px solid var(--line-dark); }}
  .meta-item small {{ display: block; font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(243, 240, 233, 0.56); margin-bottom: 4px; }}
  .meta-item strong {{ font-size: 13.5px; font-weight: 500; color: var(--ivory); }}

  /* Approved Signature Showcase Card (Right Column of Hero) */
  .identity-showcase {{ background: rgba(243, 240, 233, 0.055); border: 1px solid var(--line-dark); border-radius: var(--radius-lg); padding: 22px; display: flex; flex-direction: column; gap: 14px; }}
  .showcase-head {{ display: flex; justify-content: space-between; align-items: center; gap: 10px; flex-wrap: wrap; }}
  .showcase-label {{ font-size: 10.5px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--champagne); }}
  .showcase-pill {{ font-size: 11px; color: var(--ivory); background: rgba(200,185,166,0.16); border: 1px solid var(--line-dark); padding: 4px 11px; border-radius: 999px; }}
  .showcase-lockup-card {{
    background: var(--ivory); color: var(--ash); border-radius: var(--radius-md);
    padding: 32px 22px 24px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px;
  }}
  .showcase-pair {{ display: flex; align-items: center; justify-content: center; gap: 18px; flex-wrap: wrap; }}
  .showcase-big-mark {{ width: 82px; height: 82px; color: var(--ash); }}
  .showcase-pair-wm {{ height: 36px; width: auto; color: var(--ash); }}
  .showcase-caption {{ font-size: 12px; color: var(--ash-soft); text-align: center; max-width: 400px; line-height: 1.5; }}
  .showcase-duo {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }}
  .showcase-tile {{
    border-radius: var(--radius-md); padding: 18px 14px;
    display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; text-align: center;
  }}
  .showcase-tile.lid-tile {{ background: linear-gradient(145deg, #EFECE4, #E3DDD1); color: var(--ash); }}
  .showcase-tile.dark-tile {{ background: var(--ash-deep); border: 1px solid var(--line-dark); color: var(--ivory); }}
  .jar-lid-seal {{
    width: 88px; height: 88px; border-radius: 50%;
    background: radial-gradient(circle at 32% 28%, #474540, #34332F 68%, #22211E);
    box-shadow: 0 10px 22px rgba(36,35,32,0.28);
    display: flex; align-items: center; justify-content: center;
  }}
  .tile-cap {{ font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; opacity: 0.78; }}

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
  .pg-mark-live {{ width: clamp(54px, 11vw, 74px); height: clamp(54px, 11vw, 74px); }}
  .pg-wm-live {{ height: clamp(34px, 7.5vw, 52px); width: auto; }}
  .pg-caption {{ font-size: 11.5px; letter-spacing: 0.1em; text-transform: uppercase; opacity: 0.72; text-align: center; }}
  .pg-controls {{ background: var(--white); border-top: 1px solid var(--line); padding: 14px 16px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px; }}
  .pg-swatches {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .surface-btn {{ display: inline-flex; align-items: center; gap: 8px; min-height: 44px; padding: 0 14px; border-radius: 8px; border: 1px solid var(--line); font-size: 12px; font-weight: 500; background: var(--ivory-card); transition: border-color 0.18s, background 0.18s; }}
  .surface-btn.active {{ border-color: var(--ash); background: var(--ivory); box-shadow: inset 0 0 0 1px var(--ash); }}
  .sw-chip {{ width: 14px; height: 14px; border-radius: 50%; border: 1px solid rgba(52,51,47,0.22); flex-shrink: 0; }}

  .arch-grid {{ display: grid; grid-template-columns: 1fr; gap: 16px; margin-bottom: 8px; }}
  .arch-card {{ background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); padding: 24px 20px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 18px; min-width: 0; }}
  .arch-card.dark {{ background: var(--ash); border-color: var(--ash); color: var(--ivory); }}
  .arch-stage {{ min-height: 108px; display: flex; align-items: center; justify-content: center; }}
  .arch-svg {{ max-height: 52px; width: auto; }}
  .arch-svg-sq {{ width: 78px; height: 78px; }}
  .arch-svg-tall {{ max-height: 92px; width: auto; }}
  .app-icon-tile {{ width: 78px; height: 78px; border-radius: 18px; background: var(--ash); color: var(--ivory); display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 22px rgba(52,51,47,0.16); }}

  .arch-meta {{ display: flex; justify-content: space-between; align-items: flex-end; gap: 10px; padding-top: 12px; border-top: 1px solid var(--line); }}
  .arch-card.dark .arch-meta {{ border-color: var(--line-dark); }}
  .arch-meta strong {{ display: block; font-size: 13px; font-weight: 500; }}
  .arch-meta span {{ font-size: 11.5px; color: var(--ash-soft); }}
  .arch-card.dark .arch-meta span {{ color: rgba(243,240,233,0.68); }}
  .dl-link {{ font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; font-weight: 500; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--line); min-height: 36px; display: inline-flex; align-items: center; white-space: nowrap; transition: background 0.16s; }}
  .dl-link:hover {{ background: rgba(52,51,47,0.06); }}
  .arch-card.dark .dl-link {{ border-color: var(--line-dark); color: var(--champagne); }}
  .arch-card.dark .dl-link:hover {{ background: rgba(200,185,166,0.12); }}

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

  /* ---------------- 04. 5-SKU PACKAGING SHELF ---------------- */
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
  .v-mark {{ width: 24px; height: 24px; color: var(--ash); }}
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

  .dl-grid {{ display: grid; grid-template-columns: 1fr; gap: 14px; margin-bottom: 28px; }}
  .dl-card {{ background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-md); padding: 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 14px; }}
  .dl-card strong {{ font-size: 15px; display: block; margin-bottom: 4px; }}
  .dl-card p {{ font-size: 12.5px; color: var(--ash-soft); }}
  .dl-btn-row {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .btn-dark-sm {{ display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 18px; border-radius: 999px; background: var(--ash); color: var(--ivory); font-size: 11.5px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; transition: background 0.18s; }}
  .btn-dark-sm:hover {{ background: var(--ash-deep); }}
  .btn-light-sm {{ display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 16px; border-radius: 999px; border: 1px solid var(--line); background: var(--ivory-card); color: var(--ash); font-size: 11.5px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; transition: background 0.18s; }}
  .btn-light-sm:hover {{ background: var(--ivory-deep); }}

  /* ---------------- 06. CUSTOM ZIP ASSET PICKER ---------------- */
  .zip-builder {{
    background: var(--white); border: 1px solid var(--line); border-radius: var(--radius-lg);
    overflow: hidden; box-shadow: 0 12px 30px rgba(52,51,47,0.05);
  }}
  .zip-toolbar {{
    padding: 18px 22px; background: var(--ivory); border-bottom: 1px solid var(--line);
    display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px;
  }}
  .zip-toolbar-title {{ display: flex; flex-direction: column; gap: 2px; }}
  .zip-toolbar-title strong {{ font-size: 14.5px; font-weight: 600; }}
  .zip-toolbar-title span {{ font-size: 12px; color: var(--ash-soft); }}
  .zip-toolbar-actions {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .zip-pill-btn {{
    min-height: 38px; padding: 0 14px; border-radius: 999px; border: 1px solid var(--line);
    background: var(--white); font-size: 11px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase;
    transition: background 0.16s, border-color 0.16s;
  }}
  .zip-pill-btn:hover {{ border-color: var(--ash); background: var(--ivory-card); }}

  .asset-picker-grid {{ display: grid; grid-template-columns: 1fr; gap: 14px; padding: 20px 22px; }}
  .asset-card {{
    background: var(--ivory-card); border: 1.5px solid var(--line); border-radius: var(--radius-md);
    padding: 16px 18px; display: flex; flex-direction: column; gap: 10px;
    transition: border-color 0.2s var(--ease-luxury), background-color 0.2s var(--ease-luxury), box-shadow 0.2s;
  }}
  .asset-card.selected {{
    background: var(--white); border-color: var(--ash);
    box-shadow: 0 8px 20px rgba(52,51,47,0.07);
  }}
  .asset-card-top {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; }}
  .group-check-wrap {{ display: flex; align-items: flex-start; gap: 12px; cursor: pointer; flex: 1; min-width: 0; }}
  .group-cb {{ position: absolute; opacity: 0; width: 1px; height: 1px; pointer-events: none; }}
  .custom-box {{
    width: 22px; height: 22px; border-radius: 6px; border: 1.5px solid rgba(52,51,47,0.34);
    background: var(--white); flex-shrink: 0; margin-top: 2px; position: relative;
    transition: background 0.16s, border-color 0.16s;
  }}
  .group-cb:checked + .custom-box {{ background: var(--ash); border-color: var(--ash); }}
  .group-cb:checked + .custom-box::after {{
    content: ''; position: absolute; left: 6px; top: 2px; width: 6px; height: 11px;
    border: solid var(--ivory); border-width: 0 2px 2px 0; transform: rotate(45deg);
  }}
  .group-cb:indeterminate + .custom-box {{ background: var(--champagne-deep); border-color: var(--champagne-deep); }}
  .group-cb:indeterminate + .custom-box::after {{
    content: ''; position: absolute; left: 4px; top: 8px; width: 11px; height: 2px; background: var(--white);
  }}
  .group-cb:focus-visible + .custom-box {{ outline: 2px solid var(--ash); outline-offset: 2px; }}
  .group-titles {{ display: flex; flex-direction: column; gap: 2px; min-width: 0; }}
  .asset-badge {{ font-size: 9.5px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--champagne-deep); font-weight: 500; }}
  .group-titles strong {{ font-size: 14.5px; font-weight: 600; line-height: 1.25; }}
  .group-count {{ font-size: 11px; color: var(--ash-soft); white-space: nowrap; padding-top: 2px; }}
  .asset-desc {{ font-size: 12.5px; color: var(--ash-soft); line-height: 1.5; padding-left: 34px; }}

  .file-drawer {{ padding-left: 34px; }}
  .file-drawer summary {{
    font-size: 11.5px; font-weight: 500; color: var(--ash); cursor: pointer;
    list-style: none; display: inline-flex; align-items: center; gap: 6px;
    padding: 4px 10px; border-radius: 6px; background: rgba(52,51,47,0.05);
  }}
  .file-drawer summary::-webkit-details-marker {{ display: none; }}
  .file-drawer summary::before {{ content: '▸'; font-size: 10px; transition: transform 0.16s; }}
  .file-drawer[open] summary::before {{ transform: rotate(90deg); }}
  .file-list {{
    margin-top: 10px; display: grid; gap: 6px; max-height: 186px; overflow-y: auto;
    padding: 10px; border-radius: 8px; background: var(--ivory); border: 1px solid var(--line);
  }}
  .file-row {{
    display: flex; align-items: center; gap: 8px; font-size: 12px; cursor: pointer;
    padding: 4px 6px; border-radius: 6px;
  }}
  .file-row:hover {{ background: rgba(52,51,47,0.05); }}
  .file-cb {{ width: 16px; height: 16px; accent-color: var(--ash); flex-shrink: 0; cursor: pointer; }}
  .file-name {{ flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 11px; }}
  .file-size {{ font-size: 10.5px; color: var(--ash-soft); flex-shrink: 0; }}

  .zip-footer {{
    padding: 18px 22px; background: var(--ash); color: var(--ivory);
    display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 14px;
  }}
  .zip-summary {{ display: flex; flex-direction: column; gap: 6px; flex: 1; min-width: 220px; }}
  .zip-summary strong {{ font-size: 14px; font-weight: 500; }}
  .zip-summary span {{ font-size: 12px; color: rgba(243,240,233,0.72); }}
  .zip-progress-track {{
    display: none; width: 100%; max-width: 340px; height: 6px; border-radius: 999px;
    background: rgba(243,240,233,0.18); overflow: hidden; margin-top: 2px;
  }}
  .zip-progress-track.active {{ display: block; }}
  .zip-progress-fill {{ width: 0%; height: 100%; background: var(--champagne); transition: width 120ms linear; }}
  .btn-download-zip {{
    display: inline-flex; align-items: center; justify-content: center; gap: 10px;
    min-height: 48px; padding: 0 24px; border-radius: 999px;
    background: var(--champagne); color: var(--ash-deep);
    font-size: 12px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase;
    transition: background 0.18s, transform 0.15s, opacity 0.18s;
  }}
  .btn-download-zip:hover:not(:disabled) {{ background: #D8CBB9; }}
  .btn-download-zip:active:not(:disabled) {{ transform: scale(0.98); }}
  .btn-download-zip:disabled {{ opacity: 0.45; cursor: not-allowed; }}

  /* ---------------- FOOTER ---------------- */
  .footer {{ background: var(--ash); color: var(--ivory); padding: 56px 0 48px; }}
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
    position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%) translateY(14px);
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
    .asset-picker-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .asset-card:last-child:nth-child(odd) {{ grid-column: 1 / -1; }}
    .type-item {{ grid-template-columns: 200px 1fr; }}
    .footer-top {{ grid-template-columns: 1.4fr 1fr 1fr; }}
    .footer-bot {{ flex-direction: row; align-items: center; }}
  }}

  /* ---------------- DESKTOP (>= 1024px) ---------------- */
  @media (min-width: 1024px) {{
    :root {{ --nav-h: 68px; }}
    .wrap {{ padding: 0 40px; }}
    .nav-links {{ display: flex; }}
    .btn-pdf-sm {{ display: inline-flex; }}
    .menu-toggle {{ display: none; }}
    .hero {{ padding: 72px 0 80px; }}
    .hero-grid {{ grid-template-columns: 1.02fr 0.98fr; gap: 52px; }}
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
        {mark_svg("nav-mark")}
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
        <a href="#production-assets">Downloads</a>
      </nav>

      <div class="nav-actions">
        <a href="10-brand-guidelines/selunea-brand-guidelines.pdf?v=20261126" target="_blank" class="btn-pdf-sm">Brand Book PDF</a>
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
      <a href="#strategy">Brand Strategy <span class="num">01</span></a>
      <a href="#logo-system">Logo Architecture <span class="num">02</span></a>
      <a href="#color-type">Color &amp; Typography <span class="num">03</span></a>
      <a href="#packaging">5-SKU Packaging <span class="num">04</span></a>
      <a href="#applications">Brand Applications <span class="num">05</span></a>
      <a href="#production-assets">Production Assets &amp; ZIP <span class="num">06</span></a>
    </nav>
    <div class="drawer-foot">
      <a href="10-brand-guidelines/selunea-brand-guidelines.pdf?v=20261126" target="_blank" class="btn-dark-sm" style="width:100%;">Open Brand Guidelines PDF</a>
      <div style="display:flex;justify-content:space-between;align-items:center;padding-top:6px;">
        <span style="font-size:11.5px;color:var(--ash-soft);">Presented for <b>NANA</b></span>
        {kalla_light}
      </div>
    </div>
  </div>

  <!-- HERO + APPROVED OFFICIAL IDENTITY SHOWCASE -->
  <section class="hero dark-surface" id="top">
    <div class="wrap hero-grid">
      <div>
        <div class="hero-kicker">Official Brand Identity System · Lunar Elegance</div>
        <div class="hero-brand-stack">
          {mark_svg("hero-mark")}
          {wm_hero}
        </div>
        <p class="hero-quote">“Beauty in Every Phase.”</p>
        <p class="hero-sub">
          Sistem identitas visual resmi <strong>SELUNÉA</strong> yang memadukan Brand Mark <strong>Celestial Lotus-Moon</strong> dengan wordmark couture <em>high-contrast</em> — dirangkum utuh dari strategi, palet mineral, kemasan 5 SKU, hingga panduan produksi siap cetak.
        </p>
        <div class="hero-cta-row">
          <a href="#logo-system" class="btn-ivory">Explore Logo System</a>
          <a href="10-brand-guidelines/selunea-brand-guidelines.pdf?v=20261126" target="_blank" class="btn-outline-champ">Brand Guidelines PDF</a>
        </div>
        <div class="hero-meta-bar">
          <div class="meta-item"><small>Founder &amp; Owner</small><strong>NANA</strong></div>
          <div class="meta-item"><small>Tagline</small><strong>Skincare for every version of you.</strong></div>
          <div class="meta-item"><small>Identity &amp; Direction</small><div style="margin-top:2px;">{kalla_hero}</div></div>
        </div>
      </div>

      <div class="identity-showcase" aria-label="SELUNÉA Official Brand Mark Showcase">
        <div class="showcase-head">
          <span class="showcase-label">Approved Brand Mark · Final Master</span>
          <span class="showcase-pill">Celestial Lotus-Moon · 100/100</span>
        </div>

        <div class="showcase-lockup-card">
          <div class="showcase-pair">
            {mark_svg("showcase-big-mark")}
            <svg viewBox="0 0 755 256" class="showcase-pair-wm" aria-label="SELUNÉA">{wm_inner}</svg>
          </div>
          <p class="showcase-caption">
            Empat kelopak fase bulan simetris berpadu busur sabit diagonal dan inti mutiara — di-<em>outline</em> penuh sebagai vektor murni untuk ketajaman foil, sablon kaca, dan ikon digital.
          </p>
        </div>

        <div class="showcase-duo">
          <div class="showcase-tile lid-tile">
            <div class="jar-lid-seal">{mark_champ_lid}</div>
            <span class="tile-cap">Champagne Foil · Jar Lid</span>
          </div>
          <div class="showcase-tile dark-tile">
            {mark_ivory_rev}
            <span class="tile-cap" style="color:var(--champagne);">Reversed · Midnight Ash</span>
          </div>
        </div>
      </div>
    </div>
  </section>

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
            <li><b>Celestial Lotus-Moon Crest:</b> Simetri halus empat kelopak bulan dan inti mutiara yang abadi.</li>
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
          <div class="sec-num">02 · Official Logo Architecture</div>
          <h2 class="sec-h2">Bespoke Wordmark &amp; <em>Celestial Lotus-Moon</em></h2>
        </div>
        <p class="sec-desc">
          Seluruh variasi master logo SELUNÉA telah di-<em>expand</em> menjadi <em>outlined vector paths</em> murni (audit 100/100 pada Brand Mark), termasuk versi <em>reversed white</em> dan potongan responsif ukuran kecil.
        </p>
      </div>

      <div class="playground" aria-label="Interactive Logo Surface Preview">
        <div class="pg-stage" id="pgStage">
          <div class="pg-lockup-live">
            {mark_svg("pg-mark-live")}
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
        <div class="arch-card"><div class="arch-stage">{mark_ash_arch}</div><div class="arch-meta"><div><strong>Official Brand Mark</strong><span>Celestial Lotus-Moon · 100/100</span></div><a href="05-logo-final/svg/selunea-brand-mark-midnight-ash.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card"><div class="arch-stage">{mono_ash}</div><div class="arch-meta"><div><strong>Celestial S Monogram</strong><span>Caps, Seals &amp; Foil Accents</span></div><a href="05-logo-final/svg/selunea-monogram-s-midnight-ash.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card"><div class="arch-stage">{hlock_ash}</div><div class="arch-meta"><div><strong>Horizontal Lockup</strong><span>Header, Banners &amp; Collateral</span></div><a href="05-logo-final/svg/selunea-horizontal-lockup-midnight-ash.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card"><div class="arch-stage">{slock_ash}</div><div class="arch-meta"><div><strong>Stacked Lockup</strong><span>Folding Cartons &amp; Bags</span></div><a href="05-logo-final/svg/selunea-stacked-lockup-midnight-ash.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card dark dark-surface"><div class="arch-stage">{wm_white_arch}</div><div class="arch-meta"><div><strong>Reversed White</strong><span>Irradiation-Thinned (~4%)</span></div><a href="05-logo-final/svg/selunea-primary-wordmark-white-reversed.svg" download class="dl-link">SVG</a></div></div>
        <div class="arch-card"><div class="arch-stage"><div class="app-icon-tile">{mark_white_tile}</div></div><div class="arch-meta"><div><strong>App &amp; Social Icon</strong><span>Midnight Ash Tile · 16–512 px</span></div><a href="05-logo-final/web-icons/favicon.svg" download class="dl-link">SVG</a></div></div>
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

  <!-- 04 · 5-SKU PACKAGING FAMILY -->
  <section class="section section-alt reveal" id="packaging">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">04 · 5-SKU Packaging System</div>
          <h2 class="sec-h2">Five-Phase <em>Product Family</em></h2>
        </div>
        <p class="sec-desc">Penerapan resmi Brand Mark <strong>Celestial Lotus-Moon</strong> dan wordmark SELUNÉA pada seluruh 5 kemasan skincare — dari tube matte Moon Ivory hingga botol kaca frosted dan jar satin Champagne.</p>
      </div>

      <div class="live-shelf-wrap">
        <div class="live-shelf-head">
          <span>SELUNÉA 5-SKU Lineup · Celestial Lotus-Moon Identity</span>
          <span>Geser ke samping pada layar ponsel →</span>
        </div>
        <div class="live-shelf-row">
          <div class="v-col"><div class="v-stage"><div class="v-tube"><div class="v-fop" style="height:212px;"><div class="v-top">{mark_svg("v-mark")}<svg viewBox="0 0 755 256" class="v-wm" aria-hidden="true">{wm_inner}</svg></div><div><div class="v-cat">Phase 01 · Cleanse</div><div class="v-name">Facial<br/>Cleanser</div><div class="v-band" style="background:var(--sage);"></div></div><div class="v-net">120 mL</div></div><div style="height:16px;background:var(--sage);"></div></div><div class="v-tube-cap"></div><div class="v-shadow"></div></div><div class="v-label"><strong>01 · Cleanser</strong><span>Sage Haze · Tube</span></div></div>
          <div class="v-col"><div class="v-stage"><div class="v-toner-cap"></div><div class="v-toner"><div class="v-fop"><div class="v-top">{mark_svg("v-mark")}<svg viewBox="0 0 755 256" class="v-wm" aria-hidden="true">{wm_inner}</svg></div><div><div class="v-cat">Phase 02 · Prepare</div><div class="v-name">Balancing<br/>Toner</div><div class="v-band" style="background:var(--lavender);"></div></div><div class="v-net">150 mL</div></div></div><div class="v-shadow"></div></div><div class="v-label"><strong>02 · Toner</strong><span>Frosted · Silver Cap</span></div></div>
          <div class="v-col"><div class="v-stage"><div class="v-bulb"></div><div class="v-collar"></div><div class="v-serum"><div class="v-fop" style="padding:12px 8px;"><div class="v-top">{mark_svg("v-mark", "width:20px;height:20px;")}<svg viewBox="0 0 782 256" class="v-wm" aria-hidden="true">{wm_sm_inner}</svg></div><div><div class="v-cat">Phase 03 · Treat</div><div class="v-name" style="font-size:16px;">Daily<br/>Serum</div><div class="v-band" style="background:var(--lavender);"></div></div><div class="v-net">30 mL</div></div></div><div class="v-shadow"></div></div><div class="v-label"><strong>03 · Serum</strong><span>Champagne Dropper</span></div></div>
          <div class="v-col"><div class="v-stage"><div class="v-jar-lid"></div><div class="v-jar"><div class="v-fop" style="padding:10px 10px 8px;"><div class="v-top" style="gap:3px;">{mark_svg("v-mark", "width:19px;height:19px;")}<svg viewBox="0 0 782 256" class="v-wm" style="width:56%;" aria-hidden="true">{wm_sm_inner}</svg></div><div><div class="v-name" style="font-size:16px;">Moisturizer</div><div class="v-band" style="background:var(--nude);"></div></div><div class="v-net">50 mL</div></div></div><div class="v-shadow" style="width:124px;"></div></div><div class="v-label"><strong>04 · Moisturizer</strong><span>Frosted Jar · Nude</span></div></div>
          <div class="v-col"><div class="v-stage"><div class="v-spf"><div class="v-fop" style="height:170px;padding:12px 8px 10px;"><div class="v-top">{mark_svg("v-mark", "width:20px;height:20px;")}<svg viewBox="0 0 782 256" class="v-wm" aria-hidden="true">{wm_sm_inner}</svg></div><div><div class="v-cat">Phase 05 · Shield</div><div class="v-name" style="font-size:16px;">Daily<br/>Sunscreen</div><div class="v-band" style="background:var(--nude);"></div></div><div class="v-net">50 mL</div></div><div style="height:16px;background:var(--nude);"></div></div><div class="v-spf-cap"></div><div class="v-shadow"></div></div><div class="v-label"><strong>05 · Sunscreen</strong><span>Matte Oval Tube</span></div></div>
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
        <p class="sec-desc">Penerapan identitas final pada kartu nama resmi <strong>NANA (Founder &amp; Owner)</strong>, pengalaman unboxing, media sosial, dan katalog e-commerce SELUNÉA.</p>
      </div>

      <div class="owner-spot">
        <div class="bcard-live ivory">
          <div style="display:flex;justify-content:space-between;align-items:center;">{wm_card}{mark_svg("", "width:30px;height:30px;color:#34332F;")}</div>
          <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap;">
            <div>
              <div style="font-family:var(--font-display);font-size:26px;font-weight:600;letter-spacing:0.06em;line-height:1.1;">NANA</div>
              <div style="font-size:10.5px;letter-spacing:0.16em;text-transform:uppercase;color:var(--ash-soft);">Founder &amp; Owner</div>
            </div>
            <div style="text-align:right;font-size:11.5px;color:var(--ash-soft);line-height:1.55;">nana@selunea.com<br/>@selunea.skin · selunea.com</div>
          </div>
        </div>
        <div class="bcard-live ash dark-surface">
          {mark_svg("", "width:46px;height:46px;color:#C8B9A6;")}
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

  <!-- 06 · PRODUCTION ASSETS & CUSTOM ZIP DOWNLOADER -->
  <section class="section section-alt" id="production-assets">
    <div class="wrap">
      <div class="section-head">
        <div>
          <div class="sec-num">06 · Production Assets &amp; Downloads</div>
          <h2 class="sec-h2">Production Assets &amp; <em>Custom ZIP</em></h2>
        </div>
        <p class="sec-desc">Buka dokumen PDF final secara langsung atau pilih sendiri paket &amp; file aset utama yang dibutuhkan, lalu kemas otomatis menjadi satu file <strong>.ZIP</strong>.</p>
      </div>

      <div class="dl-grid">
        <div class="dl-card">
          <div>
            <strong>Brand Guidelines Document</strong>
            <p>Dokumen resmi 15 bab lengkap dengan Brand Mark Celestial Lotus-Moon siap cetak &amp; presentasi (622 KB).</p>
          </div>
          <div class="dl-btn-row">
            <a href="10-brand-guidelines/selunea-brand-guidelines.pdf?v=20261126b" target="_blank" class="btn-dark-sm">Open PDF</a>
            <a href="10-brand-guidelines/selunea-brand-guidelines.pdf?v=20261126b" download="SELUNEA-Brand-Guidelines.pdf" class="btn-light-sm">Download PDF</a>
            <a href="10-brand-guidelines/selunea-brand-guidelines.html" target="_blank" class="btn-light-sm">HTML</a>
          </div>
        </div>
        <div class="dl-card">
          <div>
            <strong>Client Presentation Deck</strong>
            <p>Deck presentasi 5 slide landscape penuh dengan mockup resmi (NANA) dan sistem Celestial Lotus-Moon (204 KB).</p>
          </div>
          <div class="dl-btn-row">
            <a href="11-presentations/selunea-client-presentation.pdf?v=20261126b" target="_blank" class="btn-dark-sm">Open PDF</a>
            <a href="11-presentations/selunea-client-presentation.pdf?v=20261126b" download="SELUNEA-Client-Presentation.pdf" class="btn-light-sm">Download PDF</a>
            <a href="11-presentations/selunea-client-presentation.html" target="_blank" class="btn-light-sm">HTML</a>
          </div>
        </div>
        <div class="dl-card">
          <div>
            <strong>5-SKU Packaging Architecture</strong>
            <p>Lembar spesifikasi kemasan 5 SKU, folding carton pattern Celestial Lotus-Moon &amp; panduan produksi (678 KB).</p>
          </div>
          <div class="dl-btn-row">
            <a href="08-packaging/01-skincare-packaging-family.pdf?v=20261126b" target="_blank" class="btn-dark-sm">Open PDF</a>
            <a href="08-packaging/01-skincare-packaging-family.pdf?v=20261126b" download="SELUNEA-5SKU-Packaging.pdf" class="btn-light-sm">Download PDF</a>
            <a href="08-packaging/01-skincare-packaging-family.png?v=20261126b" download class="btn-light-sm">PNG</a>
          </div>
        </div>
      </div>

      <div class="zip-builder" aria-label="Custom Brand Asset ZIP Downloader">
        <div class="zip-toolbar">
          <div class="zip-toolbar-title">
            <strong>Pilih Main Assets untuk Diunduh (.ZIP)</strong>
            <span>Centang kategori atau buka “Pilih file satuan” untuk memilih file spesifik.</span>
          </div>
          <div class="zip-toolbar-actions">
            <button type="button" class="zip-pill-btn" id="selectAllAssets">Pilih Semua</button>
            <button type="button" class="zip-pill-btn" id="clearAllAssets">Hapus Pilihan</button>
          </div>
        </div>

        <div class="asset-picker-grid">
          {"".join(asset_cards_html)}
        </div>

        <div class="zip-footer dark-surface">
          <div class="zip-summary">
            <strong id="zipCountTitle">Menghitung file terpilih…</strong>
            <span id="zipStatusText">Aset akan dikemas rapi ke dalam folder SELUNEA-Brand-Assets-by-KALLA.zip</span>
            <div class="zip-progress-track" id="zipProgressTrack"><div class="zip-progress-fill" id="zipProgressFill"></div></div>
          </div>
          <button type="button" class="btn-download-zip" id="downloadZipBtn">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
              <path d="M8 2v8m0 0-3-3m3 3 3-3M2.5 11.5v1.5a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-1.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span id="zipBtnLabel">Download Selected (.ZIP)</span>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER COLOPHON -->
  <footer class="footer dark-surface">
    <div class="wrap">
      <div class="footer-top">
        <div>
          <div style="display:flex;align-items:center;gap:14px;">{mark_svg("", "width:36px;height:36px;color:#C8B9A6;")}{wm_footer}</div>
          <div class="footer-quote">“Beauty in Every Phase.”</div>
          <p style="font-size:13px;color:rgba(243,240,233,0.68);margin-top:8px;max-width:340px;">Skincare for every version of you. Brand Identity System prepared exclusively for <strong>NANA</strong> (Founder &amp; Owner).</p>
        </div>
        <div class="footer-col">
          <h4>Sections</h4>
          <a href="#strategy">Brand Strategy</a>
          <a href="#logo-system">Logo Architecture</a>
          <a href="#color-type">Color &amp; Typography</a>
          <a href="#packaging">5-SKU Packaging</a>
          <a href="#production-assets">Production Assets &amp; ZIP</a>
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
  const toast = document.getElementById('toast');
  let toastTimer = null;
  function showToast(msg) {{
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 2500);
  }}

  // Editorial Scroll Reveal (safe for tall mobile sections & direct #hash jumps!)
  function revealVisibleNow() {{
    const vh = window.innerHeight || 900;
    document.querySelectorAll('.reveal:not(.in-view)').forEach(el => {{
      const r = el.getBoundingClientRect();
      if (r.top < vh + 40 && r.bottom > -40) el.classList.add('in-view');
    }});
  }}
  if ('IntersectionObserver' in window) {{
    const revObs = new IntersectionObserver((entries, obs) => {{
      entries.forEach(e => {{
        if (e.isIntersecting) {{ e.target.classList.add('in-view'); obs.unobserve(e.target); }}
      }});
    }}, {{ threshold: 0.01 }});
    document.querySelectorAll('.reveal').forEach(el => revObs.observe(el));
    window.addEventListener('hashchange', () => setTimeout(revealVisibleNow, 50));
    window.addEventListener('load', revealVisibleNow);
    setTimeout(revealVisibleNow, 80);
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

  // Surface Contrast Playground
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

  // Copy HEX Swatches
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

  // ---------------- ZERO-DEPENDENCY CLIENT-SIDE ZIP BUILDER ----------------
  const CRC_TABLE = (() => {{
    const t = new Uint32Array(256);
    for (let i = 0; i < 256; i++) {{
      let c = i;
      for (let k = 0; k < 8; k++) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
      t[i] = c >>> 0;
    }}
    return t;
  }})();

  function crc32(bytes) {{
    let c = 0xFFFFFFFF;
    for (let i = 0; i < bytes.length; i++) c = CRC_TABLE[(c ^ bytes[i]) & 0xFF] ^ (c >>> 8);
    return (c ^ 0xFFFFFFFF) >>> 0;
  }}

  function buildZipBlob(entries) {{
    const enc = new TextEncoder();
    const localParts = [];
    const centralParts = [];
    let offset = 0;

    const now = new Date();
    const dosTime = ((now.getHours() & 0x1F) << 11) | ((now.getMinutes() & 0x3F) << 5) | ((now.getSeconds() >> 1) & 0x1F);
    const dosDate = (((Math.max(1980, now.getFullYear()) - 1980) & 0x7F) << 9) | (((now.getMonth() + 1) & 0x0F) << 5) | (now.getDate() & 0x1F);

    // Prepend explicit directory entries for 100% compatibility across Windows Explorer, WinRAR, 7-Zip & macOS
    const seenDirs = new Set();
    const fullList = [];
    for (const item of entries) {{
      const parts = item.name.split('/');
      let cur = '';
      for (let i = 0; i < parts.length - 1; i++) {{
        cur += parts[i] + '/';
        if (!seenDirs.has(cur)) {{
          seenDirs.add(cur);
          fullList.push({{ name: cur, data: new Uint8Array(0), isDir: true }});
        }}
      }}
      fullList.push({{ name: item.name, data: item.data, isDir: false }});
    }}

    for (const item of fullList) {{
      const nameBytes = enc.encode(item.name);
      const data = item.data;
      const crc = item.isDir ? 0 : crc32(data);
      const extAttr = item.isDir ? 0x10 : 0x20; // DOS directory vs archive attribute

      const lh = new Uint8Array(30 + nameBytes.length);
      const lv = new DataView(lh.buffer);
      lv.setUint32(0, 0x04034B50, true);
      lv.setUint16(4, 20, true);
      lv.setUint16(6, 0, true);      // Standard ASCII flags (universal compatibility)
      lv.setUint16(8, 0, true);      // Store (uncompressed)
      lv.setUint16(10, dosTime, true);
      lv.setUint16(12, dosDate, true);
      lv.setUint32(14, crc, true);
      lv.setUint32(18, data.length, true);
      lv.setUint32(22, data.length, true);
      lv.setUint16(26, nameBytes.length, true);
      lv.setUint16(28, 0, true);
      lh.set(nameBytes, 30);
      localParts.push(lh);
      if (data.length > 0) localParts.push(data);

      const ch = new Uint8Array(46 + nameBytes.length);
      const cv = new DataView(ch.buffer);
      cv.setUint32(0, 0x02014B50, true);
      cv.setUint16(4, 20, true);
      cv.setUint16(6, 20, true);
      cv.setUint16(8, 0, true);
      cv.setUint16(10, 0, true);
      cv.setUint16(12, dosTime, true);
      cv.setUint16(14, dosDate, true);
      cv.setUint32(16, crc, true);
      cv.setUint32(20, data.length, true);
      cv.setUint32(24, data.length, true);
      cv.setUint16(28, nameBytes.length, true);
      cv.setUint16(30, 0, true);
      cv.setUint16(32, 0, true);
      cv.setUint16(34, 0, true);
      cv.setUint16(36, 0, true);
      cv.setUint32(38, extAttr, true);
      cv.setUint32(42, offset, true);
      ch.set(nameBytes, 46);
      centralParts.push(ch);

      offset += lh.length + data.length;
    }}

    const centralSize = centralParts.reduce((s, p) => s + p.length, 0);
    const eocd = new Uint8Array(22);
    const ev = new DataView(eocd.buffer);
    ev.setUint32(0, 0x06054B50, true);
    ev.setUint16(4, 0, true);
    ev.setUint16(6, 0, true);
    ev.setUint16(8, fullList.length, true);
    ev.setUint16(10, fullList.length, true);
    ev.setUint32(12, centralSize, true);
    ev.setUint32(16, offset, true);
    ev.setUint16(20, 0, true);

    // Flatten into a single contiguous Uint8Array for rock-solid downloads across all browsers
    const totalLen = offset + centralSize + eocd.length;
    const out = new Uint8Array(totalLen);
    let pos = 0;
    for (const part of localParts) {{ out.set(part, pos); pos += part.length; }}
    for (const part of centralParts) {{ out.set(part, pos); pos += part.length; }}
    out.set(eocd, pos);
    return new Blob([out], {{ type: 'application/zip' }});
  }}

  async function fetchBinaryAsset(url) {{
    const bustUrl = url + (url.includes('?') ? '&' : '?') + '_cb=' + Date.now();
    // Primary: fetch with cache: 'no-store'
    try {{
      const res = await fetch(bustUrl, {{ cache: 'no-store' }});
      if (res.ok) {{
        const buf = await res.arrayBuffer();
        if (buf && buf.byteLength > 0) return new Uint8Array(buf);
      }}
    }} catch (e) {{}}
    // Fallback: XMLHttpRequest arraybuffer (bypasses occasional fetch cache/PDF interceptor quirks)
    return await new Promise((resolve, reject) => {{
      const xhr = new XMLHttpRequest();
      xhr.open('GET', url + '?_xhr=' + Date.now(), true);
      xhr.responseType = 'arraybuffer';
      xhr.onload = () => {{
        if (xhr.status >= 200 && xhr.status < 300 && xhr.response && xhr.response.byteLength > 0) {{
          resolve(new Uint8Array(xhr.response));
        }} else {{
          reject(new Error('File kosong atau gagal dimuat: ' + url));
        }}
      }};
      xhr.onerror = () => reject(new Error('Gagal mengambil ' + url));
      xhr.send();
    }});
  }}

  const groupCbs = Array.from(document.querySelectorAll('.group-cb'));
  const fileCbs = Array.from(document.querySelectorAll('.file-cb'));
  const zipCountTitle = document.getElementById('zipCountTitle');
  const zipStatusText = document.getElementById('zipStatusText');
  const zipBtn = document.getElementById('downloadZipBtn');
  const zipBtnLabel = document.getElementById('zipBtnLabel');
  const zipProgressTrack = document.getElementById('zipProgressTrack');
  const zipProgressFill = document.getElementById('zipProgressFill');

  function syncZipUI() {{
    let activeGroups = 0;
    groupCbs.forEach(gcb => {{
      const gid = gcb.dataset.groupMaster;
      const children = fileCbs.filter(f => f.dataset.group === gid);
      const checkedCount = children.filter(f => f.checked).length;
      gcb.checked = checkedCount === children.length && children.length > 0;
      gcb.indeterminate = checkedCount > 0 && checkedCount < children.length;
      const card = document.querySelector(`[data-card-group="${{gid}}"]`);
      if (card) card.classList.toggle('selected', checkedCount > 0);
      if (checkedCount > 0) activeGroups++;
    }});
    const selectedFiles = fileCbs.filter(f => f.checked);
    zipBtn.disabled = selectedFiles.length === 0;
    if (selectedFiles.length === 0) {{
      zipCountTitle.textContent = 'Belum ada aset yang dipilih';
      zipStatusText.textContent = 'Centang minimal satu kategori atau file untuk membuat arsip .ZIP.';
    }} else {{
      zipCountTitle.textContent = `${{selectedFiles.length}} file terpilih dari ${{activeGroups}} kategori`;
      zipStatusText.textContent = 'Siap dikemas langsung ke SELUNEA-Brand-Assets-by-KALLA.zip';
    }}
  }}

  groupCbs.forEach(gcb => {{
    gcb.addEventListener('change', () => {{
      const gid = gcb.dataset.groupMaster;
      fileCbs.filter(f => f.dataset.group === gid).forEach(f => {{ f.checked = gcb.checked; }});
      syncZipUI();
    }});
  }});

  fileCbs.forEach(fcb => fcb.addEventListener('change', syncZipUI));

  document.getElementById('selectAllAssets').addEventListener('click', () => {{
    fileCbs.forEach(f => {{ f.checked = true; }});
    syncZipUI();
  }});

  document.getElementById('clearAllAssets').addEventListener('click', () => {{
    fileCbs.forEach(f => {{ f.checked = false; }});
    syncZipUI();
  }});

  zipBtn.addEventListener('click', async () => {{
    const selected = fileCbs.filter(f => f.checked);
    if (!selected.length) return;
    zipBtn.disabled = true;
    zipBtnLabel.textContent = 'Mengemas .ZIP…';
    zipProgressTrack.classList.add('active');
    zipProgressFill.style.width = '4%';

    try {{
      const entries = [];
      for (let i = 0; i < selected.length; i++) {{
        const el = selected[i];
        const fname = el.dataset.zip.split('/').pop();
        zipStatusText.textContent = `Mengambil ${{i + 1}} / ${{selected.length}}: ${{fname}}`;
        const data = await fetchBinaryAsset(el.dataset.url);
        entries.push({{ name: el.dataset.zip, data }});
        zipProgressFill.style.width = Math.round(((i + 1) / selected.length) * 100) + '%';
      }}
      zipStatusText.textContent = 'Menyusun arsip ZIP…';
      const blob = buildZipBlob(entries);
      const sizeKb = Math.round(blob.size / 1024);
      const sizeLabel = sizeKb >= 1024 ? (sizeKb / 1024).toFixed(2) + ' MB' : sizeKb + ' KB';
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'SELUNEA-Brand-Assets-by-KALLA.zip';
      document.body.appendChild(a);
      a.click();
      a.remove();
      setTimeout(() => URL.revokeObjectURL(url), 10000);
      showToast(`Berhasil mengunduh ${{entries.length}} aset (${{sizeLabel}})`);
    }} catch (err) {{
      showToast('Gagal mengemas ZIP — pastikan halaman dibuka lewat http:// / GitHub Pages');
      console.error(err);
    }} finally {{
      zipBtnLabel.textContent = 'Download Selected (.ZIP)';
      setTimeout(() => {{
        zipProgressTrack.classList.remove('active');
        zipProgressFill.style.width = '0%';
        syncZipUI();
      }}, 900);
    }}
  }});

  syncZipUI();
</script>
</body>
</html>
"""
    out_file = BASE / "index.html"
    out_file.write_text(html, encoding="utf-8")
    print("Built finalized SELUNÉA Brand Identity showcase:", out_file)


if __name__ == "__main__":
    build_website()
