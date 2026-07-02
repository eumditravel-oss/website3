import glob
import re
import os

menus = {
    '01': {
        'title': '회사소개',
        'items': {
            '0101': ('인사말', '신뢰를 바탕으로 최상의 안전진단 서비스를 제공합니다.'),
            '0102': ('연혁', '(주)신영에스씨엠이 걸어온 발자취를 소개합니다.'),
            '0103': ('주요실적', '수많은 공공기관 및 민간 기업과 함께하며 축적된 노하우'),
            '0104': ('오시는길', '찾아오시는 길을 상세히 안내해 드립니다.')
        }
    },
    '02': {
        'title': '업무분야',
        'items': {
            '0201': ('안전진단', '건축물의 구조적 안전성을 정밀하게 진단합니다.'),
            '0202': ('안전점검', '사고 예방을 위한 철저한 안전점검 서비스'),
            '0203': ('건축물관리점검', '정기적인 점검을 통해 건축물의 수명을 연장합니다.'),
            '0204': ('건설공사 정기안전점검', '건설 현장의 안전을 책임지는 정기 점검'),
            '0205': ('내진성능평가', '지진으로부터 안전한 건축물을 위한 내진성능평가'),
            '0206': ('법원감정', '정확하고 객관적인 법원 감정 서비스'),
            '0207': ('인접건축물 사전조사', '공사 전 인접 건축물의 상태를 면밀히 조사합니다.'),
            '0208': ('구조설계/감리', '안전하고 경제적인 구조설계 및 감리'),
            '0209': ('시설물보수/보강공사', '진단 결과를 바탕으로 한 최적의 보수·보강 솔루션')
        }
    },
    '03': {
        'title': '인증 및 장비현황',
        'items': {
            '0301': ('인증현황', '국가 공인 안전진단 전문기관의 확실한 자격증명'),
            '0302': ('장비보유현황', '정밀한 진단을 위한 최첨단 측정 및 검사 장비 보유')
        }
    },
    '0401': {
        'title': '고객센터',
        'items': {
            '0401': ('공지사항', '새로운 소식과 유용한 정보를 확인하세요.')
        }
    },
    '0402': {
        'title': '무료견적문의',
        'items': {
            '0402': ('견적문의', '전문가가 빠르고 정확하게 견적을 상담해 드립니다.')
        }
    }
}

def get_menu_info(page_id):
    if page_id in ['0401', '0402']:
        cat = menus[page_id]
        item = cat['items'][page_id]
        # For simplicity, extract title dictionary for sidebar
        sidebar_items = {k: v[0] for k, v in cat['items'].items()}
        return cat['title'], item[0], item[1], sidebar_items, page_id
    else:
        top_id = page_id[:2]
        if top_id in menus:
            cat = menus[top_id]
            title = cat['title']
            item = cat['items'].get(page_id, ('메뉴', '설명'))
            sidebar_items = {k: v[0] for k, v in cat['items'].items()}
            return title, item[0], item[1], sidebar_items, top_id
    return "메뉴", "페이지", "설명", {}, "00"

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

