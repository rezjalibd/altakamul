import json, os

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'
with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
    t = json.load(f)

def reg(k, ar, fa, en):
    t['ar'][k] = ar
    t['fa'][k] = fa
    t['en'][k] = en

reg("btn_explore_service", "استكشاف تفاصيل الخدمة ←", "مشاهده جزئیات این خدمت ←", "Explore Service Details →")
reg("cta_tag", "بدء التعاون الاستراتيجي", "شروع همکاری استراتژیک", "Strategic Partnership")
reg("cta_title", "هل تخطط لتوسيع تجارتك الدولية أو توريد شحناتك عبر عُمان؟", "آیا به دنبال توسعه تجارت بین‌الملل یا ترانزیت کالا از طریق عمان هستید؟", "Planning to expand global trade or route shipments via Oman?")
reg("cta_sub", "فريقنا القانوني والتجاري واللوجستي جاهز لدراسة متطلباتك وتقديم حلول مخصصة لحماية رأس مالك وتسريع إنجاز الصفقات.", "تیم حقوقی، بازرگانی و لجستیکی تکامل آماده امکان‌سنجی نیازهای شما و ارائه راهکارهای مطمئن جهت حفظ سرمایه و تسریع معاملات است.", "Our legal, commercial, and logistics team is ready to analyze your requirements and deliver tailored solutions safeguarding capital.")

reg("page_about_tag", "الهوية المؤسسية والترخيص", "هویت سازمانی و مجوزها", "Corporate Identity & Licensing")
reg("page_about_title", "ريادة في إدارة صفقات التجارة الدولية وتطوير سلاسل الإمداد", "پیشگام در بازرگانی بین‌الملل، ترانزیت و توسعه سلاسل تأمین", "Pioneering Cross-Border Trade & Supply Chain Development")
reg("page_about_sub", "شركة تكامل للتجارة الدولية ش.م.م، بيت تجارة عُماني رائد يتخذ من العاصمة مسقط مقراً لربط الأسواق العالمية بمنطقة الخليج والشرق الأوسط.", "شرکت بازرگانی بین‌المللی تکامل، خانه تجارت معتبر مستقر در مسقط برای اتصال بازارهای بین‌المللی به عمان و کشورهای خلیج فارس.", "Al Takamul International Trading LLC: Oman's premier trading house based in Muscat linking global markets to the GCC and Middle East.")

reg("page_contact_tag", "المكتب الرئيسي وقنوات التواصل", "دفاتر اداری و پل‌های ارتباطی", "Headquarters & Inquiries")
reg("page_contact_title", "المكتب الرئيسي وقنوات التواصل المباشر", "دفاتر مرکزی و راه‌های ارتباط مستقیم با تکامل", "Muscat Headquarters & Direct Channels")
reg("page_contact_sub", "فريقنا التجاري والقانوني متاح للرد على استفساراتكم ومناقشة فرص التعاون والصفقات من الأحد إلى الخميس.", "کارشناسان بازرگانی و حقوقی تکامل از یکشنبه تا پنج‌شنبه آماده پاسخگویی به استعلامات و بررسی قراردادهای تجاری هستند.", "Our commercial and legal desk is available Sunday through Thursday to handle inquiries and evaluate commercial opportunities.")

reg("contact_c1_title", "الاتصال المباشر وواتساب", "ارتباط تلفنی و پشتیبانی واتساپ", "Direct Phone & WhatsApp")
reg("contact_c1_desc", "خطوط الاتصال المباشرة ومكتب خدمة العملاء عبر واتساب لخدمة الشركاء التجاريين على مدار الساعة.", "پاسخگویی سریع کارشناسان تجاری به تماس‌ها و پیام‌های کاری تجار و فعالان اقتصادی.", "Direct phone lines and dedicated WhatsApp customer desk serving partners worldwide.")

reg("contact_c2_title", "البريد الإلكتروني الرسمي", "مکاتبات رسمی و ثبت استعلام", "Official Corporate Email")
reg("contact_c2_desc", "لاستقبال طلبات عروض الأسعار، العقود الرسمية، والاستفسارات المالية والمصرفية المعتمدة.", "ارسال پروفرما، اسناد فنی مناقصات، درخواست‌های بانکی و اعتبارات اسنادی تجاری.", "Official mailbox for RFQs, contractual tenders, and banking verification documents.")

