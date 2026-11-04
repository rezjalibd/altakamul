import json, os

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'
TRANS_PATH = os.path.join(BASE_DIR, 'translations.json')
JS_TRANS_PATH = os.path.join(BASE_DIR, 'js/translations_data.js')

with open(TRANS_PATH, 'r', encoding='utf-8') as f:
    t = json.load(f)

# Comprehensive legal, privacy, terms, and hub keys
new_keys = {
    # Privacy Policy Page
    "page_priv_tag": {
        "ar": "سياسة الخصوصية وحماية البيانات",
        "fa": "سیاست حفظ حریم خصوصی و امنیت داده‌ها",
        "en": "Privacy Policy & Data Protection"
    },
    "page_priv_title": {
        "ar": "سياسة الخصوصية وسرية البيانات التجارية",
        "fa": "سیاست حفظ حریم خصوصی و محرمانگی داده‌های تجاری",
        "en": "Privacy Policy & Commercial Data Confidentiality"
    },
    "page_priv_sub": {
        "ar": "التزام مؤسسي بحماية خصوصية الشركاء وسرية الصفقات الدولية بموجب قانون حماية البيانات الشخصية العماني (المرسوم السلطاني 6/2022).",
        "fa": "تعهد سازمانی به حفاظت از حریم خصوصی شرکا و محرمانگی معاملات تجاری بر اساس قانون حفاظت از داده‌های سلطنت عمان (فرمان سلطانی ۶/۲۰۲۲).",
        "en": "Institutional commitment to protecting partner privacy and international trade confidentiality under Oman's Personal Data Protection Law (Royal Decree 6/2022)."
    },
    "priv_s1_title": {
        "ar": "١. الإطار القانوني والصفة المؤسسية",
        "fa": "۱. چارچوب حقوقی و جایگاه سازمانی",
        "en": "1. Legal Framework & Institutional Standing"
    },
    "priv_s1_desc": {
        "ar": "تخضع كافة إجراءات جمع ومعالجة البيانات لشركة تكامل للتجارة الدولية ش.م.م (سجل تجاري: 1389420) لأحكام قانون حماية البيانات الشخصية الصادر بالمرسوم السلطاني رقم 6/2022 وقانون المعاملات الإلكترونية رقم 69/2008. تضمن الشركة أن جميع المعلومات المقدمة من الموردين والمشترين تعامل كبيانات سرية للغاية ومحمية بموجب أرفع معايير الحوكمة المؤسسية.",
        "fa": "کلیه فرایندهای جمع‌آوری و پردازش داده‌ها در بازرگانی بین‌المللی تکامل (شماره ثبت: ۱۳۸۹۴۲۰) مشمول قانون حفاظت از داده‌های شخصی سلطنت عمان (فرمان سلطانی ۶/۲۰۲۲) و قانون تجارت الکترونیک (۶۹/۲۰۰۸) است. این شرکت تضمین می‌نماید که تمامی اطلاعات دریافتی از تأمین‌کنندگان و خریداران کاملاً محرمانه بوده و تحت بالاترین استانداردهای حاکمیت سازمانی نگهداری می‌شود.",
        "en": "All data collection and processing activities of Al Takamul International Trading LLC (CR: 1389420) are governed by the Oman Personal Data Protection Law (Royal Decree 6/2022) and Electronic Transactions Law (69/2008). The company guarantees that all corporate and transaction details provided by buyers and suppliers are treated with the highest confidentiality."
    },
    "priv_s2_title": {
        "ar": "٢. نطاق البيانات المجمعة في التعاملات التجارية",
        "fa": "۲. دامنه داده‌های جمع‌آوری‌شده در معاملات تجاری",
        "en": "2. Scope of Collected Commercial Data"
    },
    "priv_s2_desc": {
        "ar": "تشمل البيانات المجمعة: بيانات التحقق المؤسسي (KYC) للمفوضين بالتوقيع، أرقام السجلات والبطاقات الضريبية، الوثائق التجارية (الفواتير، بوالص الشحن، شهادات المنشأ)، وتفاصيل الحسابات والاعتمادات البنكية المسجلة عبر نظام سويفت (SWIFT)، إلى جانب المراسلات الفنية لطلبات الاستيراد والتصدير.",
        "fa": "داده‌های جمع‌آوری‌شده شامل: احراز هویت شرکتی (KYC) صاحبان امضا، اسناد ثبت شرکت و مالیاتی، مدارک بازرگانی (فاکتورهای تجاری، بارنامه‌های دریایی و هوایی، گواهی مبدأ)، اطلاعات حساب‌های بانکی و اعتبارات اسنادی در سامانه سوئیفت، و مشخصات فنی کالاهای مبادلاتی است.",
        "en": "Data collected includes: Corporate Know-Your-Customer (KYC) records of authorized signatories, tax and registration numbers, trade documentation (commercial invoices, bills of lading, certificates of origin), bank account and SWIFT documentary credit details, and technical product specifications."
    },
    "priv_s3_title": {
        "ar": "٣. الأغراض المشروعة لمعالجة البيانات",
        "fa": "۳. اهداف قانونی پردازش داده‌ها",
        "en": "3. Legitimate Purposes of Processing"
    },
    "priv_s3_desc": {
        "ar": "نستخدم البيانات حصرياً لـ: تنفيذ ومتابعة عقود البيع والشراء الدولية، إصدار التراخيص والتخليص الجمركي عبر نظام بيان التابع لشرطة عُمان السلطانية، التحقق من الملاءة المالية ومكافحة غسيل الأموال وتمويل الإرهاب بموجب القانون رقم 30/2016، وتنسيق سلاسل الإمداد اللوجستية البحرية والجوية.",
        "fa": "داده‌ها منحصراً جهت اهداف زیر پردازش می‌شوند: اجرای دقیق قراردادهای خرید و فروش بین‌المللی، اخذ مجوزها و ترخیص قطعی گمرکی در سامانه الکترونیکی بیان پلیس سلطنتی عمان، اعتبارسنجی مالی و انطباق با مقررات مبارزه با پولشویی (قانون ۳۰/۲۰۱۶)، و هماهنگی خطوط کشتیرانی و لجستیک ترکیبی.",
        "en": "Data is processed strictly for: Executing and administering international trade contracts, regulatory clearance through the Royal Oman Police Bayan customs portal, financial solvency and Anti-Money Laundering (AML/CFT Law 30/2016) verification, and coordinating multimodal logistics pipelines."
    },
    "priv_s4_title": {
        "ar": "٤. سرية الأسرار التجارية واتفاقيات عدم الإفصاح (NDA)",
        "fa": "۴. محرمانگی اسرار تجاری و توافق‌نامه‌های NDA",
        "en": "4. Trade Secrets & Mutual Non-Disclosure Agreements"
    },
    "priv_s4_desc": {
        "ar": "تدرك تكامل الطبيعة الحساسة للأسواق الدولية، وتعتبر قوائم الموردين وهوامش التسعير والعملاء المحتملين أسراراً تجارية غير قابلة للمشاركة. نوقع اتفاقيات عدم إفصاح ملزمة قانوناً مع كافة الشركاء، مع التزام تام بعدم مشاركة أي معلومة إلا بموافقة خطية مسبقة من العميل.",
        "fa": "تکامل به ماهیت حساس بازارهای بین‌المللی واقف است و فهرست‌های تأمین‌کنندگان، مارجین‌های سود و فرمول‌های قیمت‌گذاری را اسرار تجاری غیرقابل‌افشا می‌داند. ما قراردادهای محرمانگی متقابل (NDA) منعقد می‌کنیم و هرگونه اشتراک‌گذاری داده منوط به موافقت کتبی و رسمی طرفین است.",
        "en": "Al Takamul recognizes the proprietary nature of global commodities and treats supplier catalogs, margin structures, and commercial leads as strictly protected trade secrets. We execute legally binding NDAs and will not disclose sensitive partner information without prior written consent."
    },
    "priv_s5_title": {
        "ar": "٥. مشاركة البيانات مع الجهات الرقابية والموانئ",
        "fa": "۵. اشتراک‌گذاری داده‌ها با مراجع نظارتی و بنادر",
        "en": "5. Data Disclosure to Regulators & Port Authorities"
    },
    "priv_s5_desc": {
        "ar": "لا يتم الإفصاح عن البيانات إلا للجهات الرسمية المصرح لها قانوناً بسلطنة عُمان وتشمل: الإدارة العامة للجمارك (نظام بيان)، إدارات الموانئ والمناطق الحرة (صحار، صلالة، الدقم)، وزارة التجارة والصناعة وترويج الاستثمار، والمصارف المعنية بإدارة الاعتمادات المستندية، وذلك في حدود ما تقتضيه متطلبات إتمام الصفقة فقط.",
        "fa": "افشای اطلاعات صرفاً به مراجع رسمی و قانونی سلطنت عمان محدود می‌گردد که شامل: اداره کل گمرک (سامانه بیان)، مدیریت بنادر و مناطق آزاد (صحار، صلاله، دقم)، وزارت بازرگانی و سرمایه‌گذاری، و بانک‌های کارگزار گشاینده اعتبارات اسنادی، و منحصراً در چارچوب الزامات اجرای معامله است.",
        "en": "Data is disclosed strictly to authorized statutory bodies in Oman: Directorate General of Customs (Bayan portal), Free Zone Authorities (Sohar, Salalah, Duqm), the Ministry of Commerce, and correspondent banks issuing L/Cs, solely to the extent required to execute transactions."
    },
    "priv_s6_title": {
        "ar": "٦. النقل الآمن للبيانات عبر الحدود الدولية",
        "fa": "۶. انتقال امن داده‌ها از مرزهای بین‌المللی",
        "en": "6. Cross-Border International Data Transfers"
    },
    "priv_s6_desc": {
        "ar": "في حال تطلبت العمليات التجارية تبادل مستندات الشحن والفحص مع جهات تفتيش دولية (مثل SGS أو Bureau Veritas) أو مصارف مراسلة خارجية، يتم نقل البيانات عبر قنوات مصرفية ورقمية مشفرة تضمن أعلى مستويات الحماية وتمنع أي وصول غير مصرح به.",
        "fa": "در صورتی که اجرای معامله نیازمند تبادل اسناد حمل و بازرسی فنی با شرکت‌های معتبر جهانی (مانند SGS یا Bureau Veritas) یا بانک‌های کارگزار خارجی باشد، کلیه داده‌ها از طریق بسترها و پروتکل‌های رمزنگاری‌شده ایمن منتقل می‌شوند.",
        "en": "Where cross-border operations necessitate sharing shipping manifests or technical inspection records with accredited testing agencies (e.g., SGS, Bureau Veritas) or foreign banks, transmission occurs across encrypted enterprise channels ensuring zero unauthorized interception."
    },
    "priv_s7_title": {
        "ar": "٧. التدابير الأمنية ومدة الاحتفاظ بالسجلات",
        "fa": "۷. اقدامات امنیتی و دوره نگهداری سوابق",
        "en": "7. Security Measures & Record Retention"
    },
    "priv_s7_desc": {
        "ar": "نطبق بروتوكولات تشفير متقدمة (TLS 1.3 / AES-256) لحماية قواعد البيانات والمراسلات. يتم الاحتفاظ بسجلات المعاملات التجارية والعقود لمدة 10 سنوات امتثالاً للمتطلبات المحاسبية والقانونية المنصوص عليها في قانون التجارة العماني وقانون الشركات التجارية رقم 18/2019، ليتم بعدها إتلافها أو أرشفتها بشكل آمن.",
        "fa": "ما از پروتکل‌های رمزنگاری پیشرفته (TLS 1.3 و AES-256) برای حفاظت از پایگاه‌های داده و مکاتبات استفاده می‌کنیم. اسناد قراردادها و تراکنش‌های تجاری بر اساس الزامات قانونی قانون تجارت و قانون شرکت‌های تجاری عمان (۱۸/۲۰۱۹) به مدت ۱۰ سال نگهداری و پس از آن به صورت ایمن امحا یا آرشیو دائم می‌شوند.",
        "en": "We apply advanced encryption (TLS 1.3 / AES-256) across all systems. Commercial contracts, invoices, and audit logs are retained for 10 years in strict compliance with Omani Commercial Companies Law (RD 18/2019), after which they are securely purged or archived."
    },
    "priv_s8_title": {
        "ar": "٨. حقوق أصحاب البيانات والشركات",
        "fa": "۸. حقوق صاحبان داده و شرکت‌های تجاری",
        "en": "8. Rights of Corporate Clients & Data Principals"
    },
    "priv_s8_desc": {
        "ar": "يحق لكل شريك تجاري طلب الاطلاع على بياناته المخزنة، تصحيح أي معلومات غير دقيقة، طلب شهادة امتثال للمعاملات المؤرشفة، وتقديم أي استفسار أو اعتراض بشأن معالجة البيانات من خلال التواصل المباشر مع مكتب الامتثال القانوني للشركة.",
        "fa": "تمامی شرکای تجاری حق دارند به داده‌های ثبت‌شده خود دسترسی داشته باشند، درخواست تصحیح اطلاعات نادرست ثبت کنند، گواهی انطباق تراکنش‌های بایگانی‌شده را دریافت نمایند و هرگونه ابهام یا بازبینی را با واحد حقوقی و انطباق شرکت مطرح کنند.",
        "en": "Commercial partners have the right to access stored records, request rectification of inaccurate data, obtain compliance audit summaries for archived trades, and raise inquiries regarding processing by contacting our legal compliance team."
    },
    "priv_s9_title": {
        "ar": "٩. الاتصال بمسؤول الامتثال وحماية البيانات",
        "fa": "۹. تماس با مسئول انطباق و حفاظت از داده‌ها",
        "en": "9. Compliance & DPO Contact"
    },
    "priv_s9_desc": {
        "ar": "لأي استفسارات تتعلق بسياسة الخصوصية وسرية البيانات، يرجى التواصل مع إدارة الامتثال عبر البريد الإلكتروني: compliance@omantakamul.com أو هاتفياً على: 96871081635+ / مسقط، سلطنة عُمان. نلتزم بالرد على كافة الإخطارات والطلبات في غضون 14 يوم عمل.",
        "fa": "برای هرگونه استعلام، مشاوره یا درخواست در خصوص سیاست‌های حفظ محرمانگی و حریم خصوصی، می‌توانید با واحد انطباق تکامل از طریق ایمیل compliance@omantakamul.com یا تلفن ۹۶۸۷۱۰۸۱۶۳۵+ در مسقط در ارتباط باشید. تعهد پاسخگویی حداکثر طی ۱۴ روز کاری است.",
        "en": "For any inquiries regarding data protection and confidentiality protocols, contact our Compliance Office via compliance@omantakamul.com or phone: +968 7108 1635 / Muscat, Oman. We commit to addressing all formal inquiries within 14 business days."
    },

    # Terms & Conditions Page
    "page_term_tag": {
        "ar": "الشروط والأحكام والتعاقد التجاري",
        "fa": "شرایط و ضوابط و چارچوب قراردادهای تجاری",
        "en": "Terms & Conditions & Commercial Contracting"
    },
    "page_term_title": {
        "ar": "الشروط والأحكام المنظمة للتعاملات التجارية الدولية",
        "fa": "شرایط و مقررات حاکم بر معاملات و قراردادهای بین‌المللی",
        "en": "Terms & Conditions Governing International Trade Transactions"
    },
    "page_term_sub": {
        "ar": "الإطار القانوني والتعاقدي المعتمد لكافة الخدمات والصفقات التجارية التي تديرها شركة تكامل للتجارة الدولية ش.م.م (سجل تجاري: 1389420).",
        "fa": "چارچوب حقوقی و قراردادی معتبر برای کلیه خدمات و معاملات تجاری به مدیریت بازرگانی بین‌المللی تکامل (شماره ثبت: ۱۳۸۹۴۲۰).",
        "en": "The certified legal and contractual framework governing all trade services and deals managed by Al Takamul International Trading LLC (CR: 1389420)."
    },
    "term_s1_title": {
        "ar": "١. الأهلية القانونية ونطاق الأنشطة المرخصة",
        "fa": "۱. صلاحیت قانونی و دامنه فعالیت‌های مجاز",
        "en": "1. Legal Capacity & Scope of Licensed Activities"
    },
    "term_s1_desc": {
        "ar": "شركة تكامل للتجارة الدولية ش.م.م شركة ذات مسؤولية محدودة مسجلة في سلطنة عمان (CR: 1389420). تعمل الشركة بموجب التراخيص الصادرة من وزارة التجارة والصناعة وترويج الاستثمار، وتشمل أنشطتها: الاستيراد والتصدير العام، التمثيل التجاري وبيت التجارة (Trading House)، الوساطة في الصفقات الدولية، واستشارات سلاسل الإمداد وإدارة المشتريات.",
        "fa": "بازرگانی بین‌المللی تکامل شرکت با مسئولیت محدود ثبت‌شده در سلطنت عمان (شماره ثبت: ۱۳۸۹۴۲۰) است که تحت مجوزهای رسمی وزارت تجارت، صنعت و ترویج سرمایه‌گذاری فعالیت می‌کند. دامنه فعالیت‌ها شامل صادرات و واردات کالا، نمایندگی بازرگانی و خانه تجارت (Trading House)، کارگزاری معاملات کلان و مشاوره تخصصی زنجیره تأمین و اعتبارات است.",
        "en": "Al Takamul International Trading LLC is an Omani limited liability corporation (CR: 1389420) operating under licenses issued by the Ministry of Commerce, Industry and Investment Promotion. Scope includes general import/export, international trading house representation, commodity brokerage, and supply chain procurement management."
    },
    "term_s2_title": {
        "ar": "٢. الصفة التجارية وإخلاء المسؤولية المصرفية",
        "fa": "۲. ماهیت بازرگانی و سلب مسئولیت بانکی",
        "en": "2. Commercial Standing & Banking Disclaimer"
    },
    "term_s2_desc": {
        "ar": "توضح تكامل أنها بيت تجارة دولي وشركة إدارة صادرات (EMC)، وليست مصرفاً أو مؤسسة إقراض أو وسيطاً مالياً مرخصاً من البنك المركزي العُماني. كافة الترتيبات المتعلقة بالاعتمادات المستندية (L/C) أو الضمانات البنكية وحسابات الضمان (Escrow) يتم فتحها وإدارتها حصرياً عبر المصارف التجارية المعتمدة محلياً ودولياً ووفق اللوائح المصرفية السارية.",
        "fa": "تکامل رسماً تصریح می‌نماید که یک خانه تجارت بین‌الملل و شرکت مدیریت صادرات (EMC) است و بانک، مؤسسه اعتباری یا صرافی دارای مجوز از بانک مرکزی عمان نیست. کلیه امور اعتبارات اسنادی (L/C)، ضمانت‌نامه‌های بانکی و حساب‌های امانی (Escrow) منحصراً از طریق بانک‌های تجاری معتبر دارای مجوز اجرا و مدیریت می‌شوند.",
        "en": "Al Takamul explicitly states that it is an International Trading House and Export Management Company (EMC), not a licensed commercial bank or credit-granting financial institution under Central Bank of Oman jurisdiction. All Letters of Credit (L/C), bank guarantees, and escrow mechanisms are structured exclusively through authorized commercial banks."
    },
    "term_s3_title": {
        "ar": "٣. شروط التجارة الدولية (Incoterms® 2020) والمسؤوليات",
        "fa": "۳. قواعد اینکوترمز ۲۰۲۰ و حدود مسئولیت‌ها",
        "en": "3. Incoterms® 2020 Rules & Shipping Liabilities"
    },
    "term_s3_desc": {
        "ar": "تخضع كافة عمليات التوريد والشحن لقواعد الإنكوترمز الصادرة عن غرفة التجارة الدولية (Incoterms 2020) مثل FOB, CIF, CFR, DAP, DDP وفق ما يُحدد صراحة في كل عقد تجاري مستقل. تنتقل المخاطر والمسؤوليات التأمينية استناداً إلى مصطلح التسليم المتفق عليه، ويلتزم المشتري بتغطية التأمين البحري الشامل (Institute Cargo Clauses A) ما لم ينص العقد على خلاف ذلك.",
        "fa": "تمامی فرایندهای تأمین و حمل کالا تحت قواعد رسمی اتاق بازرگانی بین‌المللی (اینکوترمز ۲۰۲۰) نظیر FOB، CIF، CFR، DAP و DDP انجام می‌پذیرد. نقطه انتقال ریسک، مسئولیت‌ها و پرداخت هزینه بیمه باربری دقیقاً بر اساس ترم قرارداد تعیین می‌گردد و خریدار ملزم به اخذ بیمه‌نامه دریایی معتبر (کلوز A) خواهد بود مگر اینکه در متن قرارداد توافق دیگری درج شده باشد.",
        "en": "All procurement and shipping operations are executed in strict accordance with ICC Incoterms® 2020 rules (e.g., FOB, CIF, CFR, DAP, DDP) as specified in individual commercial agreements. Risk transfer and insurance liabilities vest according to the agreed delivery term, with Institute Cargo Clauses (A) marine coverage required unless otherwise stated."
    },
    "term_s4_title": {
        "ar": "٤. الاعتمادات المستندية وآليات الدفع الدولية",
        "fa": "۴. ساختار اعتبارات اسنادی و روش‌های پرداخت بین‌المللی",
        "en": "4. Documentary Credits & International Payment Structures"
    },
    "term_s4_desc": {
        "ar": "تطبق على كافة الاعتمادات المستندية القواعد والأعراف الموحدة للاعتمادات المستندية (ICC UCP 600) والضمانات البنكية عند الطلب (URDG 758). لا يتم الإفراج عن البضائع أو تسليم بوالص الشحن الأصلية إلا بعد استيفاء الشروط المالية وتأكيد الدفع البنكي غير القابل للنقض.",
        "fa": "کلیه اعتبارات اسنادی مشمول مقررات متحدالشکل اعتبارات اسنادی اتاق بازرگانی بین‌المللی (ICC UCP 600) و ضمانت‌نامه‌های عندالمطالبه (URDG 758) است. آزادسازی کالا و واگذاری اسناد مالکیت و بارنامه‌های اصلی صرفاً پس از تحقق کامل تعهدات مالی و تأیید قطعی بانکی انجام خواهد شد.",
        "en": "All documentary credit facilities adhere strictly to the ICC Uniform Customs and Practice for Documentary Credits (UCP 600) and Uniform Rules for Demand Guarantees (URDG 758). Cargo release and original title documents are surrendered only upon definitive, irrevocable bank payment confirmation."
    },
    "term_s5_title": {
        "ar": "٥. الفحص الفني، معايير المطابقة، وإجراءات الاعتراض",
        "fa": "۵. بازرسی فنی، انطباق استاندارد و فرایند ادعاها",
        "en": "5. Technical Inspection, Conformity & Claim Procedures"
    },
    "term_s5_desc": {
        "ar": "تخضع البضائع الموردة لشهادات الفحص الفني الصادرة من شركات معاينة دولية مستقلة (مثل SGS, Bureau Veritas, Intertek) في ميناء الشحن لمطابقة المواصفات القياسية الخليجية (GSO). في حال وجود أي اختلاف ظاهري أو عيب، يجب تقديم إخطار رسمي كتابي خلال 7 أيام عمل من تاريخ تفريغ الشحنة في ميناء الوصول مصحوباً بتقرير معاينة رسمي، وإلا اعتبرت الشحنة مقبولة نهائياً.",
        "fa": "کالاهای مبادلاتی مشمول بازرسی فنی مستقل توسط مراجع بین‌المللی (مانند SGS، Bureau Veritas یا Intertek) در مبدأ بارگیری جهت انطباق با استانداردهای خلیج فارس (GSO) هستند. در صورت وجود هرگونه مغایرت یا آسیب، مشتری موظف است حداکثر ظرف ۷ روز کاری پس از تخلیه در بندر مقصد، گزارش رسمی خود را ارسال نماید، در غیر این صورت محموله تأییدشده نهایی تلقی می‌شود.",
        "en": "Consignments undergo independent pre-shipment inspection (SGS, Bureau Veritas, Intertek) at loading ports to verify compliance with GCC Standardization Organization (GSO) requirements. Formal defect notices must be lodged in writing within 7 business days from discharge at destination port, accompanied by accredited survey reports."
    },
    "term_s6_title": {
        "ar": "٦. بنود القوة القاهرة والحد من المسؤولية اللوجستية",
        "fa": "۶. شرایط فورس‌ماژور و محدودیت مسئولیت‌های لجستیکی",
        "en": "6. Force Majeure & Limitation of Liability"
    },
    "term_s6_desc": {
        "ar": "لا تتحمل شركة تكامل أي مسؤولية مالية عن التأخير أو عدم التنفيذ الناجم عن ظروف القوة القاهرة خارجة عن السيطرة المعقولة، بما في ذلك: النزاعات المسلحة، إغلاق الممرات الملاحية أو المضائق، الكوارث الطبيعية، القرصنة البحرية، الإضرابات العامة، أو القرارات الحكومية المفاجئة بحظر التصدير/الاستيراد. وتقتصر المسؤولية القصوى للشركة في جميع الأحوال على قيمة أتعاب الإدارة التجارية للخدمة محل التعاقد.",
        "fa": "بازرگانی تکامل هیچ‌گونه مسئولیتی در قبال خسارات ناشی از فورس‌ماژور شامل جنگ، بسته شدن آبراه‌ها و کانال‌های بین‌المللی، بلایای طبیعی، دزدی دریایی، اعتصابات بندری یا تحریم‌ها و ممنوعیت‌های ناگهانی دولتی ندارد. حداکثر مسئولیت مالی شرکت در هر شرایطی به کارمزد مدیریت خدمات همان قرارداد محدود است.",
        "en": "Al Takamul shall not be liable for delivery failure or delays caused by Force Majeure events beyond reasonable control, including armed hostilities, waterway closures, natural disasters, maritime piracy, port strikes, or sudden trade embargoes. Maximum aggregate liability is strictly capped at the commercial management fee paid."
    },
    "term_s7_title": {
        "ar": "٧. الامتثال لمكافحة غسيل الأموال والعقوبات التجارية",
        "fa": "۷. انطباق مبارزه با پولشویی و تحریم‌های تجاری",
        "en": "7. AML, CFT & International Sanctions Compliance"
    },
    "term_s7_desc": {
        "ar": "تلتزم تكامل التزاماً صارماً بالقانون العماني لمكافحة غسيل الأموال وتمويل الإرهاب (القانون رقم 30/2016) وقوائم العقوبات المعتمدة دولياً. يحق للشركة إنهاء أي صفقة فوراً وتجميد الإجراءات وإخطار السلطات الرسمية في حال ثبوت عدم صحة وثائق المصدر/المستورد أو محاولة إدخال بضائع مقيدة أو محظورة دولياً.",
        "fa": "تکامل پایبندی کامل به قوانین مبارزه با پولشویی عمان (قانون ۳۰/۲۰۱۶) و لیست‌های تحریمی رسمی دارد. در صورت احراز هرگونه جعل اسناد یا تلاش برای تبادل کالاهای غیرمجاز، شرکت حق فسخ فوری قرارداد، توقف عملیات و ارجاع موضوع به مراجع قانونی ذی‌صلاح را برای خود محفوظ می‌دارد.",
        "en": "Al Takamul strictly enforces compliance with Oman's AML/CFT Law (Royal Decree 30/2016) and international sanctions directives. The company reserves the absolute right to suspend operations, terminate contracts, and report to competent statutory authorities upon discovering falsified documentation or prohibited transactions."
    },
    "term_s8_title": {
        "ar": "٨. حماية الأسرار التجارية والملكية الفكرية",
        "fa": "۸. حفاظت از اسرار تجاری و مالکیت فکری",
        "en": "8. Commercial Trade Secrets & IP Protection"
    },
    "term_s8_desc": {
        "ar": "تظل كافة الدراسات التحليلية، خطط المسارات اللوجستية، تصاميم سلاسل التوريد، وهوية العلامة التجارية لشركة تكامل ملكية فكرية حصرية للشركة ومحمية بموجب قوانين حماية الملكية الفكرية العمانية. يحظر نسخها أو استخدامها لأغراض تجارية أخرى دون موافقة خطية صريحة.",
        "fa": "کلیه تحلیل‌های بازرگانی، مهندسی مسیرهای لجستیک، معماری زنجیره تأمین و هویت تجاری تکامل متعلق به این شرکت بوده و تحت حمایت قوانین مالکیت فکری سلطنت عمان قرار دارد. هرگونه کپی‌برداری یا بهره‌برداری غیرمجاز پیگرد حقوقی خواهد داشت.",
        "en": "All analytical trade studies, route logistics models, supply chain engineering frameworks, and Al Takamul trademarks are the exclusive intellectual property of the company and protected under Omani IP legislation. Unauthorized copying, reverse-engineering, or publication is strictly prohibited."
    },
    "term_s9_title": {
        "ar": "٩. القانون الحاكم والتحكيم وفض النزاعات",
        "fa": "۹. قانون حاکم، داوری تجاری و حل‌وفصل اختلافات",
        "en": "9. Governing Law & Dispute Resolution"
    },
    "term_s9_desc": {
        "ar": "تخضع هذه الشروط وكافة العقود المرتبطة بها وتفسر حصرياً وفق القوانين والأنظمة النافذة في سلطنة عمان. في حال نشوء أي نزاع تجاري، يتم السعي لحله ودياً خلال 30 يوماً، وفي حال تعذر ذلك، يحال النزاع إلى المحاكم التجارية المختصة في سلطنة عُمان أو إلى التحكيم التجاري وفق قواعد مركز عُمان للتحكيم التجاري (OAC) إذا نص العقد على ذلك.",
        "fa": "این شرایط و کلیه قراردادهای تنظیمی منحصراً بر اساس قوانین و مقررات سلطنت عمان تفسیر و اجرا می‌شوند. در صورت بروز اختلاف، طرفین ابتدا ظرف ۳۰ روز تلاش برای حل دوستانه خواهند نمود؛ در صورت عدم حصول توافق، مرجع رسیدگی دادگاه‌های تجاری سلطنت عمان یا مرکز داوری تجاری عمان (OAC) خواهد بود.",
        "en": "These Terms and all related commercial agreements are governed exclusively by the laws of the Sultanate of Oman. Any dispute shall first be addressed through good-faith negotiation for 30 days, failing which it shall be submitted to the Commercial Courts of Oman or arbitration under Oman Commercial Arbitration Centre (OAC) rules."
    },

    # Additional Hub Section Badges and Labels
    "hub_sohar_badge": {
        "ar": "بوابة الخليج الشمالية • عمق بحري 25 متراً",
        "fa": "دروازه شمالی خلیج فارس • عمق اسکله ۲۵ متر",
        "en": "Northern Gulf Gateway • 25m Deepwater Draft"
    },
    "hub_salalah_badge": {
        "ar": "المحيط الهندي • محطة الترانزيت العالمية",
        "fa": "اقیانوس هند • ایستگاه ترانزیت و ترانشیپ جهانی",
        "en": "Indian Ocean Hub • Major Global Transshipment Terminal"
    },
    "hub_duqm_badge": {
        "ar": "أضخم مدينة اقتصادية متكاملة (2,000 كم²)",
        "fa": "بزرگترین شهر یکپارچه اقتصادی منطقه (۲,۰۰۰ کیلومترمربع)",
        "en": "Integrated Mega Economic Hub (2,000 km²)"
    },
    "hub_khazaen_badge": {
        "ar": "الميناء الجاف الأوسط وبوابة التجارة لليمن",
        "fa": "بندر خشک مرکزی مسقط و گذرگاه تجاری یمن",
        "en": "Central Dry Port & Yemen Strategic Gateway"
    }
}

for k, v in new_keys.items():
    t[k] = v

with open(TRANS_PATH, 'w', encoding='utf-8') as f:
    json.dump(t, f, ensure_ascii=False, indent=2)

with open(JS_TRANS_PATH, 'w', encoding='utf-8') as f:
    f.write(f'window.ALT_TRANSLATIONS = {json.dumps(t, ensure_ascii=False)};')

print(f"Successfully registered {len(new_keys)} new keys. Total dictionary keys: {len(t)}")
