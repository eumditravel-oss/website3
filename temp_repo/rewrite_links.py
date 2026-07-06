import os
import re

base_dir = "f:/webpage2"
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html') and f != 'test.html']

updated_count = 0

for file in html_files:
    filepath = os.path.join(base_dir, file)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file}: {e}")
        continue

    # Replace bo_table links
    def replacer(match):
        bo_table = match.group(1)
        return f'href="./sub_{bo_table}.html"'

    pattern = r'href="http://sinyoungscm\.com/bbs/board\.php\?bo_table=([a-zA-Z0-9_]+)[^"]*"'
    new_content = re.sub(pattern, replacer, content)

    # Replace home links
    new_content = re.sub(r'href="http://sinyoungscm\.com/?"', 'href="./index.html"', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated links in {file}")
        updated_count += 1

print(f"Done. Updated {updated_count} files.")
