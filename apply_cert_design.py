import re

def process_file(filepath, title_name, desc, default_badge, meta_text, is_contain=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    li_blocks = html_content.split('<li class="gall_li')
    items = []
    for li in li_blocks[1:]:
        img_match = re.search(r'<img src="([^"]+)"', li)
        img_src = img_match.group(1) if img_match else ""
        
        title_start = li.find('class="bo_tit">')
        if title_start != -1:
            comment_end = li.find('-->', title_start)
            if comment_end != -1:
                title_text = li[comment_end+3:li.find('</a>', comment_end)]
                title_clean = title_text.strip().replace('\\n', '').replace('\\r', '')
                title_clean = re.sub(r'\\s+', ' ', title_clean)
                title_clean = title_clean.split('<span')[0].strip()
                items.append((img_src, title_clean))

    portfolio_html = f"""
        <div class="history-intro fade-up" style="text-align: left; margin-bottom: 40px; padding-bottom: 0; border: none;">
            <h2 style="font-size: 32px; margin-bottom: 15px;">{title_name}</h2>
            <p style="font-size: 16px; color: #555; line-height: 1.6;">{desc}</p>
        </div>

        <div class="portfolio-header fade-up">
            <div class="portfolio-filters">
                <button class="filter-btn active">전체</button>
            </div>
            <div class="portfolio-search">
                <input type="text" placeholder="검색어 입력">
                <button><i class="fas fa-search"></i></button>
            </div>
        </div>

        <div class="portfolio-controls fade-up">
            <div class="portfolio-total">
                Total <strong>{len(items)}</strong>건
            </div>
            <div class="portfolio-actions">
                <select>
                    <option>최신순</option>
                    <option>이름순</option>
                </select>
                <div class="view-toggles">
                    <button class="view-btn active"><i class="fas fa-th-large"></i></button>
                    <button class="view-btn"><i class="fas fa-bars"></i></button>
                </div>
            </div>
        </div>

        <div class="portfolio-grid fade-up">
"""

    img_style = 'style="object-fit: contain; background: #f8fafc; padding: 10px;"' if is_contain else ''
    year = 2024
    for i, (img, title) in enumerate(items):
        if not title: continue
        
        card_html = f"""
            <div class="portfolio-card">
                <div class="card-img">
                    <img src="{img}" alt="{title}" {img_style}>
                    <span class="card-badge">{default_badge}</span>
                </div>
                <div class="card-body">
                    <h3 class="card-title">{title}</h3>
                    <div class="card-meta">
                        <span class="meta-item"><i class="fas fa-check-circle"></i> {meta_text}</span>
                        <span class="meta-item"><i class="far fa-calendar-alt"></i> {year}</span>
                    </div>
                </div>
            </div>
"""
        portfolio_html += card_html

    portfolio_html += """
        </div>

        <div class="portfolio-pagination fade-up">
            <a href="#" class="page-btn"><i class="fas fa-angle-double-left"></i></a>
            <a href="#" class="page-btn"><i class="fas fa-angle-left"></i></a>
            <a href="#" class="page-btn active">1</a>
            <a href="#" class="page-btn">2</a>
            <a href="#" class="page-btn"><i class="fas fa-angle-right"></i></a>
            <a href="#" class="page-btn"><i class="fas fa-angle-double-right"></i></a>
        </div>
"""

    start_idx = html_content.find(f'<h2 class="page-title">{title_name}</h2>')
    if start_idx == -1: start_idx = html_content.find('<!-- 게시판 목록 시작 { -->')
    end_idx = html_content.find('</main>')

    if start_idx != -1 and end_idx != -1:
        new_html = html_content[:start_idx] + portfolio_html + "\\n" + html_content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated {filepath}")
    else:
        print(f"Failed {filepath}")

# Update sub_0301.html (인증현황)
process_file('f:/website3/sub_0301.html', '인증현황', '(주)한강엔지니어링의 공신력 있는 각종 인증 및 면허 현황입니다.', '공식인증', '국가공인', is_contain=True)

# Update sub_0302.html (장비보유현황)
process_file('f:/website3/sub_0302.html', '장비보유현황', '정밀하고 안전한 진단을 위해 (주)한강엔지니어링이 보유하고 있는 최신 첨단 장비 현황입니다.', '첨단장비', '정밀측정', is_contain=False)
