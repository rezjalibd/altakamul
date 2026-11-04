import re

BUILDER_PATH = '/opt/data/cache/scratch/altakamul-site/scripts/render_all_pages_v5.py'

with open(BUILDER_PATH, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the hero section tag in each build function to include subpage-hero
code = re.sub(
    r'<!-- Hero Section -->\s*<section class="section-container"[^>]*>',
    '<!-- Hero Section -->\n  <section class="section-container subpage-hero">',
    code
)

with open(BUILDER_PATH, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated render_all_pages_v5.py with subpage-hero")
