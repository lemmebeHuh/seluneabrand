"""
SELUNÉA — Customer-Facing Womenswear Link-in-Bio (Dark & Bright Monochrome Edition)
Output: c:/Users/ridwa/Desktop/selunea/selunea-brand-identity/links.html

Features:
- Contemporary Womenswear positioning (zero skincare mentions)
- Smooth Dark & Bright theme toggle (Black & White + Champagne/Bronze accent, saved to localStorage)
- Ultra-concise, to-the-point link buttons (single-line clarity, zero wall-of-text bloat)
- Immersive smooth motion: orbital halo, ticker marquee, pointer spotlight, smooth accordion
- Removed per brief: top-left @selun.ea button, Share button, 5-phase, Follow & Shop via
- Brand-only footer (zero KALLA, zero owner name, zero brand guideline references)
"""

import re
import urllib.parse
from pathlib import Path

BASE = Path(r"c:\Users\ridwa\Desktop\selunea\selunea-brand-identity")
SVG_DIR = BASE / "05-logo-final" / "svg"


def strip_svg_inner(path: Path) -> tuple[str, str]:
    """Return (viewBox, inner_xml_with_currentColor) from an official SVG master."""
    txt = path.read_text(encoding="utf-8").strip()
    txt = re.sub(r"<title[^>]*>.*?</title>\s*", "", txt, flags=re.S)
    vb_m = re.search(r'viewBox="([^"]+)"', txt)
    vb = vb_m.group(1) if vb_m else "0 0 256 256"
    m = re.search(r"<svg[^>]*>(.*)</svg>", txt, flags=re.S)
    inner = m.group(1).strip() if m else txt
    inner = re.sub(r'fill="#[0-9a-fA-F]{3,6}"', 'fill="currentColor"', inner)
    return vb, inner


def build_favicon_data_uri() -> str:
    """Build inline SVG data URI using the small-responsive Celestial Lotus-Moon mark."""
    _, mark_inner = strip_svg_inner(SVG_DIR / "selunea-brand-mark-small-responsive.svg")
    mark_white = mark_inner.replace("currentColor", "#FFFFFF")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">'
        '<rect width="256" height="256" rx="56" fill="#0B0B0D"/>'
        f'<g transform="translate(36 36) scale(0.718)">{mark_white}</g>'
        "</svg>"
    )
    return "data:image/svg+xml," + urllib.parse.quote(svg)


