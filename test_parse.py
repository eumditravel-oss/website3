import re

with open('f:/website3/sub_0103.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract li elements
li_blocks = content.split('<li class="gall_li')
items = []
for li in li_blocks[1:]:
    img_match = re.search(r'<img src="([^"]+)"', li)
    img_src = img_match.group(1) if img_match else ""
    
    # Extract title. It's after class="bo_tit">, after the comment <!-- ... -->
    title_start = li.find('class="bo_tit">')
    if title_start != -1:
        # find the end of the comment
        comment_end = li.find('-->', title_start)
        if comment_end != -1:
            title_text = li[comment_end+3:li.find('</a>', comment_end)]
            title_clean = title_text.strip().replace('\n', '').replace('\r', '')
            # Clean multiple spaces
            title_clean = re.sub(r'\s+', ' ', title_clean)
            items.append((img_src, title_clean))

for i, item in enumerate(items):
    print(i, item)
