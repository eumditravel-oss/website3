import urllib.request
from bs4 import BeautifulSoup
import re

url = 'http://sinyoungscm.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print("=== CSS FILES ===")
for link in soup.find_all('link', rel='stylesheet'):
    print(link.get('href'))

print("\n=== JS FILES ===")
for script in soup.find_all('script'):
    src = script.get('src')
    if src:
        print(src)

print("\n=== MEGA MENU DUMP ===")
gnb = soup.find('nav', id='gnb')
if gnb:
    for li1 in gnb.find_all('li', class_='gnb_1dli'):
        a1 = li1.find('a', class_='gnb_1da')
        if a1:
            print(f"- {a1.text.strip()} ({a1.get('href')})")
            ul2 = li1.find('ul')
            if ul2:
                for li2 in ul2.find_all('li', class_='gnb_2dli'):
                    a2 = li2.find('a', class_='gnb_2da')
                    if a2:
                        print(f"  └─ {a2.text.strip()} ({a2.get('href')})")