def build_linktree():
    mark_vb, mark_inner = strip_svg_inner(SVG_DIR / "selunea-brand-mark-white-reversed.svg")
    wm_vb, wm_inner = strip_svg_inner(SVG_DIR / "selunea-primary-wordmark-white-reversed.svg")
    favicon_uri = build_favicon_data_uri()

    marquee_items = (
        "<span>CONTEMPORARY WOMENSWEAR</span><span class='m-dot'></span>"
        "<span>MONOCHROME EDIT</span><span class='m-dot'></span>"
        "<span>TIMELESS SILHOUETTES</span><span class='m-dot'></span>"
        "<span>BEAUTY IN EVERY PHASE</span><span class='m-dot'></span>"
    )

    html = f"""<!DOCTYPE html>
<html lang="id" data-theme="dark">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>SELUNÉA — Contemporary Womenswear</title>
<meta name="description" content="SELUNÉA (@selun.ea) — Contemporary womenswear. Official links: Shopee, Tokopedia, Instagram." />
<link rel="icon" type="image/svg+xml" href="{favicon_uri}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet" />
<script>
  try {{
    const savedTheme = localStorage.getItem('selunea_links_theme');
    if (savedTheme === 'light' || savedTheme === 'dark') {{
      document.documentElement.setAttribute('data-theme', savedTheme);
    }}
  }} catch (e) {{}}
</script>
<style>
  :root, [data-theme="dark"] {{
    --bg: #0B0B0D;
    --sheet-a: rgba(20, 20, 24, 0.96);
    --sheet-b: rgba(14, 14, 17, 0.98);
    --surface: #121215;
    --card: #18181D;
    --card-hover: #202027;
    --ink: #FFFFFF;
    --muted: #A1A1AA;
    --accent: #D5C3AA;
    --accent-pill-bg: rgba(213, 195, 170, 0.14);
    --accent-pill-fg: #D5C3AA;
    --hero-bg: #FFFFFF;
    --hero-fg: #0B0B0D;
    --hero-icon-bg: #0B0B0D;
    --hero-icon-fg: #D5C3AA;
    --hero-arrow-line: rgba(11, 11, 13, 0.22);
    --emblem-bg: #0B0B0D;
    --emblem-fg: #FFFFFF;
    --line: rgba(255, 255, 255, 0.12);
    --line-strong: rgba(255, 255, 255, 0.24);
    --orbit-a: #FFFFFF;
    --orbit-b: #D5C3AA;
    --glow: rgba(213, 195, 170, 0.10);
    --spot: rgba(213, 195, 170, 0.16);
    --spot-hero: rgba(213, 195, 170, 0.34);
    --sheet-shadow: 0 28px 70px rgba(0, 0, 0, 0.65);
    --toast-bg: #FFFFFF;
    --toast-fg: #0B0B0D;
  }}

  [data-theme="light"] {{
    --bg: #F3F2EE;
    --sheet-a: rgba(255, 255, 255, 0.98);
    --sheet-b: rgba(250, 249, 246, 0.98);
    --surface: #F7F6F3;
    --card: #FAF9F6;
    --card-hover: #F2F0EB;
    --ink: #0B0B0D;
    --muted: #52525B;
    --accent: #6B5B4B;
    --accent-pill-bg: rgba(107, 91, 75, 0.12);
    --accent-pill-fg: #6B5B4B;
    --hero-bg: #0B0B0D;
    --hero-fg: #FFFFFF;
    --hero-icon-bg: #FFFFFF;
    --hero-icon-fg: #0B0B0D;
    --hero-arrow-line: rgba(213, 195, 170, 0.36);
    --emblem-bg: #0B0B0D;
    --emblem-fg: #D5C3AA;
    --line: rgba(11, 11, 13, 0.12);
    --line-strong: rgba(11, 11, 13, 0.25);
    --orbit-a: #0B0B0D;
    --orbit-b: #6B5B4B;
    --glow: rgba(107, 91, 75, 0.08);
    --spot: rgba(107, 91, 75, 0.10);
    --spot-hero: rgba(213, 195, 170, 0.22);
    --sheet-shadow: 0 22px 54px rgba(11, 11, 13, 0.08);
    --toast-bg: #0B0B0D;
    --toast-fg: #FFFFFF;
  }}

  :root {{
    --font-display: 'Cormorant Garamond', Georgia, serif;
    --font-sans: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    --ease: cubic-bezier(0.22, 1, 0.36, 1);
  }}

  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ -webkit-text-size-adjust: 100%; }}
  body {{
    min-height: 100dvh;
    background: var(--bg);
    color: var(--ink);
    font-family: var(--font-sans);
    font-size: 15px;
    line-height: 1.5;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px 14px 44px;
    -webkit-font-smoothing: antialiased;
    position: relative;
    overflow-x: hidden;
    transition: background-color 0.38s var(--ease), color 0.38s var(--ease);
  }}

  /* Immersive Ambient Orbital Backdrop */
  .ambient-stage {{
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
  }}
  .ambient-glow {{
    position: absolute;
    left: 50%;
    top: -160px;
    width: 720px;
    height: 720px;
    transform: translateX(-50%);
    background: radial-gradient(circle, var(--glow) 0%, transparent 68%);
    transition: background 0.38s var(--ease);
  }}
  .ambient-rings {{
    position: absolute;
    left: 50%;
    top: -90px;
    width: 820px;
    height: 820px;
    margin-left: -410px;
    opacity: 0.24;
    animation: slowOrbit 72s linear infinite;
  }}
  @keyframes slowOrbit {{
    from {{ transform: rotate(0deg); }}
    to {{ transform: rotate(360deg); }}
  }}

  a {{ color: inherit; text-decoration: none; }}
  button {{ font-family: inherit; cursor: pointer; background: none; border: none; color: inherit; }}
  :focus-visible {{ outline: 2px solid var(--accent); outline-offset: 3px; border-radius: 12px; }}

  /* Main Sheet */
  .sheet {{
    position: relative;
    z-index: 1;
    width: 100%;
    max-width: 460px;
    background: linear-gradient(180deg, var(--sheet-a) 0%, var(--sheet-b) 100%);
    border: 1px solid var(--line);
    border-radius: 28px;
    padding: 20px 18px 26px;
    box-shadow: var(--sheet-shadow);
    display: flex;
    flex-direction: column;
    gap: 18px;
    transition: background 0.38s var(--ease), border-color 0.38s var(--ease), box-shadow 0.38s var(--ease);
  }}

  /* Theme Toggle Row (Right-aligned only, zero left pill / share clutter) */
  .theme-bar {{
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }}
  .theme-switch {{
    display: inline-flex;
    align-items: center;
    gap: 2px;
    padding: 3px;
    border-radius: 999px;
    background: var(--card);
    border: 1px solid var(--line);
    transition: background-color 0.3s var(--ease), border-color 0.3s var(--ease);
  }}
  .theme-opt {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    min-height: 34px;
    padding: 0 12px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--muted);
    transition: background-color 0.24s var(--ease), color 0.24s var(--ease);
  }}
  .theme-opt[aria-pressed="true"] {{
    background: var(--ink);
    color: var(--bg);
  }}
  .theme-opt svg {{ width: 13px; height: 13px; }}

  /* Staggered Entrance Choreography */
  .stagger {{
    opacity: 0;
    transform: translateY(14px);
    animation: riseIn 0.7s var(--ease) forwards;
    animation-delay: var(--d, 0ms);
  }}
  @keyframes riseIn {{
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  /* Profile Header */
  .profile {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 10px;
    padding: 0 6px 2px;
  }}
  .emblem-orbit {{
    position: relative;
    width: 92px;
    height: 92px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .emblem-halo {{
    position: absolute;
    inset: 0;
    border-radius: 50%;
    border: 1px dashed var(--accent);
    opacity: 0.45;
    animation: slowOrbit 36s linear infinite;
  }}
  .emblem-core {{
    width: 74px;
    height: 74px;
    border-radius: 50%;
    background: var(--emblem-bg);
    border: 1px solid var(--line-strong);
    color: var(--emblem-fg);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.45s var(--ease), border-color 0.35s var(--ease), color 0.35s var(--ease);
  }}
  .emblem-orbit:hover .emblem-core {{
    transform: scale(1.05);
    border-color: var(--accent);
  }}
  .emblem-core svg {{ width: 40px; height: 40px; }}

  .fashion-kicker {{
    font-size: 10px;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: var(--accent);
    font-weight: 500;
  }}
  .wm-lockup {{
    width: 186px;
    height: auto;
    color: var(--ink);
    transition: color 0.35s var(--ease);
  }}
  .tagline {{
    font-family: var(--font-display);
    font-style: italic;
    font-weight: 400;
    font-size: 24px;
    line-height: 1.12;
    color: var(--ink);
  }}
  .bio {{
    font-size: 13px;
    color: var(--muted);
    max-width: 320px;
    line-height: 1.5;
  }}

  /* Smooth Editorial Ticker Strip */
  .marquee-wrap {{
    overflow: hidden;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    padding: 8px 0;
    margin: 0 -18px;
    mask-image: linear-gradient(90deg, transparent 0%, #000 12%, #000 88%, transparent 100%);
    -webkit-mask-image: linear-gradient(90deg, transparent 0%, #000 12%, #000 88%, transparent 100%);
  }}
  .marquee-track {{
    display: flex;
    width: max-content;
    animation: ticker 26s linear infinite;
  }}
  .marquee-wrap:hover .marquee-track {{ animation-play-state: paused; }}
  .marquee-group {{
    display: flex;
    align-items: center;
    gap: 16px;
    padding-right: 16px;
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--muted);
    white-space: nowrap;
  }}
  .m-dot {{
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: var(--accent);
    display: inline-block;
  }}
  @keyframes ticker {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-50%); }}
  }}

  /* Concise, To-The-Point Monochrome Link Stack */
  .links-stack {{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}

  .card-spotlight {{
    position: relative;
    overflow: hidden;
    isolation: isolate;
  }}
  .card-spotlight::before {{
    content: '';
    position: absolute;
    inset: 0;
    z-index: -1;
    opacity: 0;
    background: radial-gradient(260px circle at var(--mx, 50%) var(--my, 50%), var(--spot), transparent 65%);
    transition: opacity 0.26s ease;
  }}
  .card-spotlight:hover::before {{ opacity: 1; }}

  /* Primary Contrast CTA (Shopee) */
  .link-hero {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    min-height: 62px;
    padding: 11px 14px;
    border-radius: 16px;
    background: var(--hero-bg);
    color: var(--hero-fg);
    border: 1px solid var(--hero-bg);
    transition: transform 0.26s var(--ease), box-shadow 0.26s var(--ease), background-color 0.35s var(--ease), color 0.35s var(--ease);
  }}
  .link-hero.card-spotlight::before {{
    background: radial-gradient(260px circle at var(--mx, 50%) var(--my, 50%), var(--spot-hero), transparent 65%);
  }}
  .link-hero:hover {{ transform: translateY(-2px); }}
  .link-hero:active {{ transform: scale(0.985); }}
  .link-hero .icon-box {{
    background: var(--hero-icon-bg);
    color: var(--hero-icon-fg);
    border-color: transparent;
  }}
  .link-hero .arrow-pill {{
    border-color: var(--hero-arrow-line);
    color: var(--hero-fg);
  }}

  /* Concise Standard Cards */
  .link-card {{
    width: 100%;
    text-align: left;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    min-height: 58px;
    padding: 10px 14px;
    border-radius: 16px;
    background: var(--card);
    color: var(--ink);
    border: 1px solid var(--line);
    transition: transform 0.24s var(--ease), border-color 0.24s var(--ease), background-color 0.3s var(--ease), color 0.3s var(--ease);
  }}
  .link-card:hover {{
    background: var(--card-hover);
    border-color: var(--accent);
    transform: translateY(-2px);
  }}
  .link-card:active {{ transform: scale(0.985); }}

  .card-left {{
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: 0;
  }}
  .icon-box {{
    width: 38px;
    height: 38px;
    border-radius: 10px;
    background: var(--surface);
    border: 1px solid var(--line);
    color: var(--ink);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    transition: border-color 0.22s, color 0.22s, transform 0.26s var(--ease), background-color 0.3s var(--ease);
  }}
  .link-card:hover .icon-box {{
    border-color: var(--accent);
    color: var(--accent);
    transform: scale(1.04);
  }}
  .icon-box svg {{ width: 18px; height: 18px; }}

  .btn-label {{
    font-size: clamp(13px, 3.6vw, 14.5px);
    font-weight: 500;
    line-height: 1.25;
    display: flex;
    align-items: center;
    gap: 7px;
    flex-wrap: nowrap;
    white-space: nowrap;
  }}
  .pill-tag {{
    font-size: 9.5px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 2px 8px;
    border-radius: 999px;
    background: var(--accent-pill-bg);
    color: var(--accent-pill-fg);
    font-weight: 500;
  }}
  .link-hero .pill-tag {{
    background: var(--accent);
    color: #FFFFFF;
  }}
  [data-theme="dark"] .link-hero .pill-tag {{
    background: #0B0B0D;
    color: #D5C3AA;
  }}

  .arrow-pill {{
    width: 30px;
    height: 30px;
    border-radius: 50%;
    border: 1px solid var(--line);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: var(--muted);
    transition: transform 0.24s var(--ease), color 0.22s, border-color 0.22s;
  }}
  .link-hero:hover .arrow-pill,
  .link-card:hover .arrow-pill {{ transform: translateX(3px); }}
  .link-card:hover .arrow-pill {{
    color: var(--accent);
    border-color: var(--accent);
  }}
  .link-card[aria-expanded="true"] .arrow-pill {{
    transform: rotate(90deg);
    color: var(--accent);
    border-color: var(--accent);
  }}

  /* Smooth Grid-Row Accordion (Style Edit) */
  .accordion-wrap {{
    display: grid;
    grid-template-rows: 0fr;
    opacity: 0;
    transition: grid-template-rows 0.42s var(--ease), opacity 0.34s ease, margin-top 0.42s var(--ease);
    margin-top: -6px;
  }}
  .accordion-wrap.open {{
    grid-template-rows: 1fr;
    opacity: 1;
    margin-top: 0;
  }}
  .accordion-inner {{ overflow: hidden; }}
  .maison-drawer {{
    background: var(--surface);
    border: 1px solid var(--line-strong);
    border-radius: 16px;
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 11px;
  }}
  .maison-pills {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .edit-pill {{
    min-height: 32px;
    padding: 0 11px;
    border-radius: 999px;
    border: 1px solid var(--line);
    background: var(--card);
    font-size: 11.5px;
    color: var(--muted);
    transition: background-color 0.2s, color 0.2s, border-color 0.2s;
  }}
  .edit-pill:hover {{ border-color: var(--accent); color: var(--ink); }}
  .edit-pill.active {{
    background: var(--ink);
    color: var(--bg);
    border-color: var(--ink);
    font-weight: 500;
  }}
  .edit-note {{
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
    transition: opacity 0.18s ease;
  }}

  /* Brand-Only Footer */
  .foot {{
    padding-top: 14px;
    border-top: 1px solid var(--line);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    text-align: center;
  }}
  .foot-brand {{
    font-size: 11.5px;
    letter-spacing: 0.18em;
    color: var(--accent);
    font-weight: 500;
  }}
  .foot-sub {{
    font-size: 11.5px;
    color: var(--muted);
  }}

  .toast {{
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%) translateY(14px);
    background: var(--toast-bg);
    color: var(--toast-fg);
    border: 1px solid var(--accent);
    padding: 9px 17px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 500;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s, transform 0.2s var(--ease);
    z-index: 50;
    white-space: nowrap;
  }}
  .toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}

  @media (min-width: 640px) {{
    body {{ padding: 42px 20px 56px; }}
    .sheet {{ padding: 22px 24px 28px; }}
    .marquee-wrap {{ margin: 0 -24px; }}
  }}
  @media (prefers-reduced-motion: reduce) {{
    .ambient-rings, .marquee-track {{ animation: none !important; }}
    .stagger {{ opacity: 1 !important; transform: none !important; animation: none !important; }}
    *, *::before, *::after {{ transition: none !important; }}
  }}
</style>
</head>
<body>
  <div class="ambient-stage" aria-hidden="true">
    <div class="ambient-glow"></div>
    <svg class="ambient-rings" viewBox="0 0 820 820" fill="none">
      <circle cx="410" cy="410" r="290" stroke="var(--orbit-a)" stroke-width="0.8" stroke-dasharray="4 8"/>
      <circle cx="426" cy="396" r="370" stroke="var(--orbit-b)" stroke-width="0.9"/>
    </svg>
  </div>

  <main class="sheet">
    <!-- Dark / Bright Theme Toggle -->
    <div class="theme-bar stagger" style="--d: 20ms;">
      <div class="theme-switch" role="group" aria-label="Pilih mode tampilan">
        <button type="button" class="theme-opt" data-set-theme="dark" aria-pressed="true">
          <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <path d="M13.2 10.1A5.5 5.5 0 0 1 5.9 2.8a5.5 5.5 0 1 0 7.3 7.3Z" stroke="currentColor" stroke-width="1.35" stroke-linejoin="round"/>
          </svg>
          <span>Dark</span>
        </button>
        <button type="button" class="theme-opt" data-set-theme="light" aria-pressed="false">
          <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <circle cx="8" cy="8" r="3" stroke="currentColor" stroke-width="1.35"/>
            <path d="M8 1.5v1.4M8 13.1v1.4M1.5 8h1.4M13.1 8h1.4M3.4 3.4l1 1M11.6 11.6l1 1M12.6 3.4l-1 1M4.4 11.6l-1 1" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
          </svg>
          <span>Bright</span>
        </button>
      </div>
    </div>

    <!-- Brand Profile Header -->
    <header class="profile stagger" style="--d: 60ms;">
      <div class="emblem-orbit">
        <div class="emblem-halo" aria-hidden="true"></div>
        <div class="emblem-core">
          <svg viewBox="{mark_vb}" role="img" aria-label="SELUNÉA">{mark_inner}</svg>
        </div>
      </div>
      <span class="fashion-kicker">Contemporary Womenswear</span>
      <svg viewBox="{wm_vb}" class="wm-lockup" role="img" aria-label="SELUNÉA">{wm_inner}</svg>
      <p class="tagline">“Beauty in Every Phase.”</p>
      <p class="bio">Busana wanita kontemporer dengan siluet tenang untuk setiap fase aktivitasmu.</p>
    </header>

    <!-- Editorial Marquee -->
    <div class="marquee-wrap stagger" style="--d: 110ms;" aria-hidden="true">
      <div class="marquee-track">
        <div class="marquee-group">{marquee_items}</div>
        <div class="marquee-group">{marquee_items}</div>
      </div>
    </div>

    <!-- To-The-Point Links Stack -->
    <nav class="links-stack" aria-label="Tautan Resmi SELUNÉA">
      <!-- Shopee -->
      <a href="https://shopee.co.id/selun.ea" target="_blank" rel="noopener noreferrer" class="link-hero card-spotlight stagger" style="--d: 160ms;">
        <div class="card-left">
          <span class="icon-box" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none"><path d="M6 8h12l-1 12H7L6 8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 8V6a3 3 0 0 1 6 0v2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          </span>
          <span class="btn-label"><span>Shopee Official Store</span><span class="pill-tag">Shop</span></span>
        </div>
        <span class="arrow-pill" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M5 11 11 5M6.5 5H11v4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
      </a>

      <!-- Tokopedia -->
      <a href="https://www.tokopedia.com/selunea" target="_blank" rel="noopener noreferrer" class="link-card card-spotlight stagger" style="--d: 210ms;">
        <div class="card-left">
          <span class="icon-box" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none"><path d="M5.5 7.5h13l-.8 12.5H6.3L5.5 7.5Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 7.5a3 3 0 0 1 6 0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="10" cy="13" r="1" fill="currentColor"/><circle cx="14" cy="13" r="1" fill="currentColor"/></svg>
          </span>
          <span class="btn-label"><span>Tokopedia Official Store</span></span>
        </div>
        <span class="arrow-pill" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M5 11 11 5M6.5 5H11v4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
      </a>

      <!-- Instagram @selun.ea -->
      <a href="https://instagram.com/selun.ea" target="_blank" rel="noopener noreferrer" class="link-card card-spotlight stagger" style="--d: 260ms;">
        <div class="card-left">
          <span class="icon-box" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none"><rect x="3.5" y="3.5" width="17" height="17" rx="5" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="12" r="3.8" stroke="currentColor" stroke-width="1.6"/><circle cx="17" cy="7" r="1" fill="currentColor"/></svg>
          </span>
          <span class="btn-label"><span>Instagram · @selun.ea</span></span>
        </div>
        <span class="arrow-pill" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M5 11 11 5M6.5 5H11v4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
      </a>

      <!-- DM Order & Konsultasi -->
      <a href="https://ig.me/m/selun.ea" target="_blank" rel="noopener noreferrer" class="link-card card-spotlight stagger" style="--d: 310ms;">
        <div class="card-left">
          <span class="icon-box" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none"><path d="M20.5 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3.5 20.5l1.4-4.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 7.5 7.5v.5Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
          </span>
          <span class="btn-label"><span>Order &amp; Tanya Size (DM)</span></span>
        </div>
        <span class="arrow-pill" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M5 11 11 5M6.5 5H11v4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
      </a>

      <!-- Tentang SELUNÉA Accordion -->
      <button type="button" class="link-card card-spotlight stagger" id="storyToggleBtn" style="--d: 360ms;" aria-expanded="false" aria-controls="storyAccordion">
        <div class="card-left">
          <span class="icon-box" aria-hidden="true">
            <svg viewBox="{mark_vb}" aria-hidden="true">{mark_inner}</svg>
          </span>
          <span class="btn-label"><span>Tentang SELUNÉA</span><span class="pill-tag">Edit</span></span>
        </div>
        <span class="arrow-pill" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M6 3.5 10.5 8 6 12.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
      </button>

      <div class="accordion-wrap" id="storyAccordion">
        <div class="accordion-inner">
          <div class="maison-drawer">
            <div class="maison-pills" role="tablist" aria-label="Karakter Koleksi SELUNÉA">
              <button type="button" class="edit-pill active" role="tab" aria-selected="true" data-note="Siluet bersih yang mudah dipadupadankan dari kerja hingga makan malam.">Tailored Ease</button>
              <button type="button" class="edit-pill" role="tab" aria-selected="false" data-note="Potongan jatuh yang mengikuti gerak tubuh secara alami dan ringan.">Fluid Draping</button>
              <button type="button" class="edit-pill" role="tab" aria-selected="false" data-note="Palet hitam, putih, dan aksen hangat untuk lemari kapsul harian.">Monochrome Edit</button>
            </div>
            <p class="edit-note" id="editNote">Siluet bersih yang mudah dipadupadankan dari kerja hingga makan malam.</p>
          </div>
        </div>
      </div>

      <!-- Email Inquiries (One concise button -> copies email cleanly) -->
      <button type="button" class="link-card card-spotlight stagger" id="copyEmailBtn" style="--d: 410ms;">
        <div class="card-left">
          <span class="icon-box" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none"><rect x="3.5" y="5.5" width="17" height="13" rx="2.5" stroke="currentColor" stroke-width="1.6"/><path d="m4.5 7 7.5 5.5L19.5 7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <span class="btn-label"><span>hello@selunea.com</span><span class="pill-tag">Copy</span></span>
        </div>
        <span class="arrow-pill" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><rect x="5" y="5" width="7.5" height="8" rx="1.5" stroke="currentColor" stroke-width="1.4"/><path d="M3.5 10.5v-6A1.5 1.5 0 0 1 5 3h5.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
        </span>
      </button>
    </nav>

    <!-- Brand-Only Footer -->
    <footer class="foot stagger" style="--d: 460ms;">
      <div class="foot-brand">© SELUNÉA</div>
      <div class="foot-sub">Contemporary Womenswear · Beauty in Every Phase.</div>
    </footer>
  </main>

  <div class="toast" id="toast" role="status" aria-live="polite"></div>

<script>
  const toast = document.getElementById('toast');
  let toastTimer = null;
  function showToast(msg) {{
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 2200);
  }}

  // Dark & Bright Mode Switcher
  const themeButtons = Array.from(document.querySelectorAll('[data-set-theme]'));
  function applyTheme(mode, notify = false) {{
    const next = mode === 'light' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    themeButtons.forEach(btn => {{
      btn.setAttribute('aria-pressed', String(btn.dataset.setTheme === next));
    }});
    try {{ localStorage.setItem('selunea_links_theme', next); }} catch (e) {{}}
    if (notify) showToast(next === 'light' ? 'Mode Bright aktif' : 'Mode Dark aktif');
  }}
  applyTheme(document.documentElement.getAttribute('data-theme') || 'dark', false);
  themeButtons.forEach(btn => {{
    btn.addEventListener('click', () => applyTheme(btn.dataset.setTheme, true));
  }});

  // Interactive Pointer Spotlight on Cards
  document.querySelectorAll('.card-spotlight').forEach(card => {{
    card.addEventListener('pointermove', (e) => {{
      const rect = card.getBoundingClientRect();
      card.style.setProperty('--mx', (e.clientX - rect.left) + 'px');
      card.style.setProperty('--my', (e.clientY - rect.top) + 'px');
    }});
  }});

  // Smooth Accordion Toggle (Tentang SELUNÉA)
  const storyBtn = document.getElementById('storyToggleBtn');
  const storyAccordion = document.getElementById('storyAccordion');
  storyBtn.addEventListener('click', () => {{
    const isOpen = storyAccordion.classList.toggle('open');
    storyBtn.setAttribute('aria-expanded', String(isOpen));
  }});

  // Interactive Style Edit Pills
  const editPills = Array.from(document.querySelectorAll('.edit-pill'));
  const editNote = document.getElementById('editNote');
  editPills.forEach(pill => {{
    pill.addEventListener('click', () => {{
      editPills.forEach(p => {{
        const active = p === pill;
        p.classList.toggle('active', active);
        p.setAttribute('aria-selected', String(active));
      }});
      editNote.style.opacity = '0';
      setTimeout(() => {{
        editNote.textContent = pill.dataset.note;
        editNote.style.opacity = '1';
      }}, 140);
    }});
  }});

  // Copy Email
  document.getElementById('copyEmailBtn').addEventListener('click', async () => {{
    try {{ await navigator.clipboard.writeText('hello@selunea.com'); }} catch (e) {{}}
    showToast('hello@selunea.com tersalin');
  }});
</script>
</body>
</html>
"""
    out = BASE / "links.html"
    out.write_text(html, encoding="utf-8")
    print(f"Built Dark & Bright SELUNÉA Womenswear Linktree: {out} ({out.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build_linktree()