reg("contact_c3_title", "العنوان والمقر الرئيسي", "نشانی دفتر مرکزی عمان", "Muscat Corporate Office")
reg("contact_c3_desc", "سجل تجاري: 1389420 • منطقة الأعمال المركزية، محافظة مسقط، سلطنة عُمان.", "شماره ثبت تجاری: ۱۳۸۹۴۲۰ • منطقه مرکزی تجارت و کسب‌وکار، استان مسقط، سلطنت عمان.", "CR 1389420 • Central Business District, Muscat Governorate, Sultanate of Oman.")

reg("contact_form_title", "إرسال استفسار مباشر إلى الإدارة التجارية", "فرم ارسال پیام مستقیم به مدیریت بازرگانی", "Send Direct Message to Commercial Management")
reg("form_message", "شرح متطلبات الشحنة، بلد المنشأ، والمواصفات الفنية", "شرح مشخصات کالا، تناژ، شرایط اینکوترمز و الزامات پرداخت", "Cargo Specifications, Origin & Payment Terms")

reg("page_serv_tag", "المصفوفة التشغيلية المعتمدة", "ماتریس عملیاتی جامع", "Operational Services Matrix")
reg("page_serv_title", "مصفوفة الخدمات ونماذج الشراكة التجارية", "ماتریس خدمات و مدل‌های همکاری تجاری", "Commercial Services Matrix & Partnership Models")
reg("page_serv_sub", "منظومة متكاملة من 5 خدمات محورية مصممة لتلبية احتياجات الشركات العالمية، المستثمرين، والموردين في سلطنة عمان ومنطقة الخليج العربي.", "پنج خدمت بنیادین بازرگانی بین‌المللی برای پوشش کامل نیازهای واردکنندگان، صادرکنندگان و مجریان پروژه‌ها.", "Comprehensive portfolio of 5 core services tailored for global enterprises, investors, and industrial suppliers in Oman and GCC.")

reg("serv_badge_1", "الركن الأول", "ستون ۱", "Pillar 1")
reg("serv_badge_2", "الركن الثاني", "ستون ۲", "Pillar 2")
reg("serv_badge_3", "الركن الثالث", "ستون ۳", "Pillar 3")
reg("serv_badge_4", "الركن الرابع", "ستون ۴", "Pillar 4")
reg("serv_badge_5", "الركن الخامس", "ستون ۵", "Pillar 5")

reg("serv_card1_title", "1. التجارة الدولية وبيت التجارة (International Trading House)", "۱. بازرگانی بین‌الملل و خانه تجارت (Trading House)", "1. International Trading House & Cross-Border Deals")
reg("serv_card1_desc", "شراء وبيع البضائع والسلع لحسابنا أو لحساب الغير على المستوى الدولي، الوساطة التجارية الدولية وعقد الصفقات الكبرى، التمثيل التجاري والوكالات للشركات الأجنبية الراغبة في دخول السوق العماني والخليجي، وإدارة صفقات التجارة وفق شروط Incoterms 2020.", "خرید و فروش بین‌المللی کالا، مدیریت معاملات کلان، اخذ و اعطای نمایندگی انحصاری تجاری و تنظیم قراردادها بر مبنای اینکوترمز ۲۰۲۰.", "Sourcing and sales of commodities on principal and agency basis, cross-border brokering, commercial representation, and Incoterms 2020 governance.")

reg("serv_card2_title", "2. الاستيراد والتصدير وإعادة التصدير (Import, Export & Re-Export)", "۲. واردات، صادرات و صادرات مجدد (Re-Export)", "2. Import, Export & Re-Export Operations")
reg("serv_card2_desc", "استيراد المنتجات والسلع إلى سلطنة عمان واستيفاء الموافقات التنظيمية، تصدير المنتجات العمانية إلى الأسواق الإقليمية والدولية، إعادة التصدير من المناطق الحرة العمانية (صحار، صلالة، الدقم)، والتخليص الجمركي وإدارة سلاسل الإمداد المتكاملة عبر نظام بيان.", "تسهیل واردات و اخذ مجوزهای استاندارد، صادرات محصولات تولیدی عمان، ترانزیت و صادرات مجدد از مناطق آزاد با سامانه گمرکی بیان.", "Direct imports into Oman, exporting national goods, bonded re-export transit from Sohar/Salalah/Duqm, and integrated Bayan customs clearing.")

