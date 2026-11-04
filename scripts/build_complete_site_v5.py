import json, os, re

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'

# Load existing translations
with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
    t = json.load(f)

print(f"Initial keys count: {len(t['ar'])}")

# Helper to register translations safely
def register_trans(key, ar, fa, en):
    t['ar'][key] = ar
    t['fa'][key] = fa
    t['en'][key] = en

# 1. Register Nav and Common Keys
register_trans("nav_home", "الرئيسية", "صفحه اصلی", "Home")
register_trans("nav_about", "من نحن", "درباره ما", "About Us")
register_trans("nav_services", "خدماتنا", "خدمات ما", "Our Services")
register_trans("nav_hubs", "الموانئ والمناطق الحرة", "بنادر و مناطق آزاد", "Ports & Free Zones")
register_trans("nav_process", "آلية العمل", "فرایند اجرایی", "Execution Workflow")
register_trans("nav_contact", "اتصل بنا", "تماس با ما", "Contact Us")
register_trans("nav_faq", "الأسئلة الشائعة", "پرسش‌های متداول", "FAQ")
register_trans("btn_request_short", "طلب استشارة", "درخواست مشاوره", "Consultation")
register_trans("btn_request", "طلب استشارة تجارية", "درخواست مشاوره تجاری", "Request Trade Consultation")
register_trans("brand_name", "شركة تكامل للتجارة الدولية", "بازرگانی بین‌المللی تکامل", "Al Takamul International Trading LLC")
register_trans("brand_sub", "Al Takamul International Trading LLC", "Al Takamul International Trading LLC", "Al Takamul International Trading LLC")

# 2. Register Hubs Page Keys
register_trans("hubs_page_tag", "البنية اللوجستية الاستراتيجية", "زیرساخت استراتژیک لجستیک", "Strategic Logistics Infrastructure")
register_trans("hubs_page_title", "بوابات عمان البحرية والمناطق الاقتصادية الخاصة", "بسترهای تجاری، بنادر و مناطق آزاد سلطنت عمان", "Oman Maritime Gateways & Special Economic Zones")
register_trans("hubs_page_sub", "موقع جيوسياسي فريد خارج مضيق هرمز يربط خطوط الملاحة بين آسيا وأوروبا وأفريقيا مع إعفاءات جمركية وضريبية تصل إلى 100%.", "موقعیت ژئوپلیتیک استثنایی در خارج از تنگه هرمز با اتصال به آب‌های آزاد اقیانوس هند و معافیت‌های ۱۰۰ درصدی مالیاتی و گمرکی.", "Exceptional geopolitical location outside the Strait of Hormuz connecting Asia, Europe, and Africa with 100% tax and customs exemptions.")

register_trans("hubs_stat_1_val", "خارج هرمز", "خارج از تنگه هرمز", "Outside Hormuz")
register_trans("hubs_stat_1_lbl", "ممر بحري مفتوح 100%", "دسترسی مستقیم به اقیانوس هند", "100% Open Ocean Access")

register_trans("hubs_stat_2_val", "0% ضرائب", "۰٪ مالیات شرکتی و فردی", "0% Tax")
register_trans("hubs_stat_2_lbl", "إعفاء ضريبي يصل لـ 25 عاماً", "معافیت مالیاتی تا ۲۵ سال در مناطق آزاد", "Up to 25-Year Tax Holidays")

register_trans("hubs_stat_3_val", "100% تملك", "۱۰۰٪ مالکیت خارجی", "100% Ownership")
register_trans("hubs_stat_3_lbl", "حرية كاملة لتحويل الأرباح", "انتقال نامحدود سود و سرمایه", "Full Capital Repatriation")

register_trans("hubs_stat_4_val", "اتفاقيات FTA", "معاهدات تجارت آزاد جهانی", "Global FTAs")
register_trans("hubs_stat_4_lbl", "تجارة حرة مع أمريكا ودول الخليج", "توافق تجارت آزاد با آمریکا و حوزه خلیج فارس", "US-Oman FTA & GCC Unified Market")

