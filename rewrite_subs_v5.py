import glob
import re
import os

menus = {
    '01': {
        'title': '회사소개',
        'en_title': 'COMPANY',
        'items': {
            '0101': ('인사말', '신뢰를 바탕으로 최상의 안전진단 서비스를 제공합니다.', 'fa-user-tie'),
            '0102': ('연혁', '(주)한강엔지니어링이 걸어온 발자취를 소개합니다.', 'fa-calendar-alt'),
            '0103': ('주요실적', '수많은 공공기관 및 민간 기업과 함께하며 축적된 노하우', 'fa-list-alt'),
            '0104': ('오시는길', '찾아오시는 길을 상세히 안내해 드립니다.', 'fa-map-marked-alt')
        }
    },
    '02': {
        'title': '업무분야',
        'en_title': 'BUSINESS',
        'items': {
            '0201': ('안전진단', '건축물의 구조적 안전성을 정밀하게 진단합니다.', 'fa-search'),
            '0202': ('안전점검', '사고 예방을 위한 철저한 안전점검 서비스', 'fa-clipboard-check'),
            '0203': ('건축물관리점검', '정기적인 점검을 통해 건축물의 수명을 연장합니다.', 'fa-building'),
            '0204': ('건설공사 정기안전점검', '건설 현장의 안전을 책임지는 정기 점검', 'fa-hard-hat'),
            '0205': ('내진성능평가', '지진으로부터 안전한 건축물을 위한 내진성능평가', 'fa-house-crack'),
            '0206': ('법원감정', '정확하고 객관적인 법원 감정 서비스', 'fa-scale-balanced'),
            '0207': ('인접건축물 사전조사', '공사 전 인접 건축물의 상태를 면밀히 조사합니다.', 'fa-search-location'),
            '0208': ('구조설계/감리', '안전하고 경제적인 구조설계 및 감리', 'fa-drafting-compass'),
            '0209': ('시설물보수/보강공사', '진단 결과를 바탕으로 한 최적의 보수·보강 솔루션', 'fa-tools')
        }
    },
    '03': {
        'title': '인증 및 장비현황',
        'en_title': 'CERTIFICATE',
        'items': {
            '0301': ('인증현황', '국가 공인 안전진단 전문기관의 확실한 자격증명', 'fa-certificate'),
            '0302': ('장비보유현황', '정밀한 진단을 위한 최첨단 측정 및 검사 장비 보유', 'fa-microscope')
        }
    },
    '04': {
        'title': '고객센터',
        'en_title': 'CUSTOMER',
        'items': {
            '0401': ('공지사항', '새로운 소식과 유용한 정보를 확인하세요.', 'fa-bullhorn'),
            '0402': ('견적문의', '전문가가 빠르고 정확하게 견적을 상담해 드립니다.', 'fa-file-invoice-dollar')
        }
    }
}

def get_menu_info(page_id):
    top_id = page_id[:2]
    if top_id in menus:
        cat = menus[top_id]
        title = cat['title']
        en_title = cat.get('en_title', 'SUBPAGE')
        if page_id in cat['items']:
            item = cat['items'][page_id]
        else:
            item = ('메뉴', '설명', 'fa-chevron-right')
        sidebar_items = {k: v for k, v in cat['items'].items()}
        return title, en_title, item[0], item[1], sidebar_items, top_id
    return "메뉴", "MENU", "페이지", "설명", {}, "00"