reg("serv_card3_title", "3. توريد وتأمين احتياجات المشاريع (Procurement Services)", "۳. تأمین و تدارکات پروژه‌ها و خطوط تولید (Procurement)", "3. Turnkey Project & Industrial Procurement")
reg("serv_card3_desc", "سورسينج وتوريد المواد الخام للمصانع والمنشآت، توريد الآلات ومعدات الإنتاج وقطع الغيار الصناعية، إدارة سلاسل الإمداد لمشاريع البنية التحتية والمقاولات، والفحص الفني ومطابقة المواصفات قبل الشحن والتسليم.", "سورسینگ مواد اولیه صنعتی، خرید ماشین‌آلات تولید و قطعات یدکی، مدیریت تدارکات پروژه‌های عمرانی و بازرسی کنترل کیفیت قبل از حمل.", "Raw material sourcing, manufacturing machinery, industrial spare parts, EPC supply chain handling, and certified pre-shipment inspection.")

reg("serv_card4_title", "4. الاستشارات المالية والاعتمادات المستندية (Financial & L/C Advisory)", "۴. مشاوره پرداخت و اعتبارات اسنادی (Financial & L/C)", "4. Trade Finance & Documentary Credit Advisory")
reg("serv_card4_desc", "هيكلة وتدقيق الاعتمادات المستندية (Letters of Credit - L/C) لحماية أطراف الصفقة، استشارات الدفع التجاري والضمانات المصرفية (Bank Guarantees)، إدارة مخاطر الصرف والعملات الأجنبية في الصفقات الدولية، والربط مع المؤسسات المالية لتمويل التجارة.", "ساختاردهی اعتبارات اسنادی دیداری و مدت‌دار (L/C)، ضمانت‌نامه‌های بانکی حسن اجرای کار، پوشش ریسک نوسانات ارزی و تعامل با بانک‌های معتبر.", "Structuring documentary letters of credit (L/C), bank performance bonds, currency risk hedging, and financial institutional coordination.")

reg("serv_card5_title", "5. بنية التصنيع وهوية صُنع في عُمان (Contract Manufacturing & Made in Oman)", "۵. زیرساخت تولید و برند ساخت عمان (Made in Oman)", "5. Contract Manufacturing & Made in Oman Value-Add")
reg("serv_card5_desc", "التصنيع التعاقدي للمنتجات عبر مصانع عمانية قائمة (Contract Manufacturing)، إصدار شهادة المنشأ العمانية والاستفادة من اتفاقيات التجارة الحرة، تأسيس خطوط الإنتاج والمصانع في المناطق الحرة والمدن الصناعية (مدائن)، وبرامج القيمة المحلية المضافة (ICV).", "تولید برون‌سپاری‌شده در کارخانجات عمان، اخذ گواهی مبدأ عمان و معافیت گمرکی در بازارهای آمریکا و خلیج فارس و اخذ مشوق‌های صنعتی مدائن.", "Contract manufacturing in established Omani factories, Certificate of Origin issuance, US-Oman FTA zero tariffs, and Madayn industrial incentives.")

reg("page_proc_tag", "الركن الثالث • التوريد الاستراتيجي", "ستون ۳ • تدارکات استراتژیک", "Pillar 3 • Strategic Sourcing")
reg("page_proc_title", "توريد وتأمين احتياجات المشاريع (Procurement Services)", "تأمین و تدارکات جامع پروژه‌ها و کارخانجات", "Turnkey Project Procurement & Industrial Sourcing")
reg("page_proc_sub", "تأمين المواد الخام، الآلات، وخطوط الإنتاج للمشاريع الصناعية والإنشائية والبنية التحتية مع إدارة الفحص والمطابقة والتسليم في الموقع.", "تأمین مواد اولیه، ماشین‌آلات سنگین، خطوط اتوماسیون و تجهیزات مهندسی با بازرسی فنی و تحویل در محل پروژه.", "Securing raw materials, machinery, and production lines for industrial and infrastructure projects with verified site delivery.")

reg("proc_c1_title_old", "سورسينج وتوريد المواد الخام", "سورسینگ و تأمین مواد اولیه صنعتی", "Raw Material Sourcing")
reg("proc_c1_desc_old", "البحث عن أفضل الموردين المعتمدين عالمياً، التفاوض على الأسعار، وتأمين تدفق مستمر للمواد الخام الصناعية بأسعار تنافسية.", "شناسایی معتبرترین تولیدکنندگان بین‌المللی، تثبیت قیمت و تضمین پایداری خطوط تولید کارخانجات با بهترین کیفیت.", "Identifying top certified global suppliers, price negotiation, and continuous raw material delivery at competitive rates.")

