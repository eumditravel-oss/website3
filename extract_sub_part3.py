import urllib.request
import re

url = 'http://sinyoungscm.com/bbs/board.php?bo_table=0101'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')

# Extract the footer block
footer_start = html.find('<!-- 하단 시작 { -->')
if footer_start == -1:
    footer_start = html.find('<div id="ft">')

part3 = html[footer_start:]

# Replace URLs with absolute paths
part3 = re.sub(r'href="/(?!/)', 'href="http://sinyoungscm.com/', part3)
part3 = re.sub(r'src="/(?!/)', 'src="http://sinyoungscm.com/', part3)
part3 = re.sub(r'href="([^h/][^"]*\.css.*?)"', r'href="http://sinyoungscm.com/\1"', part3)
part3 = re.sub(r'src="([^h/][^"]*\.js.*?)"', r'src="http://sinyoungscm.com/\1"', part3)
part3 = re.sub(r"url\('/(?!/)", "url('http://sinyoungscm.com/", part3)
part3 = part3.replace('href="../', 'href="http://sinyoungscm.com/')
part3 = part3.replace('src="../', 'src="http://sinyoungscm.com/')

dirs = ['theme', 'js', 'img', 'plugin', 'data', 'css', 'sub', 'editor']
for d in dirs:
    part3 = re.sub(r'href="' + d + r'/', 'href="http://sinyoungscm.com/' + d + '/', part3)
    part3 = re.sub(r'src="' + d + r'/', 'src="http://sinyoungscm.com/' + d + '/', part3)

with open('f:/webpage2/sub_part3_footer.html', 'w', encoding='utf-8') as f:
    f.write(part3)

print("Sub Part 3 successfully extracted and saved to sub_part3_footer.html")
print(f"Total size: {len(part3)} characters.")