with open('f:/website3/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()
mega_header = idx_content[idx_content.find('<!-- Mobile Overlay -->'):idx_content.find('</header>')+9]
mega_header += '\\n<div class="mega-overlay"></div>'

new_footer = """
</div> <!-- End wrapper -->

<!-- Footer -->
<footer id="footer">
    <div class="container">
        <div class="footer-inner">
            <div class="f-info">
                <div class="f-logo">
                    <img src="./img/logo.png" alt="(주)한강엔지니어링">
                </div>
                <p><strong>대표 :</strong> 우상진 &nbsp;|&nbsp; <strong>사업자등록번호 :</strong> 212-81-91777</p>
                <p><strong>본사 :</strong> 서울시 성동구 연무장5가길 7 현대테라스타워 W동 1006호</p>
                <p><strong>TEL :</strong> 02-6959-0729 &nbsp;|&nbsp; <strong>FAX :</strong> 02-6959-0730 &nbsp;|&nbsp; <strong>Mobile :</strong> 010-9700-2926 &nbsp;|&nbsp; <strong>E-mail :</strong> hangang0730@daum.net</p>
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
    filename = os.path.basename(filepath)
    page_id = filename.replace('sub_', '').replace('.html', '')
    
    # Skip 0101 as it was manually finalized
    if page_id == '0101':
        continue
    
    # We only process main pages like 0102, 0401, not _part files (although they might be globbed if not careful, but there are no part files in original structure we just care about top level)
    if '_' in page_id:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # EXTRACT ORIGINAL CONTENT SAFELY
    main_start = content.find('<main class="sub-content content-body')
    if main_start == -1:
        # Some boards might not have it exactly? Let's check
        main_start = content.find('<main')
    
    if main_start != -1:
        main_start = content.find('>', main_start) + 1
    else:
        # Fallback if no main tag
        main_start = content.find('</aside>') + 8
        
    cta_start = content.find('<!-- Bottom CTA -->')
    if cta_start == -1:
        cta_start = content.find('</main>', main_start)
        if cta_start == -1:
            cta_start = len(content)

    extracted_html = content[main_start:cta_start].strip()
    
    # Clean up garbage tags at the end of extracted content
    while extracted_html.endswith('</div>') or extracted_html.endswith('</main>'):
        if extracted_html.endswith('</div>'):
            extracted_html = extracted_html[:-6].strip()
        elif extracted_html.endswith('</main>'):
            extracted_html = extracted_html[:-7].strip()

    # GENERATE NEW STRUCTURE
    cat_title, en_title, sub_title, lead_text, sub_items, cat_id = get_menu_info(page_id)
    
    sidebar_items_html = ""
    for k, v in sub_items.items():
        link = f"./sub_{k}.html"
        active_class = "active" if k == page_id else ""
        sidebar_items_html += f'<li class="{active_class}"><a href="{link}"><i class="fas {v[2]}"></i> <span>{v[0]}</span></a></li>\\n                '

    new_body = mega_header + f"""
<div id="wrapper">
    <div class="subpage-new-layout">
        <aside class="sidebar-new">
            <div class="sidebar-header">
                <h2>{cat_title}</h2>
                <span class="en">{en_title}</span>
            </div>
            <ul class="sidebar-menu-new">
                {sidebar_items_html}
            </ul>
            <div class="sidebar-contact">
                <div class="contact-icon"><i class="fas fa-headset"></i></div>
                <h3>문의안내</h3>
                <p>궁금하신 사항을<br>친절히 안내해 드립니다.</p>
                <div class="phone">02-6959-0729</div>
                <div class="hours">평일 09:00 - 18:00</div>
            </div>
        </aside>

        <div class="content-wrapper">
            <div class="breadcrumb-new">
                <i class="fas fa-home"></i> &gt; <span>{cat_title}</span> &gt; <span class="current">{sub_title}</span>
            </div>
            
            <main class="content-main">
{extracted_html}
            </main>
        </div>
    </div>

    <!-- Bottom CTA -->
    <div class="sub-contact-cta">
        <div class="container">
            <div class="cta-inner fade-up">
                <h2>고객 만족을 위한 빠른 문의</h2>
                <div class="cta-actions">
                    <a href="tel:02-6959-0729" class="btn btn-outline-white"><i class="fas fa-phone"></i> 02-6959-0729</a>
                    <a href="mailto:hangang0730@daum.net" class="btn btn-outline-white"><i class="fas fa-envelope"></i> hangang0730@daum.net</a>
                    <a href="./sub_0402.html" class="btn btn-point"><i class="fas fa-file-invoice"></i> 온라인 견적 양식 작성</a>
                </div>
            </div>
        </div>
    </div>
""" + new_footer

    head_start = content.find('<head>')
    head_end = content.find('</head>')
    
    # Re-inject body
    body_start = content.find('<body')
    body_start = content.find('>', body_start) + 1
    
    final_content = content[:body_start] + '\\n' + new_body + '\\n</body>\\n</html>'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)

print("V5 Safe Extraction Update complete.")