reg("proc_c2_title_old", "توريد الآلات ومعدات الإنتاج", "تأمین ماشین‌آلات و خطوط تولید سنگین", "Production Machinery & Industrial Plants")
reg("proc_c2_desc_old", "شراء وشحن خطوط الإنتاج والآلات الثقيلة من المصانع العالمية مع الفحص الفني المسبق وضمان مطابقة المواصفات التعاقدية.", "خرید و واردات دستگاه‌های صنعتی پیشرفته همراه با بازرسی فنی پیش از بارگیری و گواهی انطباق با استاندارد.", "Procurement and shipping of heavy machinery and production lines with verified pre-shipment technical inspection.")

reg("proc_c3_title_old", "إدارة سلاسل الإمداد للمشاريع", "مدیریت جامع زنجیره تأمین پروژه‌ها", "Project Supply Chain Management")
reg("proc_c3_desc_old", "إدارة المشتريات من مرحلة الطلب وحتى التسليم في الموقع (Door-to-Site) مع الجدولة الزمنية وتأمين مخاطر النقل والتوريد.", "هدایت لجستیک پروژه از مرحله استعلام و ثبت سفارش تا تحویل در محل کارگاه با پوشش کامل ریسک‌های حمل.", "End-to-end procurement logistics from RFQ stage to on-site delivery under strict delivery schedules.")

reg("page_fa_tag", "الركن الرابع • الأمان المالي", "ستون ۴ • امنیت مالی", "Pillar 4 • Financial Security")
reg("page_fa_title", "الاستشارات المالية وهندسة الدفع التجاري (Trade Finance & Payment Structuring)", "مشاوره پرداخت و ساختاردهی اعتبارات اسنادی", "Trade Finance & Commercial Payment Engineering")
reg("page_fa_sub", "تأمين المعاملات المالية الدولية عبر الاعتمادات المستندية وحلول الدفع الموثوقة بالتعاون مع بنوك عُمانية ودولية رائدة لحماية كافة الأطراف.", "تضمین امنیت مالی معاملات ارزی از طریق ابزارهای بانکی بین‌المللی و اعتبارات اسنادی معتبر با همکاری بانک‌های پیشرو.", "Securing international transactions through documentary letters of credit and trusted institutional banking mechanisms.")

reg("fa_c1_title_old", "الاعتمادات المستندية (L/C Structuring)", "ساختاردهی اعتبارات اسنادی (L/C)", "L/C Structuring & Governance")
reg("fa_c1_desc_old", "صياغة وتدقيق شروط خطابات الاعتماد المستندي غير القابلة للإلغاء والمعززة لحماية مصالح المشتري والبائع وضمان مطابقة المستندات.", "تنظیم و ممیزی دقیق شروط ال‌سی‌های بانکی غیرقابل برگشت و معزز جهت صیانت کامل از سرمایه طرفین معامله.", "Drafting and auditing terms of irrevocable confirmed letters of credit ensuring flawless document compliance.")

reg("fa_c2_title_old", "ضمانات الدفع والتحصيل المستندي", "ضمانت‌های پرداخت و بروات اسنادی (CAD)", "Payment Guarantees & Document Collections")
reg("fa_c2_desc_old", "هيكلة آليات الدفع الآمنة وفق معايير غرفة التجارة الدولية (UCP 600)، التحصيل المستندي (CAD)، وحلول الضمان المصرفي للمشاريع.", "مهندسی ابزارهای تسویه مالی امن منطبق با مقررات UCP 600 اتاق بازرگانی بین‌المللی و وصول اسناد مشروط.", "Structuring secure payment mechanisms under ICC UCP 600 standards, documentary collections, and bank project guarantees.")

reg("fa_c3_title_old", "إدارة مخاطر الصرف والعملات", "پوشش ریسک نوسانات ارزی در صفقات", "Foreign Exchange Risk Hedging")
reg("fa_c3_desc_old", "استشارات تحوط ضد تقلبات أسعار الصرف، واختيار العملات المناسبة للصفقات (USD, EUR, OMR, AED) لتفادي الخسائر الناتجة عن تذبذب الأسواق.", "تحلیل و انتخاب بهینه سبد ارزی معامله (دلار، یورو، ریال عمان، درهم) جهت خنثی‌سازی تکانه‌های بازار ارز.", "Hedging against exchange rate volatility and selecting optimum currency mixes (USD, EUR, OMR, AED) to protect margins.")

