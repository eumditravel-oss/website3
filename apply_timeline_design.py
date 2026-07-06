import re

# 1. Update CSS
with open('f:/website3/css/redesign_main.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

new_timeline_css = """/* Premium Vertical Timeline */
.timeline-section {
    position: relative;
    max-width: 900px;
    margin: 60px auto;
    padding: 20px;
}
.timeline-section::before {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 2px;
    background: #e5e7eb;
    transform: translateX(-50%);
}
.timeline-item {
    position: relative;
    margin-bottom: 30px;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.timeline-item:nth-child(odd) {
    flex-direction: row-reverse;
}
/* Connector line */
.timeline-item::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 5%;
    height: 2px;
    background: #e5e7eb;
    z-index: 0;
}
.timeline-item:nth-child(even)::after {
    left: 45%;
}
.timeline-item:nth-child(odd)::after {
    right: 45%;
}
.timeline-marker {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #0044cc;
    border: 4px solid #fff;
    box-shadow: 0 0 0 4px #e5e7eb;
    z-index: 2;
    transition: all 0.3s ease;
}
.timeline-item:hover .timeline-marker {
    background: #0033cc;
    box-shadow: 0 0 0 6px #dbeafe;
}
.timeline-content {
    width: 45%;
    background: #fff;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
    border: 1px solid #f1f5f9;
    display: flex;
    align-items: center;
    gap: 25px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    z-index: 1;
}
.timeline-item:hover .timeline-content {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0, 51, 204, 0.08);
}
.timeline-icon {
    flex: 0 0 60px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #eff6ff;
    color: #0044cc;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
}
.timeline-text {
    flex: 1;
}
.timeline-date {
    font-size: 24px;
    color: #0044cc;
    font-weight: 800;
    margin-bottom: 8px;
    letter-spacing: 0;
}
.timeline-desc {
    font-size: 16px;
    color: #111;
    font-weight: 700;
    line-height: 1.4;
}
.timeline-desc span {
    display: block;
    margin-top: 6px;
    color: #666;
    font-size: 13px;
    font-weight: 400;
}
@media(max-width: 768px) {
    .timeline-section::before { left: 30px; }
    .timeline-item { flex-direction: column; align-items: flex-start; margin-bottom: 40px; }
    .timeline-item:nth-child(odd) { flex-direction: column; }
    .timeline-item::after { display: none; }
    .timeline-marker { left: 30px; top: 50%; transform: translate(-50%, -50%); }
    .timeline-content { padding: 20px; margin-left: 70px; width: calc(100% - 70px); }
    .timeline-item:hover .timeline-content { transform: translateX(5px); }
}"""

# Replace the block
start_idx = css_content.find('/* Premium Vertical Timeline */')
end_idx = css_content.find('/* History Intro */')
if start_idx != -1 and end_idx != -1:
    new_css = css_content[:start_idx] + new_timeline_css + '\n\n' + css_content[end_idx:]
    with open('f:/website3/css/redesign_main.css', 'w', encoding='utf-8') as f:
        f.write(new_css)
    print("CSS updated.")

# 2. Update HTML
with open('f:/website3/sub_0102.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

new_timeline_html = """        <section class="timeline-section">
            <div class="timeline-item fade-up">
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <div class="timeline-icon"><i class="fas fa-building"></i></div>
                    <div class="timeline-text">
                        <div class="timeline-date">2023. 01.</div>
                        <div class="timeline-desc">본점 이전<span>(경기도 광명시 소하로 190, 광명G타워 B동 1314호)</span></div>
                    </div>
                </div>
            </div>
            
            <div class="timeline-item fade-up" style="transition-delay: 0.1s;">
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <div class="timeline-icon"><i class="fas fa-building"></i></div>
                    <div class="timeline-text">
                        <div class="timeline-date">2020. 02.</div>
                        <div class="timeline-desc">본점 이전<span>(경기도 김포시 김포한강4로 176, 현대프라자 201호)</span></div>
                    </div>
                </div>
            </div>
            
            <div class="timeline-item fade-up" style="transition-delay: 0.2s;">
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <div class="timeline-icon"><i class="fas fa-file-contract"></i></div>
                    <div class="timeline-text">
                        <div class="timeline-date">2017. 02.</div>
                        <div class="timeline-desc">본점 이전<span>(중랑구 동일로 241-1, 3층)</span></div>
                    </div>
                </div>
            </div>
            
            <div class="timeline-item fade-up" style="transition-delay: 0.3s;">
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <div class="timeline-icon"><i class="fas fa-award"></i></div>
                    <div class="timeline-text">
                        <div class="timeline-date">2013. 06.</div>
                        <div class="timeline-desc">안전진단전문기관 면허 취득</div>
                    </div>
                </div>
            </div>
            
            <div class="timeline-item fade-up" style="transition-delay: 0.4s;">
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <div class="timeline-icon"><i class="fas fa-building"></i></div>
                    <div class="timeline-text">
                        <div class="timeline-date">2010. 09.</div>
                        <div class="timeline-desc">본점 이전<span>(서울시 성동구 연무장5가길 7 현대테라스타워 W동 1005호)</span></div>
                    </div>
                </div>
            </div>
            
            <div class="timeline-item fade-up" style="transition-delay: 0.5s;">
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <div class="timeline-icon"><i class="fas fa-handshake"></i></div>
                    <div class="timeline-text">
                        <div class="timeline-date">2010. 08.</div>
                        <div class="timeline-desc">주식회사 한강엔지니어링 설립</div>
                    </div>
                </div>
            </div>
        </section>"""

start_idx = html_content.find('<section class="timeline-section">')
end_idx = html_content.find('</section>') + 10
if start_idx != -1 and end_idx != -1:
    new_html = html_content[:start_idx] + new_timeline_html + html_content[end_idx:]
    with open('f:/website3/sub_0102.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("HTML updated.")
