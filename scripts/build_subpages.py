import os, glob, re
from generate_pages import get_header, get_footer

BASE_DIR = '/opt/data/cache/scratch/altakamul-site'
PAGES_DIR = os.path.join(BASE_DIR, 'pages')

header_html = get_header(is_root=False)
footer_html = get_footer(is_root=False)

head_scripts = '''  <!-- Synchronous In-Memory Locale Engine -->
  <script src="../js/translations_data.js"></script>
  <script src="../js/main.js?v=4.0"></script>'''

for fpath in glob.glob(os.path.join(PAGES_DIR, '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Head scripts
    if 'translations_data.js' not in content:
        content = re.sub(r'<script src=\"\.\./js/main\.js[^\"]*\"></script>', head_scripts, content)
    else:
        content = re.sub(r'<script src=\"\.\./js/main\.js[^\"]*\"></script>', '<script src="../js/main.js?v=4.0"></script>', content)

    # 2. Update Header & Drawer
    # Replace header and drawer
    content = re.sub(r'<!-- Site Header -->.*?<main class=\"main-wrapper\">', header_html + '\n\n  <main class="main-wrapper">', content, flags=re.DOTALL)

    # 3. Update Footer, Mobile Sticky CTA & Back to top
    content = re.sub(r'<!-- Mobile Sticky CTA Bar -->.*?</html>', footer_html + '\n\n</body>\n</html>', content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated subpage:', os.path.basename(fpath))

print("All 14 subpages successfully updated with unified Header, Drawer, Footer, and Sync Translations!")
