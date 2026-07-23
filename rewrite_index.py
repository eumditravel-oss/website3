import os

html_content = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>(주)한강엔지니어링 | 안전진단 전문기관</title>

<!-- FontAwesome for SVG Icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">

<!-- Core CSS -->
<link rel="stylesheet" href="./css/redesign_main.css">
</head>
<body>

<!-- Mobile Overlay -->
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
        
        <!-- Desktop Nav -->
        <ul class="gnb">
            <li><a href="./sub_0101.html">회사소개</a></li>
            <li><a href="./sub_0201.html">업무분야</a></li>
            <li><a href="./sub_0301.html">인증 및 장비현황</a></li>
            <li><a href="./sub_0401.html">고객센터</a></li>
            <li><a href="./sub_0402.html">무료견적문의</a></li>
        </ul>
        
        <!-- Mobile Menu Btn -->
        <button class="btn-mobile-menu" id="btn-menu-open" aria-label="메뉴 열기">
            <i class="fas fa-bars"></i>
        </button>
    </div>
</header>

<!-- Hero Section -->
<section class="hero">
    <div class="container">
        <div class="hero-content fade-up">
            <div class="hero-subtitle">정부공인 안전진단 전문기관</div>
            <h1 class="hero-title">신뢰를 최우선으로 하는<br>안전진단 전문기관</h1>
            <p class="hero-desc">(주)한강엔지니어링은 정밀한 진단과 최첨단 장비로<br>여러분의 안전을 가장 먼저 생각합니다.</p>
            <div class="hero-actions">
                <a href="./sub_0402.html" class="btn btn-primary"><i class="fas fa-file-invoice"></i> 무료 견적 문의</a>
                <a href="./sub_0201.html" class="btn btn-outline" style="color:#fff!important; border-color:rgba(255,255,255,0.5);"><i class="fas fa-building"></i> 업무분야 보기</a>
            </div>
        </div>
    </div>
</section>

<!-- Trust Metrics -->
<section class="container">
    <div class="trust-metrics fade-up">
        <div class="metric-card">
            <div class="metric-icon"><i class="fas fa-chart-line"></i></div>
            <div class="metric-number"><span class="count-up" data-target="172">0</span>건</div>
            <div class="metric-label">주요사업실적</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon"><i class="fas fa-shield-halved"></i></div>
            <div class="metric-number"><span class="count-up" data-target="81">0</span>건</div>
            <div class="metric-label">안전점검·정밀안전진단</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon"><i class="fas fa-train-subway"></i></div>
            <div class="metric-number"><span class="count-up" data-target="37">0</span>건</div>
            <div class="metric-label">철도·지하철 시설물 용역</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon"><i class="fas fa-building-shield"></i></div>
            <div class="metric-number"><span class="count-up" data-target="26">0</span>건</div>
            <div class="metric-label">인접건축물 현황조사</div>
        </div>
    </div>
</section>

<!-- Business Areas -->
<section class="section-padding">
    <div class="container">
        <div class="text-center fade-up">
            <h2 class="section-title">전문 업무 분야</h2>
            <p class="section-desc">최고의 기술력으로 정확하고 신뢰성 있는 안전진단 서비스를 제공합니다.</p>
        </div>
        <div class="business-grid fade-up">
            <a href="./sub_0201.html" class="business-card">
                <div class="b-icon"><i class="fas fa-search-location"></i></div>
                <h3 class="b-title">안전진단</h3>
                <p class="b-desc">노후되거나 구조적 결함이 예상되는 건축물에 대한 정밀 진단 수행.</p>
            </a>
            <a href="./sub_0202.html" class="business-card">
                <div class="b-icon"><i class="fas fa-clipboard-check"></i></div>
                <h3 class="b-title">안전점검</h3>
                <p class="b-desc">시설물의 물리적, 기능적 결함을 조기에 발견하기 위한 정기 점검.</p>
            </a>
            <a href="./sub_0203.html" class="business-card">
                <div class="b-icon"><i class="fas fa-building"></i></div>
                <h3 class="b-title">건축물관리점검</h3>
                <p class="b-desc">건축물 관리법에 따른 체계적인 유지 및 안전 관리 계획 수립.</p>
            </a>
            <a href="./sub_0204.html" class="business-card">
                <div class="b-icon"><i class="fas fa-helmet-safety"></i></div>
                <h3 class="b-title">건설공사 정기안전점검</h3>
                <p class="b-desc">건설 공사 중 발생할 수 있는 위험 요소를 사전에 차단하는 필수 점검.</p>
            </a>
            <a href="./sub_0205.html" class="business-card">
                <div class="b-icon"><i class="fas fa-house-crack"></i></div>
                <h3 class="b-title">내진성능평가</h3>
                <p class="b-desc">지진 발생 시 건축물의 저항 능력을 수치화하여 안정성 검증.</p>
            </a>
            <a href="./sub_0206.html" class="business-card">
                <div class="b-icon"><i class="fas fa-scale-balanced"></i></div>
                <h3 class="b-title">법원감정</h3>
                <p class="b-desc">건축 분쟁 시 공정한 법원 감정을 위한 객관적인 구조 기술 자료 제공.</p>
            </a>
            <a href="./sub_0207.html" class="business-card">
                <div class="b-icon"><i class="fas fa-binoculars"></i></div>
                <h3 class="b-title">인접건축물 사전조사</h3>
                <p class="b-desc">신축 공사 전, 주변 건축물의 균열 및 상태를 기록하여 분쟁을 예방.</p>
            </a>
            <a href="./sub_0208.html" class="business-card">
                <div class="b-icon"><i class="fas fa-pen-ruler"></i></div>
                <h3 class="b-title">구조설계/감리</h3>
                <p class="b-desc">안전하고 경제적인 구조 설계 및 시공 단계의 철저한 감리 수행.</p>
            </a>
            <a href="./sub_0209.html" class="business-card">
                <div class="b-icon"><i class="fas fa-trowel-bricks"></i></div>
                <h3 class="b-title">시설물보수/보강공사</h3>
                <p class="b-desc">진단 결과를 바탕으로 한 최적의 보수, 보강 공법 적용 및 시공.</p>
            </a>
        </div>
    </div>
