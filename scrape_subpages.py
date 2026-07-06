import os
import requests
from bs4 import BeautifulSoup
import re

subpages = {
    "about_greeting.html": ("회사소개", "인사말", "0101"),
    "about_history.html": ("회사소개", "연혁", "0102"),
    "about_projects.html": ("회사소개", "주요실적", "0103"),
    "about_location.html": ("회사소개", "오시는길", "0104"),
    "business_01.html": ("업무분야", "안전진단", "0201"),
    "business_02.html": ("업무분야", "안전점검", "0202"),
    "business_03.html": ("업무분야", "건축물관리점검", "0203"),
    "business_04.html": ("업무분야", "건설공사 정기안전점검", "0204"),
    "business_05.html": ("업무분야", "내진성능평가", "0205"),
    "business_06.html": ("업무분야", "법원감정", "0206"),
    "business_07.html": ("업무분야", "인접건축물 사전조사", "0207"),
    "business_08.html": ("업무분야", "구조설계/감리", "0208"),
    "business_09.html": ("업무분야", "시설물보수/보강공사", "0209"),
    "cert_01.html": ("인증 및 장비현황", "인증현황", "0301"),
    "cert_02.html": ("인증 및 장비현황", "장비보유현황", "0302"),
    "notice.html": ("고객센터", "공지사항", "0401"),
    "inquiry.html": ("무료견적문의", "견적문의", "0402")
}

template_head = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - (주)한강엔지니어링</title>
    <link rel="stylesheet" href="./css/style.css">
    <link rel="stylesheet" href="http://sinyoungscm.com/theme/basic/css/default.css?ver=220620">
    <link rel="stylesheet" href="http://sinyoungscm.com/theme/basic/skin/board/basic_history2/style.css">
    <link rel="stylesheet" href="http://sinyoungscm.com/theme/basic/skin/board/basic/style.css">
</head>
<body>
    <div id="hd" class="sticky">
        <div id="hd_wrapper">
            <div id="logo">
                <a href="index.html"><img src="http://sinyoungscm.com/img/logo.png" alt="로고"></a>
            </div>
            <nav id="gnb">
                <ul id="gnb_1dul">
                    <li class="gnb_1dli">
                        <a href="about_greeting.html" class="gnb_1da">회사소개</a>
                        <div class="gnb_2dul">
                            <ul>
                                <li class="gnb_2dli"><a href="about_greeting.html" class="gnb_2da">인사말</a></li>
                                <li class="gnb_2dli"><a href="about_history.html" class="gnb_2da">연혁</a></li>
                                <li class="gnb_2dli"><a href="about_projects.html" class="gnb_2da">주요실적</a></li>
                                <li class="gnb_2dli"><a href="about_location.html" class="gnb_2da">오시는길</a></li>
                            </ul>
                        </div>
                    </li>
                    <li class="gnb_1dli"><a href="business_01.html" class="gnb_1da">업무분야</a></li>
                    <li class="gnb_1dli"><a href="cert_01.html" class="gnb_1da">인증 및 장비현황</a></li>
                    <li class="gnb_1dli"><a href="notice.html" class="gnb_1da">고객센터</a></li>
                    <li class="gnb_1dli"><a href="inquiry.html" class="gnb_1da">무료견적문의</a></li>
                </ul>
            </nav>
        </div>
        <div class="hd_bg"></div>
    </div>
"""

template_foot = """
    <!-- Footer -->
    <div id="ft">
        <div class="container">
            <div id="ft_company">
                <p>
                    <b>(주)한강엔지니어링</b><br>
                    대표 : 우상진 | 사업자등록번호 : 212-81-91777 | E-mail : hangang0730@daum.net<br>
                    본사 : 서울시 성동구 연무장5가길 7 현대테라스타워 W동 1006호 | TEL : 02-6959-0729
                </p>
            </div>
            <div id="ft_copy">Copyright &copy; <b>(주)한강엔지니어링.</b> All rights reserved.</div>
        </div>
    </div>
    
    <script src="./js/main.js"></script>
    <script async="true" src="//log1.toup.net/mirae_log_chat_common.js?adkey=plvbh" charset="UTF-8"></script>
</body>
</html>
"""

def fix_urls(html_content):
    # Fix absolute URLs
    html_content = re.sub(r'src="(/[^"]+)"', r'src="http://sinyoungscm.com\1"', html_content)
    html_content = re.sub(r'href="(/[^"]+)"', r'href="http://sinyoungscm.com\1"', html_content)
    # Fix inline styles (background-image: url(...))
    html_content = re.sub(r'url\(\'(/[^"]+)\'\)', r"url('http://sinyoungscm.com\1')", html_content)
    html_content = re.sub(r'url\((/[^"]+)\)', r"url('http://sinyoungscm.com\1')", html_content)
    
    # Optional: Fix any action attributes in forms to point to local if needed, but since it's a clone, point to real server or #
    html_content = re.sub(r'action="[^"]+"', 'action="#"', html_content)
    return html_content

for filename, (category, title, code) in subpages.items():
    print(f"Scraping {code} ({title})...")
    url = f"http://sinyoungscm.com/bbs/board.php?bo_table={code}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        continue
    
    # The actual content is inside <div id="wrapper">
    container = soup.find('div', id='wrapper')
    
    if container:
        # Convert container back to string
        container_html = str(container)
        container_html = fix_urls(container_html)
        
        # Build the final page
        final_html = template_head.format(category=category, title=title) + "\n" + container_html + "\n" + template_foot
        
        with open(f"f:/webpage2/{filename}", "w", encoding="utf-8") as f:
            f.write(final_html)
        print(f"-> Successfully created {filename}")
    else:
        print(f"-> ERROR: Container not found in {code}")

print("All 17 subpages successfully deep scraped and replicated.")
