files = [
    'f:/website3/sub_0103.html',
    'f:/website3/sub_0301.html',
    'f:/website3/sub_0302.html'
]

script_tag = '<script src="./js/portfolio.js"></script>\n</body>'

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'portfolio.js' not in content:
        content = content.replace('</body>', script_tag)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected portfolio.js into {filepath}")
    else:
        print(f"portfolio.js already in {filepath}")
