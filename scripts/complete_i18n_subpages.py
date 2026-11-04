import json, os, re

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'

with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
    t = json.load(f)

# Master dictionary of all subpages untranslated keys
data_keys = {
    "ar": {
        # Navigation & Mobile Drawer
        "nav_all_services": "جميع الخدمات والحلول",
        "mobile_sub_services": "دليل الخدمات التخصصية",
        "mobile_sub_hubs": "الموانئ والمناطق الحرة",
        "btn_explore_pillar": "استعراض الركن",
        "btn_whatsapp_cta": "تواصل عبر واتساب",
        "btn_whatsapp_instant": "تواصل فوري عبر واتساب",
        "btn_rfq_submit": "إرسال استدراج عروض (RFQ)",
        "btn_consult_logistics": "استشر فريق العمليات اللوجستية",
        "btn_start_localization": "بدء دراسة توطين منتج في عُمان",
        "btn_advisory_request": "طلب استشارة ائتمانية وتجارية",

        # 404 & Thank you
        "err_404_title": "الصفحة غير موجودة",
        "err_404_desc": "عذراً، الرابط الذي تحاول الوصول إليه غير متاح أو تم نقله. يمكنك العودة إلى الصفحة الرئيسية أو التواصل معنا مباشرة.",
        "thank_you_title": "تم استلام طلبكم التجاري بنجاح",
        "thank_you_desc": "شكراً لتواصلكم مع شركة تكامل للتجارة الدولية ش.م.م. تم توجيه طلبكم إلى القسم التجاري المختص وسيتواصل معكم مستشارنا خلال ۲۴ ساعة عمل.",

        # About Page Content
        "ab_vision_desc": "أن نكون بيت التجارة واللوجستيات المفضل والأكثر موثوقية في سلطنة عُمان والمنطقة، من خلال بناء تحالفات تجارية مستدامة وتمكين هوية المنتج الوطني.",
        "ab_mission_title": "رسالتنا التشغيلية",
        "ab_mission_desc": "تقديم حلول متكاملة في التوريد، التصدير، الاستيراد، وتوطين خطوط التجميع بأعلى معايير الشفافية والحوكمة وضمان حقوق الأطراف المتعاقدة.",
        "ab_values_title": "قيمنا الجوهرية",
        "ab_values_desc": "الأمانة والسرية التجارية التامة (NDA)، الامتثال التنظيمي والتشريعي الكامل، الكفاءة في إدارة التكاليف، والسرعة في إنجاز العمليات الميدانية.",
        "ab_official_info_title": "المعلومات والبيانات الرسمية للشركة",
        "lbl_legal_name": "الاسم القانوني بالعربية:",
        "val_legal_name": "شركة تكامل للتجارة الدولية ش.م.م",
        "lbl_cr_number": "رقم السجل التجاري (CR):",
        "lbl_headquarters": "المقر الرئيسي:",
        "val_headquarters": "مسقط - واحة المعرفة (KOM)",
        "lbl_phone_wa": "الهاتف المباشر والواتساب:",
        "lbl_official_email": "البريد الإلكتروني المعتمد:",

        # Contact Page Content
        "ct_phone_title": "الاتصال الهاتفي وواتساب",
        "ct_phone_desc": "خط العمل المباشر والمحادثات التجارية السريعة.",
        "ct_email_title": "البريد الإلكتروني المعتمد",
        "ct_email_desc": "لإرسال استدراج العروض (RFQ) والعقود والمستندات.",
        "ct_hq_title": "المقر الرئيسي بمسقط",
        "ct_hq_desc": "واحة المعرفة مسقط (KOM)، مجمع الأعمال، سلطنة عُمان.",
        "ct_form_title": "إرسال رسالة مباشرة لفريق العمل",

        # Services Matrix Page Content
        "srv_card1_title": "١. التجارة الدولية وبيت التجارة (International Trading House)",
        "srv_card1_desc": "إبرام الصفقات، الوساطة، الوكالات التجارية، والتمثيل الحصري للعلامات التجارية العالمية في الأسواق الإقليمية.",
        "srv_card2_title": "٢. الاستيراد والتصدير وإعادة التصدير (Import, Export & Re-Export)",
        "srv_card2_desc": "شحنات الترانزيت، المناولة في الموانئ والمناطق الحرة بصحار وصلالة والدقم، وتنسيق العمليات اللوجستية.",
        "srv_card3_title": "٣. توريد وتأمين احتياجات المشاريع (Project Procurement)",
        "srv_card3_desc": "تأمين الآلات الصناعية، المعدات الثقيلة، المواد الخام، وقطع الغيار للمشاريع التنموية والإنشائية.",
        "srv_card4_title": "٤. الاستشارات المالية والاعتمادات (Trade & Financial Advisory)",
        "srv_card4_desc": "هيكلة صيغ الدفع، فحص الجدارة والائتمان التجاري، صيغ خطابات الضمان والاعتمادات المستندية (L/C).",
        "srv_card5_title": "٥. بنية التصنيع وهوية «صُنع في عُمان» (Made in Oman Infrastructure)",
        "srv_card5_desc": "التصنيع التعاقدي، خطوط التجميع، تحقيق القيمة المحلية المضافة (ICV)، والتصدير بدون جمارك عبر اتفاقيات FTA.",

        # FAQ Page Content
        "faq_q1": "ما هي المزايا الاستراتيجية للتجارة عبر سلطنة عُمان؟",
        "faq_a1": "تتمتع سلطنة عُمان بموقع استراتيجي خارج مضيق هرمز مفتوح على المحيط الهندي، وترتبط باتفاقيات تجارة حرة (FTA) مع الولايات المتحدة وسنغافورة ودول EFTA، بالإضافة إلى منظومة موانئ ومناطق حرة حديثة بإعفاءات ضريبية وجمركية تصل إلى 100%.",
        "faq_q2": "كيف تدعم شركة تكامل مشاريع وسم «صُنع في عُمان»؟",
        "faq_a2": "نساعد الشركات في تقييم الجدوى الصناعية، التعاقد مع مصانع وورش معتمدة في عُمان (التصنيع التعاقدي)، استيراد المواد الخام والآلات، وتحقيق نسب القيمة المحلية المضافة (ICV) المطلوبة للحصول على الهوية الوطنية العمانية.",
        "faq_q3": "هل تقدم شركة تكامل تمويلاً مباشراً أو قروضاً؟",
        "faq_a3": "لا. شركة تكامل ليست مؤسسة مصرفية أو مانحة للقروض؛ نحن نقدم استشارات تجارية ومالية متخصصة لهيكلة شروط الدفع، فحص الجدارة الائتمانية للأطراف، صياغة شروط الاعتمادات المستندية (L/C) والتنسيق مع المؤسسات المالية المرخصة.",
        "faq_q4": "ما هي شروط الإنكوترمز التي تديرونها في صفقات التوريد؟",
        "faq_a4": "ندير كافة شروط التسليم الدولية بما في ذلك EXW, FOB, CFR, CIF, DAP و DDP بحسب الاتفاق التجاري وطبيعة المنشأ والوجهة النهائية.",
        "faq_q5": "هل تشترطون نوعاً محدداً من البضائع أو المنتجات؟",
        "faq_a5": "نطاق عملنا كبيت تجارة دولية يغطي معظم السلع التجارية والصناعية؛ مع الالتزام التام بالقوانين العمانية والحصول على الموافقات الخاصة بالسلع المقيدة مثل الأغذية والأدوية والمواد الكيميائية.",
        "faq_q6": "كيف تضمنون سرية معلومات الشركاء والموردين؟",
        "faq_a6": "نوقع اتفاقيات سرية معلومات ملزمة قانوناً (Non-Disclosure Agreements - NDA) قبل بدء تبادل البيانات التسعيرية أو قوائم الموردين والعملاء.",

        # Financial Advisory Page Content
        "fa_compliance_notice_lbl": "إشعار الحوكمة والامتثال المصرفي:",
        "fa_compliance_notice_desc": "شركة تكامل للتجارة الدولية ش.م.م بيت تجارة دولية واستشارات تعاقدية وليست مؤسسة مصرفية أو مانحة للقروض أو صرافة. تنحصر خدماتنا في تقديم الاستشارات الفنية وهيكلة شروط الدفع التجاري والاعتمادات المستندية والتنسيق مع البنوك المعتمدة.",
        "fa_sub1_title": "هيكلة الدفع والاعتمادات المستندية",
        "fa_sub1_desc": "المشورة الفنية في إعداد شروط L/C المعززة، خطابات الضمان المصرفية (Bank Guarantees / Performance Bonds) وشروط الدفع مقابل المستندات (CAD/DP).",
        "fa_sub2_title": "فحص الجدارة والملاءة الائتمانية",
        "fa_sub2_desc": "تقييم الوضع المالي وسجل المعاملات للموردين والمشترين الجدد قبل إبرام الصفقات لتجنب حالات التخلف عن السداد أو النزاعات التجارية.",
        "fa_sub3_title": "تحليل تكاليف الاستيراد ورأس المال",
        "fa_sub3_desc": "حساب دقيق لـ Landed Cost متضمناً الرسوم الجمركية، نولون الشحن، التأمين البحري، ونفقات التمويل ورأس المال العامل المطلوب لتنفيذ الصفقة.",

        # Import Export Page Content
        "ie_sub1_title": "الاستيراد المباشر للسلطنة",
        "ie_sub1_desc": "استيراد السلع والمواد لحساب الشركات والمشاريع في عمان، استيفاء الموافقات التنظيمية، وإدارة المستندات الملاحية والفحص النوعي للبضائع.",
        "ie_sub2_title": "التصدير وإعادة التصدير",
        "ie_sub2_desc": "إعادة تصدير الشحنات إلى دول الخليج، أفريقيا، والهند مع الاستفادة من الإعفاءات الجمركية المتاحة بالمناطق الحرة بصحار وصلالة والدقم.",
        "ie_sub3_title": "إدارة المستندات الجمركية",
        "ie_sub3_desc": "إصدار وتصديق شهادات المنشأ (COO)، الفواتير التجارية المعتمدة، بوالص الشحن (B/L)، وقوائم التعبئة المتوافقة مع متطلبات الجمارك.",
        "ie_sub4_title": "الامتثال التنظيمي للسلع المقيدة والخاصة",
        "ie_sub4_desc": "نلتزم بأعلى معايير الحوكمة؛ بالنسبة للسلع التي تتطلب تصاريح متخصصة (مثل الأغذية، الأدوية، الكيماويات والمعدات الطبية)، نقوم بالتنسيق مع الجهات الحكومية والرقابية العمانية لضمان الفسح النظامي دون تأخير.",

        # Made in Oman Page Content
        "mo_sub1_title": "التصنيع التعاقدي (Contract Mfg)",
        "mo_sub1_desc": "الربط مع مصانع وورش معتمدة في سلطنة عمان لتصنيع وتجميع منتجاتكم مع الحفاظ الكامل على ملكية علامتكم التجارية وتركيبتكم السرية.",
        "mo_sub2_title": "خطوط التجميع والتعبئة النهائية",
        "mo_sub2_desc": "استيراد المكونات والمواد النصف مصنعة وإجراء التجميع والاختبار والتعبئة داخل عمان لتحقيق معايير المنشأ الوطني العماني.",
        "mo_sub3_title": "ملف ترخيص هوية المنتج الوطني",
        "mo_sub3_desc": "إعداد ملف الحسابات والوثائق الخاصة بنسبة القيمة المحلية المضافة (ICV) وتقديمها للجهات المعنية لنيل حق استخدام شعار «صُنع في عُمان».",
        "mo_sub4_title": "المزايا التصديرية لشعار صُنع في عُمان",
        "mo_sub4_desc": "المنتج الحاصل على شهادة المنشأ العمانية المعتمدة يستفيد مباشرة من مزايا استراتيجية كبرى:",
        "mo_feat_gcc": "• دخول بدون رسوم جمركية لكافة دول مجلس التعاون (GCC)",
        "mo_feat_fta": "• معافاة جمركية تامة للسوق الأمريكي عبر اتفاقية (US-Oman FTA)",
        "mo_feat_tender": "• أفضلية إلزامية بنسبة 10% في المشتريات والمناقصات الحكومية العمانية",
        "mo_feat_arab": "• نفاذ تفضيلي للدول العربية عبر اتفاقية تيسير وتنمية التبادل التجاري",

        # Privacy Page Content
        "priv_s1_title": "١. جمع المعلومات واستخدامها",
        "priv_s1_desc": "نجمع فقط البيانات الضرورية لتنفيذ الإجراءات التجارية والاتصال بكم، مثل الاسم، البريد الإلكتروني، رقم الهاتف، والمواصفات الفنية للسلع المطلوبة. لا نقوم ببيع أو تأجير هذه البيانات لأي طرف ثالث نهائياً.",
        "priv_s2_title": "٢. اتفاقيات عدم الإفصاح والسرية (NDA)",
        "priv_s2_desc": "تعتبر كافة التفاصيل المالية وهوامش الأسعار وقوائم المصنعين والمشترين معلومات سرية ومحمية قانوناً بموجب اتفاقيات السرية المبرمة، ولا يتم الإفصاح عنها إلا للجهات الحكومية والرقابية بموجب أمر قضائي ملزم.",
        "priv_s3_title": "٣. أمن البيانات",
        "priv_s3_desc": "نطبق معايير أمنية وإلكترونية متطورة لحماية سجلات المعاملات والاتصالات التجارية من أي وصول غير مصرح به أو تلف.",

        # Procurement Page Content
        "pr_sub1_title": "المعدات الثقيلة وخطوط الإنتاج",
        "pr_sub1_desc": "تأمين الآلات الصناعية، المعدات الميكانيكية والكهربائية المتطورة، قطع الغيار الاستراتيجية ومولدات الطاقة للمشاريع التنموية.",
        "pr_sub2_title": "المواد الخام والسلع الوسيطة",
        "pr_sub2_desc": "توريد مستلزمات الصناعة من معادن، بوليمرات، مواد كيميائية وسلع أساسية من كبار المنتجين بأسعار تنافسية ومواصفات معتمدة.",
        "pr_sub3_title": "تجهيزات الضيافة والمجمعات",
        "pr_sub3_desc": "تأمين متطلبات الفنادق الكبرى، المجمعات التجارية، والأبراج السكنية من مواد تشطيب وأثاث ومعدات إدارة المرافق.",
        "pr_sub4_title": "نماذج التعاقد المتاحة للشركات والمطورين",
        "pr_model1_title": "١. الشراء والبيع المباشر (Direct Trading)",
        "pr_model1_desc": "تقوم شركة تكامل بشراء المعدات والمواد لحسابها الخاص ثم إعادة بيعها للمشروع بفاتورة تجارية محلية موحدة مع تحمل مسؤولية التوريد والضمانات الفنية المتفق عليها.",
        "pr_model2_title": "٢. التوريد بالوكالة والعمولة (Agency Procurement)",
        "pr_model2_desc": "نقوم بتمثيل العميل والتفاوض نيابة عنه وإدارة المناقصات واستدراج عروض الأسعار الدولية مقابل نسبة عمولة محددة بشفافية تامة في الفواتير الأصلية.",

        # Terms Page Content
        "term_s1_title": "١. نطاق الأنشطة والصفة القانونية",
        "term_s1_desc": "شركة تكامل للتجارة الدولية ش.م.م شركة مسجلة رسمياً بسلطنة عمان بموجب السجل التجاري رقم CR 1389420. تعمل الشركة في مجالات الاستيراد والتصدير، التوريد للمشاريع، الوساطة التجارية، والاستشارات المالية والتجارية وفق التراخيص الصادرة من وزارة التجارة والصناعة وترويج الاستثمار.",
        "term_s2_title": "٢. الشروط المالية والاعتمادات المستندية",
        "term_s2_desc": "تؤكد الشركة أنها ليست مصرفاً أو مؤسسة إقراض مالي. جميع استشارات الدفع والاعتمادات تخضع لقواعد غرفة التجارة الدولية (UCP 600) والأنظمة المصرفية المعتمدة لدى البنك المركزي العُماني.",
        "term_s3_title": "٣. شروط الشحن والإنكوترمز (Incoterms 2020)",
        "term_s3_desc": "تحدد التزامات البائع والمشتري ونقاط انتقال المخاطر والتأمين ونفقات الشحن بدقة في العقود المستقلة الموقعة لكل معاملة تجارية استناداً إلى أحدث إصدارات قواعد غرفة التجارة الدولية.",
        "term_s4_title": "٤. القانون الواجب التطبيق والاختصاص القضائي",
        "term_s4_desc": "تخضع كافة التعاملات والعقود التجارية والاتفاقيات للقوانين والأنظمة المعمول بها في سلطنة عُمان، وتختص المحاكم العمانية بالنظر في أي نزاع ينشأ عنها ما لم يتفق الطرفان كتابة على التحكيم التجاري.",

        # Request Form Select Options
        "opt_srv_it": "التجارة الدولية وبيت التجارة (International Trade)",
        "opt_srv_ie": "الاستيراد والتصدير وإعادة التصدير (Import/Export)",
        "opt_srv_pr": "توريد احتياجات المشاريع (Procurement)",
        "opt_srv_fa": "الاستشارات المالية والاعتمادات (Trade Advisory)",
        "opt_srv_mo": "بنية وهوية صُنع في عُمان (Made in Oman)",
        "opt_budget_1": "أقل من 50,000 دولار",
        "opt_budget_2": "50,000 - 250,000 دولار",
        "opt_budget_3": "250,000 - 1,000,000 دولار",
        "opt_budget_4": "أكثر من 1,000,000 دولار"
    },
    "fa": {
        # Navigation & Mobile Drawer
        "nav_all_services": "مشاهده کلیه خدمات و راهکارها",
        "mobile_sub_services": "فهرست خدمات تخصصی",
        "mobile_sub_hubs": "بنادر و مناطق آزاد",
        "btn_explore_pillar": "بررسی جزئیات رکن",
        "btn_whatsapp_cta": "ارتباط در واتساپ",
        "btn_whatsapp_instant": "ارتباط فوری در واتساپ",
        "btn_rfq_submit": "ارسال استعلام بها (RFQ)",
        "btn_consult_logistics": "مشاوره با تیم عملیات لجستیک",
        "btn_start_localization": "بررسی تولید محصول در عمان",
        "btn_advisory_request": "درخواست مشاوره اعتباری و تجاری",

        # 404 & Thank you
        "err_404_title": "صفحه یافت نشد",
        "err_404_desc": "متأسفانه صفحه‌ای که به دنبال آن بودید یافت نشد یا منتقل شده است. می‌توانید به صفحه اصلی بازگردید یا با کارشناسان ما تماس بگیرید.",
        "thank_you_title": "درخواست تجاری شما با موفقیت ثبت شد",
        "thank_you_desc": "از تماس شما با شرکت بازرگانی بین‌المللی تکامل سپاسگزاریم. درخواست شما به واحد تخصصی ارجاع شد و کارشناس بازرگانی ظرف ۲۴ ساعت کاری با شما تماس خواهد گرفت.",

        # About Page Content
        "ab_vision_desc": "تبدیل شدن به معتمدترین و پیشروترین خانه بازرگانی و لجستیک در سلطنت عمان و خاورمیانه، از طریق خلق ائتلاف‌های استراتژیک تجاری و توانمندسازی برندهای ملی.",
        "ab_mission_title": "مأموریت عملیاتی ما",
        "ab_mission_desc": "ارائه راهکارهای یکپارچه در تأمین صنعتی، صادرات، واردات، و راه‌اندازی خطوط تولید در عمان با بالاترین سطوح انضباط حقوقی و صیانت از منافع طرفین.",
        "ab_values_title": "ارزش‌های محوری",
        "ab_values_desc": "امانت‌داری و حفظ کامل محرمانگی اسرار تجاری (NDA)، پایبندی به الزامات قانونی، شفافیت در بهینه‌سازی هزینه‌ها و چابکی در اجرای میدانی فرایندها.",
        "ab_official_info_title": "مشخصات و اطلاعات هویتی شرکت",
        "lbl_legal_name": "نام قانونی ثبتی:",
        "val_legal_name": "شركة تكامل للتجارة الدولية ش.م.م",
        "lbl_cr_number": "شماره ثبت تجاری عمان (CR):",
        "lbl_headquarters": "دفتر مرکزی:",
        "val_headquarters": "مسقط - واحه المعرفه (KOM)، مجتمع کسب‌وکار",
        "lbl_phone_wa": "تلفن مستقیم و واتساپ:",
        "lbl_official_email": "ایمیل رسمی و مکاتبات:",

        # Contact Page Content
        "ct_phone_title": "ارتباط تلفنی و پشتیبانی واتساپ",
        "ct_phone_desc": "خط ارتباطی مستقیم جهت گفتگوهای بازرگانی فوری و مشاوره سریع.",
        "ct_email_title": "پست الکترونیک رسمی",
        "ct_email_desc": "جهت ارسال اسناد تجاری، استعلام قیمت (RFQ) و پیش‌نویس قراردادها.",
        "ct_hq_title": "دفتر مرکزی در مسقط",
        "ct_hq_desc": "واحه المعرفه مسقط (KOM)، مجتمع کسب‌وکار، سلطنت عمان.",
        "ct_form_title": "ارسال پیام مستقیم به کارشناسان بازرگانی",

        # Services Matrix Page Content
        "srv_card1_title": "۱. بازرگانی بین‌الملل و خانه تجارت (International Trading House)",
        "srv_card1_desc": "انعقاد معاملات فرامرزی، وساطت تجاری، اخذ نمایندگی رسمی و عاملیت فروش برندهای بین‌المللی در بازارهای منطقه‌ای.",
        "srv_card2_title": "۲. واردات، صادرات و ترانزیت مجدد (Import, Export & Re-Export)",
        "srv_card2_desc": "حمل دریایی و هوایی، عملیات انبارداری باندی در بنادر صحار، صلاله و دقم، و مدیریت حرفه‌ای ترخیص گمرکی.",
        "srv_card3_title": "۳. تأمین و تدارکات تجهیزات پروژه‌ای (Project Procurement)",
        "srv_card3_desc": "تأمین ماشین‌آلات صنعتی، خطوط تولید سنگین، مواد اولیه کارخانجات و اقلام یدکی پروژه‌های عمرانی و زیرساختی.",
        "srv_card4_title": "۴. راهکارهای اعتباری و پرداخت (Trade & Financial Advisory)",
        "srv_card4_desc": "مشاوره تخصصی در تدوین اعتبارات اسنادی (L/C)، ضمانت‌نامه‌های بانکی، اعتبارسنجی خریداران خارجی و پوشش ریسک‌های مالی.",
        "srv_card5_title": "۵. زیرساخت تولید و نشان «ساخت عمان» (Made in Oman Infrastructure)",
        "srv_card5_desc": "تولید قراردادی، خطوط مونتاژ نهایی، تحقق شاخص ارزش بومی (ICV) و صادرات با تعرفه صفر به آمریکا از طریق FTA عمان.",

        # FAQ Page Content
        "faq_q1": "مزیت‌های استراتژیک تجارت و ترانزیت از طریق سلطنت عمان چیست؟",
        "faq_a1": "عمان خارج از تنگه هرمز و مشرف به آب‌های آزاد اقیانوس هند واقع شده و پیمان تجارت آزاد (FTA) با آمریکا و کشورهای EFTA دارد. بنادر پیشرفته و مناطق آزاد آن معافیت مالیاتی و گمرکی ۱۰۰٪ ارائه می‌دهند.",
        "faq_q2": "هلدینگ تکامل چگونه از پروژه «ساخت عمان» حمایت می‌کند؟",
        "faq_a2": "ما سرمایه‌گذاران را در ارزیابی توجیه اقتصادی، تولید قراردادی در کارخانجات معتبر عمان، واردات مواد اولیه و کسب شاخص ارزش افزوده (ICV) برای دریافت نشان ملی ساخت عمان همراهی می‌کنیم.",
        "faq_q3": "آیا شرکت تکامل وام یا تسهیلات مالی مستقیم ارائه می‌دهد؟",
        "faq_a3": "خیر. شرکت تکامل یک نهاد بانکی نیست؛ خدمات ما صرفاً مشاوره تخصصی در ساختاردهی روش‌های پرداخت، اعتبارسنجی طرفین، تدوین شرایط اعتبارات اسنادی (L/C) و هماهنگی با بانک‌های مجاز است.",
        "faq_q4": "چه قواعدی از اینکوترمز در قراردادهای بازرگانی اجرا می‌شود؟",
        "faq_a4": "ما تمامی ترم‌های استاندارد Incoterms 2020 از جمله EXW, FOB, CFR, CIF, DAP و DDP را بر اساس توافق طرفین و مدل بهینه لجستیک مدیریت می‌کنیم.",
        "faq_q5": "آیا محدودیت کالایی در خدمات بازرگانی وجود دارد؟",
        "faq_a5": "دامنه فعالیت ما کلیه کالاهای مجاز تجاری و صنعتی را در بر می‌گیرد؛ برای اقلام خاص نظیر دارو و مواد غذایی نیز تمامی مجوزهای وزارتخانه‌ها و گمرک عمان به شکل رسمی اخذ می‌گردد.",
        "faq_q6": "محرمانگی اطلاعات شرکا و تأمین‌کنندگان چگونه تضمین می‌شود؟",
        "faq_a6": "پیش از تبادل هرگونه اطلاعات فنی، لیست مشتریان یا قیمت‌گذاری، قرارداد رسمی عدم افشای اطلاعات (NDA) با ضمانت حقوقی معتبر منعقد می‌گردد.",

        # Financial Advisory Page Content
        "fa_compliance_notice_lbl": "اطلاعیه شفافیت و انطباق بانکی:",
        "fa_compliance_notice_desc": "شرکت بازرگانی بین‌المللی تکامل یک خانه تجارت و مشاوره بازرگانی است و بانک، مؤسسه مالی یا صرافی محسوب نمی‌شود. کلیه خدمات ما در چارچوب مشاوره مهندسی ابزارهای پرداخت تجاری، بررسی شرایط L/C و هماهنگی با شبکه بانکی مجاز عمان ارائه می‌شود.",
        "fa_sub1_title": "ساختاردهی پرداخت و اعتبارات اسنادی",
        "fa_sub1_desc": "مشاوره تخصصی در گشایش L/C تأییدشده، ضمانت‌نامه‌های حسن انجام تعهدات و پیش‌پرداخت (Bank Guarantees)، و پرداخت در برابر اسناد (CAD).",
        "fa_sub2_title": "اعتبارسنجی و بررسی اهلیت تجاری",
        "fa_sub2_desc": "تحلیل ریسک اعتباری و سوابق تجاری خریداران و فروشندگان خارجی پیش از انعقاد قرارداد، جهت پیشگیری از عدم تعهد و مناقشات مالی.",
        "fa_sub3_title": "تحلیل هزینه نهایی کالا (Landed Cost)",
        "fa_sub3_desc": "محاسبه دقیق بهای تمام‌شده کالا در مقصد شامل حقوق گمرکی، کرایه حمل بین‌المللی، بیمه باربری و هزینه‌های خواب سرمایه برای هر معامله.",

        # Import Export Page Content
        "ie_sub1_title": "واردات مستقیم به سلطنت عمان",
        "ie_sub1_desc": "واردات تخصصی مواد اولیه و تجهیزات، ثبت در سامانه گمرکی بیان، اخذ مجوزهای استاندارد و بازرسی کیفی پیش از ترخیص نهایی.",
        "ie_sub2_title": "صادرات و صادرات مجدد فرامرزی",
        "ie_sub2_desc": "صادرات مجدد کالا به مقاصد حوزه خلیج فارس، شرق آفریقا و شبه‌قاره هند با بهره‌گیری از مزایای انبارداری باندی در بنادر صحار، صلاله و دقم.",
        "ie_sub3_title": "مدیریت اسناد و تشریفات گمرکی",
        "ie_sub3_desc": "صدور و تأیید گواهی مبدأ (COO)، فاکتورهای تجاری رسمی، بارنامه‌های معتبر کشتیرانی (B/L) و لیست‌های عدلبندی منطبق بر استانداردهای گمرک.",
        "ie_sub4_title": "انطباق قانونی کالاهای دارای مقررات خاص",
        "ie_sub4_desc": "برای اقلام نیازمند استعلامات فنی (مواد غذایی، دارویی و شیمیایی)، هماهنگی جامع با وزارت صنعت، تجارت و گمرک عمان جهت ترخیص قانونمند به عمل می‌آید.",

        # Made in Oman Page Content
        "mo_sub1_title": "تولید تحت قرارداد (Contract Manufacturing)",
        "mo_sub1_desc": "پیوند با کارخانجات مجهز و دارای پروانه در عمان جهت تولید و بسته‌بندی محصولات شما با حفظ ۱۰۰٪ مالکیت فرمول و برند تجاری‌تان.",
        "mo_sub2_title": "راه‌اندازی خطوط مونتاژ و بسته‌بندی نهایی",
        "mo_sub2_desc": "واردات قطعات و مواد نیمه‌ساخته به مناطق صنعتی عمان و انجام مراحل تکمیلی جهت احراز ضوابط ساخت ملی و اخذ گواهی مبدأ عمان.",
        "mo_sub3_title": "پرونده فنی و نشان ملی «صُنع في عُمان»",
        "mo_sub3_desc": "محاسبه و تدوین گزارش رسمی ارزش افزوده داخلی (ICV) و ارائه به مراجع ذی‌صلاح جهت دریافت مجوز رسمی استفاده از نشان ساخت عمان.",
        "mo_sub4_title": "مزایای رقابتی نشان ساخت عمان در بازارهای صادراتی",
        "mo_sub4_desc": "محصولاتی که موفق به اخذ گواهی رسمی ساخت عمان می‌شوند از امتیازات تجاری زیر برخوردار می‌گردند:",
        "mo_feat_gcc": "• ورود به کلیه ۶ کشور شورای همکاری خلیج فارس (GCC) بدون پرداخت عوارض گمرکی",
        "mo_feat_fta": "• معافیت ۱۰۰٪ از تعرفه واردات به خاک ایالات متحده آمریکا بر پایه پیمان US-Oman FTA",
        "mo_feat_tender": "• اولویت قطعی ۱۰ درصدی در مناقصات دولتی و پروژه‌های زیرساختی سلطنت عمان",
        "mo_feat_arab": "• دسترسی ترجیحی به بازارهای عربی تحت پیمان توسعه مبادلات تجاری GAFTA",

        # Privacy Page Content
        "priv_s1_title": "۱. جمع‌آوری و بهره‌برداری از اطلاعات",
        "priv_s1_desc": "ما صرفاً اطلاعات ضروری برای پیگیری معاملات بازرگانی نظیر مشخصات فردی، ایمیل و نیازمندی‌های کالایی را دریافت می‌کنیم و اطلاعات شما هرگز در اختیار شخص ثالث قرار نمی‌گیرد.",
        "priv_s2_title": "۲. قراردادهای محرمانگی و عدم افشا (NDA)",
        "priv_s2_desc": "تمامی جزئیات مالی، نرخ‌های کارخانجات و اسامی طرف‌های معامله مشمول حفاظت اکید قانونی بوده و صرفاً با رضایت کتبی طرفین قابلیت تبادل دارند.",
        "priv_s3_title": "۳. امنیت فنی و حفظ داده‌ها",
        "priv_s3_desc": "اطلاعات تجاری شرکا تحت استانداردهای رمزنگاری روز و پروتکل‌های امن ذخیره‌سازی نگهداری می‌شوند.",

        # Procurement Page Content
        "pr_sub1_title": "تجهیزات صنعتی و خطوط تولید سنگین",
        "pr_sub1_desc": "تأمین ماشین‌آلات مکانیکی، برقی، ژنراتورهای صنعتی و قطعات یدکی استراتژیک برای کارخانجات و پروژه‌های توسعه‌ای منطقه.",
        "pr_sub2_title": "مواد اولیه و کالاهای واسطه‌ای صنعتی",
        "pr_sub2_desc": "خرید و حمل مستقیم فلزات، پلیمرها، مواد پتروشیمی و نهاده‌های معدنی از تولیدکنندگان تراز اول جهان با استانداردهای کیفی تضمین‌شده.",
        "pr_sub3_title": "تجهیز پروژه‌های هتلداری و مجتمع‌های تجاری",
        "pr_sub3_desc": "تأمین جامع ملزومات پروژه‌های عمرانی، هتل‌های ۵ ستاره و مجتمع‌های تجاری شامل متریال لوکس، مبلمان تخصصی و سامانه‌های ساختمانی.",
        "pr_sub4_title": "مدل‌های قراردادی همکاری با شرکت‌ها و پیمانکاران",
        "pr_model1_title": "۱. خرید و فروش مستقیم (Direct Trading)",
        "pr_model1_desc": "شرکت تکامل اقلام را با سرمایه خود خریداری کرده و با صدور فاکتور رسمی معتبر و ضمانت انطباق کالا به خریدار تحویل می‌دهد.",
        "pr_model2_title": "۲. کارگزاری خرید و حق‌العمل‌کاری (Agency Procurement)",
        "pr_model2_desc": "ما به نمایندگی از شما وارد مذاکرات بین‌المللی شده و بهترین قیمت‌های جهانی را در ازای کارمزد شفاف و فاکتورهای رسمی دست اول محقق می‌کنیم.",

        # Terms Page Content
        "term_s1_title": "۱. هویت قانونی و چارچوب فعالیت",
        "term_s1_desc": "شرکت بازرگانی بین‌المللی تکامل با شماره ثبت تجاری CR 1389420 در سلطنت عمان تأسیس شده و در چارچوب اساسنامه رسمی و مجوزهای وزارت تجارت، صنعت و ترویج سرمایه‌گذاری عمان فعالیت می‌نماید.",
        "term_s2_title": "۲. الزامات مالی و اعتبارات اسنادی",
        "term_s2_desc": "تکامل یک شرکت بازرگانی است و کلیه مشاوره‌های مالی منطبق با مقررات متحدالشکل اعتبارات اسنادی اتاق بازرگانی بین‌المللی (UCP 600) و ضوابط بانک مرکزی عمان ارائه می‌گردد.",
        "term_s3_title": "۳. قواعد بین‌المللی اینکوترمز (Incoterms 2020)",
        "term_s3_desc": "تعهدات حمل، انتقال ریسک و مسئولیت‌های بیمه‌ای در هر معامله به طور صریح بر پایه جدیدترین نگارش اتاق بازرگانی بین‌المللی در قراردادهای دوجانبه درج می‌گردد.",
        "term_s4_title": "۴. قانون حاکم و مرجع حل اختلاف",
        "term_s4_desc": "تمامی قراردادها و مبادلات تابع قوانین تجاری سلطنت عمان بوده و محاکم قضایی مسقط مرجع نهایی رسیدگی به هرگونه مناقشه حقوقی احتمالی می‌باشند.",

        # Request Form Select Options
        "opt_srv_it": "بازرگانی بین‌الملل و خانه تجارت (International Trade)",
        "opt_srv_ie": "واردات، صادرات و ترانزیت مجدد (Import/Export)",
        "opt_srv_pr": "تأمین و تدارکات پروژه‌ها (Procurement)",
        "opt_srv_fa": "مشاوره پرداخت و اعتبارات اسنادی (Trade Advisory)",
        "opt_srv_mo": "زیرساخت تولید و ساخت عمان (Made in Oman)",
        "opt_budget_1": "کمتر از ۵۰,۰۰۰ دلار",
        "opt_budget_2": "۵۰,۰۰۰ تا ۲۵۰,۰۰۰ دلار",
        "opt_budget_3": "۲۵۰,۰۰۰ تا ۱,۰۰۰,۰۰۰ دلار",
        "opt_budget_4": "بیش از ۱,۰۰۰,۰۰۰ دلار"
    },
    "en": {
        # Navigation & Mobile Drawer
        "nav_all_services": "Overview of All Services & Solutions",
        "mobile_sub_services": "Specialized Services Catalog",
        "mobile_sub_hubs": "Strategic Ports & Free Zones",
        "btn_explore_pillar": "Explore Pillar Details",
        "btn_whatsapp_cta": "Chat on WhatsApp",
        "btn_whatsapp_instant": "Instant WhatsApp Support",
        "btn_rfq_submit": "Submit Request for Quotation (RFQ)",
        "btn_consult_logistics": "Consult Supply Chain Team",
        "btn_start_localization": "Explore Manufacturing in Oman",
        "btn_advisory_request": "Request Financial & Trade Advisory",

        # 404 & Thank you
        "err_404_title": "Page Not Found",
        "err_404_desc": "The page you are looking for does not exist or has been moved. You can return to the homepage or contact our team directly.",
        "thank_you_title": "Your Trade Request Has Been Received",
        "thank_you_desc": "Thank you for reaching out to Al Takamul International Trading LLC. Your specification has been routed to our commercial team, and an advisor will contact you within 24 business hours.",

        # About Page Content
        "ab_vision_desc": "To stand as the preeminent and most trusted international trading house and supply chain partner in the Sultanate of Oman and the wider MENA region.",
        "ab_mission_title": "Operational Mission",
        "ab_mission_desc": "Delivering turnkey solutions in industrial procurement, cross-border export/import, and domestic manufacturing setup with rigorous institutional governance.",
        "ab_values_title": "Institutional Values",
        "ab_values_desc": "Uncompromising commercial confidentiality (strict NDAs), regulatory adherence, cost transparency, and operational velocity in field execution.",
        "ab_official_info_title": "Corporate Entity & Regulatory Credentials",
        "lbl_legal_name": "Official Registered Name:",
        "val_legal_name": "Al Takamul International Trading LLC",
        "lbl_cr_number": "Commercial Registration (CR):",
        "lbl_headquarters": "Headquarters:",
        "val_headquarters": "Muscat - Knowledge Oasis Muscat (KOM), Business Complex",
        "lbl_phone_wa": "Direct Desk & WhatsApp:",
        "lbl_official_email": "Executive Email Desk:",

        # Contact Page Content
        "ct_phone_title": "Direct Phone & WhatsApp Desk",
        "ct_phone_desc": "Fast-track communication channel for direct trade inquiries and partner dialogue.",
        "ct_email_title": "Institutional Email Communication",
        "ct_email_desc": "For sending Requests for Quotation (RFQ), contracts, specifications, and manifests.",
        "ct_hq_title": "Headquarters in Muscat",
        "ct_hq_desc": "Knowledge Oasis Muscat (KOM), Business Complex, Sultanate of Oman.",
        "ct_form_title": "Send Direct Inquiry to Commercial Desk",

        # Services Matrix Page Content
        "srv_card1_title": "1. International Trading House & Representation",
        "srv_card1_desc": "Structuring international trade transactions, deal brokerage, and acting as exclusive regional commercial agent.",
        "srv_card2_title": "2. Import, Export & Re-Export Logistics",
        "srv_card2_desc": "Ocean and air shipments, bonded handling in Sohar, Salalah, and Duqm ports, and seamless Bayan customs clearance.",
        "srv_card3_title": "3. Project Procurement & Strategic Supply",
        "srv_card3_desc": "Sourcing turnkey industrial machinery, production lines, strategic feedstocks, and equipment for major developers.",
        "srv_card4_title": "4. Trade Advisory & Payment Structuring",
        "srv_card4_desc": "Specialized consulting on Documentary Letters of Credit (L/C), Bank Guarantees, counterparty vetting, and capital hedging.",
        "srv_card5_title": "5. Manufacturing Infrastructure & Made in Oman",
        "srv_card5_desc": "Contract manufacturing, assembly line establishment, achieving In-Country Value (ICV), and zero-duty US export access via FTA.",

        # FAQ Page Content
        "faq_q1": "What strategic advantages does trading through Oman offer?",
        "faq_a1": "Oman sits outside the Strait of Hormuz directly facing the Indian Ocean, features deepwater ports, and holds bilateral Free Trade Agreements (FTAs) with the US, Singapore, and EFTA alongside 100% foreign ownership and zero corporate tax freezones.",
        "faq_q2": "How does Al Takamul support 'Made in Oman' initiatives?",
        "faq_a2": "We assist manufacturers with industrial feasibility, contracting with accredited Omani factories, raw material importation, and meeting In-Country Value (ICV) thresholds to attain official Made in Oman certification.",
        "faq_q3": "Does Al Takamul provide direct loans or banking credit?",
        "faq_a3": "No. Al Takamul is an international trading house, not a bank or lending institution. We provide advisory on payment mechanics, draft compliant Letter of Credit terms, and coordinate with licensed commercial banks.",
        "faq_q4": "Which Incoterms rules do you execute in commercial contracts?",
        "faq_a4": "We manage contracts governed by all ICC Incoterms 2020 terms including EXW, FOB, CFR, CIF, DAP, and DDP according to partner requirements.",
        "faq_q5": "Are there limitations on commodity categories handled?",
        "faq_a5": "We handle a comprehensive spectrum of industrial and commercial commodities, coordinating with Omani regulatory authorities for controlled items such as food, pharmaceuticals, and chemicals.",
        "faq_q6": "How is partner and vendor confidentiality safeguarded?",
        "faq_a6": "We execute legally binding Non-Disclosure Agreements (NDAs) prior to exchanging pricing structures, formulations, or vendor specifications.",

        # Financial Advisory Page Content
        "fa_compliance_notice_lbl": "Governance & Banking Compliance Notice:",
        "fa_compliance_notice_desc": "Al Takamul International Trading LLC is an institutional trading house and trade consultancy, not a bank, loan provider, or money transmitter. All services are strictly limited to payment engineering advisory, L/C structuring, and coordinating with licensed banking institutions.",
        "fa_sub1_title": "Payment Structuring & Letters of Credit",
        "fa_sub1_desc": "Advising on confirmed L/Cs, Bank Guarantees (Performance & Advance Payment Bonds), and Cash Against Documents (CAD).",
        "fa_sub2_title": "Counterparty Vetting & Solvency Review",
        "fa_sub2_desc": "Assessing financial standing and transaction history of prospective global suppliers and buyers to prevent defaults and contractual disputes.",
        "fa_sub3_title": "Landed Cost & Working Capital Analysis",
        "fa_sub3_desc": "Rigorous calculation of total landed costs including duties, ocean freight, marine insurance, and capital carry costs.",

        # Import Export Page Content
        "ie_sub1_title": "Direct Import Clearance into Oman",
        "ie_sub1_desc": "Importing commodities and capital equipment for Omani enterprises, securing approvals, and conducting origin inspections.",
        "ie_sub2_title": "Cross-Border Export & Re-Export",
        "ie_sub2_desc": "Re-exporting transshipment cargo to GCC, East Africa, and India utilizing bonded freezone facilities in Sohar, Salalah, and Duqm.",
        "ie_sub3_title": "Customs Documentation & Compliance",
        "ie_sub3_desc": "Issuing authenticated Certificates of Origin (COO), legalized commercial invoices, bills of lading, and packing lists.",
        "ie_sub4_title": "Regulatory Clearance for Specialized Goods",
        "ie_sub4_desc": "Managing institutional clearances for food, pharmaceuticals, and chemicals with the Ministry of Commerce, Consumer Protection, and Royal Oman Police Customs.",

        # Made in Oman Page Content
        "mo_sub1_title": "Contract Manufacturing (OEM/Private Label)",
        "mo_sub1_desc": "Connecting global firms with vetted manufacturing plants across Oman while safeguarding 100% intellectual property and formulations.",
        "mo_sub2_title": "Assembly & Packaging Setup",
        "mo_sub2_desc": "Importing semi-finished components for final assembly and quality inspection within Oman to achieve national origin status.",
        "mo_sub3_title": "National In-Country Value (ICV) Certification",
        "mo_sub3_desc": "Auditing and filing local value add accounting to qualify for official license to bear the Made in Oman trademark.",
        "mo_sub4_title": "Export Privileges of Made in Oman Certification",
        "mo_sub4_desc": "Certified Omani manufactured goods capture premier international market advantages:",
        "mo_feat_gcc": "• Duty-free entry into all 6 GCC member states",
        "mo_feat_fta": "• 100% tariff exemption on entry to the United States under US-Oman FTA",
        "mo_feat_tender": "• Mandatory 10% price preference in Omani government tenders and procurements",
        "mo_feat_arab": "• Preferential entry into Arab League markets under GAFTA",

        # Privacy Page Content
        "priv_s1_title": "1. Information Collection & Usage",
        "priv_s1_desc": "We gather only essential commercial details to process inquiries and execute transactions. We do not sell or rent partner data under any circumstances.",
        "priv_s2_title": "2. Confidentiality & Non-Disclosure (NDAs)",
        "priv_s2_desc": "All financial details, margin structures, supplier lists, and buyer identities are strictly protected under enforceable NDAs.",
        "priv_s3_title": "3. Data Security & Storage",
        "priv_s3_desc": "Transactions and commercial communications are secured utilizing modern enterprise-grade security protocols.",

        # Procurement Page Content
        "pr_sub1_title": "Industrial Machinery & Production Lines",
        "pr_sub1_desc": "Turnkey procurement of mechanical systems, heavy equipment, power generators, and spare parts for infrastructure projects.",
        "pr_sub2_title": "Raw Materials & Strategic Feedstocks",
        "pr_sub2_desc": "Institutional sourcing of metals, polymers, chemicals, and industrial commodities from premier global producers.",
        "pr_sub3_title": "Commercial & Hospitality Fit-Outs",
        "pr_sub3_desc": "Supplying tier-one hotels, commercial complexes, and towers with high-specification materials, furnishings, and facility equipment.",
        "pr_sub4_title": "Procurement Engagement Models",
        "pr_model1_title": "1. Direct Purchase & Resale (Principal Trading)",
        "pr_model1_desc": "Al Takamul procures equipment on its own account and resells directly under a consolidated local invoice with warranties.",
        "pr_model2_title": "2. Procurement by Agency & Commission",
        "pr_model2_desc": "We act as your dedicated purchasing agent, negotiating directly with international manufacturers for a transparent commission.",

        # Terms Page Content
        "term_s1_title": "1. Legal Entity & Scope of Operations",
        "term_s1_desc": "Al Takamul International Trading LLC is an institutional company registered in the Sultanate of Oman under CR 1389420, licensed by the Ministry of Commerce, Industry and Investment Promotion.",
        "term_s2_title": "2. Financial Terms & Letter of Credit Rules",
        "term_s2_desc": "Al Takamul is not a banking entity. All trade advisory is provided in accordance with ICC Uniform Customs and Practice for Documentary Credits (UCP 600) and Central Bank of Oman regulations.",
        "term_s3_title": "3. Shipping Rules & Incoterms 2020",
        "term_s3_desc": "Risk transfer, freight obligations, and marine insurance points are defined precisely within each transaction agreement under ICC Incoterms rules.",
        "term_s4_title": "4. Governing Law & Jurisdiction",
        "term_s4_desc": "All interactions and commercial agreements are governed by the commercial laws of the Sultanate of Oman and the jurisdiction of Muscat commercial courts.",

        # Request Form Select Options
        "opt_srv_it": "International Trading House (Institutional Commerce)",
        "opt_srv_ie": "Import, Export & Re-Export Logistics",
        "opt_srv_pr": "Project Procurement & Supply",
        "opt_srv_fa": "Trade Finance Advisory & L/Cs",
        "opt_srv_mo": "Made in Oman & US FTA Industrialization",
        "opt_budget_1": "Under $50,000 USD",
        "opt_budget_2": "$50,000 - $250,000 USD",
        "opt_budget_3": "$250,000 - $1,000,000 USD",
        "opt_budget_4": "Over $1,000,000 USD"
    }
}

for lang in ['ar', 'fa', 'en']:
    t[lang].update(data_keys[lang])

with open(os.path.join(BASE_DIR, 'translations.json'), 'w', encoding='utf-8') as f:
    json.dump(t, f, ensure_ascii=False, indent=2)

with open(os.path.join(BASE_DIR, 'js', 'translations_data.js'), 'w', encoding='utf-8') as f:
    f.write(f"window.ALT_TRANSLATIONS = {json.dumps(t, ensure_ascii=False)};")

print("Added all missing keys to translations.json and js/translations_data.js successfully!")
