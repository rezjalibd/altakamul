import json, os, glob, re

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'

with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
    t = json.load(f)

# Add missing keys
missing_dict = {
    "ar": {
        "hub_sohar_title": "ميناء وصناعية صحار",
        "hub_salalah_title": "ميناء صلالة الاستراتيجي",
        "hub_duqm_title": "المنطقة الاقتصادية بالدقم (SEZAD)",
        "nav_request": "طلب استشارة تجارية",
        "form_submit": "إرسال الطلب التجاري الآن"
    },
    "fa": {
        "hub_sohar_title": "بندر و منطقه آزاد صحار",
        "hub_salalah_title": "بندر استراتژیک صلاله",
        "hub_duqm_title": "منطقه ویژه اقتصادی دقم (SEZAD)",
        "nav_request": "درخواست مشاوره تجاری",
        "form_submit": "ثبت و ارسال درخواست تجاری"
    },
    "en": {
        "hub_sohar_title": "Sohar Port & Freezone",
        "hub_salalah_title": "Salalah Deepwater Port",
        "hub_duqm_title": "Duqm Special Economic Zone (SEZAD)",
        "nav_request": "Request Trade Consultation",
        "form_submit": "Submit Trade Request Now"
    }
}

for lang in ['ar', 'fa', 'en']:
    t[lang].update(missing_dict[lang])

# Collect all keys used in all HTML files
all_html_keys = set()
for fpath in glob.glob(os.path.join(BASE_DIR, '*.html')) + glob.glob(os.path.join(BASE_DIR, 'pages', '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    keys = re.findall(r'data-i18n=\"([^\"]+)\"', html)
    all_html_keys.update(keys)

print(f"Total HTML keys used: {len(all_html_keys)}")

# Check for any remaining missing keys across all 3 languages
any_missing = False
for lang in ['ar', 'fa', 'en']:
    missing = [k for k in sorted(all_html_keys) if k not in t[lang] or not str(t[lang][k]).strip()]
    if missing:
        any_missing = True
        print(f"ERROR: {lang} still missing {len(missing)} keys: {missing}")
    else:
        print(f"SUCCESS: {lang} has 100% of all {len(all_html_keys)} keys!")

if not any_missing:
    with open(os.path.join(BASE_DIR, 'translations.json'), 'w', encoding='utf-8') as f:
        json.dump(t, f, ensure_ascii=False, indent=2)

    with open(os.path.join(BASE_DIR, 'js', 'translations_data.js'), 'w', encoding='utf-8') as f:
        f.write(f"window.ALT_TRANSLATIONS = {json.dumps(t, ensure_ascii=False)};")
    print("translations.json and js/translations_data.js saved with 100% coverage!")
