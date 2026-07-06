import os
import re
import urllib.request
import urllib.parse

base_dir = "f:/webpage2"
downloaded = set()

def download_file(url, local_path):
    if local_path in downloaded: return
    if os.path.exists(local_path):
        downloaded.add(local_path)
        return
    
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        print(f"Downloading {url} -> {local_path}")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        downloaded.add(local_path)
    except Exception as e:
        print(f"Failed {url}: {e}")

def process_css(css_path, base_url):
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        try:
            with open(css_path, 'r', encoding='euc-kr') as f:
                content = f.read()
        except:
            return
            
    urls = re.findall(r'url\([\'"]?(.*?)[\'"]?\)', content)
    for u in urls:
        if u.startswith('data:') or u.startswith('#'): continue
        
        full_url = urllib.parse.urljoin(base_url, u).split('#')[0].split('?')[0]
        if not full_url.startswith('http://sinyoungscm.com/'):
            continue
            
        rel_path = urllib.parse.urlparse(full_url).path
        if rel_path.startswith('/'): rel_path = rel_path[1:]
        local_target = os.path.normpath(os.path.join(base_dir, rel_path))
        
        full_url_clean = 'http://sinyoungscm.com/' + rel_path
        download_file(full_url_clean, local_target)

print("Starting to process HTML files...")

# 1. Process all HTML files
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(base_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find all http://sinyoungscm.com/... URLs ending with asset extensions
    pattern = r'http://sinyoungscm\.com/([^"\'\)\s>]+\.(?:css|js|png|jpg|jpeg|gif|svg|woff|woff2|eot|ttf|ico))(?:[\?][^"\'\)\s>]*)?'
    
    def replacer(match):
        full_url_with_query = match.group(0)
        rel_path = match.group(1)
        
        # Clean URL and local target
        full_url_clean = 'http://sinyoungscm.com/' + rel_path
        local_target = os.path.normpath(os.path.join(base_dir, rel_path))
        
        download_file(full_url_clean, local_target)
            
        # Return relative path for HTML
        return "./" + rel_path

    new_content = re.sub(pattern, replacer, content)
    
    # Let's also catch 'theme/', 'img/', 'data/' urls that might not have extensions but are directories (rare)
    # Actually, we already replaced everything with absolute. Let's stick to files.
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("HTML processing and initial asset downloading finished.")

# 2. Process all downloaded CSS files to get fonts and background images
print("Scanning downloaded CSS files for inner assets...")
css_files = []
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.css'):
            css_files.append(os.path.join(root, file))

for css_file in css_files:
    rel = os.path.relpath(css_file, base_dir).replace('\\', '/')
    base_url = 'http://sinyoungscm.com/' + rel
    process_css(css_file, base_url)

# Second pass for CSS files downloaded from the first pass
for css_file in css_files:
    rel = os.path.relpath(css_file, base_dir).replace('\\', '/')
    base_url = 'http://sinyoungscm.com/' + rel
    process_css(css_file, base_url)

print("All tasks completed.")