register_trans("hubs_sec1_tag", "المراكز اللوجستية المحورية", "هاب‌های اصلی ترانزیت و صنعت", "Pivotal Logistics Centers")
register_trans("hubs_sec1_title", "أربعة مراكز عالمية تدير تدفقات التجارة الدولية", "چهار بستر بین‌المللی پیشران تجارت و ترانزیت کالا", "Four Global Hubs Driving International Trade")
register_trans("hubs_sec1_sub", "تتكامل الموانئ والمناطق الحرة في سلطنة عمان لتقديم حلول شاملة للتخزين، التوزيع، وإعادة التصدير.", "همگرایی بنادر و مناطق آزاد عمان برای ارائه خدمات ذخیره‌سازی تحت کلید، انبارش سرد و صادرات مجدد.", "Integrated Omani ports and free zones offering bonded warehousing, cold chain, and re-export solutions.")

register_trans("hub_sohar_full_title", "ميناء ومنطقة صحار الحرة (Sohar Port & Freezone)", "بندر و منطقه آزاد صحار (Sohar)", "Sohar Port & Freezone")
register_trans("hub_sohar_full_desc", "المركز الصناعي واللوجستي الأسرع نمواً في الشرق الأوسط. يتميز برباط مباشر مع شبكة الطرق السريعة لدولة الإمارات العربية المتحدة ودول الخليج، مع محطات مخصصة للبتروكيماويات، المعادن، والمواد الغذائية السائبة وغاطس بحري يصل إلى 25 متراً.", "قطب صنعتی و لجستیکی با اتصال مستقیم زمینی به امارات و شبکه بزرگراهی خلیج فارس، اسکله‌های فوق‌عمیق ۲۵ متری و ترمینال‌های تخصصی پتروشیمی، فلزات و مواد غذایی.", "Fastest-growing industrial and logistics hub in the Middle East with direct highway links to UAE/GCC, dedicated petrochemical/metal/food terminals, and 25m deep-water berths.")
register_trans("hub_sohar_f1", "غاطس بحري عميق لاستقبال أضخم سفن الحاويات والصب الجاف", "اسکله‌های عمیق ۲۵ متری با قابلیت پهلوگیری بزرگ‌ترین کشتی‌های کانتینری", "Deep berths accommodating ultra-large container and bulk carriers")
register_trans("hub_sohar_f2", "مجمع غذائي وصناعي متكامل مع صوامع ومخازن تحت المظلة الجمركية", "خوشه یکپارچه صنایع غذایی و پتروشیمی همراه با انبارهای گمرکی اختصاصی", "Integrated food and industrial cluster with bonded silos and warehousing")
register_trans("hub_sohar_f3", "بوابة مباشرة وسريعة للسوق الإماراتي والخليجي عبر المنافذ البرية", "مسیر سریع صادرات زمینی به بازارهای امارات و شبه‌جزیره عربستان", "Express overland transit gateway to the UAE and broader GCC markets")

register_trans("hub_salalah_full_title", "ميناء ومنطقة صلالة الحرة (Salalah Port & Freezone)", "بندر و منطقه آزاد استراتژیک صلاله (Salalah)", "Salalah Port & Freezone")
register_trans("hub_salalah_full_desc", "أكبر ميناء لمناولة الحاويات العابرة في سلطنة عُمان على المحيط الهندي مباشرة. يختصر زمن الإبحار إلى أوروبا وأمريكا وأفريقيا بنحو أسبوعين مقارنة بموانئ الخليج العربي الداخلية، مع ممر شحن جوي-بحري يربطه بمطار صلالة الدولي في أقل من ساعتين.", "بزرگ‌ترین بندر ترانشیپ کانتینری عمان در ساحل مستقیم اقیانوس هند؛ صرفه‌جویی دو هفته‌ای در زمان حمل به اروپا و آمریکا در مقایسه با بنادر داخل خلیج فارس و دارای کریدور ترانزیت ترکیبی دریا-هوا.", "Oman's flagship Indian Ocean transshipment hub, cutting transit times to Europe and the Americas by two weeks compared to Upper Gulf ports, with a 2-hour sea-air multimodal corridor.")
register_trans("hub_salalah_f1", "موقع محيطي مباشر يتجاوز كافة مضائق التوتر الجيوسياسي الإقليمي", "موقعیت اقیانوسی مستقیم بدون نیاز به عبور از تنگه‌های تنش‌خیز منطقه‌ای", "Direct open-ocean positioning bypassing regional maritime chokepoints")
register_trans("hub_salalah_f2", "محطات حاويات عالمية بمناولة تتجاوز 4.5 مليون حاوية نمطية سنوياً", "ظرفیت کانتینری سالانه بیش از ۴.۵ میلیون TEU با استاندارد جهانی APM", "World-class terminal handling over 4.5 million TEU annually")
register_trans("hub_salalah_f3", "بنية لوجستية متطورة للأدوية والأغذية المبردة وسلاسل التبريد العميقة", "زیرساخت پیشرفته زنجیره سرمایش دارویی، شیلات و مواد پروتئینی", "State-of-the-art cold chain infrastructure for pharmaceuticals and perishables")

