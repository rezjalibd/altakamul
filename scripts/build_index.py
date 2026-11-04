import os
from generate_pages import get_header, get_footer

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'

header_html = get_header(is_root=True)
footer_html = get_footer(is_root=True)

index_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>شركة تكامل للتجارة الدولية | Al Takamul International Trading LLC</title>
  <meta name="description" content="بيت التجارة الدولية وحلول سلاسل الإمداد وتوطين الصناعة في سلطنة عُمان. الاستيراد والتصدير، توريد المشاريع، الاستشارات المالية وهوية صُنع في عُمان.">
  <link rel="icon" type="image/png" href="images/logo.png">
  
  <!-- Preload Typography -->
  <link rel="preload" href="fonts/PeydaWebFaNum-Bold.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/IRANSansXFaNum-Regular.woff2" as="font" type="font/woff2" crossorigin>

  <!-- Google Fonts for English -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css/style.css?v=4.0">
  
  <!-- Synchronous In-Memory Locale Engine -->
  <script src="js/translations_data.js"></script>
  <script src="js/main.js?v=4.0"></script>
</head>
<body>

  <!-- Ambient Animated Backdrop Mesh -->
  <div class="canvas-backdrop">
    <div class="shape-blob shape-1"></div>
    <div class="shape-blob shape-2"></div>
    <div class="shape-blob shape-3"></div>
  </div>

