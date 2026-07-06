import os

mega_header = """<!-- Mobile Overlay -->
<div class="m-overlay" id="m-overlay"></div>

<!-- Mobile Navigation -->
<nav class="mobile-nav" id="mobile-nav">
    <button class="btn-close-menu" id="btn-menu-close" aria-label="메뉴 닫기">
        <i class="fas fa-times"></i>
    </button>
    <ul class="m-gnb">
        <li>
            <a href="./sub_0101.html" class="subOpen">회사소개 <i class="fa fa-chevron-down"></i></a>
            <ul class="gnb_2dul_mo">
                <li><a href="./sub_0101.html">인사말</a></li>
                <li><a href="./sub_0102.html">연혁</a></li>
                <li><a href="./sub_0103.html">주요실적</a></li>
                <li><a href="./sub_0104.html">오시는길</a></li>
            </ul>
        </li>
        <li>
            <a href="./sub_0201.html" class="subOpen">업무분야 <i class="fa fa-chevron-down"></i></a>
            <ul class="gnb_2dul_mo">
                <li><a href="./sub_0201.html">안전진단</a></li>
                <li><a href="./sub_0202.html">안전점검</a></li>
                <li><a href="./sub_0203.html">건축물관리점검</a></li>
                <li><a href="./sub_0204.html">건설공사 정기안전점검</a></li>
                <li><a href="./sub_0205.html">내진성능평가</a></li>
                <li><a href="./sub_0206.html">법원감정</a></li>
                <li><a href="./sub_0207.html">인접건축물 사전조사</a></li>
                <li><a href="./sub_0208.html">구조설계/감리</a></li>
                <li><a href="./sub_0209.html">시설물보수/보강공사</a></li>
            </ul>
        </li>
        <li>
            <a href="./sub_0301.html" class="subOpen">인증 및 장비현황 <i class="fa fa-chevron-down"></i></a>
            <ul class="gnb_2dul_mo">
                <li><a href="./sub_0301.html">인증현황</a></li>
                <li><a href="./sub_0302.html">장비보유현황</a></li>
            </ul>
        </li>
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
        <nav class="gnb-wrap">
            <ul class="gnb">
                <li data-target="menu-01"><a href="./sub_0101.html">회사소개</a></li>
                <li data-target="menu-02"><a href="./sub_0201.html">업무분야</a></li>
                <li data-target="menu-03"><a href="./sub_0301.html">인증 및 장비현황</a></li>
                <li data-target="menu-04"><a href="./sub_0401.html">고객센터</a></li>
                <li data-target="menu-05"><a href="./sub_0402.html">무료견적문의</a></li>
            </ul>
        </nav>
        <button class="btn-mobile-menu" id="btn-menu-open" aria-label="메뉴 열기">
            <i class="fas fa-bars"></i>
        </button>
    </div>

    <!-- Megamenu Panel -->
    <div class="mega-menu-panel" aria-hidden="true">
        <div class="container mega-container">
            <div class="mega-cols">
                <div class="mega-col" id="menu-01">
                    <h3 class="mega-title"><a href="./sub_0101.html">회사소개</a></h3>
                    <ul class="mega-list">
                        <li><a href="./sub_0101.html">인사말</a></li>
                        <li><a href="./sub_0102.html">연혁</a></li>
                        <li><a href="./sub_0103.html">주요실적</a></li>
                        <li><a href="./sub_0104.html">오시는길</a></li>
                    </ul>
                </div>
                <div class="mega-col" id="menu-02">
                    <h3 class="mega-title"><a href="./sub_0201.html">업무분야</a></h3>
                    <ul class="mega-list">
                        <li><a href="./sub_0201.html">안전진단</a></li>
                        <li><a href="./sub_0202.html">안전점검</a></li>
                        <li><a href="./sub_0203.html">건축물관리점검</a></li>
                        <li><a href="./sub_0204.html">건설공사 정기안전점검</a></li>
                        <li><a href="./sub_0205.html">내진성능평가</a></li>
                        <li><a href="./sub_0206.html">법원감정</a></li>
                        <li><a href="./sub_0207.html">인접건축물 사전조사</a></li>
                        <li><a href="./sub_0208.html">구조설계/감리</a></li>
                        <li><a href="./sub_0209.html">시설물보수/보강공사</a></li>
                    </ul>
                </div>
                <div class="mega-col" id="menu-03">
                    <h3 class="mega-title"><a href="./sub_0301.html">인증 및 장비현황</a></h3>
                    <ul class="mega-list">
                        <li><a href="./sub_0301.html">인증현황</a></li>
                        <li><a href="./sub_0302.html">장비보유현황</a></li>
                    </ul>
                </div>
                <div class="mega-col" id="menu-04">
                    <h3 class="mega-title"><a href="./sub_0401.html">고객센터</a></h3>
                    <ul class="mega-list">
                        <li><a href="./sub_0401.html">공지사항</a></li>
                    </ul>
                </div>
                <div class="mega-col" id="menu-05">
                    <h3 class="mega-title"><a href="./sub_0402.html">무료견적문의</a></h3>
                    <ul class="mega-list">
                        <li><a href="./sub_0402.html">견적문의</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="mega-cta">
                <p>전문가의 빠르고 정확한 진단</p>
                <a href="./sub_0402.html" class="btn btn-point"><i class="fas fa-file-invoice"></i> 무료 견적 문의</a>
                <div class="mega-phone" style="margin-top:15px;"><i class="fas fa-phone"></i> 02-484-4700</div>
            </div>
        </div>
    </div>
</header>
<div class="mega-overlay"></div>"""

with open('f:/website3/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace from <!-- Mobile Overlay --> to </header>
start_idx = content.find('<!-- Mobile Overlay -->')
end_idx = content.find('</header>') + 9

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + mega_header + content[end_idx:]
    with open('f:/website3/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html")
