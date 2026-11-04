import re

CSS_PATH = '/opt/data/cache/scratch/altakamul-site/css/style.css'
MAIN_JS_PATH = '/opt/data/cache/scratch/altakamul-site/js/main.js'

accordion_css = '''
/* --------------------------------------------------------------------------
   Nested Accordion Submenus for Mobile Navigation Drawer
   -------------------------------------------------------------------------- */
.mobile-accordion-group {
  border-bottom: 1px solid var(--border-color);
  width: 100%;
}

.mobile-accordion-toggle {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 13px 4px;
  background: none;
  border: none;
  font-family: inherit;
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
  cursor: pointer;
  text-align: inherit;
}

.mobile-accordion-toggle .accordion-chevron {
  transition: transform 0.3s ease;
  color: var(--primary-gold);
}

.mobile-accordion-group.active .mobile-accordion-toggle .accordion-chevron {
  transform: rotate(180deg);
}

.mobile-submenu {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  padding: 0 10px;
  background: var(--bg-surface-elevated);
  border-radius: 8px;
  margin-bottom: 0;
}

.mobile-accordion-group.active .mobile-submenu {
  max-height: 420px;
  padding: 8px 12px 10px;
  margin-bottom: 10px;
}

.mobile-submenu-link {
  display: block;
  padding: 9px 4px;
  font-size: 0.9rem;
  color: var(--text-secondary);
  text-decoration: none;
  border-bottom: 1px dashed var(--border-color);
  transition: color 0.2s, padding 0.2s;
}

.mobile-submenu-link:last-child {
  border-bottom: none;
}

.mobile-submenu-link:hover,
.mobile-submenu-link:active {
  color: var(--primary-gold);
}
'''

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

if '.mobile-accordion-group' not in css:
    css += accordion_css
    with open(CSS_PATH, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added mobile accordion CSS to style.css!")
else:
    print("Mobile accordion CSS already present in style.css.")

with open(MAIN_JS_PATH, 'r', encoding='utf-8') as f:
    js_code = f.read()

# Add toggleMobileSubmenu to main.js if not present
if 'toggleMobileSubmenu' not in js_code:
    hook = 'window.toggleMobileMenu = function (e) {'
    replacement = '''window.toggleMobileSubmenu = function (e, id) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    const group = e.currentTarget.closest('.mobile-accordion-group');
    if (!group) return;

    // Optional: close other accordion groups
    document.querySelectorAll('.mobile-accordion-group').forEach(other => {
      if (other !== group) {
        other.classList.remove('active');
      }
    });

    group.classList.toggle('active');
  };

  window.toggleMobileMenu = function (e) {'''
    js_code = js_code.replace(hook, replacement)
    with open(MAIN_JS_PATH, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print("Added toggleMobileSubmenu to js/main.js!")
else:
    print("toggleMobileSubmenu already present in js/main.js.")