# Include the megamenu header (same as rewrite_subs_v2)
with open('f:/website3/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()
mega_header = idx_content[idx_content.find('<!-- Mobile Overlay -->'):idx_content.find('</header>')+9]
mega_header += '\n<div class="mega-overlay"></div>'

new_footer = """
    <!-- Bottom CTA -->
    <div class="sub-contact-cta">
        <div class="container">
            <div class="cta-inner fade-up">
                <h2>고객 만족을 위한 빠른 문의</h2>
                <div class="cta-actions">
                    <a href="tel:02-484-4700" class="btn btn-outline-white"><i class="fas fa-phone"></i> 02-484-4700</a>
                    <a href="mailto:scm4700@naver.com" class="btn btn-outline-white"><i class="fas fa-envelope"></i> scm4700@naver.com</a>
                    <a href="./sub_0402.html" class="btn btn-point"><i class="fas fa-file-invoice"></i> 온라인 견적 양식 작성</a>
                </div>
            </div>
        </div>
    </div>

</div> <!-- End wrapper -->

<!-- Footer -->
<footer id="footer">
    <div class="container">
        <div class="footer-inner">
            <div class="f-info">
                <div class="f-logo">
                    <img src="./img/logo.png" alt="(주)신영에스씨엠">
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
            Copyright &copy; (주)신영에스씨엠. All rights reserved.
        </div>
    </div>
</footer>
<script src="./js/redesign_motion.js"></script>
"""

# Dummy Content Templates
dummy_gallery = """
    <div class="info-card fade-up">
        <i class="fas fa-check-circle" style="color: var(--color-point); margin-bottom: 12px; font-size: 24px;"></i>
        <p>※ <strong>매년 수십 건 이상</strong>의 정밀 안전진단 및 점검을 성공적으로 수행하고 있습니다.</p>
    </div>

    <h3 class="section-title fade-up">최근 실적/현황 갤러리</h3>
    <div class="gallery-grid fade-up">
        <div class="gallery-card">
            <div class="img-wrap"><img src="./img/main01.jpg" alt="이미지"></div>
            <div class="txt-wrap">
                <h4>[진단] 서울 OO 업무시설</h4>
                <p>정밀안전진단 및 내진평가</p>
            </div>
        </div>
        <div class="gallery-card">
            <div class="img-wrap"><img src="./img/main02.jpg" alt="이미지"></div>
            <div class="txt-wrap">
                <h4>[점검] 경기 OO 교육시설</h4>
                <p>건축물 정기안전점검</p>
            </div>
        </div>
        <div class="gallery-card">
            <div class="img-wrap"><img src="./img/main03.jpg" alt="이미지"></div>
            <div class="txt-wrap">
                <h4>[평가] 인천 OO 주거시설</h4>
                <p>내진성능평가 수행</p>
            </div>
        </div>
        <div class="gallery-card">
            <div class="img-wrap"><img src="./img/main04.jpg" alt="이미지"></div>
            <div class="txt-wrap">
                <h4>[조사] 강원 OO 공공시설</h4>
                <p>인접건축물 사전조사</p>
            </div>
        </div>
    </div>
"""

dummy_service = """
    <div class="info-card fade-up">
        <i class="fas fa-building" style="color: var(--color-point); margin-bottom: 12px; font-size: 24px;"></i>
        <p>※ 최첨단 장비와 풍부한 경험을 갖춘 전문 기술진이 <strong>체계적이고 정밀한 서비스</strong>를 제공합니다.</p>
    </div>

    <h3 class="section-title fade-up">서비스 주요 내용</h3>
    <p class="fade-up">
        해당 분야에 대한 전문적인 지식과 다년간의 노하우를 바탕으로, 건축물의 현재 상태를 정확히 진단하고 최적의 솔루션을 제시합니다.
        시각적 결함뿐만 아니라 구조적 결함을 찾아내어 잠재적인 위험 요소를 사전에 제거합니다.
    </p>
    
    <div style="margin: 40px 0;">
        <img src="./img/main02.jpg" alt="서비스 이미지" style="width: 100%; border-radius: var(--radius-md); box-shadow: var(--shadow-sm);" class="fade-up">
    </div>

    <h3 class="section-title fade-up">기대 효과</h3>
    <ul class="fade-up" style="line-height: 1.8; color: var(--color-text-muted); font-size: 17px; margin-bottom: 40px;">
        <li>건축물의 내구수명 증진 및 자산가치 보존</li>
        <li>잠재적 붕괴 및 파손 위험 사전 예방을 통한 인명 보호</li>
        <li>유지관리 비용의 효율적 분배 및 절감 효과</li>
        <li>관련 법규 준수 및 법적 분쟁 예방</li>
    </ul>
"""

sub_files = glob.glob('f:/website3/sub_*.html')

for filepath in sub_files:
    filename = os.path.basename(filepath)
    page_id = filename.replace('sub_', '').replace('.html', '')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get title
    title_match = re.search(r'<title>(.*?)</title>', content)
    page_title_tag = title_match.group(1) if title_match else "(주)신영에스씨엠"
    
    cat_title, sub_title, lead_text, sub_items, cat_id = get_menu_info(page_id)
    
    # Check if it's a board page
    is_board = page_id in ['0401', '0402']

    # For board pages, we must extract the original board HTML
    # For others, we replace the content with our beautiful templates to make it look full
    
    board_content = ""
    if is_board:
        container_start = content.find('<main class="sub-content content-body">')
        if container_start == -1:
             container_start = content.find('<main class="sub-content content-body fade-up">')
             
        if container_start != -1:
            wrapper_end = content.find('</main>', container_start)
            board_content = content[container_start:wrapper_end]
            # remove existing title and lead text if any
            board_content = re.sub(r'<h2 class="page-title">.*?</h2>', '', board_content, flags=re.DOTALL)
            board_content = re.sub(r'<p class="lead-text">.*?</p>', '', board_content, flags=re.DOTALL)
            board_content = re.sub(r'^<main[^>]*>\s*', '', board_content)
        else:
            # Fallback
            container_start = content.find('<div id="container">')
            wrapper_end = content.rfind('<!-- } 콘텐츠 끝 -->')
            if wrapper_end == -1:
                wrapper_end = content.find('<hr>', container_start)
            board_content = content[container_start:wrapper_end]
            board_content = re.sub(r'<h2 id="container_title">.*?</h2>', '', board_content, flags=re.DOTALL)
            board_content = re.sub(r'^<div id="container">\s*', '', board_content)
            if board_content.endswith('</div>'):
                board_content = board_content[:-6].strip()

    # Determine main content HTML
    main_content_html = f'''
    <h2 class="page-title">{sub_title}</h2>
    <p class="lead-text">{lead_text}</p>
    '''

    if is_board:
        main_content_html += board_content
    else:
        if page_id in ['0103', '0301', '0302']:
            main_content_html += dummy_gallery
        elif page_id.startswith('02'):
            main_content_html += dummy_service
        else:
            # General generic content
            main_content_html += f'''
    <div class="info-card fade-up">
        <i class="fas fa-info-circle" style="color: var(--color-point); margin-bottom: 12px; font-size: 24px;"></i>
        <p>※ 고객 여러분의 소중한 생명과 재산을 보호하기 위해 최선을 다하는 <strong>(주)신영에스씨엠</strong>입니다.</p>
    </div>
    <h3 class="section-title fade-up">주요 안내</h3>
    <p class="fade-up">
        안전한 대한민국을 만들기 위해 저희 임직원 모두는 끊임없는 기술 개발과 역량 강화에 힘쓰고 있습니다.
        가장 정확한 진단, 가장 정직한 점검으로 보답하겠습니다.
    </p>
'''

    # Build sidebar
    sidebar_items_html = ""
    for k, v in sub_items.items():
        active_class = "active" if k == page_id else ""
        sidebar_items_html += f'<li class="{active_class}"><a href="./sub_{k}.html">{v}</a></li>\n                '

    # Build new layout WITHOUT .fade-up on top elements
    new_body = mega_header + f"""
<div id="wrapper">
    <div class="sub-hero">
        <div class="sub-hero-bg"></div>
        <div class="container sub-hero-content">
            <h1 class="sub-hero-title">{cat_title}</h1>
            <p class="sub-hero-desc">신뢰를 최우선으로 하는 안전진단 전문기관</p>
        </div>
    </div>

    <div class="breadcrumb">
        <div class="container">
            <span><i class="fas fa-home"></i> 홈</span>
            <span><i class="fas fa-chevron-right"></i> {cat_title}</span>
            <span class="current"><i class="fas fa-chevron-right"></i> {sub_title}</span>
        </div>
    </div>

    <div class="container sub-layout">
        <aside class="sub-sidebar">
            <h2 class="sidebar-title">{cat_title}</h2>
            <ul class="sidebar-menu">
                {sidebar_items_html}
            </ul>
        </aside>

        <main class="sub-content content-body">
            {main_content_html}
        </main>
    </div>
""" + new_footer

    # Replace head
    head_start = content.find('<head>')
    head_end = content.find('</head>')
    new_head = content[:head_start+6] + '\n' + new_head_template.format(title=page_title_tag) + '\n' + content[head_end:]
    
    body_start = new_head.find('<body')
    body_start = new_head.find('>', body_start) + 1
    
    final_content = new_head[:body_start] + '\n' + new_body + '\n</body>\n</html>'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)

print("Updated sub files with advanced content templates and removed above-the-fold fade-up classes.")
