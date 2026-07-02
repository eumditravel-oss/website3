import os

mappings = {
    'about_greeting.html': 'sub_0101.html',
    'about_history.html': 'sub_0102.html',
    'about_projects.html': 'sub_0103.html',
    'about_location.html': 'sub_0104.html',
    'business_01.html': 'sub_0201.html',
    'business_02.html': 'sub_0202.html',
    'business_03.html': 'sub_0203.html',
    'business_04.html': 'sub_0204.html',
    'business_05.html': 'sub_0205.html',
    'business_06.html': 'sub_0206.html',
    'business_07.html': 'sub_0207.html',
    'business_08.html': 'sub_0208.html',
    'business_09.html': 'sub_0209.html',
    'cert_01.html': 'sub_0301.html',
    'cert_02.html': 'sub_0302.html',
    'notice.html': 'sub_0401.html',
    'inquiry.html': 'sub_0402.html',
}

for old, new in mappings.items():
    if os.path.exists(old):
        content = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=./{new}">
    <title>Redirecting...</title>
</head>
<body>
    <script>window.location.href = "./{new}";</script>
    <p>페이지가 이동되었습니다. <a href="./{new}">여기를 클릭하세요.</a></p>
</body>
</html>'''
        with open(old, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Redirected {old} -> {new}')
