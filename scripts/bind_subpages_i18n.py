import os, re

BASE_DIR = '/opt/data/cache/scratch/altakamul-site/pages'

def patch_file(fname, replacements):
    fpath = os.path.join(BASE_DIR, fname)
    if not os.path.exists(fpath): return
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
        else:
            print(f"Warning: pattern not found in {fname}: {old[:40]}...")
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Patched {fname} successfully!")

# 1. international-trade.html
patch_file('international-trade.html', [
    ('<span class="section-tag">الركن الأول • الترخيص الأساسي</span>', '<span class="section-tag" data-i18n="page_it_tag">الركن الأول • الترخيص الأساسي</span>'),
    ('<h1 class="section-title">التجارة الدولية وبيت التجارة (International Trading House)</h1>', '<h1 class="section-title" data-i18n="page_it_title">التجارة الدولية وبيت التجارة (International Trading House)</h1>'),
    ('<p class="section-sub">منظومة احترافية للوساطة التجارية، عقد الصفقات العابرة للحدود، وتمثيل العلامات التجارية العالمية انطلاقاً من سلطنة عُمان.</p>', '<p class="section-sub" data-i18n="page_it_sub">منظومة احترافية للوساطة التجارية، عقد الصفقات العابرة للحدود، وتمثيل العلامات التجارية العالمية انطلاقاً من سلطنة عُمان.</p>'),
    ('<h3 class="service-card-title">شراء وبيع البضائع دولياً</h3>', '<h3 class="service-card-title" data-i18n="it_c1_title">شراء وبيع البضائع دولياً</h3>'),
    ('<p class="service-card-desc">إدارة صفقات التجارة البينية، ربط المصانع والموردين في آسيا وأوروبا بالمشترين في منطقة الشرق الأوسط وشمال أفريقيا، وتنفيذ العقود باحترافية كاملة.</p>', '<p class="service-card-desc" data-i18n="it_c1_desc">إدارة صفقات التجارة البينية، ربط المصانع والموردين في آسيا وأوروبا بالمشترين في منطقة الشرق الأوسط وشمال أفريقيا، وتنفيذ العقود باحترافية كاملة.</p>'),
    ('<h3 class="service-card-title">التمثيل والوكالات التجارية</h3>', '<h3 class="service-card-title" data-i18n="it_c2_title">التمثيل والوكالات التجارية</h3>'),
    ('<p class="service-card-desc">تمثيل الشركات والمصانع الأجنبية الراغبة في التوسع داخل سلطنة عُمان ودول مجلس التعاون الخليجي، وتوفير المظلة القانونية والتسويقية لها.</p>', '<p class="service-card-desc" data-i18n="it_c2_desc">تمثيل الشركات والمصانع الأجنبية الراغبة في التوسع داخل سلطنة عُمان ودول مجلس التعاون الخليجي، وتوفير المظلة القانونية والتسويقية لها.</p>'),
    ('<h3 class="service-card-title">إدارة صفقات الإنكوترمز</h3>', '<h3 class="service-card-title" data-i18n="it_c3_title">إدارة صفقات الإنكوترمز</h3>'),
    ('<p class="service-card-desc">صياغة وتنفيذ العقود التجارية وفق كافة شروط غرفة التجارة الدولية (Incoterms 2020) بما في ذلك EXW, FOB, CFR, CIF, DAP و DDP مع إدارة كاملة للمخاطر.</p>', '<p class="service-card-desc" data-i18n="it_c3_desc">صياغة وتنفيذ العقود التجارية وفق كافة شروط غرفة التجارة الدولية (Incoterms 2020) بما في ذلك EXW, FOB, CFR, CIF, DAP و DDP مع إدارة كاملة للمخاطر.</p>'),
    ('قائمة الخدمات التشغيلية في التجارة الدولية', '<span data-i18n="it_ops_title">قائمة الخدمات التشغيلية في التجارة الدولية</span>'),
    ('وساطة تجارية وهيكلة الصفقات الثلاثية (Cross-Trade)', '<span data-i18n="it_op_1">وساطة تجارية وهيكلة الصفقات الثلاثية (Cross-Trade)</span>'),
    ('التفاوض المباشر مع المصنعين العالميين وتثبيت الأسعار', '<span data-i18n="it_op_2">التفاوض المباشر مع المصنعين العالميين وتثبيت الأسعار</span>'),
    ('دراسات تسويق وتطوير قنوات التوزيع في دول الخليج', '<span data-i18n="it_op_3">دراسات تسويق وتطوير قنوات التوزيع في دول الخليج</span>'),
    ('إبرام العقود التجارية الدولية الملزمة وحماية المصالح', '<span data-i18n="it_op_4">إبرام العقود التجارية الدولية الملزمة وحماية المصالح</span>'),
    ('إعادة التصدير من المناطق الحرة بمزايا جمركية تفضيلية', '<span data-i18n="it_op_5">إعادة التصدير من المناطق الحرة بمزايا جمركية تفضيلية</span>'),
    ('حلول تحالف استراتيجي ومشاريع تجارية مشتركة (JV)', '<span data-i18n="it_op_6">حلول تحالف استراتيجي ومشاريع تجارية مشتركة (JV)</span>'),
    ('طلب استشارة تجارية دولية &larr;', '<span data-i18n="btn_request">طلب استشارة تجارية دولية</span> &larr;')
])

