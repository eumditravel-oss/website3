import glob
import re

files = glob.glob('f:/website3/sub_02*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to make sure both "관련법" and "실시대상" are full-width if they are currently just `service-card fade-up`.
    # Wait, any card that is just `<div class="service-card fade-up">` in a grid where there is no adjacent card to pair with
    # might be an issue. But for safety, let's just target "실시대상" and "관련법".
    
    new_content = re.sub(
        r'<div class="service-card fade-up">(\s*<div class="service-card-header">\s*<div class="service-card-icon"><i class="[^"]+"></i></div>\s*<h4>실시대상</h4>)',
        r'<div class="service-card full-width fade-up">\1',
        content
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath}")
