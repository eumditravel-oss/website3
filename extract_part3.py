import urllib.request
import re

req = urllib.request.Request('http://sinyoungscm.com/', headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')

# Extract the footer block
footer_start = html.find('<!-- 하단 시작 { -->')
if footer_start == -1:
    footer_start = html.find('<div id="ft">')

part3 = html[footer_start:]

# Remove trailing </html> which belongs to the wrapper/base, though keeping it is fine.
# We will just extract to the end of the file.

# Replace URLs with absolute paths
part3 = re.sub(r'href="/(?!/)', 'href="http://sinyoungscm.com/', part3)
part3 = re.sub(r'src="/(?!/)', 'src="http://sinyoungscm.com/', part3)
part3 = re.sub(r'href="([^h/][^"]*\.css.*?)"', r'href="http://sinyoungscm.com/\1"', part3)
part3 = re.sub(r'src="([^h/][^"]*\.js.*?)"', r'src="http://sinyoungscm.com/\1"', part3)
part3 = re.sub(r"url\('/(?!/)", "url('http://sinyoungscm.com/", part3)
part3 = re.sub(r'src="img/', 'src="http://sinyoungscm.com/img/', part3)
part3 = re.sub(r"url\('img/", "url('http://sinyoungscm.com/img/", part3)

with open('f:/webpage2/part3_footer.html', 'w', encoding='utf-8') as f:
    f.write(part3)

print("Part 3 successfully extracted and saved to part3_footer.html")
print(f"Total size: {len(part3)} characters.")
