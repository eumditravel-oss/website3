import glob
import re
import os

new_head_template = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>{title}</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
<link rel="stylesheet" href="./css/redesign_main.css">
<link rel="stylesheet" href="./sub/sub.css">
<!-- Subpage specific css/js for forms if needed -->
<script src="./js/jquery-1.12.4.min.js"></script>
"""

new_header = """<!-- Mobile Overlay -->
<div class="m-overlay" id="m-overlay"></div>

<!-- Mobile Navigation -->
<nav class="mobile-nav" id="mobile-nav">
    <button class="btn-close-menu" id="btn-menu-close" aria-label="메뉴 닫기">
        <i class="fas fa-times"></i>
    </button>
    <ul class="m-gnb">
        <li><a href="./sub_0101.html">회사소개</a></li>
        <li><a href="./sub_0201.html">업무분야</a></li>
        <li><a href="./sub_0301.html">인증 및 장비현황</a></li>
        <li><a href="./sub_0401.html">고객센터</a></li>
        <li><a href="./sub_0402.html">무료견적문의</a></li>
    </ul>
</nav>

<!-- Header -->
<header id="header">
    <div class="container header-inner">
        <a href="./index.html" class="logo">
            <img src="./img/logo.png" alt="(주)한강엔지니어링">
        </a>
        <ul class="gnb">
            <li><a href="./sub_0101.html">회사소개</a></li>
            <li><a href="./sub_0201.html">업무분야</a></li>
            <li><a href="./sub_0301.html">인증 및 장비현황</a></li>
            <li><a href="./sub_0401.html">고객센터</a></li>
            <li><a href="./sub_0402.html">무료견적문의</a></li>
        </ul>
        <button class="btn-mobile-menu" id="btn-menu-open" aria-label="메뉴 열기">
            <i class="fas fa-bars"></i>
        </button>
    </div>
</header>

<div id="wrapper" style="margin-top: 80px;">
"""

new_footer = """
<!-- Footer -->
<footer id="footer" style="margin-top: 80px;">
    <div class="container">
        <div class="footer-inner">
            <div class="f-info">
                <div class="f-logo">
                    <img src="./img/logo.png" alt="(주)한강엔지니어링">
                </div>
                <p><strong>대표 :</strong> 이관배 &nbsp;|&nbsp; <strong>사업자등록번호 :</strong> 212-81-91777</p>
                <p><strong>서울사무실 :</strong> 서울특별시 성동구 성수일로4길 25, 서울숲코오롱디지털타워 1차 809호</p>
                <p><strong>광명사무실 :</strong> 경기도 광명시 소하로 190, 광명G타워 B동 1314호</p>
                <p><strong>TEL :</strong> 02-484-4700 &nbsp;|&nbsp; <strong>FAX :</strong> 02-484-4750 &nbsp;|&nbsp; <strong>E-mail :</strong> scm4700@naver.com</p>
            </div>
            <div style="text-align: right; align-self: flex-end;">
                <a href="#header" class="btn btn-outline" style="border-color: rgba(255,255,255,0.2); color:#fff!important;">
                    <i class="fas fa-arrow-up"></i> 맨 위로
                </a>
            </div>
        </div>
        <div class="f-copy">
            Copyright &copy; (주)한강엔지니어링. All rights reserved.
        </div>
    </div>
</footer>
<script src="./js/redesign_motion.js"></script>
"""

sub_files = glob.glob('f:/website3/sub_*.html')

for filepath in sub_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Extract title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else "(주)한강엔지니어링"
    
    # 2. Replace head
    head_start = content.find('<head>')
    head_end = content.find('</head>')
    if head_start != -1 and head_end != -1:
        content = content[:head_start+6] + '\n' + new_head_template.format(title=title) + '\n' + content[head_end:]
    
    # 3. Replace Header (from <body> to <div id="wrapper">)
    body_match = re.search(r'<body[^>]*>', content)
    if body_match:
        body_end_idx = body_match.end()
        wrapper_idx = content.find('<div id="wrapper">', body_end_idx)
        if wrapper_idx != -1:
            wrapper_end_idx = wrapper_idx + len('<div id="wrapper">')
            content = content[:body_end_idx] + '\n' + new_header + content[wrapper_end_idx:]

    # 4. Replace Footer (from <hr> or <!-- 하단 시작 { --> to end)
    footer_idx = content.find('<!-- 하단 시작 { -->')
    if footer_idx == -1:
        footer_idx = content.find('<div id="ft">')
        
    if footer_idx != -1:
        # Also remove preceding <hr> if exists
        hr_idx = content.rfind('<hr>', 0, footer_idx)
        if hr_idx != -1 and hr_idx > footer_idx - 50:
            footer_idx = hr_idx
            
        end_body_idx = content.find('</body>', footer_idx)
        if end_body_idx != -1:
            content = content[:footer_idx] + new_footer + '\n</body>' + content[end_body_idx+7:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(sub_files)} sub files.")
