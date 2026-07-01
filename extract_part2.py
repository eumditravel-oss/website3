import urllib.request
import re

req = urllib.request.Request('http://sinyoungscm.com/', headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')

# Extract the main body block
body_start = html.find('<!-- 콘텐츠 시작 { -->')
if body_start == -1:
    body_start = html.find('<div id="wrapper">') # fallback

body_end = html.find('<!-- 하단 시작 { -->')
if body_end == -1:
    body_end = html.find('<div id="ft">') # fallback

body_content = html[body_start:body_end]

# Extract the slider javascripts or anything at the bottom before footer if needed
# The main page has a visual slider: <div id="visual">
# Let's ensure the whole middle section is captured.

part2 = f"<!-- Part 2: Main Body -->\n{body_content}"

# Replace URLs with absolute paths
part2 = re.sub(r'href="/(?!/)', 'href="http://sinyoungscm.com/', part2)
part2 = re.sub(r'src="/(?!/)', 'src="http://sinyoungscm.com/', part2)
part2 = re.sub(r'href="([^h/][^"]*\.css.*?)"', r'href="http://sinyoungscm.com/\1"', part2)
part2 = re.sub(r'src="([^h/][^"]*\.js.*?)"', r'src="http://sinyoungscm.com/\1"', part2)
part2 = re.sub(r"url\('/(?!/)", "url('http://sinyoungscm.com/", part2)
part2 = re.sub(r'src="img/', 'src="http://sinyoungscm.com/img/', part2)
part2 = re.sub(r"url\('img/", "url('http://sinyoungscm.com/img/", part2)

with open('f:/webpage2/part2_body.html', 'w', encoding='utf-8') as f:
    f.write(part2)

print("Part 2 successfully extracted and saved to part2_body.html")
print(f"Total size: {len(part2)} characters.")
