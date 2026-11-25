# Logo Design Skill — Repository & Environment Inspection Report

**Project:** SELUNÉA — Complete Brand Identity Development  
**Stage:** Stage 1 — Repository Inspection & Brand Research  
**Skill Path:** `C:\Users\ridwa\.gemini\config\skills\logo-design`  
**Inspection Date:** 2026-11-25

---

## 1. Installation Requirements & Local Environment Status

The `logo-design` skill is architected as a **dependency-free Python 3 toolkit** paired with structured brand-design reference manuals and a local reference catalog.

| Requirement | Status on This Machine | Details / Notes |
|---|---|---|
| **Python 3** | Installed & Ready | `Python 3.14.2` (64-bit Windows) — use `python` on Windows (not `python3` store stub) |
| **SVG → PNG / HTML Renderer** | Ready (`chrome`) | `C:\Program Files\Google\Chrome\Application\chrome.exe` detected by `render_png.py --which` |
| **Pillow (`PIL`)** | Installed | Supports image manipulation and `favicon.ico` / PNG operations |
| **Optional Native Vector/PDF CLIs** | Not installed | `cairosvg`, `rsvg-convert`, `inkscape`, `magick`, `reportlab`, `weasyprint` are not installed |
| **PDF Export Strategy** | Ready via Headless Chrome | Chrome supports `--headless --print-to-pdf` from HTML/SVG for vector-sharp PDF presentation boards, logo sheets, and brand guidelines |
| **Local Brand Fonts** | Not installed locally | None of `Cormorant Garamond`, `Bodoni Moda`, `Instrument Serif`, `DM Sans`, or `Manrope` are installed in `Windows\Fonts` yet. For final vector logos, letterforms must be constructed/converted to **pure SVG `<path>` outlines** (no live `<text>`). For HTML presentations & guidelines, Google Fonts / SIL OFL webfonts can be loaded or bundled. |

**Conclusion:** Zero additional installation is required to execute Stages 1–9 cleanly, including SVG validation, transparent PNG rendering, multi-slide presentation boards, web/favicon sets, and Chrome-rendered PDF exports.

---

## 2. Available Workflow (Skill Methodology vs. SELUNÉA 9-Stage Plan)

The `logo-design` skill operates on a disciplined 7-phase agency workflow with a strict **Concept Checkpoint**:

| Skill Phase | Activity | Mapped to SELUNÉA Stage |
|---|---|---|
| **Phase 1 — Discovery → Brief** | Audience, adjectives, competitive frame, constraints, explicit assumptions | Stage 1 (Brand Strategy & Research) |
| **Phase 2 — Research & Strategy** | Category conventions, clichés to ban, word mapping, mark-type selection | Stage 1 & Stage 2 (Creative Direction & Moodboard) |
| **Phase 3 — Concepts** | 8–12 one-sentence ideas → shortlist 3 genuinely distinct visual concepts | Stage 3 (Generate 3 Logo Concepts) |
| **Phase 4 — Build in SVG (Black First)** | Construction specs first, clean `viewBox="0 0 256 256"`, solid black on white, outlined paths only | Stage 3 (Vector Construction) |
| **Phase 5 — Test & Refine (≥2 loops)** | `svg_audit.py`, `preview_sheet.py` (16–24 px scale, squint, mirror, 180°, shelf test, optical fixes) | Stage 3 & Stage 4 (QA & Comparison) |
| **Phase 6 — Concept Checkpoint (STOP)** | Greyscale `concept_sheet.py` + rationale → **wait for client approval** | Stage 4 (Present & Wait for Approval) |
| **Phase 7 — Build Complete Kit** | Final optical refinement, color system, lockups, responsive small-size cut, presentation boards, variants, brand guidelines | Stages 5–9 (Refinement, Identity, Packaging, Guidelines, Export) |

Both `selenua.md` and `logo-design` strictly prohibit finalizing logos or generating packaging/brand kits before concept approval.

---

## 3. Available Scripts (`scripts/`)

All 9 Python scripts are standalone and verified:

| Script | Primary Role | Key Flags / Capabilities |
|---|---|---|
| `search_library.py` | Query the 1,432-SVG reference library | `--type`, `--technique`, `--geometry`, `--subject`, `--industry`, `--type-style`, `--case`, `--mood`, `--exemplary`, `--summary`, `--format table/paths` |
| `svg_audit.py` | Automated vector QA & compliance scoring | Checks `viewBox`, `<title>`, live `<text>`, rasters, filters, color count, gradients, unexpanded strokes, white "fake knockouts", near-miss angles (0.3–3°), tiny details, viewBox padding/centering, complexity vs. library, and `--bg "#HEX"` contrast |
| `render_png.py` | Render SVGs to transparent PNGs & screenshot HTML | Uses headless Chrome (`--size`, `--width`, `--height`, `--padding`, `--bg`), batch `--out-dir`, `--ico` multi-size `favicon.ico`, and HTML page screenshots |
| `concept_sheet.py` | Generate single-page concept comparison board | Renders large mark + lockup + true `64 / 32 / 16 px` scale tests, titles, one-line ideas, recommendation badge, and `--greyscale` mode (outputs `.svg` + `.png`) |
| `preview_sheet.py` | Comprehensive visual stress-test HTML sheet | Size ladder (16 px upward), pixel-level favicon test, light/dark/brand/photo/pattern backgrounds, greyscale, mono B&W, squint blur, mirror, 180° rotation, browser tab / app icon / avatar / header / card contexts, side-by-side & competitor shelf test (`--refs`) |
| `presentation_board.py` | Client-ready HTML presentation deck (+ PNG slides) | Driven by JSON spec; supports 17 built-in mockups (`shopping-bag`, `box`, `business-card`, `website`, `social`, `tote`, `signage`, `sticker`, `app-icon`, `favicon-tab`, etc.) and `--png-dir` slide export |
| `export_variants.py` | Production logo asset pipeline from master SVG | Outputs `-black.svg`, `-white.svg`, `-mono-<hex>.svg`, `-square.svg`, `-favicon.svg`, `-app-icon.svg`, multi-size transparent PNGs (`--png`), and full `--web-icons` PWA set (`favicon.ico`, `apple-touch-icon.png`, `icon-192/512`, `maskable-512`, `site.webmanifest`, `head-snippet.html`) with `--favicon-source` & `--optical-offset` |
| `svglib.py` | Shared SVG parsing & geometry library | Internal helper used across audit, rendering, and export scripts |
| `build_catalog.py` | Library catalog maintainer | Rebuilds `catalog.json` / `stats.json` (maintainer use only) |

