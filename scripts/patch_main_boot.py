with open('/opt/data/cache/scratch/altakamul-site/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace boot block
old_boot = '''  // 8. Synchronous Immediate Execution & DOM Setup
  window.initTheme();
  document.addEventListener('DOMContentLoaded', () => {
    window.initTheme();
    window.applyTranslations(currentLang);
    initStickyHeader();
    initBackToTop();
    ensureDrawerOverlay();
  });
})();'''

new_boot = '''  // 8. Robust Immediate Root Attributes & Hydration Boot
  document.documentElement.setAttribute('lang', currentLang);
  document.documentElement.setAttribute('dir', (currentLang === 'en' ? 'ltr' : 'rtl'));
  window.initTheme();

  function boot() {
    window.initTheme();
    window.applyTranslations(currentLang);
    initStickyHeader();
    initBackToTop();
    ensureDrawerOverlay();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();'''

if old_boot in js:
    js = js.replace(old_boot, new_boot)
    with open('/opt/data/cache/scratch/altakamul-site/js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Patched js/main.js boot sequence successfully!")
else:
    print("Notice: old_boot not found directly, checking regex replacement...")
    import re
    js = re.sub(r'// 8\. Synchronous Immediate Execution.*?\}\)\(\);', new_boot, js, flags=re.DOTALL)
    with open('/opt/data/cache/scratch/altakamul-site/js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Patched js/main.js with regex!")