register_trans("hub_duqm_full_title", "المنطقة الاقتصادية الخاصة بالدقم (SEZAD)", "منطقه ویژه اقتصادی دقم (SEZAD)", "Duqm Special Economic Zone (SEZAD)")
register_trans("hub_duqm_full_desc", "أضخم مشروع اقتصادي متكامل في الشرق الأوسط بمساحة 2,000 كم². يضم ميناء الدقم التجاري المتعدد الأغراض، الحوض الجاف لإصلاح السفن العملاقة، مصفاة الدقم، ومجمعات الهيدروجين الأخضر والصناعات الثقيلة ومستودعات التخزين الاستراتيجي للنفط والغاز والبضائع.", "بزرگ‌ترین پهنه اقتصادی یکپارچه خاورمیانه با مساحت ۲,۰۰۰ کیلومتر مربع شامل بندر تجاری چندمنظوره، حوض خشک تعمیرات سوپرتانکرها، پالایشگاه، مزارع هیدروژن سبز و انبارهای استراتژیک کالا.", "The Middle East's largest special economic zone (2,000 km²) featuring a multipurpose deep seaport, supertanker dry dock, oil refinery, green hydrogen complexes, and strategic bulk reserves.")
register_trans("hub_duqm_f1", "حوض جاف عالمي متقدم لصيانة وإصلاح ناقلات النفط وسفن الصب", "حوضچه خشک عظیم برای تعمیر و نگهداری پیشرفته سوپرتانکرها و شناورهای تجاری", "World-class drydock for repairs and maintenance of supertankers and bulkers")
register_trans("hub_duqm_f2", "أراضي صناعية ولوجستية بمساحات غير محدودة وعقود انتفاع طويلة الأمد", "اراضی لجستیکی و صنعتی وسیع با قراردادهای واگذاری بلندمدت و تعرفه‌های رقابتی", "Vast industrial land parcels with attractive long-term usufruct lease agreements")
register_trans("hub_duqm_f3", "منظومة إعفاءات ضريبية وحوافز استثمارية ملكية بنسبة 100%", "بسته جامع معافیت‌های مالیاتی و گمرکی تا سقف ۳۰ سال و مالکیت تام خارجی", "Comprehensive 30-year tax exemptions package and 100% foreign enterprise ownership")

register_trans("hub_khazaen_full_title", "مدينة خزائن الاقتصادية والمنطقة الحرة بالمزيونة", "شهر اقتصادی خزائن و منطقه آزاد المزیونه", "Khazaen Economic City & Al Mazunah Freezone")
register_trans("hub_khazaen_full_desc", "خزائن هي الميناء الجاف والمركز اللوجستي الأوسط الرابط بين مسقط وصحار، بينما المزيونة تمثل المنفذ البري الاستراتيجي لتجارة الترانزيت نحو الجمهورية اليمنية وأسواق شرق أفريقيا مع مزايا تجارة تفضيلية للمصدرين والمستوردين.", "خزائن به عنوان بندر خشک و مرکز لجستیک پیونددهنده مسقط و صحار عمل کرده و المزیونه دروازه زمینی ترانزیت به یمن و شرق آفریقا با معافیت‌های تجاری است.", "Khazaen serves as the premier inland dry port linking Muscat and Sohar, while Al Mazunah forms the strategic land gateway to Yemen and East Africa.")
register_trans("hub_khazaen_f1", "ميناء جاف ذكي يربط محطات الحاويات البحرية بالعاصمة مسقط", "بندر خشک هوشمند با اتصال ریلی و جاده‌ای سریع به محوطه پایتخت", "Smart inland dry port seamlessly connecting sea terminals with Muscat")
register_trans("hub_khazaen_f2", "منفذ بري متكامل لتجارة إعادة التصدير والترانزيت إلى الأسواق المجاورة", "گذرگاه اختصاصی ترانزیت و صادرات مجدد کالا به کشورهای همجوار", "Dedicated overland gateway for re-export and transit trade to regional markets")
register_trans("hub_khazaen_f3", "مستودعات مكيفة وحلول تخزين ذكية قصيرة وطويلة الأجل", "انبارهای مدرن با مدیریت هوشمند موجودی کالا و سردخانه‌های مجهز", "Climate-controlled smart warehousing for short and long-term inventories")

