# SELUNÉA — Complete Brand Identity Handover & Asset Inventory

**Brand:** SELUNÉA · *"Beauty in Every Phase."* · *"Skincare for every version of you."*  
**Creative Direction:** Lunar Elegance (High-Contrast Couture Editorial Sans + Tri-Phase Lunar Geometry)  
**Status:** Production-Ready Identity Kit (Stages 1–9 Completed & Validated)

---

## Folder Directory & Key Deliverables

| Folder | Contents |
|---|---|
| `01-brand-strategy/` | [01-creative-direction.md](01-brand-strategy/01-creative-direction.md) — Strategic brief, Lunar Elegance pillars, WCAG color hierarchy, typography direction |
| `02-research/` | [01-skill-repository-inspection.md](02-research/01-skill-repository-inspection.md) · [02-initial-visual-research.md](02-research/02-initial-visual-research.md) · [03-concept-longlist-and-direction.md](02-research/03-concept-longlist-and-direction.md) |
| `03-moodboard/` | [01-lunar-elegance-moodboard.png](03-moodboard/01-lunar-elegance-moodboard.png) · `.html` — Tactile surfaces, color ratio, live font specimens & Stage 3 roadmap |
| `04-logo-concepts/` | Full iterative history (`v1`→`v4`), [selunea-concepts-overview-v4.png](04-logo-concepts/selunea-concepts-overview-v4.png), [preview-stress-test.html](04-logo-concepts/preview-stress-test.html), [00-concept-comparison-and-rationale.md](04-logo-concepts/00-concept-comparison-and-rationale.md) |
| `05-logo-final/` | **Master Vector Suite (`svg/`):** Primary Wordmark, Secondary Skincare Logo, Tri-Phase Lunar Brand Mark, Celestial `S` Monogram, Horizontal Lockup, Stacked Lockup, Small-Size Responsive cuts, Black, Irradiation-Thinned White, Champagne, Midnight Ash · **Transparent High-Res PNGs (`png/`):** 1024–1600 px · **Complete Web/PWA Icons (`web-icons/`):** `favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `icon-192/512`, `maskable-512`, `site.webmanifest`, `head-snippet.html` |
| `06-color-typography/` | [01-design-tokens.json](06-color-typography/01-design-tokens.json) · [02-design-tokens.css](06-color-typography/02-design-tokens.css) · [03-color-typography-board.png](06-color-typography/03-color-typography-board.png) |
| `07-graphic-assets/` | Reusable vector assets: `lunar-phase-divider.svg`, `orbital-frame-accent.svg`, `phase-pattern-tile.svg`, `pearl-luminosity-backdrop.svg` |
| `08-packaging/` | [01-skincare-packaging-family.png](08-packaging/01-skincare-packaging-family.png) · `.pdf` · `.html` — Coherent 5-SKU family (Cleanser, Toner, Serum, Moisturizer, Sunscreen), Folding Cartons & Blind-Deboss/Foil Cap Seals |
| `09-brand-applications/` | [01-stationery-and-collateral.png](09-brand-applications/01-stationery-and-collateral.png) (Business cards, Thank-You card, Ritual Insert, Shopping Bag, Tissue Paper, Stickers, Mailer Box) · [02-social-and-digital.png](09-brand-applications/02-social-and-digital.png) (Instagram profile/feed/stories, Storefront Hero + 5-SKU Listing, Art Direction rules) |
| `10-brand-guidelines/` | **[selunea-brand-guidelines.pdf](10-brand-guidelines/selunea-brand-guidelines.pdf)** · `.html` — Complete 15-section client-grade Brand Identity Guidelines (7-page A4 landscape editorial manual) |
| `11-presentations/` | **[selunea-client-presentation.pdf](11-presentations/selunea-client-presentation.pdf)** · `.html` · `slides/slide-01..05.png` — Client presentation deck with 6 retail/beauty mockups |
| `12-source-files/` | Reproducible parametric Python vector & board generators (`build_stage3_concepts.py`, `build_stage3_concepts_v4_editorial_sans.py`, `build_stage5_logo_system.py`, `build_stage6_7_8_boards.py`) |

---

## Final Validation & Pre-Production Notes

1. **Vector Purity (`svg_audit.py`):** Zero `<text>` tags, zero `<filter>` effects, zero embedded rasters, zero fake white knockouts. Brand Mark = **100/100** (9 anchors), Monogram S = **100/100** (21 anchors), Small Responsive Mark = **100/100**, Primary Wordmark & Lockups = **91–92/100**.
2. **Optical & Print Craft:** Includes dedicated **irradiation-thinned white reversed artwork** (~4% thinned for dark surfaces) and **small-size responsive wordmark & favicon mark** for 30 mL serum bottles and 16 px browser tabs.
3. **Typography Licensing:** `Cormorant Garamond` and `DM Sans` are SIL Open Font License 1.1 (safe for commercial branding, print, and web). Final logo wordmarks are 100% custom outlined vector paths.
4. **Required Client Actions Before Launch:**
   - Conduct a formal legal **trademark search** (local/regional Class 3 cosmetics registry + reverse image search).
   - Approve physical **Pantone swatch drawdowns, frosted glass silkscreen tests, and satin champagne hot-foil press proofs** with your packaging supplier prior to mass production.
