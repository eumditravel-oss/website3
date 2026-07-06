import glob

html_files = glob.glob('f:/website3/**/*.html', recursive=True)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '\\n' in content:
        new_content = content.replace('\\n', '\n')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")