register_trans("hubs_services_tag", "خدمات تكامل الميدانية", "خدمات میدانی و حقوقی تکامل", "Al Takamul On-Site Services")
register_trans("hubs_services_title", "كيف تمكنك تكامل من استثمار مزايا المناطق الحرة؟", "نقش بازرگانی تکامل در بهره‌برداری تجاری از بنادر و مناطق آزاد", "How Al Takamul Powers Your Free Zone Operations")
register_trans("hubs_services_sub", "نوفر المظلة التجارية، القانونية، واللوجستية الكاملة للشركات الدولية الراغبة في تأسيس أعمالها أو عبور شحناتها عبر عُمان.", "ما زیرساخت حقوقی، لجستیکی و بازرگانی لازم برای ورود شرکت‌ها به بنادر عمان و ترخیص روان کالا را فراهم می‌سازیم.", "We deliver full commercial, legal, and operational infrastructure for global enterprises routing cargo through Oman.")

register_trans("hubs_serv1_title", "التخليص الجمركي الذكي عبر نظام بيان (Bayan)", "ترخیص گمرکی تخصصی در سامانه یکپارچه بیان (Bayan)", "Smart Customs Clearance via Bayan System")
register_trans("hubs_serv1_desc", "تسجيل وتخليص الشحنات مسبقاً قبل وصول السفن، وإصدار المعاملات الجمركية تحت بند الإعفاءات المعمول بها في المناطق الحرة دون تأخير.", "اظهار و ترخیص کالا پیش از پهلوگیری کشتی و بهره‌مندی حداکثری از معافیت‌های تعرفه‌ای بدون توقف کالا در مبادی ورودی.", "Pre-arrival clearance and electronic declaration ensuring zero demurrage and full free zone tariff exemptions.")

register_trans("hubs_serv2_title", "إدارة المستودعات الجمركية (Bonded Warehousing)", "مدیریت انبارهای تحت کلید گمرک (Bonded)", "Bonded Warehousing & Storage Management")
register_trans("hubs_serv2_desc", "تأمين مساحات تخزين جافة ومبردة داخل النطاق الجمركي المعفى لتخزين البضائع وإعادة تعبئتها وفرزها دون سداد أي رسوم جمركية مسبقة.", "اجاره و مدیریت انبارهای مسقف و روباز گمرکی برای دپوی کالا، سورتینگ و بسته‌بندی مجدد بدون پرداخت حقوق ورودی گمرک.", "Securing dry and temperature-controlled storage within customs-exempt zones with value-add packaging and sorting.")

register_trans("hubs_serv3_title", "إصدار شهادات المنشأ والعبور الترانزيت", "صدور گواهی مبدأ و اسناد ترانزیت بین‌المللی", "Certificates of Origin & Transit Documentation")
register_trans("hubs_serv3_desc", "توثيق عمليات إعادة التصدير عبر غرفة تجارة وصناعة عُمان والجهات المختصة للاستفادة من الاتفاقيات التجارية الخليجية والدولية.", "اخذ و تایید گواهی‌های مبدأ عمان جهت بهره‌مندی خریداران از تعرفه صفر در بازارهای شورای همکاری خلیج فارس و آمریکا.", "Attesting re-export shipments via Oman Chamber of Commerce to leverage preferential FTA tariff treatments.")

register_trans("hubs_serv4_title", "التمثيل القانوني وعقود الانتفاع الاستثماري", "نمایندگی قانونی و انعقاد قراردادهای انتفاع صنعتی", "Legal Representation & Usufruct Contracts")
register_trans("hubs_serv4_desc", "صياغة وتوقيع عقود استئجار الأراضي والمكاتب الصناعية مع إدارات المناطق الحرة وتوفير الغطاء التجاري المسجل رسمياً.", "انعقاد قراردادهای رسمی اجاره زمین‌های صنعتی و کارگاهی و مدیریت الزامات ثبت شرکت‌های سرمایه‌گذار در عمان.", "Negotiating and executing industrial land leases with zone authorities under full corporate and regulatory compliance.")

