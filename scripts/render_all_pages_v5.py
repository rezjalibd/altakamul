import json, os
from generate_all_subpages_v5 import get_head, get_header, get_footer

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'
PAGES_DIR = os.path.join(BASE_DIR, 'pages')

with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
    t = json.load(f)

# Common Breadcrumb component
def breadcrumb(title_key, default_title):
    return f'''  <div class="breadcrumb" style="max-width:1280px; margin:20px auto 0; padding:0 24px; font-size:0.85rem; color:var(--text-muted);">
    <a href="../index.html" style="color:var(--text-muted); text-decoration:none;" data-i18n="nav_home">الرئيسية</a>
    <span style="margin:0 8px;">/</span>
    <span style="color:var(--primary-gold);" data-i18n="{title_key}">{default_title}</span>
  </div>'''

# Common CTA Section
def cta_block():
    return '''  <section class="section-container" style="padding-top:20px; padding-bottom:80px;">
    <div style="background:var(--brand-gradient); border:1px solid var(--border-gold); border-radius:28px; padding:50px 36px; text-align:center; position:relative; overflow:hidden; box-shadow:var(--shadow-lg);">
      <div style="position:relative; z-index:2; max-width:760px; margin:0 auto;">
        <span class="section-tag" style="background:rgba(255,255,255,0.1); color:#FDE68A; border-color:rgba(253,230,138,0.4);" data-i18n="cta_tag">بدء التعاون الاستراتيجي</span>
        <h2 style="font-size:2.2rem; font-weight:800; color:#FFFFFF; margin:16px 0;" data-i18n="cta_title">هل تخطط لتوسيع تجارتك الدولية أو توريد شحناتك عبر عُمان؟</h2>
        <p style="font-size:1.05rem; color:#E2E8F0; margin-bottom:32px; line-height:1.75;" data-i18n="cta_sub">فريقنا القانوني والتجاري واللوجستي جاهز لدراسة متطلباتك وتقديم حلول مخصصة لحماية رأس مالك وتسريع إنجاز الصفقات.</p>
        <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
          <a href="./request.html" class="btn-cta" style="padding:14px 32px; font-size:1rem;" data-i18n="btn_request">طلب استشارة تجارية</a>
          <a href="./contact.html" class="btn-secondary" style="padding:14px 32px; font-size:1rem;" data-i18n="nav_contact">اتصل بنا مباشرة</a>
        </div>
      </div>
    </div>
  </section>'''

