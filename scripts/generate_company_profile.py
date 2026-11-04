import os
import json
import base64

OUTPUT_HTML = "/opt/data/cache/scratch/altakamul-site/profile.html"
OUTPUT_HTML_ALT = "/opt/data/cache/scratch/altakamul-site/company-profile.html"
OUTPUT_CSS = "/opt/data/cache/scratch/altakamul-site/css/profile.css"
PDF_DIR = "/opt/data/cache/scratch/altakamul-site/pdf"
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs("/opt/data/cache/scratch/altakamul-site/css", exist_ok=True)

# CSS Content
CSS_CONTENT = """/* ==========================================================================
   Al Takamul International Trading LLC - Company Profile & Executive Dossier
   Typography: Peyda (Headings) & IRANSansX (Body)
   Theme: Light & Dark | Optimized for Screen & A4 Print
   Doc Ref: DOC: TK-CORP-2026/V1
   ========================================================================== */

/* 1. LOCAL FONTS */
@font-face {
  font-family: 'Peyda';
  src: url('../fonts/PeydaWebFaNum-Regular.woff2') format('woff2'),
       url('../fonts/PeydaFaNum-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Peyda';
  src: url('../fonts/PeydaWebFaNum-Bold.woff2') format('woff2'),
       url('../fonts/PeydaFaNum-Bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'IRANSansX';
  src: url('../fonts/IRANSansXFaNum-Regular.woff2') format('woff2'),
       url('../fonts/IRANSansXFaNum-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'IRANSansX';
  src: url('../fonts/IRANSansXFaNum-Bold.woff2') format('woff2'),
       url('../fonts/IRANSansXFaNum-Bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

/* 2. DESIGN TOKENS */
:root {
  --color-primary: #025F73;
  --color-primary-hover: #0388A6;
  --color-primary-dark: #013D4A;
  --color-primary-subtle: rgba(2, 95, 115, 0.08);
  --color-primary-border: rgba(2, 95, 115, 0.22);

  --color-accent: #C5A059;
  --color-accent-hover: #B38E46;
  --color-accent-subtle: rgba(197, 160, 89, 0.12);

  --bg-page: #F4F7F9;
  --bg-card: #FFFFFF;
  --bg-card-subtle: #F8FAFB;
  --bg-dark: #01242D;
  --bg-dark-card: #043542;

  --text-main: #141E24;
  --text-muted: #4A5B66;
  --text-dim: #7A8E99;
  --text-inverse: #FFFFFF;

  --border-subtle: #E2E8EC;
  --border-strong: #CBD5DC;

  --font-heading: 'Peyda', 'Segoe UI', system-ui, -apple-system, sans-serif;
  --font-body: 'IRANSansX', 'Segoe UI', system-ui, -apple-system, sans-serif;

  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-full: 9999px;

  --shadow-sm: 0 2px 6px rgba(2, 95, 115, 0.05);
  --shadow-md: 0 6px 18px rgba(2, 95, 115, 0.08);
  --shadow-lg: 0 14px 28px rgba(2, 95, 115, 0.12);
}

[data-theme="dark"] {
  --bg-page: #060D11;
  --bg-card: #0C171E;
  --bg-card-subtle: #11222C;
  --text-main: #F4F7F9;
  --text-muted: #9BB0BD;
  --text-dim: #647B88;
  --border-subtle: #192D38;
  --border-strong: #264353;
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.4);
}

/* 3. BASE STYLES */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
}

html, body {
  background-color: var(--bg-page);
  color: var(--text-main);
  font-family: var(--font-body);
  direction: rtl;
  text-align: right;
  line-height: 1.6;
}

/* 4. EXECUTIVE CONTROL BAR (SCREEN ONLY) */
.executive-control-bar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(1, 36, 45, 0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(197, 160, 89, 0.3);
  padding: 12px 24px;
  color: #FFFFFF;
}

.control-bar-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}

.control-brand-info {
  display: flex;
  align-items: center;
  gap: 14px;
}

.control-doc-tag {
  font-family: var(--font-heading);
  font-size: 0.8rem;
  letter-spacing: 0.5px;
  background: rgba(197, 160, 89, 0.15);
  color: var(--color-accent);
  border: 1px solid rgba(197, 160, 89, 0.35);
  padding: 3px 10px;
  border-radius: var(--radius-full);
}

.control-meta-text {
  font-size: 0.85rem;
  color: #CBD5DC;
}

.control-actions {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.btn-ctrl {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-body);
  font-size: 0.85rem;
  font-weight: 700;
  padding: 8px 16px;
  border-radius: var(--radius-md);
  text-decoration: none;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid transparent;
}

.btn-ctrl-primary {
  background: var(--color-accent);
  color: #01242D;
}

.btn-ctrl-primary:hover {
  background: var(--color-accent-hover);
  transform: translateY(-1px);
}

.btn-ctrl-outline {
  background: rgba(255, 255, 255, 0.08);
  color: #FFFFFF;
  border-color: rgba(255, 255, 255, 0.2);
}

.btn-ctrl-outline:hover {
  background: rgba(255, 255, 255, 0.15);
}

.btn-theme-toggle {
  width: 38px;
  height: 38px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-md);
  color: #FFFFFF;
  cursor: pointer;
  font-size: 1rem;
}

/* 5. A4 PROFILE WRAPPER & SHEETS */
.profile-document-container {
  max-width: 1000px;
  margin: 32px auto 64px auto;
  padding: 0 16px;
  display: flex;
  flex-direction: column;
  gap: 36px;
}

.profile-page {
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--border-subtle);
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  padding: 44px 48px 36px 48px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 1120px;
}

/* 6. RUNNING PAGE HEADERS & FOOTERS */
.page-running-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 14px;
  margin-bottom: 24px;
  font-size: 0.8rem;
  color: var(--text-dim);
}

.page-running-header .header-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  color: var(--color-primary);
  font-weight: 700;
  font-family: var(--font-heading);
}

.page-running-header .header-logo-icon {
  width: 24px;
  height: 24px;
  object-fit: contain;
}

.page-running-header .header-doc-code {
  font-family: var(--font-heading);
  letter-spacing: 0.5px;
}

.page-running-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--border-subtle);
  padding-top: 14px;
  margin-top: 24px;
  font-size: 0.78rem;
  color: var(--text-dim);
}

.page-running-footer .footer-cr {
  font-family: var(--font-body);
}

.page-running-footer .footer-confidential {
  color: var(--color-accent);
  font-weight: 700;
}

.page-running-footer .page-number {
  font-family: var(--font-heading);
  font-weight: 700;
  background: var(--bg-card-subtle);
  padding: 3px 10px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
}

/* 7. PAGE 1: COVER HERO (FULL BLEED PRESTIGE) */
.page-cover {
  background: linear-gradient(135deg, #011E26 0%, #01313D 45%, #024756 100%);
  color: #FFFFFF;
  border: 1px solid rgba(197, 160, 89, 0.3);
  padding: 60px 54px 44px 54px;
  position: relative;
  min-height: 1120px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.cover-decor-ring {
  position: absolute;
  top: -60px;
  left: -60px;
  width: 280px;
  height: 280px;
  border: 1.5px solid rgba(197, 160, 89, 0.25);
  border-radius: 50%;
  pointer-events: none;
}

.cover-decor-ring-inner {
  position: absolute;
  top: 25px;
  left: 25px;
  width: 230px;
  height: 230px;
  border: 1px dashed rgba(197, 160, 89, 0.15);
  border-radius: 50%;
  pointer-events: none;
}

.cover-decor-diamond {
  position: absolute;
  bottom: 120px;
  right: -30px;
  width: 140px;
  height: 140px;
  border: 1.5px solid rgba(197, 160, 89, 0.2);
  transform: rotate(45deg);
  pointer-events: none;
}

.cover-header-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  z-index: 2;
}

.cover-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(197, 160, 89, 0.15);
  color: var(--color-accent);
  border: 1px solid rgba(197, 160, 89, 0.4);
  padding: 6px 16px;
  border-radius: var(--radius-full);
  font-size: 0.85rem;
  font-weight: 700;
  font-family: var(--font-heading);
}

.pulse-dot {
  width: 8px;
  height: 8px;
  background: #10B981;
  border-radius: 50%;
  box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
  animation: pulseGreen 2s infinite;
}

@keyframes pulseGreen {
  0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
  70% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
  100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

.cover-logo-wrapper {
  background: #FFFFFF;
  padding: 8px 16px;
  border-radius: var(--radius-md);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
  display: inline-flex;
  align-items: center;
}

.cover-logo-img {
  height: 48px;
  width: auto;
  object-fit: contain;
}

.cover-body-center {
  position: relative;
  z-index: 2;
  margin: 60px 0;
}

.cover-category-tag {
  color: var(--color-accent);
  font-family: var(--font-heading);
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: 0.8px;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.cover-title {
  font-family: var(--font-heading);
  font-size: 3rem;
  font-weight: 700;
  line-height: 1.25;
  color: #FFFFFF;
  margin-bottom: 22px;
}

.cover-title span {
  color: var(--color-accent);
}

.cover-desc {
  font-size: 1.15rem;
  line-height: 1.8;
  color: #D1DEE5;
  max-width: 720px;
  margin-bottom: 36px;
}

.cover-pillars-strip {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-top: 20px;
}

.cover-pillar-card {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  backdrop-filter: blur(8px);
}

.cover-pillar-card h4 {
  font-family: var(--font-heading);
  font-size: 0.95rem;
  color: var(--color-accent);
  margin-bottom: 6px;
}

.cover-pillar-card p {
  font-size: 0.8rem;
  line-height: 1.5;
  color: #C0D0D9;
}

.cover-footer-meta {
  border-top: 1px solid rgba(255, 255, 255, 0.15);
  padding-top: 24px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  position: relative;
  z-index: 2;
}

.cover-meta-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.cover-meta-lbl {
  font-size: 0.75rem;
  color: #94A9B5;
  text-transform: uppercase;
}

.cover-meta-val {
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 700;
  color: #FFFFFF;
}

/* 8. COMMON SECTION TYPOGRAPHY & CHIPS */
.section-chapter-chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-heading);
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--color-primary);
  background: var(--color-primary-subtle);
  border: 1px solid var(--color-primary-border);
  padding: 4px 12px;
  border-radius: var(--radius-full);
  margin-bottom: 10px;
}

.page-title {
  font-family: var(--font-heading);
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--color-primary-dark);
  line-height: 1.35;
  margin-bottom: 8px;
}

[data-theme="dark"] .page-title {
  color: #FFFFFF;
}

.page-subtitle {
  font-size: 0.92rem;
  color: var(--text-muted);
  line-height: 1.65;
  margin-bottom: 22px;
}

/* 9. GRIDS & CARDS (PAGE CONTENT) */
.page-content-flow {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  gap: 18px;
}

.card-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.card-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

.card-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.feature-box {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  position: relative;
}

.feature-box.featured-gold {
  border-color: rgba(197, 160, 89, 0.4);
  background: rgba(197, 160, 89, 0.04);
}

.feature-box-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}

.feature-icon-badge {
  width: 32px;
  height: 32px;
  border-radius: var(--radius-sm);
  background: var(--color-primary-subtle);
  color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
}

.featured-gold .feature-icon-badge {
  background: var(--color-accent-subtle);
  color: var(--color-accent);
}

.feature-box-title {
  font-family: var(--font-heading);
  font-size: 0.98rem;
  font-weight: 700;
  color: var(--text-main);
}

.feature-box-desc {
  font-size: 0.84rem;
  color: var(--text-muted);
  line-height: 1.6;
}

/* 10. UNIFORM SERVICES MATRIX (PAGE 4) */
.services-matrix-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.service-matrix-item {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 14px 18px;
  display: grid;
  grid-template-columns: 90px 1.2fr 1.6fr 1fr;
  align-items: center;
  gap: 16px;
}

.srv-code-badge {
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 700;
  background: var(--color-primary);
  color: #FFFFFF;
  text-align: center;
  padding: 6px 10px;
  border-radius: var(--radius-sm);
}

.srv-name-col {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.srv-title {
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--color-primary-dark);
}

[data-theme="dark"] .srv-title {
  color: #FFFFFF;
}

.srv-en-title {
  font-size: 0.75rem;
  color: var(--text-dim);
  font-family: var(--font-body);
}

.srv-scope-text {
  font-size: 0.82rem;
  color: var(--text-muted);
  line-height: 1.5;
}

.srv-deliverable-box {
  background: #FFFFFF;
  border: 1px solid rgba(197, 160, 89, 0.35);
  border-radius: var(--radius-sm);
  padding: 8px 12px;
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--text-main);
}

[data-theme="dark"] .srv-deliverable-box {
  background: var(--bg-card);
}

.srv-deliverable-box strong {
  color: var(--color-accent);
  display: block;
  font-size: 0.72rem;
  margin-bottom: 2px;
  text-transform: uppercase;
}

/* 11. CHECKLIST AND BULLETS */
.bullet-list-check {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 8px;
}

.bullet-list-check li {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-size: 0.84rem;
  color: var(--text-muted);
  line-height: 1.5;
}

.bullet-list-check li::before {
  content: "✓";
  color: var(--color-accent);
  font-weight: 700;
  font-family: var(--font-heading);
  background: var(--color-accent-subtle);
  width: 18px;
  height: 18px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  flex-shrink: 0;
  margin-top: 2px;
}

/* 12. STEP PIPELINE (PAGE 6) */
.pipeline-steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

.pipeline-step-card {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 14px 16px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.step-phase-badge {
  font-family: var(--font-heading);
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--color-accent);
  background: var(--color-accent-subtle);
  display: inline-block;
  padding: 2px 8px;
  border-radius: var(--radius-sm);
  width: fit-content;
}

.step-title {
  font-family: var(--font-heading);
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--text-main);
}

.step-desc {
  font-size: 0.8rem;
  color: var(--text-muted);
  line-height: 1.5;
}

/* 13. SIGNATORY BLOCK (PAGE 7) */
.signatory-box-grid {
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  gap: 20px;
  margin-top: 14px;
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 20px;
}

.seal-stamp-box {
  border: 2px dashed rgba(197, 160, 89, 0.4);
  border-radius: var(--radius-md);
  background: rgba(197, 160, 89, 0.03);
  padding: 16px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 140px;
}

.seal-icon-svg {
  width: 44px;
  height: 44px;
  color: var(--color-accent);
}

.seal-title {
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--color-accent);
}

.seal-sub {
  font-size: 0.72rem;
  color: var(--text-dim);
}

/* 14. METRICS ROW & HIGHLIGHT BOX */
.metrics-row-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 12px;
}

.metric-stat-card {
  background: var(--color-primary-subtle);
  border: 1px solid var(--color-primary-border);
  border-radius: var(--radius-md);
  padding: 14px 16px;
  text-align: center;
}

.metric-val {
  font-family: var(--font-heading);
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--color-primary);
  line-height: 1.2;
}

.metric-lbl {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 4px;
}

/* 15. CALLOUT NOTICE */
.legal-callout-notice {
  background: rgba(2, 95, 115, 0.04);
  border-right: 4px solid var(--color-primary);
  padding: 12px 16px;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  font-size: 0.82rem;
  line-height: 1.6;
  color: var(--text-muted);
}

.legal-callout-notice strong {
  color: var(--color-primary-dark);
}

/* 16. PRINT OPTIMIZATION (EXACT A4 MEDIA PRINT) */
@media print {
  @page {
    size: A4 portrait;
    margin: 0;
  }

  html, body {
    background: #FFFFFF !important;
    color: #141E24 !important;
    font-size: 11pt;
    width: 210mm;
    margin: 0;
    padding: 0;
  }

  .no-print, .executive-control-bar {
    display: none !important;
  }

  .profile-document-container {
    max-width: 210mm !important;
    margin: 0 !important;
    padding: 0 !important;
    gap: 0 !important;
  }

  .profile-page {
    width: 210mm !important;
    height: 297mm !important;
    max-height: 297mm !important;
    min-height: 297mm !important;
    box-sizing: border-box !important;
    padding: 16mm 18mm 14mm 18mm !important;
    margin: 0 !important;
    border-radius: 0 !important;
    border: none !important;
    box-shadow: none !important;
    page-break-after: always !important;
    break-after: page !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    overflow: hidden !important;
    background: #FFFFFF !important;
    position: relative !important;
  }

  .page-cover {
    background: linear-gradient(135deg, #011E26 0%, #01313D 45%, #024756 100%) !important;
    color: #FFFFFF !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    padding: 22mm 20mm 18mm 20mm !important;
  }

  .cover-pillar-card, .cover-badge, .cover-decor-ring, .cover-decor-diamond {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  .srv-code-badge, .metric-stat-card, .feature-icon-badge, .pulse-dot {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  .page-running-header {
    margin-bottom: 16px !important;
  }

  .page-running-footer {
    margin-top: 16px !important;
  }
}

/* 17. RESPONSIVE (MOBILE & TABLET SCREEN) */
@media (max-width: 820px) {
  .executive-control-bar {
    padding: 10px 14px;
  }

  .control-brand-info {
    font-size: 0.75rem;
  }

  .control-actions .btn-ctrl span {
    display: none;
  }

  .profile-page {
    padding: 24px 20px 20px 20px;
    min-height: auto;
  }

  .page-cover {
    padding: 36px 20px 24px 20px;
    min-height: auto;
  }

  .cover-title {
    font-size: 2rem;
  }

  .cover-pillars-strip {
    grid-template-columns: 1fr;
  }

  .cover-footer-meta {
    grid-template-columns: repeat(2, 1fr);
  }

  .card-grid-2, .card-grid-3, .card-grid-4, .pipeline-steps-grid {
    grid-template-columns: 1fr !important;
  }

  .service-matrix-item {
    grid-template-columns: 1fr !important;
    gap: 8px;
  }

  .signatory-box-grid {
    grid-template-columns: 1fr !important;
  }

  .metrics-row-4 {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}
"""

with open(OUTPUT_CSS, "w", encoding="utf-8") as f:
    f.write(CSS_CONTENT)

print(f"Generated CSS at: {OUTPUT_CSS}")