# 3. Register Process Page Keys
register_trans("proc_page_tag", "حوكمة العمليات التجارية", "حکمرانی و استانداردهای عملیاتی", "Operational Trade Governance")
register_trans("proc_page_title", "آلية العمل والمسار التنفيذي الشامل للصفقات", "فرایند اجرایی، چارچوب گام‌به‌گام و مدیریت قراردادها", "Execution Workflow & Trade Management Pipeline")
register_trans("proc_page_sub", "منهجية مؤسسية صارمة من 6 مراحل تضمن أمان التدفقات المالية، مطابقة المواصفات القياسية، والتسليم الدقيق وفق الإنكوترمز 2020.", "متدولوژی ساختاریافته ۶ مرحله‌ای برای تضمین امنیت مالی، بازرسی فنی استاندارد و تحویل به موقع بر مبنای قواعد اینکوترمز ۲۰۲۰.", "A rigorous 6-phase institutional framework ensuring financial security, strict quality conformity, and on-time Incoterms 2020 delivery.")

register_trans("proc_step1_badge", "المرحلة الأولى", "مرحله ۱", "Phase 1")
register_trans("proc_step1_title", "دراسة الجدوى والتدقيق التنظيمي والمطابقة", "امکان‌سنجی تجاری، اعتبارسنجی و تطبیق استانداردها", "Feasibility, Vetting & Regulatory Scrutiny")
register_trans("proc_step1_desc", "دراسة كود النظام المنسق للبضائع (HS Code)، فحص المتطلبات الفنية والمواصفات القياسية الخليجية (GSO)، والتحقق من الملاءة المالية والقانونية للمصنعين والمشترين من خلال سجلات التدقيق المالي المعتمدة.", "بررسی کدهای تعرفه گمرکی (HS Code)، انطباق با الزامات استاندارد سازمان ملی استاندارد عمان و خلیج فارس (GSO) و اعتبارسنجی کامل طرفین معامله.", "HS Code classification, GCC standardization (GSO) compliance analysis, and deep financial and corporate vetting of counterparties.")

register_trans("proc_step2_badge", "المرحلة الثانية", "مرحله ۲", "Phase 2")
register_trans("proc_step2_title", "صياغة العقود التجارية وهيكلة الإنكوترمز", "تنظیم قراردادهای حقوقی و قواعد اینکوترمز ۲۰۲۰", "Contract Structuring & Incoterms 2020")
register_trans("proc_step2_desc", "إعداد عقود بيع وشراء دولية ملزمة ثنائية اللغة، تحدد بدقة مسؤوليات الشحن والتأمين والمخاطر وفق (Incoterms 2020) مثل FOB, CIF, DAP, DDP مع إدراج شروط التحكيم التجاري المعتمدة في سلطنة عمان.", "تدوین قراردادهای دوزبانه بین‌المللی فروش کالا با تفکیک دقیق تعهدات حمل، بیمه، انتقال ریسک و تعیین مرجع داوری تجاری معتبر در عمان.", "Drafting binding bilingual sale agreements specifying risk transfer, shipping obligations under Incoterms 2020, and institutional arbitration clauses.")

register_trans("proc_step3_badge", "المرحلة الثالثة", "مرحله ۳", "Phase 3")
register_trans("proc_step3_title", "هندسة الدفع والضمانات المصرفية (L/C & Escrow)", "ساختاردهی پرداخت مالی و اعتبارات اسنادی بانکی", "Payment Structuring & Banking Guarantees")
register_trans("proc_step3_desc", "فتح وإدارة الاعتمادات المستندية غير القابلة للإلغاء المعززة (Irrevocable Confirmed L/C) أو الضمانات البنكية (Performance Bonds) وحسابات الضمان المعلقة (Escrow) عبر بنوك عُمانية ودولية رائدة لحماية السيولة وحقوق الشركاء.", "گشایش اعتبارات اسنادی دیداری و مدت‌دار معتبر، ضمانت‌نامه‌های بانکی حسن انجام کار و حساب‌های واسط تضمینی نزد بانک‌های تراز اول.", "Structuring irrevocable confirmed documentary credits (L/C), performance bonds, and escrow mechanisms via top-tier banks.")

