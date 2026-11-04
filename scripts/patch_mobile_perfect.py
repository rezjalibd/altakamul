with open('/opt/data/cache/scratch/altakamul-site/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_perfect = '''
/* --------------------------------------------------------------------------
   PERFECT MOBILE & ZERO OVERFLOW FIXES
   -------------------------------------------------------------------------- */
@media (max-width: 768px) {
  .canvas-backdrop {
    display: none !important;
  }

  .floating-geo-shape {
    display: none !important;
  }

  .hero-section {
    padding: 24px 0 20px !important;
  }

  .section-container {
    padding: 28px 16px !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    overflow-x: hidden !important;
  }

  .hero-title {
    font-size: 1.6rem !important;
    line-height: 1.3 !important;
    word-break: break-word !important;
    overflow-wrap: break-word !important;
  }

  .hero-badge {
    white-space: normal !important;
    display: inline-flex !important;
    max-width: 100% !important;
    font-size: 0.76rem !important;
    padding: 5px 12px !important;
    line-height: 1.4 !important;
  }

  .brand-logo {
    width: 34px !important;
    height: 34px !important;
  }

  .brand-title {
    font-size: 0.88rem !important;
    max-width: 125px !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    white-space: nowrap !important;
  }

  .btn-theme-toggle {
    width: 36px !important;
    height: 36px !important;
  }

  .mobile-toggle {
    width: 36px !important;
    height: 36px !important;
  }

  .lang-toggle-btn {
    padding: 6px 10px !important;
    font-size: 0.78rem !important;
  }

  .hero-buttons {
    flex-direction: column !important;
    gap: 12px !important;
    width: 100% !important;
  }

  .hero-buttons .btn-cta,
  .hero-buttons .btn-secondary {
    width: 100% !important;
    text-align: center !important;
    box-sizing: border-box !important;
  }

  .hero-visual-card {
    padding: 16px !important;
    margin-top: 16px !important;
  }

  .radar-container {
    width: 220px !important;
    height: 220px !important;
    margin: 10px auto !important;
  }
}
'''

css += mobile_perfect

with open('/opt/data/cache/scratch/altakamul-site/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied perfect mobile tweaks!")