# 1. PAGE: HUBS.HTML
def build_hubs_page():
    content = f'''{get_head("بوابات عمان البحرية والمناطق الاقتصادية الخاصة | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("nav_hubs", "الموانئ والمناطق الحرة")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="hubs_page_tag">البنية اللوجستية الاستراتيجية</span>
      <h1 class="section-title" data-i18n="hubs_page_title">بوابات عمان البحرية والمناطق الاقتصادية الخاصة</h1>
      <p class="section-sub" data-i18n="hubs_page_sub">موقع جيوسياسي فريد خارج مضيق هرمز يربط خطوط الملاحة بين آسيا وأوروبا وأفريقيا مع إعفاءات جمركية وضريبية تصل إلى 100%.</p>
    </div>

    <!-- Stat Highlights -->
    <div class="stats-grid" style="margin-bottom:60px;">
      <div class="stat-card">
        <div class="stat-val" data-i18n="hubs_stat_1_val">خارج هرمز</div>
        <div class="stat-label" data-i18n="hubs_stat_1_lbl">ممر بحري مفتوح 100%</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" data-i18n="hubs_stat_2_val">0% ضرائب</div>
        <div class="stat-label" data-i18n="hubs_stat_2_lbl">إعفاء ضريبي يصل لـ 25 عاماً</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" data-i18n="hubs_stat_3_val">100% تملك</div>
        <div class="stat-label" data-i18n="hubs_stat_3_lbl">حرية كاملة لتحويل الأرباح</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" data-i18n="hubs_stat_4_val">اتفاقيات FTA</div>
        <div class="stat-label" data-i18n="hubs_stat_4_lbl">تجارة حرة مع أمريكا ودول الخليج</div>
      </div>
    </div>

    <!-- Hubs Detailed Cards -->
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="hubs_sec1_tag">المراكز اللوجستية المحورية</span>
      <h2 class="section-title" data-i18n="hubs_sec1_title">أربعة مراكز عالمية تدير تدفقات التجارة الدولية</h2>
      <p class="section-sub" data-i18n="hubs_sec1_sub">تتكامل الموانئ والمناطق الحرة في سلطنة عمان لتقديم حلول شاملة للتخزين، التوزيع، وإعادة التصدير.</p>
    </div>

    <div style="display:flex; flex-direction:column; gap:36px; margin-bottom:70px;">
      <!-- Sohar -->
      <div id="sohar" class="service-card" style="padding:40px;">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">
          <div style="width:52px; height:52px; border-radius:14px; background:rgba(197,160,89,0.15); display:flex; align-items:center; justify-content:center; color:var(--primary-gold); font-size:1.5rem;">⚓</div>
          <div>
            <h3 class="service-card-title" style="font-size:1.45rem;" data-i18n="hub_sohar_full_title">ميناء ومنطقة صحار الحرة (Sohar Port & Freezone)</h3>
            <span style="font-size:0.85rem; color:var(--primary-gold); font-weight:700;">بوابة الخليج الشمالية • عمق بحري 25 متراً</span>
          </div>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:24px;" data-i18n="hub_sohar_full_desc">المركز الصناعي واللوجستي الأسرع نمواً في الشرق الأوسط. يتميز برباط مباشر مع شبكة الطرق السريعة لدولة الإمارات العربية المتحدة ودول الخليج، مع محطات مخصصة للبتروكيماويات، المعادن، والمواد الغذائية السائبة وغاطس بحري يصل إلى 25 متراً.</p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_sohar_f1">غاطس بحري عميق لاستقبال أضخم سفن الحاويات والصب الجاف</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_sohar_f2">مجمع غذائي وصناعي متكامل مع صوامع ومخازن تحت المظلة الجمركية</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_sohar_f3">بوابة مباشرة وسريعة للسوق الإماراتي والخليجي عبر المنافذ البرية</span></div>
        </div>
      </div>

      <!-- Salalah -->
      <div id="salalah" class="service-card" style="padding:40px;">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">
          <div style="width:52px; height:52px; border-radius:14px; background:rgba(197,160,89,0.15); display:flex; align-items:center; justify-content:center; color:var(--primary-gold); font-size:1.5rem;">🌊</div>
          <div>
            <h3 class="service-card-title" style="font-size:1.45rem;" data-i18n="hub_salalah_full_title">ميناء ومنطقة صلالة الحرة (Salalah Port & Freezone)</h3>
            <span style="font-size:0.85rem; color:var(--primary-gold); font-weight:700;">المحيط الهندي • محطة الترانشیب العالمية</span>
          </div>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:24px;" data-i18n="hub_salalah_full_desc">أكبر ميناء لمناولة الحاويات العابرة في سلطنة عُمان على المحيط الهندي مباشرة. يختصر زمن الإبحار إلى أوروبا وأمريكا وأفريقيا بنحو أسبوعين مقارنة بموانئ الخليج العربي الداخلية، مع ممر شحن جوي-بحري يربطه بمطار صلالة الدولي في أقل من ساعتين.</p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_salalah_f1">موقع محيطي مباشر يتجاوز كافة مضائق التوتر الجيوسياسي الإقليمي</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_salalah_f2">محطات حاويات عالمية بمناولة تتجاوز 4.5 مليون حاوية نمطية سنوياً</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_salalah_f3">بنية لوجستية متطورة للأدوية والأغذية المبردة وسلاسل التبريد العميقة</span></div>
        </div>
      </div>

      <!-- Duqm -->
      <div id="duqm" class="service-card" style="padding:40px;">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">
          <div style="width:52px; height:52px; border-radius:14px; background:rgba(197,160,89,0.15); display:flex; align-items:center; justify-content:center; color:var(--primary-gold); font-size:1.5rem;">🏗️</div>
          <div>
            <h3 class="service-card-title" style="font-size:1.45rem;" data-i18n="hub_duqm_full_title">المنطقة الاقتصادية الخاصة بالدقم (SEZAD)</h3>
            <span style="font-size:0.85rem; color:var(--primary-gold); font-weight:700;">أكبر منطقة اقتصادية • 2,000 كم² • الحوض الجاف العالمي</span>
          </div>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:24px;" data-i18n="hub_duqm_full_desc">أضخم مشروع اقتصادي متكامل في الشرق الأوسط بمساحة 2,000 كم². يضم ميناء الدقم التجاري المتعدد الأغراض، الحوض الجاف لإصلاح السفن العملاقة، مصفاة الدقم، ومجمعات الهيدروجين الأخضر والصناعات الثقيلة ومستودعات التخزين الاستراتيجي للنفط والغاز والبضائع.</p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_duqm_f1">حوض جاف عالمي متقدم لصيانة وإصلاح ناقلات النفط وسفن الصب</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_duqm_f2">أراضي صناعية ولوجستية بمساحات غير محدودة وعقود انتفاع طويلة الأمد</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_duqm_f3">منظومة إعفاءات ضريبية وحوافز استثمارية ملكية بنسبة 100%</span></div>
        </div>
      </div>

      <!-- Khazaen & Mazunah -->
      <div id="khazaen" class="service-card" style="padding:40px;">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">
          <div style="width:52px; height:52px; border-radius:14px; background:rgba(197,160,89,0.15); display:flex; align-items:center; justify-content:center; color:var(--primary-gold); font-size:1.5rem;">🚚</div>
          <div>
            <h3 class="service-card-title" style="font-size:1.45rem;" data-i18n="hub_khazaen_full_title">مدينة خزائن الاقتصادية والمنطقة الحرة بالمزيونة</h3>
            <span style="font-size:0.85rem; color:var(--primary-gold); font-weight:700;">الميناء الجاف بمسقط • بوابة الترانزيت البري لليمن وأفريقيا</span>
          </div>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:24px;" data-i18n="hub_khazaen_full_desc">خزائن هي الميناء الجاف والمركز اللوجستي الأوسط الرابط بين مسقط وصحار، بينما المزيونة تمثل المنفذ البري الاستراتيجي لتجارة الترانزيت نحو الجمهورية اليمنية وأسواق شرق أفريقيا مع مزايا تجارة تفضيلية للمصدرين والمستوردين.</p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_khazaen_f1">ميناء جاف ذكي يربط محطات الحاويات البحرية بالعاصمة مسقط</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_khazaen_f2">منفذ بري متكامل لتجارة إعادة التصدير والترانزيت إلى الأسواق المجاورة</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:14px 18px; font-size:0.92rem; color:var(--text-secondary);">✔ <span data-i18n="hub_khazaen_f3">مستودعات مكيفة وحلول تخزين ذكية قصيرة وطويلة الأجل</span></div>
        </div>
      </div>
    </div>

    <!-- On-Site Al Takamul Services -->
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="hubs_services_tag">خدمات تكامل الميدانية</span>
      <h2 class="section-title" data-i18n="hubs_services_title">كيف تمكنك تكامل من استثمار مزايا المناطق الحرة؟</h2>
      <p class="section-sub" data-i18n="hubs_services_sub">نوفر المظلة التجارية، القانونية، واللوجستية الكاملة للشركات الدولية الراغبة في تأسيس أعمالها أو عبور شحناتها عبر عُمان.</p>
    </div>

    <div class="cards-grid-4" style="margin-bottom:70px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="hubs_serv1_title">التخليص الجمركي الذكي عبر نظام بيان (Bayan)</h3>
        <p class="service-card-desc" data-i18n="hubs_serv1_desc">تسجيل وتخليص الشحنات مسبقاً قبل وصول السفن، وإصدار المعاملات الجمركية تحت بند الإعفاءات المعمول بها في المناطق الحرة دون تأخير.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="hubs_serv2_title">إدارة المستودعات الجمركية (Bonded Warehousing)</h3>
        <p class="service-card-desc" data-i18n="hubs_serv2_desc">تأمين مساحات تخزين جافة ومبردة داخل النطاق الجمركي المعفى لتخزين البضائع وإعادة تعبئتها وفرزها دون سداد أي رسوم جمركية مسبقة.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="hubs_serv3_title">إصدار شهادات المنشأ والعبور الترانزيت</h3>
        <p class="service-card-desc" data-i18n="hubs_serv3_desc">توثيق عمليات إعادة التصدير عبر غرفة تجارة وصناعة عُمان والجهات المختصة للاستفادة من الاتفاقيات التجارية الخليجية والدولية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="hubs_serv4_title">التمثيل القانوني وعقود الانتفاع الاستثماري</h3>
        <p class="service-card-desc" data-i18n="hubs_serv4_desc">صياغة وتوقيع عقود استئجار الأراضي والمكاتب الصناعية مع إدارات المناطق الحرة وتوفير الغطاء التجاري المسجل رسمياً.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'hubs.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/hubs.html")

# 2. PAGE: PROCESS.HTML
def build_process_page():
    content = f'''{get_head("آلية العمل والمسار التنفيذي الشامل | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("nav_process", "آلية العمل")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="proc_page_tag">حوكمة العمليات التجارية</span>
      <h1 class="section-title" data-i18n="proc_page_title">آلية العمل والمسار التنفيذي الشامل للصفقات</h1>
      <p class="section-sub" data-i18n="proc_page_sub">منهجية مؤسسية صارمة من 6 مراحل تضمن أمان التدفقات المالية، مطابقة المواصفات القياسية، والتسليم الدقيق وفق الإنكوترمز 2020.</p>
    </div>

    <!-- 6 Detailed Process Steps -->
    <div style="display:flex; flex-direction:column; gap:28px; margin-bottom:70px;">
      <!-- Step 1 -->
      <div class="service-card" style="padding:36px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:64px; height:64px; border-radius:18px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.6rem; box-shadow:0 8px 24px rgba(197,160,89,0.3);">
          01
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step1_badge">المرحلة الأولى</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step1_title">دراسة الجدوى والتدقيق التنظيمي والمطابقة</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step1_desc">دراسة كود النظام المنسق للبضائع (HS Code)، فحص المتطلبات الفنية والمواصفات القياسية الخليجية (GSO)، والتحقق من الملاءة المالية والقانونية للمصنعين والمشترين من خلال سجلات التدقيق المالي المعتمدة.</p>
        </div>
      </div>

      <!-- Step 2 -->
      <div class="service-card" style="padding:36px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:64px; height:64px; border-radius:18px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.6rem; box-shadow:0 8px 24px rgba(197,160,89,0.3);">
          02
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step2_badge">المرحلة الثانية</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step2_title">صياغة العقود التجارية وهيكلة الإنكوترمز</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step2_desc">إعداد عقود بيع وشراء دولية ملزمة ثنائية اللغة، تحدد بدقة مسؤوليات الشحن والتأمين والمخاطر وفق (Incoterms 2020) مثل FOB, CIF, DAP, DDP مع إدراج شروط التحكيم التجاري المعتمدة في سلطنة عمان.</p>
        </div>
      </div>

      <!-- Step 3 -->
      <div class="service-card" style="padding:36px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:64px; height:64px; border-radius:18px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.6rem; box-shadow:0 8px 24px rgba(197,160,89,0.3);">
          03
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step3_badge">المرحلة الثالثة</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step3_title">هندسة الدفع والضمانات المصرفية (L/C & Escrow)</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step3_desc">فتح وإدارة الاعتمادات المستندية غير القابلة للإلغاء المعززة (Irrevocable Confirmed L/C) أو الضمانات البنكية (Performance Bonds) وحسابات الضمان المعلقة (Escrow) عبر بنوك عُمانية ودولية رائدة لحماية السيولة وحقوق الشركاء.</p>
        </div>
      </div>

      <!-- Step 4 -->
      <div class="service-card" style="padding:36px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:64px; height:64px; border-radius:18px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.6rem; box-shadow:0 8px 24px rgba(197,160,89,0.3);">
          04
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step4_badge">المرحلة الرابعة</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step4_title">المطابقة ومراقبة الجودة والفحص قبل الشحن</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step4_desc">متابعة خطوط الإنتاج وسحب العينات الفنية وإجراء الفحوصات المخبرية عبر شركات فحص دولية مستقلة (مثل SGS أو Bureau Veritas) وإصدار شهادة المطابقة المسبقة (Certificate of Conformity) المعتمدة قبل السماح بتحميل الشحنة.</p>
        </div>
      </div>

      <!-- Step 5 -->
      <div class="service-card" style="padding:36px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:64px; height:64px; border-radius:18px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.6rem; box-shadow:0 8px 24px rgba(197,160,89,0.3);">
          05
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step5_badge">المرحلة الخامسة</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step5_title">اللوجستيات والتخليص الجمركي في نظام بيان</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step5_desc">حجز مساحات الشحن البحري أو الجوي، إصدار بوالص الشحن الرسمية (Bill of Lading)، وتفعيل التخليص الإلكتروني المسبق في نظام 'بيان' الجمركي التابع لشرطة عمان السلطانية، واستيفاء كافة الموافقات الصحية والبيئية فور الرسو.</p>
        </div>
      </div>

      <!-- Step 6 -->
      <div class="service-card" style="padding:36px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:64px; height:64px; border-radius:18px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.6rem; box-shadow:0 8px 24px rgba(197,160,89,0.3);">
          06
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step6_badge">المرحلة السادسة</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step6_title">التفريغ، التخزين، والتسليم النهائي أو التصدير</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step6_desc">تفريغ الشحنات في المستودعات الجمركية أو المخازن المركزية، وتنسيق النقل البري إلى موقع العميل النهائي، أو إعادة الشحن للأسواق الإقليمية مصحوبة بشهادة منشأ عُمانية رسمية تسجل القيمة المضافة.</p>
        </div>
      </div>
    </div>

    <!-- Required Trade Documents Grid -->
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="proc_docs_tag">التوثيق القانوني والجمركي</span>
      <h2 class="section-title" data-i18n="proc_docs_title">قائمة الوثائق الإلزامية لحماية الصفقات التجارية</h2>
      <p class="section-sub" data-i18n="proc_docs_sub">تلتزم تكامل بإعداد وتدقيق حزمة الوثائق الكاملة لضمان سرعة الإفراج الجمركي وعدم تحمل أي غرامات تأخير أو رسوم أرضيات.</p>
    </div>

    <div class="cards-grid-3" style="margin-bottom:70px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_inv_title">الفاتورة التجارية المصدقة (Commercial Invoice)</h3>
        <p class="service-card-desc" data-i18n="doc_inv_desc">تتضمن وصفاً دقيقاً للبضائع، البنود الجمركية، شروط الإنكوترمز، ومصدقة حسب الأصول من غرفة التجارة والسفارة المعنية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_bl_title">بوليصة الشحن الأصلية (Bill of Lading / AWB)</h3>
        <p class="service-card-desc" data-i18n="doc_bl_desc">سند الملكية النهائي الصادر عن الخط الملاحي أو شركة الطيران، يحدد ميناء التحميل وميناء التفريغ وجهة الاستلام.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_co_title">شهادة المنشأ الرسمية (Certificate of Origin)</h3>
        <p class="service-card-desc" data-i18n="doc_co_desc">إثبات قانوني لمصدر البضائع للاستفادة من الإعفاءات الجمركية الخليجية واتفاقيات التجارة الحرة وتفادي أي تعريفات حمائية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_pack_title">قائمة التعبئة والأوزان (Packing List)</h3>
        <p class="service-card-desc" data-i18n="doc_pack_desc">تفصيل دقيق لعدد الطرود، الحاويات، الأوزان الإجمالية والصافية، وأبعاد الصناديق لتسهيل الفحص الجمركي والتفريغ.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_cert_title">شهادة الفحص والمطابقة (Inspection Certificate)</h3>
        <p class="service-card-desc" data-i18n="doc_cert_desc">تقرير فني معتمد صادر عن وكالات الفحص المستقلة يثبت خلو الشحنة من العيوب ومطابقتها للمواصفات الفنية التعاقدية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_ins_title">بوليصة التأمين البحري (Marine Cargo Insurance)</h3>
        <p class="service-card-desc" data-i18n="doc_ins_desc">تغطية تأمينية شاملة وفق شروط معهد المكتتبين بلندن (Institute Cargo Clauses A) لحماية رأس المال ضد المخاطر البحرية.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'process.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/process.html")

build_hubs_page()
build_process_page()

# 3. PAGE: ABOUT.HTML
def build_about_page():
    content = f'''{get_head("من نحن ورؤيتنا الاستراتيجية | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("nav_about", "من نحن")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_about_tag">الهوية المؤسسية والترخيص</span>
      <h1 class="section-title" data-i18n="page_about_title">ريادة في إدارة صفقات التجارة الدولية وتطوير سلاسل الإمداد</h1>
      <p class="section-sub" data-i18n="page_about_sub">شركة تكامل للتجارة الدولية ش.م.م، بيت تجارة عُماني رائد يتخذ من العاصمة مسقط مقراً لربط الأسواق العالمية بمنطقة الخليج والشرق الأوسط.</p>
    </div>

    <!-- Governance & Regulatory Highlights -->
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="about_sec_gov_tag">الحوكمة والامتثال القانوني</span>
      <h2 class="section-title" data-i18n="about_sec_gov_title">كيان تجاري مسجل وفق أرقى المعايير التنظيمية العمانية</h2>
      <p class="section-sub" data-i18n="about_sec_gov_sub">تلتزم شركة تكامل للتجارة الدولية (سجل تجاري: 1389420) بأعلى معايير الشفافية المالية والامتثال لأنظمة التجارة الدولية ومكافحة غسيل الأموال.</p>
    </div>

    <div class="cards-grid-3" style="margin-bottom:70px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="about_card_reg_title">السجل التجاري والترخيص الأساسي</h3>
        <p class="service-card-desc" data-i18n="about_card_reg_desc">سجل تجاري رقم 1389420 مسجل لدى وزارة التجارة والصناعة وترويج الاستثمار، بعضوية معتمدة في غرفة تجارة وصناعة عمان لتمثيل التجارة العامة والتصدير والاستيراد.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="about_card_v2040_title">التوافق مع رؤية عمان 2040</h3>
        <p class="service-card-desc" data-i18n="about_card_v2040_desc">دعم أهداف التنويع الاقتصادي الوطني عبر ترسيخ سلطنة عمان كمركز لوجستي محوري يربط التجارة الإقليمية بالأسواق الدولية وتوطين الصناعات ذات القيمة المضافة.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="about_card_risk_title">إدارة المخاطر والشفافية المصرفية</h3>
        <p class="service-card-desc" data-i18n="about_card_risk_desc">معاملات خاضعة للتدقيق المستندي المستقل، مع قنوات مصرفية موثوقة وعقود تجارية تخضع لقوانين التحكيم التجاري المعتمدة دولياً ومحلياً.</p>
      </div>
    </div>

    <!-- 4 Pillars Section -->
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="about_sec_pillars_tag">الأركان المؤسسية</span>
      <h2 class="section-title" data-i18n="about_sec_pillars_title">الركائز الأربع التي تبنى عليها صفقات تكامل</h2>
    </div>

    <div class="cards-grid-4" style="margin-bottom:70px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="about_pil_1_title">السرعة والدقة في التنفيذ اللوجستي</h3>
        <p class="service-card-desc" data-i18n="about_pil_1_desc">تقليص زمن عبور الحاويات والتخليص الجمركي المسبق عبر نظام بيان الإلكتروني لتفادي أي غرامات تأخير أو رسوم تخزين.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="about_pil_2_title">الأمان المالي والاعتمادات المستندية</h3>
        <p class="service-card-desc" data-i18n="about_pil_2_desc">استخدام هياكل دفع بنكية متطورة واعتمادات مستندية معززة غير قابلة للإلغاء لحماية أموال المشترين والموردين.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="about_pil_3_title">الجودة المطابقة للمواصفات العالمية</h3>
        <p class="service-card-desc" data-i18n="about_pil_3_desc">فحص البضائع عبر وكالات تفتيش دولية مستقلة وإصدار شهادات المطابقة القياسية (CoC) قبل مغادرة موانئ الشحن.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="about_pil_4_title">المرونة الجيوسياسية خارج المضائق</h3>
        <p class="service-card-desc" data-i18n="about_pil_4_desc">تأمين تدفقات الإمداد عبر موانئ عمان المطلة على المحيط الهندي وبحر العرب بعيداً عن التوترات الإقليمية.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/about.html")

# 4. PAGE: INTERNATIONAL-TRADE.HTML
def build_international_trade_page():
    content = f'''{get_head("التجارة الدولية وبيت التجارة | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("service_1_title", "التجارة الدولية وبيت التجارة")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_it_tag">الركن الأول • الترخيص الأساسي</span>
      <h1 class="section-title" data-i18n="page_it_title">التجارة الدولية وبيت التجارة (International Trading House)</h1>
      <p class="section-sub" data-i18n="page_it_sub">منظومة احترافية للوساطة التجارية، عقد الصفقات العابرة للحدود، وتمثيل العلامات التجارية العالمية انطلاقاً من سلطنة عُمان.</p>
    </div>

    <div class="cards-grid-3" style="margin-bottom:60px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="it_c1_title">شراء وبيع البضائع دولياً</h3>
        <p class="service-card-desc" data-i18n="it_c1_desc">إدارة صفقات التجارة البينية، ربط المصانع والموردين في آسيا وأوروبا بالمشترين في منطقة الشرق الأوسط وشمال أفريقيا، وتنفيذ العقود باحترافية كاملة.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="it_c2_title">التمثيل والوكالات التجارية</h3>
        <p class="service-card-desc" data-i18n="it_c2_desc">تمثيل الشركات والمصانع الأجنبية الراغبة في التوسع داخل سلطنة عُمان ودول مجلس التعاون الخليجي، وتوفير المظلة القانونية والتسويقية لها.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="it_c3_title">إدارة صفقات الإنكوترمز</h3>
        <p class="service-card-desc" data-i18n="it_c3_desc">صياغة وتنفيذ العقود التجارية وفق كافة شروط غرفة التجارة الدولية (Incoterms 2020) بما في ذلك EXW, FOB, CFR, CIF, DAP و DDP مع إدارة كاملة للمخاطر.</p>
      </div>
    </div>

    <!-- Covered Commodity Sectors -->
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="it_sec_sectors_tag">القطاعات السلعية</span>
      <h2 class="section-title" data-i18n="it_sec_sectors_title">محفظة السلع الأساسية التي ندير صفقاتها الدولية</h2>
      <p class="section-sub" data-i18n="it_sec_sectors_sub">خبرة ميدانية عميقة في إدارة سلاسل الإمداد للسلع الصناعية والغذائية والإنشائية مع الالتزام بأعلى معايير الجودة.</p>
    </div>

    <div class="cards-grid-4" style="margin-bottom:70px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="it_sec1_title">المواد الغذائية والمنتجات الزراعية السائبة</h3>
        <p class="service-card-desc" data-i18n="it_sec1_desc">إدارة عقود توريد الحبوب، السكر، الزيوت النباتية، المعكرونة، والأغذية المعلبة مع فحص دقيق للمعايير الصحية وشهادات الحلال الخليجية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="it_sec2_title">البتروكيماويات والبوليمرات والمذيبات الصناعية</h3>
        <p class="service-card-desc" data-i18n="it_sec2_desc">وساطة وتجارة حبيبات البلاستيك (PE, PP, PVC)، المواد الكيميائية الأساسية، وحلول التعبئة الصناعية من كبرى المجمعات البتروكيماوية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="it_sec3_title">حديد التسليح والمعادن ومواد البناء الإنشائية</h3>
        <p class="service-card-desc" data-i18n="it_sec3_desc">عقود توريد كتل الحديد، حديد التسليح، الأنابيب الصناعية، الإسمنت المقاوم، والجبس لمشاريع البنية التحتية والإنشاءات الضخمة.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="it_sec4_title">المعدات الثقيلة وقطع الغيار الصناعية</h3>
        <p class="service-card-desc" data-i18n="it_sec4_desc">شراء وتوريد خطوط الإنتاج المتكاملة، معدات المناولة، المولدات الكهربائية، وقطع الغيار الأصلية المعتمدة من المصانع العالمية.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'international-trade.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/international-trade.html")

# 5. PAGE: IMPORT-EXPORT.HTML
def build_import_export_page():
    content = f'''{get_head("الاستيراد والتصدير وإعادة التصدير | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("service_2_title", "الاستيراد والتصدير وإعادة التصدير")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_ie_tag">الركن الثاني • العمليات اللوجستية</span>
      <h1 class="section-title" data-i18n="page_ie_title">الاستيراد والتصدير وإعادة التصدير (Import, Export & Re-Export)</h1>
      <p class="section-sub" data-i18n="page_ie_sub">تنفيذ وتنسيق سلاسل الإمداد المتكاملة عبر موانئ ومطارات سلطنة عمان مع تخليص جمركي ذكي وإدارة كاملة للشحنات البحرية والجوية والبرية.</p>
    </div>

    <div class="cards-grid-3" style="margin-bottom:60px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="ie_c1_title">الاستيراد إلى سلطنة عمان</h3>
        <p class="service-card-desc" data-i18n="ie_c1_desc">تسهيل استيراد المنتجات والسلع لحسابنا أو لحساب الغير، واستيفاء كافة الموافقات التنظيمية والفنية والصحية من الجهات المختصة في سلطنة عُمان.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="ie_c2_title">التصدير من سلطنة عمان</h3>
        <p class="service-card-desc" data-i18n="ie_c2_desc">تسويق وتصدير المنتجات العمانية الصناعية والزراعية إلى الأسواق الدولية، وإصدار شهادات المنشأ الرسمية والتنسيق مع الموانئ العالمية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="ie_c3_title">إعادة التصدير الترانزيت (Re-Export)</h3>
        <p class="service-card-desc" data-i18n="ie_c3_desc">استغلال الموانئ العمانية الحرة (صحار، صلالة، الدقم) لتخزين وإعادة تصدير البضائع للأسواق المجاورة مع الاستفادة من الإعفاءات الجمركية.</p>
      </div>
    </div>

    <!-- Multimodal Transit Modes -->
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="ie_sec_modes_tag">أنماط وحلول الشحن والتخليص</span>
      <h2 class="section-title" data-i18n="ie_sec_modes_title">شبكة نقل متعددة الوسائط لتغطية كافة متطلبات التجارة</h2>
      <p class="section-sub" data-i18n="ie_sec_modes_sub">حلول لوجستية متكاملة تضمن أعلى كفاءة زمنية وتكلفة تشغيلية منافسة لجميع أنواع الشحنات البحرية، الجوية، والبرية.</p>
    </div>

    <div class="cards-grid-4" style="margin-bottom:70px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="ie_m1_title">الشحن البحري بالحاويات الكاملة والمجمعة (FCL / LCL)</h3>
        <p class="service-card-desc" data-i18n="ie_m1_desc">حجوزات مباشرة مع كبرى الخطوط الملاحية العالمية من وإلى موانئ صحار، صلالة، والدقم بحاويات قياسية ومبردة وخزانات ISO Tank.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="ie_m2_title">النقل البري الترانزيت عبر أسطول الشاحنات الخليجي</h3>
        <p class="service-card-desc" data-i18n="ie_m2_desc">شاحنات مجهزة لنقل البضائع المبردة والجافة عبر المنافذ البرية العمانية مع الإمارات، السعودية، واليمن مع تصاريح العبور السريع.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="ie_m3_title">الشحن الجوي للشحنات العاجلة والحرجة (Air Cargo)</h3>
        <p class="service-card-desc" data-i18n="ie_m3_desc">خدمات الشحن الجوي عبر مطاري مسقط وصلالة الدوليين للأدوية، الإلكترونيات الدقيقة، والعينات التجارية الحساسة ذات القيمة العالية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="ie_m4_title">إعادة التصدير الجمركي من المستودعات الحرة (Re-Export)</h3>
        <p class="service-card-desc" data-i18n="ie_m4_desc">تفريغ البضائع بالمستودعات المعفاة، إعادة تعبئتها، وتصديرها بصفقات ثلاثية مع إصدار شهادات منشأ معتمدة تفيد القيمة المضافة.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'import-export.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/import-export.html")

# 6. PAGE: PROCUREMENT.HTML
def build_procurement_page():
    content = f'''{get_head("توريد وتأمين احتياجات المشاريع | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("service_3_title", "توريد وتأمين احتياجات المشاريع")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_proc_tag">الركن الثالث • التوريد الاستراتيجي</span>
      <h1 class="section-title" data-i18n="page_proc_title">توريد وتأمين احتياجات المشاريع (Procurement Services)</h1>
      <p class="section-sub" data-i18n="page_proc_sub">تأمين المواد الخام، الآلات، وخطوط الإنتاج للمشاريع الصناعية والإنشائية والبنية التحتية مع إدارة الفحص والمطابقة والتسليم في الموقع.</p>
    </div>

    <div class="cards-grid-3" style="margin-bottom:60px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="proc_c1_title_old">سورسينج وتوريد المواد الخام</h3>
        <p class="service-card-desc" data-i18n="proc_c1_desc_old">البحث عن أفضل الموردين المعتمدين عالمياً، التفاوض على الأسعار، وتأمين تدفق مستمر للمواد الخام الصناعية بأسعار تنافسية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="proc_c2_title_old">توريد الآلات ومعدات الإنتاج</h3>
        <p class="service-card-desc" data-i18n="proc_c2_desc_old">شراء وشحن خطوط الإنتاج والآلات الثقيلة من المصانع العالمية مع الفحص الفني المسبق وضمان مطابقة المواصفات التعاقدية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="proc_c3_title_old">إدارة سلاسل الإمداد للمشاريع</h3>
        <p class="service-card-desc" data-i18n="proc_c3_desc_old">إدارة المشتريات من مرحلة الطلب وحتى التسليم في الموقع (Door-to-Site) مع الجدولة الزمنية وتأمين مخاطر النقل والتوريد.</p>
      </div>
    </div>

    <!-- Technical Sourcing Capabilities -->
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="proc_sec_cap_tag">القدرات الفنية والتوريد</span>
      <h2 class="section-title" data-i18n="proc_sec_cap_title">توريد متكامل لاحتياجات مشاريع البنية التحتية والمصانع</h2>
      <p class="section-sub" data-i18n="proc_sec_cap_sub">نوفر سلاسل توريد مؤمنة للمقاولين ومطوري المشاريع الصناعية مع الالتزام التام بالمواصفات الهندسية وجداول التسليم الصارمة.</p>
    </div>

    <div class="cards-grid-4" style="margin-bottom:70px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="proc_c1_title">خطوط الإنتاج الصناعي ومحطات المعالجة</h3>
        <p class="service-card-desc" data-i18n="proc_c1_desc">توريد معدات التشكيل المعدني، خطوط التعبئة والتغليف الآلية، وحدات تكرير المياه، ومحطات المعالجة الحرارية والكيميائية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="proc_c2_title">المواد الخام الوسيطة والمضافات الكيميائية</h3>
        <p class="service-card-desc" data-i18n="proc_c2_desc">تأمين الكيماويات المتخصصة، الماسترباتش، كربونات الكالسيوم، الصمغ الصناعي، والبوليمرات اللازمة لتشغيل المصانع المحلية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="proc_c3_title">معدات توليد الطاقة وأنظمة التوليد الاحتياطي</h3>
        <p class="service-card-desc" data-i18n="proc_c3_desc">توريد المحولات الكهربائية عالية الجهد، مولدات الديزل الصناعية، التوربينات، وأنظمة التحكم الآلي PLC للبيئات الصحراوية والصناعية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="proc_c4_title">أنابيب النفط والغاز والصمامات الهندسية المعيارية</h3>
        <p class="service-card-desc" data-i18n="proc_c4_desc">توريد أنابيب الفولاذ الكربوني غير الملحومة وفق معايير API 5L، الصمامات الكروية والبوابية، والفلنجات للمشاريع البترولية والمائية.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'procurement.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/procurement.html")

# 7. PAGE: FINANCIAL-ADVISORY.HTML
def build_financial_advisory_page():
    content = f'''{get_head("الاستشارات المالية والاعتمادات المستندية | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("service_4_title", "الاستشارات المالية والاعتمادات")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_fa_tag">الركن الرابع • الأمان المالي</span>
      <h1 class="section-title" data-i18n="page_fa_title">الاستشارات المالية وهندسة الدفع التجاري (Trade Finance & Payment Structuring)</h1>
      <p class="section-sub" data-i18n="page_fa_sub">تأمين المعاملات المالية الدولية عبر الاعتمادات المستندية وحلول الدفع الموثوقة بالتعاون مع بنوك عُمانية ودولية رائدة لحماية كافة الأطراف.</p>
    </div>

    <div class="cards-grid-3" style="margin-bottom:60px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="fa_c1_title_old">الاعتمادات المستندية (L/C Structuring)</h3>
        <p class="service-card-desc" data-i18n="fa_c1_desc_old">صياغة وتدقيق شروط خطابات الاعتماد المستندي غير القابلة للإلغاء والمعززة لحماية مصالح المشتري والبائع وضمان مطابقة المستندات.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="fa_c2_title_old">ضمانات الدفع والتحصيل المستندي</h3>
        <p class="service-card-desc" data-i18n="fa_c2_desc_old">هيكلة آليات الدفع الآمنة وفق معايير غرفة التجارة الدولية (UCP 600)، التحصيل المستندي (CAD)، وحلول الضمان المصرفي للمشاريع.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="fa_c3_title_old">إدارة مخاطر الصرف والعملات</h3>
        <p class="service-card-desc" data-i18n="fa_c3_desc_old">استشارات تحوط ضد تقلبات أسعار الصرف، واختيار العملات المناسبة للصفقات (USD, EUR, OMR, AED) لتفادي الخسائر الناتجة عن تذبذب الأسواق.</p>
      </div>
    </div>

    <!-- Credit Instruments & Banking Tools -->
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="fa_sec_tools_tag">الأدوات المالية والائتمانية</span>
      <h2 class="section-title" data-i18n="fa_sec_tools_title">حلول مصرفية واستشارية مبتكرة لتمويل وتأمين الصفقات</h2>
      <p class="section-sub" data-i18n="fa_sec_tools_sub">نساعد الشركات على تصميم هياكل تمويل تجارية متقدمة تحافظ على سيولتها وتضمن استرداد الأموال مع الامتثال المصرفي الكامل.</p>
    </div>

    <div class="cards-grid-4" style="margin-bottom:70px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="fa_i1_title">الاعتمادات المستندية غير القابلة للإلغاء (Irrevocable L/C)</h3>
        <p class="service-card-desc" data-i18n="fa_i1_desc">هيكلة اعتمادات مستندية بالاطلاع (Sight L/C) أو مؤجلة الدفع (Usance L/C) معززة من بنوك دولية ذات تصنيف ائتماني رفيع تضمن السداد بمجرد مطابقة المستندات.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="fa_i2_title">الاعتمادات الدوارة والمحولة (Revolving & Transferable L/C)</h3>
        <p class="service-card-desc" data-i18n="fa_i2_desc">حلول مثالية للتجار الدوليين ووسطاء الصفقات الثلاثية لتحويل الاعتماد لصالح المورد النهائي مع حماية هامش الربح والسرية التجارية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="fa_i3_title">خطابات الضمان المصرفي وسندات الإنجاز (Bank Guarantees & PB)</h3>
        <p class="service-card-desc" data-i18n="fa_i3_desc">إصدار وإدارة ضمانات حسن التنفيذ (Performance Bond 10%)، ضمانات الدفعة المقدمة (APG)، وضمانات دخول المناقصات للمشاريع الكبرى.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="fa_i4_title">حسابات الضمان المالي المشروط (Escrow Accounts)</h3>
        <p class="service-card-desc" data-i18n="fa_i4_desc">إيداع أموال الصفقات لدى أطراف مصرفية أو قانونية معتمدة لا تفرج عن السيولة للمورد إلا بعد صدور تقرير الفحص الفني المستقل.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'financial-advisory.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/financial-advisory.html")

# 8. PAGE: MADE-IN-OMAN.HTML
def build_made_in_oman_page():
    content = f'''{get_head("بنية التصنيع وهوية صُنع في عُمان | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("service_5_title", "بنية التصنيع وهوية صُنع في عُمان")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_mio_tag">الركن الخامس • القيمة المضافة</span>
      <h1 class="section-title" data-i18n="page_mio_title">بنية التصنيع وهوية صُنع في عُمان (Contract Manufacturing & Made in Oman)</h1>
      <p class="section-sub" data-i18n="page_mio_sub">مساعدة المصانع والمستثمرين على تأسيس خطوط الإنتاج، التصنيع التعاقدي، الاستفادة من اتفاقيات التجارة الحرة، وإصدار شهادة المنشأ العمانية.</p>
    </div>

    <div class="cards-grid-3" style="margin-bottom:60px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="mio_c1_title_old">التصنيع التعاقدي (Contract Manufacturing)</h3>
        <p class="service-card-desc" data-i18n="mio_c1_desc_old">ربط الشركات بالمصانع العمانية القائمة لتصنيع وتعبئة منتجاتها تحت علامتها التجارية الخاصة مع ضمان الالتزام بمعايير الجودة العمانية والخليجية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="mio_c2_title_old">شهادة المنشأ العمانية المعتمدة</h3>
        <p class="service-card-desc" data-i18n="mio_c2_desc_old">المساعدة في استيفاء شروط القيمة المضافة الوطنية (In-Country Value) للحصول على شهادة المنشأ العمانية ودخول الأسواق الخليجية بدون رسوم جمركية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="mio_c3_title_old">الاستفادة من اتفاقيات التجارة الحرة (FTA)</h3>
        <p class="service-card-desc" data-i18n="mio_c3_desc_old">استغلال اتفاقية التجارة الحرة بين سلطنة عُمان والولايات المتحدة الأمريكية، واتفاقيات دول مجلس التعاون، لتصدير المنتجات بإعفاءات جمركية كاملة.</p>
      </div>
    </div>

    <!-- Value-Add & Preferential Market Access -->
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="mio_sec_val_tag">القيمة المضافة والتصنيع المشترك</span>
      <h2 class="section-title" data-i18n="mio_sec_val_title">بوابة التصنيع الوطني والوصول التفضيلي للأسواق العالمية</h2>
      <p class="section-sub" data-i18n="mio_sec_val_sub">استثمر في المزايا التنافسية للغاز الصناعي، الكهرباء المدعومة، والإعفاءات الجمركية للوصول إلى أسواق تضم أكثر من مليار مستهلك.</p>
    </div>

    <div class="cards-grid-4" style="margin-bottom:70px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="mio_v1_title">اتفاقية التجارة الحرة مع الولايات المتحدة الأمريكية (US-Oman FTA)</h3>
        <p class="service-card-desc" data-i18n="mio_v1_desc">تصدير المنتجات المصنعة في عمان إلى السوق الأمريكي بتعريفة جمركية 0% وبدون أي قيود كوتا للمنتجات المستوفية لمعايير القيمة المضافة الوطنية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="mio_v2_title">شهادة المنشأ العمانية الموحدة لدول مجلس التعاون الخليجي</h3>
        <p class="service-card-desc" data-i18n="mio_v2_desc">دخول بضائعك إلى أسواق السعودية والإمارات والكويت وقطر والبحرين بدون أي رسوم جمركية كمنتج وطني خليجي مستوفٍ لنسبة 40% قيمة مضافة.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="mio_v3_title">التصنيع التعاقدي وتعبئة وتغليف العلامات التجارية (Private Label)</h3>
        <p class="service-card-desc" data-i18n="mio_v3_desc">إنتاج منتجاتك في مصانع عمانية قائمة أو داخل ورش متخصصة دون الحاجة لبناء مصنع كامل، مع الاستفادة من علامة 'صُنع في عُمان'.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="mio_v4_title">حوافز مدائن والمدن الصناعية (Madayn Support)</h3>
        <p class="service-card-desc" data-i18n="mio_v4_desc">أراضي صناعية بأسعار إيجار رمزية مدعومة، إعفاءات جمركية على استيراد الآلات والمواد الخام، وتسهيلات حكومية سريعة لترخيص المشاريع.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'made-in-oman.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/made-in-oman.html")

# 9. PAGE: SERVICES.HTML
def build_services_page():
    content = f'''{get_head("مصفوفة الخدمات ونماذج الشراكة التجارية | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("nav_services", "خدماتنا")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_serv_tag">المصفوفة التشغيلية المعتمدة</span>
      <h1 class="section-title" data-i18n="page_serv_title">مصفوفة الخدمات ونماذج الشراكة التجارية</h1>
      <p class="section-sub" data-i18n="page_serv_sub">منظومة متكاملة من 5 خدمات محورية مصممة لتلبية احتياجات الشركات العالمية، المستثمرين، والموردين في سلطنة عمان ومنطقة الخليج العربي.</p>
    </div>

    <!-- 5 Core Services Detailed Cards -->
    <div style="display:flex; flex-direction:column; gap:36px; margin-bottom:70px;">
      <!-- Service 1 -->
      <div class="service-card" style="padding:40px;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:18px; flex-wrap:wrap; gap:12px;">
          <div>
            <span class="section-tag" style="margin-bottom:8px;" data-i18n="serv_badge_1">الركن الأول</span>
            <h2 class="service-card-title" style="font-size:1.5rem;" data-i18n="serv_card1_title">1. التجارة الدولية وبيت التجارة (International Trading House)</h2>
          </div>
          <a href="./international-trade.html" class="btn-secondary" style="font-size:0.88rem; padding:8px 20px;" data-i18n="btn_explore_service">استكشاف تفاصيل الخدمة &larr;</a>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:20px;" data-i18n="serv_card1_desc">شراء وبيع البضائع والسلع لحسابنا أو لحساب الغير على المستوى الدولي، الوساطة التجارية الدولية وعقد الصفقات الكبرى، التمثيل التجاري والوكالات للشركات الأجنبية الراغبة في دخول السوق العماني والخليجي، وإدارة صفقات التجارة وفق شروط Incoterms 2020.</p>
      </div>

      <!-- Service 2 -->
      <div class="service-card" style="padding:40px;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:18px; flex-wrap:wrap; gap:12px;">
          <div>
            <span class="section-tag" style="margin-bottom:8px;" data-i18n="serv_badge_2">الركن الثاني</span>
            <h2 class="service-card-title" style="font-size:1.5rem;" data-i18n="serv_card2_title">2. الاستيراد والتصدير وإعادة التصدير (Import, Export & Re-Export)</h2>
          </div>
          <a href="./import-export.html" class="btn-secondary" style="font-size:0.88rem; padding:8px 20px;" data-i18n="btn_explore_service">استكشاف تفاصيل الخدمة &larr;</a>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:20px;" data-i18n="serv_card2_desc">استيراد المنتجات والسلع إلى سلطنة عمان واستيفاء الموافقات التنظيمية، تصدير المنتجات العمانية إلى الأسواق الإقليمية والدولية، إعادة التصدير من المناطق الحرة العمانية (صحار، صلالة، الدقم)، والتخليص الجمركي وإدارة سلاسل الإمداد المتكاملة عبر نظام بيان.</p>
      </div>

      <!-- Service 3 -->
      <div class="service-card" style="padding:40px;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:18px; flex-wrap:wrap; gap:12px;">
          <div>
            <span class="section-tag" style="margin-bottom:8px;" data-i18n="serv_badge_3">الركن الثالث</span>
            <h2 class="service-card-title" style="font-size:1.5rem;" data-i18n="serv_card3_title">3. توريد وتأمين احتياجات المشاريع (Procurement Services)</h2>
          </div>
          <a href="./procurement.html" class="btn-secondary" style="font-size:0.88rem; padding:8px 20px;" data-i18n="btn_explore_service">استكشاف تفاصيل الخدمة &larr;</a>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:20px;" data-i18n="serv_card3_desc">سورسينج وتوريد المواد الخام للمصانع والمنشآت، توريد الآلات ومعدات الإنتاج وقطع الغيار الصناعية، إدارة سلاسل الإمداد لمشاريع البنية التحتية والمقاولات، والفحص الفني ومطابقة المواصفات قبل الشحن والتسليم.</p>
      </div>

      <!-- Service 4 -->
      <div class="service-card" style="padding:40px;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:18px; flex-wrap:wrap; gap:12px;">
          <div>
            <span class="section-tag" style="margin-bottom:8px;" data-i18n="serv_badge_4">الركن الرابع</span>
            <h2 class="service-card-title" style="font-size:1.5rem;" data-i18n="serv_card4_title">4. الاستشارات المالية والاعتمادات المستندية (Financial & L/C Advisory)</h2>
          </div>
          <a href="./financial-advisory.html" class="btn-secondary" style="font-size:0.88rem; padding:8px 20px;" data-i18n="btn_explore_service">استكشاف تفاصيل الخدمة &larr;</a>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:20px;" data-i18n="serv_card4_desc">هيكلة وتدقيق الاعتمادات المستندية (Letters of Credit - L/C) لحماية أطراف الصفقة، استشارات الدفع التجاري والضمانات المصرفية (Bank Guarantees)، إدارة مخاطر الصرف والعملات الأجنبية في الصفقات الدولية، والربط مع المؤسسات المالية لتمويل التجارة.</p>
      </div>

      <!-- Service 5 -->
      <div class="service-card" style="padding:40px;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:18px; flex-wrap:wrap; gap:12px;">
          <div>
            <span class="section-tag" style="margin-bottom:8px;" data-i18n="serv_badge_5">الركن الخامس</span>
            <h2 class="service-card-title" style="font-size:1.5rem;" data-i18n="serv_card5_title">5. بنية التصنيع وهوية صُنع في عُمان (Contract Manufacturing & Made in Oman)</h2>
          </div>
          <a href="./made-in-oman.html" class="btn-secondary" style="font-size:0.88rem; padding:8px 20px;" data-i18n="btn_explore_service">استكشاف تفاصيل الخدمة &larr;</a>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:20px;" data-i18n="serv_card5_desc">التصنيع التعاقدي للمنتجات عبر مصانع عمانية قائمة (Contract Manufacturing)، إصدار شهادة المنشأ العمانية والاستفادة من اتفاقيات التجارة الحرة، تأسيس خطوط الإنتاج والمصانع في المناطق الحرة والمدن الصناعية (مدائن)، وبرامج القيمة المحلية المضافة (ICV).</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'services.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/services.html")

# 10. PAGE: CONTACT.HTML
def build_contact_page():
    content = f'''{get_head("اتصل بنا والمكتب الرئيسي بمسقط | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("nav_contact", "اتصل بنا")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_contact_tag">المكتب الرئيسي وقنوات التواصل</span>
      <h1 class="section-title" data-i18n="page_contact_title">المكتب الرئيسي وقنوات التواصل المباشر</h1>
      <p class="section-sub" data-i18n="page_contact_sub">فريقنا التجاري والقانوني متاح للرد على استفساراتكم ومناقشة فرص التعاون والصفقات من الأحد إلى الخميس.</p>
    </div>

    <div class="cards-grid-3" style="margin-bottom:60px;">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="contact_c1_title">الاتصال المباشر وواتساب</h3>
        <p class="service-card-desc" style="font-size:1.05rem; font-weight:700; color:var(--primary-gold); margin-bottom:12px;">+968 7108 1635<br>+968 3153 6000</p>
        <p class="service-card-desc" data-i18n="contact_c1_desc">خطوط الاتصال المباشرة ومكتب خدمة العملاء عبر واتساب لخدمة الشركاء التجاريين على مدار الساعة.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="contact_c2_title">البريد الإلكتروني الرسمي</h3>
        <p class="service-card-desc" style="font-size:1.05rem; font-weight:700; color:var(--primary-gold); margin-bottom:12px;">info@omantakamul.com</p>
        <p class="service-card-desc" data-i18n="contact_c2_desc">لاستقبال طلبات عروض الأسعار، العقود الرسمية، والاستفسارات المالية والمصرفية المعتمدة.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="contact_c3_title">العنوان والمقر الرئيسي</h3>
        <p class="service-card-desc" style="font-size:1.05rem; font-weight:700; color:var(--primary-gold); margin-bottom:12px;">مسقط، سلطنة عُمان</p>
        <p class="service-card-desc" data-i18n="contact_c3_desc">سجل تجاري: 1389420 • منطقة الأعمال المركزية، محافظة مسقط، سلطنة عُمان.</p>
      </div>
    </div>

    <!-- Quick Message Form Card -->
    <div style="background:var(--bg-surface); border:1px solid var(--border-gold); border-radius:24px; padding:40px; max-width:800px; margin:0 auto 70px; box-shadow:var(--shadow-md);">
      <h3 style="font-size:1.4rem; font-weight:800; color:var(--primary-gold); margin-bottom:24px; text-align:center;" data-i18n="contact_form_title">إرسال استفسار مباشر إلى الإدارة التجارية</h3>
      <form onsubmit="event.preventDefault(); window.location.href='./thank-you.html';" style="display:flex; flex-direction:column; gap:20px;">
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;">
          <div>
            <label class="form-label" data-i18n="form_name">الاسم الكريم / الشركة</label>
            <input type="text" class="form-input" required placeholder="الاسم الكامل أو اسم المؤسسة">
          </div>
          <div>
            <label class="form-label" data-i18n="form_phone">رقم الهاتف (مع مفتاح الدولة)</label>
            <input type="tel" class="form-input" required placeholder="+968 ...">
          </div>
        </div>
        <div>
          <label class="form-label" data-i18n="form_email">البريد الإلكتروني الرسمي</label>
          <input type="email" class="form-input" required placeholder="name@company.com">
        </div>
        <div>
          <label class="form-label" data-i18n="form_message">تفاصيل الاستفسار أو متطلبات الشحنة</label>
          <textarea class="form-textarea" rows="4" required placeholder="اكتب تفاصيل طلبك أو السلعة المطلوبة..."></textarea>
        </div>
        <button type="submit" class="btn-cta" style="width:100%; justify-content:center; padding:14px;" data-i18n="form_submit">إرسال الطلب التجاري الآن</button>
      </form>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'contact.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/contact.html")

# 11. PAGE: FAQ.HTML
def build_faq_page():
    content = f'''{get_head("الأسئلة الشائعة | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("nav_faq", "الأسئلة الشائعة")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_faq_tag">مركز المعلومات والإجابات</span>
      <h1 class="section-title" data-i18n="page_faq_title">الأسئلة الشائعة حول خدمات تكامل والتجارة في عُمان</h1>
      <p class="section-sub" data-i18n="page_faq_sub">إجابات شاملة ومفصلة حول الإجراءات الجمركية، الاعتمادات المستندية، مزايا المناطق الحرة، ونماذج التعاقد المتاحة.</p>
    </div>

    <!-- FAQ Items Grid -->
    <div style="display:flex; flex-direction:column; gap:20px; max-width:960px; margin:0 auto 70px;">
      <div class="service-card" style="padding:28px;">
        <h3 class="service-card-title" style="font-size:1.15rem; color:var(--primary-gold); margin-bottom:12px;" data-i18n="faq_q1">ما هي المزايا الجيوسياسية للتجارة عبر موانئ سلطنة عمان؟</h3>
        <p class="service-card-desc" style="font-size:0.95rem; line-height:1.8;" data-i18n="faq_a1">تقع موانئ عمان (صحار، صلالة، الدقم) على المحيط الهندي وبحر العرب مباشرة خارج مضيق هرمز، مما يجنب التجارة مخاطر الإغلاق والتوترات الإقليمية، ويقلل تكاليف التأمين البحري وزمن الإبحار نحو الأسواق العالمية.</p>
      </div>

      <div class="service-card" style="padding:28px;">
        <h3 class="service-card-title" style="font-size:1.15rem; color:var(--primary-gold); margin-bottom:12px;" data-i18n="faq_q2">كيف تساعد تكامل في إدارة الاعتمادات المستندية (L/C)؟</h3>
        <p class="service-card-desc" style="font-size:0.95rem; line-height:1.8;" data-i18n="faq_a2">نقدم استشارات متخصصة لصياغة وتدقيق شروط خطابات الاعتماد المستندي، التحقق من مطابقة المستندات المصرفية وفق قواعد UCP 600، واختيار البنوك المعززة ذات التصنيف الائتماني الرفيع لضمان أمان الدفع لكلا الطرفين.</p>
      </div>

      <div class="service-card" style="padding:28px;">
        <h3 class="service-card-title" style="font-size:1.15rem; color:var(--primary-gold); margin-bottom:12px;" data-i18n="faq_q3">ما هي شروط الاستفادة من علامة "صُنع في عُمان" واتفاقيات التجارة الحرة؟</h3>
        <p class="service-card-desc" style="font-size:0.95rem; line-height:1.8;" data-i18n="faq_a3">يتطلب ذلك تحقيق نسبة قيمة مضافة محلية لا تقل عن 40% داخل سلطنة عمان، مما يمنح المنتج إعفاءً جمركياً كاملاً في دول مجلس التعاون الخليجي، والاستفادة من اتفاقية التجارة الحرة مع الولايات المتحدة الأمريكية (تعريفة 0%).</p>
      </div>

      <div class="service-card" style="padding:28px;">
        <h3 class="service-card-title" style="font-size:1.15rem; color:var(--primary-gold); margin-bottom:12px;" data-i18n="faq_q4">هل يمكن لشركة تكامل العمل كوكيل تجاري أو ممثل لشركتنا في عمان؟</h3>
        <p class="service-card-desc" style="font-size:0.95rem; line-height:1.8;" data-i18n="faq_a4">نعم، نوفر خدمات التمثيل التجاري والوكالات للشركات العالمية والمصانع الراغبة في دخول السوق العماني وأسواق الشرق الأوسط، وتوفير المظلة القانونية والتسويقية اللازمة لتوزيع منتجاتها باحترافية.</p>
      </div>

      <div class="service-card" style="padding:28px;">
        <h3 class="service-card-title" style="font-size:1.15rem; color:var(--primary-gold); margin-bottom:12px;" data-i18n="faq_q5">ما هي المدة اللازمة لإنهاء إجراءات التخليص الجمركي في نظام بيان؟</h3>
        <p class="service-card-desc" style="font-size:0.95rem; line-height:1.8;" data-i18n="faq_a5">بفضل التسجيل والتخليص المسبق الذي تطبقه تكامل قبل رسو السفينة، تفرج الجمارك العمانية عن معظم الشحنات النمطية في غضون 24 إلى 48 ساعة فقط، مما يمنع تكبد رسوم الأرضيات وتأخير الحاويات.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'faq.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/faq.html")

# 12. PAGE: REQUEST.HTML
def build_request_page():
    content = f'''{get_head("طلب استشارة تجارية | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("btn_request", "طلب استشارة تجارية")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container" style="padding-top:40px; padding-bottom:40px;">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_req_tag">بوابة الطلبات الرسمية</span>
      <h1 class="section-title" data-i18n="page_req_title">طلب استشارة تجارية أو دراسة صفقة دولية</h1>
      <p class="section-sub" data-i18n="page_req_sub">يرجى ملء النموذج أدناه بدقة لمساعدة فريقنا التجاري والقانوني في تقييم متطلباتك وتقديم المقترح الأنسب خلال 24 ساعة عمل.</p>
    </div>

    <!-- Structured RFQ Form -->
    <div style="background:var(--bg-surface); border:1px solid var(--border-gold); border-radius:24px; padding:44px; max-width:850px; margin:0 auto 70px; box-shadow:var(--shadow-lg);">
      <form onsubmit="event.preventDefault(); window.location.href='./thank-you.html';" style="display:flex; flex-direction:column; gap:24px;">
        
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;">
          <div>
            <label class="form-label" data-i18n="form_name">الاسم الكريم / الشركة</label>
            <input type="text" class="form-input" required placeholder="الاسم الكامل أو اسم المؤسسة">
          </div>
          <div>
            <label class="form-label" data-i18n="form_phone">رقم الهاتف (مع مفتاح الدولة)</label>
            <input type="tel" class="form-input" required placeholder="+968 ...">
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;">
          <div>
            <label class="form-label" data-i18n="form_email">البريد الإلكتروني الرسمي</label>
            <input type="email" class="form-input" required placeholder="name@company.com">
          </div>
          <div>
            <label class="form-label" data-i18n="req_service_select">الخدمة المطلوبة</label>
            <select class="form-select" required>
              <option value="" disabled selected data-i18n="req_opt_0">-- اختر الخدمة --</option>
              <option value="it" data-i18n="service_1_title">التجارة الدولية وبيت التجارة</option>
              <option value="ie" data-i18n="service_2_title">الاستيراد والتصدير وإعادة التصدير</option>
              <option value="proc" data-i18n="service_3_title">توريد وتأمين احتياجات المشاريع</option>
              <option value="fa" data-i18n="service_4_title">الاستشارات المالية والاعتمادات المستندية</option>
              <option value="mio" data-i18n="service_5_title">بنية التصنيع وهوية صُنع في عُمان</option>
            </select>
          </div>
        </div>

        <div>
          <label class="form-label" data-i18n="form_message">شرح متطلبات الشحنة، بلد المنشأ، والمواصفات الفنية</label>
          <textarea class="form-textarea" rows="5" required placeholder="يرجى توضيح نوع السلعة، الكمية التقديرية، شروط الإنكوترمز المفضلة (FOB/CIF)، وأي متطلبات مصرفية خاصة..."></textarea>
        </div>

        <button type="submit" class="btn-cta" style="width:100%; justify-content:center; padding:16px; font-size:1.05rem;" data-i18n="form_submit">إرسال الطلب التجاري الآن</button>
      </form>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'request.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/request.html")

build_about_page()
build_international_trade_page()
build_import_export_page()
build_procurement_page()
build_financial_advisory_page()
build_made_in_oman_page()
build_services_page()
build_contact_page()
build_faq_page()
build_request_page()
