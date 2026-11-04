from generate_all_subpages_v5 import get_header, get_footer
import os, re

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'
PAGES_DIR = os.path.join(BASE_DIR, 'pages')

other_pages = ['404.html', 'terms.html', 'privacy.html', 'thank-you.html']

new_header = get_header(is_root=False)
new_footer = get_footer(is_root=False)

for p in other_pages:
    fpath = os.path.join(PAGES_DIR, p)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Header & Drawer
    html = re.sub(r'<!-- Site Header -->.*?<!-- /Mobile Drawer -->', new_header + '\n  <!-- /Mobile Drawer -->', html, flags=re.DOTALL)
    if '<!-- /Mobile Drawer -->' not in html:
        html = re.sub(r'<!-- Site Header -->.*?</aside>', new_header, html, flags=re.DOTALL)

    # Update Footer
    html = re.sub(r'<!-- Mobile Sticky CTA Bar -->.*?</html>', new_footer, html, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated header and footer for {p}")

print("All peripheral pages updated!")
