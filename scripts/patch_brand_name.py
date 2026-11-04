import json

with open('/opt/data/cache/scratch/altakamul-site/translations.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

t['ar']['brand_name'] = "شركة تكامل للتجارة الدولية"
t['fa']['brand_name'] = "بازرگانی بین‌المللی تکامل"
t['en']['brand_name'] = "Al Takamul Trading"

with open('/opt/data/cache/scratch/altakamul-site/translations.json', 'w', encoding='utf-8') as f:
    json.dump(t, f, ensure_ascii=False, indent=2)

with open('/opt/data/cache/scratch/altakamul-site/js/translations_data.js', 'w', encoding='utf-8') as f:
    f.write(f"window.ALT_TRANSLATIONS = {json.dumps(t, ensure_ascii=False)};")

print("Updated brand names to fit beautifully!")
