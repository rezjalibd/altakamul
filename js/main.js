/**
 * Al Takamul International Trading LLC — Sovereign Corporate Engine
 * Persian / Arabic / English Real-Time State Controller
 * Zero-Flash Theme & Locale Hydration
 * Native Mobile Touch & Responsive Architecture
 */

(function () {
  'use strict';

  // Read current language & theme from localStorage with safe defaults
  let currentLang = localStorage.getItem('altakamul_lang') || 'ar';
  let currentTheme = localStorage.getItem('altakamul_theme') || 'dark';
  let translations = {};

  function getBasePath() {
    return (window.location.pathname.match(/\/pages\//) ? '../' : './');
  }

  // Theme Initializer
  function initTheme() {
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
  }

  window.toggleTheme = function () {
    currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('altakamul_theme', currentTheme);
    initTheme();
  };

  // Translations Loader & Engine
  async function loadTranslations() {
    try {
      const res = await fetch(getBasePath() + 'translations.json');
      if (res.ok) {
        translations = await res.json();
        applyTranslations(currentLang);
      }
    } catch (e) {
      console.warn('Could not load translations.json', e);
    }
  }

  function applyTranslations(lang) {
    if (!translations || !translations[lang]) return;
    const dict = translations[lang];

    // Direction & HTML Lang Attribute
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
  }

  window.setLanguage = function (lang) {
    currentLang = lang;
    localStorage.setItem('altakamul_lang', lang);
    applyTranslations(lang);
    const menu = document.getElementById('langDropdownMenu');
    if (menu) menu.classList.remove('active');
  };

  window.toggleLangMenu = function (e) {
    if (e) e.stopPropagation();
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

  // Sticky Header with Glass Blur
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

  // Mobile Drawer Toggle
  window.toggleMobileMenu = function () {
    const drawer = document.getElementById('mobileDrawer');
    const overlay = document.getElementById('mobileDrawerOverlay');
    if (drawer && overlay) {
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
    }
  };

  window.closeMobileMenu = function () {
    const drawer = document.getElementById('mobileDrawer');
    const overlay = document.getElementById('mobileDrawerOverlay');
    if (drawer) drawer.classList.remove('active');
    if (overlay) overlay.classList.remove('active');
    document.body.style.overflow = '';
  };

  // FAQ Accordion
  window.toggleFaq = function (el) {
    const item = el.closest('.faq-item');
    if (item) {
      item.classList.toggle('active');
    }
  };

  // Back to Top Button
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

  // Lead Form Submission Simulation
  window.handleTradeRequest = function (e) {
    e.preventDefault();
    const btn = e.target.querySelector('button[type="submit"]');
    if (btn) {
      const origText = btn.innerHTML;
      btn.innerHTML = '...';
      btn.disabled = true;
      setTimeout(() => {
        alert(currentLang === 'fa' ? 'درخواست شما با موفقیت ثبت شد. کارشناسان ما به زودی با شما تماس خواهند گرفت.' : (currentLang === 'ar' ? 'تم استلام طلبكم بنجاح. سيتواصل معكم مستشارنا التجاري في أقرب وقت.' : 'Your trade consultation request has been received. Our advisors will contact you shortly.'));
        e.target.reset();
        btn.innerHTML = origText;
        btn.disabled = false;
      }, 700);
    }
  };

  // Boot sequence
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    loadTranslations();
    initStickyHeader();
    initBackToTop();
  });
})();