register_trans("proc_step4_badge", "المرحلة الرابعة", "مرحله ۴", "Phase 4")
register_trans("proc_step4_title", "المطابقة ومراقبة الجودة والفحص قبل الشحن", "سورسینگ، ممیزی کیفیت و بازرسی قبل از بارگیری", "Sourcing, Quality Control & Pre-Shipment Inspection")
register_trans("proc_step4_desc", "متابعة خطوط الإنتاج وسحب العينات الفنية وإجراء الفحوصات المخبرية عبر شركات فحص دولية مستقلة (مثل SGS أو Bureau Veritas) وإصدار شهادة المطابقة المسبقة (Certificate of Conformity) المعتمدة قبل السماح بتحميل الشحنة.", "کنترل خطوط تولید، نمونه‌برداری آزمایشگاهی و صدور گواهی بازرسی بین‌المللی کالا از مراجع مستقل مانند SGS پیش از هرگونه بارگیری.", "Factory auditing, laboratory sample testing, and third-party pre-shipment inspection certificates (SGS, Bureau Veritas) before dispatch.")

register_trans("proc_step5_badge", "المرحلة الخامسة", "مرحله ۵", "Phase 5")
register_trans("proc_step5_title", "اللوجستيات والتخليص الجمركي في نظام بيان", "هماهنگی حمل، بارگیری و ترخیص هوشمند گمرکی", "Logistics Coordination & Bayan Customs Clearance")
register_trans("proc_step5_desc", "حجز مساحات الشحن البحري أو الجوي، إصدار بوالص الشحن الرسمية (Bill of Lading)، وتفعيل التخليص الإلكتروني المسبق في نظام 'بيان' الجمركي التابع لشرطة عمان السلطانية، واستيفاء كافة الموافقات الصحية والبيئية فور الرسو.", "رزرو خطوط کشتیرانی، صدور بارنامه رسمی، ثبت بارنامه در سامانه گمرکی بیان و اخذ تاییدیه سازمان‌های بهداشت و کشاورزی بدون توقف محموله.", "Ocean and air freight booking, bill of lading issuance, automated filing on Oman Police Bayan customs portal, and regulatory clearances.")

register_trans("proc_step6_badge", "المرحلة السادسة", "مرحله ۶", "Phase 6")
register_trans("proc_step6_title", "التفريغ، التخزين، والتسليم النهائي أو التصدير", "تخلیه انبار، توزیع نهایی یا صادرات مجدد با گواهی مبدأ", "Discharge, Warehousing, Final Delivery & Re-Export")
register_trans("proc_step6_desc", "تفريغ الشحنات في المستودعات الجمركية أو المخازن المركزية، وتنسيق النقل البري إلى موقع العميل النهائي، أو إعادة الشحن للأسواق الإقليمية مصحوبة بشهادة منشأ عُمانية رسمية تسجل القيمة المضافة.", "انبارش تحت کلید در مناطق آزاد، توزیع ناوگانی به مقصد نهایی خریدار، یا بازتوزیع منطقه‌ای با گواهی‌های ترانزیت و ارزش افزوده صادراتی.", "Discharge into bonded warehouses, secure domestic freight delivery, or regional re-export accompanied by validated certificates of origin.")

register_trans("proc_docs_tag", "التوثيق القانوني والجمركي", "مدارک و الزامات مستندسازی", "Documentation & Compliance Architecture")
register_trans("proc_docs_title", "قائمة الوثائق الإلزامية لحماية الصفقات التجارية", "فهرست اسناد رسمی موردنیاز برای اجرای امن معاملات", "Mandatory Trade Documents for Seamless Execution")
register_trans("proc_docs_sub", "تلتزم تكامل بإعداد وتدقيق حزمة الوثائق الكاملة لضمان سرعة الإفراج الجمركي وعدم تحمل أي غرامات تأخير أو رسوم أرضيات.", "تیم تکامل نظارت جامع بر اصالت و صحت اسناد گمرکی، بانکی و حمل‌ونقل را تضمین می‌نماید.", "Al Takamul manages the complete verified documentary packet to eliminate port demurrage and customs delays.")

