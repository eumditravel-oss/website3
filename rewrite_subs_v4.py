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
        
        # If the page_id is exactly '0401' or '0402', they might fall under '04'
        if page_id in cat['items']:
            item = cat['items'][page_id]
        else:
            item = ('메뉴', '설명', 'fa-chevron-right')
            
        sidebar_items = {k: v for k, v in cat['items'].items()}
        return title, en_title, item[0], item[1], sidebar_items, top_id
    return "메뉴", "MENU", "페이지", "설명", {}, "00"

new_head_template = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>{title}</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
<link rel="stylesheet" href="./css/redesign_main.css">
<link rel="stylesheet" href="./sub/sub.css">
<script src="./js/jquery-1.12.4.min.js"></script>
"""

with open('f:/website3/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()
mega_header = idx_content[idx_content.find('<!-- Mobile Overlay -->'):idx_content.find('</header>')+9]
mega_header += '\n<div class="mega-overlay"></div>'

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

# Dummy generic content templates
dummy_gallery = """
    <div class="info-card fade-up">
        <i class="fas fa-check-circle" style="color: var(--color-point); margin-bottom: 12px; font-size: 24px;"></i>
        <p>※ <strong>매년 수십 건 이상</strong>의 정밀 안전진단 및 점검을 성공적으로 수행하고 있습니다.</p>
    </div>
    <h3 class="section-title fade-up">최근 실적/현황 갤러리</h3>
    <div class="gallery-grid fade-up">
        <div class="gallery-card"><div class="img-wrap"><img src="./img/main01.jpg" alt="이미지"></div><div class="txt-wrap"><h4>[진단] 서울 OO 업무시설</h4><p>정밀안전진단 및 내진평가</p></div></div>
        <div class="gallery-card"><div class="img-wrap"><img src="./img/main02.jpg" alt="이미지"></div><div class="txt-wrap"><h4>[점검] 경기 OO 교육시설</h4><p>건축물 정기안전점검</p></div></div>
        <div class="gallery-card"><div class="img-wrap"><img src="./img/main03.jpg" alt="이미지"></div><div class="txt-wrap"><h4>[평가] 인천 OO 주거시설</h4><p>내진성능평가 수행</p></div></div>
        <div class="gallery-card"><div class="img-wrap"><img src="./img/main04.jpg" alt="이미지"></div><div class="txt-wrap"><h4>[조사] 강원 OO 공공시설</h4><p>인접건축물 사전조사</p></div></div>
    </div>
"""

dummy_service = """
    <div class="info-card fade-up">
        <i class="fas fa-building" style="color: var(--color-point); margin-bottom: 12px; font-size: 24px;"></i>
        <p>※ 최첨단 장비와 풍부한 경험을 갖춘 전문 기술진이 <strong>체계적이고 정밀한 서비스</strong>를 제공합니다.</p>
    </div>
    <h3 class="section-title fade-up">서비스 주요 내용</h3>
    <p class="fade-up">해당 분야에 대한 전문적인 지식과 다년간의 노하우를 바탕으로, 건축물의 현재 상태를 정확히 진단하고 최적의 솔루션을 제시합니다.</p>
    <div style="margin: 40px 0;"><img src="./img/main02.jpg" alt="서비스 이미지" style="width: 100%; border-radius: var(--radius-md); box-shadow: var(--shadow-sm);" class="fade-up"></div>
