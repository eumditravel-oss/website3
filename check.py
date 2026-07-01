import os
with open('f:/webpage2/business_01.html', 'r', encoding='utf-8') as f:
    text = f.read()
    print("wrapper count:", text.count('id="wrapper"'))
    print("visual count:", text.count('id="visual"'))
    
with open('f:/webpage2/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    print("index wrapper count:", text.count('id="wrapper"'))
    print("index visual count:", text.count('id="visual"'))
