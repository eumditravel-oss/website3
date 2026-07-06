import urllib.request
import re

url = 'http://sinyoungscm.com/bbs/board.php?bo_table=0101'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')

# Extract the main body block for subpage
body_start = html.find('<!-- 콘텐츠 시작 { -->')
if body_start == -1:
    body_start = html.find('<div id="wrapper">')

body_end = html.find('<!-- 하단 시작 { -->')
if body_end == -1:
    body_end = html.find('<div id="ft">')

part2 = html[body_start:body_end]
part2 = f"<!-- Part 2: Main Body -->\n{part2}"

# Relative URL replacements
part2 = re.sub(r'href="/(?!/)', 'href="http://sinyoungscm.com/', part2)
part2 = re.sub(r'src="/(?!/)', 'src="http://sinyoungscm.com/', part2)
part2 = re.sub(r'href="([^h/][^"]*\.css.*?)"', r'href="http://sinyoungscm.com/\1"', part2)
part2 = re.sub(r'src="([^h/][^"]*\.js.*?)"', r'src="http://sinyoungscm.com/\1"', part2)
part2 = re.sub(r"url\('/(?!/)", "url('http://sinyoungscm.com/", part2)

dirs = ['theme', 'js', 'img', 'plugin', 'data', 'css', 'sub', 'editor']
for d in dirs:
    part2 = re.sub(r'href="' + d + r'/', 'href="http://sinyoungscm.com/' + d + '/', part2)
    part2 = re.sub(r'src="' + d + r'/', 'src="http://sinyoungscm.com/' + d + '/', part2)
    part2 = re.sub(r"url\('" + d + r'/', "url('http://sinyoungscm.com/" + d + '/', part2)
    
part2 = part2.replace('href="../', 'href="http://sinyoungscm.com/')
part2 = part2.replace('src="../', 'src="http://sinyoungscm.com/')

with open('f:/webpage2/sub_part2_body.html', 'w', encoding='utf-8') as f:
    f.write(part2)

print("Sub Part 2 successfully extracted and saved to sub_part2_body.html")
print(f"Total size: {len(part2)} characters.")
