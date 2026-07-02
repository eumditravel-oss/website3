import glob
import os

sub_files = glob.glob('f:/website3/sub_*.html')

count = 0
for filepath in sub_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The literal \n followed by spaces is what's causing the issue
    if r'\n                ' in content:
        # Replace the literal two-character string "\n" with an actual newline "\n"
        content = content.replace(r'\n                ', '\n                ')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Fixed literal \\n in {count} sub files.")