register_trans("doc_inv_title", "الفاتورة التجارية المصدقة (Commercial Invoice)", "فاکتور رسمی بازرگانی ممهور (Commercial Invoice)", "Attested Commercial Invoice")
register_trans("doc_inv_desc", "تتضمن وصفاً دقيقاً للبضائع، البنود الجمركية، شروط الإنكوترمز، ومصدقة حسب الأصول من غرفة التجارة والسفارة المعنية.", "دربرگیرنده مشخصات کامل اقلام، کدهای تعرفه، ارزش کالا و تایید شده توسط اتاق بازرگانی.", "Itemized specifications, HS codes, declared values, and Chamber of Commerce attestation.")

register_trans("doc_bl_title", "بوليصة الشحن الأصلية (Bill of Lading / AWB)", "بارنامه رسمی بین‌المللی (Bill of Lading / AWB)", "Original Bill of Lading (B/L) / Air Waybill")
register_trans("doc_bl_desc", "سند الملكية النهائي الصادر عن الخط الملاحي أو شركة الطيران، يحدد ميناء التحميل وميناء التفريغ وجهة الاستلام.", "سند مالکیت قطعی کالا صادرشده توسط خط کشتیرانی بین‌المللی با ذکر بنادر مبدأ و مقصد.", "Definitive document of title issued by ocean carrier specifying discharge ports and consignee rights.")

register_trans("doc_co_title", "شهادة المنشأ الرسمية (Certificate of Origin)", "گواهی مبدأ رسمی (Certificate of Origin)", "Certificate of Origin (CoO)")
register_trans("doc_co_desc", "إثبات قانوني لمصدر البضائع للاستفادة من الإعفاءات الجمركية الخليجية واتفاقيات التجارة الحرة وتفادي أي تعريفات حمائية.", "اثبات مبدأ جغرافیایی تولید کالا جهت بهره‌مندی از تعرفه صفر در بازار کشورهای منطقه.", "Official proof of product manufacturing origin unlocking FTA duty exemptions and preferential treatments.")

register_trans("doc_pack_title", "قائمة التعبئة والأوزان (Packing List)", "پکینگ لیست جزئیات بارگیری (Packing List)", "Detailed Packing List")
register_trans("doc_pack_desc", "تفصيل دقيق لعدد الطرود، الحاويات، الأوزان الإجمالية والصافية، وأبعاد الصناديق لتسهيل الفحص الجمركي والتفريغ.", "شرح جزئی بسته‌بندی، ابعاد، اوزان خالص و ناخالص برای بازرسی فوری در محوطه گمرکی.", "Comprehensive package breakdown, gross/net weights, and container dimensions for customs verification.")

register_trans("doc_cert_title", "شهادة الفحص والمطابقة (Inspection Certificate)", "گواهی بازرسی و تطابق استاندارد (Inspection Certificate)", "Quality & Inspection Certificate")
register_trans("doc_cert_desc", "تقرير فني معتمد صادر عن وكالات الفحص المستقلة يثبت خلو الشحنة من العيوب ومطابقتها للمواصفات الفنية التعاقدية.", "گزارش آزمایشگاهی رسمی شرکت‌های بازرسی بین‌المللی مبنی بر سلامت و انطباق کیفی کالا.", "Independent inspection agency certification validating chemical, physical, and contractual conformity.")

register_trans("doc_ins_title", "بوليصة التأمين البحري (Marine Cargo Insurance)", "بیمه‌نامه معتبر باربری بین‌المللی (Cargo Insurance)", "Marine Cargo Insurance Policy")
register_trans("doc_ins_desc", "تغطية تأمينية شاملة وفق شروط معهد المكتتبين بلندن (Institute Cargo Clauses A) لحماية رأس المال ضد المخاطر البحرية.", "پوشش کامل بیمه‌ای کلوز A منطبق با شرایط انستیتو بیمه‌گران لندن برای جبران هرگونه خسارت حین حمل.", "Comprehensive Institute Cargo Clauses (A) coverage protecting cargo value against all maritime perils.")

print(f"Total keys after new pages: {len(t['ar'])}")

# Save updated translations
with open(os.path.join(BASE_DIR, 'translations.json'), 'w', encoding='utf-8') as f:
    json.dump(t, f, ensure_ascii=False, indent=2)

with open(os.path.join(BASE_DIR, 'js', 'translations_data.js'), 'w', encoding='utf-8') as f:
    f.write(f"window.ALT_TRANSLATIONS = {json.dumps(t, ensure_ascii=False)};")

print("Saved updated translations!")
