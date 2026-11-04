/**
 * Al Takamul International Trading LLC — Main Controller
 * Three-Language Engine (Arabic default RTL, English LTR, Persian RTL)
 * Complete Persistent State & DOM Synchronization
 * Mobile Drawer, Sticky Header, Spaced FAQ Accordion, Forms
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
    const flagEl = document.querySelector('.current-lang-flag');
    const codeEl = document.querySelector('.current-lang-code');
    if (flagEl) flagEl.textContent = dict.lang_flag || (lang === 'en' ? '🇬🇧' : (lang === 'fa' ? '🇮🇷' : '🇴🇲'));
    if (codeEl) codeEl.textContent = lang.toUpperCase();

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

  document.addEventListener('click', () => {
    const menu = document.getElementById('langDropdownMenu');
    if (menu) menu.classList.remove('active');
  });

  // Sticky Header
  function initStickyHeader() {
    const header = document.querySelector('.site-header');
    if (!header) return;
    window.addEventListener('scroll', () => {
      header.classList.toggle('scrolled', window.scrollY > 20);
    });
  }

  // Mobile Drawer
  window.toggleMobileMenu = function () {
    const drawer = document.getElementById('mobileDrawer');
    const overlay = document.getElementById('mobileOverlay');
    if (drawer && overlay) {
      const isCurrentlyActive = drawer.classList.contains('active');
      if (isCurrentlyActive) {
        drawer.classList.remove('active');
        overlay.classList.remove('active');
      } else {
        drawer.classList.add('active');
        overlay.classList.add('active');
      }
    }
  };

  window.closeMobileMenu = function () {
    const drawer = document.getElementById('mobileDrawer');
    const overlay = document.getElementById('mobileOverlay');
    if (drawer && overlay) {
      drawer.classList.remove('active');
      overlay.classList.remove('active');
    }
  };

  // FAQ Accordion
  window.toggleFaq = function (el) {
    el.classList.toggle('active');
  };

  // Back To Top
  function initBackToTop() {
    const btn = document.getElementById('backToTopBtn');
    if (!btn) return;
    window.addEventListener('scroll', () => {
      btn.classList.toggle('active', window.scrollY > 250);
    });
    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Form Handling
  window.handleTradeRequest = function (e) {
    e.preventDefault();
    const form = e.target;
    const btn = form.querySelector('button[type="submit"]');
    if (btn) {
      btn.innerText = '...';
      btn.disabled = true;
    }

    setTimeout(() => {
      window.location.href = getBasePath() + 'pages/thank-you.html';
    }, 600);
  };

  // Bootstrap
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    loadTranslations();
    initStickyHeader();
    initBackToTop();

    document.querySelectorAll('.btn-theme-toggle').forEach(btn => {
      btn.addEventListener('click', window.toggleTheme);
    });

    document.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', window.closeMobileMenu);
    });
  });
})();
