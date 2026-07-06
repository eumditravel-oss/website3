import glob
import re

files = glob.glob('f:/website3/sub_02*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(
        r'<div class="service-card fade-up">(\s*<div class="service-card-header">\s*<div class="service-card-icon"><i class="[^"]+"></i></div>\s*<h4>관련법</h4>)',
        r'<div class="service-card full-width fade-up">\1',
        content
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath}")
