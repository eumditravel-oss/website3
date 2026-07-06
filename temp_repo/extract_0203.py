import urllib.request
import re
import html.parser
import sys

url = 'http://sinyoungscm.com/bbs/board.php?bo_table=0203'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req)
    live_html = resp.read().decode('utf-8')
except Exception as e:
    print(f"Error fetching URL: {e}")
    sys.exit(1)

# Split into 3 parts
body_start = live_html.find('<!-- 콘텐츠 시작 { -->')
if body_start == -1: body_start = live_html.find('<div id="wrapper">')
footer_start = live_html.find('<!-- 하단 시작 { -->')
if footer_start == -1: footer_start = live_html.find('<div id="ft">')

part1 = live_html[:body_start]
part2 = live_html[body_start:footer_start]
part3 = live_html[footer_start:]

# Replace relative URLs
def replace_urls(html_str):
    res = re.sub(r'href="/(?!/)', 'href="http://sinyoungscm.com/', html_str)
    res = re.sub(r'src="/(?!/)', 'src="http://sinyoungscm.com/', res)
    res = re.sub(r'href="([^h/][^"]*\.css.*?)"', r'href="http://sinyoungscm.com/\1"', res)
    res = re.sub(r'src="([^h/][^"]*\.js.*?)"', r'src="http://sinyoungscm.com/\1"', res)
    res = re.sub(r"url\('/(?!/)", "url('http://sinyoungscm.com/", res)
    
    dirs = ['theme', 'js', 'img', 'plugin', 'data', 'css', 'sub', 'editor', 'skin']
    for d in dirs:
        res = re.sub(r'href="' + d + r'/', 'href="http://sinyoungscm.com/' + d + '/', res)
        res = re.sub(r'src="' + d + r'/', 'src="http://sinyoungscm.com/' + d + '/', res)
        res = re.sub(r"url\('" + d + r'/', "url('http://sinyoungscm.com/" + d + '/', res)
        
    res = res.replace('href="../', 'href="http://sinyoungscm.com/')
    res = res.replace('src="../', 'src="http://sinyoungscm.com/')
    return res

part1_clean = replace_urls(part1)
part2_clean = "<!-- Part 2: Main Body -->\n" + replace_urls(part2)
part3_clean = replace_urls(part3)

# Write to disk
with open('f:/webpage2/sub_0203_part1.html', 'w', encoding='utf-8') as f: f.write(part1_clean)
with open('f:/webpage2/sub_0203_part2.html', 'w', encoding='utf-8') as f: f.write(part2_clean)
with open('f:/webpage2/sub_0203_part3.html', 'w', encoding='utf-8') as f: f.write(part3_clean)

combined = part1_clean + '\n' + part2_clean + '\n' + part3_clean
with open('f:/webpage2/sub_0203.html', 'w', encoding='utf-8') as f: f.write(combined)

# Integrity Check
live_html_clean = replace_urls(live_html)

class D(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.d = []
    def handle_starttag(self, tag, attrs):
        self.d.append(tag)
    def handle_endtag(self, tag):
        self.d.append('/' + tag)

l = D()
l.feed(live_html_clean)
r = D()
r.feed(combined)

match = l.d == r.d
print('DOM Match:', match)
print('Live elements count:', len(l.d))
print('Local elements count:', len(r.d))

if not match:
    for i in range(min(len(l.d), len(r.d))):
        if l.d[i] != r.d[i]:
            print(f"Mismatch at index {i}: Live={l.d[i]}, Local={r.d[i]}")
            break
