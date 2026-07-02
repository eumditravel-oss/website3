import urllib.request
req = urllib.request.Request('http://sinyoungscm.com/bbs/board.php?bo_table=0201', headers={'User-Agent': 'Mozilla/5.0'})
live_html = urllib.request.urlopen(req).read().decode('utf-8')
print('LIVE visual occurrences:', live_html.count('id="visual"'))
