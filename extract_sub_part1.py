import urllib.request
import re

url = 'http://sinyoungscm.com/bbs/board.php?bo_table=0101'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')

# Extract head
head_match = re.search(r'<head>.*?</head>', html, re.DOTALL)
head = head_match.group(0) if head_match else ""

# Extract from <body> to just before content starts
body_to_content_start = html.find('<body>')
content_start = html.find('<!-- 콘텐츠 시작 { -->')
if content_start == -1:
    content_start = html.find('<div id="wrapper">')

body_to_content = html[body_to_content_start:content_start]

part1 = f"<!doctype html>\n<html lang=\"ko\">\n{head}\n{body_to_content}"

# Replace URLs with absolute paths
part1 = re.sub(r'href="/(?!/)', 'href="http://sinyoungscm.com/', part1)
part1 = re.sub(r'src="/(?!/)', 'src="http://sinyoungscm.com/', part1)
part1 = re.sub(r'href="([^h/][^"]*\.css.*?)"', r'href="http://sinyoungscm.com/bbs/\1"', part1) # In subpage, relative urls might point differently? 
# Actually, let's fix relative URLs properly based on absolute paths.
# If they start with theme/, js/, img/, plugin/, etc.
part1 = re.sub(r'href="(theme/[^"]+)"', r'href="http://sinyoungscm.com/\1"', part1)
part1 = re.sub(r'src="(js/[^"]+)"', r'src="http://sinyoungscm.com/\1"', part1)
part1 = re.sub(r'href="(js/[^"]+)"', r'href="http://sinyoungscm.com/\1"', part1)
part1 = re.sub(r'src="(theme/[^"]+)"', r'src="http://sinyoungscm.com/\1"', part1)
part1 = re.sub(r'href="(\.\./[^"]+)"', r'href="http://sinyoungscm.com/\1"', part1) # .. resolving
part1 = part1.replace('href="http://sinyoungscm.com/../', 'href="http://sinyoungscm.com/')

# For URL that starts with just filename like 'style.css', they are relative to /bbs/
# But wait, in the subpage, css links might be like `<link rel="stylesheet" href="http://sinyoungscm.com/theme/basic/css/default.css?ver=220620">`
# Let's just use the absolute regex for common dirs
dirs = ['theme', 'js', 'img', 'plugin', 'data', 'css', 'sub']
for d in dirs:
    part1 = re.sub(r'href="' + d + r'/', 'href="http://sinyoungscm.com/' + d + '/', part1)
    part1 = re.sub(r'src="' + d + r'/', 'src="http://sinyoungscm.com/' + d + '/', part1)
    part1 = re.sub(r"url\('" + d + r'/', "url('http://sinyoungscm.com/" + d + '/', part1)

with open('f:/webpage2/sub_part1_header.html', 'w', encoding='utf-8') as f:
    f.write(part1)

print("Sub Part 1 successfully extracted and saved to sub_part1_header.html")
print(f"Total size: {len(part1)} characters.")
