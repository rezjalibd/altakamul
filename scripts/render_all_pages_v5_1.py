import json, os
from generate_all_subpages_v5 import get_head, get_header, get_footer

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'
PAGES_DIR = os.path.join(BASE_DIR, 'pages')

with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
    t = json.load(f)

def breadcrumb(title_key, default_title):
    return f'''  <div class="breadcrumb" style="max-width:1280px; margin:20px auto 0; padding:0 24px; font-size:0.85rem; color:var(--text-muted);">
    <a href="../index.html" style="color:var(--text-muted); text-decoration:none;" data-i18n="nav_home">الرئيسية</a>
    <span style="margin:0 8px;">/</span>
    <span style="color:var(--primary-gold);" data-i18n="{title_key}">{default_title}</span>
  </div>'''

def cta_block():
    return '''  <section class="section-container" style="padding-top:20px; padding-bottom:80px;">
    <div style="background:var(--brand-gradient); border:1px solid var(--border-gold); border-radius:28px; padding:50px 36px; text-align:center; position:relative; overflow:hidden; box-shadow:var(--shadow-lg);">
      <div style="position:relative; z-index:2; max-width:760px; margin:0 auto;">
        <span class="section-tag" style="background:rgba(255,255,255,0.12); color:#FDE68A; border-color:rgba(253,230,138,0.4);" data-i18n="cta_tag">بدء التعاون الاستراتيجي</span>
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
  <section class="section-container subpage-hero">
    <div class="section-header">
      <span class="section-tag" data-i18n="hubs_page_tag">البنية اللوجستية الاستراتيجية</span>
      <h1 class="section-title" data-i18n="hubs_page_title">بوابات عمان البحرية والمناطق الاقتصادية الخاصة</h1>
      <p class="section-sub" data-i18n="hubs_page_sub">موقع جيوسياسي فريد خارج مضيق هرمز يربط خطوط الملاحة بين آسيا وأوروبا وأفريقيا مع إعفاءات جمركية وضريبية تصل إلى 100%.</p>
    </div>

    <!-- Stat Highlights -->
    <div class="stats-grid">
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
  </section>

  <!-- Hubs Detailed Cards Stack -->
  <section class="section-container" style="padding-top:20px; padding-bottom:40px;">
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="hubs_sec1_tag">المراكز اللوجستية المحورية</span>
      <h2 class="section-title" data-i18n="hubs_sec1_title">أربعة مراكز عالمية تدير تدفقات التجارة الدولية</h2>
      <p class="section-sub" data-i18n="hubs_sec1_sub">تتكامل الموانئ والمناطق الحرة في سلطنة عمان لتقديم حلول شاملة للتخزين، التوزيع، وإعادة التصدير.</p>
    </div>

    <div class="vertical-cards-stack">
      <!-- Sohar -->
      <div id="sohar" class="service-card" style="padding:36px;">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">
          <div style="width:54px; height:54px; border-radius:14px; background:rgba(197,160,89,0.15); display:flex; align-items:center; justify-content:center; color:var(--primary-gold); font-size:1.6rem; flex-shrink:0;">⚓</div>
          <div>
            <h3 class="service-card-title" style="font-size:1.45rem; margin-bottom:4px;" data-i18n="hub_sohar_full_title">ميناء ومنطقة صحار الحرة (Sohar Port & Freezone)</h3>
            <span style="font-size:0.85rem; color:var(--primary-gold); font-weight:700;" data-i18n="hub_sohar_badge">بوابة الخليج الشمالية • عمق بحري 25 متراً</span>
          </div>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:20px;" data-i18n="hub_sohar_full_desc">المركز الصناعي واللوجستي الأسرع نمواً في الشرق الأوسط. يتميز برباط مباشر مع شبكة الطرق السريعة لدولة الإمارات العربية المتحدة ودول الخليج، مع محطات مخصصة للبتروكيماويات، المعادن، والمواد الغذائية السائبة وغاطس بحري يصل إلى 25 متراً.</p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:12px;">
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_sohar_f1">غاطس بحري عميق لاستقبال أضخم سفن الحاويات والصب الجاف</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_sohar_f2">مجمع غذائي وصناعي متكامل مع صوامع ومخازن تحت المظلة الجمركية</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_sohar_f3">بوابة مباشرة وسريعة للسوق الإماراتي والخليجي عبر المنافذ البرية</span></div>
        </div>
      </div>

      <!-- Salalah -->
      <div id="salalah" class="service-card" style="padding:36px;">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">
          <div style="width:54px; height:54px; border-radius:14px; background:rgba(197,160,89,0.15); display:flex; align-items:center; justify-content:center; color:var(--primary-gold); font-size:1.6rem; flex-shrink:0;">🌊</div>
          <div>
            <h3 class="service-card-title" style="font-size:1.45rem; margin-bottom:4px;" data-i18n="hub_salalah_full_title">ميناء ومنطقة صلالة الحرة (Salalah Port & Freezone)</h3>
            <span style="font-size:0.85rem; color:var(--primary-gold); font-weight:700;" data-i18n="hub_salalah_badge">المحيط الهندي • محطة الترانزيت العالمية</span>
          </div>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:20px;" data-i18n="hub_salalah_full_desc">أكبر ميناء لمناولة الحاويات العابرة في سلطنة عُمان على المحيط الهندي مباشرة. يختصر زمن الإبحار إلى أوروبا وأمريكا وأفريقيا بنحو أسبوعين مقارنة بموانئ الخليج العربي الداخلية، مع ممر شحن جوي-بحري يربطه بمطار صلالة الدولي في أقل من ساعتين.</p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:12px;">
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_salalah_f1">موقع جغرافي مفتوح على خطوط التجارة العالمية بين الشرق والغرب</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_salalah_f2">خدمات الربط البحري الجوي السريع عبر مطار صلالة للشحنات المستعجلة</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_salalah_f3">مركز متقدم لمعالجة وتوزيع السلع لأسواق شرق ووسط أفريقيا</span></div>
        </div>
      </div>

      <!-- Duqm -->
      <div id="duqm" class="service-card" style="padding:36px;">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">
          <div style="width:54px; height:54px; border-radius:14px; background:rgba(197,160,89,0.15); display:flex; align-items:center; justify-content:center; color:var(--primary-gold); font-size:1.6rem; flex-shrink:0;">🏗</div>
          <div>
            <h3 class="service-card-title" style="font-size:1.45rem; margin-bottom:4px;" data-i18n="hub_duqm_full_title">المنطقة الاقتصادية الخاصة بالدقم (SEZAD)</h3>
            <span style="font-size:0.85rem; color:var(--primary-gold); font-weight:700;" data-i18n="hub_duqm_badge">أضخم مدينة اقتصادية متكاملة (2,000 كم²)</span>
          </div>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:20px;" data-i18n="hub_duqm_full_desc">أضخم مشروع اقتصادي متكامل في الشرق الأوسط بمساحة 2,000 كم². يضم ميناء الدقم التجاري المتعدد الأغراض، الحوض الجاف لإصلاح السفن العملاقة، مصفاة الدقم، ومجمعات الهيدروجين الأخضر والصناعات الثقيلة ومستودعات التخزين الاستراتيجي للنفط والغاز والبضائع.</p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:12px;">
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_duqm_f1">مساحات صناعية وتخزينية ضخمة بعقود انتفاع طويلة الأمد</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_duqm_f2">حوض جاف عالمي ومرافق تصدير المواد البتروكيماوية والمعادن</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_duqm_f3">إعفاءات ضريبية وحوافز استثمارية حصرية تصل إلى 30 عاماً</span></div>
        </div>
      </div>

      <!-- Khazaen & Mazunah -->
      <div id="khazaen" class="service-card" style="padding:36px;">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">
          <div style="width:54px; height:54px; border-radius:14px; background:rgba(197,160,89,0.15); display:flex; align-items:center; justify-content:center; color:var(--primary-gold); font-size:1.6rem; flex-shrink:0;">🏢</div>
          <div>
            <h3 class="service-card-title" style="font-size:1.45rem; margin-bottom:4px;" data-i18n="hub_khazaen_full_title">مدينة خزائن الاقتصادية والمنطقة الحرة بالمزيونة</h3>
            <span style="font-size:0.85rem; color:var(--primary-gold); font-weight:700;" data-i18n="hub_khazaen_badge">الميناء الجاف الأوسط وبوابة التجارة لليمن</span>
          </div>
        </div>
        <p class="service-card-desc" style="font-size:1rem; line-height:1.8; margin-bottom:20px;" data-i18n="hub_khazaen_full_desc">خزائن هي الميناء الجاف والمركز اللوجستي الأوسط الرابط بين مسقط وصحار، بينما المزيونة تمثل المنفذ البري الاستراتيجي لتجارة الترانزيت نحو الجمهورية اليمنية وأسواق شرق أفريقيا مع مزايا تجارة تفضيلية للمصدرين والمستوردين.</p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:12px;">
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_khazaen_f1">ميناء جاف وسوق مركزي للخضار والفواكه ومستودعات الأدوية</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_khazaen_f2">معبر المزيونة التجاري لترانزيت السلع والبضائع نحو الأسواق اليمنية</span></div>
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-color); border-radius:12px; padding:12px 16px; font-size:0.9rem; color:var(--text-secondary);">✔ <span data-i18n="hub_khazaen_f3">إجراءات جمركية مسرعة ومراكز لوجستية مبردة لإعادة التصدير</span></div>
        </div>
      </div>
    </div>

    <!-- On-Ground Services -->
    <div class="section-header" style="margin-top:50px; margin-bottom:36px;">
      <span class="section-tag" data-i18n="hubs_sec2_tag">خدمات تكامل الميدانية</span>
      <h2 class="section-title" data-i18n="hubs_sec2_title">حلول عملياتية متكاملة داخل الموانئ والمناطق الحرة</h2>
    </div>

    <div class="cards-grid-4">
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
    content = f'''{get_head("آلية العمل والمسار التنفيذي للصفقات | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("nav_process", "آلية العمل")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container subpage-hero">
    <div class="section-header">
      <span class="section-tag" data-i18n="proc_page_tag">حوكمة العمليات التجارية</span>
      <h1 class="section-title" data-i18n="proc_page_title">آلية العمل والمسار التنفيذي الشامل للصفقات</h1>
      <p class="section-sub" data-i18n="proc_page_sub">منهجية مؤسسية صارمة من 6 مراحل تضمن أمان التدفقات المالية، مطابقة المواصفات القياسية، والتسليم الدقيق وفق الإنكوترمز 2020.</p>
    </div>
  </section>

  <!-- 6 Detailed Process Steps -->
  <section class="section-container" style="padding-top:10px; padding-bottom:40px;">
    <div class="vertical-cards-stack">
      <!-- Step 1 -->
      <div class="service-card" style="padding:32px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:60px; height:60px; border-radius:16px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.5rem; box-shadow:0 8px 24px rgba(197,160,89,0.3); flex-shrink:0;">
          01
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px; flex-wrap:wrap;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step1_badge">المرحلة الأولى</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step1_title">دراسة الجدوى والتدقيق التنظيمي والمطابقة</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step1_desc">دراسة كود النظام المنسق للبضائع (HS Code)، فحص المتطلبات الفنية والمواصفات القياسية الخليجية (GSO)، والتحقق من الملاءة المالية والقانونية للمصنعين والمشترين من خلال سجلات التدقيق المالي المعتمدة.</p>
        </div>
      </div>

      <!-- Step 2 -->
      <div class="service-card" style="padding:32px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:60px; height:60px; border-radius:16px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.5rem; box-shadow:0 8px 24px rgba(197,160,89,0.3); flex-shrink:0;">
          02
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px; flex-wrap:wrap;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step2_badge">المرحلة الثانية</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step2_title">صياغة العقود التجارية وهيكلة الإنكوترمز</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step2_desc">إعداد عقود بيع وشراء دولية ملزمة ثنائية اللغة، تحدد بدقة مسؤوليات الشحن والتأمين والمخاطر وفق (Incoterms 2020) مثل FOB, CIF, DAP, DDP مع إدراج شروط التحكيم التجاري المعتمدة في سلطنة عمان.</p>
        </div>
      </div>

      <!-- Step 3 -->
      <div class="service-card" style="padding:32px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:60px; height:60px; border-radius:16px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.5rem; box-shadow:0 8px 24px rgba(197,160,89,0.3); flex-shrink:0;">
          03
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px; flex-wrap:wrap;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step3_badge">المرحلة الثالثة</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step3_title">هندسة الدفع والضمانات المصرفية (L/C & Escrow)</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step3_desc">فتح وإدارة الاعتمادات المستندية غير القابلة للإلغاء المعززة (Irrevocable Confirmed L/C) أو الضمانات البنكية (Performance Bonds) وحسابات الضمان المعلقة (Escrow) عبر بنوك عُمانية ودولية رائدة لحماية السيولة وحقوق الشركاء.</p>
        </div>
      </div>

      <!-- Step 4 -->
      <div class="service-card" style="padding:32px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:60px; height:60px; border-radius:16px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.5rem; box-shadow:0 8px 24px rgba(197,160,89,0.3); flex-shrink:0;">
          04
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px; flex-wrap:wrap;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step4_badge">المرحلة الرابعة</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step4_title">المطابقة ومراقبة الجودة والفحص قبل الشحن</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step4_desc">تعيين مكاتب فحص ومعاينة دولية معتمدة (مثل SGS, Bureau Veritas) لفحص جودة السلع في أرض المصنع أو ميناء التحميل، وتدقيق شهادات التحليل والتعبئة لضمان سلامتها الكاملة قبل إبحار السفن.</p>
        </div>
      </div>

      <!-- Step 5 -->
      <div class="service-card" style="padding:32px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:60px; height:60px; border-radius:16px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.5rem; box-shadow:0 8px 24px rgba(197,160,89,0.3); flex-shrink:0;">
          05
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px; flex-wrap:wrap;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step5_badge">المرحلة الخامسة</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step5_title">الشحن اللوجستي والتخليص المسبق بنظام بيان</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step5_desc">حجز المساحات البحرية وحاويات الشحن المبردة والجافة، استلام بوالص الشحن الأصلية (Bill of Lading)، وبدء إجراءات التخليص الجمركي الفوري عبر النافذة الإلكترونية الموحدة لشرطة عمان السلطانية قبل وصول الشحنة للميناء.</p>
        </div>
      </div>

      <!-- Step 6 -->
      <div class="service-card" style="padding:32px; display:flex; gap:24px; align-items:flex-start;">
        <div style="min-width:60px; height:60px; border-radius:16px; background:linear-gradient(135deg, var(--primary-gold) 0%, #9E7D3B 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; font-size:1.5rem; box-shadow:0 8px 24px rgba(197,160,89,0.3); flex-shrink:0;">
          06
        </div>
        <div style="flex:1;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px; flex-wrap:wrap;">
            <span class="section-tag" style="margin:0; font-size:0.75rem;" data-i18n="proc_step6_badge">المرحلة السادسة</span>
            <h3 class="service-card-title" style="margin:0; font-size:1.35rem;" data-i18n="proc_step6_title">التسليم النهائي، المستودعات، وإعادة التصدير</h3>
          </div>
          <p class="service-card-desc" style="font-size:0.98rem; line-height:1.8;" data-i18n="proc_step6_desc">استلام البضائع في المستودعات الجمركية المعفاة (Bonded) أو نقلها برياً وبحرياً للوجهة النهائية للمشتري، وإصدار شهادات الإفراج النهائي ووثائق منشأ إعادة التصدير مع تسوية الحسابات البنكية بدقة.</p>
        </div>
      </div>
    </div>

    <!-- Required Documentation Grid -->
    <div class="section-header" style="margin-top:50px; margin-bottom:36px;">
      <span class="section-tag" data-i18n="proc_docs_tag">التوثيق القانوني والجمركي</span>
      <h2 class="section-title" data-i18n="proc_docs_title">قائمة الوثائق الإلزامية لحماية الصفقات التجارية</h2>
      <p class="section-sub" data-i18n="proc_docs_sub">تلتزم تكامل بإعداد وتدقيق حزمة الوثائق الكاملة لضمان سرعة الإفراج الجمركي وعدم تحمل أي غرامات تأخير أو رسوم أرضيات.</p>
    </div>

    <div class="cards-grid-3">
      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_inv_title">الفاتورة التجارية المصدقة (Commercial Invoice)</h3>
        <p class="service-card-desc" data-i18n="doc_inv_desc">تتضمن وصفاً دقيقاً للبضائع، البنود الجمركية، شروط الإنكوترمز، ومصدقة حسب الأصول من غرفة التجارة والسفارة المعنية.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_bl_title">بوليصة الشحن البحرية الأصلية (Bill of Lading)</h3>
        <p class="service-card-desc" data-i18n="doc_bl_desc">وثيقة ملكية الشحنة وعقد النقل البحري، تثبت استلام البضائع على متن السفينة بحالة سليمة متطابقة مع شروط الاعتماد المستندي.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_co_title">شهادة المنشأ الرسمية (Certificate of Origin)</h3>
        <p class="service-card-desc" data-i18n="doc_co_desc">تثبت بلد الصنع الأصلي للسلعة للاستفادة من الإعفاءات الجمركية الممنوحة بموجب اتفاقيات التجارة الحرة والاتحاد الجمركي الخليجي.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_pack_title">قائمة التعبئة والتغليف التفصيلية (Packing List)</h3>
        <p class="service-card-desc" data-i18n="doc_pack_desc">توضح الأوزان الإجمالية والصافية، أرقام الطرود والحاويات، والعلامات المميزة لتسهيل الفحص الجمركي والتفريغ السريع.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_insp_title">شهادات المعاينة والمطابقة الفنية (SGS / BV)</h3>
        <p class="service-card-desc" data-i18n="doc_insp_desc">تقارير مختبرية مستقلة تؤكد سلامة البضائع ومطابقتها للمواصفات الخليجية القياسية المعتمدة من وزارة التجارة والصناعة.</p>
      </div>

      <div class="service-card">
        <h3 class="service-card-title" data-i18n="doc_ins_title">بوليصة التأمين البحري الشامل (Marine Insurance)</h3>
        <p class="service-card-desc" data-i18n="doc_ins_desc">تغطية تأمينية كاملة ضد كافة المخاطر البحرية (Institute Cargo Clauses A) لحماية رأس مال الشحنة خلال رحلة الإبحار.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'process.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/process.html")

# 3. PAGE: ABOUT.HTML (Hero bug fixed, duplicate section-header eliminated)
def build_about_page():
    content = f'''{get_head("من نحن ورؤيتنا الاستراتيجية | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("nav_about", "من نحن")}

<main class="main-wrapper">
  <!-- Unified Clean Hero Section -->
  <section class="section-container subpage-hero">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_about_tag">الهوية المؤسسية والترخيص</span>
      <h1 class="section-title" data-i18n="page_about_title">ريادة في إدارة صفقات التجارة الدولية وتطوير سلاسل الإمداد</h1>
      <p class="section-sub" data-i18n="page_about_sub">شركة تكامل للتجارة الدولية ش.م.م، بيت تجارة عُماني رائد يتخذ من العاصمة مسقط مقراً لربط الأسواق العالمية بمنطقة الخليج والشرق الأوسط.</p>
    </div>

    <!-- Corporate Credentials Stats Grid -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-val" data-i18n="footer_cr">CR 1389420</div>
        <div class="stat-label">سجل تجاري معتمد بسلطنة عمان</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">عُمان 2040</div>
        <div class="stat-label">شريك وطني في تنمية سلاسل الإمداد</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">100%</div>
        <div class="stat-label">شفافية مالية وامتثال مصرفي معتمد</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">مسقط</div>
        <div class="stat-label">المقر الرئيسي وإدارة العمليات اللوجستية</div>
      </div>
    </div>
  </section>

  <!-- Section 1: Institutional Pillars (Clean spacing & margins) -->
  <section class="section-container" style="padding-top:20px; padding-bottom:40px;">
    <div class="section-header" style="margin-bottom:36px;">
      <span class="section-tag" data-i18n="about_sec_pillars_tag">الأركان المؤسسية</span>
      <h2 class="section-title" data-i18n="about_sec_pillars_title">الركائز الأربع التي تبنى عليها صفقات تكامل</h2>
    </div>

    <div class="cards-grid-4">
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

    <!-- Section 2: Governance & Regulation (Separate section-header with clear gap) -->
    <div class="section-header" style="margin-top:60px; margin-bottom:36px;">
      <span class="section-tag" data-i18n="about_sec_gov_tag">الحوكمة والامتثال القانوني</span>
      <h2 class="section-title" data-i18n="about_sec_gov_title">كيان تجاري مسجل وفق أرقى المعايير التنظيمية العمانية</h2>
      <p class="section-sub" data-i18n="about_sec_gov_sub">تلتزم شركة تكامل للتجارة الدولية (سجل تجاري: 1389420) بأعلى معايير الشفافية المالية والامتثال لأنظمة التجارة الدولية ومكافحة غسيل الأموال.</p>
    </div>

    <div class="cards-grid-3">
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
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/about.html")

# 4. PAGE: PRIVACY.HTML (Detailed, institutional 9-clause legal policy)
def build_privacy_page():
    content = f'''{get_head("سياسة الخصوصية وسرية البيانات | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("footer_privacy", "سياسة الخصوصية")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container subpage-hero">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_priv_tag">سياسة الخصوصية وحماية البيانات</span>
      <h1 class="section-title" data-i18n="page_priv_title">سياسة الخصوصية وسرية البيانات التجارية</h1>
      <p class="section-sub" data-i18n="page_priv_sub">التزام مؤسسي بحماية خصوصية الشركاء وسرية الصفقات الدولية بموجب قانون حماية البيانات الشخصية العماني (المرسوم السلطاني 6/2022).</p>
    </div>
  </section>

  <section class="section-container" style="padding-top:10px; padding-bottom:40px;">
    <div class="legal-document-container">
      <div class="legal-section-card">
        <h2 data-i18n="priv_s1_title">١. الإطار القانوني والصفة المؤسسية</h2>
        <p data-i18n="priv_s1_desc">تخضع كافة إجراءات جمع ومعالجة البيانات لشركة تكامل للتجارة الدولية ش.م.م (سجل تجاري: 1389420) لأحكام قانون حماية البيانات الشخصية الصادر بالمرسوم السلطاني رقم 6/2022 وقانون المعاملات الإلكترونية رقم 69/2008. تضمن الشركة أن جميع المعلومات المقدمة من الموردين والمشترين تعامل كبيانات سرية للغاية ومحمية بموجب أرفع معايير الحوكمة المؤسسية.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="priv_s2_title">٢. نطاق البيانات المجمعة في التعاملات التجارية</h2>
        <p data-i18n="priv_s2_desc">تشمل البيانات المجمعة: بيانات التحقق المؤسسي (KYC) للمفوضين بالتوقيع، أرقام السجلات والبطاقات الضريبية، الوثائق التجارية (الفواتير، بوالص الشحن، شهادات المنشأ)، وتفاصيل الحسابات والاعتمادات البنكية المسجلة عبر نظام سويفت (SWIFT)، إلى جانب المراسلات الفنية لطلبات الاستيراد والتصدير.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="priv_s3_title">٣. الأغراض المشروعة لمعالجة البيانات</h2>
        <p data-i18n="priv_s3_desc">نستخدم البيانات حصرياً لـ: تنفيذ ومتابعة عقود البيع والشراء الدولية، إصدار التراخيص والتخليص الجمركي عبر نظام بيان التابع لشرطة عُمان السلطانية، التحقق من الملاءة المالية ومكافحة غسيل الأموال وتمويل الإرهاب بموجب القانون رقم 30/2016، وتنسيق سلاسل الإمداد اللوجستية البحرية والجوية.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="priv_s4_title">٤. سرية الأسرار التجارية واتفاقيات عدم الإفصاح (NDA)</h2>
        <p data-i18n="priv_s4_desc">تدرك تكامل الطبيعة الحساسة للأسواق الدولية، وتعتبر قوائم الموردين وهوامش التسعير والعملاء المحتملين أسراراً تجارية غير قابلة للمشاركة. نوقع اتفاقيات عدم إفصاح ملزمة قانوناً مع كافة الشركاء، مع التزام تام بعدم مشاركة أي معلومة إلا بموافقة خطية مسبقة من العميل.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="priv_s5_title">٥. مشاركة البيانات مع الجهات الرقابية والموانئ</h2>
        <p data-i18n="priv_s5_desc">لا يتم الإفصاح عن البيانات إلا للجهات الرسمية المصرح لها قانوناً بسلطنة عُمان وتشمل: الإدارة العامة للجمارك (نظام بيان)، إدارات الموانئ والمناطق الحرة (صحار، صلالة، الدقم)، وزارة التجارة والصناعة وترويج الاستثمار، والمصارف المعنية بإدارة الاعتمادات المستندية، وذلك في حدود ما تقتضيه متطلبات إتمام الصفقة فقط.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="priv_s6_title">٦. النقل الآمن للبيانات عبر الحدود الدولية</h2>
        <p data-i18n="priv_s6_desc">في حال تطلبت العمليات التجارية تبادل مستندات الشحن والفحص مع جهات تفتيش دولية (مثل SGS أو Bureau Veritas) أو مصارف مراسلة خارجية، يتم نقل البيانات عبر قنوات مصرفية ورقمية مشفرة تضمن أعلى مستويات الحماية وتمنع أي وصول غير مصرح به.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="priv_s7_title">٧. التدابير الأمنية ومدة الاحتفاظ بالسجلات</h2>
        <p data-i18n="priv_s7_desc">نطبق بروتوكولات تشفير متقدمة (TLS 1.3 / AES-256) لحماية قواعد البيانات والمراسلات. يتم الاحتفاظ بسجلات المعاملات التجارية والعقود لمدة 10 سنوات امتثالاً للمتطلبات المحاسبية والقانونية المنصوص عليها في قانون التجارة العماني وقانون الشركات التجارية رقم 18/2019، ليتم بعدها إتلافها أو أرشفتها بشكل آمن.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="priv_s8_title">٨. حقوق أصحاب البيانات والشركات</h2>
        <p data-i18n="priv_s8_desc">يحق لكل شريك تجاري طلب الاطلاع على بياناته المخزنة، تصحيح أي معلومات غير دقيقة، طلب شهادة امتثال للمعاملات المؤرشفة، وتقديم أي استفسار أو اعتراض بشأن معالجة البيانات من خلال التواصل المباشر مع مكتب الامتثال القانوني للشركة.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="priv_s9_title">٩. الاتصال بمسؤول الامتثال وحماية البيانات</h2>
        <p data-i18n="priv_s9_desc">لأي استفسارات تتعلق بسياسة الخصوصية وسرية البيانات، يرجى التواصل مع إدارة الامتثال عبر البريد الإلكتروني: compliance@omantakamul.com أو هاتفياً على: 96871081635+ / مسقط، سلطنة عُمان. نلتزم بالرد على كافة الإخطارات والطلبات في غضون 14 يوم عمل.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'privacy.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/privacy.html")

# 5. PAGE: TERMS.HTML (Detailed, institutional 9-clause terms)
def build_terms_page():
    content = f'''{get_head("الشروط والأحكام واللوائح التجارية | شركة تكامل")}
{get_header(is_root=False)}
{breadcrumb("footer_terms", "الشروط والأحكام")}

<main class="main-wrapper">
  <!-- Hero Section -->
  <section class="section-container subpage-hero">
    <div class="section-header">
      <span class="section-tag" data-i18n="page_term_tag">الشروط والأحكام والتعاقد التجاري</span>
      <h1 class="section-title" data-i18n="page_term_title">الشروط والأحكام المنظمة للتعاملات التجارية الدولية</h1>
      <p class="section-sub" data-i18n="page_term_sub">الإطار القانوني والتعاقدي المعتمد لكافة الخدمات والصفقات التجارية التي تديرها شركة تكامل للتجارة الدولية ش.م.م (سجل تجاري: 1389420).</p>
    </div>
  </section>

  <section class="section-container" style="padding-top:10px; padding-bottom:40px;">
    <div class="legal-document-container">
      <div class="legal-section-card">
        <h2 data-i18n="term_s1_title">١. الأهلية القانونية ونطاق الأنشطة المرخصة</h2>
        <p data-i18n="term_s1_desc">شركة تكامل للتجارة الدولية ش.م.م شركة ذات مسؤولية محدودة مسجلة في سلطنة عمان (CR: 1389420). تعمل الشركة بموجب التراخيص الصادرة من وزارة التجارة والصناعة وترويج الاستثمار، وتشمل أنشطتها: الاستيراد والتصدير العام، التمثيل التجاري وبيت التجارة (Trading House)، الوساطة في الصفقات الدولية، واستشارات سلاسل الإمداد وإدارة المشتريات.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="term_s2_title">٢. الصفة التجارية وإخلاء المسؤولية المصرفية</h2>
        <p data-i18n="term_s2_desc">توضح تكامل أنها بيت تجارة دولي وشركة إدارة صادرات (EMC)، وليست مصرفاً أو مؤسسة إقراض أو وسيطاً مالياً مرخصاً من البنك المركزي العُماني. كافة الترتيبات المتعلقة بالاعتمادات المستندية (L/C) أو الضمانات البنكية وحسابات الضمان (Escrow) يتم فتحها وإدارتها حصرياً عبر المصارف التجارية المعتمدة محلياً ودولياً ووفق اللوائح المصرفية السارية.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="term_s3_title">٣. شروط التجارة الدولية (Incoterms® 2020) والمسؤوليات</h2>
        <p data-i18n="term_s3_desc">تخضع كافة عمليات التوريد والشحن لقواعد الإنكوترمز الصادرة عن غرفة التجارة الدولية (Incoterms 2020) مثل FOB, CIF, CFR, DAP, DDP وفق ما يُحدد صراحة في كل عقد تجاري مستقل. تنتقل المخاطر والمسؤوليات التأمينية استناداً إلى مصطلح التسليم المتفق عليه، ويلتزم المشتري بتغطية التأمين البحري الشامل (Institute Cargo Clauses A) ما لم ينص العقد على خلاف ذلك.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="term_s4_title">٤. الاعتمادات المستندية وآليات الدفع الدولية</h2>
        <p data-i18n="term_s4_desc">تطبق على كافة الاعتمادات المستندية القواعد والأعراف الموحدة للاعتمادات المستندية (ICC UCP 600) والضمانات البنكية عند الطلب (URDG 758). لا يتم الإفراج عن البضائع أو تسليم بوالص الشحن الأصلية إلا بعد استيفاء الشروط المالية وتأكيد الدفع البنكي غير القابل للنقض.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="term_s5_title">٥. الفحص الفني، معايير المطابقة، وإجراءات الاعتراض</h2>
        <p data-i18n="term_s5_desc">تخضع البضائع الموردة لشهادات الفحص الفني الصادرة من شركات معاينة دولية مستقلة (مثل SGS, Bureau Veritas, Intertek) في ميناء الشحن لمطابقة المواصفات القياسية الخليجية (GSO). في حال وجود أي اختلاف ظاهري أو عيب، يجب تقديم إخطار رسمي كتابي خلال 7 أيام عمل من تاريخ تفريغ الشحنة في ميناء الوصول مصحوباً بتقرير معاينة رسمي، وإلا اعتبرت الشحنة مقبولة نهائياً.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="term_s6_title">٦. بنود القوة القاهرة والحد من المسؤولية اللوجستية</h2>
        <p data-i18n="term_s6_desc">لا تتحمل شركة تكامل أي مسؤولية مالية عن التأخير أو عدم التنفيذ الناجم عن ظروف القوة القاهرة خارجة عن السيطرة المعقولة، بما في ذلك: النزاعات المسلحة، إغلاق الممرات الملاحية أو المضائق، الكوارث الطبيعية، القرصنة البحرية، الإضرابات العامة، أو القرارات الحكومية المفاجئة بحظر التصدير/الاستيراد. وتقتصر المسؤولية القصوى للشركة في جميع الأحوال على قيمة أتعاب الإدارة التجارية للخدمة محل التعاقد.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="term_s7_title">٧. الامتثال لمكافحة غسيل الأموال والعقوبات التجارية</h2>
        <p data-i18n="term_s7_desc">تلتزم تكامل التزاماً صارماً بالقانون العماني لمكافحة غسيل الأموال وتمويل الإرهاب (القانون رقم 30/2016) وقوائم العقوبات المعتمدة دولياً. يحق للشركة إنهاء أي صفقة فوراً وتجميد الإجراءات وإخطار السلطات الرسمية في حال ثبوت عدم صحة وثائق المصدر/المستورد أو محاولة إدخال بضائع مقيدة أو محظورة دولياً.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="term_s8_title">٨. حماية الأسرار التجارية والملكية الفكرية</h2>
        <p data-i18n="term_s8_desc">تظل كافة الدراسات التحليلية، خطط المسارات اللوجستية، تصاميم سلاسل التوريد، وهوية العلامة التجارية لشركة تكامل ملكية فكرية حصرية للشركة ومحمية بموجب قوانين حماية الملكية الفكرية العمانية. يحظر نسخها أو استخدامها لأغراض تجارية أخرى دون موافقة خطية صريحة.</p>
      </div>

      <div class="legal-section-card">
        <h2 data-i18n="term_s9_title">٩. القانون الحاكم والتحكيم وفض النزاعات</h2>
        <p data-i18n="term_s9_desc">تخضع هذه الشروط وكافة العقود المرتبطة بها وتفسر حصرياً وفق القوانين والأنظمة النافذة في سلطنة عمان. في حال نشوء أي نزاع تجاري، يتم السعي لحله ودياً خلال 30 يوماً، وفي حال تعذر ذلك، يحال النزاع إلى المحاكم التجارية المختصة في سلطنة عُمان أو إلى التحكيم التجاري وفق قواعد مركز عُمان للتحكيم التجاري (OAC) إذا نص العقد على ذلك.</p>
      </div>
    </div>
  </section>

  {cta_block()}
</main>

{get_footer(is_root=False)}'''
    with open(os.path.join(PAGES_DIR, 'terms.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated pages/terms.html")

# Run builders
build_hubs_page()
build_process_page()
build_about_page()
build_privacy_page()
build_terms_page()
print("Successfully generated all enhanced target pages!")