</section>

<!-- Major Projects -->
<section class="section-padding section-bg-light">
    <div class="container">
        <div class="text-center fade-up">
            <h2 class="section-title">주요 실적</h2>
            <p class="section-desc">풍부한 경험을 바탕으로 다양한 시설물의 안전을 책임져왔습니다.</p>
        </div>
        <div class="projects-grid fade-up">
            <div class="project-card">
                <img src="./data/editor/2605/b89c2edcc7e30b61b41f589983060736_1778492665_1356.jpg" alt="실적 1">
                <div class="project-overlay"><h4 class="project-title">아파트 정밀안전진단</h4></div>
            </div>
            <div class="project-card">
                <img src="./data/editor/2605/b89c2edcc7e30b61b41f589983060736_1778492455_171.png" alt="실적 2">
                <div class="project-overlay"><h4 class="project-title">공공기관 내진성능평가</h4></div>
            </div>
            <div class="project-card">
                <img src="./data/editor/2603/6b5eba9fd637f461678ff05058031eb6_1773815081_4929.png" alt="실적 3">
                <div class="project-overlay"><h4 class="project-title">상업시설 보수보강 설계</h4></div>
            </div>
            <div class="project-card">
                <img src="./data/editor/2603/6b5eba9fd637f461678ff05058031eb6_1773814718_4109.png" alt="실적 4">
                <div class="project-overlay"><h4 class="project-title">인접건축물 사전조사</h4></div>
            </div>
        </div>
        <div class="text-center fade-up" style="margin-top: 40px;">
            <a href="./sub_0103.html" class="btn btn-outline">전체 실적 보기 <i class="fas fa-arrow-right"></i></a>
        </div>
    </div>
</section>

<!-- Contact Section -->
<section class="section-padding contact-section">
    <div class="container fade-up">
        <div class="contact-wrap">
            <div class="contact-map">
                <!-- 카카오맵 -->
                <div id="daumRoughmapContainer1749090060288" class="root_daum_roughmap root_daum_roughmap_landing" style="width:100%; height:100%;"></div>
                <script charset="UTF-8" class="daum_roughmap_loader_script" src="https://ssl.daumcdn.net/dmaps/map_js_init/roughmapLoader.js"></script>
                <script charset="UTF-8">
                    new daum.roughmap.Lander({
                        "timestamp" : "1749090060288",
                        "key" : "3zsch4b4suk"
                    }).render();
                </script>
            </div>
            <div class="contact-info">
                <h2>고객 만족을 위한 빠른 문의</h2>
                <p>정확한 현장 분석을 위해 유선 전화나 이메일로 상담해 주시면, 최단 시간 내에 전문가가 답변해 드립니다.</p>
                <div class="c-box">
                    <i class="fas fa-phone-volume"></i>
                    <h4>대표 전화</h4>
                    <a href="tel:02-6959-0729">02-6959-0729</a>
                </div>
                <div class="c-box">
                    <i class="fas fa-envelope-open-text"></i>
                    <h4>이메일 문의</h4>
                    <a href="mailto:hangang0730@daum.net" style="font-size:22px;">hangang0730@daum.net</a>
                </div>
                <a href="./sub_0402.html" class="btn btn-point"><i class="fas fa-file-signature"></i> 온라인 견적 양식 작성하기</a>
            </div>
        </div>
    </div>
</section>

<!-- Latest News Section -->
<section class="section-padding">
    <div class="container fade-up">
        <div class="news-grid">
            <div class="news-box">
                <div class="news-header">
                    <h3><i class="fas fa-bullhorn" style="color:var(--color-point); margin-right:8px;"></i> 공지사항</h3>
                    <a href="./sub_0401.html">더보기 <i class="fas fa-plus"></i></a>
                </div>
                <ul class="news-list">
                    <li><a href="./sub_0401.html"><span>안녕하세요. (주)한강엔지니어링입니다.</span> <span class="news-date">06-05</span></a></li>
                </ul>
            </div>
            <div class="news-box">
                <div class="news-header">
                    <h3><i class="fas fa-file-lines" style="color:var(--color-point); margin-right:8px;"></i> 무료견적문의</h3>
                    <a href="./sub_0402.html">더보기 <i class="fas fa-plus"></i></a>
                </div>
                <ul class="news-list">
                    <li><a href="./sub_0402.html"><span><i class="fas fa-lock" style="font-size:12px; margin-right:4px;"></i> 철거 안전진단 문의</span> <span class="news-date">오늘</span></a></li>
                    <li><a href="./sub_0402.html"><span><i class="fas fa-lock" style="font-size:12px; margin-right:4px;"></i> 건물 안전진단</span> <span class="news-date">06-30</span></a></li>
                    <li><a href="./sub_0402.html"><span><i class="fas fa-lock" style="font-size:12px; margin-right:4px;"></i> 옹벽 붕괴 전조 발생</span> <span class="news-date">06-28</span></a></li>
                    <li><a href="./sub_0402.html"><span><i class="fas fa-lock" style="font-size:12px; margin-right:4px;"></i> 일반안전점검 견적 요청</span> <span class="news-date">06-27</span></a></li>
                </ul>
            </div>
        </div>
    </div>
</section>

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

<!-- Scripts -->
<script src="./js/redesign_motion.js"></script>
</body>
</html>"""

with open('f:/website3/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