reg("page_mio_tag", "الركن الخامس • القيمة المضافة", "ستون ۵ • ارزش افزوده ملی", "Pillar 5 • Value-Add Advantage")
reg("page_mio_title", "بنية التصنيع وهوية صُنع في عُمان (Contract Manufacturing & Made in Oman)", "زیرساخت تولید قراردادی و جهش صادرات با برند ساخت عمان", "Contract Manufacturing & Made in Oman Hub")
reg("page_mio_sub", "مساعدة المصانع والمستثمرين على تأسيس خطوط الإنتاج، التصنيع التعاقدي، الاستفادة من اتفاقيات التجارة الحرة، وإصدار شهادة المنشأ العمانية.", "همراهی سرمایه‌گذاران و تولیدکنندگان جهت تولید بدون کارخانه، بهره‌برداری از معاهدات تجارت آزاد و اخذ گواهی مبدأ معتبر عمان.", "Empowering manufacturers and global investors with contract production lines, bilateral FTA tariff exemptions, and Omani origin certification.")

reg("mio_c1_title_old", "التصنيع التعاقدي (Contract Manufacturing)", "تولید قراردادی و برون‌سپاری صنعتی", "Contract Manufacturing Services")
reg("mio_c1_desc_old", "ربط الشركات بالمصانع العمانية القائمة لتصنيع وتعبئة منتجاتها تحت علامتها التجارية الخاصة مع ضمان الالتزام بمعايير الجودة العمانية والخليجية.", "اتصال صاحبان برند به کارخانجات فعال عمان برای فرآوری و بسته‌بندی کالا با برند اختصاصی با رعایت کامل استانداردهای منطقه‌ای.", "Partnering enterprises with certified Omani plants for toll manufacturing, private labeling, and GCC quality compliance.")

reg("mio_c2_title_old", "شهادة المنشأ العمانية المعتمدة", "گواهی مبدأ عمان و ارزش افزوده داخلی (ICV)", "Accredited Omani Certificate of Origin")
reg("mio_c2_desc_old", "المساعدة في استيفاء شروط القيمة المضافة الوطنية (In-Country Value) للحصول على شهادة المنشأ العمانية ودخول الأسواق الخليجية بدون رسوم جمركية.", "تطبیق فرمول‌های ارزش افزوده محلی جهت دریافت رسمی گواهی مبدأ اتاق بازرگانی عمان و ورود بدون تعرفه به بازارهای خلیج فارس.", "Guiding producers through In-Country Value calculations to secure authentic Omani Certificates of Origin for tariff-free GCC distribution.")

reg("mio_c3_title_old", "الاستفادة من اتفاقيات التجارة الحرة (FTA)", "مزیت‌های معاهده تجارت آزاد با آمریکا (FTA)", "Leveraging Bilateral Free Trade Agreements")
reg("mio_c3_desc_old", "استغلال اتفاقية التجارة الحرة بين سلطنة عُمان والولايات المتحدة الأمريكية، واتفاقيات دول مجلس التعاون، لتصدير المنتجات بإعفاءات جمركية كاملة.", "صادرات بدون سهمیه و با تعرفه صفر درصد به بازار ایالات متحده آمریکا و سایر بازارهای طرف معاهدات تجاری عمان.", "Capitalizing on the landmark US-Oman Free Trade Agreement and regional treaties for 100% duty-free export access.")

reg("page_req_tag", "بوابة الطلبات الرسمية", "درگاه رسمی ثبت استعلام", "Official RFQ Portal")
reg("page_req_title", "طلب استشارة تجارية أو دراسة صفقة دولية", "ثبت درخواست مشاوره تجاری یا ارزیابی معامله بین‌المللی", "Trade Consultation & Transaction Assessment Request")
reg("page_req_sub", "يرجى ملء النموذج أدناه بدقة لمساعدة فريقنا التجاري والقانوني في تقييم متطلباتك وتقديم المقترح الأنسب خلال 24 ساعة عمل.", "لطفاً فرم زیر را تکمیل نمایید تا کارشناسان تکامل پس از بررسی مدارک ظرف حداکثر ۲۴ ساعت کاری با شما تماس بگیرند.", "Please complete the form below to enable our commercial and legal desks to evaluate your requirements within 24 business hours.")

reg("req_service_select", "الخدمة المطلوبة", "نوع خدمت موردنظر", "Required Service")
reg("req_opt_0", "-- اختر الخدمة --", "-- انتخاب خدمت بازرگانی --", "-- Select Service --")

with open(os.path.join(BASE_DIR, 'translations.json'), 'w', encoding='utf-8') as f:
    json.dump(t, f, ensure_ascii=False, indent=2)

with open(os.path.join(BASE_DIR, 'js', 'translations_data.js'), 'w', encoding='utf-8') as f:
    f.write(f"window.ALT_TRANSLATIONS = {json.dumps(t, ensure_ascii=False)};")

print("Registered all 65 keys successfully!")
