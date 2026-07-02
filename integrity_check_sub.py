import urllib.request
import re
import html.parser

url = 'http://sinyoungscm.com/bbs/board.php?bo_table=0101'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
live_html = urllib.request.urlopen(req).read().decode('utf-8')
local_html = open('f:/webpage2/sub_0101.html', encoding='utf-8').read()

# Apply identical rules to live_html so we can compare structural DOM elements
live_html = re.sub(r'href="/(?!/)', 'href="http://sinyoungscm.com/', live_html)
live_html = re.sub(r'src="/(?!/)', 'src="http://sinyoungscm.com/', live_html)
live_html = re.sub(r'href="([^h/][^"]*\.css.*?)"', r'href="http://sinyoungscm.com/\1"', live_html)
live_html = re.sub(r'src="([^h/][^"]*\.js.*?)"', r'src="http://sinyoungscm.com/\1"', live_html)
live_html = re.sub(r"url\('/(?!/)", "url('http://sinyoungscm.com/", live_html)

dirs = ['theme', 'js', 'img', 'plugin', 'data', 'css', 'sub', 'editor']
for d in dirs:
    live_html = re.sub(r'href="' + d + r'/', 'href="http://sinyoungscm.com/' + d + '/', live_html)
    live_html = re.sub(r'src="' + d + r'/', 'src="http://sinyoungscm.com/' + d + '/', live_html)
    live_html = re.sub(r"url\('" + d + r'/', "url('http://sinyoungscm.com/" + d + '/', live_html)
    
live_html = live_html.replace('href="../', 'href="http://sinyoungscm.com/')
live_html = live_html.replace('src="../', 'src="http://sinyoungscm.com/')

class D(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.d = []
    def handle_starttag(self, tag, attrs):
        self.d.append(tag)
    def handle_endtag(self, tag):
        self.d.append('/' + tag)

l = D()
l.feed(live_html)
r = D()
r.feed(local_html)

match = l.d == r.d
print('DOM Match:', match)
print('Live elements count:', len(l.d))
print('Local elements count:', len(r.d))

if not match:
    for i in range(min(len(l.d), len(r.d))):
        if l.d[i] != r.d[i]:
            print(f"Mismatch at index {i}: Live={l.d[i]}, Local={r.d[i]}")
            break
