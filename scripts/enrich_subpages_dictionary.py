import json, os

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'
with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
    t = json.load(f)

def reg(k, ar, fa, en):
    t['ar'][k] = ar
    t['fa'][k] = fa
    t['en'][k] = en

# ABOUT PAGE RICH CONTENT
reg("about_sec_gov_tag", "الحوكمة والامتثال القانوني", "حاکمیت شرکتی و اعتبار حقوقی", "Corporate Governance & Compliance")
reg("about_sec_gov_title", "كيان تجاري مسجل وفق أرقى المعايير التنظيمية العمانية", "ساختار رسمی ثبت‌شده ذیل قوانین مترقی تجارت سلطنت عمان", "Formally Registered Entity under Omani Commercial Law")
reg("about_sec_gov_sub", "تلتزم شركة تكامل للتجارة الدولية (سجل تجاري: 1389420) بأعلى معايير الشفافية المالية والامتثال لأنظمة التجارة الدولية ومكافحة غسيل الأموال.", "بازرگانی بین‌المللی تکامل با شماره ثبت تجاری ۱۳۸۹۴۲۰ منطبق با استانداردهای بین‌المللی شفافیت، مبارزه با پولشویی و قوانین اتاق بازرگانی فعالیت می‌نماید.", "Operating under Omani Commercial Registration CR 1389420, fully compliant with international trade compliance, FATF standards, and OCC regulations.")

reg("about_card_reg_title", "السجل التجاري والترخيص الأساسي", "شماره ثبت تجاری و مجوزهای حاکمیتی", "Commercial Registration & Licensing")
reg("about_card_reg_desc", "سجل تجاري رقم 1389420 مسجل لدى وزارة التجارة والصناعة وترويج الاستثمار، بعضوية معتمدة في غرفة تجارة وصناعة عمان لتمثيل التجارة العامة والتصدير والاستيراد.", "ثبت رسمی در وزارت بازرگانی و صنایع عمان و عضویت فعال در اتاق بازرگانی و صنایع عمان برای کلیه فعالیت‌های تجاری، واردات و صادرات.", "CR 1389420 licensed by the Ministry of Commerce, Industry and Investment Promotion with accredited Oman Chamber of Commerce membership.")

reg("about_card_v2040_title", "التوافق مع رؤية عمان 2040", "همسویی بنیادین با سند چشم‌انداز عمان ۲۰۴۰", "Oman Vision 2040 Strategic Alignment")
reg("about_card_v2040_desc", "دعم أهداف التنويع الاقتصادي الوطني عبر ترسيخ سلطنة عمان كمركز لوجستي محوري يربط التجارة الإقليمية بالأسواق الدولية وتوطين الصناعات ذات القيمة المضافة.", "مشارکت فعال در تنوع‌بخشی به اقتصاد غیرنفتی و تبدیل عمان به پل ارتباطی تجارت منطقه با بهره‌گیری از زیرساخت‌های بندری پیشرفته.", "Actively driving economic diversification by anchoring Oman as a global logistics hub connecting regional and international supply chains.")

reg("about_card_risk_title", "إدارة المخاطر والشفافية المصرفية", "مدیریت ریسک و شفافیت تعاملات بانکی", "Risk Management & Banking Transparency")
reg("about_card_risk_desc", "معاملات خاضعة للتدقيق المستندي المستقل، مع قنوات مصرفية موثوقة وعقود تجارية تخضع لقوانين التحكيم التجاري المعتمدة دولياً ومحلياً.", "نظارت اسنادی دقیق بر تراکنش‌ها، استفاده از بسترهای بانکی معتبر و اعمال مراجع داوری حقوقی شناخته‌شده در قراردادهای فروش.", "Independent documentary verification, institutional banking relationships, and contracts governed by recognized commercial arbitration rules.")

reg("about_sec_pillars_tag", "الأركان المؤسسية", "ارکان استراتژیک", "Institutional Pillars")
reg("about_sec_pillars_title", "الركائز الأربع التي تبنى عليها صفقات تكامل", "چهار ستون راهبردی در مدیریت معاملات بین‌المللی", "Four Strategic Pillars Powering Al Takamul")

