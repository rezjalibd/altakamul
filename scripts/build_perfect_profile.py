import os
import json

OUTPUT_HTML = "/opt/data/cache/scratch/altakamul-site/profile.html"
OUTPUT_HTML_ALT = "/opt/data/cache/scratch/altakamul-site/company-profile.html"
OUTPUT_CSS = "/opt/data/cache/scratch/altakamul-site/css/profile.css"
PDF_PATH = "/opt/data/cache/scratch/altakamul-site/pdf/Al-Takamul-Company-Profile-2026.pdf"
PDF_ROOT_PATH = "/opt/data/cache/scratch/altakamul-site/Al-Takamul-Company-Profile-2026.pdf"

# Master CSS for Company Profile
CSS_CODE = """/* ==========================================================================
   Al Takamul International Trading LLC - Master Executive Profile Stylesheet
   Designed for High-End Digital Screen & Pixel-Perfect Vector A4 Print
   Fonts: Peyda (Titles) & IRANSansX (Body)
   Colors: #025F73 (Petrol Marine) | #C5A059 (Prestige Gold) | #01242D (Deep Slate)
   ========================================================================== */

/* 1. TYPOGRAPHY (LOCAL EMBED) */
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

  --bg-page: #F6F9FA;
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

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-full: 9999px;

  --shadow-sm: 0 2px 6px rgba(2, 95, 115, 0.06);
  --shadow-md: 0 6px 18px rgba(2, 95, 115, 0.08);
  --shadow-lg: 0 16px 32px rgba(2, 95, 115, 0.12);
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

/* 3. RESET & BASE */
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
  line-height: 1.65;
}

/* 4. EXECUTIVE CONTROL BAR (SCREEN ONLY) */
.executive-control-bar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(1, 36, 45, 0.96);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(197, 160, 89, 0.35);
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
  background: rgba(197, 160, 89, 0.18);
  color: var(--color-accent);
  border: 1px solid rgba(197, 160, 89, 0.4);
  padding: 4px 12px;
  border-radius: var(--radius-full);
}

.control-meta-text {
  font-size: 0.88rem;
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
  font-size: 0.86rem;
  font-weight: 700;
  padding: 8px 18px;
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
  border-color: rgba(255, 255, 255, 0.22);
}

.btn-ctrl-outline:hover {
  background: rgba(255, 255, 255, 0.16);
}

.btn-theme-toggle {
  width: 40px;
  height: 40px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.22);
  border-radius: var(--radius-md);
  color: #FFFFFF;
  cursor: pointer;
  font-size: 1.05rem;
}

/* 5. A4 PROFILE WRAPPER & SHEETS (SCREEN VIEW) */
.profile-document-container {
  max-width: 1040px;
  margin: 36px auto 72px auto;
  padding: 0 20px;
  display: flex;
  flex-direction: column;
  gap: 48px;
}

.profile-page {
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--border-subtle);
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  padding: 48px 52px 38px 52px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 1200px;
}

/* 6. RUNNING HEADERS & FOOTERS */
.page-running-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 16px;
  margin-bottom: 28px;
  font-size: 0.82rem;
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
  width: 26px;
  height: 26px;
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
  padding-top: 16px;
  margin-top: 28px;
  font-size: 0.8rem;
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
  padding: 4px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
}

/* 7. PAGE 1: LUXURY COVER HERO */
.page-cover {
  background: linear-gradient(135deg, #011E26 0%, #01313D 45%, #024756 100%);
  color: #FFFFFF;
  border: 1px solid rgba(197, 160, 89, 0.35);
  padding: 64px 58px 48px 58px;
  position: relative;
  min-height: 1200px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.cover-decor-ring {
  position: absolute;
  top: -60px;
  left: -60px;
  width: 300px;
  height: 300px;
  border: 1.5px solid rgba(197, 160, 89, 0.25);
  border-radius: 50%;
  pointer-events: none;
}

.cover-decor-ring-inner {
  position: absolute;
  top: 30px;
  left: 30px;
  width: 240px;
  height: 240px;
  border: 1px dashed rgba(197, 160, 89, 0.18);
  border-radius: 50%;
  pointer-events: none;
}

.cover-decor-diamond {
  position: absolute;
  bottom: 130px;
  right: -30px;
  width: 150px;
  height: 150px;
  border: 1.5px solid rgba(197, 160, 89, 0.22);
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
  gap: 10px;
  background: rgba(197, 160, 89, 0.16);
  color: var(--color-accent);
  border: 1px solid rgba(197, 160, 89, 0.45);
  padding: 7px 18px;
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 700;
  font-family: var(--font-heading);
}

.pulse-dot {
  width: 9px;
  height: 9px;
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
  padding: 10px 18px;
  border-radius: var(--radius-md);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
  display: inline-flex;
  align-items: center;
}

.cover-logo-img {
  height: 52px;
  width: auto;
  object-fit: contain;
}

.cover-body-center {
  position: relative;
  z-index: 2;
  margin: 54px 0;
}

.cover-category-tag {
  color: var(--color-accent);
  font-family: var(--font-heading);
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: 0.8px;
  margin-bottom: 18px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.cover-title {
  font-family: var(--font-heading);
  font-size: 3.1rem;
  font-weight: 700;
  line-height: 1.25;
  color: #FFFFFF;
  margin-bottom: 24px;
}

.cover-title span {
  color: var(--color-accent);
}

.cover-desc {
  font-size: 1.15rem;
  line-height: 1.8;
  color: #D1DEE5;
  max-width: 740px;
  margin-bottom: 40px;
}

.cover-pillars-strip {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  margin-top: 24px;
}

.cover-pillar-card {
  background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: var(--radius-md);
  padding: 18px 20px;
  backdrop-filter: blur(8px);
}

.cover-pillar-card h4 {
  font-family: var(--font-heading);
  font-size: 1rem;
  color: var(--color-accent);
  margin-bottom: 8px;
}

.cover-pillar-card p {
  font-size: 0.84rem;
  line-height: 1.55;
  color: #C0D0D9;
}

.cover-footer-meta {
  border-top: 1px solid rgba(255, 255, 255, 0.18);
  padding-top: 26px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  position: relative;
  z-index: 2;
}

.cover-meta-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.cover-meta-lbl {
  font-size: 0.78rem;
  color: #94A9B5;
  text-transform: uppercase;
}

.cover-meta-val {
  font-family: var(--font-heading);
  font-size: 1rem;
  font-weight: 700;
  color: #FFFFFF;
}

/* 8. COMMON SECTION HEADINGS & BADGES */
.section-chapter-chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--color-primary);
  background: var(--color-primary-subtle);
  border: 1px solid var(--color-primary-border);
  padding: 5px 14px;
  border-radius: var(--radius-full);
  margin-bottom: 12px;
}

.page-title {
  font-family: var(--font-heading);
  font-size: 1.85rem;
  font-weight: 700;
  color: var(--color-primary-dark);
  line-height: 1.35;
  margin-bottom: 10px;
}

[data-theme="dark"] .page-title {
  color: #FFFFFF;
}

.page-subtitle {
  font-size: 0.95rem;
  color: var(--text-muted);
  line-height: 1.7;
  margin-bottom: 26px;
}

/* 9. GRIDS, CARDS & SPACING SCALES */
.page-content-flow {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  gap: 20px;
}

.card-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.card-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.card-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.feature-box {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 20px 22px;
  position: relative;
}

.feature-box.featured-gold {
  border-color: rgba(197, 160, 89, 0.45);
  background: rgba(197, 160, 89, 0.05);
}

.feature-box-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}

.feature-icon-badge {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  background: var(--color-primary-subtle);
  color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.05rem;
  flex-shrink: 0;
}

.featured-gold .feature-icon-badge {
  background: var(--color-accent-subtle);
  color: var(--color-accent);
}

.feature-box-title {
  font-family: var(--font-heading);
  font-size: 1.02rem;
  font-weight: 700;
  color: var(--text-main);
}

.feature-box-desc {
  font-size: 0.88rem;
  color: var(--text-muted);
  line-height: 1.65;
}

/* 10. UNIFORM SERVICES MATRIX (PAGE 4) */
.services-matrix-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.service-matrix-item {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px 20px;
  display: grid;
  grid-template-columns: 85px 1.25fr 1.6fr 1.15fr;
  align-items: center;
  gap: 18px;
}

.srv-code-badge {
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 700;
  background: var(--color-primary);
  color: #FFFFFF;
  text-align: center;
  padding: 7px 12px;
  border-radius: var(--radius-sm);
}

.srv-name-col {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.srv-title {
  font-family: var(--font-heading);
  font-size: 1rem;
  font-weight: 700;
  color: var(--color-primary-dark);
}

[data-theme="dark"] .srv-title {
  color: #FFFFFF;
}

.srv-en-title {
  font-size: 0.78rem;
  color: var(--text-dim);
}

.srv-scope-text {
  font-size: 0.86rem;
  color: var(--text-muted);
  line-height: 1.55;
}

.srv-deliverable-box {
  background: #FFFFFF;
  border: 1px solid rgba(197, 160, 89, 0.4);
  border-radius: var(--radius-sm);
  padding: 10px 14px;
  font-size: 0.82rem;
  line-height: 1.5;
  color: var(--text-main);
}

[data-theme="dark"] .srv-deliverable-box {
  background: var(--bg-card);
}

.srv-deliverable-box strong {
  color: var(--color-accent);
  display: block;
  font-size: 0.75rem;
  margin-bottom: 3px;
  text-transform: uppercase;
}

/* 11. CHECKLISTS AND BULLETS */
.bullet-list-check {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
  margin-top: 10px;
}

.bullet-list-check li {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  font-size: 0.88rem;
  color: var(--text-muted);
  line-height: 1.55;
}

.bullet-list-check li::before {
  content: "✓";
  color: var(--color-accent);
  font-weight: 700;
  font-family: var(--font-heading);
  background: var(--color-accent-subtle);
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  flex-shrink: 0;
  margin-top: 2px;
}

/* 12. STEP PIPELINE (PAGE 6) */
.pipeline-steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.pipeline-step-card {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.step-phase-badge {
  font-family: var(--font-heading);
  font-size: 0.76rem;
  font-weight: 700;
  color: var(--color-accent);
  background: var(--color-accent-subtle);
  display: inline-block;
  padding: 3px 10px;
  border-radius: var(--radius-sm);
  width: fit-content;
}

.step-title {
  font-family: var(--font-heading);
  font-size: 0.96rem;
  font-weight: 700;
  color: var(--text-main);
}

.step-desc {
  font-size: 0.84rem;
  color: var(--text-muted);
  line-height: 1.55;
}

/* 13. REFINED CORPORATE ACCREDITATION BLOCK (PAGE 7) */
.accreditation-executive-grid {
  display: grid;
  grid-template-columns: 1.35fr 1fr;
  gap: 22px;
  margin-top: 16px;
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 24px;
}

.exec-endorsement-col {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.corporate-verification-card {
  background: #FFFFFF;
  border: 1.5px solid rgba(197, 160, 89, 0.4);
  border-radius: var(--radius-md);
  padding: 20px 22px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 10px;
  box-shadow: var(--shadow-sm);
}

[data-theme="dark"] .corporate-verification-card {
  background: var(--bg-card);
}

.verification-logo-img {
  height: 48px;
  width: auto;
  object-fit: contain;
}

.verification-company-ar {
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--color-primary-dark);
}

[data-theme="dark"] .verification-company-ar {
  color: #FFFFFF;
}

.verification-company-en {
  font-size: 0.76rem;
  color: var(--text-dim);
}

.verification-badges-row {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 4px;
}

.verif-chip {
  font-family: var(--font-heading);
  font-size: 0.74rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: var(--radius-full);
}

.verif-chip-cr {
  background: var(--color-primary-subtle);
  color: var(--color-primary);
  border: 1px solid var(--color-primary-border);
}

.verif-chip-occi {
  background: var(--color-accent-subtle);
  color: var(--color-accent);
  border: 1px solid rgba(197, 160, 89, 0.35);
}

.verif-status-badge {
  font-size: 0.74rem;
  color: #10B981;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 2px;
}

/* 14. METRICS ROW & HIGHLIGHT BOX */
.metrics-row-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 16px;
}

.metric-stat-card {
  background: var(--color-primary-subtle);
  border: 1px solid var(--color-primary-border);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  text-align: center;
}

.metric-val {
  font-family: var(--font-heading);
  font-size: 1.7rem;
  font-weight: 700;
  color: var(--color-primary);
  line-height: 1.2;
}

.metric-lbl {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-top: 5px;
}

/* 15. CALLOUT NOTICE */
.legal-callout-notice {
  background: rgba(2, 95, 115, 0.05);
  border-right: 4px solid var(--color-primary);
  padding: 14px 20px;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  font-size: 0.88rem;
  line-height: 1.65;
  color: var(--text-muted);
}

.legal-callout-notice strong {
  color: var(--color-primary-dark);
}

/* 16. PRINT STYLESHEET (STRICTLY PRESERVES GRIDS & STANDARD SPACING) */
@media print {
  @page {
    size: A4 portrait;
    margin: 0;
  }

  html, body {
    background: #FFFFFF !important;
    color: #141E24 !important;
    font-size: 8.5pt !important;
    line-height: 1.5 !important;
    width: 210mm !important;
    margin: 0 !important;
    padding: 0 !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  .no-print, .executive-control-bar {
    display: none !important;
  }

  .profile-document-container {
    max-width: 210mm !important;
    width: 210mm !important;
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
    padding: 13mm 16mm 11mm 16mm !important;
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
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
  }

  .page-cover {
    background: linear-gradient(135deg, #011E26 0%, #01313D 45%, #024756 100%) !important;
    color: #FFFFFF !important;
    padding: 18mm 16mm 14mm 16mm !important;
  }

  .cover-body-center {
    margin: 26px 0 !important;
  }

  .cover-title {
    font-size: 2.35rem !important;
    margin-bottom: 16px !important;
  }

  .cover-desc {
    font-size: 0.95rem !important;
    line-height: 1.65 !important;
    margin-bottom: 22px !important;
  }

  .cover-pillars-strip {
    gap: 12px !important;
  }

  .cover-pillar-card {
    padding: 12px 14px !important;
  }

  .cover-footer-meta {
    padding-top: 16px !important;
    gap: 12px !important;
  }

  .page-running-header {
    padding-bottom: 10px !important;
    margin-bottom: 14px !important;
    font-size: 0.74rem !important;
  }

  .page-running-footer {
    padding-top: 10px !important;
    margin-top: 14px !important;
    font-size: 0.72rem !important;
  }

  .section-chapter-chip {
    font-size: 0.74rem !important;
    padding: 3px 10px !important;
    margin-bottom: 6px !important;
  }

  .page-title {
    font-size: 1.4rem !important;
    margin-bottom: 6px !important;
    line-height: 1.35 !important;
  }

  .page-subtitle {
    font-size: 0.8rem !important;
    line-height: 1.5 !important;
    margin-bottom: 14px !important;
  }

  .page-content-flow {
    gap: 12px !important;
  }

  /* PRESERVE STANDARD GRIDS IN PRINT (NO COLLAPSE!) */
  .card-grid-2 {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 12px !important;
  }

  .card-grid-3 {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 10px !important;
  }

  .card-grid-4 {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 10px !important;
  }

  .feature-box {
    padding: 10px 14px !important;
    border-radius: 8px !important;
  }

  .feature-box-header {
    margin-bottom: 6px !important;
    gap: 8px !important;
  }

  .feature-icon-badge {
    width: 28px !important;
    height: 28px !important;
    font-size: 0.85rem !important;
  }

  .feature-box-title {
    font-size: 0.88rem !important;
  }

  .feature-box-desc {
    font-size: 0.76rem !important;
    line-height: 1.45 !important;
  }

  .bullet-list-check {
    gap: 5px !important;
    margin-top: 6px !important;
  }

  .bullet-list-check li {
    font-size: 0.76rem !important;
    gap: 7px !important;
    line-height: 1.4 !important;
  }

  .bullet-list-check li::before {
    width: 15px !important;
    height: 15px !important;
    font-size: 0.65rem !important;
  }

  .metrics-row-4 {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 10px !important;
    margin-top: 6px !important;
    margin-bottom: 6px !important;
  }

  .metric-stat-card {
    padding: 10px 12px !important;
  }

  .metric-val {
    font-size: 1.35rem !important;
  }

  .metric-lbl {
    font-size: 0.7rem !important;
    margin-top: 3px !important;
  }

  .legal-callout-notice {
    padding: 10px 14px !important;
    font-size: 0.76rem !important;
    line-height: 1.45 !important;
  }

  /* PRESERVE 4-COLUMN SERVICE MATRIX IN PRINT */
  .services-matrix-list {
    gap: 9px !important;
  }

  .service-matrix-item {
    padding: 9px 14px !important;
    gap: 12px !important;
    display: grid !important;
    grid-template-columns: 68px 1.2fr 1.6fr 1.1fr !important;
    border-radius: 8px !important;
  }

  .srv-code-badge {
    font-size: 0.78rem !important;
    padding: 5px 8px !important;
  }

  .srv-title {
    font-size: 0.86rem !important;
  }

  .srv-en-title {
    font-size: 0.7rem !important;
  }

  .srv-scope-text {
    font-size: 0.74rem !important;
    line-height: 1.4 !important;
  }

  .srv-deliverable-box {
    padding: 6px 10px !important;
    font-size: 0.7rem !important;
    line-height: 1.35 !important;
  }

  .srv-deliverable-box strong {
    font-size: 0.66rem !important;
  }

  /* PRESERVE 3-COLUMN WORKFLOW STEPS IN PRINT */
  .pipeline-steps-grid {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 10px !important;
  }

  .pipeline-step-card {
    padding: 10px 12px !important;
    gap: 5px !important;
    border-radius: 8px !important;
  }

  .step-phase-badge {
    font-size: 0.68rem !important;
    padding: 2px 7px !important;
  }

  .step-title {
    font-size: 0.82rem !important;
  }

  .step-desc {
    font-size: 0.72rem !important;
    line-height: 1.4 !important;
  }

  /* PRESERVE BALANCED ACCREDITATION GRID IN PRINT */
  .accreditation-executive-grid {
    display: grid !important;
    grid-template-columns: 1.35fr 1fr !important;
    padding: 14px 18px !important;
    gap: 16px !important;
    margin-top: 10px !important;
  }

  .corporate-verification-card {
    padding: 12px 14px !important;
    gap: 6px !important;
  }

  .verification-logo-img {
    height: 38px !important;
  }

  .verification-company-ar {
    font-size: 0.84rem !important;
  }

  .verification-company-en {
    font-size: 0.7rem !important;
  }
}

/* 17. RESPONSIVE ONLY FOR SCREEN VIEWPORT (MOBILE & TABLET) */
@media screen and (max-width: 820px) {
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
    padding: 28px 20px 24px 20px;
    min-height: auto;
  }

  .page-cover {
    padding: 40px 22px 28px 22px;
    min-height: auto;
  }

  .cover-title {
    font-size: 2.1rem;
  }

  .cover-pillars-strip {
    grid-template-columns: 1fr;
  }

  .cover-footer-meta {
    grid-template-columns: repeat(2, 1fr);
  }

  .card-grid-2, .card-grid-3, .card-grid-4, .pipeline-steps-grid {
    grid-template-columns: 1fr;
  }

  .service-matrix-item {
    grid-template-columns: 1fr;
    gap: 10px;
  }

  .accreditation-executive-grid {
    grid-template-columns: 1fr;
  }

  .metrics-row-4 {
    grid-template-columns: repeat(2, 1fr);
  }
}
"""

with open(OUTPUT_CSS, "w", encoding="utf-8") as f:
    f.write(CSS_CODE)

print("Master CSS generated.")
