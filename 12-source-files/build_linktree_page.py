"""
SELUNÉA — Customer-Facing Standalone One-Page Link-in-Bio (Linktree Style) Builder
Output: c:/Users/ridwa/Desktop/selunea/selunea-brand-identity/links.html

Strictly for SELUNÉA's skincare customers & audience:
- Official Instagram handle: @selun.ea (https://instagram.com/selun.ea)
- Zero internal brand-guideline / presentation / agency (KALLA) / owner (NANA) mentions
- 100% self-contained single HTML file with inline outlined SVG brand marks & wordmark
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
    mark_ivory = mark_inner.replace("currentColor", "#F3F0E9")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">'
        '<rect width="256" height="256" rx="56" fill="#34332F"/>'
        f'<g transform="translate(36 36) scale(0.718)">{mark_ivory}</g>'
        "</svg>"
    )
    return "data:image/svg+xml," + urllib.parse.quote(svg)


def build_linktree():
    mark_vb, mark_inner = strip_svg_inner(SVG_DIR / "selunea-brand-mark-midnight-ash.svg")
    wm_vb, wm_inner = strip_svg_inner(SVG_DIR / "selunea-primary-wordmark-midnight-ash.svg")
    mono_vb, mono_inner = strip_svg_inner(SVG_DIR / "selunea-monogram-s-midnight-ash.svg")
    favicon_uri = build_favicon_data_uri()

    skus = [
        (
            "01",
            "Cleanse",
            "Facial Cleanser",
            "Langkah awal untuk membersihkan kulit dengan lembut tanpa rasa kering.",
            "120 mL",
            "#D9DFD5",
        ),
        (
            "02",
            "Prepare",
            "Balancing Toner",
            "Membantu menyegarkan dan menyiapkan kelembapan alami kulit setiap hari.",
            "150 mL",
            "#DCD9E2",
        ),
        (
            "03",
            "Treat",
            "Daily Serum",
            "Perawatan harian bernutrisi ringan untuk membantu menjaga kilau sehat kulit.",
            "30 mL",
            "#DCD9E2",
        ),
        (
            "04",
            "Nourish",
            "Moisturizer",
            "Mengunci hidrasi agar kulit terasa tenang, lembut, dan kenyal lebih lama.",
            "50 mL",
            "#E4DAD0",
        ),
        (
            "05",
            "Shield",
            "Daily Sunscreen",
            "Langkah perlindungan harian yang ringan dan nyaman untuk rutinitas pagi.",
            "50 mL",
            "#E4DAD0",
        ),
    ]

    ritual_tabs = "\n          ".join(
        f'<button type="button" class="phase-tab{" active" if i == 0 else ""}" '
        f'role="tab" aria-selected="{"true" if i == 0 else "false"}" '
        f'data-phase="{p}" data-step="{step}" data-name="{name}" '
        f'data-desc="{desc}" data-net="{net}" data-tint="{tint}">'
        f'<span class="phase-dot" style="background:{tint};" aria-hidden="true"></span>'
        f'<span>{p}</span></button>'
        for i, (p, step, name, desc, net, tint) in enumerate(skus)
    )

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>SELUNÉA — Beauty in Every Phase</title>
<meta name="description" content="SELUNÉA (@selun.ea) — Skincare for every version of you. Jelajahi 5 langkah perawatan harian, update terbaru, dan saluran resmi SELUNÉA." />
<link rel="icon" type="image/svg+xml" href="{favicon_uri}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400;1,500&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet" />
<style>
  :root {{
    --ivory: #F3F0E9;
    --ivory-card: #FAF8F4;
    --ivory-desk: #EAE4DA;
    --ash: #34332F;
    --ash-soft: #5B5953;
    --ash-deep: #242320;
    --champagne: #C8B9A6;
    --silver: #B8B7B1;
    --sage: #D9DFD5;
    --lavender: #DCD9E2;
    --nude: #E4DAD0;
    --white: #FFFFFF;
    --line: rgba(52, 51, 47, 0.14);
    --line-strong: rgba(52, 51, 47, 0.28);
    --font-display: 'Cormorant Garamond', Georgia, serif;
    --font-sans: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    --ease: cubic-bezier(0.22, 1, 0.36, 1);
  }}

  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ -webkit-text-size-adjust: 100%; }}
  body {{
    min-height: 100dvh;
    background: var(--ivory);
    color: var(--ash);
    font-family: var(--font-sans);
    font-size: 15px;
    line-height: 1.55;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 18px 14px 40px;
    -webkit-font-smoothing: antialiased;
    position: relative;
    overflow-x: hidden;
  }}

  /* Subtle lunar-orbital rings behind desktop frame */
  .bg-orbit {{
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
  }}
  .bg-orbit svg {{
    position: absolute;
    left: 50%;
    top: -120px;
    transform: translateX(-50%);
    width: 960px;
    height: 960px;
    opacity: 0.42;
  }}

  a {{ color: inherit; text-decoration: none; }}
  button {{ font-family: inherit; cursor: pointer; background: none; border: none; color: inherit; }}
  :focus-visible {{ outline: 2px solid var(--ash); outline-offset: 3px; border-radius: 10px; }}

  .sheet {{
    position: relative;
    z-index: 1;
    width: 100%;
    max-width: 480px;
    background: var(--ivory-card);
    border: 1px solid var(--line);
    border-radius: 26px;
    padding: 20px 18px 26px;
    box-shadow: 0 18px 48px rgba(52, 51, 47, 0.08);
    display: flex;
    flex-direction: column;
    gap: 18px;
  }}

  /* Top Utility Bar */
  .top-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
  }}
  .handle-pill {{
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 6px 12px;
    border-radius: 999px;
    background: var(--ivory);
    border: 1px solid var(--line);
    font-size: 11.5px;
    font-weight: 500;
    letter-spacing: 0.06em;
    color: var(--ash);
  }}
  .handle-pill svg {{ width: 15px; height: 15px; flex-shrink: 0; }}
  .share-btn {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    min-height: 40px;
    padding: 0 14px;
    border-radius: 999px;
    border: 1px solid var(--line);
    background: var(--white);
    font-size: 11.5px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    transition: border-color 0.18s, background 0.18s, transform 0.15s;
  }}
  .share-btn:hover {{ border-color: var(--ash); background: var(--ivory); }}
  .share-btn:active {{ transform: scale(0.97); }}

  /* Profile Header */
  .profile {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 6px 8px 2px;
    gap: 11px;
  }}
  .avatar-ring {{
    width: 88px;
    height: 88px;
    border-radius: 50%;
    padding: 4px;
    border: 1px solid var(--line-strong);
    background: var(--white);
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .avatar-core {{
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: var(--ash);
    color: var(--champagne);
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .avatar-core svg {{ width: 46px; height: 46px; }}
  .wm-lockup {{ width: 184px; height: auto; color: var(--ash); margin-top: 2px; }}
  .tagline {{
    font-family: var(--font-display);
    font-style: italic;
    font-weight: 500;
    font-size: 24px;
    line-height: 1.15;
    color: var(--ash);
  }}
  .bio {{
    font-size: 13.5px;
    color: var(--ash-soft);
    max-width: 340px;
    line-height: 1.55;
  }}

  /* Featured Primary Banner Card */
  .featured-link {{
    background: var(--ash);
    color: var(--ivory);
    border-radius: 18px;
    padding: 18px 18px 17px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    transition: transform 0.2s var(--ease), background 0.2s;
  }}
  .featured-link:hover {{ background: var(--ash-deep); transform: translateY(-2px); }}
  .featured-link:active {{ transform: scale(0.99); }}
  .featured-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
  }}
  .featured-kicker {{
    font-size: 10px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--champagne);
    font-weight: 500;
  }}
  .featured-arrow {{
    width: 32px;
    height: 32px;
    border-radius: 50%;
    border: 1px solid rgba(200, 185, 166, 0.35);
    color: var(--champagne);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }}
  .featured-title {{
    font-family: var(--font-display);
    font-size: 25px;
    font-weight: 500;
    line-height: 1.12;
  }}
  .featured-sub {{
    font-size: 12.5px;
    color: rgba(243, 240, 233, 0.84);
    line-height: 1.45;
  }}

  /* Interactive 5-Phase Ritual Strip */
  .ritual-card {{
    background: var(--white);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .section-mini-head {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 10.5px;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--ash-soft);
    font-weight: 500;
  }}
  .phase-tabs {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 6px;
  }}
  .phase-tab {{
    min-height: 44px;
    border-radius: 10px;
    border: 1px solid var(--line);
    background: var(--ivory-card);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    font-size: 11px;
    font-weight: 500;
    color: var(--ash);
    transition: border-color 0.16s, background 0.16s, transform 0.14s;
  }}
  .phase-tab:hover {{ border-color: var(--ash); }}
  .phase-tab.active {{
    background: var(--ash);
    color: var(--ivory);
    border-color: var(--ash);
  }}
  .phase-dot {{
    width: 14px;
    height: 4px;
    border-radius: 99px;
    border: 1px solid rgba(52, 51, 47, 0.18);
  }}
  .phase-tab.active .phase-dot {{ border-color: rgba(255, 255, 255, 0.35); }}

  .ritual-detail {{
    background: var(--ivory);
    border-radius: 12px;
    padding: 14px;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 12px;
    border-left: 5px solid var(--sage);
    transition: border-color 0.24s var(--ease);
  }}
  .ritual-detail small {{
    display: block;
    font-size: 10px;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--ash-soft);
    margin-bottom: 3px;
  }}
  .ritual-detail strong {{
    display: block;
    font-family: var(--font-display);
    font-size: 21px;
    font-weight: 600;
    line-height: 1.1;
  }}
  .ritual-detail span.meta {{
    display: block;
    font-size: 12px;
    color: var(--ash-soft);
    line-height: 1.45;
    margin-top: 5px;
  }}
  .ritual-net {{
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 6px 10px;
    border-radius: 8px;
    background: var(--white);
    border: 1px solid var(--line);
    white-space: nowrap;
    flex-shrink: 0;
  }}

  /* Main Linktree Stack */
  .link-group {{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}
  .link-item {{
    width: 100%;
    text-align: left;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    min-height: 60px;
    padding: 12px 14px;
    border-radius: 14px;
    background: var(--white);
    border: 1px solid var(--line);
    transition: transform 0.18s var(--ease), border-color 0.18s, background 0.18s;
  }}
  .link-item:hover {{
    border-color: var(--ash);
    background: var(--ivory);
    transform: translateY(-1px);
  }}
  .link-item:active {{ transform: scale(0.99); }}
  .link-left {{
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: 0;
  }}
  .link-icon {{
    width: 38px;
    height: 38px;
    border-radius: 10px;
    background: var(--ivory);
    border: 1px solid var(--line);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: var(--ash);
  }}
  .link-icon svg {{ width: 18px; height: 18px; }}
  .link-text {{ min-width: 0; }}
  .link-text strong {{
    display: block;
    font-size: 14px;
    font-weight: 500;
    color: var(--ash);
    line-height: 1.25;
  }}
  .link-text span {{
    display: block;
    font-size: 12px;
    color: var(--ash-soft);
    line-height: 1.38;
  }}
  .link-right {{
    color: var(--ash-soft);
    flex-shrink: 0;
    display: inline-flex;
    align-items: center;
    transition: transform 0.2s var(--ease);
  }}
  .link-item[aria-expanded="true"] .link-right {{
    transform: rotate(90deg);
  }}

  /* Expandable Story Drawer */
  .story-drawer {{
    display: none;
    background: var(--ivory);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 15px 16px;
    font-size: 13px;
    color: var(--ash-soft);
    line-height: 1.6;
  }}
  .story-drawer.open {{ display: block; }}
  .story-drawer p + p {{ margin-top: 8px; }}
  .story-drawer strong {{ color: var(--ash); font-weight: 500; }}

  /* Contact Row with Quick Copy */
  .contact-card {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    padding: 12px 14px;
    border-radius: 14px;
    background: var(--ivory);
    border: 1px solid var(--line);
  }}
  .contact-link {{
    display: flex;
    align-items: center;
    gap: 12px;
    flex: 1;
    min-width: 0;
    min-height: 44px;
  }}
  .copy-pill {{
    min-height: 40px;
    padding: 0 13px;
    border-radius: 999px;
    background: var(--white);
    border: 1px solid var(--line);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    flex-shrink: 0;
    transition: border-color 0.16s, background 0.16s;
  }}
  .copy-pill:hover {{ border-color: var(--ash); background: var(--ivory-card); }}

  /* Social Icon Row */
  .social-row {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    padding-top: 2px;
  }}
  .social-btn {{
    display: inline-flex;
    align-items: center;
    gap: 7px;
    min-height: 44px;
    padding: 0 16px;
    border-radius: 999px;
    background: var(--white);
    border: 1px solid var(--line);
    font-size: 12px;
    font-weight: 500;
    color: var(--ash);
    transition: border-color 0.16s, background 0.16s;
  }}
  .social-btn:hover {{ border-color: var(--ash); background: var(--ivory); }}

  /* Footer (Strictly Brand Only) */
  .foot {{
    padding-top: 14px;
    border-top: 1px solid var(--line);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    text-align: center;
  }}
  .foot-brand {{
    font-size: 12px;
    color: var(--ash);
    font-weight: 500;
    letter-spacing: 0.08em;
  }}
  .foot-sub {{
    font-size: 11.5px;
    color: var(--ash-soft);
  }}

  .toast {{
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%) translateY(14px);
    background: var(--ash-deep);
    color: var(--ivory);
    border: 1px solid var(--champagne);
    padding: 10px 18px;
    border-radius: 999px;
    font-size: 12.5px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s, transform 0.2s var(--ease);
    z-index: 50;
    white-space: nowrap;
  }}
  .toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}

  @media (min-width: 640px) {{
    body {{
      background: linear-gradient(180deg, #F3F0E9 0%, #EAE4DA 100%);
      padding: 40px 20px 56px;
    }}
    .sheet {{
      padding: 26px 26px 30px;
    }}
  }}
  @media (prefers-reduced-motion: reduce) {{
    *, *::before, *::after {{ transition: none !important; }}
  }}
</style>
</head>
<body>
  <div class="bg-orbit" aria-hidden="true">
    <svg viewBox="0 0 960 960" fill="none">
      <circle cx="480" cy="480" r="320" stroke="#C8B9A6" stroke-width="1"/>
      <circle cx="496" cy="468" r="410" stroke="#B8B7B1" stroke-width="0.9"/>
    </svg>
  </div>

  <main class="sheet">
    <!-- Top Bar -->
    <div class="top-bar">
      <a href="https://instagram.com/selun.ea" target="_blank" rel="noopener noreferrer" class="handle-pill">
        <svg viewBox="{mono_vb}" aria-hidden="true">{mono_inner}</svg>
        <span>@selun.ea</span>
      </a>
      <button type="button" class="share-btn" id="sharePageBtn" aria-label="Bagikan halaman SELUNÉA">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true">
          <path d="M12 5.5a2 2 0 1 0 0-4 2 2 0 0 0 0 4ZM4 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4ZM12 14.5a2 2 0 1 0 0-4 2 2 0 0 0 0 4ZM5.7 7l4.6-2.5M5.7 9l4.6 2.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
        </svg>
        <span>Share</span>
      </button>
    </div>

    <!-- Brand Header -->
    <header class="profile">
      <div class="avatar-ring">
        <div class="avatar-core">
          <svg viewBox="{mark_vb}" role="img" aria-label="SELUNÉA">{mark_inner}</svg>
        </div>
      </div>
      <svg viewBox="{wm_vb}" class="wm-lockup" role="img" aria-label="SELUNÉA">{wm_inner}</svg>
      <p class="tagline">“Beauty in Every Phase.”</p>
      <p class="bio">Skincare for every version of you. Perawatan kulit kontemporer yang lembut, tenang, dan konsisten untuk mendampingi setiap fase hari Anda.</p>
    </header>

    <!-- Primary Featured Link -->
    <a href="https://instagram.com/selun.ea" target="_blank" rel="noopener noreferrer" class="featured-link">
      <div class="featured-top">
        <span class="featured-kicker">Official Instagram · @selun.ea</span>
        <span class="featured-arrow" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
            <path d="M4 12 12 4M6 4h6v6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
      </div>
      <div class="featured-title">Follow &amp; Shop via @selun.ea</div>
      <div class="featured-sub">Kabar peluncuran rangkaian skincare terbaru, panduan ritual harian, &amp; pemesanan resmi.</div>
    </a>

    <!-- Interactive 5-Phase Daily Ritual Explorer -->
    <section class="ritual-card" aria-label="Rangkaian 5 Fase Perawatan Harian">
      <div class="section-mini-head">
        <span>The 5-Phase Daily Ritual</span>
        <span>5 Essentials</span>
      </div>
      <div class="phase-tabs" role="tablist" aria-label="Pilih fase produk SELUNÉA">
        {ritual_tabs}
      </div>
      <div class="ritual-detail" id="ritualPanel" role="tabpanel">
        <div>
          <small id="ritualPhase">Phase 01 · Cleanse</small>
          <strong id="ritualName">Facial Cleanser</strong>
          <span class="meta" id="ritualDesc">Langkah awal untuk membersihkan kulit dengan lembut tanpa rasa kering.</span>
        </div>
        <span class="ritual-net" id="ritualNet">120 mL</span>
      </div>
    </section>

    <!-- Customer Links Stack -->
    <nav class="link-group" aria-label="Tautan Resmi SELUNÉA">
      <a href="https://instagram.com/selun.ea" target="_blank" rel="noopener noreferrer" class="link-item">
        <div class="link-left">
          <span class="link-icon" style="background:var(--sage);" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
          </span>
          <div class="link-text">
            <strong>Konsultasi &amp; Order via DM Instagram</strong>
            <span>Hubungi tim kami langsung di @selun.ea</span>
          </div>
        </div>
        <span class="link-right" aria-hidden="true">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M6 3.5 10.5 8 6 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
      </a>

      <button type="button" class="link-item" id="storyToggleBtn" aria-expanded="false" aria-controls="storyDrawer">
        <div class="link-left">
          <span class="link-icon" style="background:var(--lavender);" aria-hidden="true">
            <svg viewBox="{mark_vb}" aria-hidden="true">{mark_inner}</svg>
          </span>
          <div class="link-text">
            <strong>Tentang SELUNÉA · Filosofi Kami</strong>
            <span>Kenali makna “Beauty in Every Phase.”</span>
          </div>
        </div>
        <span class="link-right" aria-hidden="true">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M6 3.5 10.5 8 6 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
      </button>

      <div class="story-drawer" id="storyDrawer">
        <p><strong>Terinspirasi dari fase bulan</strong> yang senantiasa berubah namun tetap utuh, SELUNÉA hadir untuk merayakan ritme alami kulit perempuan Indonesia di setiap fase kehidupan.</p>
        <p>Dengan pendekatan perawatan harian yang tenang dan konsisten—dari <em>Cleanse</em> hingga <em>Shield</em>—kami percaya merawat kulit adalah momen jeda yang sederhana namun bermakna setiap hari.</p>
      </div>

      <a href="https://selunea.com" target="_blank" rel="noopener noreferrer" class="link-item">
        <div class="link-left">
          <span class="link-icon" style="background:var(--nude);" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.6"/><path d="M4 12h16M12 3.5a12 12 0 0 1 0 17M12 3.5a12 12 0 0 0 0 17" stroke="currentColor" stroke-width="1.5"/></svg>
          </span>
          <div class="link-text">
            <strong>Official Website · selunea.com</strong>
            <span>Jelajahi cerita produk dan etalase resmi</span>
          </div>
        </div>
        <span class="link-right" aria-hidden="true">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M6 3.5 10.5 8 6 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
      </a>

      <!-- Customer Care Email with Quick Copy -->
      <div class="contact-card">
        <a href="mailto:hello@selunea.com" class="contact-link">
          <span class="link-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none"><rect x="3.5" y="5.5" width="17" height="13" rx="2.5" stroke="currentColor" stroke-width="1.6"/><path d="m4.5 7 7.5 5.5L19.5 7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <div class="link-text">
            <strong>Customer Care &amp; Kolaborasi</strong>
            <span>hello@selunea.com</span>
          </div>
        </a>
        <button type="button" class="copy-pill" id="copyEmailBtn">Copy</button>
      </div>
    </nav>

    <!-- Social Links -->
    <div class="social-row" aria-label="Kanal Resmi SELUNÉA">
      <a href="https://instagram.com/selun.ea" target="_blank" rel="noopener noreferrer" class="social-btn">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.7"/>
          <circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/>
          <circle cx="17.2" cy="6.8" r="1" fill="currentColor"/>
        </svg>
        <span>@selun.ea</span>
      </a>
      <a href="https://www.tiktok.com/@selun.ea" target="_blank" rel="noopener noreferrer" class="social-btn">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <path d="M14 4v10.5a3.5 3.5 0 1 1-2.6-3.38V8.1a6.5 6.5 0 1 0 5.6 6.4V9.2a6.2 6.2 0 0 0 3.5 1.1V7.2a3.8 3.8 0 0 1-3.5-3.2H14Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
        </svg>
        <span>TikTok</span>
      </a>
      <a href="https://selunea.com" target="_blank" rel="noopener noreferrer" class="social-btn">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.6"/>
          <path d="M3.5 12h17M12 3a13 13 0 0 1 0 18M12 3a13 13 0 0 0 0 18" stroke="currentColor" stroke-width="1.5"/>
        </svg>
        <span>Website</span>
      </a>
    </div>

    <!-- Brand-Only Footer -->
    <footer class="foot">
      <div class="foot-brand">© SELUNÉA</div>
      <div class="foot-sub">Beauty in Every Phase · Skincare for every version of you.</div>
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

  // 5-Phase Ritual Switcher
  const tabs = Array.from(document.querySelectorAll('.phase-tab'));
  const panel = document.getElementById('ritualPanel');
  const elPhase = document.getElementById('ritualPhase');
  const elName = document.getElementById('ritualName');
  const elDesc = document.getElementById('ritualDesc');
  const elNet = document.getElementById('ritualNet');

  tabs.forEach(btn => {{
    btn.addEventListener('click', () => {{
      tabs.forEach(t => {{
        const active = t === btn;
        t.classList.toggle('active', active);
        t.setAttribute('aria-selected', String(active));
      }});
      elPhase.textContent = `Phase ${{btn.dataset.phase}} · ${{btn.dataset.step}}`;
      elName.textContent = btn.dataset.name;
      elDesc.textContent = btn.dataset.desc;
      elNet.textContent = btn.dataset.net;
      panel.style.borderLeftColor = btn.dataset.tint;
    }});
  }});

  // Expandable Brand Philosophy Drawer
  const storyBtn = document.getElementById('storyToggleBtn');
  const storyDrawer = document.getElementById('storyDrawer');
  storyBtn.addEventListener('click', () => {{
    const isOpen = storyDrawer.classList.toggle('open');
    storyBtn.setAttribute('aria-expanded', String(isOpen));
  }});

  // Copy Email
  document.getElementById('copyEmailBtn').addEventListener('click', async () => {{
    try {{ await navigator.clipboard.writeText('hello@selunea.com'); }} catch (e) {{}}
    showToast('Email hello@selunea.com tersalin');
  }});

  // Share Page
  document.getElementById('sharePageBtn').addEventListener('click', async () => {{
    const url = window.location.href;
    if (navigator.share) {{
      try {{
        await navigator.share({{
          title: 'SELUNÉA — Beauty in Every Phase.',
          text: 'Skincare for every version of you.',
          url
        }});
        return;
      }} catch (e) {{}}
    }}
    try {{ await navigator.clipboard.writeText(url); }} catch (e) {{}}
    showToast('Tautan SELUNÉA tersalin');
  }});
</script>
</body>
</html>
"""
    out = BASE / "links.html"
    out.write_text(html, encoding="utf-8")
    print(f"Built customer-facing SELUNÉA Linktree page: {out} ({out.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build_linktree()
