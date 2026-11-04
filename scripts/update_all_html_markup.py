import os, glob, re

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'

# 1. Standard Nested Mobile Drawer Component for Home (index.html)
home_drawer_html = '''  <!-- Mobile Drawer Overlay & Drawer with Nested Submenus -->
  <div class="mobile-drawer-overlay" id="mobileDrawerOverlay" onclick="closeMobileMenu()"></div>
  <aside class="mobile-drawer" id="mobileDrawer">
    <div class="mobile-drawer-header">
      <span style="font-weight:800; font-size:1.05rem;" data-i18n="brand_name">شركة تكامل</span>
      <button class="mobile-close-btn" onclick="closeMobileMenu()" aria-label="Close">&times;</button>
    </div>
    <div class="mobile-nav-links">
      <a href="index.html" class="mobile-nav-link" data-i18n="nav_home">الرئيسية</a>
      <a href="pages/about.html" class="mobile-nav-link" data-i18n="nav_about">من نحن</a>

      <!-- Nested Services Accordion -->
      <div class="mobile-accordion-group">
        <button class="mobile-accordion-toggle" onclick="toggleMobileSubmenu(event, 'subServices')">
          <span data-i18n="nav_services">دليل الخدمات</span>
          <svg class="accordion-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="mobile-submenu" id="subServices">
          <a href="pages/services.html" class="mobile-submenu-link" data-i18n="nav_all_services">← جميع الخدمات والحلول</a>
          <a href="pages/international-trade.html" class="mobile-submenu-link" data-i18n="service_1_title">التجارة الدولية وبيت التجارة</a>
          <a href="pages/import-export.html" class="mobile-submenu-link" data-i18n="service_2_title">الاستيراد والتصدير وإعادة التصدير</a>
          <a href="pages/procurement.html" class="mobile-submenu-link" data-i18n="service_3_title">توريد وتأمين احتياجات المشاريع</a>
          <a href="pages/financial-advisory.html" class="mobile-submenu-link" data-i18n="service_4_title">الاستشارات المالية والاعتمادات</a>
          <a href="pages/made-in-oman.html" class="mobile-submenu-link" data-i18n="service_5_title">بنية التصنيع وهوية صُنع في عُمان</a>
        </div>
      </div>

      <!-- Nested Hubs Accordion -->
      <div class="mobile-accordion-group">
        <button class="mobile-accordion-toggle" onclick="toggleMobileSubmenu(event, 'subHubs')">
          <span data-i18n="nav_hubs">الموانئ والمناطق الحرة</span>
          <svg class="accordion-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="mobile-submenu" id="subHubs">
          <a href="index.html#hub-sohar" class="mobile-submenu-link" onclick="closeMobileMenu()" data-i18n="hub_sohar_title">ميناء ومنطقة صحار الحرة</a>
          <a href="index.html#hub-salalah" class="mobile-submenu-link" onclick="closeMobileMenu()" data-i18n="hub_salalah_title">ميناء ومنطقة صلالة الحرة</a>
          <a href="index.html#hub-duqm" class="mobile-submenu-link" onclick="closeMobileMenu()" data-i18n="hub_duqm_title">منطقة الدقم الاقتصادية (SEZAD)</a>
        </div>
      </div>

      <a href="index.html#process" class="mobile-nav-link" onclick="closeMobileMenu()" data-i18n="nav_process">آلية العمل</a>
      <a href="pages/contact.html" class="mobile-nav-link" data-i18n="nav_contact">اتصل بنا</a>
      <a href="pages/faq.html" class="mobile-nav-link" data-i18n="nav_faq">الأسئلة الشائعة</a>

      <div style="margin-top:20px;">
        <a href="pages/request.html" class="btn-cta" style="width:100%; justify-content:center;" data-i18n="btn_request">طلب استشارة تجارية</a>
      </div>
    </div>
  </aside>'''

