import urllib.request
import re
import html.parser

req = urllib.request.Request('http://sinyoungscm.com/', headers={'User-Agent': 'Mozilla/5.0'})
live_html = urllib.request.urlopen(req).read().decode('utf-8')
local_html = open('f:/webpage2/index.html', encoding='utf-8').read()

live_html = re.sub(r'href="/(?!/)', 'href="http://sinyoungscm.com/', live_html)
live_html = re.sub(r'src="/(?!/)', 'src="http://sinyoungscm.com/', live_html)
live_html = re.sub(r'href="([^h/][^"]*\.css.*?)"', r'href="http://sinyoungscm.com/\1"', live_html)
live_html = re.sub(r'src="([^h/][^"]*\.js.*?)"', r'src="http://sinyoungscm.com/\1"', live_html)
live_html = re.sub(r"url\('/(?!/)", "url('http://sinyoungscm.com/", live_html)
live_html = re.sub(r'src="img/', 'src="http://sinyoungscm.com/img/', live_html)
live_html = re.sub(r"url\('img/", "url('http://sinyoungscm.com/img/", live_html)

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
    # Find first mismatch
    for i in range(min(len(l.d), len(r.d))):
        if l.d[i] != r.d[i]:
            print(f"Mismatch at index {i}: Live={l.d[i]}, Local={r.d[i]}")
            break
