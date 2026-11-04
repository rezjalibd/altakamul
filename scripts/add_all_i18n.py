import json, os, re

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'

with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
    t = json.load(f)

# New keys dictionary
extra_keys = {
  "ar": {
    "page_it_tag": "الركن الأول • الترخيص الأساسي",
    "page_it_title": "التجارة الدولية وبيت التجارة (International Trading House)",
    "page_it_sub": "منظومة احترافية للوساطة التجارية، عقد الصفقات العابرة للحدود، وتمثيل العلامات التجارية العالمية انطلاقاً من سلطنة عُمان.",
    "it_c1_title": "شراء وبيع البضائع دولياً",
    "it_c1_desc": "إدارة صفقات التجارة البينية، ربط المصانع والموردين في آسیا وأوروبا بالمشترين في الشرق الأوسط، وتنفيذ العقود باحترافية كاملة.",
    "it_c2_title": "التمثيل والوكالات التجارية",
    "it_c2_desc": "تمثيل الشركات والمصانع الأجنبية الراغبة في التوسع داخل سلطنة عُمان والخليج، وتوفير المظلة القانونية والتسويقية لها.",
    "it_c3_title": "إدارة صفقات الإنكوترمز",
    "it_c3_desc": "صياغة وتنفيذ العقود التجارية وفق كافة شروط غرفة التجارة الدولية (Incoterms 2020) مع إدارة كاملة للمخاطر.",
    "it_ops_title": "قائمة الخدمات التشغيلية في التجارة الدولية",
    "it_op_1": "وساطة تجارية وهيكلة الصفقات الثلاثية (Cross-Trade)",
    "it_op_2": "التفاوض المباشر مع المصنعين العالميين وتثبيت الأسعار",
    "it_op_3": "دراسات تسويق وتطوير قنوات التوزيع في دول الخليج",
    "it_op_4": "إبرام العقود التجارية الدولية الملزمة وحماية المصالح",
    "it_op_5": "إعادة التصدير من المناطق الحرة بمزايا جمركية تفضيلية",
    "it_op_6": "حلول تحالف استراتيجي ومشاريع تجارية مشتركة (JV)",

    "page_ie_tag": "الركن الثاني • سلاسل الإمداد",
    "page_ie_title": "الاستيراد والتصدير وإعادة التصدير (Import, Export & Re-Export)",
    "page_ie_sub": "حلول لوجستية وتجارية متكاملة لربط الموانئ العمانية بالأسواق العالمية وتسهيل عبور البضائع.",
    "ie_c1_title": "تصدير المنتجات العمانية",
    "ie_c1_desc": "فتح أسواق تصديرية جديدة للمنتجات المصنعة في سلطنة عمان والاستفادة من اتفاقيات التجارة الحرة والإعفاءات الجمركية.",
    "ie_c2_title": "الاستيراد والتخليص الجمركي",
    "ie_c2_desc": "إدارة عمليات الاستيراد للبضائع الحيوية والمواد الخام، إتمام المعاملات الجمركية ونظام بيان في موانئ صحار، صلالة والدقم.",
    "ie_c3_title": "إعادة التصدير والترانزيت",
    "ie_c3_desc": "تخزين ومناولة البضائع في المستودعات الجمركية الحرة وإعادة شحنها للأسواق المجاورة دون دفع رسوم جمركية.",

    "page_pr_tag": "الركن الثالث • الدعم الصناعي والمشاريع",
    "page_pr_title": "توريد وتأمين احتياجات المشاريع (Project Procurement & Supply)",
    "page_pr_sub": "تأمين المواد الخام، الآلات، والمعدات الكبرى للشركات والمصانع والمقاولين في سلطنة عمان ودول المنطقة.",
    "pr_c1_title": "المواد الخام الصناعية",
    "pr_c1_desc": "توريد البتروكيماويات، المعادن، البوليمرات ومواد البناء الأساسية للمصانع وشركات المقاولات الكبرى بأسعار تنافسية.",
    "pr_c2_title": "الآلات وخطوط الإنتاج",
    "pr_c2_desc": "استيراد وتوريد الآلات الصناعية، المعدات الثقيلة، وأنظمة الطاقة من كبرى الشركات المصنعة في آسيا وأوروبا.",
    "pr_c3_title": "فحص ومطابقة الجودة",
    "pr_c3_desc": "إجراء الفحوصات الفنية والتفتيش في بلد المنشأ لضمان مطابقة الشحنات للمواصفات والمقاييس العمانية والخليجية.",

    "page_fa_tag": "الركن الرابع • الحلول المالية التجارية",
    "page_fa_title": "الاستشارات المالية والاعتمادات (Trade Advisory & L/Cs)",
    "page_fa_sub": "استشارات متخصصة في هندسة الدفع التجاري، إدارة الاعتمادات المستندية، وتقليل المخاطر المالية الدولية.",
    "fa_c1_title": "الاعتمادات المستندية (LC)",
    "fa_c1_desc": "مساعدة الشركات في صياغة ومراجعة شروط الاعتمادات المستندية (Letter of Credit) لضمان حقوق المشتري والمورد.",
    "fa_c2_title": "خطابات الضمان (LG)",
    "fa_c2_desc": "استشارات إصدار خطابات الضمان المصرفية لحسن التنفيذ والدفعة المقدمة عبر البنوك العمانية والإقليمية المعتمدة.",
    "fa_c3_title": "تقييم مخاطر الدول والشركاء",
    "fa_c3_desc": "تحليل المخاطر الجيوسياسية، استقرار العملات، وفحص الملاءة المالية للموردين والمشترين قبل توقيع الصفقات الكبرى.",

    "page_mo_tag": "الركن الخامس • القيمة المحلية المضافة",
    "page_mo_title": "بنية التصنيع وهوية صُنع في عُمان (Made in Oman)",
    "page_mo_sub": "تمكين المستثمرين من تأسيس خطوط الإنتاج والاستفادة من اتفاقية التجارة الحرة مع أمريكا والإعفاءات الجمركية.",
    "mo_c1_title": "تأسيس وترخيص المصانع",
    "mo_c1_desc": "مرافقة المستثمرين في استخراج السجلات والتراخيص الصناعية واستئجار الأراضي في مدائن والمناطق الحرة.",
    "mo_c2_title": "شهادة المنشأ العمانية",
    "mo_c2_desc": "استيفاء متطلبات القيمة المحلية المضافة (ICV) وإصدار شهادات المنشأ الرسمية للتصدير بدون جمارك إلى أمريكا والخليج.",
    "mo_c3_title": "حوافز المناطق الحرة",
    "mo_c3_desc": "الاستفادة من ملكية أجنبية بنسبة 100%، إعفاء تام من ضريبة الدخل والجمارك، وحرية تحويل الأرباح ورؤوس الأموال.",

    "page_ab_tag": "نبذة عن الهلدينغ والرؤية",
    "page_ab_title": "ريادة في التجارة الدولية وتوطين الصناعة",
    "page_ab_sub": "شركة تكامل للتجارة الدولية ش.م.م ، بيت تجارة متكامل تأسس في مسقط ليكون الجسر الموثوق للتجارة العالمية والاستثمار الصناعي.",
    "ab_c1_title": "رؤيتنا الاستراتيجية",
    "ab_c1_desc": "أن نكون البوابة الأولى والمفضلة للشركات العالمية الراغبة في اتخاذ سلطنة عمان مركزاً تجارياً وصناعياً رئيسياً في الشرق الأوسط.",
    "ab_c2_title": "رسالتنا المؤسسية",
    "ab_c2_desc": "تقديم خدمات تجارية ولوجستية واستشارية رفيعة المستوى تدعم نمو شركائنا، وتساهم بفعالية في رؤية عُمان 2040.",
    "ab_c3_title": "قيمنا الأساسية",
    "ab_c3_desc": "الشفافية المطلقة، الأمانة في المعاملات، الامتثال الكامل للقوانين، والالتزام الصارم بحماية مصالح وسرية بيانات عملائنا.",

    "page_srv_tag": "دليل الخدمات الشامل",
    "page_srv_title": "مصفوفة الخدمات التجارية والتعاقد",
    "page_srv_sub": "منظومة متكاملة من 5 أركان تشغيلية مصممة لتلبية احتياجات الشركات، المصانع، والمستثمرين في التجارة الإقليمية والدولية.",

    "page_ct_tag": "تواصل معنا مباشرة",
    "page_ct_title": "قنوات الاتصال المباشر والمكاتب",
    "page_ct_sub": "فريقنا المتخصص في مسقط جاهز لاستقبال استفساراتكم ومناقشة تفاصيل صفقاتكم وشراكاتكم التجارية.",

    "page_rq_tag": "خدمة المستثمرين والتجار",
    "page_rq_title": "طلب استشارة تجارية وصفقة جديدة",
    "page_rq_sub": "يرجى تعبئة النموذج أدناه وسيقوم أحد مستشارينا التجاريين بالتواصل معكم خلال 24 ساعة لدراسة طلبكم.",

    "page_faq_tag": "دليل المعلومات والأسئلة",
    "page_faq_title": "الأسئلة الشائعة والإجابات المؤسسية",
    "page_faq_sub": "كل ما تحتاج معرفته حول آليات عمل بيت التجارة الدولية تكامل، الامتثال المصرفي، وشروط التعاقد.",

    "page_priv_tag": "الشفافية والحوكمة",
    "page_priv_title": "سياسة الخصوصية وحماية البيانات",
    "page_priv_sub": "التزامنا الراسخ بحماية سرية المعلومات التجارية والبيانات الشخصية لشركائنا وعملائنا.",

    "page_term_tag": "الأطر القانونية والتعاقدية",
    "page_term_title": "الشروط والأحكام العامة",
    "page_term_sub": "القواعد المنظمة لاستخدام منصة تكامل والتعامل التجاري وفق القانون العماني والأعراف الدولية."
  },
  "fa": {
    "page_it_tag": "رکن اول • مجوز بنیادین",
    "page_it_title": "بازرگانی بین‌الملل و خانه تجارت (International Trading House)",
    "page_it_sub": "پلتفرم حرفه‌ای وساطت تجاری، انعقاد معاملات فرامرزی، و اخذ نمایندگی برندهای بین‌المللی با مبدأ سلطنت عمان.",
    "it_c1_title": "خرید و فروش بین‌المللی کالا",
    "it_c1_desc": "مدیریت معاملات تجاری دوجانبه، پیوند کارخانجات آسیا و اروپا با خریداران خاورمیانه و اجرای قراردادها با انضباط کامل.",
    "it_c2_title": "نمایندگی و کارگزاری تجاری",
    "it_c2_desc": "نمایندگی رسمی کارخانجات خارجی متقاضی حضور در عمان و خلیج فارس تحت چتر قانونی و بازاریابی تخصصی.",
    "it_c3_title": "مدیریت قراردادهای اینکوترمز",
    "it_c3_desc": "تنظیم و اجرای قراردادهای بازرگانی منطبق با استاندارد اینکوترمز ۲۰۲۰ و مدیریت حرفه‌ای ریسک‌های ترانزیت.",
    "it_ops_title": "فهرست خدمات اجرایی در بازرگانی بین‌الملل",
    "it_op_1": "وساطت تجاری و ساختاردهی معاملات سه‌جانبه (Cross-Trade)",
    "it_op_2": "مذاکره مستقیم با تولیدکنندگان جهانی و تثبیت نرخ قراردادها",
    "it_op_3": "مطالعات بازار و توسعه کانال‌های توزیع در کشورهای حوزه خلیج فارس",
    "it_op_4": "انعقاد قراردادهای الزام‌آور بین‌المللی و صیانت از منافع طرفین",
    "it_op_5": "صادرات مجدد از مناطق آزاد با مزایای تعرفه‌ای ممتاز",
    "it_op_6": "طراحی مدل‌های جوینت ونچر (JV) و ائتلاف‌های استراتژیک صنعتی",

    "page_ie_tag": "رکن دوم • زنجیره تأمین فرامرزی",
    "page_ie_title": "واردات، صادرات و صادرات مجدد (Import, Export & Re-Export)",
    "page_ie_sub": "راهکارهای جامع لجستیکی برای اتصال بنادر عمان به شاهراه‌های تجاری جهان و ترانزیت بدون اصطکاک کالا.",
    "ie_c1_title": "صادرات محصولات تولیدی عمان",
    "ie_c1_desc": "گسترش بازارهای هدف برای کالاهای ساخت عمان با بهره‌گیری از تعرفه صفر در چارچوب معاهدات تجارت آزاد.",
    "ie_c2_title": "واردات و ترخیص گمرکی تخصصی",
    "ie_c2_desc": "مدیریت واردات اقلام اساسی و مواد اولیه از طریق سامانه گمرکی بیان در بنادر صحار، صلاله و دقم.",
    "ie_c3_title": "صادرات مجدد و انبارداری باندی",
    "ie_c3_desc": "دپو و مدیریت کالا در انبارهای مناطق آزاد بدون پرداخت حقوق گمرکی و ارسال مجدد به مقاصد منطقه‌ای.",

    "page_pr_tag": "رکن سوم • تدارکات صنعتی و پروژه‌ای",
    "page_pr_title": "تأمین و تدارکات پروژه‌ها (Project Procurement & Supply)",
    "page_pr_sub": "تأمین مواد اولیه صنعتی، ماشین‌آلات پیشرفته و خطوط تولید برای کارخانجات و شرکت‌های عمرانی در عمان و منطقه.",
    "pr_c1_title": "مواد اولیه و کالاهای پایه",
    "pr_c1_desc": "تأمین محصولات پتروشیمی، فلزات، پلیمرها و مصالح استراتژیک ساختمانی با نرخ‌های رقابتی و دست اول.",
    "pr_c2_title": "ماشین‌آلات و خطوط تولید صنعتی",
    "pr_c2_desc": "واردات تجهیزات پیشرفته صنعتی و ماشین‌آلات سنگین از سازندگان معتبر آسیا و اروپا به مقصد پروژه‌ها.",
    "pr_c3_title": "بازرسی و کنترل کیفیت مبدأ",
    "pr_c3_desc": "انجام بازرسی‌های فنی در کشور مبدأ جهت تضمین انطباق کامل محموله‌ها با استانداردهای عمان و خلیج فارس.",

    "page_fa_tag": "رکن چهارم • راهکارهای اعتباری و بانکی",
    "page_fa_title": "مشاوره پرداخت و اعتبارات اسنادی (Trade Advisory & L/Cs)",
    "page_fa_sub": "مشاوره تخصصی در مهندسی ابزارهای پرداخت بین‌المللی، مدیریت اعتبارات اسنادی و پوشش ریسک‌های نقدینگی.",
    "fa_c1_title": "اعتبارات اسنادی (LC)",
    "fa_c1_desc": "مشاوره حقوقی و بانکی در تنظیم و بازگشایی ال‌سی‌های بین‌المللی با هدف محافظت از منابع مالی خریدار و فروشنده.",
    "fa_c2_title": "ضمانت‌نامه‌های بانکی (LG)",
    "fa_c2_desc": "مشاوره صدور ضمانت‌نامه‌های پیش‌پرداخت، حسن انجام کار و شرکت در مناقصات از طریق بانک‌های معتبر عمانی.",
    "fa_c3_title": "ارزیابی ریسک طرف‌های تجاری",
    "fa_c3_desc": "اعتبارسنجی خریداران و فروشندگان خارجی و تحلیل ریسک‌های انتقال ارز پیش از نهایی‌سازی معاملات بزرگ.",

    "page_mo_tag": "رکن پنجم • بومی‌سازی و ارزش افزوده",
    "page_mo_title": "زیرساخت تولید و برند ساخت عمان (Made in Oman)",
    "page_mo_sub": "همراهی سرمایه‌گذاران در راه‌اندازی کارخانه و بهره‌مندی از پیمان تجارت آزاد آمریکا و معافیت‌های مالیاتی کامل.",
    "mo_c1_title": "تأسیس و اخذ مجوزهای کارخانه",
    "mo_c1_desc": "اخذ ثبت تجاری، مجوزهای صنعتی و اجاره اراضی در شهرک‌های صنعتی مدائن و مناطق آزاد تجاری عمان.",
    "mo_c2_title": "گواهی مبدأ ملی عمان",
    "mo_c2_desc": "تأمین شاخص ارزش افزوده داخلی (ICV) و اخذ گواهی رسمی ساخت عمان جهت صادرات بدون عوارض گمرکی به آمریکا.",
    "mo_c3_title": "مزایای مناطق آزاد تجاری",
    "mo_c3_desc": "مالکیت ۱۰۰٪ بدون نیاز به شریک محلی، معافیت دائمی از مالیات بر درآمد و آزادی کامل در انتقال ارز و سرمایه.",

    "page_ab_tag": "درباره هلدینگ و چشم‌انداز",
    "page_ab_title": "پیشگام در بازرگانی بین‌الملل و توسعه صنعتی",
    "page_ab_sub": "شرکت بازرگانی بین‌المللی تکامل، خانه‌ای برای پیوند پایدار سرمایه‌گذاران با فرصت‌های کم‌نظیر تجارت و تولید در سلطنت عمان.",
    "ab_c1_title": "چشم‌انداز استراتژیک",
    "ab_c1_desc": "تبدیل شدن به برترین پلتفرم تجاری برای شرکت‌های پیشرو در راه‌اندازی هاب‌های تولیدی و بازرگانی در عمان.",
    "ab_c2_title": "مأموریت سازمانی",
    "ab_c2_desc": "ارائه خدمات بازرگانی استاندارد و امن که موجب خلق ارزش افزوده اقتصادی و تحقق اهداف سند چشم‌انداز عمان ۲۰۴۰ گردد.",
    "ab_c3_title": "ارزش‌های بنیادین",
    "ab_c3_desc": "شفافیت مطلق، انضباط حقوقی، امانت‌داری کامل در معاملات، و تعهد بی‌قیدوشرط به حفظ محرمانگی اسرار تجاری موکلان.",

    "page_srv_tag": "راهنمای جامع خدمات",
    "page_srv_title": "ماتریس خدمات و مدل‌های همکاری تجاری",
    "page_srv_sub": "مجموعه‌ای یکپارچه از ۵ رکن عملیاتی برای پوشش تمامی نیازهای تجار، تولیدکنندگان و سرمایه‌گذاران صنعتی.",

    "page_ct_tag": "ارتباط مستقیم با کارشناسان",
    "page_ct_title": "دفاتر اداری و پل‌های ارتباطی",
    "page_ct_sub": "تیم مستقر ما در مسقط آماده بررسی نیازهای بازرگانی و میزبانی از مذاکرات دوجانبه شماست.",

    "page_rq_tag": "خدمات ویژه بازرگانان",
    "page_rq_title": "ثبت درخواست مشاوره و مذاکره تجاری",
    "page_rq_sub": "لطفاً فرم زیر را تکمیل فرمایید؛ کارشناس ارشد بازرگانی تکامل ظرف کمتر از ۲۴ ساعت کاری با شما تماس خواهد گرفت.",

    "page_faq_tag": "پایگاه دانش بازرگانی",
    "page_faq_title": "پرسش‌های پرتکرار و الزامات حقوقی",
    "page_faq_sub": "پاسخ‌های شفاف و رسمی پیرامون رویه‌های گمرکی، روش‌های پرداخت و الزامات قانونی فعالیت در عمان.",

    "page_priv_tag": "شفافیت و امنیت اطلاعات",
    "page_priv_title": "سیاست حفظ حریم خصوصی و محرمانگی داده‌ها",
    "page_priv_sub": "تعهد رسمی هلدینگ تکامل به حراست همه‌جانبه از اسرار تجاری و اطلاعات سازمانی شرکای تجاری.",

    "page_term_tag": "مقررات حقوقی و قراردادی",
    "page_term_title": "شرایط و ضوابط عمومی استفاده از خدمات",
    "page_term_sub": "اصول حاکم بر ارائه خدمات مشاوره و اجرای معاملات بر پایه قوانین تجاری عمان و استانداردهای بین‌المللی."
  },
  "en": {
    "page_it_tag": "Pillar I • Core Charter",
    "page_it_title": "International Trading House (Institutional Commerce)",
    "page_it_sub": "Institutional platform for high-volume transactions, exclusive commercial representation, and managing cross-border trade desks out of Oman.",
    "it_c1_title": "Global Commodity Sourcing & Sales",
    "it_c1_desc": "Structuring international trade transactions, connecting vetted suppliers in Asia/Europe with regional MENA buyers with full execution.",
    "it_c2_title": "Commercial Agency & Representation",
    "it_c2_desc": "Acting as trusted local and regional commercial agent for international manufacturers expanding into Oman and GCC markets.",
    "it_c3_title": "Incoterms Risk & Contract Lifecycle",
    "it_c3_desc": "Drafting and executing robust sales agreements governed by ICC Incoterms 2020 rules with comprehensive risk mitigation.",
    "it_ops_title": "Operational Capabilities in International Trade",
    "it_op_1": "Cross-trade structuring and back-to-back deal execution",
    "it_op_2": "Direct manufacturer negotiations and price hedging",
    "it_op_3": "Regional market intelligence and wholesale distribution setup",
    "it_op_4": "Enforceable commercial agreements under Omani trade law",
    "it_op_5": "Zero-tariff transshipment through bonded freezone facilities",
    "it_op_6": "Strategic Joint Ventures (JV) and commercial consortiums",

    "page_ie_tag": "Pillar II • Supply Chain Orchestration",
    "page_ie_title": "Import, Export & Re-Export (Global Freight & Customs)",
    "page_ie_sub": "Comprehensive supply chain infrastructure connecting Oman's world-class maritime ports to global consumer and industrial markets.",
    "ie_c1_title": "Omani-Origin Export Development",
    "ie_c1_desc": "Unlocking foreign export markets for products manufactured in Oman, capturing bilateral FTA tariff exemptions.",
    "ie_c2_title": "Import Logistics & Bayan Customs Release",
    "ie_c2_desc": "Managing institutional import clearances and regulatory documentation at Sohar Port, Salalah Port, and Duqm SEZAD.",
    "ie_c3_title": "Re-Export & Bonded Warehousing",
    "ie_c3_desc": "Bonded storage, break-bulk, and swift re-export to regional GCC and East African markets with zero customs duty.",

    "page_pr_tag": "Pillar III • Industrial Procurement",
    "page_pr_title": "Project Procurement & Supply (Raw Materials & Machinery)",
    "page_pr_sub": "Securing essential raw materials, production lines, and heavy machinery for industrial developers and infrastructure contractors.",
    "pr_c1_title": "Strategic Industrial Feedstocks",
    "pr_c1_desc": "Direct sourcing of polymers, petrochemicals, industrial metals, and foundational construction materials at bulk institutional pricing.",
    "pr_c2_title": "Industrial Machinery & Production Lines",
    "pr_c2_desc": "Turnkey equipment importation and delivery coordination from tier-one manufacturers in Asia, Europe, and the Americas.",
    "pr_c3_title": "Pre-Shipment Quality Assurance",
    "pr_c3_desc": "Origin inspection, SGS/Bureau Veritas compliance verification, ensuring adherence to Omani and GCC technical standards.",

    "page_fa_tag": "Pillar IV • Trade Structuring",
    "page_fa_title": "Trade Finance Advisory & L/Cs (Transactional Liquidity)",
    "page_fa_sub": "Specialized consulting on international payment structures, Documentary Letters of Credit, and securing counterparty obligations.",
    "fa_c1_title": "Documentary Letters of Credit (L/C)",
    "fa_c1_desc": "Structuring issuance and review of commercial L/Cs to safeguard both buyer capital and seller delivery compliance.",
    "fa_c2_title": "Bank Guarantee Advisory (L/G)",
    "fa_c2_desc": "Advising on Performance Bonds, Advance Payment Guarantees, and Bid Bonds issued through licensed commercial banks.",
    "fa_c3_title": "Counterparty & Sovereign Risk Analysis",
    "fa_c3_desc": "Vetting international suppliers and buyers, assessing currency volatility, and structuring risk-hedged escrow mechanisms.",

    "page_mo_tag": "Pillar V • Industrial Value",
    "page_mo_title": "Industrialization & Made in Oman (US FTA Captive Growth)",
    "page_mo_sub": "Guiding international manufacturers in establishing Omani facilities and capturing 0% US-Oman Free Trade Agreement export benefits.",
    "mo_c1_title": "Plant Setup & Industrial Licensing",
    "mo_c1_desc": "Securing industrial licenses, environmental permits, and leasing strategic plots within Madayn industrial estates and freezones.",
    "mo_c2_title": "Omani Certificate of Origin",
    "mo_c2_desc": "Achieving In-Country Value (ICV) thresholds to qualify for national Certificate of Origin and zero-duty US export entry.",
    "mo_c3_title": "Freezone Sovereignty Incentives",
    "mo_c3_desc": "100% foreign ownership, 0% corporate and personal income taxes, and uninhibited capital repatriation.",

    "page_ab_tag": "About Our Holding & Vision",
    "page_ab_title": "Leading Sovereign Trade & Industrial Expansion",
    "page_ab_sub": "Al Takamul International Trading LLC is an institutional trading house headquartered in Muscat, serving as the bridge for global trade into Oman.",
    "ab_c1_title": "Strategic Vision",
    "ab_c1_desc": "To stand as the preeminent commercial hub for global firms seeking to establish Middle Eastern manufacturing and logistics bases in Oman.",
    "ab_c2_title": "Corporate Mission",
    "ab_c2_desc": "Delivering rigorous, transparent commercial operations that drive shareholder value while accelerating Oman Vision 2040 goals.",
    "ab_c3_title": "Core Values",
    "ab_c3_desc": "Absolute transactional integrity, rigorous legal compliance, and steadfast protection of partner confidentiality.",

    "page_srv_tag": "Complete Services Catalog",
    "page_srv_title": "Services Matrix & Engagement Framework",
    "page_srv_sub": "An integrated suite of 5 operational pillars engineered to support traders, manufacturers, and international developers.",

    "page_ct_tag": "Direct Communication Desks",
    "page_ct_title": "Headquarters & Global Inquiry Desks",
    "page_ct_sub": "Our executive team in Muscat welcomes your inquiries to structure transactions, partnerships, and facility tours.",

    "page_rq_tag": "Investor & Merchant Services",
    "page_rq_title": "Request Trade Consultation & Advisory",
    "page_rq_sub": "Complete the form below. An executive trade advisor will review your specifications and reply within 24 business hours.",

    "page_faq_tag": "Knowledge Base & Guidelines",
    "page_faq_title": "Frequently Asked Questions & Advisory Rules",
    "page_faq_sub": "Clear, verified explanations on customs protocols, trade finance structures, and engagement requirements.",

    "page_priv_tag": "Governance & Security",
    "page_priv_title": "Privacy Policy & Data Protection",
    "page_priv_sub": "Our institutional commitment to safeguarding sensitive commercial data, counterpart identities, and transaction specifics.",

    "page_term_tag": "Legal & Commercial Terms",
    "page_term_title": "Terms of Service & Engagement Guidelines",
    "page_term_sub": "The legal terms governing interactions, advisory services, and transactions under the commercial laws of the Sultanate of Oman."
  }
}

# Merge extra_keys into master translations dictionary
for lang in ['ar', 'fa', 'en']:
    t[lang].update(extra_keys[lang])

with open(os.path.join(BASE_DIR, 'translations.json'), 'w', encoding='utf-8') as f:
    json.dump(t, f, ensure_ascii=False, indent=2)

with open(os.path.join(BASE_DIR, 'js', 'translations_data.js'), 'w', encoding='utf-8') as f:
    f.write(f"window.ALT_TRANSLATIONS = {json.dumps(t, ensure_ascii=False)};")

print("Added all subpage keys to translations.json and translations_data.js!")