"""

sub_files = glob.glob('f:/website3/sub_*.html')

for filepath in sub_files:
    filename = os.path.basename(filepath)
    page_id = filename.replace('sub_', '').replace('.html', '')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'<title>(.*?)</title>', content)
    page_title_tag = title_match.group(1) if title_match else "(주)한강엔지니어링"
    
    cat_title, en_title, sub_title, lead_text, sub_items, cat_id = get_menu_info(page_id)
    
    is_board = page_id in ['0401', '0402']

    board_content = ""
    if is_board:
        container_start = content.find('<main class="sub-content content-body">')
        if container_start == -1: container_start = content.find('<main class="sub-content content-body fade-up">')
        if container_start != -1:
            wrapper_end = content.find('</main>', container_start)
            board_content = content[container_start:wrapper_end]
            board_content = re.sub(r'<h2 class="page-title">.*?</h2>', '', board_content, flags=re.DOTALL)
            board_content = re.sub(r'<p class="lead-text">.*?</p>', '', board_content, flags=re.DOTALL)
            board_content = re.sub(r'^<main[^>]*>\s*', '', board_content)
        else:
            container_start = content.find('<div id="container">')
            wrapper_end = content.rfind('<!-- } 콘텐츠 끝 -->')
            if wrapper_end == -1: wrapper_end = content.find('<hr>', container_start)
            board_content = content[container_start:wrapper_end]
            board_content = re.sub(r'<h2 id="container_title">.*?</h2>', '', board_content, flags=re.DOTALL)
            board_content = re.sub(r'^<div id="container">\s*', '', board_content)
            if board_content.endswith('</div>'): board_content = board_content[:-6].strip()

    main_content_html = ""
    if page_id != '0101': # 0101 will be custom replaced later or hardcoded here
        if not is_board:
            main_content_html += f'<h2 class="page-title">{sub_title}</h2>\\n<p class="lead-text">{lead_text}</p>'
        
        if is_board:
            main_content_html += board_content
        else:
            if page_id in ['0103', '0301', '0302']: main_content_html += dummy_gallery
            elif page_id.startswith('02'): main_content_html += dummy_service
            else:
                main_content_html += f'''
                    <div class="info-card fade-up">
                        <i class="fas fa-info-circle" style="color: var(--color-point); margin-bottom: 12px; font-size: 24px;"></i>
                        <p>※ 고객 여러분의 소중한 생명과 재산을 보호하기 위해 최선을 다하는 <strong>(주)한강엔지니어링</strong>입니다.</p>
                    </div>
                '''
    else:
        # GREETING PAGE CONTENT (0101) exactly as user requested
        main_content_html = """
        <div class="greeting-new-layout">
            <div class="greeting-header-new fade-up">
                <span class="en-title">GREETING</span>
                <h2>건축물의 안전과 가치를 지키는<br><strong>든든한 파트너</strong>가 되겠습니다.</h2>
            </div>
            
            <div class="greeting-body fade-up" style="transition-delay: 0.1s;">
                <div class="greeting-text">
                    <p>안녕하십니까, (주)한강엔지니어링을 찾아주신 고객 여러분 진심으로 환영합니다.</p>
                    <p>현대 사회에서 건축물과 시설물의 안전은 그 무엇과도 타협할 수 없는 최우선 가치입니다. 저희 (주)한강엔지니어링은 수년간 축적된 현장 경험과 고도의 전문 지식을 바탕으로, 우리 사회의 근간을 이루는 다양한 시설물의 정밀 안전진단 및 유지관리 서비스를 제공하고 있습니다.</p>
                    <p>고도화된 첨단 진단 장비와 정밀한 데이터 분석 시스템을 통해 육안으로 확인하기 어려운 미세한 구조적 결함까지 정확하게 짚어내며, 이를 바탕으로 가장 효율적이고 안전한 보수·보강 솔루션을 제시합니다.</p>
                    <p>단순한 점검을 넘어, 고객의 소중한 자산과 생명을 보호한다는 막중한 사명감을 가지고 매 프로젝트에 임하겠습니다. 변함없는 신뢰로 보답하는 최고의 안전진단 전문기관이 될 것을 약속드립니다.</p>
                    <p>감사합니다.</p>
                </div>
                <div class="greeting-img">
                    <img src="./img/0101_1.jpg" alt="(주)한강엔지니어링 인사말">
                </div>
            </div>

            <div class="greeting-strengths fade-up">
                <div class="strength-item">
                    <div class="icon"><i class="fas fa-shield-alt"></i></div>
                    <h4>최우선 가치, 안전</h4>
                    <p>건축물과 시설물의 안전은 그 무엇과도 타협할 수 없는 최우선 가치입니다.</p>
                </div>
                <div class="strength-item">
                    <div class="icon"><i class="fas fa-users-cog"></i></div>
                    <h4>축적된 경험과 전문성</h4>
                    <p>수년간 축적된 현장 경험과 고도의 전문 지식을 바탕으로, 다양한 시설물의 정밀 안전진단 및 유지관리 서비스를 제공합니다.</p>
                </div>
                <div class="strength-item">
                    <div class="icon"><i class="fas fa-chart-line"></i></div>
                    <h4>정확한 진단과 최적의 솔루션</h4>
                    <p>첨단 진단 장비와 정밀한 데이터 분석 시스템을 통해 육안으로 확인하기 어려운 미세한 구조적 결함까지 정확하게 짚어냅니다.</p>
                </div>
                <div class="strength-item">
                    <div class="icon"><i class="fas fa-handshake"></i></div>
                    <h4>신뢰와 책임의 약속</h4>
                    <p>고객의 소중한 자산과 생명을 보호한다는 사명감을 가지고 매 프로젝트에 임하겠습니다. 변함없는 신뢰로 보답하겠습니다.</p>
                </div>
            </div>

            <div class="greeting-footer fade-up">
                <div class="greeting-sign">
                    대표이사 <span class="sign-name">우상진</span>
                </div>
            </div>
        </div>
        """

    sidebar_items_html = ""
    for k, v in sub_items.items():
        link = f"./sub_{k}.html"
        active_class = "active" if k == page_id else ""
        sidebar_items_html += f'<li class="{active_class}"><a href="{link}"><i class="fas {v[2]}"></i> <span>{v[0]}</span></a></li>\n                '

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
                {main_content_html}
            </main>
        </div>
    </div>
""" + new_footer

    head_start = content.find('<head>')
    head_end = content.find('</head>')
    new_head = content[:head_start+6] + '\\n' + new_head_template.format(title=page_title_tag) + '\\n' + content[head_end:]
    
    body_start = new_head.find('<body')
    body_start = new_head.find('>', body_start) + 1
    
    final_content = new_head[:body_start] + '\\n' + new_body + '\\n</body>\\n</html>'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)

print("Updated sub files with V4 (sidebar left, breadcrumb right) layout.")
