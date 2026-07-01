import urllib.request
import re

req = urllib.request.Request('http://sinyoungscm.com/', headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')

# Extract head
head_match = re.search(r'<head>.*?</head>', html, re.DOTALL)
head = head_match.group(0) if head_match else ""

# Extract header blocks
header1_start = html.find('<!-- 상단 시작 { -->')
header1_end = html.find('<!-- } 상단 끝 -->')
header1 = html[header1_start:header1_end + len('<!-- } 상단 끝 -->')]

header2_start = html.find('<!-- { mobile상단 시작 -->')
header2_end = html.find('<!-- } mobile상단 끝 -->')
header2 = html[header2_start:header2_end + len('<!-- } mobile상단 끝 -->')]

popup_start = html.find('<!-- 팝업레이어 시작 { -->')
popup_end = html.find('<!-- } 팝업레이어 끝 -->')
popup = html[popup_start:popup_end + len('<!-- } 팝업레이어 끝 -->')]

body_scripts_start = html.find('<script>')
body_scripts_end = html.find('</script>', body_scripts_start) + 9
body_scripts_1 = html[body_scripts_start:body_scripts_end]

# It might be easier to just extract from <body> to <!-- 콘텐츠 시작 { -->
body_to_content = html[html.find('<body>'):html.find('<!-- 콘텐츠 시작 { -->')]

part1 = f"<!doctype html>\n<html lang=\"ko\">\n{head}\n{body_to_content}"

# Replace URLs with absolute paths
part1 = re.sub(r'href="/(?!/)', 'href="http://sinyoungscm.com/', part1)
part1 = re.sub(r'src="/(?!/)', 'src="http://sinyoungscm.com/', part1)
part1 = re.sub(r'href="([^h/][^"]*\.css.*?)"', r'href="http://sinyoungscm.com/\1"', part1)
part1 = re.sub(r'src="([^h/][^"]*\.js.*?)"', r'src="http://sinyoungscm.com/\1"', part1)
part1 = re.sub(r"url\('/(?!/)", "url('http://sinyoungscm.com/", part1)
part1 = re.sub(r'src="img/', 'src="http://sinyoungscm.com/img/', part1)

with open('f:/webpage2/part1_header.html', 'w', encoding='utf-8') as f:
    f.write(part1)

print("Part 1 successfully extracted and saved to part1_header.html")
print(f"Total size: {len(part1)} characters.")