# 2. Standard Nested Mobile Drawer Component for Subpages (pages/*.html)
subpage_drawer_html = '''  <!-- Mobile Drawer Overlay & Drawer with Nested Submenus -->
  <div class="mobile-drawer-overlay" id="mobileDrawerOverlay" onclick="closeMobileMenu()"></div>
  <aside class="mobile-drawer" id="mobileDrawer">
    <div class="mobile-drawer-header">
      <span style="font-weight:800; font-size:1.05rem;" data-i18n="brand_name">شركة تكامل</span>
      <button class="mobile-close-btn" onclick="closeMobileMenu()" aria-label="Close">&times;</button>
    </div>
    <div class="mobile-nav-links">
      <a href="../index.html" class="mobile-nav-link" data-i18n="nav_home">الرئيسية</a>
      <a href="./about.html" class="mobile-nav-link" data-i18n="nav_about">من نحن</a>

      <!-- Nested Services Accordion -->
      <div class="mobile-accordion-group">
        <button class="mobile-accordion-toggle" onclick="toggleMobileSubmenu(event, 'subServices')">
          <span data-i18n="nav_services">دليل الخدمات</span>
          <svg class="accordion-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="mobile-submenu" id="subServices">
          <a href="./services.html" class="mobile-submenu-link" data-i18n="nav_all_services">← جميع الخدمات والحلول</a>
          <a href="./international-trade.html" class="mobile-submenu-link" data-i18n="service_1_title">التجارة الدولية وبيت التجارة</a>
          <a href="./import-export.html" class="mobile-submenu-link" data-i18n="service_2_title">الاستيراد والتصدير وإعادة التصدير</a>
          <a href="./procurement.html" class="mobile-submenu-link" data-i18n="service_3_title">توريد وتأمين احتياجات المشاريع</a>
          <a href="./financial-advisory.html" class="mobile-submenu-link" data-i18n="service_4_title">الاستشارات المالية والاعتمادات</a>
          <a href="./made-in-oman.html" class="mobile-submenu-link" data-i18n="service_5_title">بنية التصنيع وهوية صُنع في عُمان</a>
        </div>
      </div>

      <!-- Nested Hubs Accordion -->
      <div class="mobile-accordion-group">
        <button class="mobile-accordion-toggle" onclick="toggleMobileSubmenu(event, 'subHubs')">
          <span data-i18n="nav_hubs">الموانئ والمناطق الحرة</span>
          <svg class="accordion-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="mobile-submenu" id="subHubs">
          <a href="../index.html#hub-sohar" class="mobile-submenu-link" data-i18n="hub_sohar_title">ميناء ومنطقة صحار الحرة</a>
          <a href="../index.html#hub-salalah" class="mobile-submenu-link" data-i18n="hub_salalah_title">ميناء ومنطقة صلالة الحرة</a>
          <a href="../index.html#hub-duqm" class="mobile-submenu-link" data-i18n="hub_duqm_title">منطقة الدقم الاقتصادية (SEZAD)</a>
        </div>
      </div>

      <a href="../index.html#process" class="mobile-nav-link" data-i18n="nav_process">آلية العمل</a>
      <a href="./contact.html" class="mobile-nav-link" data-i18n="nav_contact">اتصل بنا</a>
      <a href="./faq.html" class="mobile-nav-link" data-i18n="nav_faq">الأسئلة الشائعة</a>

      <div style="margin-top:20px;">
        <a href="./request.html" class="btn-cta" style="width:100%; justify-content:center;" data-i18n="btn_request">طلب استشارة تجارية</a>
      </div>
    </div>
  </aside>'''

# Apply drawer update to index.html
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_content = re.sub(
    r'<div class="mobile-drawer-overlay"[^>]*>.*?<\/aside>',
    home_drawer_html,
    idx_content,
    flags=re.DOTALL
)
with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Updated index.html drawer!")

# Apply drawer update to all pages/*.html
for fpath in glob.glob(os.path.join(BASE_DIR, 'pages', '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        p_content = f.read()
    p_content = re.sub(
        r'<div class="mobile-drawer-overlay"[^>]*>.*?<\/aside>',
        subpage_drawer_html,
        p_content,
        flags=re.DOTALL
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(p_content)
    print("Updated drawer in:", os.path.basename(fpath))