reg("about_pil_1_title", "السرعة والدقة في التنفيذ اللوجستي", "سرعت و انضباط در اجرای لجستیکی", "Speed & Precision in Logistics")
reg("about_pil_1_desc", "تقليص زمن عبور الحاويات والتخليص الجمركي المسبق عبر نظام بيان الإلكتروني لتفادي أي غرامات تأخير أو رسوم تخزين.", "کاهش زمان ماندگاری کانتینرها در گمرک با ثبت سیستمی پیش از ورود و جلوگیری کامل از هزینه‌های دموراژ.", "Minimizing container dwell times through pre-arrival Bayan electronic clearing and zero demurrage protocols.")

reg("about_pil_2_title", "الأمان المالي والاعتمادات المستندية", "امنیت مالی و اعتبارات اسنادی معتبر", "Financial Security & Documentary Credits")
reg("about_pil_2_desc", "استخدام هياكل دفع بنكية متطورة واعتمادات مستندية معززة غير قابلة للإلغاء لحماية أموال المشترين والموردين.", "بهره‌گیری از ابزارهای اعتبارات اسنادی بانکی دیداری و مدت‌دار جهت ایجاد بالاترین ضریب اطمینان مالی طرفین.", "Deploying advanced banking instruments and confirmed irrevocable L/Cs to safeguard buyer and supplier capital.")

reg("about_pil_3_title", "الجودة المطابقة للمواصفات العالمية", "تطابق کامل با استانداردهای کیفی جهانی", "Certified Global Quality Standards")
reg("about_pil_3_desc", "فحص البضائع عبر وكالات تفتيش دولية مستقلة وإصدار شهادات المطابقة القياسية (CoC) قبل مغادرة موانئ الشحن.", "بازرسی فنی محموله‌ها توسط موسسات مستقل بین‌المللی نظیر SGS و صدور گواهی استاندارد پیش از بارگیری.", "Independent third-party inspection and mandatory Certificate of Conformity verification before departure.")

reg("about_pil_4_title", "المرونة الجيوسياسية خارج المضائق", "انعطاف ژئوپلیتیک و امنیت آب‌های آزاد", "Geopolitical Resilience Outside Chokepoints")
reg("about_pil_4_desc", "تأمين تدفقات الإمداد عبر موانئ عمان المطلة على المحيط الهندي وبحر العرب بعيداً عن التوترات الإقليمية.", "تضمین تداوم زنجیره تأمین بدون ریسک اختلال در تنگه‌ها با پهلوگیری مستقیم در بنادر دریای عمان و اقیانوس هند.", "Ensuring supply continuity via direct open-ocean ports on the Indian Ocean and Arabian Sea, immune to regional chokepoints.")

# INTERNATIONAL TRADE RICH CONTENT
reg("it_sec_sectors_tag", "القطاعات السلعية", "دسته‌بندی کالایی", "Covered Commodity Sectors")
reg("it_sec_sectors_title", "محفظة السلع الأساسية التي ندير صفقاتها الدولية", "سبد کالاهای استراتژیک در معاملات بین‌المللی", "Key Commodities Managed Across Global Corridors")
reg("it_sec_sectors_sub", "خبرة ميدانية عميقة في إدارة سلاسل الإمداد للسلع الصناعية والغذائية والإنشائية مع الالتزام بأعلى معايير الجودة.", "تخصص تخصصی در تأمین و بازتوزیع مواد اولیه صنعتی، پتروشیمی، فلزات و محصولات کشاورزی استاندارد.", "Specialized expertise in sourcing, bulk shipping, and distributing industrial materials, petrochemicals, and agricultural commodities.")

