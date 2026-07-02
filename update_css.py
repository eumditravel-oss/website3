import os
import re

css_path = 'f:/website3/css/redesign_main.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# 1. Update fade-up in CSS
old_fade_up = """/* Motions */
.fade-up {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s var(--easing), transform 0.8s var(--easing);
}
.fade-up.visible {
    opacity: 1;
    transform: translateY(0);
}"""

new_fade_up = """/* Motions */
.fade-up {
    opacity: 1;
    transform: none;
    transition: opacity 0.4s var(--easing), transform 0.4s var(--easing);
}
.fade-up.js-hidden {
    opacity: 0;
    transform: translateY(12px);
}
.fade-up.visible {
    opacity: 1;
    transform: none;
}"""

if old_fade_up in css_content:
    css_content = css_content.replace(old_fade_up, new_fade_up)
else:
    # Use regex if exact match fails
    css_content = re.sub(r'\.fade-up\s*\{[^}]+\}\s*\.fade-up\.visible\s*\{[^}]+\}', new_fade_up, css_content)


# 2. Append new component styles
new_components = """
/* ==========================================================
   Subpage Content Components (Advanced)
========================================================== */
.page-title {
    font-size: 36px !important;
    font-weight: 800;
    color: var(--color-text-main) !important;
    margin-top: 0;
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--color-border);
}

.lead-text {
    font-size: 20px !important;
    line-height: 1.6 !important;
    color: var(--color-text-muted) !important;
    font-weight: 500;
    margin-bottom: 40px;
    max-width: 800px;
    word-break: keep-all;
}

.section-title {
    font-size: 24px !important;
    font-weight: 700;
    color: var(--color-text-main) !important;
    margin-top: 50px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
}
.section-title::before {
    content: '';
    display: inline-block;
    width: 4px;
    height: 24px;
    background-color: var(--color-point);
    margin-right: 12px;
    border-radius: 2px;
}

.content-body p {
    font-size: 17px !important;
    line-height: 1.7 !important;
    color: var(--color-text-muted) !important;
    max-width: 800px;
    margin-bottom: 20px;
    word-break: keep-all;
}

.info-card {
    background-color: var(--color-bg-light);
    border-radius: var(--radius-md);
    padding: 30px;
    border: 1px solid var(--color-border);
    margin: 30px 0;
    box-shadow: var(--shadow-sm);
}
.info-card p {
    margin: 0 !important;
    font-size: 16px !important;
}

.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 24px;
    margin-top: 30px;
}
.gallery-card {
    background: #fff;
    border-radius: var(--radius-md);
    border: 1px solid var(--color-border);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    transition: transform 0.3s var(--easing), box-shadow 0.3s var(--easing);
}
.gallery-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-md);
}
.gallery-card .img-wrap {
    aspect-ratio: 4/3;
    overflow: hidden;
    background: var(--color-bg-light);
}
.gallery-card .img-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s var(--easing);
}
.gallery-card:hover .img-wrap img {
    transform: scale(1.05);
}
.gallery-card .txt-wrap {
    padding: 20px;
}
.gallery-card h4 {
    font-size: 18px !important;
    margin: 0 0 8px 0;
    color: var(--color-text-main) !important;
}
.gallery-card p {
    font-size: 15px !important;
    margin: 0 !important;
    color: var(--color-text-muted) !important;
}

.modern-table {
    width: 100%;
    border-collapse: collapse;
    margin: 30px 0;
    font-size: 16px;
    text-align: left;
}
.modern-table th, .modern-table td {
    padding: 16px;
    border-bottom: 1px solid var(--color-border);
}
.modern-table th {
    background-color: var(--color-bg-light);
    font-weight: 700;
    color: var(--color-text-main);
    border-top: 2px solid var(--color-text-main);
}
.modern-table tbody tr:nth-child(even) {
    background-color: rgba(248, 250, 252, 0.5);
}
.modern-table tbody tr:hover {
    background-color: var(--color-bg-light);
}
"""

if "Subpage Content Components (Advanced)" not in css_content:
    css_content += new_components

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("CSS updated successfully.")
