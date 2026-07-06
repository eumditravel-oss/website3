import re

# 1. Update CSS
with open('f:/website3/css/redesign_main.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

portfolio_css = """
/* Portfolio Redesign */
.portfolio-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
    padding-bottom: 20px;
    border-bottom: 1px solid #e5e7eb;
}
.portfolio-filters {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
.filter-btn {
    padding: 8px 18px;
    border: 1px solid #e5e7eb;
    background: #fff;
    color: #4b5563;
    border-radius: 6px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.2s;
}
.filter-btn.active, .filter-btn:hover {
    background: #0033cc;
    color: #fff;
    border-color: #0033cc;
}
.portfolio-search {
    position: relative;
    width: 250px;
}
.portfolio-search input {
    width: 100%;
    padding: 10px 40px 10px 15px;
    border: 1px solid #e5e7eb;
    border-radius: 6px;
    font-size: 14px;
}
.portfolio-search button {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: #6b7280;
    cursor: pointer;
}

.portfolio-controls {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
.portfolio-total {
    font-size: 15px;
    color: #4b5563;
}
.portfolio-total strong {
    color: #0033cc;
    font-weight: 700;
}
.portfolio-actions {
    display: flex;
    gap: 10px;
    align-items: center;
}
.portfolio-actions select {
    padding: 8px 30px 8px 12px;
    border: 1px solid #e5e7eb;
    border-radius: 6px;
    color: #4b5563;
    outline: none;
    font-size: 14px;
    appearance: none;
    background: #fff url('data:image/svg+xml;utf8,<svg fill="%236b7280" height="20" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>') no-repeat right 5px center;
}
.view-toggles {
    display: flex;
    gap: 5px;
}
.view-btn {
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #e5e7eb;
    background: #fff;
    border-radius: 6px;
    color: #9ca3af;
    cursor: pointer;
    transition: all 0.2s;
}
.view-btn.active, .view-btn:hover {
    background: #eff6ff;
    color: #0033cc;
    border-color: #dbeafe;
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 25px;
    margin-bottom: 50px;
}
.portfolio-card {
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    border: 1px solid #f3f4f6;
    transition: transform 0.3s, box-shadow 0.3s;
}
.portfolio-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}
.card-img {
    position: relative;
    width: 100%;
    height: 200px;
    overflow: hidden;
}
.card-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s;
}
.portfolio-card:hover .card-img img {
    transform: scale(1.05);
}
.card-badge {
    position: absolute;
    bottom: 15px;
    left: 15px;
    background: #eff6ff;
    color: #0033cc;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    z-index: 2;
}
.card-body {
    padding: 20px;
}
.card-title {
    font-size: 16px;
    font-weight: 700;
    color: #111;
    margin-bottom: 15px;
    line-height: 1.4;
    height: 44px;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
}
.card-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #f3f4f6;
    padding-top: 15px;
}
.meta-item {
    font-size: 13px;
    color: #6b7280;
    display: flex;
    align-items: center;
    gap: 6px;
}

.portfolio-pagination {
    display: flex;
    justify-content: center;
    gap: 5px;
    margin-top: 40px;
}
.page-btn {
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #e5e7eb;
    background: #fff;
    color: #4b5563;
    border-radius: 6px;
    cursor: pointer;
    text-decoration: none;
    font-size: 14px;
    transition: all 0.2s;
}
.page-btn.active, .page-btn:hover {
    background: #0033cc;
    color: #fff;
    border-color: #0033cc;
}
@media(max-width: 1024px) {
    .portfolio-grid { grid-template-columns: repeat(2, 1fr); }
}
@media(max-width: 768px) {
    .portfolio-grid { grid-template-columns: 1fr; }
    .portfolio-header { flex-direction: column; align-items: flex-start; gap: 15px; }
    .portfolio-search { width: 100%; }
}
"""

if "/* Portfolio Redesign */" not in css_content:
    with open('f:/website3/css/redesign_main.css', 'a', encoding='utf-8') as f:
        f.write(portfolio_css)
    print("CSS updated.")

# 2. Parse HTML and extract items
with open('f:/website3/sub_0103.html', 'r', encoding='utf-8') as f:
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
            
            # Remove any trailing extra tags if caught by accident
            title_clean = title_clean.split('<span')[0].strip()
            
            items.append((img_src, title_clean))

# 3. Build new HTML structure
def get_category(title):
    if '내진' in title: return '내진성능평가'
    if '정기' in title: return '정기안전점검'
    if '정밀' in title: return '정밀안전진단'
    if '유지관리' in title: return '유지관리'
    return '정밀안전진단'

def get_location(title):
    t = title.replace(' ', '')
    if '송도' in t: return '인천광역시 연수구'
    if '가평' in t or '청심' in t: return '경기도 가평군'
    if '여의도' in t: return '서울특별시 영등포구'
    if '판교' in t: return '경기도 성남시'
    if '성남' in t: return '경기도 성남시'
    if '여주' in t or '경강선' in t: return '경기도 여주시'
    if '강남' in t: return '서울특별시 강남구'
    if '안양' in t: return '경기도 안양시'
    if '부여' in t: return '충청남도 부여군'
    return '서울특별시 강남구'

portfolio_html = """
        <div class="history-intro fade-up" style="text-align: left; margin-bottom: 40px; padding-bottom: 0; border: none;">
            <h2 style="font-size: 32px; margin-bottom: 15px;">주요실적</h2>
            <p style="font-size: 16px; color: #555; line-height: 1.6;">(주)한강엔지니어링은 축적된 현장 경험과 전문 기술력을 바탕으로<br>건축물 및 시설물의 안전진단, 정밀점검, 내진성능평가 등 다양한 프로젝트를 수행하고 있습니다.</p>
        </div>

        <div class="portfolio-header fade-up">
            <div class="portfolio-filters">
                <button class="filter-btn active">전체</button>
                <button class="filter-btn">정밀안전진단</button>
                <button class="filter-btn">정기안전점검</button>
                <button class="filter-btn">내진성능평가</button>
                <button class="filter-btn">유지관리</button>
                <button class="filter-btn">기타</button>
            </div>
            <div class="portfolio-search">
                <input type="text" placeholder="실적명, 건물명, 위치 검색">
                <button><i class="fas fa-search"></i></button>
            </div>
        </div>

        <div class="portfolio-controls fade-up">
            <div class="portfolio-total">
                Total <strong>{total_count}</strong>건
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

year = 2023
for i, (img, title) in enumerate(items):
    cat = get_category(title)
    loc = get_location(title)
    if i == 5: year = 2022
    if i == 12: year = 2021
    
    # Check if empty title (sometimes index parsing fails on gnuboard empty items)
    if not title: continue
    
    card_html = f"""
            <div class="portfolio-card">
                <div class="card-img">
                    <img src="{img}" alt="{title}">
                    <span class="card-badge">{cat}</span>
                </div>
                <div class="card-body">
                    <h3 class="card-title">{title}</h3>
                    <div class="card-meta">
                        <span class="meta-item"><i class="fas fa-map-marker-alt"></i> {loc}</span>
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
            <a href="#" class="page-btn">3</a>
            <a href="#" class="page-btn"><i class="fas fa-angle-right"></i></a>
            <a href="#" class="page-btn"><i class="fas fa-angle-double-right"></i></a>
        </div>
"""
portfolio_html = portfolio_html.format(total_count=len(items))

# 4. Replace in original HTML
# Find the start of the <h2 class="page-title">주요실적</h2>
# Find the end of the <div class="sub-contact-cta">
start_idx = html_content.find('<h2 class="page-title">주요실적</h2>')
if start_idx == -1: start_idx = html_content.find('<!-- 게시판 목록 시작 { -->')
end_idx = html_content.find('</main>')

if start_idx != -1 and end_idx != -1:
    new_html = html_content[:start_idx] + portfolio_html + "\n" + html_content[end_idx:]
    with open('f:/website3/sub_0103.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("HTML updated.")
else:
    print("Could not find replacement boundaries in HTML.")
