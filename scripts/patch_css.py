import re

CSS_PATH = '/opt/data/cache/scratch/altakamul-site/css/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. canvas-backdrop fix
css = re.sub(
    r'\.canvas-backdrop\s*\{[^}]*\}',
    '''.canvas-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  max-width: 100vw;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}''',
    css
)

# 2. hero-badge fix
css = re.sub(
    r'(\.hero-badge\s*\{[^}]*)white-space:\s*nowrap\s*!important;',
    r'\1white-space: normal; word-break: break-word; max-width: 100%;',
    css
)

# 3. Add mobile body overflow and bottom spacing
mobile_enhancements = '''
/* Enhanced Mobile Fit & Anti-Overflow Protection */
html, body {
  overflow-x: hidden !important;
  max-width: 100vw !important;
}

main {
  padding-bottom: 80px;
}

@media (max-width: 768px) {
  .hero-badge {
    white-space: normal !important;
    word-break: break-word !important;
    max-width: 100% !important;
    font-size: 0.8rem !important;
    padding: 6px 12px !important;
  }

  .hero-title {
    font-size: 1.7rem !important;
    line-height: 1.3 !important;
    word-break: break-word !important;
    overflow-wrap: break-word !important;
  }

  .hero-desc {
    font-size: 0.92rem !important;
    line-height: 1.55 !important;
  }

  .brand-title {
    font-size: 0.92rem !important;
    max-width: 130px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .container, .hero-content, .hero-container {
    max-width: 100% !important;
    padding-left: 16px !important;
    padding-right: 16px !important;
    box-sizing: border-box !important;
  }
}
'''

css += mobile_enhancements

with open(CSS_PATH, 'w', encoding='utf-8') as f:
    f.write(css)

print("Patched style.css successfully with strict anti-overflow protection!")
