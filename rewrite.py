import bs4
import glob
import re
import traceback

def icon_for(title):
    title = title.strip()
    if '관련법' in title or '근거' in title: return 'fas fa-gavel'
    if '대상' in title: return 'fas fa-bullseye'
    if '시기' in title or '주기' in title: return 'fas fa-calendar-alt'
    if '과업' in title or '내용' in title or '절차' in title or '업무' in title: return 'fas fa-tasks'
    if '대가' in title or '비용' in title: return 'fas fa-won-sign'
    if '목적' in title: return 'fas fa-flag'
    return 'fas fa-check-circle'

def process_file(filepath):
    print(f'Processing {filepath}...')
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        soup = bs4.BeautifulSoup(html, 'html.parser')
        sub_wrap = soup.find('div', class_='sub_wrap')
        if not sub_wrap:
            print(f'No .sub_wrap in {filepath}')
            return
            
        conts = sub_wrap.find_all('div', class_='cont')
        
        new_html = '<div class="sub_wrap">\n'
        
        for cont in conts:
            title_tag = cont.find('h1')
            if not title_tag:
                title_tag = cont.find('h2')
            if not title_tag:
                continue
            section_title = title_tag.get_text(strip=True)
            
            new_html += f'''
    <section class="service-section">
        <div class="service-header fade-up">
            <h3>{section_title}</h3>
        </div>
        <div class="service-grid">
'''
            
            table = cont.find('table', recursive=False)
            if table:
                rows = table.find_all('tr', recursive=False)
                if not rows: # maybe inside tbody
                    tbody = table.find('tbody', recursive=False)
                    if tbody:
                        rows = tbody.find_all('tr', recursive=False)
                
                for row in rows:
                    th = row.find('th', recursive=False)
                    td = row.find('td', recursive=False)
                    if th and td:
                        card_title = th.get_text(strip=True)
                        card_icon = icon_for(card_title)
                        card_content = td.decode_contents()
                        
                        # Fix tables inside card_content (remove width styles to fit card)
                        card_content = re.sub(r'style="[^"]*"', '', card_content)
                        card_content = card_content.replace('class="mini_table"', '')
                        
                        is_full = 'full-width' if '<table' in card_content else ''
                        
                        new_html += f'''
            <div class="service-card {is_full} fade-up">
                <div class="service-card-header">
                    <div class="service-card-icon"><i class="{card_icon}"></i></div>
                    <h4>{card_title}</h4>
                </div>
                <div class="service-card-body">
                    {card_content}
                </div>
            </div>
'''
            new_html += '''
        </div>
    </section>
'''
        new_html += '</div>'
        
        pattern = re.compile(r'<div class="sub_wrap">.*?(?=</main>)', re.DOTALL)
        modified = pattern.sub(new_html + '\n', html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified)
        print(f'Saved {filepath}')
    except Exception as e:
        print(f'Failed on {filepath}: {e}')
        traceback.print_exc()

files = glob.glob('sub_020*.html')
for f in files:
    process_file(f)