reg("it_sec1_title", "المواد الغذائية والمنتجات الزراعية السائبة", "کالاهای اساسی، غلات و صنایع غذایی", "Food Commodities & Agricultural Bulk")
reg("it_sec1_desc", "إدارة عقود توريد الحبوب، السكر، الزيوت النباتية، المعكرونة، والأغذية المعلبة مع فحص دقيق للمعايير الصحية وشهادات الحلال الخليجية.", "تأمین غلات، دانه‌های روغنی، ماکارونی، رب گوجه‌فرنگی و کنسرویجات بر پایه استانداردهای غذایی بهداشتی خلیج فارس.", "Procurement contracts for grains, edible oils, pasta, tomato paste, and canned foods compliant with GCC Halal and phytosanitary rules.")

reg("it_sec2_title", "البتروكيماويات والبوليمرات والمذيبات الصناعية", "محصولات پتروشیمی، پلیمرها و حلال‌های صنعتی", "Petrochemicals, Polymers & Industrial Solvents")
reg("it_sec2_desc", "وساطة وتجارة حبيبات البلاستيك (PE, PP, PVC)، المواد الكيميائية الأساسية، وحلول التعبئة الصناعية من كبرى المجمعات البتروكيماوية.", "تجارت و توزیع انواع پلی‌اتیلن، پلی‌پروپیلن، پی‌وی‌سی و حلال‌های شیمیایی بر پایه آنالیزهای فنی آزمایشگاهی دقیق.", "Trading plastic resins (PE, PP, PVC), industrial chemical compounds, and raw materials directly from major petrochemical complexes.")

reg("it_sec3_title", "حديد التسليح والمعادن ومواد البناء الإنشائية", "فولاد، مقاطع ساختمانی و مصالح عمرانی", "Steel, Rebar, Metals & Construction Materials")
reg("it_sec3_desc", "عقود توريد كتل الحديد، حديد التسليح، الأنابيب الصناعية، الإسمنت المقاوم، والجبس لمشاريع البنية التحتية والإنشاءات الضخمة.", "تأمین میلگرد استاندارد، شمش فولادی، لوله‌های بدون درز، کلینکر و گچ ساختمانی برای کلان‌پروژه‌های عمرانی منطقه.", "Supplying prime steel billets, deformed rebar, seamless industrial pipes, clinker, and gypsum for mega infrastructure projects.")

reg("it_sec4_title", "المعدات الثقيلة وقطع الغيار الصناعية", "ماشین‌آلات صنعتی و تجهیزات خطوط تولید", "Industrial Machinery & Heavy Equipment")
reg("it_sec4_desc", "شراء وتوريد خطوط الإنتاج المتكاملة، معدات المناولة، المولدات الكهربائية، وقطع الغيار الأصلية المعتمدة من المصانع العالمية.", "خرید و حمل خطوط اتوماسیون صنعتی، ژنراتورهای نیروگاهی و قطعات یدکی با تضمین اصالت کالا و خدمات مهندسی.", "Sourcing complete manufacturing lines, power generators, handling gear, and OEM certified industrial components.")

# IMPORT EXPORT RICH CONTENT
reg("ie_sec_modes_tag", "أنماط وحلول الشحن والتخليص", "روش‌های حمل و ترخیص محموله‌ها", "Freight Modes & Transit Solutions")
reg("ie_sec_modes_title", "شبكة نقل متعددة الوسائط لتغطية كافة متطلبات التجارة", "شبکه چندوجهی حمل‌ونقل و ترخیص هوشمند گمرکی", "Multimodal Freight Network & Smart Bayan Clearing")
reg("ie_sec_modes_sub", "حلول لوجستية متكاملة تضمن أعلى كفاءة زمنية وتكلفة تشغيلية منافسة لجميع أنواع الشحنات البحرية، الجوية، والبرية.", "طراحی بهینه‌ترین مسیرهای حمل ترکیبی با محاسبه هزینه، سرعت و معافیت‌های گمرکی برای صاحبان کالا.", "Optimized transit routing balancing transit speed, handling cost, and regulatory exemptions across land, sea, and air.")