{header_html}

  <main class="main-wrapper">

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="section-container" style="padding-top:20px; padding-bottom:30px; position:relative;">
        <!-- Floating Geometric Shapes -->
        <div class="floating-geo-shape geo-diamond" style="top:10%; left:2%;"></div>
        <div class="floating-geo-shape geo-ring" style="bottom:12%; left:8%;"></div>

        <div class="hero-grid">
          <div>
            <div class="hero-badge">
              <span class="beacon-pulse"></span>
              <span data-i18n="hero_badge">بيت التجارة الدولية • مسقط، سلطنة عُمان</span>
            </div>
            <h1 class="hero-title">
              <span data-i18n="hero_title">بوابتكم الاستراتيجية للتجارة العالمية</span>
              <br>
              <span class="gold-gradient-text" data-i18n="hero_title_highlight">وسلاسل الإمداد وتوطين الصناعة</span>
            </h1>
            <p class="hero-subtitle" data-i18n="hero_subtitle">
              شركة تكامل للتجارة الدولية ش.م.م ، شريككم الموثوق في الاستيراد، التصدير، إدارة الصفقات الكبرى، وتمكين التصنيع بهوية «صُنع في عُمان» للنفاذ إلى الأسواق الإقليمية والدولية.
            </p>
            <div class="hero-buttons">
              <a href="./pages/request.html" class="btn-cta" data-i18n="btn_request">طلب استشارة تجارية</a>
              <a href="./pages/services.html" class="btn-secondary" data-i18n="btn_explore">استكشف خدماتنا</a>
            </div>

            <div class="hero-stats">
              <div>
                <div class="stat-val">FTA 0%</div>
                <div class="stat-label" data-i18n="stat_ftas">اتفاقيات تجارة حرة (FTA)</div>
                <div class="stat-sub" data-i18n="stat_ftas_sub">أمريكا، EFTA والدول العربية</div>
              </div>
              <div>
                <div class="stat-val">3 Hubs</div>
                <div class="stat-label" data-i18n="stat_ports">موانئ استراتيجية عالمية</div>
                <div class="stat-sub" data-i18n="stat_ports_sub">صحار، صلالة والدقم</div>
              </div>
              <div>
                <div class="stat-val">100%</div>
                <div class="stat-label" data-i18n="stat_ownership">ملكية أجنبية 100%</div>
                <div class="stat-sub" data-i18n="stat_ownership_sub">إعفاءات ضريبية وجمركية</div>
              </div>
            </div>
          </div>

          <!-- Hero Visual Card with Animated Radar -->
          <div class="hero-visual-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
              <span style="font-weight:800; font-size:0.92rem; color:var(--primary-gold);" data-i18n="radar_title">رادار الملاحة والمسارات الحية</span>
              <span style="font-size:0.75rem; color:var(--text-muted); background:var(--bg-surface-elevated); padding:3px 8px; border-radius:12px; border:1px solid var(--border-color);">
                <span class="beacon-pulse" style="width:6px; height:6px;"></span> LIVE DESK
              </span>
            </div>

            <!-- Radar Component -->
            <div class="radar-container">
              <div class="radar-grid-ring radar-ring-1"></div>
              <div class="radar-grid-ring radar-ring-2"></div>
              <div class="radar-grid-ring radar-ring-3"></div>
              <div class="radar-crosshair-h"></div>
              <div class="radar-crosshair-v"></div>
              <div class="radar-sweep"></div>
              
              <!-- Radar Blips -->
              <div class="radar-blip blip-muscat" title="Muscat HQ">
                <span class="radar-blip-label" data-i18n="radar_muscat">مسقط • المقر الرئيسي</span>
              </div>
              <div class="radar-blip blip-sohar" title="Sohar Port">
                <span class="radar-blip-label" data-i18n="radar_sohar">صحار • هاب لوجستي</span>
              </div>
              <div class="radar-blip blip-salalah" title="Salalah Port">
                <span class="radar-blip-label" data-i18n="radar_salalah">صلالة • ترانزيت</span>
              </div>
              <div class="radar-blip blip-duqm" title="Duqm SEZAD">
                <span class="radar-blip-label" data-i18n="radar_duqm">الدقم • حوض جاف</span>
              </div>
            </div>

            <div style="background:var(--bg-surface-elevated); border-radius:14px; padding:16px; border:1px solid var(--border-color);">
              <div style="display:flex; justify-content:space-between; font-size:0.84rem; margin-bottom:8px;">
                <span style="color:var(--text-muted);">OMAN CORRIDOR:</span>
                <span style="color:var(--primary-gold); font-weight:700;" data-i18n="radar_status">نشط 24/7</span>
              </div>
              <div style="font-size:0.8rem; color:var(--text-secondary); line-height:1.6;" data-i18n="footer_about">
                بيت التجارة الدولية الرائد في مسقط لتقديم خدمات التجارة العابرة للحدود، سلاسل الإمداد المتطورة، وتوطين الصناعات.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section class="section-container" id="services" style="position:relative;">
      <div class="floating-geo-shape geo-diamond" style="top:20%; right:3%;"></div>

      <div class="section-header">
        <span class="section-tag" data-i18n="tag_services">حلول تجارية متكاملة</span>
        <h2 class="section-title" data-i18n="services_title">الأركان الخمسة لمنظومة تكامل</h2>
        <p class="section-sub" data-i18n="services_sub">خدمات مؤسسية متكاملة مصممة لتمكين المستثمرين، المصنعين، والتجار من إدارة صفقاتهم بكفاءة وموثوقية عالية.</p>
      </div>

      <div class="cards-grid-3">
        <!-- Pillar 1 -->
        <div class="service-card">
          <div class="service-icon">🌐</div>
          <h3 class="service-card-title" data-i18n="service_1_title">التجارة الدولية وبيت التجارة</h3>
          <p class="service-card-desc" data-i18n="service_1_desc">عقد الصفقات الكبرى، التمثيل التجاري الحصري، وإدارة المعاملات الدولية وفق شروط الإنكوترمز مع الامتثال التجاري الكامل.</p>
          <a href="./pages/international-trade.html" class="btn-secondary" style="margin-top:auto;" data-i18n="btn_details">تفاصيل الخدمة ←</a>
        </div>

        <!-- Pillar 2 -->
        <div class="service-card">
          <div class="service-icon">🚢</div>
          <h3 class="service-card-title" data-i18n="service_2_title">الاستيراد والتصدير وإعادة التصدير</h3>
          <p class="service-card-desc" data-i18n="service_2_desc">إدارة سلاسل الإمداد العالمية، المناولة المينائية، التخليص الجمركي وإعادة التصدير بدون رسوم جمركية عبر المناطق الحرة.</p>
          <a href="./pages/import-export.html" class="btn-secondary" style="margin-top:auto;" data-i18n="btn_details">تفاصيل الخدمة ←</a>
        </div>

        <!-- Pillar 3 -->
        <div class="service-card">
          <div class="service-icon">🏗️</div>
          <h3 class="service-card-title" data-i18n="service_3_title">توريد وتأمين احتياجات المشاريع</h3>
          <p class="service-card-desc" data-i18n="service_3_desc">تأمين المواد الخام، الآلات وخطوط الإنتاج للقطاعات الحيوية مع فحص الجودة وتنسيق الشحن حتى مواقع العمل.</p>
          <a href="./pages/procurement.html" class="btn-secondary" style="margin-top:auto;" data-i18n="btn_details">تفاصيل الخدمة ←</a>
        </div>

        <!-- Pillar 4 -->
        <div class="service-card">
          <div class="service-icon">📑</div>
          <h3 class="service-card-title" data-i18n="service_4_title">الاستشارات المالية والاعتمادات</h3>
          <p class="service-card-desc" data-i18n="service_4_desc">هيكلة أدوات الدفع التجاري والاعتمادات المستندية (LC) وخطابات الضمان (LG) لتأمين المعاملات والسيولة الدولية.</p>
          <a href="./pages/financial-advisory.html" class="btn-secondary" style="margin-top:auto;" data-i18n="btn_details">تفاصيل الخدمة ←</a>
        </div>

        <!-- Pillar 5 -->
        <div class="service-card">
          <div class="service-icon">🏭</div>
          <h3 class="service-card-title" data-i18n="service_5_title">بنية التصنيع وهوية صُنع في عُمان</h3>
          <p class="service-card-desc" data-i18n="service_5_desc">تأسيس وتشغيل خطوط الإنتاج، إصدار شهادات المنشأ الوطنية، والاستفادة من اتفاقيات التجارة الحرة والإعفاءات الجمركية.</p>
          <a href="./pages/made-in-oman.html" class="btn-secondary" style="margin-top:auto;" data-i18n="btn_details">تفاصيل الخدمة ←</a>
        </div>

        <!-- Matrix Card -->
        <div class="service-card" style="background:linear-gradient(135deg, var(--bg-surface) 0%, var(--bg-surface-elevated) 100%); border-color:var(--border-gold);">
          <div class="service-icon">📊</div>
          <h3 class="service-card-title" style="color:var(--primary-gold);" data-i18n="btn_matrix">مصفوفة الخدمات المتكاملة</h3>
          <p class="service-card-desc" data-i18n="services_sub">استعرض مصفوفة التعاقد ودليل الخدمات التفصيلي مع متطلبات كل قطاع تجاري وصناعي في سلطنة عمان.</p>
          <a href="./pages/services.html" class="btn-cta" style="margin-top:auto;" data-i18n="btn_matrix">استعراض مصفوفة الخدمات ←</a>
        </div>
      </div>
    </section>

    <!-- Strategic Hubs Section with Flowing Route Lines -->
    <section class="section-container" id="hubs" style="position:relative;">
      <div class="section-header">
        <span class="section-tag" data-i18n="tag_hubs">الموانئ والمناطق الحرة</span>
        <h2 class="section-title" data-i18n="hubs_title">المحاور اللوجستية لسلطنة عُمان</h2>
        <p class="section-sub" data-i18n="hubs_sub">موقع جغرافي فريد يربط الشرق بالغرب خارج مضيق هرمز مع اتصال مباشر بأكبر خطوط الملاحة البحرية العالمية.</p>
      </div>

      <!-- Animated SVG Route Connector -->
      <svg class="route-connector-svg" viewBox="0 0 900 40">
        <path class="route-connector-line" d="M 50 20 Q 250 5 450 20 T 850 20" />
      </svg>

      <div class="cards-grid-3">
        <div class="hub-card">
          <div style="font-size:2rem; margin-bottom:14px;">⚓</div>
          <h3 class="hub-card-title" data-i18n="hub_1_title">ميناء وصناعية صحار</h3>
          <p style="font-size:0.92rem; color:var(--text-secondary); line-height:1.75;" data-i18n="hub_1_desc">
            المركز الصناعي واللوجستي الأسرع نمواً في الشرق الأوسط، يقع بالقرب من أسواق الإمارات ودول الخليج، ويتميز باتصال مباشر بشبكة الطرق الإقليمية.
          </p>
        </div>

        <div class="hub-card">
          <div style="font-size:2rem; margin-bottom:14px;">🌊</div>
          <h3 class="hub-card-title" data-i18n="hub_2_title">ميناء صلالة الاستراتيجي</h3>
          <p style="font-size:0.92rem; color:var(--text-secondary); line-height:1.75;" data-i18n="hub_2_desc">
            هاب إعادة شحن حاويات رئيسي على خط الملاحة بين آسيا وأوروبا، يربط مباشرة بشرق أفريقيا والمحيط الهندي دون الحاجة لدخول مياه الخليج.
          </p>
        </div>

        <div class="hub-card">
          <div style="font-size:2rem; margin-bottom:14px;">🏗️</div>
          <h3 class="hub-card-title" data-i18n="hub_3_title">المنطقة الاقتصادية بالدقم</h3>
          <p style="font-size:0.92rem; color:var(--text-secondary); line-height:1.75;" data-i18n="hub_3_desc">
            أكبر منطقة اقتصادية خاصة في الشرق الأوسط وشمال أفريقيا، مجهزة بحوض جاف، مصفاة بتروكيماويات، ومناطق صناعية وتعدينية شاسعة.
          </p>
        </div>
      </div>
    </section>

    <!-- Execution Workflow Section with Rotating Rings -->
    <section class="section-container" id="process" style="position:relative;">
      <div class="floating-geo-shape geo-ring" style="top:15%; right:5%;"></div>

      <div class="section-header">
        <span class="section-tag" data-i18n="tag_workflow">منظومة الإنجاز</span>
        <h2 class="section-title" data-i18n="workflow_title">آلية تنفيذ العمليات والصفقات</h2>
        <p class="section-sub" data-i18n="workflow_sub">منهجية دقيقة ومنظمة تضمن الأمان القانوني والمالي وسرعة تدفق البضائع عبر الحدود.</p>
      </div>

      <div class="process-grid">
        <div class="process-step-card">
          <div class="step-num-badge" data-i18n="step_1_num">١</div>
          <h3 style="font-size:1.15rem; font-weight:800; margin-bottom:10px;" data-i18n="step_1_title">التشخيص ودراسة المتطلبات</h3>
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.7;" data-i18n="step_1_desc">تحليل دقيق للبضاعة، الأسواق المستهدفة، التكاليف الجمركية والاتفاقيات التجارية المتاحة.</p>
        </div>

        <div class="process-step-card">
          <div class="step-num-badge" data-i18n="step_2_num">٢</div>
          <h3 style="font-size:1.15rem; font-weight:800; margin-bottom:10px;" data-i18n="step_2_title">هندسة الصفقة والتعاقد</h3>
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.7;" data-i18n="step_2_desc">صياغة العقود المتوافقة مع القانون التجاري العماني والدولي وضمان حقوق الأطراف.</p>
        </div>

        <div class="process-step-card">
          <div class="step-num-badge" data-i18n="step_3_num">٣</div>
          <h3 style="font-size:1.15rem; font-weight:800; margin-bottom:10px;" data-i18n="step_3_title">التنفيذ والشحن والتخليص</h3>
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.7;" data-i18n="step_3_desc">إدارة المستندات، الشحن البحري أو الجوي، وإجراءات التخليص الجمركي الصارمة.</p>
        </div>

        <div class="process-step-card">
          <div class="step-num-badge" data-i18n="step_4_num">٤</div>
          <h3 style="font-size:1.15rem; font-weight:800; margin-bottom:10px;" data-i18n="step_4_title">التسليم والدعم المستمر</h3>
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.7;" data-i18n="step_4_desc">وصول البضاعة للمستودعات أو موانئ الوصول وتقديم المتابعة والتقارير الدورية.</p>
        </div>
      </div>
    </section>

    <!-- Key Advantages Section -->
    <section class="section-container" style="position:relative;">
      <div class="section-header">
        <span class="section-tag" data-i18n="tag_advantages">القيمة المضافة</span>
        <h2 class="section-title" data-i18n="adv_title">لماذا تختار شركة تكامل؟</h2>
        <p class="section-sub" data-i18n="adv_sub">حلول متقدمة تجمع بين الخبرة الميدانية العمیقة والشبكة الواسعة في سلطنة عُمان والأسواق العالمية.</p>
      </div>

      <div class="cards-grid-3">
        <div class="service-card">
          <div class="service-icon">⚖️</div>
          <h3 class="service-card-title" data-i18n="adv_1_title">امتثال قانوني ومصرفي صارم</h3>
          <p class="service-card-desc" data-i18n="adv_1_desc">تطبيق أعلى معايير الشفافية والتوافق مع اللوائح المصرفية وغرف التجارة الدولية.</p>
        </div>

        <div class="service-card">
          <div class="service-icon">🌐</div>
          <h3 class="service-card-title" data-i18n="adv_2_title">شبكة إمداد عالمية موثوقة</h3>
          <p class="service-card-desc" data-i18n="adv_2_desc">ارتباط مباشر مع كبرى خطوط الشحن، المصانع المعتمدة، والموردين الاستراتيجيين.</p>
        </div>

        <div class="service-card">
          <div class="service-icon">🏷️</div>
          <h3 class="service-card-title" data-i18n="adv_3_title">استفادة قصوى من اتفاقيات FTA</h3>
          <p class="service-card-desc" data-i18n="adv_3_desc">تخفيض التكاليف الجمركية إلى الصفر للمنتجات المؤهلة بشهادة المنشأ العمانية.</p>
        </div>
      </div>
    </section>

    <!-- Spaced FAQ Accordion -->
    <section class="section-container" id="faq">
      <div class="section-header">
        <span class="section-tag" data-i18n="nav_faq">الأسئلة الشائعة</span>
        <h2 class="section-title" data-i18n="faq_heading">الأسئلة الشائعة</h2>
        <p class="section-sub" data-i18n="faq_sub">إجابات وافية حول آليات العمل، التعرفة الجمركية، والشراكة التجارية مع شركة تكامل.</p>
      </div>

      <div class="faq-grid">
        <div class="faq-item" onclick="toggleFaq(this)">
          <div class="faq-q" data-i18n="faq_1_q">ما هي المزايا الاستراتيجية للتجارة عبر سلطنة عُمان؟</div>
          <div class="faq-a" data-i18n="faq_1_a">تتمتع سلطنة عُمان بموقع استراتيجي خارج مضيق هرمز على خطوط الملاحة الدولية، مع اتفاقية تجارة حرة (FTA) مع الولايات المتحدة الأمريكية تمنح إعفاءً جمركياً كاملاً للمنتجات الوطنية، بالإضافة إلى بنية تحتية فائقة ومناطق حرة توفر تملكاً أجنبياً بنسبة 100% وإعفاءات ضريبية واسعة.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
          <div class="faq-q" data-i18n="faq_2_q">كيف تدعم شركة تكامل مشاريع وسم «صُنع في عُمان»؟</div>
          <div class="faq-a" data-i18n="faq_2_a">نساعد الشركات في تقييم الجدوى الصناعية، استيفاء معايير القيمة المحلية المضافة (ICV)، الحصول على التراخيص والموافقات من وزارة التجارة والصناعة وترويج الاستثمار، وإصدار شهادات المنشأ الوطنية للاستفادة من المزايا التصديرية المعفاة جمركياً.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
          <div class="faq-q" data-i18n="faq_3_q">هل تقدم شركة تكامل تمويلاً مباشراً أو قروضاً؟</div>
          <div class="faq-a" data-i18n="faq_3_a">لا. شركة تكامل ليست مؤسسة مصرفية أو مانحة للقروض. نحن نقدم استشارات متخصصة في هندسة الدفع التجاري، إدارة الاعتمادات المستندية (LC) وخطابات الضمان (LG) بالتعاون مع البنوك المعتمدة لتأمين المعاملات والسيولة.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
          <div class="faq-q" data-i18n="faq_4_q">ما هي شروط الإنكوترمز التي تديرونها في صفقاتكم؟</div>
          <div class="faq-a" data-i18n="faq_4_a">ندير كافة شروط التسليم الدولية بما في ذلك FOB، CIF، CFR، DAP، وDDP، ونتولى التنسيق اللوجستي، التأمين، والتخليص الجمركي وفق أعلى المعايير المهنية المعتمدة دولياً.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
          <div class="faq-q" data-i18n="faq_5_q">هل تشترطون نوعاً محدداً من البضائع أو السلع؟</div>
          <div class="faq-a" data-i18n="faq_5_a">نطاق عملنا كبيت تجارة دولية يغطي معظم السلع الصناعية، المواد الخام، المواد الغذائية، والمعدات الكبرى، مع اشتراط توافق البضائع الكامل مع القوانين واللوائح العمانية والدولية المعمول بها.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
          <div class="faq-q" data-i18n="faq_6_q">كيف تضمنون سرية معلومات الشركاء والموردين؟</div>
          <div class="faq-a" data-i18n="faq_6_a">نوقع اتفاقيات سرية معلومات ملزمة قانوناً (NDA) قبل بدء أي محادثات تجارية، ونلتزم بأعلى معايير الحوكمة لحماية بيانات الشركاء واستراتيجياتهم التجارية.</div>
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="section-container" style="padding-top:20px;">
      <div style="background:linear-gradient(135deg, var(--bg-surface) 0%, var(--bg-surface-elevated) 100%); border:1px solid var(--border-gold); border-radius:24px; padding:45px 30px; text-align:center; box-shadow:var(--shadow-md); position:relative; overflow:hidden;">
        <div class="floating-geo-shape geo-diamond" style="top:10%; right:8%;"></div>
        <h2 style="font-size:2rem; font-weight:800; margin-bottom:14px;" data-i18n="cta_box_title">جاهزون لتوسيع تجارتكم وتأسيس حضوركم في سلطنة عُمان؟</h2>
        <p style="font-size:1.05rem; color:var(--text-secondary); max-width:700px; margin:0 auto 28px;" data-i18n="cta_box_sub">تواصلوا مع فريقنا التجاري المتخصص لدراسة صفقتكم المقبلة أو مناقشة تأسيس خطوط الإنتاج.</p>
        <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
          <a href="./pages/request.html" class="btn-cta" data-i18n="btn_request">طلب استشارة تجارية</a>
          <a href="https://wa.me/96871081635" target="_blank" rel="noopener" class="btn-secondary">تواصل عبر واتساب</a>
        </div>
      </div>
    </section>

  </main>

{footer_html}

</body>
</html>'''

with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Immaculate index.html built successfully with Radar, Living Shapes, and Full i18n!")
