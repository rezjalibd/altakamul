import os

OUTPUT_HTML = "/opt/data/cache/scratch/altakamul-site/profile.html"
OUTPUT_HTML_ALT = "/opt/data/cache/scratch/altakamul-site/company-profile.html"

# SVGs
SVG_LOGO_PATH = "img/logo.png"
SVG_DOWNLOAD = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>'
SVG_PRINT = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>'
SVG_HOME = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>'
SVG_GLOBE = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>'
SVG_SHIELD = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'
SVG_ANCHOR = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="5" r="3"></circle><line x1="12" y1="22" x2="12" y2="8"></line><path d="M5 12H2a10 10 0 0 0 20 0h-3"></path></svg>'
SVG_BRIEFCASE = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>'
SVG_INDUSTRY = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2z"></path></svg>'
SVG_CHECK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>'
SVG_SEAL = '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path><polygon points="12 6 13.8 9.6 17.8 10.2 14.9 13 15.6 17 12 15.1 8.4 17 9.1 13 6.2 10.2 10.2 9.6 12 6"></polygon></svg>'

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>الملف التعريفي المؤسسي ۲۰۲۶ | شركة التكامل للتجارة الدولية ش.ذ.م.م - سلطنة عُمان</title>
    <meta name="description" content="الملف التعريفي المؤسسي والقدرات التشغيلية لشركة التكامل للتجارة الدولية ش.ذ.م.م (سجل تجاري: ۱۳۸۹۴۲۰ - مسقط). بوابتكم الاستراتيجية للتجارة الدولية وسلاسل الإمداد وتوطين الصناعة.">
    
    <!-- Open Graph -->
    <meta property="og:title" content="الملف التعريفي المؤسسي ۲۰۲۶ | شركة التكامل للتجارة الدولية">
    <meta property="og:description" content="بيت التجارة الدولية وسلاسل الإمداد والتمثيل التجاري في سلطنة عُمان. سجل تجاري ۱۳۸۹۴۲۰.">
    <meta property="og:image" content="https://omantakamul.com/site/assets/logo/logo.webp">
    <meta property="og:type" content="article">

    <!-- Favicon -->
    <link rel="icon" type="image/png" href="img/logo.png">

    <!-- Profile Specific Master Stylesheet -->
    <link rel="stylesheet" href="css/profile.css?v=2026.1">
    
    <script>
      (function() {{
        var savedTheme = localStorage.getItem('altakamul_theme');
        if (savedTheme === 'dark' || (!savedTheme && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
          document.documentElement.setAttribute('data-theme', 'dark');
        }}
      }})();
    </script>