reg("ie_m1_title", "الشحن البحري بالحاويات الكاملة والمجمعة (FCL / LCL)", "حمل دریایی کانتینری دربست و خرده‌بار (FCL / LCL)", "Ocean Freight (FCL / LCL)")
reg("ie_m1_desc", "حجوزات مباشرة مع كبرى الخطوط الملاحية العالمية من وإلى موانئ صحار، صلالة، والدقم بحاويات قياسية ومبردة وخزانات ISO Tank.", "رزرو خطوط کشتیرانی بین‌المللی با کانتینرهای خشک، یخچالی (Reefer) و ایزوتانک برای مایعات با بهترین نرخ کرایه حمل.", "Direct carrier agreements for standard containers, reefer units, and ISO tanks connecting Sohar, Salalah, and Duqm globally.")

reg("ie_m2_title", "النقل البري الترانزيت عبر أسطول الشاحنات الخليجي", "ترانزیت زمینی ناوگانی به کشورهای شورای همکاری خلیج فارس", "Cross-Border Overland Trucking (GCC Network)")
reg("ie_m2_desc", "شاحنات مجهزة لنقل البضائع المبردة والجافة عبر المنافذ البرية العمانية مع الإمارات، السعودية، واليمن مع تصاريح العبور السريع.", "ناوگان تریلرهای چادری، کفی و یخچالی با بارنامه تیر (TIR) برای تحویل مستقیم درب به درب در امارات، عربستان و یمن.", "Fleet operations with dry and temperature-controlled trailers operating across Omani border posts with UAE, KSA, and Yemen under TIR.")

reg("ie_m3_title", "الشحن الجوي للشحنات العاجلة والحرجة (Air Cargo)", "حمل هوایی بار برای کالاهای حساس و فوری (Air Freight)", "Express Air Cargo Logistics")
reg("ie_m3_desc", "خدمات الشحن الجوي عبر مطاري مسقط وصلالة الدوليين للأدوية، الإلكترونيات الدقيقة، والعينات التجارية الحساسة ذات القيمة العالية.", "ارسال سریع محموله‌های دارویی، قطعات الکترونیک و نمونه‌های تجاری از طریق فرودگاه‌های بین‌المللی مسقط و صلاله.", "Air freight services via Muscat and Salalah airports for high-value components, pharmaceuticals, and urgent commercial samples.")

reg("ie_m4_title", "إعادة التصدير الجمركي من المستودعات الحرة (Re-Export)", "عملیات تخصصی صادرات مجدد از مناطق آزاد (Re-Export)", "Customs-Exempt Re-Export Operations")
reg("ie_m4_desc", "تفريغ البضائع بالمستودعات المعفاة، إعادة تعبئتها، وتصديرها بصفقات ثلاثية مع إصدار شهادات منشأ معتمدة تفيد القيمة المضافة.", "انبارش کالا بدون پرداخت عوارض ورودی، فرآوری، سورت و ارسال مجدد به مقاصد جدید با اسناد رسمی تجاری.", "Discharge into bonded facilities, sorting, re-packaging, and outbound dispatch under accredited value-add documentation.")

# PROCUREMENT RICH CONTENT
reg("proc_sec_cap_tag", "القدرات الفنية والتوريد", "توانمندی‌های فنی تدارکات", "Technical Sourcing Capabilities")
reg("proc_sec_cap_title", "توريد متكامل لاحتياجات مشاريع البنية التحتية والمصانع", "تأمین جامع تجهیزات برای پروژه‌های صنعتی و زیربنایی", "Turnkey Procurement for Infrastructure & Heavy Industries")
reg("proc_sec_cap_sub", "نوفر سلاسل توريد مؤمنة للمقاولين ومطوري المشاريع الصناعية مع الالتزام التام بالمواصفات الهندسية وجداول التسليم الصارمة.", "ایجاد زنجیره تأمین پایدار برای پیمانکاران EPC و کارخانجات صنعتی با نظارت بر انطباق دقیق نقشه‌ها و زمان‌بندی تحویل.", "Securing robust supply pipelines for EPC contractors and industrial developers with strict adherence to engineering specs.")

