import re

css_path = "/opt/data/cache/scratch/altakamul-site/css/profile.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace the print section with tuned rules
new_print_css = """/* 16. PRINT OPTIMIZATION (EXACT A4 MEDIA PRINT) */
@media print {
  @page {
    size: A4 portrait;
    margin: 0;
  }

  html, body {
    background: #FFFFFF !important;
    color: #141E24 !important;
    font-size: 9pt !important;
    line-height: 1.45 !important;
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
    padding: 12mm 15mm 10mm 15mm !important;
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
    margin: 24px 0 !important;
  }

  .cover-title {
    font-size: 2.3rem !important;
    margin-bottom: 14px !important;
  }

  .cover-desc {
    font-size: 0.95rem !important;
    line-height: 1.6 !important;
    margin-bottom: 20px !important;
  }

  .cover-pillars-strip {
    gap: 10px !important;
  }

  .cover-pillar-card {
    padding: 10px 12px !important;
  }

  .cover-pillar-card h4 {
    font-size: 0.85rem !important;
    margin-bottom: 3px !important;
  }

  .cover-pillar-card p {
    font-size: 0.72rem !important;
  }

  .cover-footer-meta {
    padding-top: 14px !important;
    gap: 10px !important;
  }

  .page-running-header {
    padding-bottom: 8px !important;
    margin-bottom: 10px !important;
    font-size: 0.72rem !important;
  }

  .page-running-footer {
    padding-top: 8px !important;
    margin-top: 10px !important;
    font-size: 0.7rem !important;
  }

  .section-chapter-chip {
    font-size: 0.72rem !important;
    padding: 2px 8px !important;
    margin-bottom: 4px !important;
  }

  .page-title {
    font-size: 1.35rem !important;
    margin-bottom: 4px !important;
    line-height: 1.3 !important;
  }

  .page-subtitle {
    font-size: 0.78rem !important;
    line-height: 1.45 !important;
    margin-bottom: 12px !important;
  }

  .page-content-flow {
    gap: 10px !important;
  }

  .card-grid-2 {
    gap: 10px !important;
  }

  .card-grid-3 {
    gap: 8px !important;
  }

  .card-grid-4 {
    gap: 8px !important;
  }

  .feature-box {
    padding: 8px 12px !important;
    border-radius: 6px !important;
  }

  .feature-box-header {
    margin-bottom: 4px !important;
    gap: 6px !important;
  }

  .feature-icon-badge {
    width: 26px !important;
    height: 26px !important;
    font-size: 0.8rem !important;
  }

  .feature-box-title {
    font-size: 0.86rem !important;
  }

  .feature-box-desc {
    font-size: 0.74rem !important;
    line-height: 1.4 !important;
  }

  .bullet-list-check {
    gap: 4px !important;
    margin-top: 4px !important;
  }

  .bullet-list-check li {
    font-size: 0.74rem !important;
    gap: 6px !important;
    line-height: 1.35 !important;
  }

  .bullet-list-check li::before {
    width: 14px !important;
    height: 14px !important;
    font-size: 0.6rem !important;
  }

  .metrics-row-4 {
    gap: 8px !important;
    margin-top: 4px !important;
    margin-bottom: 4px !important;
  }

  .metric-stat-card {
    padding: 8px 10px !important;
  }

  .metric-val {
    font-size: 1.25rem !important;
  }

  .metric-lbl {
    font-size: 0.68rem !important;
    margin-top: 2px !important;
  }

  .legal-callout-notice {
    padding: 8px 12px !important;
    font-size: 0.74rem !important;
    line-height: 1.4 !important;
  }

  /* Matrix Page 4 tune */
  .services-matrix-list {
    gap: 8px !important;
  }

  .service-matrix-item {
    padding: 8px 12px !important;
    gap: 10px !important;
    grid-template-columns: 65px 1.15fr 1.6fr 1.1fr !important;
    border-radius: 6px !important;
  }

  .srv-code-badge {
    font-size: 0.75rem !important;
    padding: 4px 6px !important;
  }

  .srv-title {
    font-size: 0.84rem !important;
  }

  .srv-en-title {
    font-size: 0.68rem !important;
  }

  .srv-scope-text {
    font-size: 0.72rem !important;
    line-height: 1.35 !important;
  }

  .srv-deliverable-box {
    padding: 5px 8px !important;
    font-size: 0.68rem !important;
    line-height: 1.3 !important;
  }

  .srv-deliverable-box strong {
    font-size: 0.65rem !important;
  }

  /* Steps Page 6 tune */
  .pipeline-steps-grid {
    gap: 8px !important;
  }

  .pipeline-step-card {
    padding: 8px 10px !important;
    gap: 3px !important;
    border-radius: 6px !important;
  }

  .step-phase-badge {
    font-size: 0.65rem !important;
    padding: 1px 6px !important;
  }

  .step-title {
    font-size: 0.8rem !important;
  }

  .step-desc {
    font-size: 0.7rem !important;
    line-height: 1.35 !important;
  }

  /* Signatory Page 7 tune */
  .signatory-box-grid {
    padding: 12px 14px !important;
    gap: 14px !important;
    margin-top: 8px !important;
  }

  .seal-stamp-box {
    min-height: 100px !important;
    padding: 8px !important;
    gap: 4px !important;
  }

  .seal-icon-svg {
    width: 32px !important;
    height: 32px !important;
  }

  .seal-title {
    font-size: 0.78rem !important;
  }

  .seal-sub {
    font-size: 0.68rem !important;
  }
}"""

# Replace in CSS
pattern = r"/\* 16\. PRINT OPTIMIZATION.*?(?=/\* 17\. RESPONSIVE)"
css_updated = re.sub(pattern, new_print_css + "\n\n", css, flags=re.DOTALL)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_updated)

print("Updated print CSS with high-density tuned styles.")
