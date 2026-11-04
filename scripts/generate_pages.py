import json, os, re

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'
with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
    trans = json.load(f)

# Common Components Generator
def get_header(is_root=True):
    prefix = './pages/' if is_root else './'
    home_link = './index.html' if is_root else '../index.html'
    logo_src = 'images/logo.png' if is_root else '../images/logo.png'

    return f'''  <!-- Site Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="{home_link}" class="brand-link">
        <img src="{logo_src}" alt="Al Takamul" class="brand-logo" width="42" height="42">
        <div class="brand-text-wrap">
          <span class="brand-title" data-i18n="brand_name">شركة تكامل للتجارة الدولية</span>
          <span class="brand-subtitle" data-i18n="brand_sub">Al Takamul International Trading LLC</span>
        </div>
      </a>

      <!-- Desktop Nav -->
      <nav class="main-nav">
        <a href="{home_link}" class="nav-link" data-i18n="nav_home">الرئيسية</a>
        <a href="{prefix}about.html" class="nav-link" data-i18n="nav_about">من نحن</a>
        
        <div class="nav-dropdown-wrapper">
          <a href="{prefix}services.html" class="nav-link nav-dropdown-trigger">
            <span data-i18n="nav_services">خدماتنا</span>
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </a>
          <div class="nav-dropdown-menu">
            <a href="{prefix}international-trade.html" class="dropdown-item">
              <div>
                <span class="dropdown-item-title" data-i18n="service_1_title">التجارة الدولية وبيت التجارة</span>
                <span class="dropdown-item-desc" data-i18n="service_1_desc">عقد الصفقات الكبرى والتمثيل التجاري</span>
              </div>
            </a>
            <a href="{prefix}import-export.html" class="dropdown-item">
              <div>
                <span class="dropdown-item-title" data-i18n="service_2_title">الاستيراد والتصدير وإعادة التصدير</span>
                <span class="dropdown-item-desc" data-i18n="service_2_desc">شحنات بحرية وجوية وتخليص جمركي</span>
              </div>
            </a>
            <a href="{prefix}procurement.html" class="dropdown-item">
              <div>
                <span class="dropdown-item-title" data-i18n="service_3_title">توريد وتأمين احتياجات المشاريع</span>
                <span class="dropdown-item-desc" data-i18n="service_3_desc">تأمين المواد الخام والآلات الكبرى</span>
              </div>
            </a>
            <a href="{prefix}financial-advisory.html" class="dropdown-item">
              <div>
                <span class="dropdown-item-title" data-i18n="service_4_title">الاستشارات المالية والاعتمادات</span>
                <span class="dropdown-item-desc" data-i18n="service_4_desc">هندسة الدفع والاعتمادات المستندية</span>
              </div>
            </a>
            <a href="{prefix}made-in-oman.html" class="dropdown-item">
              <div>
                <span class="dropdown-item-title" data-i18n="service_5_title">بنية التصنيع وهوية صُنع في عُمان</span>
                <span class="dropdown-item-desc" data-i18n="service_5_desc">شهادة المنشأ والاستفادة من اتفاقيات FTA</span>
              </div>
            </a>
          </div>
        </div>

        <a href="{home_link}#hubs" class="nav-link" data-i18n="nav_hubs">الموانئ والمناطق الحرة</a>
        <a href="{home_link}#process" class="nav-link" data-i18n="nav_process">آلية العمل</a>
        <a href="{prefix}contact.html" class="nav-link" data-i18n="nav_contact">اتصل بنا</a>
        <a href="{prefix}faq.html" class="nav-link" data-i18n="nav_faq">الأسئلة الشائعة</a>
      </nav>

      <!-- Header Controls -->
      <div class="header-actions">
        <!-- 3-Language Selector -->
        <div class="lang-dropdown-wrapper">
          <button class="lang-dropdown-btn" onclick="toggleLangMenu(event)" aria-label="Language Selector">
            <svg class="lang-globe-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            <span class="current-lang-code">AR</span>
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="lang-dropdown-menu" id="langDropdownMenu">
            <button class="lang-option active" data-lang="ar" onclick="setLanguage('ar')">العربية</button>
            <button class="lang-option" data-lang="fa" onclick="setLanguage('fa')">فارسی</button>
            <button class="lang-option" data-lang="en" onclick="setLanguage('en')">English</button>
          </div>
        </div>

        <!-- Theme Toggle Button -->
        <button class="btn-theme-toggle" onclick="toggleTheme()" aria-label="Toggle Theme" title="تبديل النمط">
          <svg class="theme-icon-sun" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
          </svg>
          <svg class="theme-icon-moon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" style="display:none;">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
          </svg>
        </button>

        <!-- CTA Header Button (Desktop) -->
        <a href="{prefix}request.html" class="btn-cta" data-i18n="btn_request_short">طلب استشارة</a>

        <!-- Mobile Drawer Toggle Hamburger -->
        <button class="mobile-toggle" onclick="toggleMobileMenu(event)" aria-label="Menu Toggle">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer Overlay & Drawer -->
  <div class="mobile-drawer-overlay" id="mobileDrawerOverlay" onclick="closeMobileMenu()"></div>
  <aside class="mobile-drawer" id="mobileDrawer">
    <div class="mobile-drawer-header">
      <span style="font-weight:800; font-size:1.05rem;" data-i18n="brand_name">شركة تکامل</span>
      <button class="mobile-close-btn" onclick="closeMobileMenu()" aria-label="Close">&times;</button>
    </div>
    <div class="mobile-nav-links">
      <a href="{home_link}" class="mobile-nav-link" data-i18n="nav_home">الرئيسية</a>
      <a href="{prefix}about.html" class="mobile-nav-link" data-i18n="nav_about">من نحن</a>
      <a href="{prefix}services.html" class="mobile-nav-link" data-i18n="nav_services">دليل الخدمات</a>
      <a href="{prefix}international-trade.html" class="mobile-nav-link" style="padding-right:24px;" data-i18n="service_1_title">التجارة الدولية</a>
      <a href="{prefix}import-export.html" class="mobile-nav-link" style="padding-right:24px;" data-i18n="service_2_title">الاستيراد والتصدير</a>
      <a href="{prefix}procurement.html" class="mobile-nav-link" style="padding-right:24px;" data-i18n="service_3_title">توريد المشاريع</a>
      <a href="{prefix}financial-advisory.html" class="mobile-nav-link" style="padding-right:24px;" data-i18n="service_4_title">الاستشارات المالية</a>
      <a href="{prefix}made-in-oman.html" class="mobile-nav-link" style="padding-right:24px;" data-i18n="service_5_title">صُنع في عُمان</a>
      <a href="{home_link}#hubs" class="mobile-nav-link" data-i18n="nav_hubs">الموانئ والمناطق الحرة</a>
      <a href="{home_link}#process" class="mobile-nav-link" data-i18n="nav_process">آلية العمل</a>
      <a href="{prefix}contact.html" class="mobile-nav-link" data-i18n="nav_contact">اتصل بنا</a>
      <a href="{prefix}faq.html" class="mobile-nav-link" data-i18n="nav_faq">الأسئلة الشائعة</a>
      <div style="margin-top:20px;">
        <a href="{prefix}request.html" class="btn-cta" style="width:100%; justify-content:center;" data-i18n="btn_request">طلب استشارة تجارية</a>
      </div>
    </div>
  </aside>'''