reg("proc_c1_title", "خطوط الإنتاج الصناعي ومحطات المعالجة", "خطوط اتوماسیون صنعتی و واحدهای فرآوری", "Industrial Manufacturing Lines & Process Units")
reg("proc_c1_desc", "توريد معدات التشكيل المعدني، خطوط التعبئة والتغليف الآلية، وحدات تكرير المياه، ومحطات المعالجة الحرارية والكيميائية.", "تأمین ماشین‌آلات فرمینگ فلزات، خطوط بسته‌بندی تمام‌اتوماتیک، تأسیسات تصفیه آب صنعتی و کوره‌های عملیات حرارتی.", "Sourcing metal forming machinery, automated packaging lines, industrial water treatment plants, and chemical process units.")

reg("proc_c2_title", "المواد الخام الوسيطة والمضافات الكيميائية", "مواد اولیه واسطه‌ای و افزودنی‌های تخصصی", "Intermediate Raw Materials & Specialty Additives")
reg("proc_c2_desc", "تأمين الكيماويات المتخصصة، الماسترباتش، كربونات الكالسيوم، الصمغ الصناعي، والبوليمرات اللازمة لتشغيل المصانع المحلية.", "سورسینگ مواد شیمیایی پایه، مستربچ رنگی، رزین‌های پلیمری و افزودنی‌های تولید لوله و پروفیل با گواهی آنالیز معتبر.", "Procuring specialty chemicals, color masterbatches, industrial resins, and polymer compounds with verified batch certificates.")

reg("proc_c3_title", "معدات توليد الطاقة وأنظمة التوليد الاحتياطي", "تجهیزات تولید برق و ژنراتورهای نیروگاهی", "Power Generation Equipment & Backup Turbines")
reg("proc_c3_desc", "توريد المحولات الكهربائية عالية الجهد، مولدات الديزل الصناعية، التوربينات، وأنظمة التحكم الآلي PLC للبيئات الصحراوية والصناعية.", "خرید ترانسفورماتورهای قدرت، دیزل ژنراتورهای سنگین کاترپیلار و کامینز، و تابلوهای کنترل هوشمند صنعتی مقاوم در برابر حرارت.", "High-voltage electrical transformers, industrial diesel generators, gas turbines, and PLC control cabinets engineered for arid environments.")

reg("proc_c4_title", "أنابيب النفط والغاز والصمامات الهندسية المعيارية", "لوله، اتصالات و شیرآلات صنعتی استانداردهای نفت و گاز", "API Pipes, Fittings & Specialized High-Pressure Valves")
reg("proc_c4_desc", "توريد أنابيب الفولاذ الكربوني غير الملحومة وفق معايير API 5L، الصمامات الكروية والبوابية، والفلنجات للمشاريع البترولية والمائية.", "تأمین لوله‌های بدون درز API 5L، شیرآلات فشار قوی صنعتی، اتصالات فورج‌شده و فلنج‌ها برای پروژه‌های پالایشگاهی و خطوط انتقال آب.", "API 5L certified seamless carbon steel pipes, high-pressure industrial ball/gate valves, and forged flanges for energy and water pipelines.")

# FINANCIAL ADVISORY RICH CONTENT
reg("fa_sec_tools_tag", "الأدوات المالية والائتمانية", "ابزارهای اعتباری و مالی", "Credit Instruments & Banking Tools")
reg("fa_sec_tools_title", "حلول مصرفية واستشارية مبتكرة لتمويل وتأمين الصفقات", "راهکارهای نوین ساختاردهی اعتباری و پوشش ریسک ارزی", "Innovative Banking & Credit Structuring Solutions")
reg("fa_sec_tools_sub", "نساعد الشركات على تصميم هياكل تمويل تجارية متقدمة تحافظ على سيولتها وتضمن استرداد الأموال مع الامتثال المصرفي الكامل.", "مشاوره اختصاصی در مهندسی ابزارهای بانکی بین‌المللی برای حفظ نقدینگی و حذف ریسک عدم وصول تعهدات مالی.", "Advising enterprises on advanced trade finance architectures that preserve cash flow while mitigating default risks.")