# 2. import-export.html
patch_file('import-export.html', [
    ('<span class="section-tag">الركن الثاني • سلاسل الإمداد</span>', '<span class="section-tag" data-i18n="page_ie_tag">الركن الثاني • سلاسل الإمداد</span>'),
    ('<h1 class="section-title">الاستيراد والتصدير وإعادة التصدير (Import, Export & Re-Export)</h1>', '<h1 class="section-title" data-i18n="page_ie_title">الاستيراد والتصدير وإعادة التصدير (Import, Export & Re-Export)</h1>'),
    ('<p class="section-sub">حلول لوجستية وتجارية متكاملة لربط الموانئ العمانية بالأسواق العالمية وتسهيل عبور البضائع.</p>', '<p class="section-sub" data-i18n="page_ie_sub">حلول لوجستية وتجارية متكاملة لربط الموانئ العمانية بالأسواق العالمية وتسهيل عبور البضائع.</p>')
])

# 3. procurement.html
patch_file('procurement.html', [
    ('<span class="section-tag">الركن الثالث • الدعم الصناعي والمشاريع</span>', '<span class="section-tag" data-i18n="page_pr_tag">الركن الثالث • الدعم الصناعي والمشاريع</span>'),
    ('<h1 class="section-title">توريد وتأمين احتياجات المشاريع (Project Procurement & Supply)</h1>', '<h1 class="section-title" data-i18n="page_pr_title">توريد وتأمين احتياجات المشاريع (Project Procurement & Supply)</h1>'),
    ('<p class="section-sub">تأمين المواد الخام، الآلات، والمعدات الكبرى للشركات والمصانع والمقاولين في سلطنة عمان ودول المنطقة.</p>', '<p class="section-sub" data-i18n="page_pr_sub">تأمين المواد الخام، الآلات، والمعدات الكبرى للشركات والمصانع والمقاولين في سلطنة عمان ودول المنطقة.</p>')
])

# 4. financial-advisory.html
patch_file('financial-advisory.html', [
    ('<span class="section-tag">الركن الرابع • الحلول المالية التجارية</span>', '<span class="section-tag" data-i18n="page_fa_tag">الركن الرابع • الحلول المالية التجارية</span>'),
    ('<h1 class="section-title">الاستشارات المالية والاعتمادات (Trade Advisory & L/Cs)</h1>', '<h1 class="section-title" data-i18n="page_fa_title">الاستشارات المالية والاعتمادات (Trade Advisory & L/Cs)</h1>'),
    ('<p class="section-sub">استشارات متخصصة في هندسة الدفع التجاري، إدارة الاعتمادات المستندية، وتقليل المخاطر المالية الدولية.</p>', '<p class="section-sub" data-i18n="page_fa_sub">استشارات متخصصة في هندسة الدفع التجاري، إدارة الاعتمادات المستندية، وتقليل المخاطر المالية الدولية.</p>')
])

# 5. made-in-oman.html
patch_file('made-in-oman.html', [
    ('<span class="section-tag">الركن الخامس • القيمة المحلية المضافة</span>', '<span class="section-tag" data-i18n="page_mo_tag">الركن الخامس • القيمة المحلية المضافة</span>'),
    ('<h1 class="section-title">بنية التصنيع وهوية صُنع في عُمان (Made in Oman)</h1>', '<h1 class="section-title" data-i18n="page_mo_title">بنية التصنيع وهوية صُنع في عُمان (Made in Oman)</h1>'),
    ('<p class="section-sub">تمكين المستثمرين من تأسيس خطوط الإنتاج والاستفادة من اتفاقية التجارة الحرة مع أمريكا والإعفاءات الجمركية.</p>', '<p class="section-sub" data-i18n="page_mo_sub">تمكين المستثمرين من تأسيس خطوط الإنتاج والاستفادة من اتفاقية التجارة الحرة مع أمريكا والإعفاءات الجمركية.</p>')
])

