import subprocess
import glob
import re

def fix_css_and_aos():
    files = glob.glob('sub_*.html')
    files = [f for f in files if 'part' not in f and 'old' not in f]
    
    for file in files:
        # Get old head
        try:
            result = subprocess.run(['git', 'show', f'fa6fb1a~1:{file}'], capture_output=True)
            old_html = result.stdout.decode('utf-8', errors='ignore')
        except Exception as e:
            continue
            
        # Extract board skin CSS links
        links = re.findall(r'<link.*?href=[\'"]\./theme/basic/skin/board/.*?[\'"].*?>', old_html)
        
        with open(file, 'r', encoding='utf-8') as f:
            curr_html = f.read()
            
        changed = False
        
        # Inject CSS if not already there
        for link in links:
            if link not in curr_html:
                head_end = curr_html.find('</head>')
                curr_html = curr_html[:head_end] + link + '\n' + curr_html[head_end:]
                changed = True
                print(f"Injected {link} into {file}")
                
        # Fix data-aos -> class="fade-up"
        # We need to replace data-aos="fade-up" data-aos-duration="..." data-aos-delay="..."
        # with just class="fade-up" IF it doesn't already have a class.
        # But honestly, a simple regex replacement is easier:
        # If it's <div id="history" data-aos="fade-up"...>, it becomes <div id="history" class="fade-up">
        
        # Replace data-aos="fade-up" with class="fade-up"
        if 'data-aos=' in curr_html:
            curr_html = re.sub(r'data-aos="fade-up"\s*(data-aos-\w+="[^"]*"\s*)*', 'class="fade-up" ', curr_html)
            # If the element already had a class, now it will have two class attributes, e.g., class="..." class="fade-up".
            # The browser will merge them or ignore one. It's better to inject it into the existing class if possible,
            # but for our specific cases (<div id="history"> and <div>) they didn't have classes.
            # Let's fix double class manually:
            curr_html = re.sub(r'class="([^"]+)"\s*class="fade-up"', r'class="\1 fade-up"', curr_html)
            changed = True
            print(f"Fixed AOS in {file}")
            
        if changed:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(curr_html)

if __name__ == "__main__":
    fix_css_and_aos()
