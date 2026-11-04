from generate_all_subpages_v5 import get_header, get_footer

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'
with open(f'{BASE_DIR}/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Replace Header and Drawer in index.html
new_header_drawer = get_header(is_root=True)
# Fix logo path for index.html if needed
new_header_drawer = new_header_drawer.replace('images/logo.png', 'img/logo.png')

html = re.sub(r'<!-- Site Header -->.*?<!-- /Mobile Drawer -->', new_header_drawer + '\n  <!-- /Mobile Drawer -->', html, flags=re.DOTALL)
if '<!-- /Mobile Drawer -->' not in html:
    html = re.sub(r'<!-- Site Header -->.*?</aside>', new_header_drawer, html, flags=re.DOTALL)

# Replace Footer in index.html
new_footer = get_footer(is_root=True)
new_footer = new_footer.replace('images/logo.png', 'img/logo.png')

html = re.sub(r'<!-- Mobile Sticky CTA Bar -->.*?</html>', new_footer, html, flags=re.DOTALL)

with open(f'{BASE_DIR}/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Patched index.html header, drawer, and footer!")