---

## 4. Reference Libraries & Templates

### A. Reference Library (`assets/library/`)
- **Total Files:** **1,432 real-world SVG logos** (~1,200 brands; 233 brands include paired full lockup + standalone `-icon` symbol).
- **Files:** `svg/`, `catalog.json` (911 KB), `classifications.json` (593 KB), `stats.json`, and `gallery.html` (interactive local browser).
- **Exemplary Marks:** 141 curated high-craft marks flagged `exemplary` for construction study.
- **Important Bias Note:** The catalog skews heavily toward technology brands (developer tools, frameworks, cloud, data). Skincare/beauty is not a dedicated industry tag; therefore, for SELUNÉA we query the library by **subject, technique, typography, and geometry** (`moon`, `crescent`, `orbit`, `serif`, `negative-space`, `letterform S`, `geometric-construction`) while supplying domain-specific contemporary skincare intelligence externally.
- **Usage Rule:** Reference trademarks are for **structural study and originality checking only** — never copy, trace, or adapt.

### B. Design Knowledge Base (`references/` — 14 manuals)
Covers: `principles.md`, `discovery-brief.md`, `mark-types.md`, `visual-techniques.md`, `color.md`, `typography.md`, `process.md`, `svg-construction.md`, `testing-checklist.md`, `presentation-delivery.md`, `identity-system.md`, `redesign.md`, `critique.md`, and `library-guide.md`.

### C. Templates (`templates/`)
- `brand-guidelines-template.md` — concise brand guideline scaffold (to be expanded into SELUNÉA's full 15-section client-grade brand guideline in Stage 8).
- `presentation-spec.example.json` — spec schema for `presentation_board.py`.

---

## 5. Supported Output Formats

| Format | Generation Method | Intended Deliverables |
|---|---|---|
| **Master SVG (`.svg`)** | Hand-authored clean vector geometry (outlined paths, explicit `viewBox`, no filters/rasters) | Concept proofs, final primary/secondary/mark/monogram/responsive/B&W/mono/reversed masters |
| **Transparent PNG (`.png`)** | `render_png.py` & `export_variants.py --png` via headless Chrome | High-res transparent exports (512 px, 1024 px, 2048 px), social avatars, slide images |
| **Web & App Icons (`.ico`, `.png`, `.webmanifest`)** | `export_variants.py --web-icons` | `favicon.ico` (16/32/48), `favicon.svg`, Apple touch icon (180), PWA icons (192/512/maskable) |
| **Interactive HTML (`.html`)** | `preview_sheet.py`, `presentation_board.py`, custom editorial sheets | Visual QA sheets, moodboards, packaging family showcases, presentation decks |
| **Vector-Backed PDF (`.pdf`)** | Headless Chrome `--print-to-pdf` from print-formatted HTML/SVG sheets | Print-ready logo proof sheets, client presentation PDFs, and the 15-section SELUNÉA Brand Guideline PDF |

---

## 6. Validation & Quality Control Capabilities

1. **Automated Structural Audit (`svg_audit.py`):**
   - Enforces zero live `<text>`, zero embedded rasters, zero SVG `<filter>` dependencies.
   - Detects unexpanded strokes, white fake-knockout shapes (ensuring real `fill-rule="evenodd"` holes), near-miss angles (0.3°–3° off clean axes), sub-threshold tiny details (< ~1/48 of mark), and canvas centering/padding.
   - Benchmarks anchor-point economy against the 1,432-logo dataset (square symbol median: 53 anchors; p25: 31 anchors — target low anchor count for high craft).
   - Verifies color contrast against any target surface via `--bg "#HEX"`.
2. **Visual Stress Testing (`preview_sheet.py` + Chrome Rendering + Visual Inspection):**
   - Mandatory visual inspection of every rendered PNG before presenting (never drawing SVG blind).
   - True 16 px / 24 px / 32 px legibility tests, squint-blur silhouette test, mirror & 180° rotation test (catching unintended shapes/tilts), dark/light/photo/pattern surface checks, and peer/competitor shelf test.
3. **Craft & Packaging Readiness Checks:**
   - Foil-stamp / emboss / silkscreen feasibility on frosted glass and matte ivory tubes/cartons (minimum stroke weight & counter clearance).
   - Optical corrections (round/pointed overshoot ~1–3%, optical centering, horizontal thinning, irradiation-compensated reversed white version).
   - Mandatory client advisory: automated tools cannot guarantee legal trademark clearance or physical Pantone/foil press accuracy — professional trademark search and physical press proofs remain required before production.
