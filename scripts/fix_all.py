import os, glob, re

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'

# 1. Update main.js: Clean, Single-Fire Handlers, Zero-Flash Execution
main_js_content = '''/**
 * Al Takamul International Trading LLC — Sovereign Corporate Platform
 * Instant Hydration Multi-Language Controller (Arabic, Persian, English)
 * Dynamic Dual-Theme & Touch Mobile Engine
 */

(function () {
  'use strict';

  // Read stored preferences with robust defaults
  let currentLang = localStorage.getItem('altakamul_lang') || 'ar';
  let currentTheme = localStorage.getItem('altakamul_theme') || 'dark';

  // 1. Theme Controller
  window.initTheme = function () {
    document.documentElement.setAttribute('data-theme', currentTheme);
    const sunIcons = document.querySelectorAll('.theme-icon-sun');
    const moonIcons = document.querySelectorAll('.theme-icon-moon');
    
    if (currentTheme === 'dark') {
      sunIcons.forEach(el => el.style.display = 'inline-block');
      moonIcons.forEach(el => el.style.display = 'none');
    } else {
      sunIcons.forEach(el => el.style.display = 'none');
      moonIcons.forEach(el => el.style.display = 'inline-block');
    }
  };

  window.toggleTheme = function () {
    currentTheme = (currentTheme === 'dark' ? 'light' : 'dark');
    localStorage.setItem('altakamul_theme', currentTheme);
    window.initTheme();
  };

  // 2. Multilingual Engine
  window.applyTranslations = function (lang) {
    const dict = (window.ALT_TRANSLATIONS && window.ALT_TRANSLATIONS[lang]) ? window.ALT_TRANSLATIONS[lang] : null;
    if (!dict) return;

    const dir = dict.direction || (lang === 'en' ? 'ltr' : 'rtl');
    document.documentElement.setAttribute('lang', lang);
    document.documentElement.setAttribute('dir', dir);
    if (document.body) {
      document.body.setAttribute('dir', dir);
    }

    // Apply translations to all data-i18n elements
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (dict[key]) {
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
          el.setAttribute('placeholder', dict[key]);
        } else {
          el.innerHTML = dict[key];
        }
      }
    });

    // Update Language Dropdown Selector in Header
    const codeEl = document.querySelector('.current-lang-code');
    if (codeEl) {
      codeEl.textContent = lang.toUpperCase();
    }

    // Mark active in dropdown
    document.querySelectorAll('.lang-option').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // Update document title dynamically
    const brandName = dict.brand_name || 'Al Takamul';
    const heroTitle = dict.hero_title || '';
    if (document.querySelector('title')) {
      document.title = brandName + ' | ' + (heroTitle ? heroTitle : 'International Trading House');
    }
  };

  window.setLanguage = function (lang) {
    currentLang = lang;
    localStorage.setItem('altakamul_lang', lang);
    window.applyTranslations(lang);
    const menu = document.getElementById('langDropdownMenu');
    if (menu) menu.classList.remove('active');
  };

  window.toggleLangMenu = function (e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    const menu = document.getElementById('langDropdownMenu');
    if (menu) menu.classList.toggle('active');
  };

  document.addEventListener('click', function (e) {
    const menu = document.getElementById('langDropdownMenu');
    if (menu && menu.classList.contains('active')) {
      if (!e.target.closest('.lang-dropdown-wrapper')) {
        menu.classList.remove('active');
      }
    }
  });

  // 3. Mobile Navigation Drawer Controller
  function ensureDrawerOverlay() {
    let overlay = document.getElementById('mobileDrawerOverlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = 'mobileDrawerOverlay';
      overlay.className = 'mobile-drawer-overlay';
      overlay.onclick = window.closeMobileMenu;
      document.body.appendChild(overlay);
    }
    return overlay;
  }

  window.toggleMobileMenu = function (e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    const drawer = document.getElementById('mobileDrawer');
    const overlay = ensureDrawerOverlay();
    if (!drawer) return;

    const isOpen = drawer.classList.contains('active');
    if (isOpen) {
      drawer.classList.remove('active');
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    } else {
      drawer.classList.add('active');
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeMobileMenu = function () {
    const drawer = document.getElementById('mobileDrawer');
    const overlay = document.getElementById('mobileDrawerOverlay');
    if (drawer) drawer.classList.remove('active');
    if (overlay) overlay.classList.remove('active');
    document.body.style.overflow = '';
  };

  // 4. FAQ Accordion
  window.toggleFaq = function (el) {
    const item = el.closest('.faq-item');
    if (item) {
      item.classList.toggle('active');
    }
  };

  // 5. Back to Top Button
  function initBackToTop() {
    const btn = document.getElementById('backToTopBtn');
    if (!btn) return;
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    }, { passive: true });

    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 6. Header Scrolled State
  function initStickyHeader() {
    const header = document.querySelector('.site-header');
    if (!header) return;
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  // 7. Lead Form Submission Handler
  window.handleTradeRequest = function (e) {
    e.preventDefault();
    const btn = e.target.querySelector('button[type="submit"]');
    if (btn) {
      const origText = btn.innerHTML;
      btn.innerHTML = '...';
      btn.disabled = true;
      setTimeout(() => {
        const msg = (currentLang === 'fa')
          ? 'درخواست شما با موفقیت ثبت شد. مشاوران بازرگانی ما به زودی با شما تماس خواهند گرفت.'
          : (currentLang === 'ar'
            ? 'تم استلام طلبكم بنجاح. سيتواصل معكم مستشارنا التجاري في أقرب وقت.'
            : 'Your trade consultation request has been received. Our advisors will contact you shortly.');
        alert(msg);
        e.target.reset();
        btn.innerHTML = origText;
        btn.disabled = false;
      }, 700);
    }
  };

  // 8. Synchronous Immediate Execution & DOM Setup
  window.initTheme();
  document.addEventListener('DOMContentLoaded', () => {
    window.initTheme();
    window.applyTranslations(currentLang);
    initStickyHeader();
    initBackToTop();
    ensureDrawerOverlay();
  });
})();
'''

with open(os.path.join(BASE_DIR, 'js', 'main.js'), 'w', encoding='utf-8') as f:
    f.write(main_js_content)
print("Updated js/main.js with single-fire toggle!")

# 2. Add scripts to <head> of all pages in pages/*.html
subpage_scripts = '''  <!-- Synchronous In-Memory Locale & Theme Engine -->
  <script src="../js/translations_data.js"></script>
  <script src="../js/main.js?v=4.1"></script>
</head>'''

for fpath in glob.glob(os.path.join(BASE_DIR, 'pages', '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # remove any existing script tags to avoid duplicates
    html = re.sub(r'<script src=\"\.\./js/.*?</script>\s*', '', html)
    
    # insert scripts right before </head>
    html = html.replace('</head>', subpage_scripts)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Injected scripts into <head> for:", os.path.basename(fpath))

# 3. Ensure index.html has v=4.1
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    idx_html = f.read()
idx_html = re.sub(r'main\.js(\?v=[0-9\.]+)?', 'main.js?v=4.1', idx_html)
with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(idx_html)
print("Updated index.html script tag to v=4.1!")
