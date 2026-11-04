import re

# 1. Update css/profile.css
CSS_PATH = "/opt/data/cache/scratch/altakamul-site/css/profile.css"
with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

# Make sure media query is strictly scoped to screen
css = css.replace("@media (max-width: 820px)", "@media screen and (max-width: 820px)")

# Write updated CSS
with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css)

print("Updated CSS media queries.")
