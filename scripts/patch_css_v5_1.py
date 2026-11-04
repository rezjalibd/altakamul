import re

CSS_PATH = '/opt/data/cache/scratch/altakamul-site/css/style.css'

with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add complete Grid & Spacing definitions if missing
grid_patch = '''
/* --- Comprehensive Cards Grids & Spacing System (v5.1) --- */
.cards-grid-4 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr));
  gap: 24px;
  margin-top: 24px;
  margin-bottom: 48px;
}

.cards-grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr));
  gap: 28px;
  margin-top: 24px;
  margin-bottom: 48px;
}

.cards-grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 460px), 1fr));
  gap: 28px;
  margin-top: 24px;
  margin-bottom: 48px;
}

.vertical-cards-stack {
  display: flex;
  flex-direction: column;
  gap: 28px;
  margin-top: 24px;
  margin-bottom: 48px;
}

/* Stats Grid for Hero & Hubs Sections */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin-top: 36px;
  margin-bottom: 56px;
  width: 100%;
}

@media (max-width: 991px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin-bottom: 40px;
  }
}

@media (max-width: 540px) {
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 14px;
  }
}

.stat-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 18px;
  padding: 24px 20px;
  text-align: center;
  transition: transform 220ms var(--ease-out), border-color 220ms ease, box-shadow 220ms ease;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.stat-card:hover {
  border-color: var(--primary-gold);
  transform: translateY(-4px);
  box-shadow: 0 12px 30px var(--card-glow);
}

.stat-card .stat-val {
  font-size: 1.85rem;
  font-weight: 900;
  color: var(--primary-gold);
  margin-bottom: 8px;
  line-height: 1.15;
}

.stat-card .stat-label {
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--text-secondary);
  line-height: 1.5;
}

/* Enhanced Subpage Hero Architecture */
.subpage-hero {
  padding: 44px 0 28px;
  text-align: center;
  position: relative;
  width: 100%;
}

.subpage-hero .section-header {
  max-width: 860px;
  margin: 0 auto 32px;
}

.subpage-hero .section-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 18px;
  border-radius: 999px;
  background: rgba(197, 160, 89, 0.12);
  border: 1px solid var(--border-gold);
  color: var(--primary-gold);
  font-size: 0.85rem;
  font-weight: 700;
  margin-bottom: 18px;
}

.subpage-hero .section-title {
  font-size: clamp(1.85rem, 3.5vw, 2.65rem);
  font-weight: 900;
  color: var(--text-primary);
  line-height: 1.35;
  margin-bottom: 16px;
}

.subpage-hero .section-sub {
  font-size: clamp(0.98rem, 1.6vw, 1.12rem);
  color: var(--text-secondary);
  line-height: 1.85;
  max-width: 740px;
  margin: 0 auto;
}

/* Legal Documents Structure (Privacy & Terms) */
.legal-document-container {
  max-width: 960px;
  margin: 0 auto 60px;
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.legal-section-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 20px;
  padding: 36px 32px;
  box-shadow: var(--shadow-sm);
  transition: border-color 220ms ease;
}

.legal-section-card:hover {
  border-color: var(--border-gold);
}

.legal-section-card h2,
.legal-section-card h3 {
  color: var(--primary-gold);
  font-size: 1.35rem;
  font-weight: 800;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  line-height: 1.4;
}

.legal-section-card p {
  color: var(--text-secondary);
  font-size: 0.96rem;
  line-height: 1.85;
  margin-bottom: 14px;
}

.legal-section-card p:last-child {
  margin-bottom: 0;
}

.legal-section-card ul {
  list-style: none;
  padding: 0;
  margin: 14px 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.legal-section-card ul li {
  position: relative;
  padding-inline-start: 24px;
  color: var(--text-secondary);
  font-size: 0.94rem;
  line-height: 1.75;
}

.legal-section-card ul li::before {
  content: "✦";
  position: absolute;
  inset-inline-start: 0;
  color: var(--primary-gold);
  font-size: 0.85rem;
}

/* Light Mode Hardening for New System Elements */
[data-theme="light"] .stat-card {
  background: #FFFFFF !important;
  border-color: #E2E8F0 !important;
  box-shadow: 0 4px 18px rgba(11, 25, 44, 0.04) !important;
}

[data-theme="light"] .stat-card .stat-val {
  color: #9E7D3B !important;
}

[data-theme="light"] .stat-card .stat-label {
  color: #334155 !important;
}

[data-theme="light"] .legal-section-card {
  background: #FFFFFF !important;
  border-color: #E2E8F0 !important;
  box-shadow: 0 4px 20px rgba(11, 25, 44, 0.04) !important;
}

[data-theme="light"] .legal-section-card h2,
[data-theme="light"] .legal-section-card h3 {
  color: #8C651A !important;
}

[data-theme="light"] .legal-section-card p,
[data-theme="light"] .legal-section-card ul li {
  color: #334155 !important;
}
'''

# Check if already present or replace
if '/* --- Comprehensive Cards Grids & Spacing System (v5.1) --- */' not in css:
    css += '\n' + grid_patch
    with open(CSS_PATH, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Appended v5.1 CSS definitions to style.css")
else:
    print("v5.1 CSS definitions already present")