def get_footer(is_root=True):
    prefix = './pages/' if is_root else './'
    home_link = './index.html' if is_root else '../index.html'
    logo_src = 'images/logo.png' if is_root else '../images/logo.png'

    return f'''  <!-- Mobile Sticky CTA Bar -->
  <div class="mobile-sticky-cta">
    <div class="mobile-sticky-info">
      <div class="mobile-sticky-title" data-i18n="brand_name">شركة تكامل للتجارة الدولية</div>
      <div class="mobile-sticky-tag" data-i18n="hero_badge_clean">مسقط • سلطنة عمان</div>
    </div>
    <div class="mobile-sticky-actions">
      <a href="https://wa.me/96871081635" target="_blank" rel="noopener" class="mobile-sticky-wa-btn" aria-label="WhatsApp">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
      </a>
      <a href="{prefix}request.html" class="btn-cta btn-compact" data-i18n="btn_request_short">طلب استشارة</a>
    </div>
  </div>

  <!-- Corporate Footer -->
  <footer class="site-footer">
    <div class="footer-grid">
      <div>
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:16px;">
          <img src="{logo_src}" alt="Al Takamul" style="height:36px; width:auto;">
          <span style="font-weight:800; font-size:1.1rem; color:var(--text-primary);" data-i18n="brand_name">شركة تكامل للتجارة الدولية</span>
        </div>
        <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.75; margin-bottom:16px;" data-i18n="footer_about">
          بيت التجارة الدولية الرائد في مسقط لتقديم خدمات التجارة العابرة للحدود، سلاسل الإمداد المتطورة، وتوطين الصناعات.
        </p>
        <div style="font-size:0.82rem; color:var(--primary-gold);" data-i18n="footer_cr">CR 1389420 / مسقط، سلطنة عُمان</div>
      </div>

      <div>
        <div class="footer-col-title" data-i18n="footer_col_services">خدماتنا الأساسية</div>
        <ul class="footer-links-list">
          <li><a href="{prefix}international-trade.html" class="footer-link" data-i18n="service_1_title">التجارة الدولية</a></li>
          <li><a href="{prefix}import-export.html" class="footer-link" data-i18n="service_2_title">الاستيراد والتصدير</a></li>
          <li><a href="{prefix}procurement.html" class="footer-link" data-i18n="service_3_title">توريد المشاريع</a></li>
          <li><a href="{prefix}financial-advisory.html" class="footer-link" data-i18n="service_4_title">الاستشارات المالية</a></li>
          <li><a href="{prefix}made-in-oman.html" class="footer-link" data-i18n="service_5_title">صُنع في عُمان</a></li>
        </ul>
      </div>

      <div>
        <div class="footer-col-title" data-i18n="footer_col_company">الشركة والشفافية</div>
        <ul class="footer-links-list">
          <li><a href="{prefix}about.html" class="footer-link" data-i18n="nav_about">من نحن ورؤيتنا</a></li>
          <li><a href="{prefix}services.html" class="footer-link" data-i18n="nav_services">مصفوفة الخدمات</a></li>
          <li><a href="{prefix}faq.html" class="footer-link" data-i18n="nav_faq">الأسئلة الشائعة</a></li>
          <li><a href="{prefix}privacy.html" class="footer-link" data-i18n="footer_privacy">سياسة الخصوصية</a></li>
          <li><a href="{prefix}terms.html" class="footer-link" data-i18n="footer_terms">الشروط والأحكام</a></li>
        </ul>
      </div>

      <div>
        <div class="footer-col-title" data-i18n="footer_col_contact">معلومات الاتصال</div>
        <ul class="footer-links-list">
          <li style="font-size:0.88rem; color:var(--text-secondary);" data-i18n="footer_hq_label">📍 مسقط، سلطنة عُمان - واحة المعرفة / مجمع الأعمال التجاري</li>
          <li style="font-size:0.88rem; color:var(--text-secondary);">📞 +968 7108 1635 / +968 3153 6000</li>
          <li style="font-size:0.88rem; color:var(--text-secondary);">✉️ info@omantakamul.com</li>
          <li style="margin-top:10px;">
            <a href="https://wa.me/96871081635" target="_blank" rel="noopener" class="btn-secondary" style="padding:6px 14px; font-size:0.82rem;">WhatsApp Desk</a>
          </li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div data-i18n="footer_copy">جميع الحقوق محفوظة © ٢٠٢٦ شركة تكامل للتجارة الدولية ش.م.م</div>
      <div style="display:flex; gap:16px;">
        <a href="{prefix}privacy.html" class="footer-link" data-i18n="footer_privacy">الخصوصية</a>
        <a href="{prefix}terms.html" class="footer-link" data-i18n="footer_terms">الشروط</a>
      </div>
    </div>
  </footer>

  <!-- Floating Back to Top Button -->
  <button id="backToTopBtn" class="back-to-top-btn" aria-label="Back to Top" title="إلى الأعلى">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"></polyline></svg>
  </button>'''

print("Common components helper created successfully!")
