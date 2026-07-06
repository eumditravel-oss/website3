import os

subpages = {
    "about_greeting.html": ("회사소개", "인사말", "0101", "0101_1.jpg"),
    "about_history.html": ("회사소개", "연혁", "0102", "0102_1.jpg"),
    "about_projects.html": ("회사소개", "주요실적", "0103", "0103_1.jpg"),
    "about_location.html": ("회사소개", "오시는길", "0104", "0104_1.jpg"),
    "business_01.html": ("업무분야", "안전진단", "0201", "0201_1.jpg"),
    "business_02.html": ("업무분야", "안전점검", "0202", "0202_1.jpg"),
    "business_03.html": ("업무분야", "건축물관리점검", "0203", "0203_1.jpg"),
    "business_04.html": ("업무분야", "건설공사 정기안전점검", "0204", "0204_1.jpg"),
    "business_05.html": ("업무분야", "내진성능평가", "0205", "0205_1.jpg"),
    "business_06.html": ("업무분야", "법원감정", "0206", "0206_1.jpg"),
    "business_07.html": ("업무분야", "인접건축물 사전조사", "0207", "0207_1.jpg"),
    "business_08.html": ("업무분야", "구조설계/감리", "0208", "0208_1.jpg"),
    "business_09.html": ("업무분야", "시설물보수/보강공사", "0209", "0209_1.jpg"),
    "cert_01.html": ("인증 및 장비현황", "인증현황", "0301", "0301_1.jpg"),
    "cert_02.html": ("인증 및 장비현황", "장비보유현황", "0302", "0302_1.jpg"),
    "notice.html": ("고객센터", "공지사항", "0401", "0401_1.jpg"),
    "inquiry.html": ("무료견적문의", "견적문의", "0402", "0402_1.jpg")
}

template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - (주)한강엔지니어링</title>
    <link rel="stylesheet" href="./css/style.css">
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

    <!-- 공통 상단 (Subtop) -->
    <div class="subtop">
        <div class="txt">
            <h2>{category}</h2>
            <h3>{title}</h3>
        </div>
    </div>

    <!-- 본문 레이아웃 -->
    <div class="container_wrap">
        <!-- LNB (좌측 그룹메뉴) -->
        <div id="aside" class="mo_hide">
            <section id="groupmenu" style="width:195px;">
                <table width="100%" cellpadding="0" cellspacing="0" border="0" align="center">
                    <tr height="70">
                        <td class="nanum-gb" valign="top" colspan='3' style="color:#525252; font-size:25px; line-height:80px; border-bottom:1px solid #d6d6d6;border-top:10px solid #0033cc;text-align:center;">
                            <b>{category}</b>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div id="nav1">
                                <ul>
                                    <li class="on"><a href="#" class="nanum-g" style="font-size:16px; line-height:45px; display:block;">{title}</a></li>
                                </ul>
                            </div>
                        </td>
                    </tr>
                </table>
            </section>
        </div>

        <!-- 본문 Container -->
        <div id="container">
            <h2 id="container_title">{title}</h2>
            <div class="sub_wrap">
                <div class="sub_{code}">
                    <div class="img">
                        <img src="http://sinyoungscm.com/img/{img}" alt="{title}" onerror="this.src='http://sinyoungscm.com/img/main01.jpg'">
                    </div>
                    <div class="txt">
                        <h1>신뢰를 최우선으로 하는 안전진단 전문기관</h1>
                        <h2>(주)한강엔지니어링 - {title}</h2>
                        <p>
                        저희는 최신 기술과 엄격한 안전진단 기준을 바탕으로,<br class="mo_hide"> 다양한 분야의 안전진단 서비스를 제공합니다.
                        <br><br>
                        고도화된 진단 장비와 정밀한 데이터 분석을 통해 위험 요소를 신속하게 파악하고<br class="mo_hide">
                        안전 대책을 마련함으로써, 재해 위험을 최소화하고 있습니다.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>

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
    <!-- MR Script Ver 2.0 (실시간 문의 플로팅 위젯) -->
    <script async="true" src="//log1.toup.net/mirae_log_chat_common.js?adkey=plvbh" charset="UTF-8"></script>
</body>
</html>
"""

for filename, (category, title, code, img) in subpages.items():
    with open(f"f:/webpage2/{filename}", "w", encoding="utf-8") as f:
        f.write(template.format(category=category, title=title, code=code, img=img))

print("Successfully generated all 17 subpages with the approved DOM structure.")
