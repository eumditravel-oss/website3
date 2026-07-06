import re

filepath = 'f:/website3/sub_0402.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the links from body if they exist
content = re.sub(
    r'<link rel="stylesheet" href="\./css/redesign\.css">\s*<script src="\./js/redesign_motion\.js"></script>\s*',
    '', 
    content
)

# 2. Add them to head right before </head>
if './css/redesign.css' not in content:
    content = content.replace(
        '</head>', 
        '<link rel="stylesheet" href="./css/redesign.css">\n<script src="./js/redesign_motion.js"></script>\n</head>'
    )

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
