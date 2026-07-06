import glob
import re

files = glob.glob('f:/website3/sub_*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add or update version parameter to redesign_main.css
    new_content = re.sub(
        r'href="\./css/redesign_main\.css(\?v=\d+)?"',
        r'href="./css/redesign_main.css?v=3"',
        content
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath}")