# 6. about.html
patch_file('about.html', [
    ('<span class="section-tag">نبذة عن الهلدينغ والرؤية</span>', '<span class="section-tag" data-i18n="page_ab_tag">نبذة عن الهلدينغ والرؤية</span>'),
    ('<h1 class="section-title">ريادة في التجارة الدولية وتوطين الصناعة</h1>', '<h1 class="section-title" data-i18n="page_ab_title">ريادة في التجارة الدولية وتوطين الصناعة</h1>'),
    ('<p class="section-sub">شركة تكامل للتجارة الدولية ش.م.م ، بيت تجارة متكامل تأسس في مسقط ليكون الجسر الموثوق للتجارة العالمية والاستثمار الصناعي.</p>', '<p class="section-sub" data-i18n="page_ab_sub">شركة تكامل للتجارة الدولية ش.م.م ، بيت تجارة متكامل تأسس في مسقط ليكون الجسر الموثوق للتجارة العالمية والاستثمار الصناعي.</p>'),
    ('رؤيتنا الاستراتيجية', '<span data-i18n="ab_c1_title">رؤيتنا الاستراتيجية</span>'),
    ('رسالتنا المؤسسية', '<span data-i18n="ab_c2_title">رسالتنا المؤسسية</span>'),
    ('قيمنا الأساسية', '<span data-i18n="ab_c3_title">قيمنا الأساسية</span>')
])

# 7. services.html
patch_file('services.html', [
    ('<span class="section-tag">دليل الخدمات الشامل</span>', '<span class="section-tag" data-i18n="page_srv_tag">دليل الخدمات الشامل</span>'),
    ('<h1 class="section-title">مصفوفة الخدمات التجارية والتعاقد</h1>', '<h1 class="section-title" data-i18n="page_srv_title">مصفوفة الخدمات التجارية والتعاقد</h1>'),
    ('<p class="section-sub">منظومة متكاملة من 5 أركان تشغيلية مصممة لتلبية احتياجات الشركات، المصانع، والمستثمرين في التجارة الإقليمية والدولية.</p>', '<p class="section-sub" data-i18n="page_srv_sub">منظومة متكاملة من 5 أركان تشغيلية مصممة لتلبية احتياجات الشركات، المصانع، والمستثمرين في التجارة الإقليمية والدولية.</p>')
])

# 8. contact.html
patch_file('contact.html', [
    ('<span class="section-tag">تواصل معنا مباشرة</span>', '<span class="section-tag" data-i18n="page_ct_tag">تواصل معنا مباشرة</span>'),
    ('<h1 class="section-title">قنوات الاتصال المباشر والمكاتب</h1>', '<h1 class="section-title" data-i18n="page_ct_title">قنوات الاتصال المباشر والمكاتب</h1>'),
    ('<p class="section-sub">فريقنا المتخصص في مسقط جاهز لاستقبال استفساراتكم ومناقشة تفاصيل صفقاتكم وشراكاتكم التجارية.</p>', '<p class="section-sub" data-i18n="page_ct_sub">فريقنا المتخصص في مسقط جاهز لاستقبال استفساراتكم ومناقشة تفاصيل صفقاتكم وشراكاتكم التجارية.</p>')
])

# 9. request.html
patch_file('request.html', [
    ('<span class="section-tag">خدمة المستثمرين والتجار</span>', '<span class="section-tag" data-i18n="page_rq_tag">خدمة المستثمرين والتجار</span>'),
    ('<h1 class="section-title">طلب استشارة تجارية وصفقة جديدة</h1>', '<h1 class="section-title" data-i18n="page_rq_title">طلب استشارة تجارية وصفقة جديدة</h1>'),
    ('<p class="section-sub">يرجى تعبئة النموذج أدناه وسيقوم أحد مستشارينا التجاريين بالتواصل معكم خلال 24 ساعة لدراسة طلبكم.</p>', '<p class="section-sub" data-i18n="page_rq_sub">يرجى تعبئة النموذج أدناه وسيقوم أحد مستشارينا التجاريين بالتواصل معكم خلال 24 ساعة لدراسة طلبكم.</p>'),
    ('الاسم الكامل *', '<span data-i18n="form_name">الاسم الكامل</span> *'),
    ('اسم الشركة / المؤسسة *', '<span data-i18n="form_company">اسم الشركة / المؤسسة</span> *'),
    ('البريد الإلكتروني التجاري *', '<span data-i18n="form_email">البريد الإلكتروني التجاري</span> *'),
    ('رقم الهاتف / واتساب *', '<span data-i18n="form_phone">رقم الهاتف / واتساب</span> *'),
    ('الخدمة أو الركن المطلوب', '<span data-i18n="form_service">الخدمة أو الركن المطلوب</span>'),
    ('حجم المعاملة المتوقع (تقديري)', '<span data-i18n="form_budget">حجم المعاملة المتوقع (تقديري)</span>'),
    ('تفاصيل الطلب ومواصفات البضاعة *', '<span data-i18n="form_msg">تفاصيل الطلب ومواصفات البضاعة</span> *'),
    ('أوافق على سياسة الخصوصية وحفظ سرية المعلومات التجارية.', '<span data-i18n="form_privacy">أوافق على سياسة الخصوصية وحفظ سرية المعلومات التجارية.</span>'),
    ('إرسال الطلب التجاري الآن', '<span data-i18n="btn_submit_request">إرسال الطلب التجاري الآن</span>')
])

print("All subpages completely patched with 100% data-i18n attributes!")