reg("fa_i1_title", "الاعتمادات المستندية غير القابلة للإلغاء (Irrevocable L/C)", "اعتبارات اسنادی دیداری و مدت‌دار (Sight & Usance L/C)", "Irrevocable Documentary Letters of Credit")
reg("fa_i1_desc", "هيكلة اعتمادات مستندية بالاطلاع (Sight L/C) أو مؤجلة الدفع (Usance L/C) معززة من بنوك دولية ذات تصنيف ائتماني رفيع تضمن السداد بمجرد مطابقة المستندات.", "تنظیم شرایط اعتبارات اسنادی دیداری و یوزانس با بررسی دقیق شرایط اسنادی، تاریخ بارگیری و مشخصات بانک ابلاغ‌کننده و معززکننده.", "Structuring Sight and Usance documentary credits confirmed by top-rated international banks guaranteeing payment upon documentary presentation.")

reg("fa_i2_title", "الاعتمادات الدوارة والمحولة (Revolving & Transferable L/C)", "اعتبارات اسنادی گردان و قابل‌انتقال (Revolving & Transferable)", "Revolving & Transferable L/C Architectures")
reg("fa_i2_desc", "حلول مثالية للتجار الدوليين ووسطاء الصفقات الثلاثية لتحويل الاعتماد لصالح المورد النهائي مع حماية هامش الربح والسرية التجارية.", "راهکار تخصصی برای بازرگانان واسطه‌ای جهت انتقال بخش ارزی به تأمین‌کننده نهایی با حفظ کامل محرمانگی حاشیه سود تجاری.", "Ideal frameworks for international trade intermediaries transferring credit portions to prime manufacturers while safeguarding commercial margins.")

reg("fa_i3_title", "خطابات الضمان المصرفي وسندات الإنجاز (Bank Guarantees & PB)", "ضمانت‌نامه‌های بانکی حسن انجام کار و پیش‌پرداخت", "Bank Guarantees & Performance Bonds (PB)")
reg("fa_i3_desc", "إصدار وإدارة ضمانات حسن التنفيذ (Performance Bond 10%)، ضمانات الدفعة المقدمة (APG)، وضمانات دخول المناقصات للمشاريع الكبرى.", "اخذ و تایید ضمانت‌نامه‌های رسمی بانکی اجرای قرارداد (۱۰٪)، ضمانت‌نامه استرداد پیش‌پرداخت و ضمانت‌های شرکت در مناقصه.", "Issuing and managing 10% performance bonds, advance payment guarantees, and tender bid bonds for large-scale institutional projects.")

reg("fa_i4_title", "حسابات الضمان المالي المشروط (Escrow Accounts)", "حساب‌های تضمینی امانی مشروط (Trade Escrow)", "Conditional Trade Escrow Mechanisms")
reg("fa_i4_desc", "إيداع أموال الصفقات لدى أطراف مصرفية أو قانونية معتمدة لا تفرج عن السيولة للمورد إلا بعد صدور تقرير الفحص الفني المستقل.", "مسدودسازی وجوه معامله در حساب امانی امین تا زمان ارائه گواهی بازرسی سلامت فیزیکی و تاییدیه اظهارنامه گمرکی در مقصد.", "Holding transaction funds in escrow accounts released only upon receipt of clean third-party inspection and shipping verification.")

# MADE IN OMAN RICH CONTENT
reg("mio_sec_val_tag", "القيمة المضافة والتصنيع المشترك", "ارزش افزوده و ساخت عمان", "Value-Add & Contract Manufacturing")
reg("mio_sec_val_title", "بوابة التصنيع الوطني والوصول التفضيلي للأسواق العالمية", "زیرساخت تولید قراردادی و جهش صادراتی با برند ساخت عمان", "National Manufacturing Gateway & Preferential Global Access")
reg("mio_sec_val_sub", "استثمر في المزايا التنافسية للغاز الصناعي، الكهرباء المدعومة، والإعفاءات الجمركية للوصول إلى أسواق تضم أكثر من مليار مستهلك.", "بهره‌مندی از انرژی مقرون‌به‌صرفه، معافیت‌های واردات ماشین‌آلات و صادرات بدون تعرفه به بازارهای آمریکا و کشورهای عربی.", "Leverage subsidized industrial utilities, zero raw material duties, and duty-free access to major world markets exceeding 1 billion consumers.")

