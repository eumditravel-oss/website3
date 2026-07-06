import urllib.request
from bs4 import BeautifulSoup
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

pages = {
    "index.html": "",
    "about_greeting.html": "0101",
    "about_history.html": "0102",
    "about_projects.html": "0103",
    "about_location.html": "0104",
    "business_01.html": "0201",
    "business_02.html": "0202",
    "business_03.html": "0203",
    "business_04.html": "0204",
    "business_05.html": "0205",
    "business_06.html": "0206",
    "business_07.html": "0207",
    "business_08.html": "0208",
    "business_09.html": "0209",
    "cert_01.html": "0301",
    "cert_02.html": "0302",
    "notice.html": "0401",
    "inquiry.html": "0402"
}

def patch_html(html_str):
    # Patch assets to absolute URL
    html_str = re.sub(r'(src|href)="/([^"]+)"', r'\1="http://sinyoungscm.com/\2"', html_str)
    # Patch inline CSS url(/img/...) to absolute URL
    html_str = re.sub(r'url\([\'"]?/([^\'")]+)[\'"]?\)', r'url(http://sinyoungscm.com/\1)', html_str)
    
    # Patch routing links to local HTML files
    for local_file, bo_table in pages.items():
        if bo_table:
            # Match both with and without the domain, but since we already patched absolute URLs above:
            html_str = re.sub(f'http://sinyoungscm.com/bbs/board.php\\?bo_table={bo_table}(&amp;sca=[^"]+)?', local_file, html_str)
            html_str = re.sub(f'/bbs/board.php\\?bo_table={bo_table}(&amp;sca=[^"]+)?', local_file, html_str)
            
    # Fix the home link
    html_str = re.sub(r'href="http://sinyoungscm.com/?"', 'href="index.html"', html_str)
    return html_str

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

for local_file, bo_table in pages.items():
    print(f"Hard-cloning {local_file}...")
    url = f"http://sinyoungscm.com/bbs/board.php?bo_table={bo_table}" if bo_table else "http://sinyoungscm.com/"
    
    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req, context=ctx)
        raw_html = response.read().decode('utf-8')
        
        patched_html = patch_html(raw_html)
        
        with open(f"f:/webpage2/{local_file}", "w", encoding="utf-8") as f:
            f.write(patched_html)
        print(f" -> Success")
    except Exception as e:
        print(f" -> Failed: {e}")