</head>
<body>

    <!-- EXECUTIVE STICKY CONTROL STRIP (SCREEN ONLY) -->
    <aside class="executive-control-bar no-print" aria-label="Executive Controls">
        <div class="control-bar-inner">
            <div class="control-brand-info">
                <span class="control-doc-tag">DOC: TK-CORP-2026/V1</span>
                <span class="control-meta-text">شركة التكامل للتجارة الدولية ش.ذ.م.م • مسقط (س.ت: ۱۳۸۹۴۲۰)</span>
            </div>
            <div class="control-actions">
                <a href="pdf/Al-Takamul-Company-Profile-2026.pdf" download class="btn-ctrl btn-ctrl-primary" title="تحميل النسخة الرسمية PDF">
                    {SVG_DOWNLOAD}
                    <span>تحميل الملف المؤسسي (PDF)</span>
                </a>
                <button type="button" onclick="window.print()" class="btn-ctrl btn-ctrl-outline" title="طباعة أو تصدير PDF">
                    {SVG_PRINT}
                    <span>طباعة الوثيقة</span>
                </button>
                <a href="index.html" class="btn-ctrl btn-ctrl-outline" title="العودة للرئيسية">
                    {SVG_HOME}
                    <span>الموقع الرئيسي</span>
                </a>
                <button type="button" id="themeToggleBtn" class="btn-theme-toggle" onclick="toggleTheme()" aria-label="تبديل الوضع الليلي">
                    🌙
                </button>
            </div>
        </div>
    </aside>

    <!-- MAIN PROFILE DOSSIER SHEETS CONTAINER -->
    <main class="profile-document-container" id="profileDossier">

        <!-- ==============================================================
             PAGE 1: COVER HERO (صفحة الغلاف الفاخرة)
             ============================================================== -->
        <article class="profile-page page-cover" id="page-1">
            <div class="cover-decor-ring" aria-hidden="true"></div>
            <div class="cover-decor-ring-inner" aria-hidden="true"></div>
            <div class="cover-decor-diamond" aria-hidden="true"></div>

            <!-- Cover Top Header -->
            <header class="cover-header-top">
                <div class="cover-badge">
                    <span class="pulse-dot"></span>
                    <span>وثيقة استراتيجية معتمدة • مسقط، سلطنة عُمان</span>
                </div>
                <div class="cover-logo-wrapper">
                    <img src="img/logo.png" alt="شركة التكامل للتجارة الدولية" class="cover-logo-img">
                </div>
            </header>

            <!-- Cover Center Body -->
            <div class="cover-body-center">
                <div class="cover-category-tag">
                    {SVG_GLOBE}
                    <span>AL TAKAMUL INTERNATIONAL TRADING LLC</span>
                </div>
                <h1 class="cover-title">
                    الملف التعريفي المؤسسي<br>
                    <span>والقدرات التشغيلية والتجارية</span>
                </h1>
                <p class="cover-desc">
                    بيت التجارة الدولية الرائد، سلاسل الإمداد العابرة للحدود، الاستشارات الائتمانية والصفقات الكبرى، وتمكين التصنيع تحت مظلة الهوية الوطنية «صُنع في عُمان» للنفاذ للأسواق الإقليمية والدولية.
                </p>

                <!-- Core Pillars Highlights Strip -->
                <div class="cover-pillars-strip">
                    <div class="cover-pillar-card">
                        <h4>التجارة والتمثيل الحصري</h4>
                        <p>إدارة الصفقات الكبرى وتمثيل المصانع العالمية في أسواق عمان والخليج.</p>
                    </div>
                    <div class="cover-pillar-card">
                        <h4>سلاسل الإمداد والترانزيت</h4>
                        <p>تخليص جمركي مسبق عبر نظام بيان وإعادة تصدير بمزايا المناطق الحرة.</p>
                    </div>
                    <div class="cover-pillar-card">
                        <h4>اتفاقيات التجارة الحرة</h4>
                        <p>استفادة قصوى من اتفاقية التجارة مع أمريكا (FTA) وإعفاءات جمركية ۱۰۰٪.</p>
                    </div>
                </div>
            </div>

            <!-- Cover Bottom Metadata -->
            <footer class="cover-footer-meta">
                <div class="cover-meta-item">
                    <span class="cover-meta-lbl">رقم السجل التجاري</span>
                    <span class="cover-meta-val">CR: 1389420</span>
                </div>
                <div class="cover-meta-item">
                    <span class="cover-meta-lbl">مرجع الوثيقة</span>
                    <span class="cover-meta-val">DOC: TK-CORP-2026/V1</span>
                </div>
                <div class="cover-meta-item">
                    <span class="cover-meta-lbl">المقر الإقليمي</span>
                    <span class="cover-meta-val">واحة المعرفة مسقط (KOM)</span>
                </div>
                <div class="cover-meta-item">
                    <span class="cover-meta-lbl">تاريخ الاعتماد</span>
                    <span class="cover-meta-val">نوفمبر ۲۰۲۶ / ۱۴۴۸ هـ</span>
                </div>
            </footer>
        </article>


        <!-- ==============================================================
             PAGE 2: EXECUTIVE SUMMARY & VISION 2040
             ============================================================== -->
        <article class="profile-page" id="page-2">
            <!-- Running Header -->
            <div class="page-running-header">
                <div class="header-brand">
                    <img src="img/logo.png" alt="Al Takamul" class="header-logo-icon">
                    <span>شركة التكامل للتجارة الدولية ش.ذ.م.م</span>
                </div>
                <span class="header-doc-code">الفصل الأول: الهوية والاستراتيجية</span>
            </div>

            <div class="page-content-flow">
                <div>
                    <span class="section-chapter-chip">الفصل الأول • الرؤية والرسالة المؤسسية</span>
                    <h2 class="page-title">ريادة التجارة العابرة للحدود وتطوير الممرات اللوجستية</h2>
                    <p class="page-subtitle">
                        تأسست شركة التكامل للتجارة الدولية ش.ذ.م.م في مسقط لتكون كياناً تجارياً ولوجستياً واستشارياً متقدماً يسد الفجوة بين المصانع العالمية والأسواق الإقليمية، مستفيدة من الموقع الجغرافي الاستثنائي لسلطنة عُمان خارج مضيق هرمز.
                    </p>
                </div>

                <!-- 3 Pillars Grid -->
                <div class="card-grid-3">
                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_GLOBE}</span>
                            <h3 class="feature-box-title">رؤيتنا الاستراتيجية</h3>
                        </div>
                        <p class="feature-box-desc">
                            أن نكون بيت التجارة والتمثيل الأكثر موثوقية وشريك الاختيار الأول للمستثمرين والتجار العالميين الراغبين في اتخاذ سلطنة عُمان مركزاً إقليمياً لعمليات التوزيع والترانزيت وإعادة التصدير.
                        </p>
                    </div>

                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_BRIEFCASE}</span>
                            <h3 class="feature-box-title">رسالتنا التشغيلية</h3>
                        </div>
                        <p class="feature-box-desc">
                            تقديم حلول متكاملة تضمن الأمان المالي والقانوني لصفقات التجارة الدولية، تحسين تكاليف الشحن عبر الموانئ العمانية، وتمكين المصانع من تحقيق القيمة المحلية المضافة للتصدير للأسواق العالمية.
                        </p>
                    </div>

                    <div class="feature-box featured-gold">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_SHIELD}</span>
                            <h3 class="feature-box-title">قيمنا المؤسسية</h3>
                        </div>
                        <p class="feature-box-desc">
                            النزاهة والشفافية المطلقة، السرية التجارية الصارمة بموجب اتفاقيات (NDA)، الامتثال التنظيمي للأنظمة المصرفية والجمركية، والالتزام بأعلى معايير حوكمة التجارة البينية.
                        </p>
                    </div>
                </div>

                <!-- Oman Vision 2040 Alignment Box -->
                <div class="feature-box" style="margin-top: 4px;">
                    <div class="feature-box-header">
                        <span class="feature-icon-badge">{SVG_INDUSTRY}</span>
                        <h3 class="feature-box-title">المواءمة الاستراتيجية مع «رؤية عُمان ۲۰۴۰»</h3>
                    </div>
                    <p class="feature-box-desc" style="margin-bottom: 12px;">
                        تتماشى أهداف شركة التكامل بصورة مباشرة مع المحاور الاقتصادية لرؤية سلطنة عُمان ۲۰۴۰ من خلال:
                    </p>
                    <div class="card-grid-2">
                        <ul class="bullet-list-check">
                            <li>تنويع مصادر الدخل الوطني من خلال تنشيط قطاعات التجارة غير النفطية والخدمات اللوجستية.</li>
                            <li>جذب الاستثمارات الأجنبية الصناعية عبر توطين خطوط الإنتاج والفرص الاستثمارية بالمناطق الحرة.</li>
                        </ul>
                        <ul class="bullet-list-check">
                            <li>تعزيز حضور المنتجات العمانية في سلاسل الإمداد العالمية تحت علامة «صُنع في عُمان».</li>
                            <li>تفعيل الربط اللوجستي المتعدد الوسائط بين موانئ صحار، صلالة والدقم والأسواق الاستهلاكية الكبرى.</li>
                        </ul>
                    </div>
                </div>

                <!-- Key Metrics Strip -->
                <div class="metrics-row-4" style="margin-top: 8px;">
                    <div class="metric-stat-card">
                        <div class="metric-val">100%</div>
                        <div class="metric-lbl">ملكية أجنبية واسترداد أرباح</div>
                    </div>
                    <div class="metric-stat-card">
                        <div class="metric-val">0%</div>
                        <div class="metric-lbl">رسوم جمركية مع أمريكا وEFTA</div>
                    </div>
                    <div class="metric-stat-card">
                        <div class="metric-val">4</div>
                        <div class="metric-lbl">موانئ ومحاور لوجستية عالمية</div>
                    </div>
                    <div class="metric-stat-card">
                        <div class="metric-val">24/7</div>
                        <div class="metric-lbl">إشراف وتخليص جمركي ذكي</div>
                    </div>
                </div>
            </div>

            <!-- Running Footer -->
            <div class="page-running-footer">
                <span class="footer-cr">س.ت: ۱۳۸۹۴۲۰ • مسقط، سلطنة عُمان</span>
                <span class="footer-confidential">وثيقة تجارية رسمية • سرية ومحمية</span>
                <span class="page-number">صفحة ٢ من ٧</span>
            </div>
        </article>


        <!-- ==============================================================
             PAGE 3: GOVERNANCE, LEGAL & BANKING COMPLIANCE
             ============================================================== -->
        <article class="profile-page" id="page-3">
            <div class="page-running-header">
                <div class="header-brand">
                    <img src="img/logo.png" alt="Al Takamul" class="header-logo-icon">
                    <span>شركة التكامل للتجارة الدولية ش.ذ.م.م</span>
                </div>
                <span class="header-doc-code">الفصل الثاني: الحوكمة والامتثال القانوني</span>
            </div>

            <div class="page-content-flow">
                <div>
                    <span class="section-chapter-chip">الفصل الثاني • الأطر التنظيمية والمصرفية</span>
                    <h2 class="page-title">حوكمة تعاقدية وائتمانية صارمة وفق القوانين والأعراف الدولية</h2>
                    <p class="page-subtitle">
                        تعمل شركة التكامل وفق منظومة تشريعية محكمة تتكامل فيها التراخيص التجارية العمانية مع المعايير الدولية الصادرة عن غرفة التجارة الدولية (ICC) لضمان حماية رؤوس الأموال ومصالح الشركاء المتعاقدين.
                    </p>
                </div>

                <!-- Regulatory Framework Grid -->
                <div class="card-grid-2">
                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_SHIELD}</span>
                            <h3 class="feature-box-title">الشخصية القانونية والتراخيص التجارية</h3>
                        </div>
                        <p class="feature-box-desc">
                            شركة ذات مسؤولية محدودة مسجلة رسمياً لدى وزارة التجارة والصناعة وترويج الاستثمار بموجب السجل التجاري رقم (۱۳۸۹۴۲۰). وعضو معتمد لدى غرفة تجارة وصناعة عُمان (OCCI). تخضع كافة الأنشطة لأحكام قانون الشركات التجارية العماني الصادر بالمرسوم السلطاني رقم ۱۸/۲۰۱۹.
                        </p>
                    </div>

                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_BRIEFCASE}</span>
                            <h3 class="feature-box-title">قواعد الإنكوترمز (ICC Incoterms® 2020)</h3>
                        </div>
                        <p class="feature-box-desc">
                            تخضع جميع صفقات التوريد والمبيعات الدولية للقواعد المعيارية للإنكوترمز ۲۰۲۰ (بما في ذلك EXW, FOB, CFR, CIF, DAP, DDP). يتم تحديد نقطة انتقال المخاطر والتأمين البحري التخصصي (Institute Cargo Clauses A) بدقة مطلقة ضمن بنود العقود المبرمة.
                        </p>
                    </div>

                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_GLOBE}</span>
                            <h3 class="feature-box-title">الاعتمادات المستندية (UCP 600 & URDG 758)</h3>
                        </div>
                        <p class="feature-box-desc">
                            تتم صياغة ومطابقة مستندات الشحن والتحصيل المستندي والاعتمادات المستندية غير القابلة للإلغاء المعززة طبقاً للأصول والأعراف الموحدة للاعتمادات المستندية (UCP 600) الصادرة عن غرفة التجارة الدولية، بالإضافة إلى القواعد الموحدة لخطابات الضمان (URDG 758).
                        </p>
                    </div>

                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_SHIELD}</span>
                            <h3 class="feature-box-title">مكافحة غسل الأموال والامتثال الرقابي (AML/CFT)</h3>
                        </div>
                        <p class="feature-box-desc">
                            نلتزم التزاماً كاملاً بأحكام قانون مكافحة غسل الأموال وتمويل الإرهاب العماني (المرسوم السلطاني ۳۰/۲۰۱۶) وتوجيهات مجموعة العمل المالي (FATF). نطبق إجراءات اعرف عميلك (KYC) والتحقق الصارم من مصادر الأموال والمستفيدين الحقيقيين من كافة الصفقات.
                        </p>
                    </div>
                </div>

                <!-- Banking Disclaimer Callout Box -->
                <div class="legal-callout-notice">
                    <strong>إشعار الشفافية والامتثال المصرفي:</strong> شركة التكامل للتجارة الدولية ش.ذ.م.م بيت تجارة دولية وشركة إدارة صادرات (EMC) واستشارات ائتمانية؛ وليست مصرفاً تجارياً أو مؤسسة مالية مانحة للقروض خاضعة لرقابة البنك المركزي العماني. كافة المعاملات المالية، فتح الاعتمادات المستندية، وإصدار خطابات الضمان تتم حصرياً عبر البنوك التجارية المرخصة بالسلطنة لصالح الأطراف المتعاقدة.
                </div>

                <!-- Data Privacy & Arbitration -->
                <div class="card-grid-2">
                    <div class="feature-box featured-gold">
                        <div class="feature-box-header">
                            <h4 class="feature-box-title">السرية التجارية وحماية البيانات</h4>
                        </div>
                        <p class="feature-box-desc">
                            حماية بيانات الشركاء وقوائم الموردين بموجب قانون حماية البيانات الشخصية العماني (المرسوم السلطاني ۶/۲۰۲۲) وتوقيع اتفاقيات عدم إفصاح ملزمة (NDAs).
                        </p>
                    </div>
                    <div class="feature-box featured-gold">
                        <div class="feature-box-header">
                            <h4 class="feature-box-title">حل النزاعات والداوری التجاری</h4>
                        </div>
                        <p class="feature-box-desc">
                            إخضاع النزاعات الناشئة عن المعاملات للقوانين العمانية وقواعد مركز عُمان للتحكيم التجاري (OAC) أو المحاكم التجارية المختصة بمسقط.
                        </p>
                    </div>
                </div>
            </div>

            <div class="page-running-footer">
                <span class="footer-cr">س.ت: ۱۳۸۹۴۲۰ • مسقط، سلطنة عُمان</span>
                <span class="footer-confidential">وثيقة تجارية رسمية • سرية ومحمية</span>
                <span class="page-number">صفحة ٣ من ٧</span>
            </div>
        </article>


        <!-- ==============================================================
             PAGE 4: CORE SERVICES MATRIX (مصفوفة الخدمات الخمس)
             ============================================================== -->
        <article class="profile-page" id="page-4">
            <div class="page-running-header">
                <div class="header-brand">
                    <img src="img/logo.png" alt="Al Takamul" class="header-logo-icon">
                    <span>شركة التكامل للتجارة الدولية ش.ذ.م.م</span>
                </div>
                <span class="header-doc-code">الفصل الثالث: مصفوفة الخدمات التجارية</span>
            </div>

            <div class="page-content-flow">
                <div>
                    <span class="section-chapter-chip">الفصل الثالث • الأركان الخمسة لمنظومة الأعمال</span>
                    <h2 class="page-title">مصفوفة الخدمات المؤسسية ونماذج التعاقد</h2>
                    <p class="page-subtitle">
                        نقدم منظومة متكاملة من خمس خدمات استراتيجية مصممة لتلبية متطلبات الشركات الصناعية والمستوردين وتجار السلع في الأسواق الإقليمية والدولية بكفاءة وموثوقية عالية.
                    </p>
                </div>

                <!-- Uniform Services Matrix List (SRV-01 to SRV-05) -->
                <div class="services-matrix-list">
                    <!-- Service 1 -->
                    <div class="service-matrix-item">
                        <span class="srv-code-badge">SRV-01</span>
                        <div class="srv-name-col">
                            <h3 class="srv-title">التجارة الدولية وبيت التجارة</h3>
                            <span class="srv-en-title">International Trading House</span>
                        </div>
                        <p class="srv-scope-text">
                            إدارة الصفقات الكبرى للسلع الأساسية والمواد الخام، التمثيل والوكالات التجارية الحصرية، والتوسط التعاقدي بين الموردين في آسيا وأوروبا والمشترين في الخليج والشرق الأوسط.
                        </p>
                        <div class="srv-deliverable-box">
                            <strong>مخرجات الخدمة والضمانات:</strong>
                            عقود دولية ملزمة (Incoterms 2020)، حماية الهوامش السعرية، وتمثيل قانوني معتمد.
                        </div>
                    </div>

                    <!-- Service 2 -->
                    <div class="service-matrix-item">
                        <span class="srv-code-badge">SRV-02</span>
                        <div class="srv-name-col">
                            <h3 class="srv-title">الاستيراد والتصدير والترانزيت</h3>
                            <span class="srv-en-title">Import, Export & Re-Export</span>
                        </div>
                        <p class="srv-scope-text">
                            إدارة حركة البضائع عبر موانئ صحار وصلالة والدقم والمطارات، التخليص الجمركي المسبق عبر نظام بيان، التخزين بالمستودعات الجمركية الحرة، وإعادة التصدير المعفى جمركياً.
                        </p>
                        <div class="srv-deliverable-box">
                            <strong>مخرجات الخدمة والضمانات:</strong>
                            بيانات جمركية فورية (نظام بيان)، بوالص شحن بحری/جوی، وشهادات منشأ معتمدة.
                        </div>
                    </div>

                    <!-- Service 3 -->
                    <div class="service-matrix-item">
                        <span class="srv-code-badge">SRV-03</span>
                        <div class="srv-name-col">
                            <h3 class="srv-title">توريد السلع واحتياجات المشاريع</h3>
                            <span class="srv-en-title">Project Procurement & Supply</span>
                        </div>
                        <p class="srv-scope-text">
                            تأمين خطوط الإنتاج والآلات الصناعية، البتروكيماويات، البوليمرات، حديد التسليح ومواد البناء، مع التفتيش والفحص الفني المستقل في بلد المنشأ قبل الشحن لضمان المواصفات.
                        </p>
                        <div class="srv-deliverable-box">
                            <strong>مخرجات الخدمة والضمانات:</strong>
                            شهادات فحص ومطابقة (SGS / BV)، التزام بمواصفات GSO، والتسليم بمواقع العمل.
                        </div>
                    </div>

                    <!-- Service 4 -->
                    <div class="service-matrix-item">
                        <span class="srv-code-badge">SRV-04</span>
                        <div class="srv-name-col">
                            <h3 class="srv-title">الاستشارات الائتمانية والاعتمادات</h3>
                            <span class="srv-en-title">Trade Finance & Advisory</span>
                        </div>
                        <p class="srv-scope-text">
                            هندسة شروط الدفع التجاري الآمن، صياغة ومراجعة نصوص الاعتمادات المستندية (L/C)، خطابات الضمان المصرفية (LG)، وتقديم دراسات الجدارة والملاءة الائتمانية للشركاء الدوليين.
                        </p>
                        <div class="srv-deliverable-box">
                            <strong>مخرجات الخدمة والضمانات:</strong>
                            نصوص اعتمادات معززة (UCP 600)، أدوات تحوط تقلبات الصرف، وتقليل مخاطر السداد.
                        </div>
                    </div>

                    <!-- Service 5 -->
                    <div class="service-matrix-item">
                        <span class="srv-code-badge">SRV-05</span>
                        <div class="srv-name-col">
                            <h3 class="srv-title">بنية التصنيع وهوية «صُنع في عُمان»</h3>
                            <span class="srv-en-title">Made in Oman Infrastructure</span>
                        </div>
                        <p class="srv-scope-text">
                            تمكين المستثمرين من تأسيس خطوط الإنتاج أو التصنيع التعاقدي (Toll Manufacturing)، استيفاء نسب القيمة المحلية (ICV)، والتصدير بدون جمارك بموجب اتفاقية التجارة مع أمريكا.
                        </p>
                        <div class="srv-deliverable-box">
                            <strong>مخرجات الخدمة والضمانات:</strong>
                            شهادات منشأ وطنية، إعفاء جمرکی وضريبي ۱۰۰٪، وحوافز استثمارية صناعية بمدائن.
                        </div>
                    </div>
                </div>
            </div>

            <div class="page-running-footer">
                <span class="footer-cr">س.ت: ۱۳۸۹۴۲۰ • مسقط، سلطنة عُمان</span>
                <span class="footer-confidential">وثيقة تجارية رسمية • سرية ومحمية</span>
                <span class="page-number">صفحة ٤ من ٧</span>
            </div>
        </article>


        <!-- ==============================================================
             PAGE 5: STRATEGIC PORTS & FREE ZONES (البنية التحتية)
             ============================================================== -->
        <article class="profile-page" id="page-5">
            <div class="page-running-header">
                <div class="header-brand">
                    <img src="img/logo.png" alt="Al Takamul" class="header-logo-icon">
                    <span>شركة التكامل للتجارة الدولية ش.ذ.م.م</span>
                </div>
                <span class="header-doc-code">الفصل الرابع: المحاور اللوجستية والمناطق الحرة</span>
            </div>

            <div class="page-content-flow">
                <div>
                    <span class="section-chapter-chip">الفصل الرابع • بوابات سلطنة عُمان اللوجستية</span>
                    <h2 class="page-title">موقع جيواقتصادي يربط قارات العالم خارج مضيق هرمز</h2>
                    <p class="page-subtitle">
                        تتيح البنية التحتية العمانية المتقدمة لشركة التكامل وشهدائها التجاريين النفاذ المباشر إلى خطوط الملاحة الدولية في بحر العرب والمحيط الهندي دون الخضوع للمخاطر الجيوسياسية للممرات الضيقة.
                    </p>
                </div>

                <!-- 4 Major Hubs Cards Grid -->
                <div class="card-grid-2">
                    <!-- Hub 1 -->
                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_ANCHOR}</span>
                            <div>
                                <h3 class="feature-box-title">ميناء وصناعية صحار</h3>
                                <span style="font-size: 0.75rem; color: var(--text-dim);">Sohar Port & Freezone</span>
                            </div>
                        </div>
                        <p class="feature-box-desc" style="margin-bottom: 8px;">
                            المركز الصناعي واللوجستي الأسرع نمواً في الشرق الأوسط. يتميز بغاطس عميق (۲۵ متراً) لاستقبال أضخم سفن الحاويات وناقلات البضائع السائبة، مع اتصال بري سريع بالإمارات ودول الخليج.
                        </p>
                        <ul class="bullet-list-check">
                            <li>مجمعات بتروكيماويات وصناعات معدنية ومحطة حبوب غذائية متقدمة.</li>
                            <li>منطقة حرة متكاملة توفر إعفاءات ضريبية وحرية تحويل الأرباح.</li>
                        </ul>
                    </div>

                    <!-- Hub 2 -->
                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_ANCHOR}</span>
                            <div>
                                <h3 class="feature-box-title">ميناء صلالة الاستراتيجي</h3>
                                <span style="font-size: 0.75rem; color: var(--text-dim);">Salalah Deepwater Port</span>
                            </div>
                        </div>
                        <p class="feature-box-desc" style="margin-bottom: 8px;">
                            أحد أكبر موانئ إعادة الشحن (Transshipment) في المحيط الهندي. يقع مباشرة على الخط الملاحي الرئيسي بين آسيا وأوروبا ويوفر اختصاراً زمنياً يصل إلى أسبوعين مقارنة بموانئ الخليج الداخلي.
                        </p>
                        <ul class="bullet-list-check">
                            <li>مناولة تفوق ۴.۵ مليون حاوية نمطية (TEU) سنوياً.</li>
                            <li>ممر نقل جوي - بحري متعدد الوسائط خلال ساعتين مع مطار صلالة.</li>
                        </ul>
                    </div>

                    <!-- Hub 3 -->
                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_INDUSTRY}</span>
                            <div>
                                <h3 class="feature-box-title">المنطقة الاقتصادية الخاصة بالدقم</h3>
                                <span style="font-size: 0.75rem; color: var(--text-dim);">Duqm SEZAD</span>
                            </div>
                        </div>
                        <p class="feature-box-desc" style="margin-bottom: 8px;">
                            أضخم منطقة اقتصادية خاصة في الشرق الأوسط (۲۰۰۰ كم²). مجهزة بحوض جاف ضخم لصيانة السفن، مصفاة نفط ومجمعات للصناعات الثقيلة ومشاريع إنتاج الهيدروجين الأخضر التصديرية.
                        </p>
                        <ul class="bullet-list-check">
                            <li>حوافز استثمارية وإعفاءات ضريبية تصل إلى ۳۰ عاماً قابلة للتجديد.</li>
                            <li>أراضٍ صناعية شاسعة بعقود حق انتفاع طويلة الأجل وتكلفة تفضيلية.</li>
                        </ul>
                    </div>

                    <!-- Hub 4 -->
                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_GLOBE}</span>
                            <div>
                                <h3 class="feature-box-title">مدينة خزائن والمزيونة الحرة</h3>
                                <span style="font-size: 0.75rem; color: var(--text-dim);">Khazaen & Al Mazunah</span>
                            </div>
                        </div>
                        <p class="feature-box-desc" style="margin-bottom: 8px;">
                            مدينة خزائن الاقتصادية تمثل الميناء الجاف الأحدث الرابط بين موانئ صحار ومسقط، بينما تشكل المنطقة الحرة بالمزيونة المنفذ التجاري والبري الاستراتيجي نحو الجمهورية اليمنية وشرق أفريقيا.
                        </p>
                        <ul class="bullet-list-check">
                            <li>مستودعات لوجستية وتبريد ذكي للبضائع والمواد الغذائية.</li>
                            <li>منفذ بري لتجارة الترانزیت وإعادة التصدير وتجارة الآليات والمعدات.</li>
                        </ul>
                    </div>
                </div>

                <!-- Strategic Advantages Highlight Box -->
                <div class="feature-box featured-gold" style="margin-top: 4px;">
                    <div class="feature-box-header">
                        <h4 class="feature-box-title">الحوافز والامتيازات التجارية للمناطق الحرة بعُمان</h4>
                    </div>
                    <div class="card-grid-3">
                        <div>
                            <strong style="color: var(--color-primary); display: block; font-size: 0.85rem;">إعفاء ضريبي وجمركي تام</strong>
                            <p style="font-size: 0.8rem; color: var(--text-muted);">إعفاء من ضريبة دخل الشركات وضريبة الاستيراد والتصدير بنسبة ۰٪ للبضائع العابرة.</p>
                        </div>
                        <div>
                            <strong style="color: var(--color-primary); display: block; font-size: 0.85rem;">ملكية أجنبية ۱۰۰٪</strong>
                            <p style="font-size: 0.8rem; color: var(--text-muted);">عدم اشتراط شريك محلي وحرية تامة في تحويل رأس المال والأرباح بالعملات الأجنبية.</p>
                        </div>
                        <div>
                            <strong style="color: var(--color-primary); display: block; font-size: 0.85rem;">اتفاقيات تجارة تفضيلية</strong>
                            <p style="font-size: 0.8rem; color: var(--text-muted);">النفاذ لأسواق أمريكا وسنغافورة ودول الخليج بدون حصص استيرادية أو قيود جمركية.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="page-running-footer">
                <span class="footer-cr">س.ت: ۱۳۸۹۴۲۰ • مسقط، سلطنة عُمان</span>
                <span class="footer-confidential">وثيقة تجارية رسمية • سرية ومحمية</span>
                <span class="page-number">صفحة ٥ من ٧</span>
            </div>
        </article>


        <!-- ==============================================================
             PAGE 6: OPERATIONAL WORKFLOW (آلية العمل والمسار التنفيذي)
             ============================================================== -->
        <article class="profile-page" id="page-6">
            <div class="page-running-header">
                <div class="header-brand">
                    <img src="img/logo.png" alt="Al Takamul" class="header-logo-icon">
                    <span>شركة التكامل للتجارة الدولية ش.ذ.م.م</span>
                </div>
                <span class="header-doc-code">الفصل الخامس: آلية العمل والمسار التنفيذي</span>
            </div>

            <div class="page-content-flow">
                <div>
                    <span class="section-chapter-chip">الفصل الخامس • منهجية الإنجاز وضمان الجودة</span>
                    <h2 class="page-title">المسار التنفيذي المنظم للصفقات التجارية (۶ مراحل)</h2>
                    <p class="page-subtitle">
                        نتبع منهجية مرحلية صارمة في إدارة الصفقات وسلاسل الإمداد، تضمن التحكم في التكاليف، دقة الوثائق الجمركية، والامتثال للمواصفات الفنية المعتمدة دولياً.
                    </p>
                </div>

                <!-- 6 Sequential Steps Grid -->
                <div class="pipeline-steps-grid">
                    <div class="pipeline-step-card">
                        <span class="step-phase-badge">المرحلة الأولى</span>
                        <h4 class="step-title">الدراسة والتصنيف الجمركي</h4>
                        <p class="step-desc">
                            تحليل متطلبات الصفقة، تحديد رمز النظام المنسق (HS Code)، فحص اشتراطات هيئة التقييس الخليجية (GSO)، والتحقق المالي من أهلية الأطراف.
                        </p>
                    </div>

                    <div class="pipeline-step-card">
                        <span class="step-phase-badge">المرحلة الثانية</span>
                        <h4 class="step-title">هندسة العقود والإنكوترمز</h4>
                        <p class="step-desc">
                            صياغة العقود التجارية الثنائية وفق شروط Incoterms 2020، تحديد مسؤوليات النقل والتأمين، وتضمين شروط التحكيم التجاري لحفظ الحقوق.
                        </p>
                    </div>

                    <div class="pipeline-step-card">
                        <span class="step-phase-badge">المرحلة الثالثة</span>
                        <h4 class="step-title">هيكلة أدوات الدفع المصرفي</h4>
                        <p class="step-desc">
                            تنسيق إصدار الاعتمادات المستندية غير القابلة للإلغاء (L/C) المعززة بالتعاون مع البنوك المعتمدة، أو تفعيل حسابات الضمان المشروط (Escrow).
                        </p>
                    </div>

                    <div class="pipeline-step-card">
                        <span class="step-phase-badge">المرحلة الرابعة</span>
                        <h4 class="step-title">التوريد والفحص الفني (QA)</h4>
                        <p class="step-desc">
                            متابعة تجهيز الشحنات بالمصانع المعتمدة، وإجراء الفحص المخبري والمعاينة الميدانية قبل الشحن عبر وكالات مستقلة معتمدة (SGS / BV).
                        </p>
                    </div>

                    <div class="pipeline-step-card">
                        <span class="step-phase-badge">المرحلة الخامسة</span>
                        <h4 class="step-title">الشحن والتخليص عبر بيان</h4>
                        <p class="step-desc">
                            حجز خطوط الشحن البحري أو الجوي، إصدار بوالص الشحن الرسمية، وإتمام التخليص الجمركي المسبق عبر النافذة الواحدة لجمارك عُمان (نظام بيان).
                        </p>
                    </div>

                    <div class="pipeline-step-card">
                        <span class="step-phase-badge">المرحلة السادسة</span>
                        <h4 class="step-title">التسليم وإعادة التصدير</h4>
                        <p class="step-desc">
                            نقل البضائع للمستودعات الجمركية أو مواقع المشاريع، إصدار شهادات المنشأ الرسمية، واستكمال إجراءات إعادة التصدير للأسواق الإقليمية.
                        </p>
                    </div>
                </div>

                <!-- Essential Trade Documents Framework -->
                <div class="feature-box" style="margin-top: 6px;">
                    <div class="feature-box-header">
                        <span class="feature-icon-badge">{SVG_BRIEFCASE}</span>
                        <h3 class="feature-box-title">حقيبة الوثائق والمستندات الإلزامية لكل صفقة</h3>
                    </div>
                    <div class="card-grid-3">
                        <ul class="bullet-list-check">
                            <li>فاتورة تجارية مصدقة (Commercial Invoice).</li>
                            <li>بوليصة شحن أصلية (Ocean Bill of Lading / AWB).</li>
                        </ul>
                        <ul class="bullet-list-check">
                            <li>شهادة المنشأ الرسمية (Certificate of Origin).</li>
                            <li>قائمة تعبئة تفصيلية بالأوزان (Packing List).</li>
                        </ul>
                        <ul class="bullet-list-check">
                            <li>شهادة فحص الجودة والمطابقة (Inspection Cert).</li>
                            <li>وثيقة تأمين بحري شامل (Marine Cargo Insurance).</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="page-running-footer">
                <span class="footer-cr">س.ت: ۱۳۸۹۴۲۰ • مسقط، سلطنة عُمان</span>
                <span class="footer-confidential">وثيقة تجارية رسمية • سرية ومحمية</span>
                <span class="page-number">صفحة ٦ من ٧</span>
            </div>
        </article>


        <!-- ==============================================================
             PAGE 7: CONTACTS & EXECUTIVE ENDORSEMENT (التواصل والاعتماد)
             ============================================================== -->
        <article class="profile-page" id="page-7">
            <div class="page-running-header">
                <div class="header-brand">
                    <img src="img/logo.png" alt="Al Takamul" class="header-logo-icon">
                    <span>شركة التكامل للتجارة الدولية ش.ذ.م.م</span>
                </div>
                <span class="header-doc-code">الفصل السادس: قنوات الاتصال والاعتماد الرسمي</span>
            </div>

            <div class="page-content-flow">
                <div>
                    <span class="section-chapter-chip">الفصل السادس • التواصل المؤسسي والاعتماد الرسمي</span>
                    <h2 class="page-title">المقر الرئيسي، قنوات الاتصال وبيانات التحقق</h2>
                    <p class="page-subtitle">
                        يسعد فريقنا التجاري والقانوني في مسقط باستقبال استفساراتكم ومناقشة تفاصيل مذكرات التفاهم (MoU)، عقود التوريد وتمثيل العلامات التجارية العالمية.
                    </p>
                </div>

                <!-- Contacts Directory Grid -->
                <div class="card-grid-2">
                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_BRIEFCASE}</span>
                            <h3 class="feature-box-title">المقر الرئيسي وإدارة العمليات</h3>
                        </div>
                        <ul class="bullet-list-check">
                            <li><strong>الموقع:</strong> واحة المعرفة مسقط (KOM)، مجمع الأعمال، سلطنة عُمان.</li>
                            <li><strong>السجل التجاري:</strong> CR: 1389420 • محافظة مسقط.</li>
                            <li><strong>ساعات العمل:</strong> الأحد إلى الخميس، من ۸:۰۰ ص حتى ۵:۰۰ م.</li>
                        </ul>
                    </div>

                    <div class="feature-box">
                        <div class="feature-box-header">
                            <span class="feature-icon-badge">{SVG_GLOBE}</span>
                            <h3 class="feature-box-title">قنوات الاتصال والمراسلات الرسمية</h3>
                        </div>
                        <ul class="bullet-list-check">
                            <li><strong>الهاتف المباشر وواتساب:</strong> +968 7108 1635 | +968 3153 6000</li>
                            <li><strong>البريد الإلكتروني التجاري:</strong> info@omantakamul.com</li>
                            <li><strong>البوابة الإلكترونية:</strong> https://omantakamul.com</li>
                        </ul>
                    </div>
                </div>

                <!-- Banking Desk Info -->
                <div class="legal-callout-notice" style="margin-top: 4px;">
                    <strong>مكتب التنسيق الائتماني والمصرفي:</strong> للتحقق من أرقام الحسابات الرسمية واعتمادات السويفت (SWIFT / IBAN) للتحويلات والاعتمادات المستندية، يرجى التنسيق المباشر عبر القنوات المصرفية الرسمية المعتمدة للشركة والموجهة إلى البنوك التجارية الرئيسية بمسقط (بنك مسقط / بنك ظفار).
                </div>

                <!-- Official Endorsement & Signatory Block -->
                <div class="signatory-box-grid">
                    <div>
                        <span class="section-chapter-chip" style="margin-bottom: 6px;">الاعتماد الإداري والقانوني</span>
                        <h4 style="font-family: var(--font-heading); font-size: 1rem; color: var(--color-primary-dark); margin-bottom: 6px;">
                            شركة التكامل للتجارة الدولية ش.ذ.م.م
                        </h4>
                        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 12px;">
                            صدر هذا الملف التعريفي المؤسسي لبيان القدرات التشغيلية والأنشطة التجارية المرخصة للشركة للعام ۲۰۲۶. وتعتبر كافة البيانات الواردة فيه جزءاً من الإطار التعريفي العام المنظم لعلاقات العمل والشراكات الاستثمارية.
                        </p>
                        <div style="font-size: 0.8rem; color: var(--text-main); font-weight: 700;">
                            مجلس الإدارة والإدارة التنفيذية<br>
                            <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: normal;">مسقط، سلطنة عُمان • جمادى الأولى ۱۴۴۸ هـ / نوفمبر ۲۰۲۶ م</span>
                        </div>
                    </div>

                    <!-- Seal / Stamp Graphic Box -->
                    <div class="seal-stamp-box">
                        <div class="seal-icon-svg">{SVG_SEAL}</div>
                        <div class="seal-title">ختم الاعتماد المؤسسي الرسمي</div>
                        <div class="seal-sub">AL TAKAMUL TRADING LLC • CR: 1389420</div>
                        <div style="font-size: 0.7rem; color: #10B981; font-weight: 700;">✓ وثيقة معتمدة ومسجلة</div>
                    </div>
                </div>
            </div>

            <div class="page-running-footer">
                <span class="footer-cr">س.ت: ۱۳۸۹۴۲۰ • مسقط، سلطنة عُمان</span>
                <span class="footer-confidential">وثيقة تجارية رسمية • سرية ومحمية</span>
                <span class="page-number">صفحة ٧ من ٧</span>
            </div>
        </article>

    </main>

    <!-- THEME TOGGLE SCRIPT -->
    <script>
      function toggleTheme() {{
        var current = document.documentElement.getAttribute('data-theme');
        var next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('altakamul_theme', next);
        var btn = document.getElementById('themeToggleBtn');
        if (btn) {{
          btn.textContent = next === 'dark' ? '☀️' : '🌙';
        }}
      }}
      // Set initial button icon
      (function() {{
        var current = document.documentElement.getAttribute('data-theme');
        var btn = document.getElementById('themeToggleBtn');
        if (btn) {{
          btn.textContent = current === 'dark' ? '☀️' : '🌙';
        }}
      }})();
    </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE)

with open(OUTPUT_HTML_ALT, "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE)

print("Successfully written profile.html and company-profile.html")
