import os
import re
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

html_files = [
    "index.html", "about_greeting.html", "about_history.html", "about_projects.html", "about_location.html",
    "business_01.html", "business_02.html", "business_03.html", "business_04.html", "business_05.html",
    "business_06.html", "business_07.html", "business_08.html", "business_09.html",
    "cert_01.html", "cert_02.html", "notice.html", "inquiry.html"
]

def download_and_patch_asset(url):
    if not url.startswith("http://sinyoungscm.com"):
        return url
    
    # Strip domain to get local path
    local_path = url.replace("http://sinyoungscm.com", "").split('?')[0]
    if local_path.startswith('/'):
        local_path = local_path[1:]
    
    # Only download css and js
    if not (local_path.endswith('.css') or local_path.endswith('.js')):
        return url

    # Make directories
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    if not os.path.exists(local_path):
        print(f"Downloading {url} to {local_path}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(req, context=ctx)
            content = response.read().decode('utf-8', errors='ignore')
            
            # If CSS, patch url(...)
            if local_path.endswith('.css'):
                # Patch relative URLs in CSS (like url('../img/bg.png'))
                # We will convert them to absolute http://sinyoungscm.com/... URLs to be safe
                # First, find all url()
                def replacer(match):
                    asset_url = match.group(1).strip("'\"")
                    if asset_url.startswith('http') or asset_url.startswith('data:'):
                        return match.group(0)
                    
                    # Resolve relative URL against the CSS file's URL
                    # e.g., css url is http://sinyoungscm.com/theme/basic/css/default.css
                    # asset_url is ../img/bg.png
                    from urllib.parse import urljoin
                    absolute_url = urljoin(url, asset_url)
                    return f"url('{absolute_url}')"
                
                content = re.sub(r'url\(([^)]+)\)', replacer, content)
                
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return url
    
    # Return the new local path relative to root
    return local_path

for html_file in html_files:
    if not os.path.exists(html_file):
        continue
        
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    # Find all http://sinyoungscm.com/....(css|js)
    # We will replace them in the HTML
    
    def html_replacer(match):
        full_url = match.group(1)
        if not full_url.startswith("http://sinyoungscm.com"):
            return match.group(0)
        new_path = download_and_patch_asset(full_url)
        return match.group(0).replace(full_url, new_path)
    
    # match href="..." and src="..."
    html_content = re.sub(r'href="([^"]+\.css[^"]*)"', html_replacer, html_content)
    html_content = re.sub(r'src="([^"]+\.js[^"]*)"', html_replacer, html_content)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Asset downloading and patching complete.")