reg("mio_v1_title", "اتفاقية التجارة الحرة مع الولايات المتحدة الأمريكية (US-Oman FTA)", "توافقنامه تجارت آزاد تاریخی عمان با ایالات متحده آمریکا", "US-Oman Free Trade Agreement (US FTA)")
reg("mio_v1_desc", "تصدير المنتجات المصنعة في عمان إلى السوق الأمريكي بتعريفة جمركية 0% وبدون أي قيود كوتا للمنتجات المستوفية لمعايير القيمة المضافة الوطنية.", "صادرات بدون تعرفه گمرکی (۰٪) و بدون سقف سهمیه‌بندی به بازار آمریکا برای محصولاتی که حداقل ۳۵٪ ارزش افزوده در عمان ایجاد کنند.", "Duty-free export to the United States market with 0% tariffs and zero quota restrictions for qualifying products meeting value-add criteria.")

reg("mio_v2_title", "شهادة المنشأ العمانية الموحدة لدول مجلس التعاون الخليجي", "گواهی مبدأ معتبر عمان برای معافیت گمرکی در کشورهای خلیج فارس", "Unified GCC Certificate of Origin")
reg("mio_v2_desc", "دخول بضائعك إلى أسواق السعودية والإمارات والكويت وقطر والبحرين بدون أي رسوم جمركية كمنتج وطني خليجي مستوفٍ لنسبة 40% قيمة مضافة.", "ورود آزاد کالا به بازارهای امارات، عربستان، کویت و قطر بدون حقوق گمرکی به عنوان کالای ملی کشورهای حوزه خلیج فارس.", "Tariff-free entry across Saudi Arabia, UAE, Kuwait, Qatar, and Bahrain under the GCC Unified Economic Agreement with 40% national value addition.")

reg("mio_v3_title", "التصنيع التعاقدي وتعبئة وتغليف العلامات التجارية (Private Label)", "تولید قراردادی بدون کارخانه و برچسب‌گذاری خصوصی (Private Label)", "Contract Manufacturing & Private Label Packaging")
reg("mio_v3_desc", "إنتاج منتجاتك في مصانع عمانية قائمة أو داخل ورش متخصصة دون الحاجة لبناء مصنع كامل، مع الاستفادة من علامة 'صُنع في عُمان'.", "تولید برون‌سپاری‌شده در خطوط صنعتی استاندارد عمان جهت کاهش هزینه سرمایه‌گذاری اولیه همراه با برند اختصاصی صاحب کالا.", "Outsourced manufacturing in certified Omani plants enabling asset-light operations under the prestigious 'Made in Oman' quality mark.")

reg("mio_v4_title", "حوافز مدائن والمدن الصناعية (Madayn Support)", "مشوق‌های استقرار در شهرهای صنعتی مدائن (Madayn)", "Madayn Industrial Parks Incentives")
reg("mio_v4_desc", "أراضي صناعية بأسعار إيجار رمزية مدعومة، إعفاءات جمركية على استيراد الآلات والمواد الخام، وتسهيلات حكومية سريعة لترخيص المشاريع.", "اجاره زمین‌های صنعتی مجهز به انشعابات آب، برق صنعتی و گاز ارزان، معافیت واردات تجهیزات و خطوط با اعطای تسهیلات دولتی.", "Subsidized industrial land, zero import customs on production machinery and raw inputs, and expedited single-window licensing via Madayn.")

print(f"Total keys after subpage enrichment: {len(t['ar'])}")

with open(os.path.join(BASE_DIR, 'translations.json'), 'w', encoding='utf-8') as f:
    json.dump(t, f, ensure_ascii=False, indent=2)

with open(os.path.join(BASE_DIR, 'js', 'translations_data.js'), 'w', encoding='utf-8') as f:
    f.write(f"window.ALT_TRANSLATIONS = {json.dumps(t, ensure_ascii=False)};")

print("Dictionary enrichment complete!")
