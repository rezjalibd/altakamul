import glob, re
from html.parser import HTMLParser

class UntranslatedFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.nodes = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        has_i18n = 'data-i18n' in attrs_dict
        parent_has_i18n = any(item['has_i18n'] for item in self.stack)
        self.stack.append({'tag': tag, 'has_i18n': has_i18n or parent_has_i18n, 'attrs': attrs_dict})

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if not self.stack: return
        curr_tag = self.stack[-1]['tag']
        if curr_tag in ['script', 'style', 'title']: return
        if re.search(r'[\u0600-\u06FF]', data):
            if not self.stack[-1]['has_i18n']:
                s = data.strip()
                if s:
                    self.nodes.append((curr_tag, s))

for fpath in sorted(glob.glob('/opt/data/cache/scratch/altakamul-site/*.html') + glob.glob('/opt/data/cache/scratch/altakamul-site/pages/*.html')):
    fname = fpath.split('altakamul-site/')[-1]
    with open(fpath, 'r', encoding='utf-8') as f:
        p = UntranslatedFinder()
        p.feed(f.read())
    print(f"=== {fname} ({len(p.nodes)} items) ===")
    for tag, text in p.nodes:
        print(f"  [{tag}] {text}")
