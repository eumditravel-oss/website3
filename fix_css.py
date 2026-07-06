import re

with open('f:/website3/css/redesign_main.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace .service-grid
content = re.sub(
    r'\.service-grid\s*\{\s*display:\s*grid;\s*grid-template-columns:\s*repeat\(2,\s*1fr\);\s*gap:\s*30px;\s*\}',
    r'.service-grid {\n    display: flex;\n    flex-wrap: wrap;\n    gap: 30px;\n}',
    content
)

# Replace .service-card
content = re.sub(
    r'\.service-card\s*\{\s*background:\s*var\(--color-bg-white\);',
    r'.service-card {\n    flex: 1 1 calc(50% - 15px);\n    width: 100%;\n    min-width: 300px;\n    background: var(--color-bg-white);',
    content
)

# Replace .service-card.two-cols
content = re.sub(
    r'\.service-card\.two-cols\s*\{\s*grid-column:\s*1\s*/\s*-1;\s*\}',
    r'.service-card.two-cols,\n.service-card.full-width {\n    flex: 1 1 100%;\n}',
    content
)

# Replace .service-grid mobile fallback
content = re.sub(
    r'@media\s*\(\s*max-width:\s*1024px\s*\)\s*\{\s*\.service-grid\s*\{\s*grid-template-columns:\s*1fr;\s*\}\s*\}',
    r'@media (max-width: 1024px) {\n    .service-grid {\n        flex-direction: column;\n    }\n}',
    content
)

with open('f:/website3/css/redesign_main.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done replacing.")
