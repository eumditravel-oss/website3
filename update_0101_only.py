import re

with open('f:/website3/sub_0101.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the inline <style> block specific to the old greeting layout
content = re.sub(r'<style>.*?Greeting Page Custom Layout.*?</style>', '', content, flags=re.DOTALL)

# Find the start of the wrapper
wrapper_start = content.find('<div id="wrapper">')
if wrapper_start == -1:
    print("Error: Could not find <div id=\"wrapper\">")
    exit()

# Find the end of wrapper (the </div> right before <!-- Footer -->)
# Actually, let's just find "<!-- Bottom CTA -->"
cta_start = content.find('<!-- Bottom CTA -->')
if cta_start == -1:
    print("Error: Could not find Bottom CTA")
    exit()

wrapper_content = content[wrapper_start:cta_start]

new_wrapper_content = """<div id="wrapper">
    <div class="subpage-new-layout">
        <aside class="sidebar-new">
            <div class="sidebar-header">
                <h2>회사소개</h2>
                <span class="en">COMPANY</span>
            </div>
            <ul class="sidebar-menu-new">
                <li class="active"><a href="./sub_0101.html"><i class="fas fa-user-tie"></i> <span>인사말</span></a></li>
                <li class=""><a href="./sub_0102.html"><i class="fas fa-calendar-alt"></i> <span>연혁</span></a></li>
                <li class=""><a href="./sub_0103.html"><i class="fas fa-list-alt"></i> <span>주요실적</span></a></li>
                <li class=""><a href="./sub_0104.html"><i class="fas fa-map-marked-alt"></i> <span>오시는길</span></a></li>
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
                <i class="fas fa-home"></i> &gt; <span>회사소개</span> &gt; <span class="current">인사말</span>
            </div>
            
            <main class="content-main">
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
            </main>
        </div>
    </div>\n\n    """

final_content = content[:wrapper_start] + new_wrapper_content + content[cta_start:]

with open('f:/website3/sub_0101.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Updated sub_0101.html successfully.")
